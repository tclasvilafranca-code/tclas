# -*- coding: utf-8 -*-
"""Les fulles del LLIBRE DE PEKES: l'aspecte dels albums d'alumne, a mida de
   nen petit.

   Peticio del client sobre la mostra anterior (que ja anava amb el motor dels
   albums): "mucho mas visual, la letra mas grande porque son pequenitos y
   saben leer pero hay que facilitarselo", i les fitxes de casa "mas
   dinamicas, tipo relacionar, pintar y contar, con todo lo que ya saben los
   ninos, como los colores de las notas".

   No es un disseny nou: es la mateixa capcalera (franja blau nit, kicker,
   titol en serifa, la banda de regles), els mateixos recuadres (fons calid
   amb filet ocre, fons de panell amb filet blau), les mateixes targetes i el
   mateix motor de pentagrames. El que canvia:

   - TOT mes gran: titol 32, text 12, pentagrames amb mes espai entre linies.
   - Exercicis de fitxa nous, pensats per a nens que encara llegeixen a poc
     a poc: pintar amb el codi de colors, relacionar nota amb tecla, comptar,
     i un laberint per ajudar en Mussol Misol.
   - Cada pagina es MESURA abans de dibuixar-la: si el contingut no hi cap,
     peta amb un error que diu quant sobra, en comptes de sortir-se pel peu.
"""
import io
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen.canvas import Canvas

from notation import (draw_staff, draw_clef, draw_note, note_y, BLEED_SAFE)
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit)
from hoja_piano import _lineas
from misol import dibujar_buho

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')

SUELO = 50.0          # per sota d'aixo es trepitja el peu
OBJECTIU = 70.0       # on es vol que acabi una fulla justificada
AIRE_MAX = 22.0

# el codi de colors del curs (el mateix del Canva original del client)
COLORS = {'DO': 'vermell', 'RE': 'taronja', 'MI': 'groc', 'FA': 'verd',
          'SOL': 'blau', 'LA': 'lila', 'SI': 'gris'}
NOM = {'C': 'DO', 'D': 'RE', 'E': 'MI', 'F': 'FA', 'G': 'SOL', 'A': 'LA', 'B': 'SI'}
BLANQUES = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
NEGRA_DESPRES = {0, 1, 3, 4, 5}


# --------------------------------------------------------------------------
# peces petites
# --------------------------------------------------------------------------
def _linies(text, font, size, ample):
    out, linia = [], ''
    for mot in text.split():
        prova = (linia + ' ' + mot).strip()
        if stringWidth(prova, font, size) <= ample:
            linia = prova
        else:
            if linia:
                out.append(linia)
            linia = mot
    if linia:
        out.append(linia)
    return out or ['']


def _wrap(c, text, x, y, font, size, ample, interlinia, color):
    c.setFont(font, size)
    c.setFillColor(color)
    for linia in _linies(text, font, size, ample):
        c.drawString(x, y, linia)
        y -= interlinia
    return y


def _titol_seccio(c, y, text):
    c.setFont('DejaVuSans-Bold', 11)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y - 11, text.upper())
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.6)
    c.line(MARGIN, y - 18, MARGIN + 26, y - 18)
    return y - 32


def _encap(c, y, num, titol, pista=None):
    """La capcalera d'un exercici: la casella ocre amb el numero i el titol,
       com als albums, pero a mida de nen."""
    c.setFillColor(ACCENT)
    c.roundRect(MARGIN, y - 22, 22, 22, 4, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 12.5)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 11, y - 15.6, str(num))
    tsize = _fit(titol, 'DejaVuSans-Bold', 14, CONTENT_W - 32, floor=11)
    c.setFont('DejaVuSans-Bold', tsize)
    c.setFillColor(INK)
    c.drawString(MARGIN + 32, y - 16, titol)
    y -= 26
    if pista:
        y = _wrap(c, pista, MARGIN + 32, y - 9, 'DejaVuSans', 10.5, CONTENT_W - 32,
                  13.5, MUTED) - 2
    return y - 4


