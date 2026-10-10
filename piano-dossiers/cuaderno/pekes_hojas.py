# -*- coding: utf-8 -*-
"""Les fulles del LLIBRE DE PEKES: l'aspecte dels albums d'alumne, a mida de
   nen petit.

   No es un disseny nou: es la mateixa capcalera dels albums (franja blau nit,
   kicker, titol en serifa, la banda de regles), els mateixos recuadres (fons
   calid amb filet ocre, fons de panell amb filet blau), les mateixes targetes
   i el mateix motor de pentagrames. El que canvia, per peticio del client:

   - TOT mes gran: titol 32, text 12, pentagrames amb mes espai entre linies.
   - Les DUES CLAUS des del principi: la ma dreta a la clau de Sol i la ma
     esquerra a la clau de Fa, a la teoria, al piano i a les fitxes.
   - Fitxes dinamiques, pensades per a nens que encara llegeixen a poc a poc:
     pintar amb el codi de colors, relacionar, comptar, el laberint d'en
     Mussol, dibuixar, encerclar, sopa de lletres, endevinalles...
   - Cada pagina es MESURA abans de dibuixar-la: si el contingut no hi cap,
     s'atura amb un error que diu quant sobra.

   Una limitacio del motor que cal saber: quan les dues mans s'ALTERNEN (una
   toca i l'altra calla) les barres de compas dels dos pentagrames no queden
   alineades. Per aixo les dues mans juntes nomes es fan servir quan toquen
   ALHORA; la "pregunta i resposta" va en dos pentagrames separats.
"""
import io
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen.canvas import Canvas

from notation import (draw_staff, draw_clef, draw_note, draw_rest, draw_barline,
                      draw_time_sig, note_y, BLEED_SAFE)
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit)
from hoja_piano import _lineas
from misol import dibujar_buho

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')
SOFT = HexColor('#E6DCC6')

SUELO = 50.0          # per sota d'aixo es trepitja el peu
OBJECTIU = 70.0       # on es vol que acabi una fulla justificada
AIRE_MAX = 34.0

# el codi de colors del curs (el mateix del Canva original del client)
COLORS = {'DO': 'vermell', 'RE': 'taronja', 'MI': 'groc', 'FA': 'verd',
          'SOL': 'blau', 'LA': 'lila', 'SI': 'gris'}
NOM_LLETRA = {'C': 'DO', 'D': 'RE', 'E': 'MI', 'F': 'FA', 'G': 'SOL', 'A': 'LA', 'B': 'SI'}
BLANQUES = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
NEGRA_DESPRES = {0, 1, 3, 4, 5}


def nom_de(pitch):
    return NOM_LLETRA[pitch[0]]


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


def _peu(c, y, b):
    if b.get('peu'):
        y = _wrap(c, b['peu'], MARGIN, y - 4, 'DejaVuSans', 11.5, CONTENT_W, 15, NAVY_SOFT)
    return y - 8


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
    pas = ample / float(max(len(notes), 3))
    for i, n in enumerate(notes):
        cx = x0 + i * pas + 12
        _rodoneta(c, cx, y - 9, 9)
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(INK)
        c.drawString(cx + 15, y - 13, '%s = %s' % (n, COLORS[n]))
    return y - 26


def _estrella(c, cx, cy, r, color=ACCENT, ple=False):
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
    c.setStrokeColor(color)
    c.setLineWidth(1.3)
    c.setFillColor(color if ple else white)
    c.drawPath(p, fill=1, stroke=1)


def _teclat(c, x, y_top, n, kw, kh, noms=True, inici=0, dits=None, punts=None,
            ressalta=None, buides=False):
    """Un teclat a mida de nen. `dits` {i: numero} posa el dit en un cercle,
       `punts` {i} hi posa un punt negre (la tecla que s'ha de trobar),
       `ressalta` {i} pinta la tecla de fons calid."""
    dits = dits or {}
    punts = punts or set()
    ressalta = ressalta or set()
    bw, bh = kw * 0.58, kh * 0.60
    for i in range(n):
        gi = inici + i
        kx = x + i * kw
        c.setFillColor(SOFT if i in ressalta else white)
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(1.0)
        c.rect(kx, y_top - kh, kw, kh, fill=1, stroke=1)
        if noms and not buides:
            fs = min(11.0, kw * 0.34)
            c.setFont('DejaVuSans-Bold', fs)
            c.setFillColor(NAVY if i in ressalta else MUTED)
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


def _pauta(c, x, y_top, ample, gap, clau='treble'):
    ys = draw_staff(c, x, y_top, ample, gap=gap)
    if clau:
        draw_clef(c, x + 4, ys[-1], gap, clef=clau)
    return ys[0], ys[-1]


def _nota(c, cx, top, bot, gap, pitch, clau='treble', dur='w', plica=None):
    # clau=None: un pentagrama sense clau (el tema 5, abans de les claus); les
    # notes es col·loquen igual que en clau de Sol, linia a linia
    draw_note(c, cx, bot, top, gap, pitch, dur=dur, stem_dir=plica, clef=clau or 'treble')


