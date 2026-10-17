# -*- coding: utf-8 -*-
"""Capítol 3 · Les notes i els seus colors — temes 8 a 13 (teoria + jocs). Les pàgines de notes van a COLOR."""
from nens_t02 import *                                            # noqa: F401,F403
from nens_jocs2 import p_cruci, p_cami, p_intrus, p_mosaic, p_laberint, HEART, HOUSE
from nens_t01 import pagina_jocs
from nens_tclas import (pill_dit, ORDRE, cap, nota, gran_pauta)
import nens_tclas as _nt

PRIMERA_MA = {  # dits de la posició de Do (mà dreta 1-5, mà esquerra 5-1) i de Sol
    'DO': (1, 5), 'RE': (2, 4), 'MI': (3, 3), 'FA': (4, 2), 'SOL': (5, 1),
}
TREBLE = {'DO': 'C4', 'RE': 'D4', 'MI': 'E4', 'FA': 'F4', 'SOL': 'G4', 'LA': 'A4', 'SI': 'B4'}
BASS = {'DO': 'C3', 'RE': 'D3', 'MI': 'E3', 'FA': 'F3', 'SOL': 'G3', 'LA': 'A2', 'SI': 'B2'}
UBIC_TECLA = {'DO': 'La blanca a l’esquerra de les DUES tecles negres.',
              'RE': 'La blanca del mig, entre les dues negres.',
              'MI': 'La blanca a la dreta de les dues negres.',
              'FA': 'La blanca a l’esquerra de les TRES tecles negres.',
              'SOL': 'Entre la 1a i la 2a negra del grup de tres.',
              'LA': 'Entre la 2a i la 3a negra del grup de tres.',
              'SI': 'La blanca a la dreta de les TRES tecles negres.'}
UBIC_PENT = {'DO': 'Just sota el pentagrama, amb una ratlleta.',
             'RE': 'Penja just sota la primera línia.',
             'MI': 'Viu a la primera línia del pentagrama.',
             'FA': 'Viu al primer espai del pentagrama.',
             'SOL': 'Viu a la segona línia: la de la clau de sol!',
             'LA': 'Viu al segon espai del pentagrama.',
             'SI': 'Viu a la tercera línia del pentagrama.'}
UBIC_FA = {'DO': 'A la clau de fa, el DO és al segon espai.', 'RE': 'A la clau de fa, el RE és a la tercera línia.',
           'MI': 'A la clau de fa, el MI és al tercer espai.', 'FA': 'A la clau de fa, el FA és a la quarta línia.',
           'SOL': 'A la clau de fa, el SOL és al quart espai.', 'LA': 'A la clau de fa, el LA és al primer espai.',
           'SI': 'A la clau de fa, el SI és a la segona línia.'}


def fitxa(c, x, yt, w, h, nom, dits=None, pos_dit=None):
    """Fitxa d'una nota: banda de color + teclat + pentagrama (clau de sol i de fa) + dits."""
    hexc = HexColor(COL[nom])
    ink = INK if nom == 'MI' else white
    rr(c, x + 3.4, yt - h - 3.4, w, h, 8, fill=SOMBRA, lw=0)
    rr(c, x, yt - h, w, h, 8, fill=white, lw=1.7, col=NAVY)
    rr(c, x, yt - 58, w, 58, 8, fill=hexc, lw=1.7, col=NAVY)
    c.setFillColor(hexc)
    c.rect(x + 1.5, yt - 58, w - 3, 14, stroke=0, fill=1)
    trac(c, 1.7, NAVY)
    c.line(x, yt - 58, x + w, yt - 58)
    txt(c, x + w / 2, yt - 39, nom, 36, SERIFB, ink, 'c')
    txt(c, x + w / 2, yt - 53, COLNOM[nom].upper(), 9.2, ETQ, ink, 'c')
    i = ORDRE.index(nom)
    etiqueta_sec(c, x + 12, yt - 79, 'AL TECLAT')
    kh = 56 if w < 200 else 62
    teclat(c, x + 12, yt - 88 - kh, w - 24, kh, nb=7, resalta={i: nom}, noms='resalta', color=True)
    yy = yt - 88 - kh - 18
    yy = par(c, x + 12, yy, UBIC_TECLA[nom], 11, w - 24, 13.5, SANS, INK)
    yy -= 8
    etiqueta_sec(c, x + 12, yy, 'AL PENTAGRAMA')
    gap = 7.2 if w < 200 else 8
    yy -= 16
    txt(c, x + 12, yy, 'mà dreta · clau de sol', 9.6, SANS, MUTED)
    yb = pauta(c, x + 12, yy - 8, w - 24, gap, 'treble', final=False)
    cap(c, x + w - 40, nt.note_y(yb, gap, TREBLE[nom]), gap, 'w', hexc)
    if TREBLE[nom] == 'C4':
        trac(c, 1.0, NAVY)
        c.line(x + w - 40 - gap * 1.3, nt.note_y(yb, gap, 'C4'), x + w - 40 + gap * 1.3, nt.note_y(yb, gap, 'C4'))
    yy = yb - gap * 1.8 - 12
    txt(c, x + 12, yy, 'mà esquerra · clau de fa', 9.6, SANS, MUTED)
    yb2 = pauta(c, x + 12, yy - 8, w - 24, gap, 'bass', final=False)
    cap(c, x + w - 40, nt.note_y(yb2, gap, BASS[nom], 'bass'), gap, 'w', hexc)
    yy = yb2 - 20
    par(c, x + 12, yy, UBIC_PENT[nom], 11, w - 24, 13.5, SANS, INK)
    if dits:
        hw = (w - 30) / 2.0
        pill_dit(c, x + 10, yt - h + 11, hw, 'dreta', dits[0])
        pill_dit(c, x + 20 + hw, yt - h + 11, hw, 'esq.', dits[1])


