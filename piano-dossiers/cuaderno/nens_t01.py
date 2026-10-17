# -*- coding: utf-8 -*-
"""Capítol 1 · Abans de tocar — temes 1 a 4 (teoria + jocs)."""
from nens_tclas import *                                         # noqa: F401,F403
from nens_tclas import (W, H, M, CW, NAVY, NAVY_SOFT, CREMA, WARM, WARM2, RULE, SOMBRA, INK, MUTED, OCRE, COL,
                        COLNOM, SANS, SANSB, SERIFB, ETQ, Y, txt, par, alt_par, trac, rr, pagina_tema, panell,
                        caixa_t, franja, guia, consigna, etiqueta_sec, teclat, white, HexColor, stringWidth, mussol,
                        ma)
from nens_jocs import (Pila, joc, meitats, sopa, dibuixa_sopa, llista_paraules, crucigrama, pistes, uneix,
                       veritat_fals, capcalera_vf, casella_dibuix, linia, quadres, laberint)
from nens_dib import (piano, mecanisme, nen_assegut, os_, ocell, ona, ma_real, ma_costat, fletxa, bola, clau_llarga, punts_dits)


# ======================================================================== TEMA 1 · El piano
def t1_teoria(c):
    pagina_tema(c, 1, 'El piano i les seves parts', 'El piano és un instrument enorme i ple de secrets. Mirem què hi ha a fora i a dins.', 'teoria')
    guia(c, M, Y(142), CW, 'Aquest és el piano! Té moltes peces, però només cal que en recordis cinc. '
         'I quan toques una tecla, a dins passa una cosa màgica…', color=True, size=12.5, h=80)
    # parts
    yt = Y(240)
    h = 240
    panell(c, M, yt, CW, h, 'LES PARTS DEL PIANO')
    px, pyb, ps = M + 150, yt - h + 20, 0.9
    pt = piano(c, px, pyb, ps, color=False)
    pos = {1: (px + 100 * ps, pyb + 207 * ps), 2: (px + 30 * ps, pyb + 150 * ps), 3: (px - 78 * ps, pyb + 82 * ps),
           4: (px + 42 * ps, pyb + 14 * ps), 5: (px + 100 * ps, pyb + 140 * ps)}
    for n, (bx, by) in pos.items():
        bola(c, bx, by, n, 11)
    # llegenda
    lx = M + 300
    items = [('La tapa', 'Protegeix el piano i el tanca.'),
             ('L’atril', 'Hi posem les partitures.'),
             ('El teclat', 'Tecles blanques i negres.'),
             ('Els pedals', 'Es premen amb els peus.'),
             ('Les cordes', 'Amagades a dins: elles sonen.')]
    yy = yt - 48
    for k, (t, d) in enumerate(items):
        bola(c, lx + 12, yy - 4, k + 1, 12)
        txt(c, lx + 32, yy - 2, t, 13, SANSB, NAVY)
        txt(c, lx + 32, yy - 17, d, 10.8, SANS, INK)
        yy -= 38
    # com sona
    yt = Y(496)
    h = 198
    panell(c, M, yt, CW, h, 'COM SONA UN PIANO?')
    rr(c, M + 14, yt - h + 12, 214, h - 32, 8, fill=WARM, lw=1.2, col=SOMBRA)
    mx, my, msc = M + 24, yt - h + 34, 1.0
    pts = mecanisme(c, mx, my, msc, color=False)
    fletxa(c, mx + 12, my + 80, mx + 12, my + 42, 2.2, OCRE, 9)             # prem la tecla
    ona(c, mx + 104, my + 122, 80, 3.4, 4, 2.0, OCRE)                        # vibra
    bola(c, mx + 12, my + 94, 1, 11)
    bola(c, mx + 120, my + 104, 2, 11)
    bola(c, mx + 176, my + 140, 3, 11)
    txt(c, mx + 60, my - 6, 'tecla', 10.5, SANSB, NAVY_SOFT, 'c')
    txt(c, mx + 160, my + 58, 'martellet', 10.5, SANSB, NAVY_SOFT, 'c')
    txt(c, mx + 100, my + 134, 'corda', 10.5, SANSB, NAVY_SOFT, 'c')
    lx = M + 246
    passos = [('Premo una tecla.', 'La tecla es mou com un balancí.'),
              ('El martellet pica la corda.', 'Té el cap de feltre, suau.'),
              ('La corda vibra… i sona!', 'Com una guitarra, però més gran.')]
    yy = yt - 54
    for k, (t, d) in enumerate(passos):
        bola(c, lx + 12, yy - 4, k + 1, 12)
        txt(c, lx + 32, yy - 2, t, 12.5, SANSB, NAVY)
        txt(c, lx + 32, yy - 17, d, 10.8, SANS, INK)
        yy -= 40
    # sabies que
    yt = Y(704)
    caixa_t(c, M, yt, CW, 80, 'SABIES QUE?',
            'Un piano té 88 tecles (52 de blanques i 36 de negres) i més de 200 cordes! Al principi es deia «pianoforte», '
            'que vol dir «suau i fort».', 12)
    c.showPage()