def _mes_baixa(bot, gap, notes, clau):
    return min([bot] + [note_y(bot, gap, p, clau or 'treble') for p in notes])


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
    kick = cfg['kicker'].upper()
    esq = cfg['esquina']
    kw_max = CONTENT_W - stringWidth(esq, 'DejaVuSans', 9.5) - 16
    c.setFont('DejaVuSans-Bold', _fit(kick, 'DejaVuSans-Bold', 9.5, kw_max, floor=7.5))
    c.drawString(MARGIN, y, kick)
    c.setFont('DejaVuSans', 9.5)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, esq)
    y -= 34

    tsize = _fit(cfg['titol'], 'DejaVuSerif-Bold', 32, CONTENT_W, floor=20)
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
def b_teclat(c, y, b):
    """Un teclat gran, per explicar: dits, punts, tecles ressaltades,
       rotuls a sobre, els grups de negres i les fletxes de greu/agut."""
    if b.get('titol'):
        y = _titol_seccio(c, y, b['titol'])
    n = b.get('tecles', 10)
    kw = CONTENT_W / float(n)
    kh = b.get('alt', 84.0)
    inici = b.get('inici', 0)
    etiq = b.get('etiquetes', {})
    if etiq or b.get('grups'):
        y -= 22
    if b.get('greu_agut'):
        y -= 30
        mid = y + 14
        c.setStrokeColor(ACCENT)
        c.setFillColor(ACCENT)
        c.setLineWidth(2.2)
        for sentit, text, x_txt in ((-1, '◀  GREU  ·  l’os', MARGIN),
                                    (1, 'AGUT  ·  l’ocellet  ▶', W - MARGIN)):
            c.setFont('DejaVuSans-Bold', 12)
            if sentit < 0:
                c.drawString(x_txt, mid - 4, text)
            else:
                c.drawRightString(x_txt, mid - 4, text)
        c.line(MARGIN + 150, mid, W - MARGIN - 175, mid)
    bot = _teclat(c, MARGIN, y, n, kw, kh, inici=inici, dits=b.get('dits'),
                  punts=set(b.get('punts', [])), ressalta=set(b.get('ressalta', [])))
    for i, text in etiq.items():
        cx = MARGIN + (i + 0.5) * kw
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, y + 8, text)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.2)
        c.line(cx, y + 1, cx, y + 5)
    if b.get('grups'):
        # els claudators de sobre de cada grup de negres: el 2 i el 3
        bw = kw * 0.58
        for i in range(n - 1):
            gi = (inici + i) % 7
            if gi in (0, 3):
                quantes = 2 if gi == 0 else 3
                if i + quantes > n - 1:
                    continue
                x1 = MARGIN + (i + 1) * kw - bw / 2
                x2 = MARGIN + (i + quantes) * kw + bw / 2
                c.setStrokeColor(BLUE)
                c.setLineWidth(1.6)
                c.line(x1, y + 4, x1, y + 9)
                c.line(x1, y + 9, x2, y + 9)
                c.line(x2, y + 9, x2, y + 4)
                c.setFont('DejaVuSans-Bold', 11)
                c.setFillColor(BLUE)
                c.drawCentredString((x1 + x2) / 2, y + 13, str(quantes))
    return _peu(c, bot - 12, b)


def b_mans(c, y, b):
    """Les dues mans, cadascuna sobre el seu teclat, amb els dits posats.
       El que s'ha d'entendre d'un cop d'ull: a la ma esquerra els dits van
       al reves."""
    y = _titol_seccio(c, y, b.get('titol', 'Les dues mans'))
    teclats = b['teclats']
    kh = b.get('alt', 92.0)
    sep = 28.0
    ample = (CONTENT_W - sep * (len(teclats) - 1)) / len(teclats)
    for k, t in enumerate(teclats):
        n = t.get('n', 5)
        kw = min(44.0, ample / n)
        x = MARGIN + k * (ample + sep) + (ample - n * kw) / 2
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(ACCENT)
        c.drawCentredString(x + n * kw / 2, y - 10, t['rotul'])
        _teclat(c, x, y - 18, n, kw, kh, inici=t.get('inici', 0), dits=t.get('dits'),
                ressalta=set(t.get('ressalta', [])))
    return _peu(c, y - 18 - kh - 12, b)


def b_pentagrama(c, y, b):
    """Notes soltes amb el nom a sota, en una clau o en l'altra."""
    y = _titol_seccio(c, y, b.get('titol', 'Al pentagrama'))
    clau = b.get('clau', 'treble')
    gap = b.get('gap', 12.0)
    y -= gap * 1.6
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap, clau)
    notes = b['notes']
    x0 = MARGIN + gap * 8.5
    pas = (CONTENT_W - gap * 11) / max(1, len(notes) - 1)
    base = _mes_baixa(bot, gap, [p for p, _ in notes], clau) - gap * 2.5
    for i, (p, nom) in enumerate(notes):
        cx = x0 + i * pas
        _nota(c, cx, top, bot, gap, p, clau)
        c.setFont('DejaVuSans-Bold', 14)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, base, nom)
    return _peu(c, base - 14, b)


def b_linies_espais(c, y, b):
    """La casa de les notes: les cinc linies i els quatre espais, comptats de
       baix a dalt, amb una nota a una linia i una altra a un espai."""
    y = _titol_seccio(c, y, b.get('titol', 'Cinc línies i quatre espais'))
    gap = 17.0
    x0 = MARGIN + 34
    ample = CONTENT_W - 150
    y -= gap * 0.8
    ys = draw_staff(c, x0, y, ample, gap=gap)
    bot = ys[-1]
    for i in range(5):
        ly = bot + i * gap
        c.setFont('DejaVuSerif-Bold', 15)
        c.setFillColor(ACCENT)
        c.drawRightString(x0 - 10, ly - 5, str(i + 1))
    for i in range(4):
        sy = bot + (i + 0.5) * gap
        c.setFont('DejaVuSans-Bold', 10.5)
        c.setFillColor(BLUE)
        c.drawString(x0 + ample + 10, sy - 4, 'espai %d' % (i + 1))
    _nota(c, x0 + ample * 0.32, ys[0], bot, gap, 'B4')
    _nota(c, x0 + ample * 0.68, ys[0], bot, gap, 'A4')
    c.setFont('DejaVuSans-Bold', 11)
    c.setFillColor(NAVY)
    c.drawCentredString(x0 + ample * 0.32, bot - 22, 'a una línia')
    c.drawCentredString(x0 + ample * 0.68, bot - 22, 'a un espai')
    return _peu(c, bot - 36, b)


