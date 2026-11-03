# -*- coding: utf-8 -*-
"""Seccio d'exercicis de base del dossier d'Alba (23 anys, comença ara): postura i dits, notes, figures, una mà sola,
   les dues mans, escales, acords, ritme i lectura, i un pla de practica setmanal.
   Tot sobre la posicio de cinc dits de Do i les escales de Do i Sol major (el que es fa al principi)."""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
from reportlab.lib.colors import HexColor
from mayores_motor import (MARGIN, CONTENT_W, NAVY, NAVY_SOFT, INK, MUTED, PANEL, titulo_pag, _wrap, BLANCO,
                           OCRE, AZUL, VERDE, ROJO, GRIS)
from page_layout_common import system_block, grand_staff_block
import nens_dib
import lo_front

GAP = 8.4


def ev(p, d='q', num=None, **kw):
    e = {'pitch': p, 'dur': d}
    if num:
        e['number'] = num
    e.update(kw)
    return e


def serie(notes, dur='q', dits=None):
    out = []
    for i, p in enumerate(notes):
        out.append(ev(p, dur, dits[i] if dits else None))
    return out


def _encap(c, y, txt, col=NAVY_SOFT):
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(col)
    c.drawString(MARGIN, y, txt)


def _nota(c, y, txt, h=None):
    """Caixeta amb un consell, retorna la y de sota."""
    from reportlab.pdfbase.pdfmetrics import stringWidth
    lin = max(1, int(stringWidth(txt, 'DejaVuSans', 8.4) / (CONTENT_W - 28)) + 1)
    h = h or 14 + 11.5 * lin
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    _wrap(c, txt, MARGIN + 14, y - 13, 'DejaVuSans', 8.4, CONTENT_W - 28, 11.5, INK)
    return y - h - 12


