# -*- coding: utf-8 -*-
"""Busca CAMBIOS DE ARMADURA O DE COMPAS a mitad de pieza.

   Es el hueco que dejaban abiertos `auditar_compas.py` y `auditar_tonalidad.py`:
   los dos leen el PRIMER compas de la PRIMERA pagina, asi que una pieza que
   arranca en 4/4 y se pone en 3/4 en el c. 40, o que gana dos sostenidos a
   mitad, pasaba las dos auditorias diciendo la verdad a medias. Y el alumno se
   lo encuentra de frente, solo, en casa.

   COMO LO ENCUENTRA. No hace falta leer la cifra ni contar las alteraciones:
   basta con notar que el arranque del pentagrama ha CAMBIADO. El grabador
   reimprime clave y armadura al principio de cada sistema, asi que si se
   recorta esa esquina en todos los sistemas de todas las paginas y se comparan
   entre si, un cambio de armadura salta a la vista como una mancha distinta.
   Lo mismo vale para el compas cuando se reimprime.

   Se comparan pentagramas del MISMO SITIO del sistema (el de arriba con el de
   arriba, el de abajo con el de abajo): si no, un piano normal daria cambio en
   todos los sistemas solo porque una mano va en clave de sol y la otra en
   clave de fa.

   Esto no decide nada: hace una lista corta para mirarla a ojo. Lo que se vea
   se anota, como todo lo demas.

   Uso:  python3 medir_cambios.py                (todas las partituras)
         python3 medir_cambios.py <fichero.pdf>  (una)
"""
import glob
import hashlib
import io
import contextlib
import importlib
import os
import sys

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import medir_partitura as mp                                     # noqa: E402

DPI = 150
# Cuanto hueco vacio hace falta para dar por terminado el arranque del
# pentagrama. Entre la armadura y lo que viene detras siempre hay aire; entre
# dos alteraciones de la armadura, no.
HUECO = 0.55               # en espacios de pentagrama
# Y cuanto tiene que variar la anchura del arranque para llamarlo cambio. Una
# alteracion mas ocupa algo mas de un espacio, asi que medio espacio de
# diferencia ya es mucho mas de lo que da el ruido de medida.
TOLERANCIA = 0.55


def _ancho_arranque(a, top, bot, sp):
    """Cuanto ocupa, en espacios de pentagrama, lo que hay pegado a la clave.

       Es clave + armadura (y en el primer sistema, tambien la cifra de compas).
       No hace falta leer nada: si la pieza gana o pierde alteraciones a mitad,
       este numero cambia, y con eso basta para tener que ir a mirarlo.

       Se buscaba antes comparando recortes de imagen y no valia: a lo ancho de
       la clave caben ya las primeras notas, que cambian en todos los sistemas
       por definicion, y salia que la pieza entera 'cambiaba'."""
    y1, y2 = int(top - 1.5 * sp), int(bot + 1.5 * sp)
    banda = a[max(0, y1):y2].copy()
    # Fuera las CINCO LINEAS del pentagrama: son tinta continua de lado a lado
    # y sin quitarlas no hay ni un hueco vacio en toda la linea, que es lo que
    # hacia que esto devolviera None en media docena de partituras.
    for i in range(5):
        fila = int(top + i * sp) - max(0, y1)
        banda[max(0, fila - 1):fila + 2] = False
    col = banda.any(axis=0)
    xs = np.where(col)[0]
    if not len(xs):
        return None
    x0 = int(xs[0])
    # Tramos de tinta seguidos, con sus huecos: el arranque es clave + armadura,
    # o sea el bloque de tramos que van pegados unos a otros.
    tramos = []
    x = 0
    n = len(col)
    while x < n:
        if col[x]:
            ini = x
            while x < n and col[x]:
                x += 1
            tramos.append((ini, x))
        else:
            x += 1
    if not tramos:
        return None
    # La primera raya fina es la BARRA del principio del sistema, no la clave.
    while tramos and (tramos[0][1] - tramos[0][0]) < 0.28 * sp:
        tramos.pop(0)
    if not tramos:
        return None
    hueco = max(2, int(HUECO * sp))
    ini = tramos[0][0]
    fin = tramos[0][1]
    for a1, a2 in tramos[1:]:
        if a1 - fin >= hueco:
            break
        fin = a2
    return (fin - ini) / sp


