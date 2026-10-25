# -*- coding: utf-8 -*-
"""Motor de los dosieres para alumnos de 12-20 anos (30 min de clase).

   Una PIEZA se describe con un dict (`mp_NN_*.py`) y este modulo monta sus paginas:
     ficha · manos · guia por bloques · partitura recolocada con burbujas · pauta

   La partitura de Drive NO se toca: se detectan los sistemas sobre el PDF, se corta en las
   filas en blanco que hay entre ellos y se vuelve a montar (vectorial, sin reescalar de
   forma apreciable) con aire para las burbujas. Todo lo que afirma el dosier se MIDE antes.
"""
import io
import os
import sys
import subprocess
import tempfile
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from PIL import Image
import segno
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase.pdfmetrics import stringWidth
from pypdf import PdfReader, PdfWriter
import bn
bn.instalar()
import tema_ca
tema_ca.instalar()
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, INK, MUTED, _wrap)
import ficha_info as _fi
tema_ca.post_imports()
from ficha_info import PANEL, build_ficha
from hoja_pauta import build_pauta

HERE = os.path.dirname(os.path.abspath(__file__))
ALUMNA = os.environ.get('ALUMNA', 'eva')
SRCDIR = os.path.join(HERE, '..', 'students', 'eva_sc' if ALUMNA == 'eva' else ALUMNA,
                      'source_bn' if (ALUMNA == 'lola' and os.environ.get('BN') == '1') else 'source')
OUT = os.path.join(HERE, 'entrega')
PAGE_W, PAGE_H = 595.276, 841.89
OCRE = HexColor('#8C6A3F')
AZUL = HexColor('#3E6E8F')
VERDE = HexColor('#4F7A5A')
ROJO = HexColor('#A0453A')
MORADO = HexColor('#6B5B95')
BLANCO = HexColor('#FFFFFF')
GRIS = HexColor('#D9D2BF')
COLORES_BLOQUE = [AZUL, OCRE, ROJO, VERDE, MORADO, HexColor('#B0723A'), HexColor('#3C7C7A'),
                  HexColor('#8A4A6B'), HexColor('#5A6B8C')]
if tema_ca.ACTIU:
    OCRE, AZUL, VERDE, ROJO, MORADO, GRIS = [HexColor(tema_ca.PAL[k]) for k in
                                             ('OCRE', 'AZUL', 'VERDE', 'ROJO', 'MORADO', 'GRIS')]
    COLORES_BLOQUE = [HexColor(x) for x in tema_ca.BLOQUES]


# ------------------------------------------------------------ deteccion
def _gris(pdf, pag, dpi=144):
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-png', '-f', str(pag), '-l', str(pag),
                        pdf, os.path.join(d, 'p')], check=True)
        f = [x for x in os.listdir(d) if x.endswith('.png')][0]
        return np.array(Image.open(os.path.join(d, f)).convert('L'))


def bandas(pdf, minblank=7.0):
    """Bandas de tinta separadas por filas en blanco (>= minblank pt), por pagina.
       -> [dict(pag, ancho, alto, bandas=[dict(ya, yb, left)])]; todo en pt."""
    out = []
    n = len(PdfReader(pdf).pages)
    for p in range(1, n + 1):
        arr = _gris(pdf, p)
        h, w = arr.shape
        tinta = arr[:, 20:w - 20] < 170
        filas = tinta.any(1)
        bs, ini, blanco = [], None, 0
        for r in range(h):
            if filas[r]:
                if ini is None:
                    ini = r
                blanco = 0
                fin = r
            elif ini is not None:
                blanco += 1
                if blanco / 2 >= minblank:
                    bs.append((ini, fin))
                    ini = None
        if ini is not None:
            bs.append((ini, fin))
        res = []
        for (a, b) in bs:
            cols = np.where(tinta[a:b + 1].any(0))[0]
            res.append(dict(ya=a / 2, yb=(b + 1) / 2, left=(cols.min() + 20) / 2 if len(cols) else 20))
        out.append(dict(pag=p, ancho=w / 2, alto=h / 2, bandas=res))
    return out


def _tinta(pdf, pag):
    arr = _gris(pdf, pag)
    h, w = arr.shape
    return arr[:, 20:w - 20] < 170, w / 2, h / 2