# ---------------------------------------------------------------- pagines
def pag_postura(c, n, marco_pag):
    marco_pag(c, n, 'Postura, mans i dits')
    y = titulo_pag(c, 'Postura, mans i dits',
                   'Abans de tocar una nota: com seure, com posar les mans i com es diuen els dits.')
    y -= 14
    _encap(c, y, 'COM SEURE I COM POSAR LES MANS')
    y -= 8
    items = ['Seu a la part davantera de la banqueta, amb l\'esquena dreta però relaxada.',
             'Els avantbraços, paral·lels al terra: els colzes a l\'alçada del teclat.',
             'Les espatlles baixes i el coll lliure. Els peus plans a terra.',
             'Els dits, arrodonits, com si portessis una pilota petita a la mà. Només toca la tecla la punteta del dit.',
             'El canell, a l\'altura de la mà: ni caigut ni aixecat. Les ungles, curtes.']
    for t in items:
        y = _wrap(c, '•  ' + t, MARGIN + 8, y - 6, 'DejaVuSans', 9, CONTENT_W - 16, 12.4, INK)
    y -= 12
    _encap(c, y, 'ELS DITS TENEN NÚMERO (ELS DUES MANS IGUAL: 1 = POLZE)')
    y -= 6
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(NAVY)
    c.drawCentredString(MARGIN + 120, y - 14, 'MÀ ESQUERRA')
    c.drawCentredString(MARGIN + 383, y - 14, 'MÀ DRETA')
    nens_dib.ma_real(c, MARGIN + 120, y - 178, 0.95, esq=True, dits=True, color=False)
    nens_dib.ma_real(c, MARGIN + 383, y - 178, 0.95, esq=False, dits=True, color=False)
    y -= 268
    _encap(c, y, 'POSICIÓ DE CINC DITS SOBRE EL DO')
    y -= 30
    kx, kw, kh = MARGIN + 40, 44, 54
    for lab, esq in (('MÀ DRETA', False), ('MÀ ESQUERRA', True)):
        c.setFont('DejaVuSans-Bold', 8)
        c.setFillColor(NAVY_SOFT)
        c.drawString(MARGIN, y - kh / 2 - 3, lab)
        nombres = ['DO', 'RE', 'MI', 'FA', 'SOL']
        dits = [1, 2, 3, 4, 5] if not esq else [5, 4, 3, 2, 1]
        for i in range(5):
            c.setFillColor(BLANCO)
            c.setStrokeColor(NAVY)
            c.setLineWidth(1)
            c.roundRect(kx + 90 + i * kw, y - kh, kw, kh, 4, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.circle(kx + 90 + i * kw + kw / 2, y - 14, 9, fill=1, stroke=0)
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSans-Bold', 9)
            c.drawCentredString(kx + 90 + i * kw + kw / 2, y - 17, str(dits[i]))
            c.setFillColor(INK)
            c.setFont('DejaVuSans-Bold', 8.4)
            c.drawCentredString(kx + 90 + i * kw + kw / 2, y - kh + 8, nombres[i])
        y -= kh + 16
    y = _nota(c, y - 4, "Cada dit, una tecla: el polze (1) de la mà dreta és al DO del mig del piano (el «Do central»). La mà esquerra "
                        "té el dit petit (5) al DO d'una octava més greu i el polze (1) al SOL.")
    c.showPage()


def pag_ex_dreta(c, n, marco_pag):
    marco_pag(c, n, 'Mà dreta sola')
    y = titulo_pag(c, 'Mà dreta sola',
                   'Posició de cinc dits sobre el Do central. Toca lent, comptant en veu alta, i amb el número de dit a sobre.')
    y -= 16
    x0, w0 = MARGIN, CONTENT_W
    y = system_block(c, x0, w0, y, GAP, 'a) Pujar i baixar: una nota per dit',
                     serie(['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4'], 'q', [1, 2, 3, 4, 5, 4, 3, 2])
                     + [ev('C4', 'w', 1)])
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'b) Salts de tercera (saltant un dit)',
                     serie(['C4', 'E4', 'D4', 'F4', 'E4', 'G4', 'F4', 'E4'], 'q', [1, 3, 2, 4, 3, 5, 4, 3])
                     + [ev('D4', 'h', 2), ev('C4', 'h', 1)])
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'c) Notes repetides i valors llargs',
                     [ev('C4', 'q', 1), ev('C4', 'q', 1), ev('D4', 'h', 2), ev('E4', 'q', 3), ev('E4', 'q', 3),
                      ev('F4', 'h', 4), ev('G4', 'w', 5)])
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'd) Cinc dits en ordre canviat (per no memoritzar-ho)',
                     serie(['C4', 'G4', 'D4', 'F4', 'E4', 'E4', 'F4', 'D4'], 'q', [1, 5, 2, 4, 3, 3, 4, 2])
                     + [ev('C4', 'w', 1)])
    y -= 8
    y = _nota(c, y, "Repeteix cada exercici quatre vegades. La primera, ben lent; la quarta, una mica més de pressa, "
                    "però sense equivocar-te. Si falles, torna a començar: el que compta és la repetició neta.")
    _encap(c, y, 'COM DE BÉ ET SURT?')
    y -= 8
    for k, t in enumerate(['a) ', 'b) ', 'c) ', 'd) ']):
        c.setFillColor(NAVY)
        c.setFont('DejaVuSans-Bold', 9)
        c.drawString(MARGIN + 6 + k * 120, y - 8, t)
        for j in range(4):
            c.setStrokeColor(NAVY)
            c.roundRect(MARGIN + 22 + k * 120 + j * 22, y - 14, 12, 12, 2, fill=0, stroke=1)
    c.showPage()