def b_clau(c, y, b):
    """Una clau gran, amb la linia que li dona nom ressaltada i la seva nota
       a sobre: la clau de Sol abraca la linia del Sol; la de Fa te els dos
       punts a banda i banda de la linia del Fa."""
    y = _titol_seccio(c, y, b['titol'])
    clau = b['clau']
    gap = 15.0
    y -= gap * 1.4
    ample = CONTENT_W * 0.62
    top, bot = _pauta(c, MARGIN, y, ample, gap, clau)
    ref = 'G4' if clau == 'treble' else 'F3'
    ly = note_y(bot, gap, ref, clau)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(3.2)
    c.line(MARGIN + gap * 4.5, ly, MARGIN + ample, ly)
    cx = MARGIN + ample * 0.66
    _nota(c, cx, top, bot, gap, ref, clau)
    nom = 'Sol' if clau == 'treble' else 'Fa'
    c.setFont('DejaVuSans-Bold', 15)
    c.setFillColor(ACCENT)
    c.drawString(cx + gap * 1.4, ly - 5, nom)
    # a la dreta, qui viu en aquesta clau
    tx = MARGIN + ample + 22
    c.setFont('DejaVuSans-Bold', 11)
    c.setFillColor(NAVY_SOFT)
    c.drawString(tx, top - 2, 'AQUÍ VIU...')
    c.setFont('DejaVuSerif-Bold', 17)
    c.setFillColor(NAVY)
    c.drawString(tx, top - 26, b.get('qui', 'la mà dreta' if clau == 'treble' else 'la mà esquerra'))
    _wrap(c, b.get('com', ''), tx, top - 46, 'DejaVuSans', 10.5, W - MARGIN - tx, 13.5, MUTED)
    return _peu(c, bot - gap * 2.2, b)


def _clau_llarga(c, x, top_t, bot_b):
    """La clau (claudator) que uneix els dos pentagrames del piano."""
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.4)
    c.line(x, top_t, x, bot_b)
    mig = (top_t + bot_b) / 2.0
    p = c.beginPath()
    p.moveTo(x - 3, top_t)
    p.curveTo(x - 11, top_t - 10, x - 3, mig - 12, x - 11, mig)
    p.curveTo(x - 3, mig + 12, x - 11, bot_b + 10, x - 3, bot_b)
    c.setLineWidth(2.4)
    c.drawPath(p, fill=0, stroke=1)


def b_gran(c, y, b):
    """El gran pentagrama del piano: la clau de Sol a dalt (ma dreta) i la de
       Fa a baix (ma esquerra), units per la clau. Les notes, cadascuna al seu
       pentagrama, amb el nom a sota de tot."""
    y = _titol_seccio(c, y, b.get('titol', 'El gran pentagrama'))
    gap = 10.5
    x0 = MARGIN + 16
    ample = CONTENT_W - 16 - 96
    y -= gap
    ys_t = draw_staff(c, x0, y, ample, gap=gap)
    top_t, bot_t = ys_t[0], ys_t[-1]
    draw_clef(c, x0 + 4, bot_t, gap, clef='treble')
    top_b = bot_t - gap * 5.5
    ys_b = draw_staff(c, x0, top_b, ample, gap=gap)
    bot_b = ys_b[-1]
    draw_clef(c, x0 + 4, bot_b, gap, clef='bass')
    _clau_llarga(c, x0, top_t, bot_b)
    draw_barline(c, x0 + ample, top_t, bot_b)
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(ACCENT)
    c.drawString(x0 + ample + 12, (top_t + bot_t) / 2 - 4, 'MÀ DRETA')
    c.drawString(x0 + ample + 12, (top_b + bot_b) / 2 - 4, 'MÀ ESQUERRA')
    notes = b['notes']
    xn = x0 + gap * 8
    pas = (ample - gap * 10) / max(1, len(notes) - 1)
    base = bot_b - gap * 3.4
    for i, (p, clau, nom) in enumerate(notes):
        cx = xn + i * pas
        if clau == 'treble':
            _nota(c, cx, top_t, bot_t, gap, p, 'treble')
        else:
            _nota(c, cx, top_b, bot_b, gap, p, 'bass')
        c.setFont('DejaVuSans-Bold', 12.5)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, base, nom)
    return _peu(c, base - 14, b)


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
        nsize = _fit(nom, 'DejaVuSerif-Bold', 18, bw - 22, floor=11)
        c.setFont('DejaVuSerif-Bold', nsize)
        c.setFillColor(NAVY)
        c.drawString(bx + 11, y - 37, nom)
        _wrap(c, text, bx + 11, y - 54, 'DejaVuSans', size, bw - 22, inter, INK)
    return y - h - 14


def b_escala(c, y, b):
    """Les notes com a esglaons d'una escala, amb en Mussol dalt de tot. A
       cada esglao, el nom de la nota i un cercle buit per pintar-lo del seu
       color: la idea de "pujar" es veu, no cal llegir-la."""
    y = _titol_seccio(c, y, b.get('titol', 'L’escala'))
    noms = b['notes']
    n = len(noms)
    puja = b.get('puja', 26.0 if n <= 4 else 15.0)
    alt0 = 82.0
    ample_esc = CONTENT_W * (0.66 if n <= 4 else 0.80)
    ew = ample_esc / n
    base = y - (alt0 + puja * (n - 1)) - 6
    for i, nom in enumerate(noms):
        x = MARGIN + i * ew
        h = alt0 + puja * i
        c.setFillColor(PANEL)
        c.roundRect(x + 2, base, ew - 4, h, 5, fill=1, stroke=0)
        c.setFillColor(BLUE)
        c.rect(x + 2, base + h - 3.2, ew - 4, 3.2, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', _fit(nom, 'DejaVuSerif-Bold', 21, ew - 10, floor=12))
        c.setFillColor(NAVY)
        c.drawCentredString(x + ew / 2, base + h - 30, nom)
        _rodoneta(c, x + ew / 2, base + 18, 10)
        c.setFont('DejaVuSans', 9.5)
        c.setFillColor(MUTED)
        c.drawCentredString(x + ew / 2, base + h - 44, COLORS[nom.upper()])
    alt_b = 88.0 if n <= 4 else 74.0
    dibujar_buho(c, MARGIN + ample_esc + 14, base + alt0 + puja * (n - 1) - alt_b + 6,
                 alt_b, 'happy')
    return _peu(c, base - 14, b)


def _figura(c, cx, cap_y, gap, dur):
    """Una figura o un silenci, dibuixat de veritat, amb el cap a cap_y."""
    bot = cap_y - 2 * gap
    if dur.startswith('R'):
        # el silenci, sobre el seu pentagrama petit: la seva posicio vol dir
        # alguna cosa (el de blanca s'asseu a la linia, el de rodona en penja)
        draw_staff(c, cx - gap * 2.4, bot + 4 * gap, gap * 4.8, gap=gap)
        draw_rest(c, cx, bot, bot + 4 * gap, gap, dur[1:])
    else:
        draw_note(c, cx, bot, bot + 4 * gap, gap, 'B4', dur=dur, stem_dir='up', clef='treble')


def b_figures(c, y, b):
    """Les figures (o els silencis) grans, amb el nom i el que duren."""
    y = _titol_seccio(c, y, b.get('titol', 'Les figures'))
    items = b['items']
    n = len(items)
    gap = 12.0
    pas = CONTENT_W / float(n)
    cap_y = y - gap * 4.4
    for i, (dur, nom, temps) in enumerate(items):
        cx = MARGIN + (i + 0.5) * pas
        _figura(c, cx, cap_y, gap, dur)
        c.setFont('DejaVuSans-Bold', 13.5)
        c.setFillColor(NAVY)
        c.drawCentredString(cx, cap_y - gap * 3.4, nom)
        c.setFont('DejaVuSans-Bold', 11.5)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, cap_y - gap * 3.4 - 17, temps)
    return _peu(c, cap_y - gap * 3.4 - 32, b)