def _caixeta(c, x, y, w, h):
    c.setStrokeColor(NAVY_SOFT)
    c.setLineWidth(1.0)
    c.setFillColor(white)
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)


def _rodoneta(c, cx, cy, r):
    """Un cercle buit per pintar: la llegenda de colors la pinta el nen."""
    c.setStrokeColor(NAVY_SOFT)
    c.setLineWidth(1.2)
    c.setFillColor(white)
    c.circle(cx, cy, r, fill=1, stroke=1)


def _llegenda(c, y, notes, x0=None, ample=None):
    """DO = vermell · RE = taronja... amb una rodoneta buida per pintar."""
    x0 = MARGIN if x0 is None else x0
    ample = CONTENT_W if ample is None else ample
    pas = ample / float(len(notes))
    for i, n in enumerate(notes):
        cx = x0 + i * pas + 12
        _rodoneta(c, cx, y - 9, 9)
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(INK)
        c.drawString(cx + 15, y - 13, '%s = %s' % (n, COLORS[n]))
    return y - 26


def _teclat(c, x, y_top, n, kw, kh, noms=True, inici=0, marques=None,
            dits=None, punts=None, buides=False):
    """Un teclat a mida de nen. `marques` {i: color} pinta la tecla,
       `dits` {i: numero} posa el dit en un cercle, `punts` {i} hi posa un
       punt negre (la tecla que s'ha de trobar)."""
    marques = marques or {}
    dits = dits or {}
    punts = punts or set()
    bw, bh = kw * 0.58, kh * 0.60
    for i in range(n):
        gi = inici + i
        kx = x + i * kw
        c.setFillColor(marques.get(i, white))
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(1.0)
        c.rect(kx, y_top - kh, kw, kh, fill=1, stroke=1)
        if noms and not buides:
            fs = min(11.0, kw * 0.34)
            c.setFont('DejaVuSans-Bold', fs)
            c.setFillColor(white if i in marques else MUTED)
            c.drawCentredString(kx + kw / 2, y_top - kh + 7, BLANQUES[gi % 7])
    for i in range(n - 1):
        if (inici + i) % 7 in NEGRA_DESPRES:
            bx = x + (i + 1) * kw - bw / 2
            c.setFillColor(NAVY)
            c.rect(bx, y_top - bh, bw, bh, fill=1, stroke=0)
    for i, d in dits.items():
        cx, cy = x + (i + 0.5) * kw, y_top - kh * 0.72
        c.setFillColor(ACCENT)
        c.circle(cx, cy, min(11.5, kw * 0.32), fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', min(12.5, kw * 0.36))
        c.setFillColor(white)
        c.drawCentredString(cx, cy - 4.4, str(d))
    for i in punts:
        c.setFillColor(INK)
        c.circle(x + (i + 0.5) * kw, y_top - kh * 0.72, min(6.5, kw * 0.2), fill=1, stroke=0)
    return y_top - kh


def _pauta(c, x, y_top, ample, gap, clau=True):
    ys = draw_staff(c, x, y_top, ample, gap=gap)
    if clau:
        draw_clef(c, x + 4, ys[-1], gap, clef='treble')
    return ys[0], ys[-1]


# --------------------------------------------------------------------------
# capcalera i peu
# --------------------------------------------------------------------------
def capcalera(c, cfg):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)

    y = H - 46
    c.setFont('DejaVuSans-Bold', 9.5)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, cfg['kicker'].upper())
    c.setFont('DejaVuSans', 9.5)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, cfg['esquina'])
    y -= 34

    tsize = _fit(cfg['titol'], 'DejaVuSerif-Bold', 32, CONTENT_W, floor=22)
    c.setFont('DejaVuSerif-Bold', tsize)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, cfg['titol'])
    y -= 24
    if cfg.get('intro'):
        y = _wrap(c, cfg['intro'], MARGIN, y, 'DejaVuSans', 12, CONTENT_W, 15.5, NAVY_SOFT)
        y -= 6

    if cfg.get('regles'):
        bh = 30
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.rect(MARGIN, y - bh, 3, bh, fill=1, stroke=0)
        regles = cfg['regles']
        size = 10.5
        while size > 7.5 and (sum(stringWidth(r, 'DejaVuSans-Bold', size) for r in regles)
                              + 26 * (len(regles) - 1)) > CONTENT_W - 28:
            size -= 0.25
        rx = MARGIN + 14
        for i, r in enumerate(regles):
            c.setFont('DejaVuSans-Bold', size)
            c.setFillColor(NAVY)
            c.drawString(rx, y - 19, r)
            rx += stringWidth(r, 'DejaVuSans-Bold', size)
            if i < len(regles) - 1:
                c.setFillColor(ACCENT)
                c.circle(rx + 13, y - 15.5, 2.2, fill=1, stroke=0)
                rx += 26
        y -= bh + 12

    if cfg.get('nom_data'):
        c.setFont('DejaVuSans-Bold', 10)
        c.setFillColor(NAVY_SOFT)
        c.drawString(MARGIN, y - 12, 'NOM')
        c.setStrokeColor(RULE)
        c.setLineWidth(0.9)
        c.line(MARGIN + 34, y - 14, MARGIN + CONTENT_W * 0.60, y - 14)
        c.drawString(MARGIN + CONTENT_W * 0.66, y - 12, 'DATA')
        c.line(MARGIN + CONTENT_W * 0.66 + 40, y - 14, W - MARGIN, y - 14)
        y -= 30
    return y - 4