def guia_jocs(c, text, n=None):
    guia(c, M, Y(122), CW, text, color=False, size=12.5, h=66)


def pagina_jocs(c, n, titol, intro, guia_txt):
    pagina_tema(c, n, titol, intro, 'jocs')
    guia_jocs(c, guia_txt)


def t1_jocs(c):
    pagina_jocs(c, 1, 'El piano · a jugar!', 'Agafa els llapis i fes-ho sense pressa.',
                'Ara que coneixes el piano per fora i per dins, fem uns quants jocs. Si t’encalles, mira la pàgina anterior!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · escriu el nom de cada part
    h = 162
    yt = pila.pren(h)
    y0 = joc(c, M, yt, CW, h, 1, 'ESCRIU EL NOM DE CADA PART', 'Mira els números del piano i escriu el nom de cada part.')
    px, pyb, ps = M + 86, yt - h + 12, 0.46
    piano(c, px, pyb, ps, color=False)
    pos = {1: (px + 100 * ps, pyb + 207 * ps), 2: (px + 30 * ps, pyb + 150 * ps), 3: (px - 78 * ps, pyb + 82 * ps),
           4: (px + 42 * ps, pyb + 14 * ps), 5: (px + 100 * ps, pyb + 140 * ps)}
    for n, (bx, by) in pos.items():
        bola(c, bx, by, n, 9, size=10)
    bx0 = M + 190
    txt(c, bx0 + 190, yt - 62, 'PARAULES PER TRIAR', 9.2, ETQ, OCRE)
    for k in range(5):
        yy = yt - 74 - k * 19
        bola(c, bx0 + 12, yy + 4, k + 1, 8.6, size=9.6)
        linia(c, bx0 + 30, yy, 130)
    for k, p_ in enumerate(['PEDALS', 'ATRIL', 'TECLAT', 'CORDES', 'TAPA']):
        rr(c, bx0 + 190, yt - 86 - k * 19, 100, 16, 8, fill=WARM, lw=1.1, col=OCRE)
        txt(c, bx0 + 240, yt - 81.5 - k * 19, p_, 10.2, SANSB, NAVY, 'c')
    # 2 · sopa de lletres  /  3 · ordena els passos
    h = 214
    yt = pila.pren(h)
    joc(c, M, yt, pw, h, 2, 'SOPA DE LLETRES', 'Troba 6 paraules (→ i ↓).')
    pal = ['PIANO', 'TECLA', 'PEDAL', 'CORDA', 'TAPA', 'ATRIL']
    g = sopa(pal, 8, seed=7)
    dibuixa_sopa(c, M + 14, yt - 54, g, 19, 13.5)
    llista_paraules(c, M + 14 + 8 * 19 + 18, yt - 70, pal, 12, 24)
    panell(c, x2, yt, pw, h, 'ORDENA ELS PASSOS', n=3)
    consigna(c, x2 + 14, yt - 40, 'Escriu 1, 2 i 3 per ordenar el que passa.', pw - 28)
    passos = ['La corda vibra i sona.', 'Premo una tecla.', 'El martellet pica la corda.']
    for k, t in enumerate(passos):
        yy = yt - 76 - k * 42
        rr(c, x2 + 14, yy - 14, pw - 28, 34, 8, fill=WARM, lw=1.2, col=OCRE)
        rr(c, x2 + 22, yy - 8, 24, 24, 12, fill=white, lw=1.5, col=NAVY)
        txt(c, x2 + 58, yy - 1.5, t, 11.5, SANSB, NAVY)
    # 4 · veritat o fals  /  5 · dibuixa
    h = 160
    yt = pila.pren(h)
    joc(c, M, yt, pw, h, 4, 'VERITAT O FALS?', None)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['El piano és un instrument de vent.', 'Els pedals es premen amb els peus.',
                                              'A dins del piano hi ha cordes.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'DIBUIXA EL TEU PIANO', n=5)
    casella_dibuix(c, x2 + 14, yt - h + 14, pw - 28, h - 56, 'el piano de casa teva o de l’escola')
    c.showPage()


# ======================================================================== TEMA 2 · Postura i dits
def t2_teoria(c):
    pagina_tema(c, 2, 'Com m’assec i els meus dits', 'Abans de tocar ens posem còmodes: així l’esquena i les mans no es cansen.', 'teoria')
    guia(c, M, Y(142), CW, 'Un pianista és com un esportista: ha de seure bé! Mira el nen del dibuix i fixa’t en cinc coses. '
         'Després, coneixerem els deu dits.', color=True, size=12.5, h=80)
    yt = Y(240)
    h = 262
    panell(c, M, yt, CW, h, 'ASSEGUT AL PIANO')
    s_ = 1.2
    x0, y0 = M + 56, yt - h + 26
    pt = nen_assegut(c, x0, y0, s_, color=False)
    pos = {1: (pt['esquena'][0] - 14, pt['esquena'][1] + 16), 2: (pt['seient'][0] - 26, pt['seient'][1] - 10),
           3: (pt['peu'][0] + 24, pt['peu'][1] + 18), 4: (pt['colze'][0] + 10, pt['colze'][1] + 24), 5: (pt['ma'][0] + 6, pt['ma'][1] + 26)}
    for n, (bx, by) in pos.items():
        bola(c, bx, by, n, 11.5)
    lx = M + 292
    items = [('Esquena dreta', 'Com si un fil et estirés cap amunt.'),
             ('Seu a la vora', 'A la part de davant de la banqueta.'),
             ('Peus a terra', 'Si no hi arribes, posa-hi un tamboret.'),
             ('Colzes a l’altura del teclat', 'Ni massa amunt ni massa avall.'),
             ('Mans arrodonides', 'Com si sostinguessis una pilota.')]
    yy = yt - 46
    for k, (t, d) in enumerate(items):
        bola(c, lx + 12, yy - 4, k + 1, 12)
        txt(c, lx + 32, yy - 2, t, 12.2, SANSB, NAVY)
        yy = par(c, lx + 32, yy - 16, d, 10.8, CW - 292 - 44, 12.5, SANS, INK) - 11
    # dits
    yt = Y(520)
    h = 218
    wb = 300
    panell(c, M, yt, wb, h, 'ELS DITS TENEN NÚMERO')
    for (cx, esq, nom) in ((M + 76, True, 'MÀ ESQUERRA'), (M + 226, False, 'MÀ DRETA')):
        ma_real(c, cx, yt - h + 98, 0.68, esq=esq, dits=True, color=False)
        txt(c, cx, yt - h + 14, nom, 10.2, ETQ, NAVY_SOFT, 'c')
    wc = CW - wb - 18
    xc = M + wb + 18
    panell(c, xc, yt, wc, h, 'MANS ARRODONIDES')
    ma_costat(c, xc + 26, yt - 104, True, 1.0)
    txt(c, xc + wc / 2, yt - 128, 'ARRODONIDA  ✓', 12, SANSB, NAVY, 'c')
    ma_costat(c, xc + 26, yt - 176, False, 1.0)
    txt(c, xc + wc / 2, yt - 200, 'PLANA  ✗', 12, SANSB, MUTED, 'c')
    franja(c, M, Y(752), CW, 38, 'RECORDA', 'Els dos polzes són el dit 1. Comptem de l’1 al 5!')
    c.showPage()


def t2_jocs(c):
    pagina_jocs(c, 2, 'Postura i dits · a jugar!', 'Agafa els llapis i fes-ho sense pressa.',
                'Ara que saps com seure i com es diuen els dits, juguem! Ensenya les teves mans al Mussol.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · escriu el número / 2 · uneix
    h = 214
    yt = pila.pren(h)
    joc(c, M, yt, pw, h, 1, 'QUIN NÚMERO TÉ?', 'Escriu el número a cada dit.')
    for (cx, esq) in ((M + 66, True), (M + 178, False)):
        cy = yt - h + 76
        ma_real(c, cx, cy, 0.56, esq=esq, dits=False, color=False)
        for n, (px_, py_) in punts_dits(cx, cy, 0.56, esq).items():
            rr(c, px_ - 8.5, py_ - 8.5, 17, 17, 8.5, fill=white, lw=1.4, col=NAVY)
    panell(c, x2, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=2)
    consigna(c, x2 + 14, yt - 40, 'Cada dit amb el seu número.', pw - 28)
    uneix(c, x2 + 14, yt - 80, pw - 28, ['polze', 'índex', 'del mig', 'anular', 'petit'], ['4', '1', '5', '3', '2'], fila=26,
          ampl_esq=84, ampl_dre=44, fs=12, serif=False)
    # 3 · gimnàstica / 4 · la teva mà
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'GIMNÀSTICA DE DITS', n=3)
    consigna(c, M + 14, yt - 40, 'Posa la mà sobre la taula i fes caminar els dits. Marca’ls quan els tinguis!', pw - 28)
    ex = ['1 - 2 - 3 - 4 - 5', '5 - 4 - 3 - 2 - 1', '1 - 3 - 5', '2 - 4 - 2 - 4']
    for k, t in enumerate(ex):
        yy = yt - 96 - k * 24
        rr(c, M + 18, yy - 6, 20, 20, 4, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 50, yy - 1, t, 14, SANSB, NAVY)
    panell(c, x2, yt, pw, h, 'LA TEVA MÀ', n=4)
    consigna(c, x2 + 14, yt - 40, 'Posa-hi la mà, dibuixa’n el contorn i escriu els números.', pw - 28)
    casella_dibuix(c, x2 + 14, yt - h + 14, pw - 28, h - 86, 'aquí va la teva mà')
    # 5 · veritat o fals
    h = 134
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, M + 14, yt - 36, pw - 14)
    capcalera_vf(c, x2 + 0, yt - 36, pw - 14)
    veritat_fals(c, M + 14, yt - 54, pw - 14, ['Seiem a tota la banqueta.', 'Les mans són arrodonides, com sostenint una pilota.'], 12, 14.5)
    veritat_fals(c, x2 + 0, yt - 54, pw - 14, ['Els polzes són el dit 1.', 'Els peus pengen sense tocar res.'], 12, 14.5)
    c.showPage()


# ======================================================================== TEMA 3 · Greu i agut
def t3_teoria(c):
    pagina_tema(c, 3, 'Greu i agut', 'Hi ha sons gruixuts com un ós i sons fins com un ocell.', 'teoria')
    guia(c, M, Y(142), CW, 'Recorre el teclat amb el dit! Cap a l’esquerra els sons són GREUS i cap a la dreta són AGUTS. '
         'Mira com vibren!', color=True, size=12.5, h=80)
    yt = Y(240)
    h = 290
    panell(c, M, yt, CW, h, 'DE L’ESQUERRA A LA DRETA')
    os_(c, M + 62, yt - 86, 1.0, color=False)
    ocell(c, M + CW - 54, yt - 84, 0.95, color=False)
    txt(c, M + 120, yt - 66, 'GREU', 26, SERIFB, NAVY)
    txt(c, M + 120, yt - 86, 'un so gruixut', 11.5, SANS, INK)
    txt(c, M + 120, yt - 101, 'vibra a poc a poc', 11.5, SANS, MUTED)
    txt(c, M + CW - 112, yt - 66, 'AGUT', 26, SERIFB, NAVY, 'r')
    txt(c, M + CW - 112, yt - 86, 'un so fi', 11.5, SANS, INK, 'r')
    txt(c, M + CW - 112, yt - 101, 'vibra molt de pressa', 11.5, SANS, MUTED, 'r')
    ona(c, M + 20, yt - 146, 190, 14, 2.5, 2.6, NAVY)
    ona(c, M + CW - 210, yt - 146, 190, 6, 11, 2.2, NAVY)
    teclat(c, M + 14, yt - 252, CW - 28, 76, nb=21, noms=None)
    fletxa(c, M + CW / 2 - 40, yt - h + 14, M + 26, yt - h + 14, 2.2, OCRE, 10)
    fletxa(c, M + CW / 2 + 40, yt - h + 14, M + CW - 26, yt - h + 14, 2.2, OCRE, 10)
    txt(c, M + CW / 2, yt - h + 10.5, 'GREU  ·  AGUT', 11.5, ETQ, OCRE, 'c')
    # com els reconec
    yt = Y(548)
    h = 112
    panell(c, M, yt, CW, h, 'COM ELS RECONEC?')
    pw_ = (CW - 42) / 2.0
    for k, (tit, ll) in enumerate((('GREUS', ['ós', 'tro', 'tuba', 'elefant']), ('AGUTS', ['ocell', 'flauta', 'mosquit', 'xiulet']))):
        x = M + 14 + k * (pw_ + 14)
        rr(c, x, yt - h + 12, pw_, h - 42, 8, fill=WARM, lw=1.2, col=OCRE)
        txt(c, x + 10, yt - 52, tit, 10.5, ETQ, OCRE)
        xx = x + 10
        for t in ll:
            w_ = stringWidth(t, SANSB, 11) + 14
            rr(c, xx, yt - 88, w_, 24, 12, fill=white, lw=1.4, col=NAVY)
            txt(c, xx + w_ / 2, yt - 80.5, t, 11, SANSB, NAVY, 'c')
            xx += w_ + 5
    franja(c, M, Y(678), CW, 44, 'RECORDA', 'Esquerra = GREU.   Dreta = AGUT.', 13)
    franja(c, M, Y(738), CW, 52, 'ESCOLTO', 'Toca la tecla de més a l’esquerra i la de més a la dreta: quina sembla l’ós i quina l’ocell?', 12)
    c.showPage()


def t3_jocs(c):
    pagina_jocs(c, 3, 'Greu i agut · a jugar!', 'Escolta bé i fixa’t en els animals.',
                'Si el so és gruixut, pensa en l’ós. Si és fi, pensa en l’ocell. Comencem!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · classifica
    h = 200
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'ÓS O OCELL?', n=1)
    consigna(c, M + 14, yt - 40, 'Marca si cada cosa fa un so greu (ós) o agut (ocell).', CW - 28)
    paraules = [['tro', 'mosquit', 'elefant', 'canari'], ['tuba', 'flauta', 'trombó', 'pardal']]
    for t in range(2):
        x = M + 14 + t * (pw + 4)
        os_(c, x + pw - 96, yt - 82, 0.34, color=False)
        ocell(c, x + pw - 40, yt - 80, 0.46, color=False)
        for k, w_ in enumerate(paraules[t]):
            yy = yt - 108 - k * 26
            txt(c, x + 6, yy, w_, 13, SANSB, NAVY)
            for j in range(2):
                rr(c, x + pw - 96 + j * 56 - 11, yy - 8, 22, 22, 11, fill=white, lw=1.5, col=NAVY)
    # 2 · escolta i marca / 3 · crucigrama
    h = 206
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'ESCOLTA I MARCA', n=2)
    consigna(c, M + 14, yt - 40, 'La profe toca una tecla. Marca el que sents.', pw - 28)
    txt(c, M + pw - 100, yt - 66, 'greu', 10, ETQ, MUTED, 'c')
    txt(c, M + pw - 48, yt - 66, 'agut', 10, ETQ, MUTED, 'c')
    for k in range(4):
        yy = yt - 96 - k * 32
        bola(c, M + 26, yy + 5, k + 1, 11)
        linia(c, M + 46, yy, 66)
        for j, xx in enumerate((M + pw - 100, M + pw - 48)):
            rr(c, xx - 12, yy - 8, 24, 24, 12, fill=white, lw=1.5, col=NAVY)
    panell(c, x2, yt, pw, h, 'CRUCIGRAMA', n=3)
    consigna(c, x2 + 14, yt - 40, 'Escriu una lletra a cada quadret.', pw - 28)
    spec = [('OCELL', 0, 2, 'v', 1), ('AGUT', 1, 0, 'v', 2), ('GREU', 2, 0, 'h', 3)]
    crucigrama(c, x2 + 20, yt - 54, spec, 22)
    pistes(c, x2 + 118, yt - 76, pw - 130, [('1 ↓', 'Vola i fa piulets.'), ('2 ↓', 'Un so fi, com el de l’ocell.'),
                                             ('3 →', 'Un so gruixut, com el de l’ós.')], 11.2, 13.5)
    # 4 · dibuixa
    h = 138
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'DIBUIXA', n=4)
    consigna(c, M + 14, yt - 40, 'Dibuixa un animal que faci un so greu i un animal que faci un so agut.', CW - 28)
    casella_dibuix(c, M + 14, yt - h + 12, pw - 14, h - 66, 'un animal GREU')
    casella_dibuix(c, x2, yt - h + 12, pw - 14, h - 66, 'un animal AGUT')
    c.showPage()


