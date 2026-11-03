# -*- coding: utf-8 -*-
"""Mide que figura corta lleva IMPRESA una partitura, sobre el PDF real.

   ESTO ES LO QUE NADIE MIDIO NUNCA. Las transcripciones (`TRANSCRIPCION_*.md`)
   anotan edicion, tonalidad, compas, tempo y paginas de cada partitura, pero
   NO la figura mas corta. Por eso pudo pasar que el dosier de un alumno no
   escribiera una figura que su partitura lleva impresa, y que no lo detectara
   ningun auditor: el de vocabulario solo comprueba que no se hable de lo que no
   se dibuja, no que se dibuje lo que la partitura trae.

   Una semicorchea se dibuja con DOS barras paralelas (o con una barra y un
   rabito corto, que es la figura larga-corta). En una columna de pixeles eso
   deja dos tramos oscuros del mismo grosor separados por un hueco claro, y el
   par se mantiene RECTO a lo largo de varias columnas seguidas.

   ## Lo que hace que esto mienta, y como se evita

   1. **Las partituras que son una foto.** Varias carpetas de Drive traen PDF
      que no son vectoriales: dentro llevan una imagen escaneada. El Flying
      Theme de José María es una imagen de 511x655 px a 62 ppi, y ahi las dos
      barras de una semicorchea ocupan menos de dos pixeles: no se pueden
      separar. Rasterizar ese PDF a 200 dpi no anade informacion, solo agranda
      el borron — y el detector daba 321 semicorcheas en una pieza que va
      entera en corcheas. Por eso ahora se mide el espacio de pentagrama en
      pixeles y, si no llega a `SP_MINIMO`, la partitura sale como **NO
      MEDIBLE** y hay que mirarla a ojo. Mas vale no saberlo que creer que se
      sabe.
   2. **El umbral de tinta fijo.** Hay ediciones que imprimen el pentagrama en
      gris claro; con el umbral de siempre no se encontraba ni un pentagrama y
      Peaches salia "sin semicorcheas" cuando las lleva a partir del c. 13.
   3. **El JPEG**, que difumina las lineas finas: se rasteriza a PNG.
   4. **Las cabezas de nota.** Dos cabezas de un acorde a distancia de tercera
      dejan el mismo dibujo en una columna que dos barras. Se distinguen porque
      una barra es RECTA: a lo ancho del tramo su grosor y su separacion apenas
      cambian, y una cabeza es ovalada.
   5. **La clave, la armadura y el compas** del principio de cada sistema, que
      son trazos gruesos y curvos (la clave de sol sola daba 26 falsos
      positivos en "When the Saints").
   6. **Las lineas adicionales.** Dos rayas paralelas separadas por un espacio
      exacto: el mismo dibujo que dos barras, y encima rectas. Se distinguen
      por el GROSOR — una barra es dos o tres veces mas gruesa que una linea de
      pentagrama—, asi que el grosor minimo se calcula midiendo las lineas de
      cada pentagrama en vez de fijarlo a ojo. Sin esto, el estudio de Diabelli
      salia con veinte semicorcheas y va entero en corcheas.

   Contrastado contra las partituras de `medir_figuras_patron.py`, miradas una
   a una a tamano grande.
"""
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
import score_reader as sr                                        # noqa: E402

DPI = 200

# Por debajo de este espacio de pentagrama (en pixeles) no se puede distinguir
# una barra de dos: el hueco entre ellas mide medio espacio.
SP_MINIMO = 11.0

# Y por debajo de esta resolucion propia, un PDF que solo lleva una imagen
# dentro no mejora por rasterizarlo mas grande.
PPI_MINIMO = 110

GROSOR_MIN = 0.20      # de una barra, en espacios de pentagrama
GROSOR_MAX = 0.75
SEPARA_MIN = 0.50      # entre los centros de las dos barras
SEPARA_MAX = 1.25
IGUALDAD = 0.55        # las dos barras tienen grosor parecido
SALTO_CLAVE = 6.5      # espacios que se ignoran al principio de cada sistema
LARGA = 1.10           # ancho a partir del cual es una barra doble entera
CORTA = 0.45           # y a partir del cual es un rabito de figura larga-corta
VARIA_MAX = 0.13       # una barra es recta: su grosor y su hueco casi no varian

UMBRALES = (125, 150, 175, 200)


class NoMedible(Exception):
    """La partitura no da resolucion para separar una barra de dos."""


def resolucion(pdf):
    """ppi propio del PDF: el de sus imagenes si solo lleva imagenes, o None
       si es vectorial (y entonces se puede rasterizar tan grande como haga
       falta)."""
    try:
        out = subprocess.run(['pdfimages', '-list', pdf], check=True,
                             capture_output=True, text=True).stdout
    except Exception:                                            # noqa: BLE001
        return None
    ppis = []
    for linea in out.splitlines()[2:]:
        campos = linea.split()
        if len(campos) > 13 and campos[2] == 'image':
            try:
                ppis.append(int(campos[12]))
            except ValueError:
                pass
    return min(ppis) if ppis else None