def escala_esglaons(c, x, ytop_base, noms, amp=69, hbase=16, hinc=14):
    for k, nom in enumerate(noms):
        hh = hbase + k * hinc
        bx = x + k * amp
        rr(c, bx, ytop_base, amp, hh, 2, fill=HexColor(COL[nom]), lw=1.5, col=NAVY)
        txt(c, bx + amp / 2, ytop_base + hh / 2 - 5, nom, 13, SERIFB, INK if nom == 'MI' else white, 'c')


# ======================================================================== TEMA 8 · Do, Re i Mi
def t8_teoria(c):
    pagina_tema(c, 8, 'Do, Re i Mi', 'Tres notes que sempre van juntes, com tres esglaons d’una escala.', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Hola! Avui coneixerem tres amigues que sempre van juntes: el Do, el Re i el Mi. Cada una té el seu color, '
         'la seva tecla i la seva casa al pentagrama.', color=True, size=12.5, h=86)
    cw = (CW - 28) / 3.0
    yt = Y(246)
    h = 408
    for k, nm in enumerate(('DO', 'RE', 'MI')):
        fitxa(c, M + k * (cw + 14), yt, cw, h, nm, PRIMERA_MA[nm])
    y2 = Y(670)
    h2 = 106
    panell(c, M, y2, 236, h2, 'PUGEN COM ESGLAONS')
    escala_esglaons(c, M + 14, y2 - h2 + 32, ['DO', 'RE', 'MI'], 69, 14, 13)
    txt(c, M + 14, y2 - h2 + 12, '← més GREU', 10.5, SANSB, NAVY_SOFT)
    txt(c, M + 14 + 207, y2 - h2 + 12, 'més AGUT →', 10.5, SANSB, NAVY_SOFT, 'r')
    caixa_t(c, M + 236 + 22, y2, CW - 236 - 22, h2, 'RECORDA',
            'El DO és sempre a l’esquerra de les DUES tecles negres. Troba’l i el RE i el MI són al costat!', 11.5)
    c.showPage()


