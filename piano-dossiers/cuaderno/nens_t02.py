# -*- coding: utf-8 -*-
"""Capítol 2 · El pentagrama — temes 5 a 7 (teoria + jocs)."""
from nens_t01 import *                                            # noqa: F401,F403
from nens_jocs2 import p_cruci, p_cami, p_intrus, p_mosaic, p_laberint, HEART, HOUSE
from nens_t01 import pagina_jocs
from nens_tclas import gran_pauta, cap, pauta, nt
import nens_tclas as _nt
from reportlab.pdfbase import pdfmetrics


def ypos(yb, gap, k):
    """y d'una posició del pentagrama: k=1 línia 1, 1.5 espai 1, 2 línia 2... (comptant de baix cap a dalt)."""
    return yb + (k - 1) * gap


def _bolet(c, x, y, t, fill=NAVY, ample=26):
    rr(c, x - ample / 2, y - 10, ample, 20, 10, fill=fill, lw=0)
    txt(c, x, y - 4, t, 10.5, SANSB, white, 'c')


# ======================================================================== TEMA 5 · Línies i espais
def pent_gran(c, x, ytop, w, gap, lw_lin=2.0, espais=True):
    """Pentagrama de debò, gran, amb els espais tintats."""
    yb = ytop - 4 * gap
    if espais:
        c.setFillColor(WARM2)
        for k in range(4):
            c.rect(x, yb + k * gap, w, gap, stroke=0, fill=1)
    trac(c, lw_lin, NAVY)
    for i in range(5):
        c.line(x, ytop - i * gap, x + w, ytop - i * gap)
    return yb


