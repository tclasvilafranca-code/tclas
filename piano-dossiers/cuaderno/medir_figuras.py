# -*- coding: utf-8 -*-
"""Mide que figura corta lleva IMPRESA una partitura, sobre el PDF real.

   ESTO ES LO QUE NADIE MIDIO NUNCA. Las transcripciones (`TRANSCRIPCION_*.md`)
   anotan edicion, tonalidad, compas, tempo y paginas de cada partitura, pero
   NO la figura mas corta. Por eso pudo pasar que el dosier de un alumno no
   escribiera una figura que su partitura lleva impresa de principio a fin, y
   que no lo detectara ningun auditor: el de vocabulario solo comprueba que no
   se hable de lo que no se dibuja, no que se dibuje lo que la partitura trae.


   Una semicorchea se dibuja con dos barras paralelas (o con una barra y un
   rabito corto, que es la figura larga-corta). En una columna de pixeles eso
   deja DOS tramos oscuros del mismo grosor separados por un hueco claro, y el
   par se repite a lo largo de varias columnas seguidas.

   Lo que hay que descartar para que no mienta:
     - las lineas del pentagrama y las adicionales: son finas (por eso el
       grosor minimo va en fraccion de espacio, no en pixeles);
     - las cabezas de nota: en una columna dejan un tramo de casi un espacio
       entero, mas grueso que cualquier barra;
     - los diagramas de guitarra que algunas ediciones imprimen encima del
       pentagrama: sus lineas tambien van paralelas y a la distancia justa,
       pero son de un pixel;
     - la clave, la armadura y el compas del principio de cada sistema, que
       son trazos gruesos y curvos (la clave de sol sola daba 26 falsos
       positivos en "When the Saints").
"""
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))
import score_reader as sr

DPI = 200

GROSOR_MIN = 0.20      # de una barra, en espacios de pentagrama
GROSOR_MAX = 0.75
SEPARA_MIN = 0.50      # entre los centros de las dos barras
SEPARA_MAX = 1.25
IGUALDAD = 0.55        # las dos barras tienen grosor parecido
SALTO_CLAVE = 6.5      # espacios que se ignoran al principio de cada sistema
LARGA = 1.10           # ancho a partir del cual es una barra doble entera
CORTA = 0.45           # y a partir del cual es un rabito de figura larga-corta

# Una BARRA es recta: a lo ancho del tramo, el grosor y la separacion entre las
# dos apenas cambian. Dos cabezas de nota una tercera aparte tambien dejan dos
# tramos oscuros a la distancia justa, pero son ovaladas y su grosor sube y baja
# en cada columna. Sin esta comprobacion, un acorde de dos notas con puntillo se
# contaba como semicorchea (pasaba en el Jailhouse).
VARIA_MAX = 0.13       # desviacion tipica maxima, en espacios de pentagrama


# El umbral de tinta NO puede ser fijo: hay ediciones que imprimen el
# pentagrama en gris claro (Peaches sale con las lineas por encima de 150) y
# con el umbral de siempre no se encontraba ni un pentagrama, asi que la
# partitura salia "sin semicorcheas" cuando las tiene a partir del c. 13.
# Se prueba de menos a mas y se coge el PRIMERO que encuentra pautas: subir
# de mas engorda los trazos y acaba pegando las dos barras de una semicorchea.
UMBRALES = (125, 150, 175, 200, 220)


def cargar(path):
    """(mapa de tinta, umbral) con el umbral mas bajo que encuentra pentagramas."""
    import numpy as _np
    gris = _np.array(Image.open(path).convert('L'))
    for u in UMBRALES:
        a = gris < u
        if sr.pentagramas(a):
            return a, u
    return gris < UMBRALES[0], UMBRALES[0]


def _tramos(col):
    out, ini = [], None
    for i, v in enumerate(col):
        if v and ini is None:
            ini = i
        elif not v and ini is not None:
            out.append((ini, i - 1)); ini = None
    if ini is not None:
        out.append((ini, len(col) - 1))
    return out