def t8_jocs(c):
    pagina_jocs(c, 8, 'Do, Re i Mi · a jugar!', 'Agafa els llapis i fes-ho sense pressa.',
                'Un joc darrere l’altre! Si t’encalles, torna a mirar la pàgina de les notes: allà hi ha les pistes.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · pinta
    h = 114
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA LES TECLES', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta de vermell les DO, de taronja les RE i de groc les MI.', CW - 28)
    teclat(c, M + 14, yt - h + 12, 340, 46, nb=14, resalta={0: 'DO'}, noms='resalta', color=False)
    for k, nm in enumerate(('DO', 'RE', 'MI')):
        yy = yt - 54 - k * 22
        rr(c, M + 384, yy - 8, 18, 18, 9, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 410, yy - 3, nm, 13, SERIFB, INK)
        txt(c, M + 442, yy - 3, '= ' + {'DO': 'vermell', 'RE': 'taronja', 'MI': 'groc'}[nm], 11.5, SANS, NAVY_SOFT)
    # 2 sopa / 3 crucigrama
    h = 218
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'SOPA DE LLETRES', n=2)
    consigna(c, M + 14, yt - 40, 'Troba les 7 paraules (→ i ↓).', pw - 24)
    pal = ['PIANO', 'TECLA', 'COLOR', 'NOTA', 'DO', 'RE', 'MI']
    dibuixa_sopa(c, M + 12, yt - 52, sopa(pal, 8, seed=12), 20.5, 14)
    llista_paraules(c, M + 12 + 8 * 20.5 + 16, yt - 66, pal, 12, 22)
    panell(c, x2, yt, pw, h, 'CRUCIGRAMA', n=3)
    consigna(c, x2 + 14, yt - 40, 'Una lletra a cada quadret.', pw - 24)
    spec = [('NOTA', 0, 0, 'v', 1), ('TECLA', 2, 0, 'h', 2), ('COLOR', 2, 2, 'v', 3), ('AGUT', 2, 4, 'v', 4)]
    crucigrama(c, x2 + 12, yt - 52, spec, 21)
    pistes(c, x2 + 124, yt - 66, pw - 134, [('1 ↓', 'El Do és una…'), ('2 →', 'Premem una… del piano.'),
                                             ('3 ↓', 'El vermell és un…'), ('4 ↓', 'El contrari de GREU.')], 11.5, 14)
    # 4 uneix / 5 dibuixa
    h = 210
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=4)
    consigna(c, M + 14, yt - 40, 'Cada nom amb la seva nota.', pw - 28)

    def dib(c_, xr, yy, k):
        g = 7
        yb = pauta(c_, xr, yy + 14, 108, g, 'treble', final=False)
        cap(c_, xr + 82, nt.note_y(yb, g, ['E4', 'C4', 'D4'][k]), g, 'w', white)
        if k == 1:
            trac(c_, 1.0, NAVY)
            c_.line(xr + 82 - g * 1.3, nt.note_y(yb, g, 'C4'), xr + 82 + g * 1.3, nt.note_y(yb, g, 'C4'))
    uneix(c, M + 14, yt - 80, pw - 28, ['DO', 'RE', 'MI'], ['', '', ''], fila=46, ampl_esq=58, ampl_dre=108, dibuix_dre=dib)
    panell(c, x2, yt, pw, h, 'DIBUIXA LES NOTES', n=5)
    consigna(c, x2 + 14, yt - 40, 'Dibuixa cada nota a la seva casa.', pw - 28)
    for k, (clau, nomc) in enumerate((('treble', 'clau de sol'), ('bass', 'clau de fa'))):
        yy = yt - 72 - k * 64
        txt(c, x2 + 14, yy + 2, nomc, 10, SANS, MUTED)
        yb = pauta(c, x2 + 14, yy - 13, pw - 28, 6.5, clau, final=True)
        for j, nm in enumerate(('DO', 'RE', 'MI')):
            xx = x2 + 112 + j * 52
            caseta(c, xx - 20, yb - 26, 40, 17, 4)
            txt(c, xx, yb - 21.5, nm, 11, SANSB, NAVY_SOFT, 'c')
    c.showPage()


# ======================================================================== TEMA 9 · Fa i Sol
def mans_cinc(c, x, yt, w, h, titol='LA MÀ AMB CINC NOTES', color=True):
    panell(c, x, yt, w, h, titol)
    cw_ = (w - 42) / 2.0
    for k, (t, esq) in enumerate((('MÀ DRETA', False), ('MÀ ESQUERRA', True))):
        xx = x + 14 + k * (cw_ + 14)
        dits = {i: (5 - i if esq else i + 1) for i in range(5)}
        txt(c, xx, yt - 42, t, 10.2, ETQ, OCRE)
        teclat(c, xx, yt - h + 14, cw_, 60, nb=5, resalta={i: ORDRE[i] for i in range(5)}, noms='resalta', color=color, dits=dits)


def t9_teoria(c):
    pagina_tema(c, 9, 'Fa i Sol', 'Dues notes noves per completar la mà: ara en tenim cinc, una per a cada dit!', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Molt bé! Ja saps DO, RE i MI. Ara arriben dues amigues més: el FA i el SOL. Amb elles, '
         'cada dit de la mà té la seva nota.', color=True, size=12.5, h=80)
    cw = (CW - 18) / 2.0
    yt = Y(240)
    h = 392
    for k, nm in enumerate(('FA', 'SOL')):
        fitxa(c, M + k * (cw + 18), yt, cw, h, nm, PRIMERA_MA[nm])
    mans_cinc(c, M, Y(648), CW, 134)
    c.showPage()