def b_compas(c, y, b):
    """El compas: les cajetes de la musica, amb les linies divisories i la
       doble barra del final senyalades."""
    y = _titol_seccio(c, y, b.get('titol', 'El compàs'))
    gap = 11.0
    y -= 34
    ys = draw_staff(c, MARGIN, y, CONTENT_W, gap=gap)
    top, bot = ys[0], ys[-1]
    draw_clef(c, MARGIN + 4, bot, gap, clef='treble')
    draw_time_sig(c, MARGIN + gap * 4.6, bot, gap)
    x_ini = MARGIN + gap * 6.4
    x_fi = MARGIN + CONTENT_W - 6
    n_comp = 3
    amp = (x_fi - x_ini) / n_comp
    figures = b.get('compassos', [['q', 'q', 'q', 'q'], ['h', 'h'], ['w']])
    alts = ['C4', 'E4', 'G4', 'E4']
    for k in range(n_comp):
        xb = x_ini + k * amp
        durs = figures[k]
        pas = amp / len(durs)
        for j, d in enumerate(durs):
            draw_note(c, xb + (j + 0.4) * pas, bot, top, gap, alts[j % 4], dur=d, clef='treble')
        if k < n_comp - 1:
            draw_barline(c, xb + amp, top, bot)
    draw_barline(c, x_fi - 4, top, bot, final=True)
    # els rotuls
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(ACCENT)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.4)
    c.line(x_ini + 4, top + 10, x_ini + amp - 4, top + 10)
    c.drawCentredString(x_ini + amp / 2, top + 16, 'UN COMPÀS = 4 TEMPS')
    c.drawCentredString(x_ini + amp, bot - 26, 'LÍNIA DIVISÒRIA')
    c.line(x_ini + amp, bot - 4, x_ini + amp, bot - 16)
    c.drawRightString(x_fi, bot - 26, 'DOBLE BARRA: FINAL!')
    c.drawString(MARGIN + gap * 3.2, top + 16, '4/4')
    return _peu(c, bot - 40, b)


def b_pliques(c, y, b):
    """Plica amunt o avall: per sota de la linia del mig, amunt i a la dreta;
       a la linia del mig o per sobre, avall i a l'esquerra."""
    y = _titol_seccio(c, y, b.get('titol', 'Amunt o avall?'))
    gap = 12.0
    y -= 30
    ample = CONTENT_W
    top, bot = _pauta(c, MARGIN, y, ample, gap, b.get('clau', 'treble'))
    mig = bot + 2 * gap
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.6)
    c.setDash(4, 3)
    c.line(MARGIN + gap * 4.2, mig, MARGIN + ample, mig)
    c.setDash()
    notes = b.get('notes', [('E4', 'up'), ('G4', 'up'), ('B4', 'down'), ('D5', 'down')])
    clau = b.get('clau', 'treble')
    x0 = MARGIN + gap * 8
    pas = (ample - gap * 10) / max(1, len(notes) - 1)
    for i, (p, sentit) in enumerate(notes):
        cx = x0 + i * pas
        _nota(c, cx, top, bot, gap, p, clau, dur='q', plica=sentit)
        c.setFont('DejaVuSans-Bold', 11.5)
        c.setFillColor(ACCENT if sentit == 'up' else BLUE)
        c.drawCentredString(cx, bot - gap * 3.4, 'AMUNT' if sentit == 'up' else 'AVALL')
    c.setFont('DejaVuSans-Bold', 9.5)
    c.setFillColor(ACCENT)
    c.drawRightString(MARGIN + ample, mig + 5, 'la línia del mig')
    return _peu(c, bot - gap * 3.4 - 16, b)


# --------------------------------------------------------------------------
# blocs d'AL PIANO
# --------------------------------------------------------------------------
def b_exercici(c, y, b):
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    for s in b['sistemes']:
        if s.get('cap'):
            c.setFont('DejaVuSans-Bold', 10.5)
            c.setFillColor(NAVY_SOFT)
            c.drawString(MARGIN, y - 9, s['cap'])
            y -= 12
        y = _lineas(c, y, [dict(e) for e in s['events']], s.get('compas', (4, 4)),
                    s.get('compassos', 4), gap=s.get('gap', 10.5),
                    show_time=s.get('show_time', True), clef=s.get('clau', 'treble'),
                    manos=s.get('manos', 'dobla'))
    return y - 6