def peu(c, num):
    c.setFont('DejaVuSans', 8.5)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Quadern del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(num))


# --------------------------------------------------------------------------
# blocs comuns
# --------------------------------------------------------------------------
def b_misol(c, y, b):
    alt_buho = b.get('alt', 82.0)
    size, inter = 12.5, 16.5
    tx = MARGIN + 16 + alt_buho * 1.03 + 16
    ample = MARGIN + CONTENT_W - 16 - tx
    linies = _linies(b['text'], 'DejaVuSans', size, ample)
    h_text = 36 + inter * len(linies)
    h = max(alt_buho + 18, h_text)
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3.5, h, fill=1, stroke=0)
    dibujar_buho(c, MARGIN + 16, y - h + (h - alt_buho) / 2.0, alt_buho, b.get('pose', 'normal'))
    ty = y - (h - h_text) / 2.0
    c.setFont('DejaVuSans-Bold', 10)
    c.setFillColor(ACCENT)
    c.drawString(tx, ty - 18, b.get('etiqueta', 'EN MUSSOL MISOL DIU'))
    _wrap(c, b['text'], tx, ty - 35, 'DejaVuSans', size, ample, inter, NAVY)
    return y - h - 12


def _caixa(c, y, etiqueta, text, fons, filet, size=11.5):
    inter = size * 1.33
    ample = CONTENT_W - 30
    linies = _linies(text, 'DejaVuSans', size, ample)
    h = 32 + inter * len(linies)
    c.setFillColor(fons)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(filet)
    c.rect(MARGIN, y - h, 3.5, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9.8)
    c.setFillColor(filet)
    c.drawString(MARGIN + 16, y - 17, etiqueta)
    _wrap(c, text, MARGIN + 16, y - 33, 'DejaVuSans', size, ample, inter, INK)
    return y - h - 12


def b_nota(c, y, b):
    return _caixa(c, y, b.get('etiqueta', 'RECORDA'), b['text'], PANEL, BLUE)


def b_joc(c, y, b):
    return _caixa(c, y, b.get('etiqueta', 'UN JOC'), b['text'], WARM, ACCENT)


def b_sabies(c, y, b):
    return _caixa(c, y, 'SABIES QUE...?', b['text'], PANEL, NAVY_SOFT, size=11)