def t9_jocs(c):
    pagina_jocs(c, 9, 'Fa i Sol · a jugar!', 'Ara ja coneixes cinc notes!',
                'DO, RE, MI, FA i SOL: cinc notes per a cinc dits. A veure si te les saps totes!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 112
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA LES TECLES', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta cada tecla del seu color: DO vermell, RE taronja, MI groc, FA verd i SOL blau.', CW - 28)
    teclat(c, M + 14, yt - h + 12, CW - 28, 44, nb=14, resalta={0: 'DO', 3: 'FA'}, noms='totes', color=False)
    h = 218
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'COMPLETA LA SÈRIE', n=2)
    consigna(c, M + 14, yt - 40, 'Escriu la nota que falta.', pw - 28)
    series = [['DO', 'RE', '', 'FA', 'SOL'], ['SOL', 'FA', 'MI', '', 'DO'], ['DO', '', 'MI', 'FA', ''], ['', 'FA', 'MI', 'RE', 'DO']]
    for k, sr in enumerate(series):
        yy = yt - 76 - k * 34
        for j, nm in enumerate(sr):
            xx = M + 14 + j * 44
            if nm:
                rr(c, xx, yy - 11, 40, 26, 6, fill=WARM2, lw=1.3, col=NAVY)
                txt(c, xx + 20, yy - 3.6, nm, 11.5, SANSB, NAVY, 'c')
            else:
                rr(c, xx, yy - 11, 40, 26, 6, fill=white, lw=1.6, col=NAVY, dash=(3, 2))
    p_cami(c, x2, yt, pw, h, 3, [(0, 0, 'DO'), (0, 1, 'RE'), (1, 1, 'MI'), (1, 2, 'FA'), (2, 2, 'SOL')])
    h = 210
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=4)
    consigna(c, M + 14, yt - 40, 'Cada nom amb la seva nota (clau de sol).', pw - 28)

    def dib(c_, xr, yy, k):
        g = 6.8
        yb = pauta(c_, xr, yy + 14, 108, g, 'treble', final=False)
        cap(c_, xr + 82, nt.note_y(yb, g, ['G4', 'F4', 'E4'][k]), g, 'w', white)
    uneix(c, M + 14, yt - 80, pw - 28, ['FA', 'SOL', 'MI'], ['', '', ''], fila=46, ampl_esq=58, ampl_dre=108, dibuix_dre=dib)
    panell(c, x2, yt, pw, h, 'EN MUSSOL S’HA EQUIVOCAT!', n=5)
    consigna(c, x2 + 14, yt - 40, 'Un nom està mal posat. Encercla’l i escriu el bo.', pw - 28)
    g = 7
    yb = pauta(c, x2 + 14, yt - 90, pw - 28, g, 'treble', final=True)
    for j, (p_, nm) in enumerate((('C4', 'DO'), ('F4', 'SOL'), ('G4', 'SOL'))):
        xx = x2 + 90 + j * 46
        cap(c, xx, nt.note_y(yb, g, p_), g, 'w', white)
        if p_ == 'C4':
            trac(c, 1.0, NAVY)
            c.line(xx - g * 1.3, nt.note_y(yb, g, 'C4'), xx + g * 1.3, nt.note_y(yb, g, 'C4'))
        txt(c, xx, yb - 28, nm, 12, SANSB, INK, 'c')
    linia(c, x2 + 14, yt - h + 28, pw - 28)
    c.showPage()


# ======================================================================== TEMA 10 · La i Si
def posicio_sol(c, x, yt, w, h):
    panell(c, x, yt, w, h, 'LA MÀ ES MOU: POSICIÓ DE SOL')
    cw_ = (w - 42) / 2.0
    noms5 = ['SOL', 'LA', 'SI', 'DO', 'RE']
    for k, (t, esq) in enumerate((('MÀ DRETA', False), ('MÀ ESQUERRA', True))):
        xx = x + 14 + k * (cw_ + 14)
        dits = {i: (5 - i if esq else i + 1) for i in range(5)}
        txt(c, xx, yt - 42, t + ' · el polze al SOL' if not esq else t + ' · el polze al RE', 10.2, ETQ, OCRE)
        teclat(c, xx, yt - h + 14, cw_, 60, nb=5, inici=4, resalta={i: noms5[i] for i in range(5)}, noms='resalta', color=True, dits=dits)


def t10_teoria(c):
    pagina_tema(c, 10, 'La i Si', 'Les dues últimes notes de la família: la mà es mou una mica!', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Ja només ens falten dues notes: el LA i el SI. Per tocar-les, la mà es mou: ara el polze '
         'se’n va al SOL!', color=True, size=12.5, h=80)
    cw = (CW - 18) / 2.0
    yt = Y(240)
    h = 392
    for k, (nm, dd) in enumerate((('LA', (2, 4)), ('SI', (3, 3)))):
        fitxa(c, M + k * (cw + 18), yt, cw, h, nm, dd)
    posicio_sol(c, M, Y(648), CW, 134)
    c.showPage()