def pag_ex_esquerra(c, n, marco_pag):
    marco_pag(c, n, 'Mà esquerra sola')
    y = titulo_pag(c, 'Mà esquerra sola',
                   'La mà esquerra llegeix en clau de fa. El dit 5 va al Do greu i el polze (1) al Sol: justament al revés de la dreta.')
    y -= 16
    x0, w0 = MARGIN, CONTENT_W
    y = system_block(c, x0, w0, y, GAP, 'a) Pujar i baixar: una nota per dit',
                     serie(['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3'], 'q', [5, 4, 3, 2, 1, 2, 3, 4])
                     + [ev('C3', 'w', 5)], clef='bass')
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'b) Salts de tercera',
                     serie(['C3', 'E3', 'D3', 'F3', 'E3', 'G3', 'F3', 'E3'], 'q', [5, 3, 4, 2, 3, 1, 2, 3])
                     + [ev('D3', 'h', 4), ev('C3', 'h', 5)], clef='bass')
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'c) Notes repetides i valors llargs',
                     [ev('C3', 'q', 5), ev('C3', 'q', 5), ev('D3', 'h', 4), ev('E3', 'q', 3), ev('E3', 'q', 3),
                      ev('F3', 'h', 2), ev('G3', 'w', 1)], clef='bass')
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'd) Un acord trencat: Do-Mi-Sol (cinc, tres, un)',
                     serie(['C3', 'E3', 'G3', 'E3', 'C3', 'E3', 'G3', 'E3'], 'q', [5, 3, 1, 3, 5, 3, 1, 3])
                     + [ev('C3', 'w', 5)], clef='bass')
    y -= 8
    y = _nota(c, y, "La mà esquerra sol ser la que més costa: és normal. Dedica-li els primers cinc minuts de cada dia, quan encara tens "
                    "el cap fresc.")
    c.showPage()