def _anchos(pdf):
    """[(pagina, hueco en el sistema, ancho del arranque)]"""
    out = []
    pg0 = mp.primera_de_musica(pdf)
    total = mp._paginas(pdf)
    por_sistema = None
    for pg in range(pg0, total + 1):
        tmp, ruta = mp._rasterizar(pdf, pg, DPI)
        try:
            if not ruta:
                continue
            a, ps = mp._tinta(ruta)
            if not ps:
                continue
            if por_sistema is None:
                por_sistema = mp._por_sistema(a, ps)
            for k, (top, bot) in enumerate(ps):
                sp = (bot - top) / 4.0
                w = _ancho_arranque(a, top, bot, sp)
                if w is not None:
                    out.append((pg, k % max(1, por_sistema), w))
        finally:
            mp._limpiar(tmp)
    return out


def cambios(pdf):
    """[(pagina, hueco, ancho, ancho normal)] de los sistemas cuyo arranque no
       mide lo que mide el resto.

       La referencia es la MEDIANA de los sistemas de esa misma posicion, no el
       primero: el primero lleva ademas la cifra de compas y saldria el unico
       raro de la pieza entera."""
    trozos = _anchos(pdf)
    if len(trozos) < 4:
        return [], len(trozos)
    por_hueco = {}
    for pg, k, w in trozos:
        por_hueco.setdefault(k, []).append((pg, w))
    fuera = []
    for k, lista in por_hueco.items():
        if len(lista) < 3:
            continue
        med = float(np.median([w for _p, w in lista]))
        for pg, w in lista:
            if abs(w - med) > TOLERANCIA:
                fuera.append((pg, k, w, med))
    return fuera, len(trozos)


def _partituras():
    """Las partituras distintas del proyecto, con las piezas que las usan."""
    PREF = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']
    vistos = {}
    for p in PREF:
        for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py'))):
            m = os.path.basename(f)[:-3]
            with contextlib.redirect_stdout(io.StringIO()), \
                    contextlib.redirect_stderr(io.StringIO()):
                cfg = getattr(importlib.import_module(m), 'CANCION', None)
            if not cfg:
                continue
            r = cfg.get('partitura') or ''
            if not os.path.exists(r):
                continue
            with open(r, 'rb') as fh:
                h = hashlib.md5(fh.read()).hexdigest()
            vistos.setdefault(h, [r, []])[1].append(m)
    return sorted(vistos.values())


def main(argv):
    if argv:
        for p in argv:
            fuera, n = cambios(p)
            print('%-46s %d sistemas · %d con el arranque distinto'
                  % (os.path.basename(p)[:46], n, len(fuera)))
            for pg, k, w, med in fuera:
                print('      página %d, pentagrama %d · arranque de %.1f espacios (lo normal, %.1f)'
                      % (pg, k, w, med))
        return 0

    sospechosas = []
    for ruta, usos in _partituras():
        try:
            fuera, n = cambios(ruta)
        except Exception as e:                                   # noqa: BLE001
            print('%-46s no se ha podido medir: %s' % (os.path.basename(ruta)[:46], e))
            continue
        if fuera:
            sospechosas.append((os.path.basename(ruta), len(fuera), n, usos))
        print('.', end='', flush=True)
    print('\n')
    print('PARTITURAS QUE CAMBIAN DE ARRANQUE A MITAD: %d' % len(sospechosas))
    for base, k, n, usos in sorted(sospechosas, key=lambda x: -x[1]):
        print('   %-44s %2d de %2d sistemas · %s'
              % (base[:44], k, n, ' '.join(usos)[:44]))
    print('\nMíralas a ojo: puede ser un cambio de armadura o de compás de '
          'verdad,\ny entonces la pieza tiene que decirlo.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