def b_passos(c, y, b):
    """Passos numerats, grossos: el que es fa al piano abans de llegir."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    for i, pas in enumerate(b['passos']):
        r = 13
        c.setFillColor(NAVY)
        c.circle(MARGIN + 32 + r, y - r, r, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 12)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 32 + r, y - r - 4.3, chr(ord('a') + i))
        yy = _wrap(c, pas, MARGIN + 32 + 2 * r + 12, y - 9, 'DejaVuSans', 12,
                   CONTENT_W - 32 - 2 * r - 12, 15.5, INK)
        y = min(yy, y - 2 * r - 4) - 8
    return y - 2


# --------------------------------------------------------------------------
# blocs de FITXA (els dinamics)
# --------------------------------------------------------------------------
def b_pinta(c, y, b):
    """Escriu el nom de cada nota a la caixeta i pinta-la del seu color.
       Notes grosses (espai de 14 pt): s'han de poder pintar amb una cera."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    y = _llegenda(c, y, b['llegenda'])
    clau = b.get('clau', 'treble')
    gap = 14.0
    y -= gap * 1.2
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap, clau)
    notes = b['notes']
    x0 = MARGIN + gap * 7.0
    pas = (CONTENT_W - gap * 8.6) / max(1, len(notes) - 1)
    baix = _mes_baixa(bot, gap, notes, clau)
    for i, p in enumerate(notes):
        _nota(c, x0 + i * pas, top, bot, gap, p, clau)
        _caixeta(c, x0 + i * pas - 24, baix - gap * 3.1, 48, 26)
    return baix - gap * 3.1 - 16


def b_relaciona(c, y, b):
    """Uneix cada nota del pentagrama amb la seva tecla (punt a punt)."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    esq = b['notes']                     # [(pitch, clau), ...]
    dre = b['tecles']                    # lletres, desordenades
    fila = 74.0
    gap = 10.0
    w_pent = 190.0
    n, kw, kh = 8, 22.0, 58.0
    x_tec = MARGIN + CONTENT_W - n * kw
    for i in range(len(esq)):
        fy = y - i * fila
        p, clau = esq[i]
        top, bot = _pauta(c, MARGIN, fy - 12, w_pent, gap, clau)
        _nota(c, MARGIN + w_pent * 0.66, top, bot, gap, p, clau)
        c.setFillColor(ACCENT)
        c.circle(MARGIN + w_pent + 22, (top + bot) / 2, 5, fill=1, stroke=0)
        idx = 'CDEFGAB'.index(dre[i][0])
        _teclat(c, x_tec, fy - 6, n, kw, kh, noms=False, punts={idx})
        c.setFillColor(ACCENT)
        c.circle(x_tec - 22, fy - 6 - kh / 2, 5, fill=1, stroke=0)
    return y - len(esq) * fila - 4


def b_compta(c, y, b):
    """Compta quantes notes de cada hi ha, i pinta el cercle del seu color."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    clau = b.get('clau', 'treble')
    gap = 11.0
    y -= gap * 1.4
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap, clau)
    notes = b['notes']
    x0 = MARGIN + gap * 7.2
    pas = (CONTENT_W - gap * 9.0) / max(1, len(notes) - 1)
    for i, p in enumerate(notes):
        _nota(c, x0 + i * pas, top, bot, gap, p, clau)
    yy = _mes_baixa(bot, gap, notes, clau) - gap * 2.2
    quines = b['quines']
    pas = CONTENT_W / float(len(quines))
    for i, nom in enumerate(quines):
        x = MARGIN + i * pas
        _rodoneta(c, x + 12, yy - 14, 11)
        text = 'Quants %s?' % nom
        c.setFont('DejaVuSans-Bold', 12)
        c.setFillColor(INK)
        c.drawString(x + 30, yy - 18.5, text)
        _caixeta(c, x + 30 + stringWidth(text, 'DejaVuSans-Bold', 12) + 8, yy - 26, 34, 24)
    return yy - 40


def _graella_cami(cami, files, cols, cicle, coneguts, llavor):
    """Omple la graella del laberint: el cami segueix el cicle (DO-RE-MI...) i
       la resta de caselles es reomple NOMES amb notes que el nen ja coneix,
       de manera que no hi hagi cap drecera: cap casella veina del cami pot
       dur la nota que toca despres."""
    rnd = random.Random(llavor)
    graella = [[None] * cols for _ in range(files)]
    for k, (f, co) in enumerate(cami):
        graella[f][co] = cicle[k % len(cicle)]
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
            opcions = [n for n in coneguts if n not in prohibides]
            graella[f][co] = rnd.choice(opcions)
    return graella


def b_cami(c, y, b):
    """Ajuda en Mussol Misol a arribar al piano: pinta el cami trepitjant les
       notes en ordre."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    files, cols = b['files'], b['columnes']
    cicle = b['cicle']
    graella = _graella_cami(b['cami'], files, cols, cicle, b['coneguts'], b.get('llavor', 8))
    marge_esq, marge_dre = 70.0, 70.0
    cw = (CONTENT_W - marge_esq - marge_dre) / cols
    ch = min(cw, b.get('alt_fila', 36.0))
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
    f0, _c0 = b['cami'][0]
    fN, _cN = b['cami'][-1]
    alt = 50.0
    dibujar_buho(c, MARGIN + 6, top - (f0 + 0.5) * ch - alt / 2, alt, 'happy')
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(ACCENT)
    c.drawCentredString(MARGIN + 30, top - (f0 + 0.5) * ch - alt / 2 - 10, 'SORTIDA')
    xp = x0 + cols * cw + 14
    _teclat(c, xp, top - (fN + 0.5) * ch + 16, 4, 13, 32, noms=False)
    c.drawCentredString(xp + 26, top - (fN + 0.5) * ch - 26, 'ARRIBADA')
    return top - files * ch - 22


def b_teclat_pinta(c, y, b):
    """Un teclat gran sense noms: el nen busca i pinta les tecles."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    n = b.get('tecles', 15)
    kw = CONTENT_W / float(n)
    bot = _teclat(c, MARGIN, y - 4, n, kw, b.get('alt', 66.0), buides=True,
                  inici=b.get('inici', 0))
    if b.get('pintar'):
        return _llegenda(c, bot - 12, b['pintar']) - 4
    # sense llegenda de notes: una consigna per pintar (els grups de negres,
    # la tecla mes greu...), cadascuna amb la seva rodoneta
    y = bot - 10
    for text in b.get('consignes', []):
        _rodoneta(c, MARGIN + 10, y - 9, 8)
        y = _wrap(c, text, MARGIN + 26, y - 13, 'DejaVuSans', 12, CONTENT_W - 26,
                  15.5, INK) - 6
    return y - 2