def t5_teoria(c):
    pagina_tema(c, 5, 'Línies i espais', 'El pentagrama és la casa de les notes. Té cinc línies i quatre espais.', 'teoria')
    guia(c, M, Y(142), CW, 'Mira aquesta casa de notes: té 5 línies i 4 espais entre elles. Per comptar-les, anem sempre '
         'de baix cap a dalt, com pujant escales!', color=False, size=12.5, h=80)
    yt = Y(240)
    h = 218
    panell(c, M, yt, CW, h, 'EL PENTAGRAMA')
    gap = 20
    sx, sw = M + 84, CW - 84 - 84
    yb = pent_gran(c, sx, yt - 68, sw, gap)
    for k in range(5):
        _bolet(c, M + 40, yb + k * gap, '%da' % (k + 1), OCRE, 30)
    for k in range(4):
        _bolet(c, M + CW - 44, yb + (k + 0.5) * gap, ['1r', '2n', '3r', '4t'][k], NAVY, 30)
    txt(c, M + 40, yt - 46, 'LÍNIES', 10.5, ETQ, OCRE, 'c')
    txt(c, M + CW - 44, yt - 46, 'ESPAIS', 10.5, ETQ, NAVY, 'c')
    nx0, dx = sx + 30, (sw - 60) / 8.0
    for k in range(9):
        pos = 1 + k * 0.5
        cap(c, nx0 + k * dx, yb + (pos - 1) * gap, gap * 0.78, 'w', white)
        txt(c, nx0 + k * dx, yb - 22, ('L%d' if k % 2 == 0 else 'E%d') % (1 + k // 2 if k % 2 == 0 else 1 + k // 2), 12, SANSB,
            OCRE if k % 2 == 0 else NAVY, 'c')
    txt(c, M + CW / 2, yt - h + 16, '5 línies  ·  4 espais', 14, SERIFB, NAVY, 'c')
    # B · nota a una línia / a un espai
    yt = Y(476)
    h = 140
    pw, x2 = meitats()
    for k, (tit, desc, kpos) in enumerate((('UNA NOTA A UNA LÍNIA', 'La línia passa pel mig de la nota.', 3),
                                           ('UNA NOTA A UN ESPAI', 'La nota queda entre dues línies.', 2.5))):
        x = M + k * (pw + 18)
        panell(c, x, yt, pw, h, tit)
        g = 14
        yb = pauta(c, x + 22, yt - 42, pw - 44, g, None, final=False)
        _cy = yb + (kpos - 1) * g
        cap(c, x + pw / 2, _cy, g, 'w', white)
        txt(c, x + pw / 2, yt - h + 14, desc, 11.5, SANS, INK, 'c')
    franja(c, M, Y(634), CW, 44, 'RECORDA', 'Comptem de baix cap a dalt: la 1a línia és la de baix de tot.', 12.5)
    franja(c, M, Y(694), CW, 60, 'SABIES QUE?', '«Penta» vol dir cinc i «grama» vol dir línia: pentagrama vol dir «cinc línies».', 12)
    c.showPage()


def t5_jocs(c):
    pagina_jocs(c, 5, 'Línies i espais · a jugar!', 'Compta de baix cap a dalt, sempre!',
                'La casa de les notes té 5 línies i 4 espais. Ara toca pintar, buscar i dibuixar.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · pinta
    h = 130
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA EL PENTAGRAMA', n=1)
    consigna(c, M + 14, yt - 40, 'Repassa les 5 línies de color i pinta els 4 espais d’un altre color.', CW - 28)
    pent_gran(c, M + 30, yt - 58, CW - 60, 14, 1.8, espais=False)
    # 2 · línia o espai? / 3 · sopa
    h = 238
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'LÍNIA O ESPAI?', n=2)
    consigna(c, M + 14, yt - 40, 'On viu cada nota? Marca L o E.', pw - 28)
    posicions = [(3, 'L'), (2.5, 'E'), (5, 'L'), (1.5, 'E'), (1, 'L'), (4.5, 'E')]
    for k, (kp, r) in enumerate(posicions):
        col, fila = k % 2, k // 2
        gx = M + 14 + col * 116
        gy = yt - 76 - fila * 52
        g = 7
        yb = pauta(c, gx, gy, 68, g, None, final=False)
        cap(c, gx + 34, yb + (kp - 1) * g, g, 'w', white)
        for j, l in enumerate(('L', 'E')):
            rr(c, gx + 78 + j * 22, gy - 2 * g - 9, 19, 19, 9.5, fill=white, lw=1.4, col=NAVY)
            txt(c, gx + 78 + j * 22 + 9.5, gy - 2 * g - 3.6, l, 10.5, SANSB, NAVY_SOFT, 'c')
    p_cruci(c, x2, yt, pw, h, 3, [('ESPAI', 0, 1, 'v', 1), ('NOTA', 1, 4, 'v', 2), ('LINIA', 4, 0, 'h', 3)], [('1 ↓', 'Entre dues línies hi ha un…'), ('2 ↓', 'Viu a una línia o a un espai.'), ('3 →', 'El pentagrama en té cinc.')], 20)
    # 4 · dibuixa / 5 · V/F
    h = 168
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'DIBUIXA LA NOTA', n=4)
    consigna(c, M + 14, yt - 40, 'Posa una rodona a cada lloc.', pw - 28)
    encarrecs = [(3, 'a la 3a línia'), (2.5, 'al 2n espai'), (1, 'a la 1a línia'), (4.5, 'al 4t espai')]
    for k, (kp, t) in enumerate(encarrecs):
        col, fila = k % 2, k // 2
        gx = M + 14 + col * 116
        gy = yt - 66 - fila * 50
        yb = pauta(c, gx, gy, 100, 5.5, None, final=False)
        txt(c, gx + 50, yb - 14, t, 10.5, SANSB, NAVY_SOFT, 'c')
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['El pentagrama té 5 línies.', 'Té 6 espais.', 'Comptem de dalt cap a baix.'], 12, 14.5)
    c.showPage()