def t10_jocs(c):
    pagina_jocs(c, 10, 'La i Si · a jugar!', 'Els colors de les notes ens ajuden.',
                'El LA és lila i el SI és gris. I els altres colors? Els recordes? Anem a jugar!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 114
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA LES TECLES', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta de lila les LA i de gris les SI.', CW - 28)
    teclat(c, M + 14, yt - h + 12, CW - 28, 46, nb=14, noms='totes')
    h = 218
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUINA NOTA ÉS?', n=2)
    consigna(c, M + 14, yt - 40, 'Escriu el nom de cada nota.', pw - 28)
    for k, p_ in enumerate(['A4', 'B4', 'G4', 'B4', 'A4', 'G4']):
        col, fila = k % 2, k // 2
        gx = M + 14 + col * 116
        gy = yt - 74 - fila * 46
        g = 6
        yb = pauta(c, gx, gy, 100, g, 'treble', final=False)
        cap(c, gx + 76, nt.note_y(yb, g, p_), g, 'w', white)
        linia(c, gx + 20, yb - 12, 60)
    panell(c, x2, yt, pw, h, 'CRUCIGRAMA DE COLORS', n=3)
    consigna(c, x2 + 14, yt - 40, 'De quin color és cada nota?', pw - 28)
    spec = [('GRIS', 1, 0, 'h', 1), ('GROC', 1, 0, 'v', 2), ('LILA', 0, 2, 'v', 3)]
    crucigrama(c, x2 + 14, yt - 56, spec, 24)
    pistes(c, x2 + 124, yt - 72, pw - 134, [('1 →', 'El color del SI.'), ('2 ↓', 'El color del MI.'), ('3 ↓', 'El color del LA.')], 11.5, 14)
    h = 200
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 52, pw - 14, ['El SI és de color lila.', 'Per tocar el LA i el SI, la mà es mou.',
                                               'El LA viu al segon espai.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'DIBUIXA LES NOTES', n=5)
    consigna(c, x2 + 14, yt - 40, 'Dibuixa el LA i el SI.', pw - 28)
    for k, nm in enumerate(('LA', 'SI')):
        yy = yt - 80 - k * 56
        yb = pauta(c, x2 + 14, yy, pw - 28, 6.5, 'treble', final=True)
        caseta(c, x2 + 100, yb - 26, 40, 17, 4)
        txt(c, x2 + 120, yb - 21.5, nm, 11, SANSB, NAVY_SOFT, 'c')
    c.showPage()


# ======================================================================== TEMA 11 · Les set notes
NOTES7 = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']


def nota_color(c, cx, cy, gap, nom, pitch, clef):
    """Nota rodona pintada del seu color (amb ratlleta si és el DO central)."""
    return nom


def t11_teoria(c):
    pagina_tema(c, 11, 'Les set notes', 'DO, RE, MI, FA, SOL, LA i SI: sempre en aquest ordre, i després torna a començar.', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Ja les coneixes totes! Mira-les juntes: set colors per a set notes, com un arc de Sant Martí '
         'musical.', color=True, size=12.5, h=80)
    yt = Y(240)
    h = 150
    panell(c, M, yt, CW, h, 'EL TECLAT DE COLORS')
    teclat(c, M + 14, yt - h + 14, CW - 28, 90, nb=14, resalta={i: NOTES7[i % 7] for i in range(14)}, noms='resalta', color=True)
    # pentagrames
    yt = Y(406)
    h = 232
    panell(c, M, yt, CW, h, 'AL PENTAGRAMA')
    g = 8.5
    for k, (clau, tit, pitches) in enumerate((('treble', 'mà dreta · clau de sol', ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']),
                                              ('bass', 'mà esquerra · clau de fa', ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']))):
        top = yt - 70 - k * 100
        txt(c, M + 14, top + 12, tit, 10, SANS, MUTED)
        yb = pauta(c, M + 14, top, CW - 28, g, clau, final=True)
        for j, p_ in enumerate(pitches):
            nm = NOTES7[j % 7]
            xx = M + 74 + j * 52
            cy_ = nt.note_y(yb, g, p_, clau)
            if p_ == 'C4' and clau == 'treble':
                trac(c, 1.0, NAVY)
                c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
            if p_ == 'C4' and clau == 'bass':
                trac(c, 1.0, NAVY)
                c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
            cap(c, xx, cy_, g, 'w', HexColor(COL[nm]))
            txt(c, xx, yb - 24, nm, 11, SANSB, NAVY, 'c')
    franja(c, M, Y(654), CW, 44, 'RECORDA', 'DO · RE · MI · FA · SOL · LA · SI … i després del SI torna a començar pel DO!', 12.2)
    franja(c, M, Y(712), CW, 72, 'SABIES QUE?',
           'Fa uns mil anys, un monjo anomenat Guido d’Arezzo va posar nom a les notes amb les primeres síl·labes d’un himne. '
           'Al principi el DO es deia «UT».', 12)
    c.showPage()


def mosaic_arc():
    """Graella d'un arc de Sant Martí 15×8; cada cel·la porta el codi de la nota que s'hi ha de pintar."""
    import math as _m
    g = []
    for r in range(8):
        fila = []
        for k in range(15):
            x, y = k - 7, 7 - r
            d = _m.hypot(x, y)
            if d < 7.5:
                fila.append(NOTES7[min(6, int(7.5 - d - 1e-9))])
            else:
                fila.append(None)
        g.append(fila)
    return g


def t11_jocs(c):
    pagina_jocs(c, 11, 'Les set notes · a jugar!', 'Set notes, set colors.',
                'Hi ha un dibuix amagat entre els quadrats! Pinta cada quadret del color de la seva nota i el descobriràs.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 232
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA PER NOTES', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta cada quadret del color de la seva nota.', 300)
    g = mosaic_arc()
    cs = 22
    gx, gy = M + 14, yt - 52
    for r, fila in enumerate(g):
        for k, cod in enumerate(fila):
            if cod:
                rr(c, gx + k * cs, gy - (r + 1) * cs, cs, cs, 0, fill=white, lw=1.2, col=NAVY)
                txt(c, gx + k * cs + cs / 2, gy - r * cs - cs + 7.3, cod, 8.5, SANSB, NAVY_SOFT, 'c')
    lx = M + 14 + 15 * cs + 22
    for k, nm in enumerate(NOTES7):
        yy = yt - 66 - k * 22
        rr(c, lx, yy - 8, 18, 18, 9, fill=white, lw=1.5, col=NAVY)
        txt(c, lx + 26, yy - 3.4, nm, 12, SERIFB, INK)
        txt(c, lx + 62, yy - 3.4, '= ' + COLNOM[nm], 11, SANS, NAVY_SOFT)
    h = 196
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'POSA-LES EN ORDRE', n=2)
    consigna(c, M + 14, yt - 40, 'Escriu 1 a 7 sota cada nota.', pw - 28)
    barreja = ['SOL', 'DO', 'MI', 'SI', 'RE', 'LA', 'FA']
    for k, nm in enumerate(barreja):
        col, fila = k % 4, k // 4
        xx = M + 14 + col * 58
        yy = yt - 62 - fila * 62
        rr(c, xx, yy - 26, 52, 28, 6, fill=WARM2, lw=1.4, col=NAVY)
        txt(c, xx + 26, yy - 17, nm, 12, SANSB, NAVY, 'c')
        rr(c, xx + 12, yy - 54, 28, 24, 6, fill=white, lw=1.5, col=NAVY)
    panell(c, x2, yt, pw, h, 'SOPA DE LLETRES', n=3)
    consigna(c, x2 + 14, yt - 40, 'Troba les 7 notes (→ i ↓).', pw - 28)
    dibuixa_sopa(c, x2 + 14, yt - 52, sopa(NOTES7, 8, seed=31), 17.5, 13)
    llista_paraules(c, x2 + 14 + 8 * 17.5 + 18, yt - 66, NOTES7, 11.5, 19)
    h = 104
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 36, pw - 14)
    capcalera_vf(c, x2 + 0, yt - 36, pw - 14)
    veritat_fals(c, M + 14, yt - 54, pw - 14, ['Hi ha set notes amb nom.'], 12, 14.5)
    veritat_fals(c, x2 + 0, yt - 54, pw - 14, ['Després del SI ve el RE.'], 12, 14.5)
    c.showPage()


# ======================================================================== TEMA 12 · L'octava
def t12_teoria(c):
    pagina_tema(c, 12, 'L’octava', 'Del DO fins al següent DO hi ha una octava: vuit notes.', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Compta amb mi: DO, RE, MI, FA, SOL, LA, SI… i un altre DO! Del primer DO fins a aquest DO '
         'hi ha una OCTAVA.', color=True, size=12.5, h=80)
    yt = Y(240)
    h = 188
    panell(c, M, yt, CW, h, 'VUIT NOTES, UNA OCTAVA')
    kx, ky, kh = M + 14, yt - h + 14, 90
    kw = (CW - 28) / 15.0
    teclat(c, kx, ky, CW - 28, kh, nb=15, resalta={i: NOTES7[i % 7] for i in range(15)}, noms='resalta', color=True)
    for i in range(8):
        bola(c, kx + i * kw + kw / 2, ky + kh + 20, i + 1, 10, size=11)
    trac(c, 2.2, OCRE)
    xa, xb = kx + 2, kx + 7 * kw + kw - 2
    c.line(xa, ky + kh + 38, xb, ky + kh + 38)
    c.line(xa, ky + kh + 38, xa, ky + kh + 33)
    c.line(xb, ky + kh + 38, xb, ky + kh + 33)
    txt(c, (xa + xb) / 2, ky + kh + 44, 'UNA OCTAVA', 11, ETQ, OCRE, 'c')
    yt = Y(442)
    h = 262
    panell(c, M, yt, CW, h, 'TRES DO, TRES SONS')
    g = 9
    gp = gran_pauta(c, M + 14, yt - 56, CW - 28, g, claus=True, brace=False)
    cy4 = (gp['tb'] + gp['bt']) / 2.0
    kx3 = M + 14 + 40
    kwb = (CW - 28 - 40) / 15.0
    tecla_x = [kx3 + (7 * i) * kwb + kwb / 2 for i in range(3)]
    nota_y = [nt.note_y(gp['bb'], g, 'C3', 'bass'), cy4, nt.note_y(gp['tb'], g, 'C5')]
    trac(c, 1.0, NAVY)
    c.line(tecla_x[1] - g * 1.3, cy4, tecla_x[1] + g * 1.3, cy4)
    ky2 = yt - h + 14
    for xx, yy in zip(tecla_x, nota_y):
        trac(c, 1.0, OCRE, (2, 3))
        c.line(xx, yy - g * 0.7, xx, ky2 + 68 + 4)
        c.setDash()
        cap(c, xx, yy, g, 'w', HexColor(COL['DO']))
    for k, (t, xx) in enumerate(zip(('DO greu', 'DO central', 'DO agut'), tecla_x)):
        txt(c, xx + (-8 if k == 2 else 8), ky2 + 68 + 14, t, 11.5, SANSB, NAVY, 'r' if k == 2 else 'l')
    teclat(c, kx3, ky2, kwb * 15, 68, nb=15, resalta={0: 'DO', 7: 'DO', 14: 'DO'}, noms='resalta', color=True)
    franja(c, M, Y(718), CW, 60, 'RECORDA', 'Octava vol dir «vuit»: del DO fins al següent DO. Té el mateix nom, però més greu o més agut!', 12)
    c.showPage()


def t12_jocs(c):
    pagina_jocs(c, 12, 'L’octava · a jugar!', 'Compta fins a vuit.',
                'Una octava té vuit notes. T’animes a comptar-les i a trobar tots els DO del piano?')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 142
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'COMPTA I NUMERA', n=1)
    consigna(c, M + 14, yt - 40, 'Escriu del 1 al 8 sobre cada tecla d’una octava, començant pel DO.', CW - 28)
    kx, ky, kh = M + 14, yt - h + 12, 50
    kw = (CW - 28) / 15.0
    teclat(c, kx, ky, CW - 28, kh, nb=15, resalta={0: 'DO'}, noms='resalta')
    for i in range(1, 8):
        rr(c, kx + i * kw + kw / 2 - 9, ky + kh + 12, 18, 18, 9, fill=white, lw=1.4, col=NAVY)
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'PINTA ELS DO', n=2)
    consigna(c, M + 14, yt - 40, 'Pinta els DO de vermell i encercla una octava.', pw - 28)
    teclat(c, M + 14, yt - h + 14, pw - 28, 66, nb=15, noms=None)
    panell(c, x2, yt, pw, h, 'QUANTES NOTES?', n=3)
    consigna(c, x2 + 14, yt - 40, 'Respon amb un número.', pw - 28)
    qs = ['Notes d’una octava', 'Notes amb nom diferent', 'Octaves entre dos DO seguits']
    for k, q in enumerate(['Quantes notes té una octava?', 'Quantes notes diferents (amb nom) hi ha?', 'I de DO a DO, quantes octaves?']):
        yy = yt - 78 - k * 40
        yy2 = par(c, x2 + 14, yy, q, 11.5, pw - 84, 14, SANS, INK)
        rr(c, x2 + pw - 56, yy - 14, 40, 26, 6, fill=white, lw=1.6, col=NAVY)
    h = 196
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'DIBUIXA ELS DO', n=4)
    consigna(c, M + 14, yt - 40, 'Posa el DO central i els altres dos DO.', pw - 28)
    g = 8
    gp = gran_pauta(c, M + 14, yt - 66, pw - 28, g, claus=True, brace=False)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 52, pw - 14, ['Una octava té vuit notes.', 'Dos DO seguits són tecles amb noms diferents.',
                                                'El DO agut és a la dreta del DO greu.'], 11.8, 14)
    c.showPage()