def b_divisories(c, y, b):
    """Les notes ja hi son, pero falten les linies divisories: el nen les
       dibuixa contant els temps. La primera ja esta posada, com a exemple."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    clau = b.get('clau', 'treble')
    gap = 12.0
    y -= gap * 1.8
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap, clau)
    draw_time_sig(c, MARGIN + gap * 3.6, bot, gap)
    durs = {'w': 4.0, 'h': 2.0, 'q': 1.0}
    notes = b['notes']                     # [(pitch, dur)]
    total = sum(durs[d] for _p, d in notes)
    x0 = MARGIN + gap * 6.4
    ample = CONTENT_W - gap * 6.4 - 10
    # cada nota ocupa un lloc proporcional (amb un minim), i entre compas i
    # compas es deixa un forat per dibuixar-hi la linia
    forat = gap * 2.2
    n_comp = int(round(total / 4.0))
    util = ample - forat * (n_comp - 1)
    pes = [0.55 + 0.45 * durs[d] for _p, d in notes]
    escala = util / sum(pes)
    x, acum = x0, 0.0
    exemple = b.get('exemple', True)
    for (p, d), w in zip(notes, pes):
        _nota(c, x + w * escala * 0.35, top, bot, gap, p, clau, dur=d)
        x += w * escala
        acum += durs[d]
        if abs(acum % 4.0) < 1e-6 and acum < total - 1e-6:
            if exemple and acum == 4.0:
                draw_barline(c, x + forat / 2, top, bot)
            x += forat
    draw_barline(c, MARGIN + CONTENT_W - 4, top, bot, final=True)
    return _mes_baixa(bot, gap, [p for p, _d in notes], clau) - gap * 2.4


def _cap_sense_plica(c, cx, cy, gap):
    c.saveState()
    c.translate(cx, cy)
    c.rotate(20)
    c.setFillColor(INK)
    c.ellipse(-gap * 0.62, -gap * 0.42, gap * 0.62, gap * 0.42, fill=1, stroke=0)
    c.restoreState()


def b_posa_pliques(c, y, b):
    """Caps de nota sense plica: el nen hi dibuixa la plica, amunt o avall
       segons si la nota es per sota o per sobre de la linia del mig."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    clau = b.get('clau', 'treble')
    gap = 14.0
    y -= gap * 3.2
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap, clau)
    mig = bot + 2 * gap
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.2)
    c.setDash(4, 3)
    c.line(MARGIN + gap * 4.2, mig, MARGIN + CONTENT_W, mig)
    c.setDash()
    notes = b['notes']
    x0 = MARGIN + gap * 7.0
    pas = (CONTENT_W - gap * 8.6) / max(1, len(notes) - 1)
    for i, p in enumerate(notes):
        _cap_sense_plica(c, x0 + i * pas, note_y(bot, gap, p, clau), gap)
    return bot - gap * 3.6


def b_dibuixa(c, y, b):
    """Al reves: el nom ja hi es i el nen dibuixa la nota (una rodona) al seu
       lloc del pentagrama."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    clau = b.get('clau', 'treble')
    gap = 13.0
    y -= gap * 2.0
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap, clau)
    noms = b['noms']
    x0 = MARGIN + gap * 7.0
    pas = (CONTENT_W - gap * 8.6) / max(1, len(noms) - 1)
    base = bot - gap * 3.0
    for i, nom in enumerate(noms):
        c.setFont('DejaVuSans-Bold', 14)
        c.setFillColor(ACCENT)
        c.drawCentredString(x0 + i * pas, base, nom)
    return base - 18


def b_encercla(c, y, b):
    """Un pentagrama ple de notes: encercla les que diu l'enunciat."""
    y = _encap(c, y, b['num'], b['titol'], b.get('pista'))
    clau = b.get('clau', 'treble')
    gap = 12.0
    y -= gap * 1.6
    top, bot = _pauta(c, MARGIN, y, CONTENT_W, gap, clau)
    notes = b['notes']
    x0 = MARGIN + gap * 7.0
    pas = (CONTENT_W - gap * 8.6) / max(1, len(notes) - 1)
    for i, p in enumerate(notes):
        _nota(c, x0 + i * pas, top, bot, gap, p, clau)
    return _mes_baixa(bot, gap, notes, clau) - gap * 2.6


_ABC = 'ABCDEFGHILMNOPRSTU'


def b_sopa(c, y, b):
    """Sopa de lletres, nomes en horitzontal i en vertical (per a nens de sis
       anys la diagonal es massa)."""
    y = _encap(c, y, b['num'], b.get('titol', 'Sopa de lletres'), b.get('pista'))
    paraules = [p.upper() for p in b['paraules']]
    files, cols = b.get('files', 7), b.get('columnes', 14)
    rnd = random.Random(b.get('llavor', 3))
    g = [[None] * cols for _ in range(files)]
    for p in sorted(paraules, key=len, reverse=True):
        for _ in range(500):
            vert = rnd.random() < 0.4
            if vert and len(p) > files:
                vert = False
            f = rnd.randrange(files - (len(p) if vert else 1) + 1)
            co = rnd.randrange(cols - (1 if vert else len(p)) + 1)
            cel = [(f + (k if vert else 0), co + (0 if vert else k)) for k in range(len(p))]
            if all(g[a][bb] in (None, p[k]) for k, (a, bb) in enumerate(cel)):
                for k, (a, bb) in enumerate(cel):
                    g[a][bb] = p[k]
                break
        else:
            raise ValueError('no cap la paraula %s a la sopa' % p)
    costat = min(26.0, CONTENT_W / cols)
    x0 = MARGIN + (CONTENT_W - costat * cols) / 2
    for f in range(files):
        for co in range(cols):
            x, yy = x0 + co * costat, y - (f + 1) * costat
            c.setStrokeColor(RULE)
            c.setLineWidth(0.8)
            c.setFillColor(white)
            c.rect(x, yy, costat, costat, fill=1, stroke=1)
            c.setFont('DejaVuSans-Bold', costat * 0.56)
            c.setFillColor(INK)
            c.drawCentredString(x + costat / 2, yy + costat * 0.3, g[f][co] or rnd.choice(_ABC))
    yy = y - files * costat - 14
    pas = CONTENT_W / float(min(len(paraules), 5))
    for i, p in enumerate(paraules):
        col, fil = i % 5, i // 5
        x = MARGIN + col * pas
        c.setStrokeColor(NAVY_SOFT)
        c.setFillColor(white)
        c.rect(x, yy - fil * 20 - 12, 12, 12, fill=1, stroke=1)
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(NAVY)
        c.drawString(x + 18, yy - fil * 20 - 11, p)
    return yy - ((len(paraules) - 1) // 5 + 1) * 20 - 8


def b_endevina(c, y, b):
    """Endevinalles: la resposta lletra a lletra, una a cada casella."""
    y = _encap(c, y, b['num'], b.get('titol', 'Endevina qui sóc'), b.get('pista'))
    costat = 20.0
    for text, resposta in b['items']:
        nlet = len(resposta.replace(' ', ''))
        ample_cas = nlet * (costat + 3)
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 6, y - 7, 3, fill=1, stroke=0)
        yy = _wrap(c, text, MARGIN + 18, y - 11, 'DejaVuSans', 12,
                   CONTENT_W - 18 - ample_cas - 14, 15.5, INK)
        bx = W - MARGIN - ample_cas
        for k in range(nlet):
            _caixeta(c, bx + k * (costat + 3), y - costat - 2, costat, costat)
        y = min(yy, y - costat - 4) - 10
    return y