# ======================================================================== TEMA 6 · Les claus
def clau_traç(c, x, yb, gap, clau):
    """Clau en contorn de punts, per repassar (nens: traça-la!)."""
    c.saveState()
    to = c.beginText()
    to.setTextRenderMode(1)
    c.setStrokeColor(MUTED)
    c.setLineWidth(0.9)
    c.setDash(1.5, 2.2)
    if clau == 'treble':
        to.setFont('FreeSerif', gap * 5.038)
        to.setTextOrigin(x, yb + gap * 0.318)
        to.textOut('\U0001D11E')
    else:
        to.setFont('FreeSerif', gap * 5.426)
        to.setTextOrigin(x, yb - gap * 0.062)
        to.textOut('\U0001D122')
    c.drawText(to)
    c.restoreState()


def t6_teoria(c):
    pagina_tema(c, 6, 'Clau de sol i clau de fa', 'Al començament del pentagrama hi ha un dibuix: la clau. Et diu on som al piano.', 'teoria', color=False)
    guia(c, M, Y(142), CW, 'Les claus són com un cartell: la clau de SOL és per a la mà dreta i la clau de FA és per a la mà esquerra.',
         color=True, size=12.5, h=80)
    yt = Y(240)
    h = 214
    pw, x2 = meitats()
    for k, (tit, clau, nota_, quina, colr, linia_, mans) in enumerate((
            ('CLAU DE SOL', 'treble', 'SOL', 'La 2a línia', COL['SOL'], 2, 'mà dreta · sons més aguts'),
            ('CLAU DE FA', 'bass', 'FA', 'La 4a línia', COL['FA'], 4, 'mà esquerra · sons més greus'))):
        x = M + k * (pw + 18)
        panell(c, x, yt, pw, h, tit)
        g = 16
        top = yt - 64
        yb = pauta(c, x + 18, top, pw - 36, g, clau, final=False, lw=1.4)
        yl = yb + (linia_ - 1) * g
        trac(c, 3.4, HexColor(colr))
        c.line(x + 64, yl, x + pw - 18, yl)
        txt(c, x + pw - 24, yl + 7, nota_, 13, SERIFB, HexColor(colr), 'r')
        txt(c, x + pw / 2, yt - h + 56, '%s és la línia del %s' % (quina, nota_), 12, SANSB, NAVY, 'c')
        txt(c, x + pw / 2, yt - h + 36, mans, 11.5, SANS, INK, 'c')
        _ = ma_real if False else None
    # teclat amb les dues zones
    yt = Y(472)
    h = 150
    panell(c, M, yt, CW, h, 'ON ÉS CADA CLAU AL PIANO?')
    kx, ky, kh = M + 14, yt - h + 14, 70
    teclat(c, kx, ky, CW - 28, kh, nb=21)
    kw = (CW - 28) / 21.0
    # claus: esquerra (fa) i dreta (sol)
    for (a, b, t, col) in ((0, 10.5, 'CLAU DE FA · MÀ ESQUERRA', COL['FA']), (10.5, 21, 'CLAU DE SOL · MÀ DRETA', COL['SOL'])):
        xa, xb = kx + a * kw + 2, kx + b * kw - 2
        trac(c, 3, HexColor(col))
        c.line(xa, ky + kh + 18, xb, ky + kh + 18)
        c.line(xa, ky + kh + 18, xa, ky + kh + 10)
        c.line(xb, ky + kh + 18, xb, ky + kh + 10)
        txt(c, (xa + xb) / 2, ky + kh + 26, t, 10.5, ETQ, NAVY, 'c')
    franja(c, M, Y(644), CW, 44, 'RECORDA', 'SOL = mà dreta = sons aguts.   FA = mà esquerra = sons greus.', 12.5)
    franja(c, M, Y(704), CW, 76, 'SABIES QUE?',
           'Les claus són lletres antigues disfressades! La clau de sol és una «G» (en anglès, G és el SOL) i la clau de fa '
           'és una «F» (en anglès, F és el FA).', 12)
    c.showPage()