# ======================================================================== TEMA 13 · La melodia puja i baixa
def fila_melodia(c, x, yt, w, h, titol, pitches, nom_dir, simbol, g=10):
    panell(c, x, yt, w, h, titol)
    yb = pauta(c, x + 90, yt - 46, w - 104, g, 'treble', final=True)
    n = len(pitches)
    dx = (w - 104 - 60) / max(1, n - 1)
    for j, p_ in enumerate(pitches):
        nm = {'C': 'DO', 'D': 'RE', 'E': 'MI', 'F': 'FA', 'G': 'SOL', 'A': 'LA', 'B': 'SI'}[p_[0]]
        xx = x + 90 + 46 + j * dx
        cy_ = nt.note_y(yb, g, p_)
        if p_ == 'C4':
            trac(c, 1.0, NAVY)
            c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
        cap(c, xx, cy_, g, 'w', HexColor(COL[nm]))
    # fletxa gran
    if simbol == 'up':
        fletxa(c, x + 22, yt - h + 22, x + 66, yt - 38, 4.4, OCRE, 18)
    elif simbol == 'down':
        fletxa(c, x + 22, yt - 38, x + 66, yt - h + 22, 4.4, OCRE, 18)
    else:
        fletxa(c, x + 18, yt - h / 2 - 4, x + 72, yt - h / 2 - 4, 4.4, OCRE, 18)


