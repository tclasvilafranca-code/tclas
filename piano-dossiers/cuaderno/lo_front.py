# -*- coding: utf-8 -*-
"""Pàgines inicials del dossier de Lola (8 anys): els colors de les notes i les figures i els temps."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from mayores_motor import (MARGIN, CONTENT_W, NAVY, NAVY_SOFT, INK, MUTED, PANEL, titulo_pag, _wrap,
                           BLANCO, OCRE, AZUL, VERDE, ROJO)
from notation import draw_staff, draw_clef, note_y, draw_system, GRAY
import tema_ca

COL = dict(C='#E4392B', D='#F28C0E', E='#F9C80E', F='#76B82A', G='#2E86C8', A='#A58AC9', B='#A7A397')
NOM = dict(C='DO', D='RE', E='MI', F='FA', G='SOL', A='LA', B='SI')


def _tecles(c, x, y, w, h):
    """Una octava de piano (Do a Do) amb les tecles blanques pintades i el seu nom a sota."""
    n = 8
    kw = w / n
    lletres = 'CDEFGABC'
    for i, l in enumerate(lletres):
        c.setFillColor(HexColor(COL[l]))
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.0)
        c.roundRect(x + i * kw, y, kw, h, 5, fill=1, stroke=1)
        c.setFillColor(INK)
        c.setFont('DejaVuSans-Bold', 10.5)
        c.drawCentredString(x + i * kw + kw / 2, y + 9, NOM[l])
    for i in (0, 1, 3, 4, 5):          # negres: entre Do-Re, Re-Mi, Fa-Sol, Sol-La, La-Si
        bx = x + (i + 1) * kw - kw * 0.3
        c.setFillColor(INK)
        c.roundRect(bx, y + h * 0.38, kw * 0.6, h * 0.62, 3, fill=1, stroke=0)


def _pauta(c, x, ytop, w, clau, notes, gap=8.0):
    """Pentagrama amb les set notes pintades; notes = [(pitch, lletra), ...]."""
    ys = draw_staff(c, x, ytop, w, gap)
    yb = ys[-1]
    draw_clef(c, x + 4, yb, gap, clau)
    paso = (w - 60) / len(notes)
    for k, (p, l) in enumerate(notes):
        cx = x + 56 + k * paso + paso / 2
        cy = note_y(yb, gap, p, clau)
        # linia addicional si cal (Do central i similars)
        if cy < yb - 0.1 or cy > ys[0] + 0.1:
            c.setStrokeColor(GRAY)
            c.setLineWidth(0.8)
            yy = cy
            c.line(cx - gap * 0.85, yy, cx + gap * 0.85, yy)
        c.setFillColor(HexColor(COL[l]))
        c.setStrokeColor(HexColor('#1A2332'))
        c.setLineWidth(0.7)
        c.ellipse(cx - gap * 0.66, cy - gap * 0.5, cx + gap * 0.66, cy + gap * 0.5, fill=1, stroke=1)
        c.setFillColor(INK)
        c.setFont('DejaVuSans-Bold', 8.2)
        c.drawCentredString(cx, yb - gap * 2.6 if cy >= yb - 1 else cy - gap * 1.7, NOM[l])
    return yb


def pag_colors(c, n, marco_pag, misol_pie):
    marco_pag(c, n, 'Els colors de les notes')
    y = titulo_pag(c, 'Els colors de les notes',
                   'Cada nota té un nom i un color. A totes les partitures d\'aquest dossier les notes '
                   'estan pintades així. Aprendre-les serà un joc!')
    y -= 14
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'AL PIANO: LES TECLES BLANQUES')
    _tecles(c, MARGIN, y - 134, CONTENT_W, 120)
    y -= 154
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - 46, CONTENT_W, 46, 4, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(MARGIN, y - 46, 3, 46, fill=1, stroke=0)
    _wrap(c, "Troba el DO: és la tecla blanca que hi ha just a l'esquerra del grup de DUES tecles negres. "
             "Les notes segueixen sempre el mateix ordre: DO, RE, MI, FA, SOL, LA, SI i, després, torna el DO.",
          MARGIN + 14, y - 14, 'DejaVuSans', 8.6, CONTENT_W - 28, 12, INK)
    y -= 66
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'A LA PAUTA: MÀ DRETA (CLAU DE SOL)')
    y -= 22
    notes_d = [('C4', 'C'), ('D4', 'D'), ('E4', 'E'), ('F4', 'F'), ('G4', 'G'), ('A4', 'A'), ('B4', 'B')]
    yb = _pauta(c, MARGIN, y, CONTENT_W, 'treble', notes_d, 9.0)
    y = yb - 58
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'A LA PAUTA: MÀ ESQUERRA (CLAU DE FA)')
    y -= 22
    notes_e = [('C3', 'C'), ('D3', 'D'), ('E3', 'E'), ('F3', 'F'), ('G3', 'G'), ('A3', 'A'), ('B3', 'B')]
    yb = _pauta(c, MARGIN, y, CONTENT_W, 'bass', notes_e, 9.0)
    y = yb - 50
    misol_pie(c, y, "Si t'oblides d'una nota, mira el seu color! Passa el dit sobre el piano del DO al SI "
                    "dient els noms en veu alta: DO, RE, MI... Ho fas servir cada dia i en una setmana "
                    "te'ls saps tots.", 'happy', 62.0)
    c.showPage()


FIGURES = [
    ('RODONA', 'dura 4 temps', [{'pitch': 'B4', 'dur': 'w'}], '1 - 2 - 3 - 4', OCRE),
    ('BLANCA', 'dura 2 temps', [{'pitch': 'B4', 'dur': 'h'}, {'pitch': 'B4', 'dur': 'h'}], '1-2  ·  3-4', AZUL),
    ('NEGRA', 'dura 1 temps', [{'pitch': 'B4', 'dur': 'q'}] * 4, '1  ·  2  ·  3  ·  4', VERDE),
    ('CORXERA', 'dura mig temps',
     [{'pitch': 'B4', 'dur': 'e', 'beam': g} for g in (0, 0, 1, 1, 2, 2, 3, 3)], '1-i  ·  2-i  ·  3-i  ·  4-i', ROJO),
    ('NEGRA AMB PUNTET', 'dura 1 temps i mig',
     [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}, {'pitch': 'B4', 'dur': 'q'},
      {'pitch': 'B4', 'dur': 'q'}], '1 - i  ·  2-i  ·  3  ·  4', OCRE),
    ('SILENCI DE NEGRA', 'un temps sense tocar',
     [{'rest': True, 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'},
      {'pitch': 'B4', 'dur': 'q'}], '(1)  ·  2  ·  3  ·  4', AZUL),
]


def pag_figures(c, n, marco_pag, misol_pie):
    marco_pag(c, n, 'Quant dura cada nota')
    y = titulo_pag(c, 'Quant dura cada nota',
                   'La forma de la nota ens diu quants temps ha de sonar. Compta en veu alta i '
                   'dóna un petit cop de peu a cada número.')
    y -= 10
    for nom, desc, ev, compta, col in FIGURES:
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - 78, CONTENT_W, 78, 5, fill=1, stroke=0)
        c.setFillColor(col)
        c.rect(MARGIN, y - 78, 3.2, 78, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 11)
        c.setFillColor(NAVY)
        c.drawString(MARGIN + 14, y - 20, nom)
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + 14, y - 33, desc)
        c.setFont('DejaVuSans-Bold', 9.6)
        c.setFillColor(col)
        c.drawString(MARGIN + 14, y - 56, compta)
        draw_system(c, MARGIN + 190, y - 22, CONTENT_W - 204, 6.2, ev, clef='treble', time_sig=(4, 4))
        y -= 86
    misol_pie(c, y - 2, "Una blanca val dues negres, i una negra val dues corxeres. Així, tot encaixa "
                        "com un trencaclosques!", 'normal', 58.0)
    c.showPage()