def cargar(path):
    """(mapa de tinta, umbral) con el umbral mas bajo que encuentra pentagramas."""
    gris = np.array(Image.open(path).convert('L'))
    for u in UMBRALES:
        a = gris < u
        if sr.pentagramas(a):
            return a, u
    return None, None


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


def _grosor_linea(a, top, sp):
    """Grosor tipico de una linea de pentagrama, en pixeles. Se mide sobre las
       cinco lineas del propio pentagrama: es la referencia contra la que una
       barra tiene que ser gruesa."""
    h, w = a.shape
    medidas = []
    for k in range(5):
        y = int(round(top + k * sp))
        if y < 1 or y >= h - 1:
            continue
        for x in range(0, w, max(1, w // 200)):
            if not a[y, x]:
                continue
            i = y
            while i > 0 and a[i - 1, x]:
                i -= 1
            f = y
            while f < h - 1 and a[f + 1, x]:
                f += 1
            g = f - i + 1
            if g <= 0.35 * sp:          # descartar cabezas, plicas y barras
                medidas.append(g)
    return float(np.median(medidas)) if medidas else 1.0


def _borde_izquierdo(a, y):
    fila = a[int(y) - 1:int(y) + 2].any(axis=0)
    xs = np.where(fila)[0]
    return int(xs[0]) if len(xs) else 0


def en_pagina(a):
    """[(x, y, sp, ancho)] de cada par de barras. Lanza NoMedible si los
       pentagramas de la pagina salen demasiado pequenos."""
    h, w = a.shape
    pautas = sr.pentagramas(a)
    if not pautas:
        return []
    sps = [(b - t) / 4.0 for t, b in pautas]
    if np.median(sps) < SP_MINIMO:
        raise NoMedible('el pentagrama mide %.1f px de espacio' % np.median(sps))
    fuera = []
    for top, bot in pautas:
        sp = (bot - top) / 4.0
        if sp < SP_MINIMO:
            continue
        y0, y1 = int(max(0, top - 4 * sp)), int(min(h, bot + 4 * sp))
        banda = a[y0:y1]
        # Una barra tiene que ser claramente mas gruesa que una linea de
        # pentagrama; si no, las lineas adicionales cuelan como barras dobles.
        gmin = max(GROSOR_MIN * sp, 1.8 * _grosor_linea(a, top, sp))
        gmax = GROSOR_MAX * sp
        dmin, dmax = SEPARA_MIN * sp, SEPARA_MAX * sp
        x_ini = _borde_izquierdo(a, top) + int(SALTO_CLAVE * sp)
        buenas = np.zeros(w, dtype=bool)
        alturas, huecos, gruesos = np.zeros(w), np.zeros(w), np.zeros(w)
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
                    alturas[x], huecos[x], gruesos[x] = c1 + y0, c2 - c1, (g1 + g2) / 2.0
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
    """Rasteriza (PDF o imagen) y devuelve (carpeta, rutas)."""
    tmp = tempfile.mkdtemp()
    with open(pdf, 'rb') as fh:
        cabecera = fh.read(5)
    if cabecera[:4] == b'%PDF':
        subprocess.run(['pdftoppm', '-png', '-r', str(dpi), pdf,
                        os.path.join(tmp, 'pg')], check=True,
                       stderr=subprocess.DEVNULL)
    else:
        im = Image.open(pdf).convert('L')
        f = max(1.0, (dpi / 72.0) * 595.0 / im.size[0])
        im.resize((int(im.size[0] * f), int(im.size[1] * f))).save(
            os.path.join(tmp, 'pg-1.png'))
    return tmp, sorted(os.path.join(tmp, f) for f in os.listdir(tmp)
                       if f.startswith('pg'))


def contar(pdf, dpi=DPI):
    """(barras dobles enteras, rabitos). Lanza NoMedible si la partitura no
       tiene resolucion para separarlas."""
    propia = resolucion(pdf)
    if propia is not None and propia < PPI_MINIMO:
        raise NoMedible('el PDF lleva dentro una imagen de %d ppi' % propia)
    tmp, pags = paginas(pdf, dpi)
    largas = cortas = 0
    sin_pautas = 0
    try:
        for f in pags:
            a, _u = cargar(f)
            if a is None:
                sin_pautas += 1
                continue
            for _x, _y, sp, ancho in en_pagina(a):
                if ancho >= LARGA * sp:
                    largas += 1
                elif ancho >= CORTA * sp:
                    cortas += 1
    finally:
        for f in pags:
            if os.path.exists(f):
                os.remove(f)
        os.rmdir(tmp)
    if sin_pautas == len(pags):
        raise NoMedible('no se encuentra ningun pentagrama')
    return largas, cortas


if __name__ == '__main__':
    for p in sys.argv[1:]:
        try:
            print('%-52s %s' % (os.path.basename(p)[:52], contar(p)))
        except NoMedible as exc:
            print('%-52s NO MEDIBLE · %s' % (os.path.basename(p)[:52], exc))