def t13_teoria(c):
    pagina_tema(c, 13, 'La melodia puja i baixa', 'Una melodia és una cançó feta de notes: pot pujar, baixar o repetir-se.', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Una melodia es mou com jo quan vull volar: cap amunt, cap avall o… quieta! Fixa’t en cap on '
         'van les notes.', color=True, size=12.5, h=80)
    yt = Y(240)
    fila_melodia(c, M, yt, CW, 108, 'PUJA', ['C4', 'D4', 'E4', 'F4', 'G4'], 'PUJA', 'up')
    fila_melodia(c, M, yt - 126, CW, 108, 'BAIXA', ['G4', 'F4', 'E4', 'D4', 'C4'], 'BAIXA', 'down')
    fila_melodia(c, M, yt - 252, CW, 108, 'ES REPETEIX', ['E4', 'E4', 'E4', 'E4'], 'IGUAL', 'same')
    # una melodia de debò
    yt = Y(612)
    h = 184
    panell(c, M, yt, CW, h, 'UNA MELODIA DE DEBÒ')
    g = 9
    yb = pauta(c, M + 24, yt - 56, CW - 48, g, 'treble', final=True)
    mel = ['E4', 'D4', 'C4', 'D4', 'E4', 'E4', 'E4']
    sym = ['↓', '↓', '↑', '↑', '=', '=']
    dx = (CW - 48 - 90) / 6.0
    for j, p_ in enumerate(mel):
        nm = {'C': 'DO', 'D': 'RE', 'E': 'MI'}[p_[0]]
        xx = M + 24 + 56 + j * dx
        cy_ = nt.note_y(yb, g, p_)
        if p_ == 'C4':
            trac(c, 1.0, NAVY)
            c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
        cap(c, xx, cy_, g, 'w', HexColor(COL[nm]))
        txt(c, xx, yb - 24, nm, 10.5, SANSB, NAVY, 'c')
        if j < 6:
            txt(c, xx + dx / 2, yb - 44, sym[j], 16, SANSB, OCRE, 'c')
    txt(c, M + 14, yt - h + 14, 'Aquesta melodia és la del començament de «Mary had a little lamb».', 11.5, SANS, INK)
    franja(c, M, Y(796), CW, 0.1, '', '') if False else None
    c.showPage()