def _estrella(c, cx, cy, r):
    import math
    p = c.beginPath()
    for k in range(10):
        rr = r if k % 2 == 0 else r * 0.45
        a = math.radians(90 + k * 36)
        x, yy = cx + rr * math.cos(a), cy + rr * math.sin(a)
        if k == 0:
            p.moveTo(x, yy)
        else:
            p.lineTo(x, yy)
    p.close()
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.3)
    c.setFillColor(white)
    c.drawPath(p, fill=1, stroke=1)


def b_estrelles(c, y, b):
    """El registre de la setmana, a mida de nen: una estrella per pintar
       cada dia que toca."""
    h = 78
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3.5, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9.8)
    c.drawString(MARGIN + 16, y - 17, b.get('etiqueta', 'CADA DIA QUE TOQUIS, PINTA UNA ESTRELLA'))
    dies = ['Dl', 'Dt', 'Dc', 'Dj', 'Dv', 'Ds', 'Dg']
    pas = (CONTENT_W - 32) / len(dies)
    for i, d in enumerate(dies):
        cx = MARGIN + 16 + (i + 0.5) * pas
        _estrella(c, cx, y - 44, 15)
        c.setFont('DejaVuSans-Bold', 10)
        c.setFillColor(NAVY_SOFT)
        c.drawCentredString(cx, y - h + 8, d)
    return y - h - 12


# --------------------------------------------------------------------------
# blocs de TEORIA
# --------------------------------------------------------------------------
def b_mans(c, y, b):
    """Les dues mans, cadascuna sobre el seu teclat, amb els dits posats.
       El que s'ha d'entendre d'un cop d'ull: a la ma esquerra els dits van
       al reves."""
    y = _titol_seccio(c, y, b.get('titol', 'Les dues mans'))
    n, kw, kh = 5, 42.0, 92.0
    ample = n * kw
    sep = CONTENT_W - 2 * ample
    for k, (rotul, dits) in enumerate((('MÀ ESQUERRA', b['esquerra']),
                                       ('MÀ DRETA', b['dreta']))):
        x = MARGIN + k * (ample + sep)
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(ACCENT)
        c.drawCentredString(x + ample / 2, y - 10, rotul)
        _teclat(c, x, y - 18, n, kw, kh, dits=dits)
    y -= 18 + kh + 14
    if b.get('peu'):
        y = _wrap(c, b['peu'], MARGIN, y - 4, 'DejaVuSans', 11.5, CONTENT_W, 15, NAVY_SOFT)
    return y - 8


def b_pentagrama(c, y, b):
    y = _titol_seccio(c, y, b.get('titol', 'Al pentagrama'))
    gap = 12.0
    y -= gap * 1.4
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap)
    notes = b['notes']
    x0 = MARGIN + gap * 8.5
    pas = (CONTENT_W - gap * 11) / max(1, len(notes) - 1)
    base = min([bot] + [note_y(bot, gap, p) for p, _ in notes]) - gap * 2.5
    for i, (p, nom) in enumerate(notes):
        cx = x0 + i * pas
        draw_note(c, cx, bot, top, gap, p, dur='w', clef='treble')
        c.setFont('DejaVuSans-Bold', 14)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, base, nom)
    y = base - 14
    if b.get('peu'):
        y = _wrap(c, b['peu'], MARGIN, y - 6, 'DejaVuSans', 11.5, CONTENT_W, 15, NAVY_SOFT)
    return y - 8


