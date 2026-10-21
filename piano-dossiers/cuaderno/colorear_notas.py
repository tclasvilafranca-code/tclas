# -*- coding: utf-8 -*-
"""Pinta las cabezas de nota de una partitura VECTORIAL con el color de su nombre (el mismo
   cartel de todo el curso: DO rojo, RE naranja, MI amarillo, FA verde, SOL azul, LA lila,
   SI gris), para alumnos que aun no conocen las notas.

   Como funciona (solo PDF vectorial: las cabezas son trazados cerrados de ~7x6 pt):
     1. staves: lineas horizontales largas, agrupadas de cinco en cinco por su y;
     2. las claves se asignan por orden: en cada sistema el pentagrama de arriba es de sol y el
        de abajo de fa (todas las partituras de Lola van a dos pentagramas);
     3. la altura de cada cabeza sale de su y respecto de la linea de abajo (media gap = un paso);
     4. se dibuja encima un ovalo del color (relleno si la nota es negra, aro si es blanca/redonda).
   Las alteraciones se ignoran: se pinta por la letra de la nota.
   `python3 colorear_notas.py entrada.pdf salida.pdf` deja ademas un informe de lo detectado."""
import collections
import sys

import pymupdf

COLOR = dict(C='#E4392B', D='#F28C0E', E='#F9C80E', F='#76B82A', G='#2E86C8', A='#A58AC9', B='#A7A397')
NOMBRE = dict(C='DO', D='RE', E='MI', F='FA', G='SOL', A='LA', B='SI')
LETRAS = 'CDEFGAB'


def hexa(h):
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (1, 3, 5))


def segmentos_h(dr, ancho_min=150):
    """Lineas horizontales largas: [(y, x0, x1)]; une los trozos de una misma y (MuseScore parte
       el pentagrama en un trazo por compas)."""
    por_y = collections.defaultdict(list)
    for p in dr:
        for it in p['items']:
            if it[0] == 'l':
                a, b = it[1], it[2]
                if abs(a.y - b.y) < 0.05:
                    por_y[round(a.y, 1)].append((min(a.x, b.x), max(a.x, b.x)))
            elif it[0] == 're':
                r = it[1]
                if r.height < 0.8:
                    por_y[round((r.y0 + r.y1) / 2, 1)].append((r.x0, r.x1))
    seg = []
    for y, tr in por_y.items():
        tr.sort()
        ini, fin = tr[0]
        for x0, x1 in tr[1:] + [(1e9, 1e9)]:
            if x0 > fin + 3:            # hueco: cierra el tramo
                if fin - ini >= ancho_min:
                    seg.append((y, ini, fin))
                ini, fin = x0, x1
            else:
                fin = max(fin, x1)
    return seg


def pentagramas(dr, ancho_min=150):
    """-> lista de (xl, xr, [y1..y5]) ordenada de arriba abajo."""
    lin = sorted(segmentos_h(dr, ancho_min))
    out = []
    i = 0
    while i + 4 < len(lin):
        ys = [l[0] for l in lin[i:i + 5]]
        gaps = [b - a for a, b in zip(ys, ys[1:])]
        if max(gaps) - min(gaps) < 1.2 and 3.0 < gaps[0] < 12:
            out.append((min(l[1] for l in lin[i:i + 5]), max(l[2] for l in lin[i:i + 5]), ys))
            i += 5
        else:
            i += 1
    return out


# glifos de cabeza de nota: (fuente, codigo) -> tipo 'n' negra, 'b' blanca, 'r' redonda
GLIFOS = {}
for _f in ('Leland', 'Bravura', 'BravuraText', 'Bravura Text', 'MScore', 'MScoreText'):
    GLIFOS.update({(_f, 0xe0a4): 'n', (_f, 0xe0a3): 'b', (_f, 0xe0a2): 'r'})
GLIFOS.update({('MScore', 0xe12d): 'n', ('MScore', 0xe12c): 'b', ('MScore', 0xe12b): 'r'})
GLIFOS.update({('Petrucci', 0x153): 'n', ('Petrucci', 0x2d9): 'b', ('Petrucci', 0x2d8): 'b', ('Petrucci', 0x77): 'r'})
CLAVE_G = {('Leland', 0xe050), ('Bravura', 0xe050), ('MScore', 0xe050), ('MScoreText', 0xe050), ('MScore', 0xe19e), ('Petrucci', 0x26)}
CLAVE_F = {('Leland', 0xe062), ('Bravura', 0xe062), ('MScore', 0xe062), ('MScoreText', 0xe062), ('MScore', 0xe19c), ('Petrucci', 0x3f)}