def huecos(pdf, salida_png=None, minimo=3.0):
    """AYUDA para escribir `cortes`: dibuja cada pagina con las filas en blanco (>= minimo pt)
       numeradas por su y (pt). Devuelve la lista [(pag, y_centro, largo)]."""
    from PIL import ImageDraw
    res = []
    for p in range(1, len(PdfReader(pdf).pages) + 1):
        t, w, h = _tinta(pdf, p)
        filas = t.any(1)
        im = Image.fromarray((255 - t.astype('uint8') * 255)).convert('RGB')
        d = ImageDraw.Draw(im)
        ini = None
        for r in range(len(filas) + 1):
            v = filas[r] if r < len(filas) else True
            if not v and ini is None:
                ini = r
            if v and ini is not None:
                if (r - ini) / 2 >= minimo:
                    yc = (ini + r) / 2 / 2
                    res.append((p, round(yc, 1), round((r - ini) / 2, 1)))
                    d.line([(0, (ini + r) // 2), (60, (ini + r) // 2)], fill=(220, 0, 0), width=2)
                    d.text((64, (ini + r) // 2 - 5), '%d' % round(yc), fill=(220, 0, 0))
                ini = None
        if salida_png:
            im.resize((int(im.width * 0.7), int(im.height * 0.7))).save(salida_png % p)
    return res


def tiras_por_cortes(pdf, cortes, corte_titulo=None, pie=(), inicio=None, fin_=None):
    """cortes: {pag: [y, ...]} separadores (pt) entre sistemas consecutivos de esa pagina.
       corte_titulo: y en la pagina 1 por encima del cual solo hay titulo/autor.
       -> (P, tiras) con P[i]['ancho'] y tiras [dict(pag, ya, yb, sid, sys)]"""
    P, tiras, gid = [], [], 0
    for p in range(1, len(PdfReader(pdf).pages) + 1):
        t, w, h = _tinta(pdf, p)
        P.append(dict(pag=p, ancho=w, alto=h))
        cs = list(cortes.get(p, []))
        filas = t.any(1)
        ink = np.where(filas)[0]
        if not len(ink):
            continue
        tope = h - (0 if p in pie else 62)
        util = [r for r in ink if r / 2 <= tope]
        ini = (inicio or {}).get(p, max(0, ink.min() / 2 - 4))
        fin = min(h, (max(util) / 2 + 6) if util else h)
        if fin_ and p in fin_:
            fin = fin_[p]
        lim = [ini] + cs + [fin]
        if p == 1 and corte_titulo:
            tiras.append(dict(pag=1, ya=ini, yb=corte_titulo, sid=None, sys=None))
            lim = [corte_titulo] + cs + [fin]
        for a, b in zip(lim, lim[1:]):
            sub = t[int(a * 2):int(b * 2)]
            fi = np.where(sub.any(1))[0]
            co = np.where(sub.any(0))[0]
            if not len(fi):
                continue
            sysd = dict(top=a + fi.min() / 2, bot=a + (fi.max() + 1) / 2, left=(co.min() + 20) / 2)
            tiras.append(dict(pag=p, ya=a, yb=b, sid=gid, sys=sysd))
            gid += 1
    return P, tiras


# ------------------------------------------------------------ dibujo
def _lin(txt, w, font, size):
    out, cur = [], ''
    for pal in txt.split():
        t = (cur + ' ' + pal).strip()
        if stringWidth(t, font, size) > w and cur:
            out.append(cur)
            cur = pal
        else:
            cur = t
    if cur:
        out.append(cur)
    return out


LEAD = {'IZQ': (OCRE, 'MANO IZQUIERDA'), 'DER': (AZUL, 'MANO DERECHA'),
        'AMB': (NAVY, 'LAS DOS'), 'OJO': (ROJO, 'OJO'),
        'PRIMO': (AZUL, 'PRIMO'), 'SEC': (OCRE, 'SECONDO'), 'ESC': (VERDE, 'ESCUCHA')}


def burbuja(c, x, y, w, tipo, txt, cola='arriba', cx=None):
    """Burbuja: (x, y) esquina superior izquierda (y desde arriba)."""
    col, lead = LEAD[tipo]
    size = 6.9
    lin = _lin(txt, w - 14, 'DejaVuSans', size)
    h = 12 + 9.2 * (len(lin) + 1)
    x0, y0 = x, PAGE_H - y - h
    cx = cx if cx is not None else x + 16
    c.setFillColor(BLANCO)
    c.setStrokeColor(col)
    c.setLineWidth(0.9)
    c.roundRect(x0, y0, w, h, 5, fill=1, stroke=1)
    yb = y0 + h if cola == 'arriba' else y0
    ys = yb + 6 if cola == 'arriba' else yb - 6
    p = c.beginPath()
    p.moveTo(cx - 4, yb)
    p.lineTo(cx, ys)
    p.lineTo(cx + 4, yb)
    c.setFillColor(BLANCO)
    c.drawPath(p, fill=1, stroke=0)
    c.setStrokeColor(col)
    c.line(cx - 4, yb, cx, ys)
    c.line(cx + 4, yb, cx, ys)
    c.setStrokeColor(BLANCO)
    c.setLineWidth(1.4)
    c.line(cx - 3.2, yb, cx + 3.2, yb)
    c.setFont('DejaVuSans-Bold', 6.3)
    c.setFillColor(col)
    if tema_ca.ACTIU and tipo == 'OJO':
        tema_ca.buho(c, x0 + 5, PAGE_H - y - 12.5, 12, 'happy')
        c.drawString(x0 + 21, PAGE_H - y - 10.5, lead)
    else:
        c.drawString(x0 + 7, PAGE_H - y - 10.5, lead)
    c.setFont('DejaVuSans', size)
    c.setFillColor(NAVY)
    yy = PAGE_H - y - 10.5 - 9.4
    for l in lin:
        c.drawString(x0 + 7, yy, l)
        yy -= 9.2
    return h


def alto_burbuja(w, txt):
    return 12 + 9.2 * (len(_lin(txt, w - 14, 'DejaVuSans', 6.9)) + 1)


def marca(c, x, y, w, h, col, n, tipo='caja'):
    c.setStrokeColor(Color(col.red, col.green, col.blue, alpha=0.9))
    c.setLineWidth(1.0)
    x0, y0 = x - w / 2, PAGE_H - y - h / 2
    if tipo == 'ovalo':
        c.ellipse(x0, y0, x0 + w, y0 + h, stroke=1, fill=0)
    else:
        c.roundRect(x0, y0, w, h, 3, stroke=1, fill=0)
    cx, cy = x0 + w, y0 + h
    c.setFillColor(col)
    c.circle(cx, cy, 4.4, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSans-Bold', 6)
    c.drawCentredString(cx, cy - 2.1, str(n))


def margen(c, x, num, etq, col, top, bot):
    t, b = PAGE_H - top, PAGE_H - bot
    c.setStrokeColor(col)
    c.setLineWidth(1.3)
    c.line(x, b, x, t)
    c.line(x, t, x + 4, t)
    c.line(x, b, x + 4, b)
    c.setFillColor(col)
    c.circle(x - 8.5, t - 9, 7, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSerif-Bold', 9)
    c.drawCentredString(x - 8.5, t - 12.1, str(num))
    c.saveState()
    c.setFillColor(col)
    c.setFont('DejaVuSans-Bold', 6.2)
    c.translate(x - 5.5, t - 20)
    c.rotate(-90)
    c.drawString(0, 0, etq)
    c.restoreState()


# ------------------------------------------------------------ score
GAP = 6
DX = 20.0


def disponer(tiras, burb, esc_pag):
    """Reparte tiras (+ su banda de burbujas) en paginas nuevas -> [[(tira, y0, ban_a, ban_b)]]"""
    paginas, cur, y = [], [], 30
    cap = 30 + (842 - 30 - 34)
    for t in tiras:
        s = esc_pag[t['pag']]
        bs = burb.get(t['sid'], []) if t['sid'] is not None else []
        aa = max([alto_burbuja(w, tx) for (st, w, tp, tx, cx) in bs if st == 'arriba'] or [0])
        ab = max([alto_burbuja(w, tx) for (st, w, tp, tx, cx) in bs if st == 'abajo'] or [0])
        ban_a = aa + 9 if aa else 0
        ban_b = ab + 9 if ab else 0
        total = ban_a + (t['yb'] - t['ya']) * s + ban_b + GAP
        if cur and y + total > cap:
            paginas.append(cur)
            cur, y = [], 30
        cur.append((t, y + ban_a, ban_a, ban_b))
        y += total
    paginas.append(cur)
    return paginas


def montar_partitura(spec, salida, num0):
    """PDF con la partitura recolocada y anotada. Devuelve (n_paginas, tiras)."""
    if CONTINUA:
        return montar_partitura_continua(spec, salida, num0)
    import pymupdf
    pdf = os.path.join(SRCDIR, spec['pdf'])
    P, tiras = tiras_por_cortes(pdf, spec['cortes'], spec.get('corte_titulo'), spec.get('pie', ()),
                                  spec.get('inicio'), spec.get('fin'))
    esc = {i: (PAGE_W - 24) / pg['ancho'] for i, pg in enumerate(P, 1)}
    pags = disponer(tiras, spec.get('burb', {}), esc)
    src = pymupdf.open(pdf)
    nuevo = pymupdf.open()
    for lista in pags:
        pg = nuevo.new_page(width=PAGE_W, height=PAGE_H)
        for (t, y0, ba, bb) in lista:
            s = esc[t['pag']]
            ancho_src = P[t['pag'] - 1]['ancho']
            pg.show_pdf_page(pymupdf.Rect(DX, y0, DX + ancho_src * s, y0 + (t['yb'] - t['ya']) * s), src,
                             t['pag'] - 1, clip=pymupdf.Rect(0, t['ya'], ancho_src, t['yb']))
    tmp = salida + '.base.pdf'
    nuevo.save(tmp)
    base = PdfReader(tmp)
    wr = PdfWriter()
    for i, lista in enumerate(pags):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))
        _anotar(c, spec, lista, esc, P, num0 + i)
        c.save()
        buf.seek(0)
        pg = base.pages[i]
        pg.merge_page(PdfReader(buf).pages[0])
        wr.add_page(pg)
    with open(salida, 'wb') as f:
        wr.write(f)
    os.remove(tmp)
    return len(pags)


# ------------------------------------------------------------ partitura CONTINUA (sense tallar en tires)
CONTINUA = ALUMNA in ('eva', 'sharifa', 'abril', 'alba', 'txell') and os.environ.get('PARTITURA', 'continua') != 'tiras'
ML_C = 30.0                 # marge esquerre: parentesi de bloc i numero
MAX_ESC_C = 1.12            # escala maxima de la partitura (a tot l'ample; les indicacions van a sota)


def nota_marge(c, x, y, w, lletra, tipo, txt):
    """Indicacio al marge dret: caixa amb la lletra-marca, el tipus (mA esquerra...) i el text. y des de dalt. -> alt."""
    col, lead = LEAD[tipo]
    size = 6.7
    lin = _lin(txt, w - 14, 'DejaVuSans', size)
    h = 15 + 8.8 * len(lin) + 3
    x0, y0 = x, PAGE_H - y - h
    c.setFillColor(BLANCO)
    c.setStrokeColor(col)
    c.setLineWidth(0.9)
    c.roundRect(x0, y0, w, h, 4, fill=1, stroke=1)
    c.setFillColor(col)
    c.circle(x0 + 9, PAGE_H - y - 8.5, 4.6, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSans-Bold', 6.2)
    c.drawCentredString(x0 + 9, PAGE_H - y - 10.6, lletra)
    c.setFillColor(col)
    c.setFont('DejaVuSans-Bold', 6.1)
    if tema_ca.ACTIU and tipo == 'OJO':
        tema_ca.buho(c, x0 + 16, PAGE_H - y - 12.2, 10, 'happy')
        c.drawString(x0 + 28, PAGE_H - y - 10.6, lead)
    else:
        c.drawString(x0 + 17, PAGE_H - y - 10.6, lead)
    c.setFont('DejaVuSans', size)
    c.setFillColor(NAVY)
    yy = PAGE_H - y - 20.5
    for l in lin:
        c.drawString(x0 + 7, yy, l)
        yy -= 8.8
    return h


def marca_punt(c, x, y, col, lletra):
    c.setFillColor(col)
    c.circle(x, PAGE_H - y, 5.4, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSans-Bold', 7.4)
    c.drawCentredString(x, PAGE_H - y - 2.6, lletra)


def _items_pagina(spec, sy):
    """Indicacions de la pagina en ordre: [(k_sistema, tipus, text, cx)]."""
    out = []
    for k, t in enumerate(sy):
        for (st, w_, tp, tx, cx) in spec.get('burb', {}).get(t['sid'], []):
            out.append((k, tp, tx, cx))
    return out


def _banda(items, ancho):
    """Reparteix les indicacions en files de fins a 3 columnes. -> (cw, files[[idx...]], alts[idx], alt_total)"""
    n = len(items)
    if n == 0:
        return 0, [], [], 0.0
    nc = 3 if ancho > 380 else 2
    nc = min(nc, n) if n > 1 else 1
    if n == 1:
        nc = 1
    cw = (ancho - (nc - 1) * 8) / nc if n > 1 else min(ancho, 270.0)
    alts = [15 + 8.8 * len(_lin(tx, cw - 14, 'DejaVuSans', 6.7)) + 3 for (k, tp, tx, cx) in items]
    files, tot = [], 0.0
    for r in range(0, n, nc):
        fila = list(range(r, min(r + nc, n)))
        files.append(fila)
        tot += max(alts[j] for j in fila) + 6
    return cw, files, alts, tot


def montar_partitura_continua(spec, salida, num0):
    """La partitura de Drive TAL COM ES (una pagina per pagina), a tot l'ample, amb els trams com a parentesis al marge
       esquerre i les indicacions en una banda sota la partitura; cada indicacio porta una lletra repetida en un punt
       de la partitura. Retorna el nombre de pagines."""
    import pymupdf
    pdf = os.path.join(SRCDIR, spec['pdf'])
    P, tiras = tiras_por_cortes(pdf, spec['cortes'], spec.get('corte_titulo'), spec.get('pie', ()),
                                  spec.get('inicio'), spec.get('fin'))
    src = pymupdf.open(pdf)
    nuevo = pymupdf.open()
    info = []
    ancho_util = PAGE_W - 22.0 - ML_C
    for pg_no in range(1, len(P) + 1):
        sy = [t for t in tiras if t['pag'] == pg_no and t['sid'] is not None]
        if not sy:
            continue
        ya, yb = sy[0]['ya'], sy[-1]['yb']
        t, wpt, hpt = _tinta(pdf, pg_no)
        sub = t[int(ya * 2):int(yb * 2)]
        co = np.where(sub.any(0))[0]
        x0 = max(0.0, (co.min() + 20) / 2.0 - 3)
        x1 = min(wpt, (co.max() + 20) / 2.0 + 3)
        items = _items_pagina(spec, sy)
        cw, files, alts, alt_banda = _banda(items, ancho_util)
        ytop = 36.0
        lib = 806.0 - ytop - (alt_banda + 16 if items else 0)
        s = min(ancho_util / (x1 - x0), MAX_ESC_C, lib / (yb - ya))
        wout = (x1 - x0) * s
        pg = nuevo.new_page(width=PAGE_W, height=PAGE_H)
        pg.show_pdf_page(pymupdf.Rect(ML_C, ytop, ML_C + wout, ytop + (yb - ya) * s), src, pg_no - 1,
                         clip=pymupdf.Rect(x0, ya, x1, yb))
        info.append(dict(pag=pg_no, ya=ya, yb=yb, x0=x0, s=s, wout=wout, ytop=ytop, sy=sy, ancho=P[pg_no - 1]['ancho'],
                         items=items, cw=cw, files=files, alts=alts))
    tmp = salida + '.base.pdf'
    nuevo.save(tmp)
    base = PdfReader(tmp)
    wr = PdfWriter()
    for i, I in enumerate(info):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))
        _anotar_continua(c, spec, I, num0 + i)
        c.save()
        buf.seek(0)
        pg = base.pages[i]
        pg.merge_page(PdfReader(buf).pages[0])
        wr.add_page(pg)
    with open(salida, 'wb') as f:
        wr.write(f)
    os.remove(tmp)
    return len(info)


def _anotar_continua(c, spec, I, n):
    s, ya, x0, ML, ytop = I['s'], I['ya'], I['x0'], ML_C, I['ytop']
    sy = I['sy']
    G = []
    for t in sy:
        g = t['sys']
        top = max(ytop + (g['top'] - 2 - ya) * s, ytop - 2)
        bot = min(ytop + (g['bot'] + 4 - ya) * s, ytop + (I['yb'] - ya) * s)
        G.append(dict(t=t, top=top, bot=bot, left=ML + (g['left'] - x0) * s, gl=g['left']))
    segs = []
    for k, d in enumerate(G):
        b = _bloque_de(spec, d['t']['sid'])
        if segs and segs[-1][0] is b and abs(segs[-1][2] - d['top']) < 45:
            segs[-1][2] = d['bot']
        else:
            segs.append([b, d['top'], d['bot'], d['t']['sid'] == b['sist'][0]])
    xb = ML - 7
    for b, top, bot, primero in segs:
        col = b['color']
        c.setFillColor(Color(col.red, col.green, col.blue, alpha=0.055))
        c.roundRect(xb + 3, PAGE_H - bot, ML + I['wout'] - xb - 3, bot - top, 4, fill=1, stroke=0)
        margen(c, xb, b['num'], b['cc'] if primero else 'sigue', col, top, bot)
    for (pg_o, x, y, w, h, bn_, k, tipo) in spec.get('marcas', []):
        if pg_o == I['pag'] and I['ya'] <= y <= I['yb']:
            col = [q for q in spec['bloques'] if q['num'] == bn_][0]['color']
            f = s / ((PAGE_W - 24) / I['ancho'])          # w i h estan pensats per a l'escala antiga
            marca(c, ML + (x - x0) * s, ytop + (y - ya) * s, w * f, h * f, col, k, tipo)
    # banda d'indicacions sota la partitura
    items, cw, files, alts = I['items'], I['cw'], I['files'], I['alts']
    letras = 'abcdefghijklmnopqrstuvwxyz'
    ybanda = ytop + (I['yb'] - ya) * s + 14
    usados = []
    for fila in files:
        hfila = max(alts[j] for j in fila)
        for pos, j in enumerate(fila):
            k, tp, tx, cx = items[j]
            col = LEAD[tp][0]
            lt = letras[j % len(letras)]
            nota_marge(c, ML + pos * (cw + 8), ybanda, cw, lt, tp, tx)
            d = G[k]
            gx = (d['gl'] + cx * (I['ancho'] - 30 - d['gl'])) if cx <= 1.0 else cx
            px = min(max(ML + (gx - x0) * s, ML + 6), ML + I['wout'] - 6)
            prev_bot = G[k - 1]['bot'] if k > 0 else ytop - 14
            next_top = G[k + 1]['top'] if k + 1 < len(G) else ytop + (I['yb'] - ya) * s + 14
            if d['top'] - prev_bot >= 12:
                py = d['top'] - 5.5
            elif next_top - d['bot'] >= 12:
                py = d['bot'] + 5.5
            else:
                py, px = (d['top'] + d['bot']) / 2.0, ML + I['wout'] + 4
            while any(abs(px - qx) < 10 and abs(py - qy) < 8 for qx, qy in usados):
                px += 10
                if px > ML + I['wout'] - 4:
                    px, py = ML + I['wout'] + 4, py + 10
            usados.append((px, py))
            marca_punt(c, px, py, col, lt)
        ybanda += hfila + 6
    c.setFont('DejaVuSans', 6.4)
    c.setFillColor(MUTED)
    c.drawString(34, 22, spec.get('credito', ''))
    c.drawRightString(561, 22, str(n))


def _bloque_de(spec, sid):
    for b in spec['bloques']:
        if b['sist'][0] <= sid <= b['sist'][1]:
            return b
    return None


def _anotar(c, spec, lista, esc, P, n):
    segs = []
    for (t, y0, ba, bb) in lista:
        if t['sid'] is None:
            continue
        s = esc[t['pag']]
        g = t['sys']
        b = _bloque_de(spec, t['sid'])
        top = max(y0 + (g['top'] - 2 - t['ya']) * s, y0 - 2)
        bot = min(y0 + (g['bot'] + 4 - t['ya']) * s, y0 + (t['yb'] - t['ya']) * s)
        xb = max(11.0, DX + g['left'] * s - 9)
        if segs and segs[-1][0] is b and abs(segs[-1][2] - top) < 45 and abs(segs[-1][4] - xb) < 3:
            segs[-1][2] = bot
        else:
            segs.append([b, top, bot, t['sid'] == b['sist'][0], xb, t['pag']])
    for b, top, bot, primero, xb, pg_o in segs:
        col = b['color']
        x_ini = xb + 3
        c.setFillColor(Color(col.red, col.green, col.blue, alpha=0.055))
        c.roundRect(x_ini, PAGE_H - bot, PAGE_W - 22 - x_ini, bot - top, 4, fill=1, stroke=0)
        margen(c, xb, b['num'], b['cc'] if primero else 'sigue', col, top, bot)
    for (pg_o, x, y, w, h, bn, k, tipo) in spec.get('marcas', []):
        for (t, y0, ba, bb) in lista:
            if t['pag'] == pg_o and t['ya'] <= y <= t['yb']:
                s = esc[pg_o]
                col = [q for q in spec['bloques'] if q['num'] == bn][0]['color']
                marca(c, DX + x * s, y0 + (y - t['ya']) * s, w, h, col, k, tipo)
    for (t, y0, ba, bb) in lista:
        bs = spec.get('burb', {}).get(t['sid'], []) if t['sid'] is not None else []
        s = esc[t['pag']]
        xa = xb_ = 24
        for (st, w, tp, tx, cx) in bs:
            if cx <= 1.0:
                g = t['sys']
                cx = g['left'] + cx * (P[t['pag'] - 1]['ancho'] - 30 - g['left'])
                cx = cx
            cxx = DX + cx * s
            if st == 'arriba':
                burbuja(c, xa, y0 - ba + 4, w, tp, tx, 'abajo', min(max(cxx, xa + 12), xa + w - 12))
                xa += w + 10
            else:
                burbuja(c, xb_, y0 + (t['yb'] - t['ya']) * s + 10, w, tp, tx, 'arriba',
                        min(max(cxx, xb_ + 12), xb_ + w - 12))
                xb_ += w + 10
    c.setFont('DejaVuSans', 6.4)
    c.setFillColor(MUTED)
    c.drawString(34, 22, spec.get('credito', ''))
    c.drawRightString(561, 22, str(n))


# ------------------------------------------------------------ paginas de estudio
def marco(c, kicker, derecha, n):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(18, H - 24, W - 36, 6, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, H - 44, kicker.upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, H - 44, derecha)
    c.setFont('DejaVuSans', 7.4)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(n))


def titulo_pag(c, t, sub):
    y = H - 76
    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, t)
    return _wrap(c, sub, MARGIN, y - 16, 'DejaVuSans', 9.4, CONTENT_W, 12.6, MUTED)


def _columna(c, x, y, ancho, tit, color, pasos):
    c.setFillColor(color)
    c.roundRect(x, y - 30, ancho, 30, 5, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSerif-Bold', 13)
    c.drawString(x + 14, y - 20, tit)
    y -= 44
    for i, (t, txt) in enumerate(pasos, 1):
        alto = 104 if tema_ca.ACTIU else 118
        c.setFillColor(PANEL)
        c.roundRect(x, y - alto, ancho, alto, 5, fill=1, stroke=0)
        c.setFillColor(color)
        c.rect(x, y - alto, 3, alto, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 34)
        c.setFillColor(GRIS)
        c.drawString(x + 14, y - 38, str(i))
        c.setFont('DejaVuSerif-Bold', 10.5)
        c.setFillColor(NAVY)
        c.drawString(x + 42, y - 30, t)
        _wrap(c, txt, x + 14, y - 54, 'DejaVuSans', 8.6, ancho - 28, 11.8, INK)
        y -= alto + 10
    return y


def pagina_manos(c, spec, n):
    m = spec['manos']
    marco(c, spec['kicker'], 'Cómo estudiarla', n)
    y = titulo_pag(c, m.get('titulo', 'Mano izquierda y mano derecha'),
                   m.get('sub', 'Cada mano se aprende sola. Las dos juntas llegan al final, '
                                'despacio.'))
    y -= 18
    ancho = (CONTENT_W - 16) / 2
    ya = _columna(c, MARGIN, y, ancho, m.get('tit_izq', 'MANO IZQUIERDA'), OCRE, m['izq'])
    _columna(c, MARGIN + ancho + 16, y, ancho, m.get('tit_der', 'MANO DERECHA'), AZUL, m['der'])
    y = ya - 4
    tec = m.get('tecnica', ['Muñeca suelta y hombros bajos: si te cansas, estás apretando.',
                            'Dedos curvos, cerca de las teclas, sonido ligero y parejo.',
                            'Cuenta en voz alta los golpes y no pares cuando cambie algo.'])
    h = 30 + 13 * len(tec)
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawString(MARGIN + 16, y - 16, 'LA TÉCNICA, EN %s' % {2: 'DOS', 3: 'TRES', 4: 'CUATRO'}.get(
        len(tec), str(len(tec))) + (' FRASES' if len(tec) > 1 else ' FRASE'))
    yy = y - 31
    for s in tec:
        c.setFillColor(NAVY)
        c.circle(MARGIN + 19, yy + 3, 1.8, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('DejaVuSans', 8.6)
        c.drawString(MARGIN + 28, yy, s)
        yy -= 13
    tip = (spec.get('misol') or {}).get('manos', MISOL_DEF['manos'])
    if tema_ca.ACTIU and tip and y - h - 14 - tema_ca.alto_caixa_misol(CONTENT_W, tip) > 48:
        tema_ca.caixa_misol(c, MARGIN, y - h - 14, CONTENT_W, tip, pose='normal')
    c.showPage()


MISOL_DEF = dict(
    manos="Tens pressa? Ni cas! Una mà cada cop, molt a poc a poc: el cervell necessita temps per "
          "ensenyar als dits el camí.",
    guia="Quan un bloc et surti tres cops seguits sense fallar, ja el tens. Si falles, torna "
         "enrere un compàs, no al principi!",
    pauta="Aquí ets tu la compositora! Copia un compàs que t'agradi o inventa'n un de nou. "
          "Cada nota que escrius és música teva.")


# diagramas de la guia ------------------------------------------------------
def dots(c, x, y, n, col, r=2.1, sep=5.6):
    c.setFillColor(col)
    for i in range(n):
        c.circle(x + i * sep, y, r, fill=1, stroke=0)


def grupos(c, x, y, ng, por, col, rot=None, r=2.0, sep=5.0, hueco=7, h=11):
    for g in range(ng):
        w = (por - 1) * sep + 10
        c.setFillColor(BLANCO)
        c.setStrokeColor(col)
        c.setLineWidth(0.8)
        c.roundRect(x, y - h / 2, w, h, 3, fill=1, stroke=1)
        dots(c, x + 5, y, por, col, r, sep)
        if rot:
            c.setFont('DejaVuSans', 6)
            c.setFillColor(MUTED)
            c.drawCentredString(x + w / 2, y - h / 2 - 7, rot[g] if isinstance(rot, list) else rot)
        x += w + hueco
    return x


def chip(c, x, y, txt, col, size=7.4, relleno=False):
    w = stringWidth(txt, 'DejaVuSans-Bold', size) + 12
    if relleno:
        c.setFillColor(col)
        c.roundRect(x, y - 7, w, 14, 7, fill=1, stroke=0)
        c.setFillColor(BLANCO)
    else:
        c.setFillColor(BLANCO)
        c.setStrokeColor(col)
        c.setLineWidth(0.9)
        c.roundRect(x, y - 7, w, 14, 7, fill=1, stroke=1)
        c.setFillColor(col)
    c.setFont('DejaVuSans-Bold', size)
    c.drawString(x + 6, y - 2.4, txt)
    return x + w


def flecha(c, x, y, col, largo=12):
    c.setStrokeColor(col)
    c.setFillColor(col)
    c.setLineWidth(1)
    c.line(x, y, x + largo - 3, y)
    p = c.beginPath()
    p.moveTo(x + largo, y)
    p.lineTo(x + largo - 4, y + 2.6)
    p.lineTo(x + largo - 4, y - 2.6)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    return x + largo + 4


def etq(c, x, y, txt, col=MUTED, size=6.6):
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(col)
    c.drawString(x, y, txt)


def diagrama(c, x, y, col, d):
    """d = (tipo, titulo, datos). Tipos: grupos, cadena, capas, cuenta, nota."""
    tipo, tit, dat = d
    etq(c, x, y + 13, tit.upper())
    if tipo == 'grupos':               # (n_grupos, por_grupo, [etiquetas])
        ng, por, rot = dat
        grupos(c, x, y - 4, ng, por, col, rot)
    elif tipo == 'cadena':             # [(texto, relleno)]
        xx = x
        for k, (t, r) in enumerate(dat):
            xx = chip(c, xx, y - 1, t, col, 7, relleno=r)
            if k < len(dat) - 1:
                xx = flecha(c, xx + 2, y - 1, col, 9)
    elif tipo == 'fichas':             # [texto] sin flechas
        xx = x
        for t in dat:
            xx = chip(c, xx, y - 1, t, col, 7) + 3
    elif tipo == 'capas':              # [(etiqueta, 'barras'|'puntos', color)]
        for i, it in enumerate(dat):
            t, k, cc = it[:3]
            nd = it[3] if len(it) > 3 else 6
            yy = y - 1 - i * 10
            c.setFont('DejaVuSans', 6)
            c.setFillColor(MUTED)
            c.drawString(x, yy - 2, t)
            xx = x + 84
            for q in range(4):
                if k == 'barras':
                    c.setFillColor(cc)
                    c.roundRect(xx + q * 40, yy - 3, 34, 6, 3, fill=1, stroke=0)
                else:
                    dots(c, xx + q * 40, yy, nd, cc, 1.6, min(5.4, 30.0 / max(nd - 1, 1)))
    elif tipo == 'cuenta':             # [(rotulo, n_grupos, por_grupo)]
        xx = x
        for t, ng, por in dat:
            c.setFont('DejaVuSans-Bold', 6.4)
            c.setFillColor(col)
            c.drawString(xx, y - 14, t)
            xx = grupos(c, xx, y - 2, ng, por, col, None, 2.0, 5.0, 4, 10) + 10
    elif tipo == 'nota':               # texto corto en una linea, con chip
        c.setFont('DejaVuSans', 7.4)
        c.setFillColor(INK)
        c.drawString(x, y - 3, dat)


COL_PASO = {'IZQUIERDA': OCRE, 'DERECHA': AZUL, 'JUNTAS': NAVY, 'A TEMPO': VERDE, 'OJO': ROJO,
            'PRIMO': AZUL, 'SECONDO': OCRE, 'LOS DOS': NAVY}


def tarjeta(c, y, b):
    col = b['color']
    alto = 142
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - alto, CONTENT_W, alto, 5, fill=1, stroke=0)
    c.setFillColor(col)
    c.rect(MARGIN, y - alto, 4, alto, fill=1, stroke=0)
    c.circle(MARGIN + 24, y - 20, 11, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSerif-Bold', 13)
    c.drawCentredString(MARGIN + 24, y - 24.5, str(b['num']))
    c.setFillColor(NAVY)
    c.setFont('DejaVuSerif-Bold', 12)
    c.drawString(MARGIN + 44, y - 24, b['cc'])
    c.setFont('DejaVuSans', 10)
    c.setFillColor(INK)
    c.drawString(MARGIN + 44 + stringWidth(b['cc'], 'DejaVuSerif-Bold', 12) + 10, y - 24, b['nombre'])
    diagrama(c, MARGIN + 16, y - 56, col, b['diag'])
    pasos = b['pasos']
    ancho = (CONTENT_W - 32 - 3 * 10) / 4
    for i, (p, t) in enumerate(pasos):
        x = MARGIN + 16 + i * (ancho + 10)
        c.setFillColor(COL_PASO.get(p, NAVY))
        c.rect(x, y - 84, ancho, 2, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 7)
        c.drawString(x, y - 96, p)
        _wrap(c, t, x, y - 108, 'DejaVuSans', 7.8, ancho, 9.8, INK)
    return y - alto - 10


LISTA_DEF = ['Toco de memoria la mano izquierda de los primeros bloques.',
             'Cuento los golpes y no me pierdo cuando algo cambia.',
             'Sé por dónde voy en la partitura, también en las repeticiones.',
             'Toco la pieza entera, de principio a fin, sin parar.',
             'La grabo con el móvil y la escucho.']


def paginas_guia(c, spec, n0):
    bl = spec['bloques']
    k = 0
    pagina = 0
    while k < len(bl) or pagina == 0:
        marco(c, spec['kicker'], 'Guía por bloques', n0 + pagina)
        if pagina == 0:
            y = titulo_pag(c, 'Cómo tocar cada bloque',
                           spec.get('sub_guia', 'Cada bloque, en el mismo orden: izquierda, derecha, '
                                                'juntas y a tempo.')) - 14
        else:
            y = H - 76
        for b in bl[k:k + 4]:
            y = tarjeta(c, y, b)
            k += 1
        if k >= len(bl):
            items = spec.get('lista', LISTA_DEF)
            h = 40 + 22 * len(items)
            if y - h > 48:
                y -= 14
                c.setFillColor(PANEL)
                c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
                c.setFillColor(NAVY)
                c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
                c.setFont('DejaVuSans-Bold', 8.4)
                c.drawString(MARGIN + 18, y - 22, 'ANTES DE DECIR «YA LA SÉ»')
                yy = y - 46
                for t in items:
                    c.setStrokeColor(NAVY)
                    c.setLineWidth(1)
                    c.roundRect(MARGIN + 18, yy - 3, 11, 11, 2, fill=0, stroke=1)
                    c.setFillColor(INK)
                    c.setFont('DejaVuSans', 9.4)
                    c.drawString(MARGIN + 38, yy, t)
                    yy -= 22
                tip = (spec.get('misol') or {}).get('guia', MISOL_DEF['guia'])
                if tema_ca.ACTIU and tip and yy - 14 - tema_ca.alto_caixa_misol(CONTENT_W, tip) > 44:
                    tema_ca.caixa_misol(c, MARGIN, yy - 8, CONTENT_W, tip, pose='happy')
        c.showPage()
        pagina += 1
    return pagina


# ------------------------------------------------------------ pieza completa
def _qr(url, ruta):
    segno.make(url, error='m').save(ruta, scale=10, border=2, dark='#1A2332', light='#F3F1EA')


def construir_pieza(spec, num_pag0):
    """-> (PdfWriter con las paginas, n_paginas). num_pag0: numero de la primera pagina."""
    os.makedirs(OUT, exist_ok=True)
    slug = spec['slug']
    kicker = spec['kicker']
    # 1) ficha
    qr = os.path.join(OUT, '_qr_%s.png' % slug)
    _qr(spec['yt'], qr)
    cfg = dict(spec['ficha'])
    cfg.update(kicker=kicker, page_num=num_pag0, time_sig=spec['time_sig'],
               qr=dict(cfg['qr'], png=qr))
    cfg['titulo'] = spec['titulo']
    cfg['autor'] = spec['autor']
    cfg['misol_buho'] = tema_ca.ACTIU
    f1 = os.path.join(OUT, '_f_%s.pdf' % slug)
    c = canvas.Canvas(f1, pagesize=(W, H))
    build_ficha(c, cfg)
    c.save()
    os.remove(qr)
    # 2) manos + guia
    f2 = os.path.join(OUT, '_g_%s.pdf' % slug)
    c = canvas.Canvas(f2, pagesize=(W, H))
    pagina_manos(c, spec, num_pag0 + 1)
    ng = paginas_guia(c, spec, num_pag0 + 2)
    c.save()
    # 3) partitura
    f3 = os.path.join(OUT, '_s_%s.pdf' % slug)
    ns = montar_partitura(spec, f3, num_pag0 + 2 + ng)
    # DUETS A QUATRE MANS: les dues pagines de la partitura han de quedar ENFRONTADES (comencen en pagina parell);
    # si no, s'intercala davant una fulla de paper pautat
    duo = spec.get('duo', any(k in spec['pdf'] for k in ('4_manos', 'bela_ciao', 'beginner')))
    extra = 1 if (duo and ns >= 2 and (num_pag0 + 2 + ng) % 2 == 1) else 0
    f2b = None
    if extra:
        ns = montar_partitura(spec, f3, num_pag0 + 2 + ng + 1)
        f2b = os.path.join(OUT, '_e_%s.pdf' % slug)
        c = canvas.Canvas(f2b, pagesize=(W, H))
        build_pauta(c, dict(kicker=kicker, page_num=num_pag0 + 2 + ng, titulo_pauta='Per escriure',
                            misol=None, pie_pauta='espai per apuntar passos, digitació o els compassos que us costen · '
                                                  'la partitura del duet s\'obre a la pàgina següent'))
        c.save()
    total = 1 + 1 + ng + extra + ns
    # 4) pauta (una, o dos si hace falta que la pieza ocupe un numero PAR de hojas)
    npau = 1 if (total + 1) % 2 == 0 else 2
    f4 = os.path.join(OUT, '_p_%s.pdf' % slug)
    c = canvas.Canvas(f4, pagesize=(W, H))
    for i in range(npau):
        build_pauta(c, dict(kicker=kicker, page_num=num_pag0 + total + i,
                            titulo_pauta='Para escribir',
                            misol=((spec.get('misol') or {}).get('pauta', MISOL_DEF['pauta'])
                                   if tema_ca.ACTIU and i == npau - 1 else None),
                            pie_pauta=spec.get('pie_pauta', 'la clave la pones tú · copia un compás '
                                                            'o inventa algo')))
    c.save()
    wr = PdfWriter()
    for f in (f1, f2, f2b, f3, f4):
        if f is None:
            continue
        for p in PdfReader(f).pages:
            wr.add_page(p)
        os.remove(f)
    return wr, total + npau


# ------------------------------------------------------------ ayudas para escribir piezas
def B(num, cc, nombre, sist, diag, pasos):
    return dict(num=num, cc=cc, nombre=nombre, sist=sist, diag=diag, pasos=pasos,
                color=COLORES_BLOQUE[(num - 1) % len(COLORES_BLOQUE)])


def cuenta_compas(ts, pitch='B4'):
    """Un compas del metro dado, contado en golpes. 3/4 y 4/4 y 2/4 en corcheas (2 por golpe);
       6/8, 9/8, 12/8 en grupos de tres corcheas. Solo teoria del compas, no alturas medidas."""
    n, d = ts
    ev = []
    if d == 8:
        for g in range(n // 3):
            ev += [{'pitch': pitch, 'dur': 'e', 'beam': g} for _ in range(3)]
    else:
        for g in range(n):
            ev += [{'pitch': pitch, 'dur': 'e', 'beam': g} for _ in range(2)]
    return ev


def FICHA(datos, secciones, total, ideas, especial, reto, truco, sabias, qr_texto, ts,
          ideas_titulo='La pieza en cuatro ideas', ideas_pie='', cuenta_titulo=None,
          cuenta_pie=None, cuenta_rotulo=None, clave='treble', ritmos=None):
    cuenta_titulo = cuenta_titulo or 'Cómo se cuenta el %d/%d' % ts
    if cuenta_pie is None:
        cuenta_pie = ('Un compás de %d/%d contado en corcheas. Aquí solo el ritmo, sobre una nota '
                      'cualquiera: las alturas, en tu partitura.' % ts)
    return dict(
        datos=datos, total_compases=total, secciones=secciones,
        armonia=dict(titulo=ideas_titulo, tarjetas=ideas, pie=ideas_pie),
        titulo_ritmos=cuenta_titulo, pie_ritmos=cuenta_pie,
        ritmos=ritmos or [(cuenta_rotulo or 'LA CUENTA', '%d/%d' % ts, cuenta_compas(ts), OCRE,
                           clave, None)],
        especial=especial, reto=reto, truco=truco, sabias=sabias,
        qr=dict(titulo='Escúchala', texto=qr_texto))


def D(t, *a):
    return (t, *a)