# ======================================================================== TEMA 4 · El teclat
def _clau_grup(c, x1, x2, ytop, n):
    """Clau (bracket) per sobre d'un grup de negres amb un número en un cercle."""
    trac(c, 2.2, OCRE)
    c.line(x1, ytop - 6, x1, ytop)
    c.line(x1, ytop, x2, ytop)
    c.line(x2, ytop, x2, ytop - 6)
    c.setFillColor(OCRE)
    c.circle((x1 + x2) / 2, ytop + 12, 11, stroke=0, fill=1)
    txt(c, (x1 + x2) / 2, ytop + 7.8, str(n), 14, SANSB, white, 'c')


def t4_teoria(c):
    pagina_tema(c, 4, 'El teclat: blanques i negres', 'Les tecles negres fan dibuixos: ens ajuden a no perdre’ns.', 'teoria')
    guia(c, M, Y(142), CW, 'Mira les tecles negres: es posen en grups de DUES i de TRES! Si les aprens, trobaràs qualsevol '
         'nota sense perdre’t.', color=True, size=12.5, h=80)
    # A · grups
    yt = Y(240)
    h = 184
    panell(c, M, yt, CW, h, 'GRUPS DE DUES I DE TRES')
    kx, kw, ky, kh = M + 14, (CW - 28) / 14.0, yt - h + 14, 96
    teclat(c, kx, ky, CW - 28, kh, nb=14)
    for (a, b, n) in ((1, 2, 2), (4, 6, 3), (8, 9, 2), (11, 13, 3)):
        _clau_grup(c, kx + a * kw - kw * 0.25, kx + b * kw + kw * 0.25, ky + kh + 14, n)
    # B · el DO
    yt = Y(442)
    h = 190
    panell(c, M, yt, CW, h, 'EL DO VIU A L’ESQUERRA DEL GRUP DE DUES')
    kx, ky, kh = M + 14, yt - h + 14, 96
    kw = (CW - 28) / 15.0
    teclat(c, kx, ky, CW - 28, kh, nb=15, resalta={0: 'DO', 7: 'DO', 14: 'DO'}, noms='resalta', color=True)
    for i in (0, 7):
        fletxa(c, kx + i * kw + kw / 2 + 20, ky + kh + 24, kx + i * kw + kw / 2 + 36, ky + kh + 6, 2.0, OCRE, 8)
    txt(c, M + 14, yt - 50, 'El DO és la tecla blanca que hi ha just abans de les dues negres juntes.', 12, SANS, INK)
    # C · el DO central
    yt = Y(650)
    h = 132
    panell(c, M, yt, CW, h, 'ON ÉS EL DO CENTRAL?')
    kx, ky = M + 14, yt - h + 32
    teclat(c, kx, ky, CW - 28, 50, nb=52, inici=5, resalta={23: 'DO'}, color=True)
    kw = (CW - 28) / 52.0
    cx_ = kx + 23 * kw + kw / 2
    fletxa(c, cx_, ky + 78, cx_, ky + 54, 2.4, OCRE, 10)
    txt(c, cx_, ky + 84, 'DO CENTRAL', 11.5, ETQ, OCRE, 'c')
    txt(c, M + 14, yt - h + 14, 'Aquest és tot el piano: 88 tecles. El DO central queda més o menys al mig.', 11.5, SANS, INK)
    franja(c, M, Y(786), CW, 0.1, '', '') if False else None
    c.showPage()