def b_escala(c, y, b):
    """Les notes com a esglaons d'una escala, amb en Mussol dalt de tot. A
       cada esglao, el nom de la nota i un cercle buit per pintar-lo del seu
       color: la idea de "pujar" es veu, no cal llegir-la."""
    y = _titol_seccio(c, y, b.get('titol', 'L’escala'))
    noms = b['notes']
    n = len(noms)
    puja = 26.0
    alt0 = 82.0          # el primer esglao ha de tenir lloc per al nom, el color i el cercle
    ample_esc = CONTENT_W * 0.66
    ew = ample_esc / n
    base = y - (alt0 + puja * (n - 1)) - 6
    for i, nom in enumerate(noms):
        x = MARGIN + i * ew
        h = alt0 + puja * i
        c.setFillColor(PANEL)
        c.roundRect(x + 2, base, ew - 4, h, 5, fill=1, stroke=0)
        c.setFillColor(BLUE)
        c.rect(x + 2, base + h - 3.2, ew - 4, 3.2, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 21)
        c.setFillColor(NAVY)
        c.drawCentredString(x + ew / 2, base + h - 30, nom)
        _rodoneta(c, x + ew / 2, base + 18, 10)
        c.setFont('DejaVuSans', 9.5)
        c.setFillColor(MUTED)
        c.drawCentredString(x + ew / 2, base + h - 44, COLORS[nom.upper()])
    # en Mussol, cantant al costat de l'esglao de dalt de tot
    alt_b = 92.0
    dibujar_buho(c, MARGIN + ample_esc + 24, base + alt0 + puja * (n - 1) - alt_b + 6,
                 alt_b, 'happy')
    y = base - 14
    if b.get('peu'):
        y = _wrap(c, b['peu'], MARGIN, y - 4, 'DejaVuSans', 11.5, CONTENT_W, 15, NAVY_SOFT)
    return y - 8


def b_targetes(c, y, b):
    y = _titol_seccio(c, y, b.get('titol', 'Una a una'))
    items = b['items']
    n = len(items)
    sep = 12
    bw = (CONTENT_W - sep * (n - 1)) / n
    size, inter = 10.5, 13.5
    nmax = max(len(_linies(t, 'DejaVuSans', size, bw - 22)) for _, _, t in items)
    h = 56 + nmax * inter
    for i, (etq, nom, text) in enumerate(items):
        bx = MARGIN + i * (bw + sep)
        c.setFillColor(PANEL)
        c.roundRect(bx, y - h, bw, h, 5, fill=1, stroke=0)
        c.setFillColor(BLUE)
        c.rect(bx, y - h, bw, 3.2, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 9)
        c.setFillColor(MUTED)
        c.drawString(bx + 11, y - 16, etq)
        c.setFont('DejaVuSerif-Bold', 18)
        c.setFillColor(NAVY)
        c.drawString(bx + 11, y - 37, nom)
        _wrap(c, text, bx + 11, y - 54, 'DejaVuSans', size, bw - 22, inter, INK)
    return y - h - 14


# --------------------------------------------------------------------------
# bloc d'AL PIANO
# --------------------------------------------------------------------------
def b_exercici(c, y, b):
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    for s in b['sistemes']:
        if s.get('cap'):
            c.setFont('DejaVuSans-Bold', 10.5)
            c.setFillColor(NAVY_SOFT)
            c.drawString(MARGIN, y - 9, s['cap'])
            y -= 12
        y = _lineas(c, y, [dict(e) for e in s['events']], (4, 4), s.get('compassos', 4),
                    gap=s.get('gap', 9.4), show_time=s.get('show_time', True))
    return y - 6