def t6_jocs(c):
    pagina_jocs(c, 6, 'Les claus · a jugar!', 'Mira bé el dibuix del començament.',
                'Una clau, una mà! Si les repasses amb el llapis, te les aprendràs de seguida.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · quina clau és
    h = 150
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'QUINA CLAU ÉS?', n=1)
    consigna(c, M + 14, yt - 40, 'Encercla SOL o FA a sota de cada clau.', CW - 28)
    seq = ['treble', 'bass', 'bass', 'treble', 'treble', 'bass']
    cw_ = (CW - 28) / 3.0
    for k, cl in enumerate(seq):
        col, fila = k % 3, k // 3
        gx = M + 14 + col * cw_ + 6
        gy = yt - 66 - fila * 46
        pauta(c, gx, gy, cw_ - 120, 6, cl, final=False)
        for j, l in enumerate(('SOL', 'FA')):
            xx = gx + cw_ - 110 + j * 44
            rr(c, xx, gy - 17, 40, 20, 10, fill=white, lw=1.4, col=NAVY)
            txt(c, xx + 20, gy - 10.5, l, 10.5, SANSB, NAVY_SOFT, 'c')
    # 2 · uneix / 3 · traça
    h = 226
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=2)
    consigna(c, M + 14, yt - 40, 'Cada mà amb la seva clau.', pw - 28)

    def dib(c_, xr, yy, k):
        pauta(c_, xr, yy + 11, 84, 5.2, ['bass', 'treble'][k], final=False)
    uneix(c, M + 14, yt - 84, pw - 28, ['mà dreta', 'mà esquerra'], ['', ''], fila=66, ampl_esq=92, ampl_dre=90, fs=12,
          dibuix_dre=dib, serif=False)
    panell(c, x2, yt, pw, h, 'TRAÇA LES CLAUS', n=3)
    consigna(c, x2 + 14, yt - 40, 'Repassa els puntets amb el llapis.', pw - 28)
    for k, cl in enumerate(('treble', 'bass')):
        g = 11
        top = yt - 84 - k * 70
        yb = pauta(c, x2 + 14, top, pw - 28, g, None, final=False)
        clau_traç(c, x2 + 20, yb, g, cl)
    # 4 · pinta les puntes
    h = 160
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'PINTA LA CLAU', n=4)
    consigna(c, M + 14, yt - 40, 'Pinta de verd la línia del FA i de blau la del SOL.', pw - 28)
    for k, cl in enumerate(('treble', 'bass')):
        g = 8.5
        yb = pauta(c, M + 14 + k * 112, yt - 96, 100, g, cl, final=False)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['La clau de sol és per a la mà dreta.', 'La clau de fa és per a la mà dreta.',
                                                'La clau de fa és la dels sons greus.'], 12, 14.5)
    c.showPage()