def b_vf(c, y, b):
    """Vertader o fals: rapid de fer i bo per repassar de memoria."""
    y = _encap(c, y, b['num'], b.get('titol', 'Vertader o fals?'), b.get('pista'))
    x_v, x_f = W - MARGIN - 58, W - MARGIN - 24
    c.setFont('DejaVuSans-Bold', 11)
    c.setFillColor(NAVY_SOFT)
    c.drawCentredString(x_v + 10, y - 6, 'V')
    c.drawCentredString(x_f + 10, y - 6, 'F')
    y -= 16
    for frase in b['frases']:
        yy = _wrap(c, frase, MARGIN + 12, y - 13, 'DejaVuSans', 12, x_v - MARGIN - 28, 15.5, INK)
        for bx in (x_v, x_f):
            _caixeta(c, bx, y - 20, 20, 20)
        y = min(yy, y - 22) - 6
    return y


def b_uneix(c, y, b):
    """Dues columnes de paraules per unir amb una ratlla."""
    y = _encap(c, y, b['num'], b.get('titol', 'Uneix'), b.get('pista'))
    esq, dre = b['esquerra'], b['dreta']
    fila = 26.0
    x_d = MARGIN + CONTENT_W * 0.58
    for i in range(len(esq)):
        fy = y - i * fila - 14
        c.setFont('DejaVuSans-Bold', _fit(esq[i], 'DejaVuSans-Bold', 12.5, CONTENT_W * 0.36))
        c.setFillColor(NAVY)
        c.drawString(MARGIN + 12, fy, esq[i])
        c.setFillColor(ACCENT)
        c.circle(MARGIN + CONTENT_W * 0.40, fy + 4, 4, fill=1, stroke=0)
        c.circle(x_d - 16, fy + 4, 4, fill=1, stroke=0)
        c.setFont('DejaVuSans', _fit(dre[i], 'DejaVuSans', 12, W - MARGIN - x_d))
        c.setFillColor(INK)
        c.drawString(x_d, fy, dre[i])
    return y - len(esq) * fila - 8


def b_quant_dura(c, y, b):
    """Quants temps dura cada figura (o cada silenci)? Una caixa a sota."""
    y = _encap(c, y, b['num'], b.get('titol', 'Quant dura?'), b.get('pista'))
    items = b['figures']
    gap = 11.0
    pas = CONTENT_W / float(len(items))
    cap_y = y - gap * 4.3
    for i, dur in enumerate(items):
        cx = MARGIN + (i + 0.5) * pas
        _figura(c, cx, cap_y, gap, dur)
        _caixeta(c, cx - 20, cap_y - gap * 4.2, 40, 26)
    return cap_y - gap * 4.2 - 14


def b_medalla(c, y, b):
    """La medalla del final de capitol: per pintar, amb el nom del capitol i
       la signatura de la profe. Es el que fa que el nen tanqui l'etapa."""
    h = 250
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 6, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3.5, h, fill=1, stroke=0)
    cx, cy, r = MARGIN + CONTENT_W * 0.36, y - 128, 74
    # les cintes
    c.setFillColor(white)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.6)
    for s in (-1, 1):
        p = c.beginPath()
        p.moveTo(cx + s * 22, cy - r + 10)
        p.lineTo(cx + s * 48, cy - r - 52)
        p.lineTo(cx + s * 30, cy - r - 40)
        p.lineTo(cx + s * 14, cy - r - 56)
        p.lineTo(cx + s * 2, cy - r + 6)
        p.close()
        c.drawPath(p, fill=1, stroke=1)
    c.setFillColor(white)
    c.setLineWidth(2.4)
    c.circle(cx, cy, r, fill=1, stroke=1)
    c.setLineWidth(1.2)
    c.circle(cx, cy, r - 10, fill=0, stroke=1)
    for k in range(5):
        a = math.radians(90 + k * 72)
        _estrella(c, cx + (r - 22) * math.cos(a) * 0.0 + (k - 2) * 20, cy + 34, 7)
    c.setFont('DejaVuSans-Bold', 15)
    c.setFillColor(NAVY)
    c.drawCentredString(cx, cy + 4, 'HO HE')
    c.drawCentredString(cx, cy - 15, 'ACONSEGUIT!')
    c.setFont('DejaVuSans-Bold', 9.5)
    c.setFillColor(ACCENT)
    c.drawCentredString(cx, cy - 36, 'CAPÍTOL %d' % b['capitol'])
    # a la dreta, en Mussol i la signatura
    xr = MARGIN + CONTENT_W * 0.68
    dibujar_buho(c, xr, y - 140, 110, 'happy')
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(NAVY_SOFT)
    c.drawString(xr - 10, y - h + 52, 'SIGNATURA DE LA PROFE')
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(xr - 10, y - h + 30, W - MARGIN - 16, y - h + 30)
    c.setFont('DejaVuSans', 10.5)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 18, y - h + 14, b.get('peu', 'Pinta la medalla i les estrelles!'))
    return y - h - 12