def _borde_izquierdo(a, y):
    fila = a[int(y) - 1:int(y) + 2].any(axis=0)
    xs = np.where(fila)[0]
    return int(xs[0]) if len(xs) else 0


def en_pagina(a):
    """[(x, y, sp, ancho)] de cada par de barras de la pagina."""
    h, w = a.shape
    fuera = []
    for top, bot in sr.pentagramas(a):
        sp = (bot - top) / 4.0
        if sp < 6:
            continue
        y0, y1 = int(max(0, top - 4 * sp)), int(min(h, bot + 4 * sp))
        banda = a[y0:y1]
        gmin, gmax = GROSOR_MIN * sp, GROSOR_MAX * sp
        dmin, dmax = SEPARA_MIN * sp, SEPARA_MAX * sp
        x_ini = _borde_izquierdo(a, top) + int(SALTO_CLAVE * sp)
        buenas = np.zeros(w, dtype=bool)
        alturas = np.zeros(w)
        huecos = np.zeros(w)
        gruesos = np.zeros(w)
        for x in range(x_ini, w):
            tr = [(i, f) for i, f in _tramos(banda[:, x])
                  if gmin <= (f - i + 1) <= gmax]
            for k in range(len(tr) - 1):
                g1 = tr[k][1] - tr[k][0] + 1
                g2 = tr[k + 1][1] - tr[k + 1][0] + 1
                if min(g1, g2) < IGUALDAD * max(g1, g2):
                    continue
                c1 = (tr[k][0] + tr[k][1]) / 2.0
                c2 = (tr[k + 1][0] + tr[k + 1][1]) / 2.0
                if dmin <= c2 - c1 <= dmax:
                    buenas[x] = True
                    alturas[x] = c1 + y0
                    huecos[x] = c2 - c1
                    gruesos[x] = (g1 + g2) / 2.0
                    break
        x = x_ini
        while x < w:
            if buenas[x]:
                xa = x
                while x < w and buenas[x]:
                    x += 1
                if (huecos[xa:x].std() <= VARIA_MAX * sp
                        and gruesos[xa:x].std() <= VARIA_MAX * sp):
                    fuera.append((xa, int(alturas[xa]), sp, x - xa))
            else:
                x += 1
    return fuera


def paginas(pdf, dpi=DPI):
    """Rasteriza (PDF o imagen) y devuelve las rutas de las paginas."""
    tmp = tempfile.mkdtemp()
    with open(pdf, 'rb') as fh:
        cabecera = fh.read(5)
    if cabecera[:4] == b'%PDF':
        # PNG y no JPEG: el JPEG difumina las lineas finas del pentagrama y
        # deja de encontrarlas la deteccion de pautas.
        subprocess.run(['pdftoppm', '-png', '-r', str(dpi), pdf,
                        os.path.join(tmp, 'pg')], check=True,
                       stderr=subprocess.DEVNULL)
    else:
        # Alguna partitura de Drive llega como JPEG (el Adagio de Albinoni).
        im = Image.open(pdf).convert('L')
        # subirla a la escala de un render a `dpi` para que sp sea comparable
        f = max(1.0, (dpi / 72.0) * 595.0 / im.size[0])
        im.resize((int(im.size[0] * f), int(im.size[1] * f))).save(
            os.path.join(tmp, 'pg-1.png'))
    return tmp, sorted(os.path.join(tmp, f) for f in os.listdir(tmp)
                       if f.startswith('pg'))


def contar(pdf, dpi=DPI):
    """(barras dobles enteras, rabitos) de toda la partitura."""
    tmp, pags = paginas(pdf, dpi)
    largas = cortas = 0
    for f in pags:
        a, _u = cargar(f)
        for _x, _y, sp, ancho in en_pagina(a):
            if ancho >= LARGA * sp:
                largas += 1
            elif ancho >= CORTA * sp:
                cortas += 1
        os.remove(f)
    os.rmdir(tmp)
    return largas, cortas


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print('%-52s %s' % (os.path.basename(p)[:52], contar(p)))
