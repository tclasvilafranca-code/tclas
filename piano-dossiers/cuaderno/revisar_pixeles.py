# -*- coding: utf-8 -*-
"""Revision de pixeles de los albumes montados: que nada se salga del papel.

   El auditor de cada alumno mide la `y` final de cada hoja ANTES de imprimir,
   y eso pilla el material que se pasa de largo. Lo que no pilla es lo que se
   dibuja fuera de ese calculo (un recuadro que se posiciona solo, un pie que
   crece al envolver) ni lo que pase al unir los PDF. Por eso esta revision se
   hace sobre el PDF final, rasterizado.

   Cada pagina se renderiza a 110 dpi y se mide donde esta el ultimo pixel
   oscuro por abajo y por la derecha.

   **Las paginas de partitura no se revisan**, y no es una excusa: son el PDF
   del alumno, no lo dibujamos nosotros, y muchas ediciones llegan hasta el
   borde del papel. Se distinguen porque las nuestras llevan **la banda azul
   marino de 6 pt pegada al borde de arriba** (`portada.NAVY`), que ninguna
   edicion comercial trae. Si una pagina no tiene esa banda, no es nuestra.

   Uso:  python revisar_pixeles.py [album.pdf ...]
   Sin argumentos revisa los diez cuadernos de `output/`.
"""
import glob
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(HERE, '..', 'output')

DPI = 110
PT = DPI / 72.0

# Margenes reales del formato (portada.MARGIN = 46, pie a 22 pt del borde).
BORDE_ABAJO = 20.0          # pt: nada puede bajar de aqui
BORDE_DERECHA = 46.0        # pt: el margen derecho
TOLERANCIA = 6.0            # pt: el antialias del rasterizado

OSCURO = 130                # nivel de gris que cuenta como tinta
MINIMO_FILA = 3             # pixeles de tinta para que una fila cuente


def _es_nuestra(arr):
    """La banda azul marino de 6 pt pegada al borde superior."""
    banda = arr[:int(4 * PT), :]
    if banda.size == 0:
        return False
    # La banda es continua y ocupa el ancho entero: mas del 90 % oscuro.
    return (banda < OSCURO).mean() > 0.9


def revisar(pdf):
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-jpeg', '-r', str(DPI), pdf,
                    os.path.join(tmp, 'pg')], check=True)
    paginas = sorted(glob.glob(os.path.join(tmp, 'pg-*.jpg')))
    avisos, nuestras = [], 0
    for f in paginas:
        arr = np.array(Image.open(f).convert('L'))
        if not _es_nuestra(arr):
            continue
        nuestras += 1
        alto, ancho = arr.shape
        # La banda azul marino ocupa el ancho entero a proposito: si se mide,
        # todas las paginas parecen salirse por la derecha por 1,3 pt.
        tinta = arr < OSCURO
        tinta[:int(10 * PT), :] = False
        filas = np.where(tinta.sum(axis=1) >= MINIMO_FILA)[0]
        cols = np.where(tinta.sum(axis=0) >= MINIMO_FILA)[0]
        if not len(filas):
            continue
        abajo = (alto - filas.max()) / PT          # pt libres por abajo
        derecha = (ancho - cols.max()) / PT        # pt libres por la derecha
        if abajo < BORDE_ABAJO - TOLERANCIA:
            avisos.append('%s pag %s · se acerca al borde de abajo: quedan %.1f pt'
                          % (os.path.basename(pdf), os.path.basename(f)[3:-4], abajo))
        if derecha < BORDE_DERECHA - TOLERANCIA:
            avisos.append('%s pag %s · se pasa del margen derecho: quedan %.1f pt'
                          % (os.path.basename(pdf), os.path.basename(f)[3:-4], derecha))
    for f in paginas:
        os.remove(f)
    os.rmdir(tmp)
    return len(paginas), nuestras, avisos


def main(pdfs=None):
    pdfs = pdfs or sorted(glob.glob(os.path.join(SALIDA, '*_Cuaderno_del_Pianista_*.pdf')))
    if not pdfs:
        print('no hay albumes que revisar en %s' % SALIDA)
        return 1
    total, propias, todos = 0, 0, []
    for pdf in pdfs:
        n, mias, avisos = revisar(pdf)
        total += n
        propias += mias
        todos += avisos
        print('%-46s %4d paginas · %4d nuestras · %d avisos'
              % (os.path.basename(pdf), n, mias, len(avisos)))
    print('\n%d paginas revisadas · %d dibujadas por nosotros · %d de partitura'
          % (total, propias, total - propias))
    if not todos:
        print('\nPIXELES OK — ninguna pagina nuestra se sale del papel.')
        return 0
    print('\nAVISOS:')
    for a in todos:
        print('   ' + a)
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