def t13_jocs(c):
    pagina_jocs(c, 13, 'La melodia · a jugar!', 'Cap amunt, cap avall o quietes?',
                'Mira les notes de dues en dues: pugen, baixen o són iguals? Marca-ho amb una fletxa.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PUJA, BAIXA O IGUAL?', n=1)
    consigna(c, M + 14, yt - 40, 'Mira cada parella de notes i marca què fa la melodia.', CW - 28)
    parelles = [('C4', 'E4'), ('G4', 'D4'), ('F4', 'F4'), ('A4', 'B4'), ('E4', 'C4'), ('G4', 'G4')]
    g = 7
    for k, (a, b) in enumerate(parelles):
        col, fila = k % 3, k // 3
        gx = M + 14 + col * 163
        gy = yt - 66 - fila * 76
        yb = pauta(c, gx, gy, 98, g, 'treble', final=False)
        for j, p_ in enumerate((a, b)):
            xx = gx + 50 + j * 28
            cy_ = nt.note_y(yb, g, p_)
            if p_ == 'C4':
                trac(c, 1.0, NAVY)
                c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
            cap(c, xx, cy_, g, 'w', white)
        for j, s_ in enumerate(('↑', '↓', '=')):
            rr(c, gx + 6 + j * 30, yb - 38, 26, 24, 12, fill=white, lw=1.5, col=NAVY)
            txt(c, gx + 19 + j * 30, yb - 31.5, s_, 14, SANSB, NAVY_SOFT, 'c')
    h = 160
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'DIBUIXA LA MELODIA', n=2)
    consigna(c, M + 14, yt - 40, 'Una que PUGI i una que BAIXI.', pw - 28)
    for k, t in enumerate(('puja', 'baixa')):
        yb = pauta(c, M + 14, yt - 78 - k * 44, pw - 28, 5.6, 'treble', final=False)
        txt(c, M + pw - 18, yb - 14, t, 10, SANS, MUTED, 'r')
    panell(c, x2, yt, pw, h, 'FES-HO AMB EL COS', n=3)
    consigna(c, x2 + 14, yt - 40, 'La profe toca notes. Tu puges la mà si la nota puja i la baixes si baixa.', pw - 28)
    for k, t in enumerate(('puja → mà amunt', 'baixa → mà avall', 'igual → mà quieta')):
        rr(c, x2 + 14, yt - 98 - k * 22, 18, 18, 4, fill=white, lw=1.5, col=NAVY)
        txt(c, x2 + 42, yt - 93 - k * 22, t, 11.5, SANSB, NAVY)
    h = 146
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 36, pw - 14)
    capcalera_vf(c, x2 + 0, yt - 36, pw - 14)
    veritat_fals(c, M + 14, yt - 54, pw - 14, ['Si les notes pugen al pentagrama, la melodia puja.', 'DO – MI és una melodia que baixa.'], 12, 14.5)
    veritat_fals(c, x2 + 0, yt - 54, pw - 14, ['MI – MI – MI s’està repetint.', 'Una melodia sempre ha de pujar.'], 12, 14.5)
    c.showPage()