def t4_jocs(c):
    pagina_jocs(c, 4, 'El teclat · a jugar!', 'Mira bé les tecles i pensa en el 2 i el 3.',
                'Tecles blanques, tecles negres, grups de dues i de tres… Tu pots amb tot això! Endavant.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    # 1 · compta
    h = 132
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'COMPTA LES TECLES', n=1)
    kx, ky = M + 14, yt - h + 14
    teclat(c, kx, ky, 300, 62, nb=14)
    qs = [('Blanques?', 14), ('Negres?', 10)]
    for k, (q, _) in enumerate(qs):
        yy = yt - 50 - k * 36
        txt(c, M + 340, yy, q, 13, SANSB, NAVY)
        rr(c, M + 430, yy - 10, 40, 28, 6, fill=white, lw=1.6, col=NAVY)
    consigna(c, M + 14, yt - 40, 'Quantes en veus?', 200)
    # 2 · completa
    h = 110
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'DIBUIXA LES NEGRES QUE FALTEN', n=2)
    consigna(c, M + 14, yt - 40, 'Recorda: grups de 2 i de 3.', 260)
    teclat(c, M + 14, yt - h + 12, CW - 28, 46, nb=14, negres=False)
    # 3 · troba els DO
    h = 110
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'TROBA ELS DO', n=3)
    consigna(c, M + 14, yt - 40, 'Pinta de vermell tots els DO. Encercla el DO central (el del mig).', CW - 28)
    teclat(c, M + 14, yt - h + 12, CW - 28, 42, nb=22)
    # 4 · laberint  /  5 · V/F
    h = 160
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'EL LABERINT', n=4)
    consigna(c, M + 14, yt - 40, 'Ajuda en Mussol a arribar a la tecla DO.', pw - 28)
    laberint(c, M + 20, yt - 58, 10, 4, 20, seed=11, lw=2.0)
    mussol(c, M + 8, yt - 60, 0.1, color=False, lw=1.2)
    teclat(c, M + 20 + 10 * 20 - 24, yt - 58 - 4 * 20 - 34, 28, 30, nb=1, resalta={0: 'DO'}, noms='resalta', tira=False)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 52, pw - 14, ['Les negres es posen en grups de 2 i de 3.', 'El DO és abans del grup de tres negres.',
                                                'El piano té 88 tecles.'], 11.8, 14.2)
    c.showPage()