# --------------------------------------------------------------------------
# blocs que CREIXEN: ocupen el paper que sobra amb una cosa util (un espai per
# dibuixar, pentagrames buits, les ratlles per als apunts de la profe) en
# comptes de deixar mitja fulla en blanc o d'inflar els espais entre blocs
# --------------------------------------------------------------------------
def _capsa_etiqueta(c, y, etiqueta, text, filet):
    c.setFont('DejaVuSans-Bold', 9.8)
    c.setFillColor(filet)
    c.drawString(MARGIN + 16, y - 17, etiqueta)
    if text:
        return _wrap(c, text, MARGIN + 16, y - 33, 'DejaVuSans', 11.5, CONTENT_W - 30,
                     15.3, INK) + 4
    return y - 24


def b_quadre(c, y, b):
    """Un requadre per dibuixar-hi, amb la consigna a dalt."""
    alt_txt = 32 + 15.3 * len(_linies(b['text'], 'DejaVuSans', 11.5, CONTENT_W - 30))
    h = alt_txt + b.get('alt', 110.0) + b.get('extra', 0.0)
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3.5, h, fill=1, stroke=0)
    yy = _capsa_etiqueta(c, y, b.get('etiqueta', 'DIBUIXA AQUÍ'), b['text'], ACCENT)
    c.setFillColor(white)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.setDash(3, 3)
    c.roundRect(MARGIN + 14, y - h + 12, CONTENT_W - 26, yy - (y - h + 12) - 4, 4,
                fill=1, stroke=1)
    c.setDash()
    return y - h - 12


def b_pauta_buida(c, y, b):
    """Pentagrames buits per escriure-hi claus, notes o silencis. Se'n posen
       tants com hi caben."""
    gap = 12.0
    pas = gap * 4 + 34
    alt_txt = 32 + 15.3 * len(_linies(b['text'], 'DejaVuSans', 11.5, CONTENT_W - 30))
    n = max(1, int((b.get('extra', 0.0) + pas) // pas))
    n = min(n, b.get('max', 4))
    h = alt_txt + n * pas + 6
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - h, 3.5, h, fill=1, stroke=0)
    yy = _capsa_etiqueta(c, y, b.get('etiqueta', 'ESCRIU AQUÍ'), b['text'], BLUE)
    for k in range(n):
        top = yy - 14 - k * pas
        c.setFillColor(white)
        c.rect(MARGIN + 14, top - gap * 4 - 10, CONTENT_W - 26, gap * 4 + 20, fill=1, stroke=0)
        _pauta(c, MARGIN + 22, top, CONTENT_W - 42, gap, b.get('clau'))
    return y - h - 12


def b_apunts(c, y, b):
    """Ratlles per als apunts de la profe: que ha de repassar a casa."""
    h = b.get('alt', 96.0) + b.get('extra', 0.0)
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(NAVY_SOFT)
    c.rect(MARGIN, y - h, 3.5, h, fill=1, stroke=0)
    _capsa_etiqueta(c, y, b.get('etiqueta', 'LA PROFE M’APUNTA PER A AQUESTA SETMANA'),
                    None, NAVY_SOFT)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    ly = y - 50
    while ly > y - h + 12:
        c.line(MARGIN + 16, ly, W - MARGIN - 16, ly)
        ly -= 26
    return y - h - 12


CREIXEN = {'quadre', 'pauta_buida', 'apunts'}


BLOCS = {
    'misol': b_misol, 'nota': b_nota, 'joc': b_joc, 'sabies': b_sabies,
    'estrelles': b_estrelles,
    'teclat': b_teclat, 'mans': b_mans, 'pentagrama': b_pentagrama,
    'linies_espais': b_linies_espais, 'clau': b_clau, 'gran': b_gran,
    'targetes': b_targetes, 'escala': b_escala, 'figures': b_figures,
    'compas': b_compas, 'pliques': b_pliques,
    'exercici': b_exercici, 'passos': b_passos,
    'pinta': b_pinta, 'relaciona': b_relaciona, 'compta': b_compta,
    'cami': b_cami, 'teclat_pinta': b_teclat_pinta, 'dibuixa': b_dibuixa,
    'encercla': b_encercla, 'sopa': b_sopa, 'endevina': b_endevina, 'vf': b_vf,
    'uneix': b_uneix, 'quant_dura': b_quant_dura, 'medalla': b_medalla,
    'divisories': b_divisories, 'posa_pliques': b_posa_pliques,
    'quadre': b_quadre, 'pauta_buida': b_pauta_buida, 'apunts': b_apunts,
}
SENSE_NUMERO |= CREIXEN
SENSE_NUMERO = {'misol', 'nota', 'joc', 'sabies', 'estrelles', 'teclat', 'mans',
                'pentagrama', 'linies_espais', 'clau', 'gran', 'targetes', 'escala',
                'figures', 'compas', 'pliques', 'medalla'}
# Els tipus que compten per a la norma de varietat de les fitxes
FITXA = {'pinta', 'relaciona', 'compta', 'cami', 'teclat_pinta', 'dibuixa',
         'encercla', 'sopa', 'endevina', 'vf', 'uneix', 'quant_dura',
         'divisories', 'posa_pliques'}


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
    creixen = [i for i, b in enumerate(blocs) if b['tipus'] in CREIXEN]
    if creixen and y_fi > OBJECTIU + 4:
        # el paper que sobra se l'emporten els blocs que creixen; el que no
        # aprofitin (els pentagrames van de sencer en sencer) es justifica
        extra = (y_fi - OBJECTIU - 10.0) / len(creixen)
        for i in creixen:
            blocs[i] = dict(blocs[i], extra=extra)
        prova = Canvas(io.BytesIO(), pagesize=(W, H))
        y_fi = _dibuixar(prova, capcalera(prova, cfg), blocs, 0.0)
    forats = max(1, len(blocs) - 1)
    aire = max(0.0, min(AIRE_MAX, (y_fi - OBJECTIU) / forats))

    y0 = capcalera(c, cfg)
    y_fi = _dibuixar(c, y0, blocs, aire)
    peu(c, num_pag)
    c.showPage()
    return y_fi, seguent