def pag_ex_juntes(c, n, marco_pag):
    marco_pag(c, n, 'Les dues mans juntes')
    y = titulo_pag(c, 'Les dues mans juntes',
                   'Primer a poc a poc, amb cada mà sabuda per separat. Mira només una pauta cada vegada, sense córrer.')
    y -= 16
    x0, w0 = MARGIN, CONTENT_W
    t = serie(['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4'], 'q', [1, 2, 3, 4, 5, 4, 3, 2]) + [ev('C4', 'w', 1)]
    b = serie(['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3'], 'q', [5, 4, 3, 2, 1, 2, 3, 4]) + [ev('C3', 'w', 5)]
    y = grand_staff_block(c, x0, w0, y, GAP, t, b, 'a) El mateix moviment: les dues mans pugen i baixen a l\'octava')
    y -= 6
    t2 = serie(['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4'], 'q', [1, 2, 3, 4, 5, 4, 3, 2]) + [ev('C4', 'w', 1)]
    b2 = serie(['C4', 'B3', 'A3', 'G3', 'F3', 'G3', 'A3', 'B3'], 'q', [1, 2, 3, 4, 5, 4, 3, 2]) + [ev('C4', 'w', 1)]
    y = grand_staff_block(c, x0, w0, y, GAP, t2, b2, 'b) Moviment contrari: les mans surten del Do central i s\'obren')
    y -= 6
    t3 = [ev('C4', 'q', 1), ev('D4', 'q', 2), ev('E4', 'q', 3), ev('F4', 'q', 4),
          {'rest': True, 'dur': 'w'}]
    b3 = [{'rest': True, 'dur': 'w'}, ev('C3', 'q', 5), ev('D3', 'q', 4), ev('E3', 'q', 3), ev('F3', 'q', 2)]
    y = grand_staff_block(c, x0, w0, y, GAP, t3, b3, 'c) Per torns: primer la dreta, després l\'esquerra')
    y -= 6
    t4 = [ev('C4', 'q', 1), ev('D4', 'q', 2), ev('E4', 'q', 3), ev('D4', 'q', 2), ev('C4', 'w', 1)]
    b4 = [{'pitches': ['C3', 'G3'], 'dur': 'w'}, {'pitches': ['C3', 'G3'], 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, GAP, t4, b4, 'd) Melodia a la dreta, acord llarg a l\'esquerra (quinta Do-Sol)')
    y -= 8
    _nota(c, y, "Quan una mà et surti sola, afegeix l'altra: «mà sola, mà sola, juntes». Si t'equivoques, no paris: "
                "torna a començar el compàs. El cervell aprèn a recuperar-se.")
    c.showPage()


def pag_escales(c, n, marco_pag):
    marco_pag(c, n, 'Escales de Do i Sol major')
    y = titulo_pag(c, 'Escales de Do i Sol major',
                   'Una escala és una escalera de vuit notes. Mira com passa el polze per sota: dits 1-2-3, polze, 1-2-3-4-5.')
    y -= 16
    x0, w0 = MARGIN, CONTENT_W
    up = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    dn = ['C5', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4']
    ed = [1, 2, 3, 1, 2, 3, 4, 5]
    ed2 = [5, 4, 3, 2, 1, 3, 2, 1]
    dd = [5, 4, 3, 2, 1, 3, 2, 1]
    dg = 7.0
    def par(tit, up_n, dn_n, up_d, dn_d, clef='treble', ks=None):
        nonlocal y
        y = system_block(c, x0, w0, y, dg, tit + ' · pujant', serie(up_n, 'q', up_d), clef=clef, key_sig=ks)
        y = system_block(c, x0, w0, y, dg, tit + ' · baixant', serie(dn_n, 'q', dn_d), clef=clef, key_sig=ks)
        y -= 6
    par('Do major · mà dreta: 1-2-3, polze, 1-2-3-4-5', up, dn, ed, [5, 4, 3, 2, 1, 3, 2, 1])
    par('Do major · mà esquerra: 5-4-3-2-1, polze, 3-2-1', ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4'],
        ['C4', 'B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3'], ed2, [1, 2, 3, 1, 2, 3, 4, 5], 'bass')
    par('Sol major · mà dreta (amb Fa♯)', ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5'],
        ['G5', 'F#5', 'E5', 'D5', 'C5', 'B4', 'A4', 'G4'], ed, [5, 4, 3, 2, 1, 3, 2, 1], 'treble', 'Sol mayor')
    par('Sol major · mà esquerra (amb Fa♯)', ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F#4', 'G4'],
        ['G4', 'F#4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3'], ed2, [1, 2, 3, 1, 2, 3, 4, 5], 'bass', 'Sol mayor')
    y -= 8
    y = _nota(c, y, "A Sol major, el Fa és sempre Fa♯ (una tecla negra): la partitura ho avisa amb un ♯ al principi de cada pentagrama. "
                    "Aquesta marca s'anomena «armadura».")
    c.showPage()


def pag_acords(c, n, marco_pag):
    marco_pag(c, n, 'Acords i arpegis')
    y = titulo_pag(c, 'Acords i arpegis',
                   'Un acord són tres notes que sonen juntes: la primera, una altra a dues tecles blanques i una tercera a quatre. '
                   'Un arpegi és el mateix acord tocat nota a nota.')
    y -= 16
    x0, w0 = MARGIN, CONTENT_W
    y = system_block(c, x0, w0, y, GAP, 'a) Acords de Do, Fa i Sol a la mà dreta (tres dits alhora: 1-3-5)',
                     [{'pitches': ['C4', 'E4', 'G4'], 'dur': 'h'}, {'pitches': ['F4', 'A4', 'C5'], 'dur': 'h'},
                      {'pitches': ['G4', 'B4', 'D5'], 'dur': 'h'}, {'pitches': ['C4', 'E4', 'G4'], 'dur': 'h'}])
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'b) Els mateixos acords a la mà esquerra (dits 5-3-1)',
                     [{'pitches': ['C3', 'E3', 'G3'], 'dur': 'h'}, {'pitches': ['F3', 'A3', 'C4'], 'dur': 'h'},
                      {'pitches': ['G3', 'B3', 'D4'], 'dur': 'h'}, {'pitches': ['C3', 'E3', 'G3'], 'dur': 'h'}],
                     clef='bass')
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'c) Arpegi de Do a la dreta: 1-3-5-3',
                     serie(['C4', 'E4', 'G4', 'E4', 'C4', 'E4', 'G4', 'E4'], 'q', [1, 3, 5, 3, 1, 3, 5, 3])
                     + [ev('C4', 'w', 1)])
    y -= 6
    y = system_block(c, x0, w0, y, GAP, 'd) Arpegi de Do a l\'esquerra: 5-3-1-3',
                     serie(['C3', 'E3', 'G3', 'E3', 'C3', 'E3', 'G3', 'E3'], 'q', [5, 3, 1, 3, 5, 3, 1, 3])
                     + [ev('C3', 'w', 5)], clef='bass')
    y -= 6
    t = [{'pitches': ['C4', 'E4', 'G4'], 'dur': 'h'}, {'pitches': ['F4', 'A4', 'C5'], 'dur': 'h'},
         {'pitches': ['G4', 'B4', 'D5'], 'dur': 'h'}, {'pitches': ['C4', 'E4', 'G4'], 'dur': 'h'},
         {'pitches': ['C4', 'E4', 'G4'], 'dur': 'w'}]
    b = [ev('C3', 'h', 5), ev('F3', 'h', 5), ev('G3', 'h', 5), ev('C3', 'h', 5), ev('C3', 'w', 5)]
    y = grand_staff_block(c, x0, w0, y, GAP, t, b,
                          'e) Una cançó de tres acords: la dreta toca l\'acord, l\'esquerra la nota greu (Do - Fa - Sol - Do)')
    y -= 8
    _nota(c, y, "Do, Fa i Sol (acords I, IV i V) són els tres acords amb què es poden acompanyar moltíssimes cançons. "
                "Si els dominis, ja pots acompanyar «Oh When the Saints» o «Silent Night» sense mirar.")
    c.showPage()