def glifos(pg):
    """-> (cabezas [(cx, cy, w, tipo)], claves [(x, y, 'G'|'F')]) leidas del texto del PDF."""
    cab, cla = [], []
    for b in pg.get_text('rawdict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if s['size'] < 15:
                    continue
                for ch in s['chars']:
                    k = (s['font'], ord(ch['c']))
                    if k in GLIFOS:
                        bb = ch['bbox']
                        cab.append(((bb[0] + bb[2]) / 2.0, ch['origin'][1], bb[2] - bb[0], GLIFOS[k]))
                    elif k in CLAVE_G:
                        cla.append((ch['origin'][0], ch['origin'][1], 'G'))
                    elif k in CLAVE_F:
                        cla.append((ch['origin'][0], ch['origin'][1], 'F'))
    return cab, cla


def cabezas(dr, gap):
    """Cabezas vectoriales: trazados cerrados rellenos ~ gap x 0.85*gap, de 10 o 12 curvas."""
    res = []
    for p in dr:
        r = p['rect']
        if p['fill'] is None:
            continue
        kinds = ''.join(i[0] for i in p['items'])
        if set(kinds) != {'c'}:
            continue
        if not (0.85 * gap < r.width < 1.6 * gap and 0.6 * gap < r.height < 1.2 * gap):
            continue
        res.append(((r.x0 + r.x1) / 2.0, (r.y0 + r.y1) / 2.0, r.width, 'n' if len(kinds) <= 10 else 'b'))
    return res


def colorear(entrada, salida, imprimir=False):
    doc = pymupdf.open(entrada)
    informe = []
    for pn, pg in enumerate(doc):
        dr = pg.get_drawings()
        sts = pentagramas(dr)
        if not sts:
            informe.append((pn + 1, 0, 0))
            continue
        gap = sts[0][2][1] - sts[0][2][0]
        cab = cabezas(dr, gap)
        gl, claves = glifos(pg)
        cab += gl
        sh = pg.new_shape()
        cuenta = collections.Counter()
        n = 0
        # clave de cada pentagrama: glifo de clave a su izquierda; si no, alterna sol/fa
        tipo_clave = []
        for k, (xl, xr, ys) in enumerate(sts):
            mejor = None
            for cx, cy, c in claves:
                if abs(cx - xl) < 40 and ys[0] - 2 * gap <= cy <= ys[4] + 2 * gap:
                    mejor = c
            tipo_clave.append(mejor or ('G' if k % 2 == 0 else 'F'))
        for cx, cy, w, tp in cab:
            mejor, dmin = None, 1e9
            for k, (xl, xr, ys) in enumerate(sts):
                cen = (ys[0] + ys[4]) / 2.0
                if xl - 5 <= cx <= xr + 5 and abs(cy - cen) < dmin:
                    mejor, dmin = k, abs(cy - cen)
            if mejor is None or dmin > 5.2 * gap:
                continue
            gap_k = sts[mejor][2][1] - sts[mejor][2][0]
            paso = round((sts[mejor][2][4] - cy) / (gap_k / 2.0))
            idx = ((2 if tipo_clave[mejor] == 'G' else 4) + paso) % 7   # linea de abajo: MI (sol) / SOL (fa)
            letra = LETRAS[idx]
            col = hexa(COLOR[letra])
            rx, ry = max(w, 1.25 * gap_k) / 2.0 + 0.3, gap_k / 2.0 + 0.35
            cuenta[NOMBRE[letra]] += 1
            sh.draw_oval(pymupdf.Rect(cx - rx, cy - ry, cx + rx, cy + ry))
            sh.finish(color=(0.1, 0.1, 0.1), fill=col, width=0.5)
            if tp in 'br':      # blanca / redonda: agujero blanco para que se vea hueca
                sh.draw_oval(pymupdf.Rect(cx - rx * 0.45, cy - ry * 0.55, cx + rx * 0.45, cy + ry * 0.55))
                sh.finish(color=(0.1, 0.1, 0.1), fill=(1, 1, 1), width=0.4)
            n += 1
        sh.commit()
        informe.append((pn + 1, len(sts), n, dict(cuenta)))
    doc.save(salida)
    return informe


if __name__ == '__main__':
    for fila in colorear(sys.argv[1], sys.argv[2]):
        print(fila)