# --------------------------------------------------------------------------
# blocs de FITXA (els dinamics)
# --------------------------------------------------------------------------
def b_pinta(c, y, b):
    """Escriu el nom de cada nota a la caixeta i pinta-la del seu color."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    y = _llegenda(c, y, b['llegenda'])
    gap = 12.0
    y -= gap * 1.6
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap)
    notes = b['notes']
    x0 = MARGIN + gap * 7.6
    pas = (CONTENT_W - gap * 9.6) / max(1, len(notes) - 1)
    baix = min([bot] + [note_y(bot, gap, p) for p in notes])
    for i, p in enumerate(notes):
        draw_note(c, x0 + i * pas, bot, top, gap, p, dur='w', clef='treble')
        _caixeta(c, x0 + i * pas - 22, baix - gap * 3.6, 44, 24)
    return baix - gap * 3.6 - 16


def b_relaciona(c, y, b):
    """Uneix cada nota del pentagrama amb la seva tecla."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    esq = b['notes']
    dre = b['tecles']            # el mateix, desordenat
    fila = 64.0
    gap = 7.6
    w_pent = 150.0
    n, kw, kh = 8, 19.0, 52.0
    x_tec = MARGIN + CONTENT_W - n * kw
    for i in range(len(esq)):
        fy = y - i * fila
        # esquerra: pentagrama petit amb UNA nota
        top, bot = _pauta(c, MARGIN, fy - 12, w_pent, gap)
        draw_note(c, MARGIN + w_pent * 0.68, bot, top, gap, esq[i], dur='w', clef='treble')
        c.setFillColor(ACCENT)
        c.circle(MARGIN + w_pent + 18, (top + bot) / 2, 4.2, fill=1, stroke=0)
        # dreta: teclat petit amb una tecla marcada
        idx = 'CDEFGAB'.index(dre[i][0])
        _teclat(c, x_tec, fy - 4, n, kw, kh, noms=False, punts={idx})
        c.setFillColor(ACCENT)
        c.circle(x_tec - 18, fy - 4 - kh / 2, 4.2, fill=1, stroke=0)
    return y - len(esq) * fila - 8


def b_compta(c, y, b):
    """Compta quantes notes de cada hi ha, i pinta el cercle del seu color."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    gap = 10.5
    y -= gap * 1.4
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap)
    notes = b['notes']
    x0 = MARGIN + gap * 7.2
    pas = (CONTENT_W - gap * 9.0) / max(1, len(notes) - 1)
    for i, p in enumerate(notes):
        draw_note(c, x0 + i * pas, bot, top, gap, p, dur='w', clef='treble')
    yy = min([bot] + [note_y(bot, gap, p) for p in notes]) - gap * 2.4
    quines = b['quines']
    pas = CONTENT_W / float(len(quines))
    for i, nom in enumerate(quines):
        x = MARGIN + i * pas
        _rodoneta(c, x + 12, yy - 14, 11)
        c.setFont('DejaVuSans-Bold', 12)
        c.setFillColor(INK)
        c.drawString(x + 30, yy - 18.5, 'Quants %s?' % nom)
        _caixeta(c, x + 30 + stringWidth('Quants %s?' % nom, 'DejaVuSans-Bold', 12) + 8,
                 yy - 26, 34, 24)
    return yy - 40


def _graella_cami(cami, files, cols, cicle, llavor):
    """Omple la graella del laberint: el cami segueix el cicle (DO-RE-MI...) i
       la resta de caselles es reomple de manera que NO hi hagi cap drecera:
       cap casella veina del cami pot dur la nota que toca despres."""
    rnd = random.Random(llavor)
    graella = [[None] * cols for _ in range(files)]
    for k, (f, co) in enumerate(cami):
        graella[f][co] = cicle[k % len(cicle)]
    tots = list(COLORS.keys())
    pos = {cel: k for k, cel in enumerate(cami)}
    for f in range(files):
        for co in range(cols):
            if graella[f][co] is not None:
                continue
            prohibides = set()
            for df, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                vei = (f + df, co + dc)
                if vei in pos:
                    prohibides.add(cicle[(pos[vei] + 1) % len(cicle)])
            opcions = [n for n in tots if n not in prohibides]
            graella[f][co] = rnd.choice(opcions)
    return graella


def b_cami(c, y, b):
    """Ajuda en Mussol Misol a arribar al piano: pinta el cami trepitjant les
       notes en ordre."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    files, cols = b['files'], b['columnes']
    cicle = b['cicle']
    graella = _graella_cami(b['cami'], files, cols, cicle, b.get('llavor', 8))
    marge_esq, marge_dre = 70.0, 70.0
    cw = (CONTENT_W - marge_esq - marge_dre) / cols
    ch = min(cw, 35.0)
    x0 = MARGIN + marge_esq
    top = y - 4
    for f in range(files):
        for co in range(cols):
            cx = x0 + (co + 0.5) * cw
            cy = top - (f + 0.5) * ch
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(1.0)
            c.setFillColor(white)
            c.circle(cx, cy, min(cw, ch) * 0.43, fill=1, stroke=1)
            c.setFont('DejaVuSans-Bold', 10.5)
            c.setFillColor(INK)
            c.drawCentredString(cx, cy - 3.8, graella[f][co])
    # en Mussol a la sortida i el piano a l'arribada
    f0, c0 = b['cami'][0]
    fN, cN = b['cami'][-1]
    alt = 52.0
    dibujar_buho(c, MARGIN + 4, top - (f0 + 0.5) * ch - alt / 2, alt, 'happy')
    _teclat(c, x0 + cols * cw + 14, top - (fN + 0.5) * ch + 18, 4, 13, 36, noms=False)
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(ACCENT)
    c.drawCentredString(x0 + cols * cw + 14 + 26, top - (fN + 0.5) * ch - 30, 'ARRIBADA')
    c.drawCentredString(MARGIN + 30, top - (f0 + 0.5) * ch - alt / 2 - 10, 'SORTIDA')
    return top - files * ch - 20