def pag_ritme(c, n, marco_pag):
    marco_pag(c, n, 'Ritme i lectura')
    y = titulo_pag(c, 'Ritme i lectura',
                   'Primer el ritme, sense notes: dóna palmes comptant en veu alta. Després llegeix les notes i escriu-ne el nom.')
    y -= 14
    x0, w0 = MARGIN, CONTENT_W
    q = lambda: ev('B4', 'q')
    h = lambda: ev('B4', 'h')
    e = lambda g: ev('B4', 'e', beam=g)
    _encap(c, y, 'RITME: DÓNA PALMES COMPTANT')
    y -= 12
    y = system_block(c, x0, w0, y, 6.8, 'a) 4/4 · negres i blanques: 1 · 2 · 3 · 4  |  1-2 · 3 · 4',
                     [q(), q(), q(), q(), h(), q(), q()])
    y -= 2
    y = system_block(c, x0, w0, y, 6.8, 'b) 4/4 · amb corxeres: 1 · 2-i · 3 · 4  |  1-i · 2-i · 3 · 4',
                     [q(), e(0), e(0), q(), q(), e(1), e(1), e(2), e(2), q(), q()])
    y -= 2
    y = system_block(c, x0, w0, y, 6.8, 'c) 3/4 · «1-2-3»: negra · negra · negra  |  blanca · negra  |  blanca amb puntet',
                     [q(), q(), q(), h(), q(), ev('B4', 'h.')], time_sig=(3, 4))
    y -= 2
    y = system_block(c, x0, w0, y, 6.8, 'd) Amb silencis: (1) · 2 · 3 · 4  |  1 · (2) · 3 · 4',
                     [{'rest': True, 'dur': 'q'}, q(), q(), q(), q(), {'rest': True, 'dur': 'q'}, q(), q()])
    y -= 8
    _encap(c, y, 'LECTURA: ESCRIU EL NOM DE CADA NOTA')
    y -= 12
    sol = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do']
    lect = [(['E4', 'G4', 'C4', 'D4', 'F4', 'A4', 'B4', 'G4'], 'treble', 'a) Clau de sol: '),
            (['G3', 'C3', 'E3', 'F3', 'D3', 'B3', 'A3', 'C3'], 'bass', 'b) Clau de fa: ')]
    nom = {'C': 'Do', 'D': 'Re', 'E': 'Mi', 'F': 'Fa', 'G': 'Sol', 'A': 'La', 'B': 'Si'}
    sols = []
    for notes, clef, cap in lect:
        y = system_block(c, x0, w0, y, 7.0, cap + 'escriu sota de cada nota la seva lletra (Do, Re, Mi…)',
                         [ev(p, 'q') for p in notes[:4]] + [ev(p, 'q') for p in notes[4:]], clef=clef)
        c.setStrokeColor(GRIS)
        c.setLineWidth(0.8)
        for k in range(8):
            c.line(MARGIN + 52 + k * 55, y + 6, MARGIN + 52 + k * 55 + 44, y + 6)
        sols.append(' '.join(nom[p[0]] for p in notes))
        y -= 10
    y -= 2
    c.setFont('DejaVuSans', 6.8)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y - 6, 'Solució (per a qui corregeixi): a) ' + sols[0] + '   ·   b) ' + sols[1])
    c.showPage()


