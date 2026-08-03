# -*- coding: utf-8 -*-
"""Lector de partituras: mide un PDF y devuelve las notas que hay escritas.

   Es la herramienta que hace viable el cuaderno. La regla del proyecto es que
   ningún dato musical se afirma sin medirlo, y medir a ojo veinte partituras
   es inviable, así que esto automatiza la parte mecánica:

       render 200 dpi -> localizar pentagramas -> emparejarlos en sistemas
       -> detectar barras de compás -> aislar cabezas de nota -> nombrarlas

   Lo que este lector NO hace, y por eso sigue haciendo falta mirar la
   partitura a zoom antes de escribir nada en el cuaderno:
     - no lee alteraciones accidentales (♯ ♮ ♭ sueltos)
     - no lee duraciones: distingue cabeza llena de hueca, nada más
     - no lee silencios, ligaduras, dinámicas ni digitaciones

   Sirve para levantar el esqueleto (tonalidad, nº de compases, contorno,
   forma, qué compases se repiten) y para CONTRASTAR lo que uno cree haber
   visto. La palabra final la tiene siempre el zoom.

   Dos trampas que costaron caro y están resueltas aquí:

   0. Se renderiza a 200 dpi, no a 150: por debajo de eso el rasterizado se
      come líneas enteras del pentagrama en algunas ediciones y la detección
      encuentra tres líneas donde hay cinco.
   1. NO se borran las líneas del pentagrama antes de buscar cabezas. Al
      borrarlas se parte por la mitad toda cabeza que esté *sobre* una línea,
      y se pierden justo esas. La apertura morfológica ya se come las líneas
      (2 px) sin tocar las cabezas.
   2. La numeración de compases de la edición puede no ser la real. Aquí se
      cuentan barras de compás; si el número impreso no cuadra, manda el
      recuento, y hay que dejar dicho en la transcripción cuál se usa.
"""
import os
import subprocess

import numpy as np
from PIL import Image

try:
    from scipy import ndimage
except ImportError:                                     # pragma: no cover
    raise SystemExit('score_reader necesita scipy: pip install scipy '
                     '--break-system-packages')

# Nombres por posicion, empezando UNA posicion por encima de la linea superior.
# En clave de Sol la linea superior es Fa5; en clave de Fa, La3.
TREBLE = ['G5', 'F5', 'E5', 'D5', 'C5', 'B4', 'A4', 'G4', 'F4', 'E4',
          'D4', 'C4', 'B3', 'A3', 'G3', 'F3', 'E3']
BASS = ['B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3', 'B2', 'A2', 'G2',
        'F2', 'E2', 'D2', 'C2', 'B1', 'A1', 'G1']


def render(pdf_path, out_dir, dpi=200, prefix='pg'):
    """Renderiza el PDF a JPEG y devuelve la lista de rutas, en orden."""
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, prefix)
    for old in sorted(f for f in os.listdir(out_dir) if f.startswith(prefix)):
        os.remove(os.path.join(out_dir, old))
    subprocess.run(['pdftoppm', '-jpeg', '-r', str(dpi), pdf_path, base],
                   check=True)
    return [os.path.join(out_dir, f) for f in sorted(os.listdir(out_dir))
            if f.startswith(prefix)]


def load(path, umbral=125):
    return np.array(Image.open(path).convert('L')) < umbral


def pentagramas(a, cobertura=0.55):
    """Devuelve [(y_linea_superior, y_linea_inferior), ...] de cada pentagrama
       de la pagina, de arriba abajo. Detecta las 5 lineas por proyeccion
       horizontal y las agrupa de cinco en cinco."""
    h, w = a.shape
    x0, x1 = int(w * 0.22), int(w * 0.82)
    filas = a[:, x0:x1].sum(axis=1)
    thr = 0.80 * (x1 - x0)
    ys = [i for i, v in enumerate(filas) if v > thr]
    if not ys:
        return []
    grupos, cur = [], [ys[0]]
    for v in ys[1:]:
        if v - cur[-1] <= 2:
            cur.append(v)
        else:
            grupos.append(sum(cur) / len(cur)); cur = [v]
    grupos.append(sum(cur) / len(cur))

    # agrupar en pentagramas: cinco lineas con separacion regular
    out, i = [], 0
    while i + 4 < len(grupos):
        cinco = grupos[i:i + 5]
        pasos = [cinco[k + 1] - cinco[k] for k in range(4)]
        med = sum(pasos) / 4.0
        if med > 0 and all(abs(p - med) <= max(2.0, med * 0.30) for p in pasos):
            out.append((cinco[0], cinco[4]))
            i += 5
        else:
            i += 1
    return out


def sistemas(a, doble=True):
    """Empareja los pentagramas de la pagina en sistemas.
       doble=True  -> piano: (sol, fa) de dos en dos
       doble=False -> una sola clave por sistema"""
    ps = pentagramas(a)
    if not doble:
        return [(t, b, None, None) for t, b in ps]
    out = []
    for k in range(0, len(ps) - 1, 2):
        (tt, tb), (bt, bb) = ps[k], ps[k + 1]
        out.append((tt, tb, bt, bb))
    return out