# ======================================================================== TEMA 7 · El pentagrama gran i el DO central
def t7_teoria(c):
    pagina_tema(c, 7, 'El pentagrama gran', 'Unim els dos pentagrames i trobem la nota que els uneix.', 'teoria')
    guia(c, M, Y(142), CW, 'Quan toquem amb les dues mans, necessitem els dos pentagrames junts. I entre tots dos hi viu una '
         'nota molt especial: el DO central!', color=True, size=12.5, h=80)
    yt = Y(240)
    h = 250
    panell(c, M, yt, CW, h, 'EL PENTAGRAMA GRAN')
    g = 12
    gx, gw = M + 48, 300
    gp = gran_pauta(c, gx, yt - 58, gw, g)
    cy = (gp['tb'] + gp['bt']) / 2.0
    trac(c, 1.3, NAVY)
    c.line(gx + gw / 2 - 16, cy, gx + gw / 2 + 16, cy)
    cap(c, gx + gw / 2, cy, g, 'w', HexColor(COL['DO']))
    # indicacions
    txt(c, gx + gw + 14, gp['tt'] - 20, 'clau de sol', 12, SANSB, NAVY)
    txt(c, gx + gw + 14, gp['tt'] - 36, 'mà dreta', 11, SANS, MUTED)
    txt(c, gx + gw + 14, gp['bb'] + 28, 'clau de fa', 12, SANSB, NAVY)
    txt(c, gx + gw + 14, gp['bb'] + 12, 'mà esquerra', 11, SANS, MUTED)
    txt(c, gx + gw + 14, cy - 4, '← DO central', 12, SANSB, HexColor(COL['DO']))
    txt(c, M + 14, yt - h + 52, 'Una ratlleta addicional sosté el DO central entre els dos pentagrames.', 12, SANS, INK)
    txt(c, M + 14, yt - h + 34, 'La nota és la mateixa tecla del piano: només canvia la clau amb què la llegim.', 12, SANS, INK)
    # tecla
    yt = Y(508)
    h = 126
    panell(c, M, yt, CW, h, 'AL TECLAT')
    teclat(c, M + 14, yt - h + 14, CW - 28, 58, nb=15, resalta={7: 'DO'}, noms='resalta', color=True)
    franja(c, M, Y(650), CW, 44, 'RECORDA', 'El DO central és la nota del mig: la poden tocar les dues mans.', 12.5)
    franja(c, M, Y(710), CW, 56, 'SABIES QUE?', 'En anglès, el DO central es diu «Middle C», que vol dir «el DO del mig».', 12.5)
    c.showPage()


def t7_jocs(c):
    pagina_jocs(c, 7, 'El DO central · a jugar!', 'Busca el DO central!',
                'Dos pentagrames, dues mans i un DO al mig. T’animes a trobar-lo?')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · pinta el DO central
    h = 172
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA EL DO CENTRAL', n=1)
    consigna(c, M + 14, yt - 40, 'Una de les notes és el DO central. Troba-la i pinta-la de vermell.', CW - 28)
    g = 9
    gp = gran_pauta(c, M + 30, yt - 62, CW - 60, g, brace=True)
    cy = (gp['tb'] + gp['bt']) / 2.0
    xs = [M + 120, M + 200, M + 280, M + 360, M + 440]
    notes = [('treble', 'G4', gp['tb']), ('bass', 'E3', gp['bb']), ('mid', 'C4', None), ('treble', 'E5', gp['tb']), ('bass', 'A2', gp['bb'])]
    for (cl, p_, yb_), xx in zip(notes, xs):
        if cl == 'mid':
            trac(c, 1.2, NAVY)
            c.line(xx - 10, cy, xx + 10, cy)
            cap(c, xx, cy, g, 'w', white)
        else:
            cap(c, xx, nt.note_y(yb_, g, p_, cl), g, 'w', white)
    # 2 · uneix / 3 · V/F
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'MÀ DRETA O ESQUERRA?', n=2)
    consigna(c, M + 14, yt - 40, 'Escriu D o E: amb quina mà llegeixes?', pw - 28)
    for k, cl in enumerate(('treble', 'bass', 'bass', 'treble')):
        col, fila = k % 2, k // 2
        gx = M + 14 + col * 116
        gy = yt - 76 - fila * 56
        pauta(c, gx, gy, 96, 5.6, cl, final=False)
        quadres(c, gx + 40, gy - 24, 1, 18)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=3)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['El DO central és al mig dels dos pentagrames.', 'Només la mà dreta pot tocar-lo.',
                                                'Els dos pentagrames s’uneixen amb una clau.'], 12, 14.5)
    # 4 · completa
    h = 176
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'COMPLETA EL PENTAGRAMA GRAN', n=4)
    consigna(c, M + 14, yt - 40, 'Dibuixa la clau de sol, la de fa i el DO central amb la seva ratlleta.', CW - 28)
    g = 9.5
    gx, gw = M + 40, CW - 80
    gp = gran_pauta(c, gx, yt - 62, gw, g, claus=False, brace=False)
    for yy, cl in ((gp['tb'], 'treble'), (gp['bb'], 'bass')):
        clau_traç(c, gx + 4, yy, g, cl)
    c.showPage()
