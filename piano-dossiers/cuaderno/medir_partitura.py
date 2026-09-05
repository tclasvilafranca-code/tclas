# -*- coding: utf-8 -*-
"""LA PUERTA DE ENTRADA. Se pasa una partitura por aqui ANTES de escribir una
   sola linea de su pieza.

   Los tres fallos caros de este cuaderno (dos compases mal, la figura de
   marcha del Toreador escrita al doble de lento, las semicorcheas que ninguna
   hoja dibujaba) tienen el mismo origen: la transcripcion anoto las alturas
   —que son laboriosas— y dio por supuesto lo que parecia obvio. Lo obvio es
   justo lo que nadie vuelve a mirar.

   Asi que esto hace dos cosas, y las dos importan:

     1. MIDE lo que se puede medir solo: paginas, si la primera es portada,
        cuantos pentagramas hay por sistema (o sea, si es a dos o a cuatro
        manos), la resolucion real del PDF y —si da resolucion— cuantas barras
        dobles hay, que es la firma de la semicorchea.

     2. RECORTA Y GUARDA el arranque del primer pentagrama a tamano grande:
        clave, armadura y cifra de compas. Eso NO lo adivina el programa; hay
        que mirarlo. La herramienta entrega la imagen y la lista de lo que hay
        que leer en ella y de donde va anotado.

   Y despues no hay que acordarse de nada: `auditar_compas.py` y
   `auditar_tonalidad.py` fallan mientras la pieza nueva no este en sus tablas,
   y `auditar_figuras.py` falla mientras una partitura no medible no este en
   `MIRADAS`. El sistema no deja pasar una pieza cuyo compas, armadura o figura
   no haya leido nadie.

   Uso:  python3 medir_partitura.py <partitura.pdf> [mas.pdf ...]
         python3 medir_partitura.py --alumno dilan      (toda su carpeta)
"""
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import score_reader as sr                                        # noqa: E402
import medir_figuras as mf                                       # noqa: E402

ARRANQUES = os.path.join(HERE, 'arranques')
DPI_ARRANQUE = 300
# ancho del recorte, en espacios de pentagrama: cabe clave + armadura de tres
# alteraciones + cifra de compas con holgura, y poco mas (que estorba).
ANCHO = 11


def _rasterizar(pdf, pagina, dpi):
    tmp = tempfile.mkdtemp()
    with open(pdf, 'rb') as fh:
        es_pdf = fh.read(4) == b'%PDF'
    if es_pdf:
        subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(pagina),
                        '-l', str(pagina), pdf, os.path.join(tmp, 'pg')],
                       check=True, stderr=subprocess.DEVNULL)
    else:
        Image.open(pdf).convert('L').save(os.path.join(tmp, 'pg-1.png'))
    hijos = sorted(os.path.join(tmp, f) for f in os.listdir(tmp))
    return tmp, (hijos[0] if hijos else None)


def _tinta(path):
    gris = np.array(Image.open(path).convert('L'))
    for u in mf.UMBRALES:
        a = gris < u
        ps = sr.pentagramas(a)
        if ps:
            return a, ps
    return None, []


def _paginas(pdf):
    try:
        out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
        for l in out.splitlines():
            if l.startswith('Pages:'):
                return int(l.split()[1])
    except Exception:                                            # noqa: BLE001
        pass
    return 1


def primera_de_musica(pdf, maximo=4):
    """Numero de la primera pagina que tiene pentagramas de verdad.

       Las descargas de free-scores traen una portada con el logo, la ficha de
       la obra y un QR: si se mide esa, no se mide nada. Dos partituras de
       Arnau se quedaron sin recorte por esto durante el barrido de compases."""
    for pg in range(1, min(maximo, _paginas(pdf)) + 1):
        tmp, ruta = _rasterizar(pdf, pg, 110)
        try:
            if ruta:
                _a, ps = _tinta(ruta)
                if len(ps) >= 2:
                    return pg
        finally:
            _limpiar(tmp)
    return 1


def _limpiar(tmp):
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)


def arranque(pdf, destino, pagina=None):
    """Guarda el recorte de clave + armadura + compas. Devuelve (ruta, sistemas
       por pagina, espacio de pentagrama en px)."""
    pg = pagina or primera_de_musica(pdf)
    tmp, ruta = _rasterizar(pdf, pg, DPI_ARRANQUE)
    try:
        if not ruta:
            return None, 0, 0.0
        im = Image.open(ruta)
        a, ps = _tinta(ruta)
        if not ps:
            return None, 0, 0.0
        top, bot = ps[0]
        sp = (bot - top) / 4.0
        fila = a[int(top) - 1:int(top) + 2].any(axis=0)
        xs = np.where(fila)[0]
        x0 = int(xs[0]) if len(xs) else 0
        c = im.crop((max(0, x0 - int(sp)), max(0, int(top - 3 * sp)),
                     min(im.size[0], x0 + int(ANCHO * sp)), int(bot + 3 * sp)))
        # a tamano de mirar, no de adivinar
        f = max(1, int(900 / max(1, c.size[0])))
        c = c.resize((c.size[0] * f, c.size[1] * f))
        c.save(destino)
        return destino, _por_sistema(a, ps), sp
    finally:
        _limpiar(tmp)