def barras(a, y_top, y_bot, x0=None, x1=None, tol=4):
    """Barras de compas: columnas de tinta que cruzan el sistema entero.
       Devuelve las x, incluida la del principio del sistema."""
    h, w = a.shape
    x0 = x0 if x0 is not None else int(w * 0.10)
    x1 = x1 if x1 is not None else int(w * 0.95)
    n = int(y_bot) - int(y_top) + 1
    col = a[int(y_top):int(y_bot) + 1, :]
    llenas = [x for x in range(x0, x1) if col[:, x].sum() >= n - tol]
    if not llenas:
        return []
    g, cur = [], [llenas[0]]
    for v in llenas[1:]:
        if v - cur[-1] <= 3:
            cur.append(v)
        else:
            g.append(int(sum(cur) / len(cur))); cur = [v]
    g.append(int(sum(cur) / len(cur)))
    # la barra final doble sale como dos muy juntas: fusionar
    fus = [g[0]]
    for v in g[1:]:
        if v - fus[-1] > 12:
            fus.append(v)
    return fus


def cabezas(a, top, bot, clef, x0, x1, pad=None):
    """Cabezas de nota entre x0 y x1 en el pentagrama dado.
       Devuelve [(x, nombre, posicion_decimal, llena)] ordenado por x."""
    names = TREBLE if clef == 'treble' else BASS
    step = (bot - top) / 8.0
    pad = int(round(step * 8)) if pad is None else pad   # 4 posiciones fuera
    y0 = max(0, int(top) - pad)
    banda = a[y0:int(bot) + pad, x0:x1]
    if banda.size == 0:
        return []
    # NO se borran las lineas: partirian las cabezas que estan sobre ellas.
    # OJO: `step` es media distancia entre lineas (una posicion diatonica).
    # Una cabeza de nota mide ~UN espacio, o sea ~2*step de alto. Filtrar con
    # step en vez de 2*step rechaza todas las cabezas reales y deja pasar ruido.
    ev = max(3, int(round(step * 0.93)))       # alto del elemento estructurante
    eh = max(5, int(round(step * 1.67)))       # ancho
    abierta = ndimage.binary_opening(banda, structure=np.ones((ev, eh)))
    lab, k = ndimage.label(abierta)
    out = []
    for i in range(1, k + 1):
        ys, xs = np.where(lab == i)
        h = ys.max() - ys.min() + 1
        w = xs.max() - xs.min() + 1
        if not (step * 1.10 <= h <= step * 2.85 and step * 1.45 <= w <= step * 4.55):
            continue
        densidad = len(ys) / float(h * w)
        if densidad < 0.42:
            continue
        cy = ys.mean() + y0
        p = (cy - top) / step + 1
        idx = max(0, min(len(names) - 1, int(round(p))))
        out.append((int(xs.mean()) + x0, names[idx], round(p, 2),
                    densidad > 0.72))
    out.sort()
    return out


def leer(pdf_path, out_dir, doble=True, dpi=200, prefix='pg'):
    """Lee la partitura entera. Devuelve una lista de compases:
       [{'n': 1, 'pagina': 1, 'sistema': 1, 'treble': [...], 'bass': [...]}]
       Los nombres NO llevan alteraciones accidentales (ver docstring)."""
    paginas = render(pdf_path, out_dir, dpi=dpi, prefix=prefix)
    compases, n = [], 0
    for pi, path in enumerate(paginas, 1):
        a = load(path)
        for si, (tt, tb, bt, bb) in enumerate(sistemas(a, doble=doble), 1):
            y_top, y_bot = tt, (bb if bb is not None else tb)
            bs = barras(a, y_top, y_bot)
            if len(bs) < 2:
                continue
            for k in range(len(bs) - 1):
                n += 1
                xa, xb = bs[k] + 4, bs[k + 1] - 3
                reg = {'n': n, 'pagina': pi, 'sistema': si,
                       'treble': cabezas(a, tt, tb, 'treble', xa, xb)}
                if bt is not None:
                    reg['bass'] = cabezas(a, bt, bb, 'bass', xa, xb)
                compases.append(reg)
    return compases, paginas


def resumen(compases):
    """Vuelca los compases en texto, para pegarlo en el archivo de
       transcripcion y contrastarlo a ojo."""
    filas = []
    for c in compases:
        md = ' '.join(t[1] for t in c['treble'])
        mi = ' '.join(t[1] for t in c.get('bass', []))
        filas.append('c.%03d  MD: %-34s MI: %s' % (c['n'], md, mi))
    return '\n'.join(filas)


def repeticiones(compases, minimo=2):
    """Compases identicos en las dos manos. Sirve para encontrar la FORMA sin
       leerse la pieza entera: si los cc. 35-36 son iguales que los 3-4, ahi
       vuelve el tema. Este dato se dedujo mal una vez y salio caro."""
    firma = {}
    for c in compases:
        key = (tuple(t[1] for t in c['treble']),
               tuple(t[1] for t in c.get('bass', [])))
        if not any(key):
            continue
        firma.setdefault(key, []).append(c['n'])
    return {k: v for k, v in firma.items() if len(v) >= minimo}