def pag_pla(c, n, marco_pag):
    marco_pag(c, n, 'La rutina de la setmana')
    y = titulo_pag(c, 'La rutina de la setmana',
                   'És millor tocar vint minuts cada dia que dues hores un sol dia. Aquest quadre t\'ajuda a no perdre el fil.')
    y -= 16
    _encap(c, y, 'UNA SESSIÓ DE 20 MINUTS')
    y -= 6
    parts = [('5′', 'Escalfament', 'Una escala o un exercici d\'aquestes pàgines, mà sola, molt lent.', AZUL),
             ('7′', 'La peça', 'El bloc de la setmana: mà esquerra, mà dreta i després juntes.', OCRE),
             ('5′', 'Lectura', 'Cinc notes soltes de la partitura: llegeix-les en veu alta sense tocar.', VERDE),
             ('3′', 'Final', 'Toca el que ja saps de memòria i gaudeix-ne!', ROJO)]
    ancho = (CONTENT_W - 3 * 8) / 4
    x = MARGIN
    for t, tit, txt, col in parts:
        c.setFillColor(PANEL)
        c.roundRect(x, y - 92, ancho, 92, 5, fill=1, stroke=0)
        c.setFillColor(col)
        c.rect(x, y - 92, ancho, 3, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 20)
        c.drawString(x + 10, y - 30, t)
        c.setFont('DejaVuSerif-Bold', 9.4)
        c.setFillColor(NAVY)
        c.drawString(x + 10, y - 46, tit)
        _wrap(c, txt, x + 10, y - 58, 'DejaVuSans', 7.6, ancho - 18, 9.6, INK)
        x += ancho + 8
    y -= 118
    _encap(c, y, 'LA MEVA SETMANA (MARCA CADA DIA)')
    y -= 8
    dies = ['Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres', 'Dissabte', 'Diumenge']
    cols = ['Escalfament', 'Peça', 'Lectura', 'Minuts']
    cx = [MARGIN + 100, MARGIN + 190, MARGIN + 260, MARGIN + 330]
    c.setFont('DejaVuSans-Bold', 7.4)
    c.setFillColor(MUTED)
    for x, t in zip(cx, cols):
        c.drawString(x, y - 4, t)
    y -= 12
    for d in dies:
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - 28, CONTENT_W, 28, 4, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 9.6)
        c.setFillColor(NAVY)
        c.drawString(MARGIN + 10, y - 18, d)
        c.setStrokeColor(NAVY)
        c.setLineWidth(0.9)
        for x in cx[:3]:
            c.roundRect(x + 12, y - 21, 13, 13, 2, fill=0, stroke=1)
        c.setStrokeColor(GRIS)
        c.line(cx[3], y - 20, cx[3] + 40, y - 20)
        y -= 32
    y -= 6
    y = _nota(c, y, "Tres consells que funcionen: (1) abans de tocar, mira on són els compassos difícils; (2) toca-ho lent fins que et surti "
                    "tres vegades seguides sense error; (3) si no ho veus clar, toca només dos compassos, però bé.")
    _nota(c, y, "Quan notis que un exercici ja et surt sol, no el deixis: passa'l al final de la sessió com a «bis».")
    c.showPage()