def b_teclat_pinta(c, y, b):
    """Un teclat gran sense noms: el nen busca i pinta les tecles."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    n = b.get('tecles', 15)
    kw = CONTENT_W / float(n)
    bot = _teclat(c, MARGIN, y - 4, n, kw, 68, buides=True)
    return _llegenda(c, bot - 12, b['pintar']) - 4


BLOCS = {
    'misol': b_misol, 'nota': b_nota, 'joc': b_joc, 'sabies': b_sabies,
    'mans': b_mans, 'pentagrama': b_pentagrama, 'targetes': b_targetes,
    'escala': b_escala, 'estrelles': b_estrelles,
    'exercici': b_exercici,
    'pinta': b_pinta, 'relaciona': b_relaciona, 'compta': b_compta,
    'cami': b_cami, 'teclat_pinta': b_teclat_pinta,
}
SENSE_NUMERO = {'misol', 'nota', 'joc', 'sabies', 'mans', 'pentagrama', 'targetes',
                'escala', 'estrelles'}


# --------------------------------------------------------------------------
# una fulla
# --------------------------------------------------------------------------
def _numerar(blocs, des_de=1):
    out, n = [], des_de
    for b in blocs:
        if b['tipus'] not in SENSE_NUMERO:
            b = dict(b, num=n)
            n += 1
        out.append(b)
    return out, n


def _dibuixar(c, y, blocs, aire):
    for b in blocs:
        y = BLOCS[b['tipus']](c, y, b) - aire
    return y + aire


class NoHiCap(Exception):
    pass


def fulla(c, cfg, blocs, num_pag, primer_num=1):
    """Dibuixa UNA fulla i retorna (y final, seguent numero d'exercici).

       Abans de dibuixar es mesura sobre un llenc de prova: si el contingut
       no hi cap, s'atura amb un error que diu QUANT sobra, perque es retalli
       el material. Una fulla que es surt pel peu no s'imprimeix mai."""
    blocs, seguent = _numerar(blocs, primer_num)
    prova = Canvas(io.BytesIO(), pagesize=(W, H))
    y0 = capcalera(prova, cfg)
    y_fi = _dibuixar(prova, y0, blocs, 0.0)
    if y_fi < SUELO:
        raise NoHiCap('%s: sobren %.0f pt' % (cfg['esquina'], SUELO - y_fi))
    forats = max(1, len(blocs) - 1)
    aire = max(0.0, min(AIRE_MAX, (y_fi - OBJECTIU) / forats))

    y0 = capcalera(c, cfg)
    y_fi = _dibuixar(c, y0, blocs, aire)
    peu(c, num_pag)
    c.showPage()
    return y_fi, seguent