def _por_sistema(a, ps):
    """Cuantos pentagramas tiene UN sistema, no la pagina entera.

       Es el dato que dice si la pieza va a dos manos (2) o a cuatro (4), y lo
       de cuatro manos hay que saberlo ANTES de empezar: el lector empareja mal
       los pentagramas y la transcripcion sale cruzada.

       No vale mirar los huecos: en la edicion del Toreador el hueco de dentro
       del sistema (195 px) y el de entre sistemas (220) son casi el mismo. Lo
       que si es inequivoco es la BARRA de la izquierda, que une los
       pentagramas de un sistema y se corta entre sistema y sistema."""
    if len(ps) < 2:
        return len(ps)
    fila = a[int(ps[0][0]) - 1:int(ps[0][0]) + 2].any(axis=0)
    xs = np.where(fila)[0]
    if not len(xs):
        return len(ps)
    x0 = int(xs[0])
    n = 1
    for k in range(len(ps) - 1):
        y1, y2 = int(ps[k][1]) + 2, int(ps[k + 1][0]) - 2
        if y2 <= y1:
            break
        col = a[y1:y2, max(0, x0 - 3):x0 + 4].any(axis=1)
        if col.mean() < 0.8:
            break
        n += 1
    return n


def medir(pdf):
    """Todo lo que se puede saber de una partitura sin mirarla."""
    d = dict(partitura=os.path.basename(pdf), paginas=_paginas(pdf))
    d['pagina_musica'] = primera_de_musica(pdf)
    d['portada'] = d['pagina_musica'] > 1
    # nada de splitext: media docena de estas partituras se llaman
    # "Toreador. Bizet" o "ADAGIO." y splitext se comeria medio nombre.
    base = os.path.basename(pdf)
    if base.lower().endswith('.pdf'):
        base = base[:-4]
    slug = ''.join(ch if ch.isalnum() else '_' for ch in base)[:60].strip('_')
    os.makedirs(ARRANQUES, exist_ok=True)
    ruta = os.path.join(ARRANQUES, 'ARRANQUE_%s.png' % slug)
    d['arranque'], d['pentagramas'], d['sp'] = arranque(pdf, ruta, d['pagina_musica'])
    d['ppi'] = mf.resolucion(pdf)
    try:
        largas, cortas = mf.contar(pdf)
        d['medible'] = True
        d['barras_dobles'] = largas
        d['rabitos'] = cortas
    except mf.NoMedible as e:
        d['medible'] = False
        d['motivo'] = str(e)
    except Exception as e:                                       # noqa: BLE001
        d['medible'] = False
        d['motivo'] = 'no se ha podido medir: %s' % e
    return d


def informe(d):
    print('\n%s' % d['partitura'])
    print('  páginas ................ %d%s' % (
        d['paginas'],
        '  · la música empieza en la %d (la %d es portada)'
        % (d['pagina_musica'], d['pagina_musica'] - 1) if d['portada'] else ''))
    manos = {1: 'una sola línea', 2: 'dos manos', 3: 'tres pentagramas (raro: míralo)',
             4: 'CUATRO MANOS'}.get(d['pentagramas'], '%d pentagramas' % d['pentagramas'])
    print('  pentagramas por sistema  %s' % manos)
    print('  resolución ............. %s' % (
        'vectorial (se puede ampliar todo lo que haga falta)' if d['ppi'] is None
        else '%d ppi' % d['ppi']))
    if d['medible']:
        n = d['barras_dobles']
        print('  figura más corta ....... %s (%d barras dobles medidas)'
              % ('SEMICORCHEA' if n >= 20 else
                 'corchea · sin barras dobles' if n == 0 else
                 'dudoso, míralo a ojo', n))
    else:
        print('  figura más corta ....... NO MEDIBLE · %s' % d.get('motivo', ''))
        print('                           hay que mirarla a ojo y anotarla en')
        print('                           auditar_figuras.MIRADAS')
    print('  arranque recortado ..... %s' % (d['arranque'] or '(no se ha podido)'))
    print('''
  MIRA ESA IMAGEN Y ANOTA, que esto no lo adivina nadie:
    · la CIFRA DE COMPÁS  ->  time_sig  y  auditar_compas.LEIDO
    · la ARMADURA (cuántos sostenidos o bemoles pegados a la clave)
                          ->  key_sig   y  auditar_tonalidad.LEIDO
  Y no te fíes de que "se ve claro": si una figura no te cuadra, SUMA EL
  COMPÁS. Un compás mal transcrito casi nunca cierra.''')


def main(argv):
    pdfs = []
    if argv and argv[0] == '--alumno':
        base = os.path.join(HERE, '..', 'students', argv[1], 'source')
        for raiz, _d, ficheros in os.walk(base):
            for f in sorted(ficheros):
                if not f.startswith('.'):
                    pdfs.append(os.path.join(raiz, f))
    else:
        pdfs = list(argv)
    if not pdfs:
        print(__doc__)
        return 2
    for p in pdfs:
        if not os.path.exists(p):
            print('\n%s\n  NO EXISTE' % p)
            continue
        informe(medir(p))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
