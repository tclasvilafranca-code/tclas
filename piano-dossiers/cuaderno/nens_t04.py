# -*- coding: utf-8 -*-
"""Capítol 4 · El ritme — temes 14 a 19 (teoria + jocs)."""
from nens_t03 import *                                            # noqa: F401,F403
from nens_t01 import pagina_jocs
from nens_tclas import figura
from nens_dib import cor, rellotge, petjades, metronom
from nens_mus import mus, sist, beats

DUR_NOM = {'w': 'rodona', 'h': 'blanca', 'q': 'negra', 'e': 'corxera'}
DUR_TEMPS = {'w': 4, 'h': 2, 'q': 1, 'e': 0.5, 'h.': 3, 'q.': 1.5}


def icona_fig(c, tipus, cx, cy, gap=5.5):
    """Figura petita centrada a (cx, cy) (la cabeça a cy). tipus: w h q e ee h. q."""
    if tipus.endswith('.') and tipus[:-1] in ('h', 'q'):
        figura(c, tipus[:-1], cx - gap * 0.6, cy, gap)
        c.setFillColor(NAVY)
        c.circle(cx - gap * 0.6 + gap * 1.35, cy + gap * 0.25, gap * 0.2, stroke=0, fill=1)
    else:
        figura(c, tipus, cx - (gap * 1.8 if tipus == 'ee' else 0), cy, gap)


def tira_temps(c, x, y, w, h, figs, total=4, nums=False):
    """Una caixa de `total` temps dividida en els espais de cada figura. figs: [(tipus, temps)]. Dibuixa les figures."""
    unit = w / float(total)
    pos = 0.0
    for tipus, t in figs:
        bx = x + pos * unit
        rr(c, bx + 1, y, t * unit - 2, h, 5, fill=WARM, lw=1.5, col=NAVY)
        icona_fig(c, tipus, bx + t * unit / 2, y + h * 0.38, 5.2)
        pos += t
    if nums:
        for k in range(int(total)):
            txt(c, x + k * unit + unit / 2, y - 12, str(k + 1), 9.5, SANSB, MUTED, 'c')


# ======================================================================== TEMA 14 · El pols
def t14_teoria(c):
    pagina_tema(c, 14, 'El pols', 'La música té un cor que batega sempre igual: es diu pols.', 'teoria')
    guia(c, M, Y(142), CW, 'Tic-tac, tic-tac! Sents el meu cor? El pols és un batec que no s’atura mai i sempre va igual. '
         'Totes les músiques en tenen un.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 128
    panell(c, M, yt, CW, h, 'EL POLS ÉS A TOT ARREU')
    ic = [(cor, 'el teu cor'), (rellotge, 'el rellotge'), (petjades, 'quan camines')]
    for k, (f, t) in enumerate(ic):
        cx = M + 14 + (CW - 28) / 6.0 * (2 * k + 1)
        f(c, cx, yt - 66, 1.0, color=False)
        txt(c, cx, yt - h + 14, t, 12.5, SANSB, NAVY, 'c')
    yt = Y(382)
    h = 138
    panell(c, M, yt, CW, h, 'EL POLS DE LA MÚSICA')
    for k in range(8):
        cx = M + 44 + k * 58
        fort = (k % 4 == 0)
        c.setFillColor(NAVY if fort else white)
        trac(c, 1.8, NAVY)
        c.circle(cx, yt - 68, 17 if fort else 11, stroke=1, fill=1)
        txt(c, cx, yt - 108, str(k % 4 + 1), 12.5, SANSB, OCRE if fort else NAVY_SOFT, 'c')
    txt(c, M + 44, yt - 36, 'FORT', 10, ETQ, OCRE, 'c')
    txt(c, M + 44 + 4 * 58, yt - 36, 'FORT', 10, ETQ, OCRE, 'c')
    txt(c, M + 14, yt - h + 12, 'El primer pols de cada grup de quatre sona una mica més fort.', 11.5, SANS, INK)
    yt = Y(536)
    h = 150
    panell(c, M, yt, CW, h, 'EL METRÒNOM')
    metronom(c, M + 60, yt - h + 14, 0.98, color=False)
    par(c, M + 126, yt - 50, 'És una màquina que marca el pols. Si diu 60, fa 60 batecs cada minut: un cada segon!', 12, CW - 140, 16, SANS, INK)
    yb_ = yt - 112
    trac(c, 3, OCRE)
    c.line(M + 140, yb_, M + CW - 40, yb_)
    for (xx, t) in ((M + 140, 'lent'), (M + 140 + (CW - 180) / 2, 'normal'), (M + CW - 40, 'ràpid')):
        c.setFillColor(OCRE)
        c.circle(xx, yb_, 4.5, stroke=0, fill=1)
        txt(c, xx, yb_ - 18, t, 11, SANSB, NAVY, 'c')
    franja(c, M, Y(702), CW, 40, 'RECORDA', 'El pols no corre ni s’atura: sempre va igual.', 12.5)
    franja(c, M, Y(752), CW, 36, 'ESCOLTO', 'Posa una cançó que t’agradi i pica el pols amb el peu.', 12)
    c.showPage()


def t14_jocs(c):
    pagina_jocs(c, 14, 'El pols · a jugar!', 'Tic-tac, tic-tac!',
                'Cada joc té un batec amagat. Troba’l i segueix-lo amb el llapis!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 126
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA EL POLS FORT', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta el primer cercle de cada grup de quatre: és el pols fort.', CW - 28)
    for g_ in range(2):
        for k in range(4):
            cx = M + 30 + g_ * 244 + k * 56
            trac(c, 1.6, NAVY)
            c.setFillColor(white)
            c.circle(cx, yt - 84, 14, stroke=1, fill=1)
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=2)
    consigna(c, M + 14, yt - 40, 'Uneix cada cosa amb el seu dibuix.', pw - 28)

    def dib(c_, xr, yy, k):
        if k == 0:
            metronom(c_, xr + 40, yy - 20, 0.34, color=False)
        elif k == 1:
            cor(c_, xr + 40, yy, 0.55, color=False)
        else:
            rellotge(c_, xr + 40, yy, 0.6, color=False)
    uneix(c, M + 14, yt - 84, pw - 28, ['el cor', 'el rellotge', 'el metrònom'], ['', '', ''], fila=46, ampl_esq=92, ampl_dre=84, fs=12.5,
          dibuix_dre=dib, serif=False)
    panell(c, x2, yt, pw, h, 'SOPA DE LLETRES', n=3)
    consigna(c, x2 + 14, yt - 40, 'Troba 6 paraules (→ i ↓).', pw - 28)
    pal = ['POLS', 'COR', 'TIC', 'TAC', 'FORT', 'PICA']
    dibuixa_sopa(c, x2 + 14, yt - 54, sopa(pal, 8, seed=41), 19, 13.5)
    llista_paraules(c, x2 + 14 + 8 * 19 + 18, yt - 70, pal, 12, 24)
    h = 176
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'COMPLETA', n=4)
    consigna(c, M + 14, yt - 40, 'Escriu: pols, cor o metrònom.', pw - 28)
    fr = ['El ________ és el batec de la música.', 'El ________ és el que et batega al pit.', 'El ________ marca el pols amb un pèndol.']
    for k, f in enumerate(fr):
        yy = yt - 80 - k * 28
        par(c, M + 14, yy, f, 12, pw - 28, 14, SANS, INK)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['El pols va a vegades ràpid i a vegades lent.', 'El metrònom ens ajuda a seguir el pols.', 'El pols és un so molt fort.'], 11.8, 14)
    c.showPage()


# ======================================================================== TEMA 15 · Rodona, blanca i negra
def t15_teoria(c):
    pagina_tema(c, 15, 'Rodona, blanca i negra', 'Unes notes duren més i altres menys. Aprenem tres figures.', 'teoria')
    guia(c, M, Y(142), CW, 'Fins ara hem picat el pols. Ara farem notes que duren diferent: unes s’estiren molt i unes altres són ràpides. '
         'Imagina una pizza que es reparteix!', color=False, size=12.5, h=80)
    cw = (CW - 28) / 3.0
    yt = Y(238)
    h = 262
    dades = [('w', 'RODONA', 4, 'ta - a - a - a', '1 2 3 4'), ('h', 'BLANCA', 2, 'ta - a', '1 2'), ('q', 'NEGRA', 1, 'ta', '1')]
    for k, (t, nom, n, sil, cnt) in enumerate(dades):
        x = M + k * (cw + 14)
        rr(c, x + 3.4, yt - h - 3.4, cw, h, 8, fill=SOMBRA, lw=0)
        rr(c, x, yt - h, cw, h, 8, fill=white, lw=1.7, col=NAVY)
        rr(c, x, yt - 44, cw, 44, 8, fill=NAVY, lw=1.7, col=NAVY)
        c.setFillColor(NAVY)
        c.rect(x + 1.5, yt - 44, cw - 3, 12, stroke=0, fill=1)
        txt(c, x + cw / 2, yt - 30, nom, 17, ETQ, white, 'c')
        figura(c, t, x + cw / 2, yt - (92 if t != 'w' else 84), 12 if t != 'w' else 15)
        txt(c, x + cw / 2, yt - 142, 'dura %d temps' % n if n > 1 else 'dura 1 temps', 12.5, SANSB, NAVY, 'c')
        # caixes dels temps
        bw = (cw - 28) / 4.0
        for j in range(4):
            fill_ = WARM2 if j < n else white
            rr(c, x + 14 + j * bw, yt - 178, bw - 3, 20, 3, fill=fill_, lw=1.4, col=NAVY)
        txt(c, x + cw / 2, yt - 202, 'ho diem:', 10.5, SANS, MUTED, 'c')
        txt(c, x + cw / 2, yt - 220, sil, 14, SERIFB, NAVY, 'c')
        txt(c, x + cw / 2, yt - 242, 'compta: ' + cnt, 11, SANS, INK, 'c')
    yt = Y(514)
    h = 156
    panell(c, M, yt, CW, h, 'TOTES ENTREN EN QUATRE TEMPS')
    files = [('RODONA', 'w', [4]), ('BLANCA', 'h', [2, 2]), ('NEGRA', 'q', [1, 1, 1, 1])]
    for k, (nm, t, parts) in enumerate(files):
        yy = yt - 46 - k * 33
        txt(c, M + 18, yy - 12, nm, 11, SANSB, NAVY)
        tira_temps(c, M + 100, yy - 24, CW - 124, 30, [(t, p_) for p_ in parts])
    franja(c, M, Y(692), CW, 42, 'RECORDA', 'rodona = 4 temps  ·  blanca = 2 temps  ·  negra = 1 temps', 12.5)
    franja(c, M, Y(744), CW, 44, 'SABIES QUE?', 'En anglès: la rodona és «whole note» (nota sencera), la blanca «half note» (mitja) i la negra «quarter note» (un quart).', 11.2)
    c.showPage()


def t15_jocs(c):
    pagina_jocs(c, 15, 'Rodona, blanca i negra · a jugar!', 'Compta els temps amb els dits.',
                'Una pizza es parteix en trossos: la rodona és tota, la blanca és la meitat i la negra és un quart!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 176
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'UNEIX AMB UNA LÍNIA', n=1)
    consigna(c, M + 14, yt - 40, 'Cada figura amb el seu nom i amb els temps que dura.', CW - 28)
    fig = ['q', 'w', 'h']
    noms = ['blanca', 'negra', 'rodona']
    temps = ['4', '1', '2']
    for k in range(3):
        yy = yt - 82 - k * 36
        figura(c, fig[k], M + 54, yy - 4, 6.5 if fig[k] != 'w' else 9)
        c.setFillColor(NAVY)
        c.circle(M + 94, yy + 4, 4, stroke=0, fill=1)
        rr(c, M + 200, yy - 12, 84, 26, 13, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 242, yy - 4, noms[k], 12.5, SANSB, INK, 'c')
        c.circle(M + 190, yy + 4, 4, stroke=0, fill=1)
        c.circle(M + 294, yy + 4, 4, stroke=0, fill=1)
        rr(c, M + 396, yy - 12, 70, 26, 13, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 431, yy - 4, temps[k] + (' temps' if temps[k] != '1' else ' temps'), 12, SANSB, INK, 'c')
        c.circle(M + 386, yy + 4, 4, stroke=0, fill=1)
    h = 210
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUANTS TEMPS?', n=2)
    consigna(c, M + 14, yt - 40, 'Escriu el número a cada caseta.', pw - 28)
    for k, t in enumerate(['w', 'q', 'h', 'q', 'h', 'w']):
        col, fila = k % 3, k // 3
        xx = M + 24 + col * 78
        yy = yt - 88 - fila * 74
        figura(c, t, xx + 16, yy, 6.5 if t != 'w' else 8.5)
        rr(c, xx, yy - 40, 34, 26, 6, fill=white, lw=1.6, col=NAVY)
    panell(c, x2, yt, pw, h, 'PINTA ELS TEMPS', n=3)
    consigna(c, x2 + 14, yt - 40, 'Pinta tants quadradets com temps duri cada figura.', pw - 28)
    for k, (t, n) in enumerate([('w', 4), ('h', 2), ('q', 1), ('h', 2)]):
        yy = yt - 82 - k * 32
        figura(c, t, x2 + 34, yy - 2, 5 if t != 'w' else 7)
        for j in range(4):
            rr(c, x2 + 74 + j * 36, yy - 16, 32, 24, 4, fill=white, lw=1.5, col=NAVY)
    h = 132
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['La rodona dura 4 temps.', 'La negra dura més que la blanca.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'PICA I DIGUES', n=5)
    consigna(c, x2 + 14, yt - 40, 'Pica de mans i digues «ta»: la profe t’ho proposa!', pw - 28)
    for k, t in enumerate(['q', 'q', 'h', 'q', 'q']):
        figura(c, t, x2 + 34 + k * 40, yt - 100, 6)
    for k in range(5):
        rr(c, x2 + 20 + k * 40, yt - 126, 28, 16, 4, fill=white, lw=1.2, col=MUTED, dash=(2, 2))
    c.showPage()


# ======================================================================== TEMA 16 · La corxera
def t16_teoria(c):
    pagina_tema(c, 16, 'La corxera', 'Fins ara hem comptat notes de 4, 2 i 1 temps. Avui arriba la més ràpida!', 'teoria')
    guia(c, M, Y(142), CW, 'Dues corxeres juntes tarden el mateix que una sola negra. Per això són tan ràpides: en caben moltes en un compàs!',
         color=False, size=12.5, h=80)
    pw, x2 = meitats()
    yt = Y(238)
    h = 150
    panell(c, M, yt, pw, h, 'COM ES VEU')
    figura(c, 'e', M + 58, yt - 86, 11)
    txt(c, M + 58, yt - 118, 'SOLA', 11.5, SANSB, NAVY, 'c')
    txt(c, M + 58, yt - 133, 'amb banderola', 10.5, SANS, MUTED, 'c')
    figura(c, 'ee', M + 140, yt - 86, 11)
    txt(c, M + 182, yt - 118, 'JUNTES', 11.5, SANSB, NAVY, 'c')
    txt(c, M + 182, yt - 133, 'amb barra', 10.5, SANS, MUTED, 'c')
    panell(c, x2, yt, pw, h, 'QUANT DURA?')
    files = [('RODONA', 1), ('BLANCA', 2), ('NEGRA', 4), ('CORXERA', 8)]
    for k, (nm, n) in enumerate(files):
        yy = yt - 44 - k * 22
        txt(c, x2 + 12, yy - 4, nm, 10.5, SANSB, NAVY)
        bw = (pw - 100) / float(n)
        for j in range(n):
            rr(c, x2 + 84 + j * bw, yy - 10, bw - 2.5, 20, 2, fill=WARM2, lw=1.2, col=NAVY)
            if n <= 4:
                c.setFillColor(NAVY)
                c.circle(x2 + 84 + j * bw + (bw - 2.5) / 2, yy, 3, stroke=0, fill=1)
    txt(c, x2 + 12, yt - h + 10, 'Cada fila omple els mateixos 4 temps.', 9.8, SANS, MUTED)
    yt = Y(404)
    h = 112
    panell(c, M, yt, CW, h, 'COM ES DIU: TA I TI-TI')
    for fg, sil, xx in [('q', 'ta', 56), ('q', 'ta', 160), ('ee', 'ti-ti', 262), ('q', 'ta', 400)]:
        figura(c, fg, M + xx, yt - 66, 10)
        txt(c, M + xx + (18 if fg == 'ee' else 0), yt - 98, sil, 20, SERIFB, NAVY, 'c')
    txt(c, M + CW - 14, yt - 24, 'Diguem-ho i piquem de mans!', 11.5, SANS, NAVY_SOFT, 'r')
    yt = Y(532)
    h = 118
    panell(c, M, yt, CW, h, 'COMPTA AMB LES MANS')
    bw = (CW - 28) / 8.0
    for k in range(8):
        bx = M + 14 + k * bw
        num = (k % 2 == 0)
        rr(c, bx, yt - 72, bw - 3, 34, 4, fill=NAVY if num else WARM, lw=1.5, col=NAVY)
        txt(c, bx + (bw - 3) / 2, yt - 62, str(k // 2 + 1) if num else 'i', 19 if num else 17, SANSB if num else SANS,
            white if num else NAVY_SOFT, 'c')
    par(c, M + 14, yt - 90, 'Cada número és un temps. Cada «i» és la segona corxera. Pica una palma a cada número i una palmeta suau a cada «i».',
        11.8, CW - 28, 15.5, SANS, INK)
    yt = Y(670)
    h = 112
    caixa_t(c, M, yt, pw, h, 'RECORDA', '', 12.5)
    for k, t in enumerate(['2 corxeres  =  1 negra', '4 corxeres  =  1 blanca', '8 corxeres  =  1 rodona']):
        txt(c, M + 16, yt - 56 - k * 18, t, 13, SANSB, NAVY)
    caixa_t(c, x2, yt, pw, h, 'SABIES QUE?', 'En italià, la corxera es diu «croma», que vol dir colorida!', 12.5)
    c.showPage()


def t16_jocs(c):
    pagina_jocs(c, 16, 'La corxera · a jugar!', 'Dues corxeres = una negra.',
                'Les corxeres són les més ràpides! Compta-les, pica-les i digues «ti-ti» amb mi.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 138
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'ELS RITMES DEL MUSSOL', n=1)
    consigna(c, M + 14, yt - 40, 'Escriu «ta» o «ti-ti» sota cada figura i després pica-ho de mans.', CW - 28)
    rit = [['q', 'ee', 'q'], ['ee', 'ee', 'h'], ['q', 'q', 'ee', 'q']]
    for k, r_ in enumerate(rit):
        yy = yt - 78 - k * 22
        pass
    xs0 = M + 40
    for fila, r_ in enumerate([['q', 'ee', 'q'], ['ee', 'q', 'q'], ['ee', 'ee', 'q']]):
        for j, t in enumerate(r_):
            xx = M + 40 + fila * 164 + j * 46
            figura(c, t, xx - (6 if t == 'ee' else 0), yt - 82, 6.5)
            linia(c, xx - 14, yt - 112, 36 if t == 'ee' else 28)
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUANTES CORXERES?', n=2)
    consigna(c, M + 14, yt - 40, 'Completa amb el número que toca.', pw - 28)
    eq = [('1 negra', '=', '__ corxeres'), ('1 blanca', '=', '__ corxeres'), ('1 rodona', '=', '__ corxeres'), ('3 negres', '=', '__ corxeres')]
    for k, (a, b, c_) in enumerate(eq):
        yy = yt - 82 - k * 28
        txt(c, M + 16, yy, a, 12.5, SANSB, NAVY)
        txt(c, M + 100, yy, b, 14, SANSB, OCRE)
        rr(c, M + 122, yy - 10, 32, 24, 5, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 164, yy, 'corxeres', 12.5, SANS, INK)
    panell(c, x2, yt, pw, h, 'SOPA DE LLETRES', n=3)
    consigna(c, x2 + 14, yt - 40, 'Troba 6 paraules (→ i ↓).', pw - 28)
    pal = ['CORXERA', 'TA', 'TITI', 'PICA', 'TEMPS', 'MANS']
    dibuixa_sopa(c, x2 + 14, yt - 54, sopa(pal, 8, seed=53), 19, 13.5)
    llista_paraules(c, x2 + 14 + 8 * 19 + 18, yt - 70, pal, 11.5, 24)
    h = 150
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=4)
    consigna(c, M + 14, yt - 40, 'Cada figura amb com es diu.', pw - 28)
    fi = ['ee', 'q']
    for k in range(2):
        yy = yt - 88 - k * 40
        figura(c, fi[k], M + 50 - (6 if fi[k] == 'ee' else 0), yy, 6.5)
        c.setFillColor(NAVY)
        c.circle(M + 94, yy + 2, 4, stroke=0, fill=1)
        c.circle(M + 128, yy + 2, 4, stroke=0, fill=1)
        rr(c, M + 140, yy - 10, 90, 26, 13, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 185, yy - 2, ['negra', 'dues corxeres'][k] if False else ['negra', 'corxeres'][1 - k], 12, SANSB, INK, 'c')
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['Dues corxeres duren com una negra.', 'La corxera és més lenta que la negra.', 'En una rodona hi caben 8 corxeres.'], 11.8, 14)
    c.showPage()


# ======================================================================== TEMA 17 · Els temps i sumar figures
def t17_teoria(c):
    pagina_tema(c, 17, 'Els temps i sumar figures', 'Un compàs és una caixa de quatre temps. Aprenem a omplir-la amb figures.', 'teoria')
    guia(c, M, Y(142), CW, 'Mira aquesta caixa de 4 temps! Hi podem posar les figures que vulguem, però les hem de sumar: '
         'ni més ni menys que 4.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 270
    panell(c, M, yt, CW, h, 'FORMES D’OMPLIR 4 TEMPS')
    combos = [([('w', 4)], '4  =  4'), ([('h', 2), ('h', 2)], '2 + 2  =  4'), ([('q', 1)] * 4, '1 + 1 + 1 + 1  =  4'),
              ([('h', 2), ('q', 1), ('q', 1)], '2 + 1 + 1  =  4'), ([('q', 1), ('q', 1), ('h', 2)], '1 + 1 + 2  =  4'),
              ([('q', 1), ('ee', 1), ('h', 2)], '1 + ½ + ½ + 2  =  4')]
    for k, (figs, eq) in enumerate(combos):
        yy = yt - 48 - k * 36
        tira_temps(c, M + 18, yy - 24, 290, 30, figs)
        txt(c, M + 326, yy - 14, eq, 13, SERIFB, NAVY)
    franja(c, M, Y(526), CW, 44, 'RECORDA', 'Cada compàs de 4/4 té 4 temps. Si hi sumes 4, la caixa és plena!', 12.5)
    yt = Y(590)
    h = 190
    panell(c, M, yt, CW, h, 'ELS TEMPS DE CADA FIGURA')
    tab = [('w', 'rodona', '4'), ('h', 'blanca', '2'), ('q', 'negra', '1'), ('e', 'corxera', '½')]
    cw = (CW - 28) / 4.0
    for k, (t, nm, v) in enumerate(tab):
        x = M + 14 + k * cw
        rr(c, x + 2, yt - h + 14, cw - 8, h - 52, 8, fill=WARM, lw=1.5, col=NAVY)
        figura(c, t, x + cw / 2 - 3, yt - 88 if t != 'w' else yt - 78, 9 if t != 'w' else 11)
        txt(c, x + cw / 2 - 3, yt - 124, nm, 12.5, SANSB, NAVY, 'c')
        txt(c, x + cw / 2 - 3, yt - 156, v, 26, SERIFB, OCRE, 'c')
    c.showPage()


def t17_jocs(c):
    pagina_jocs(c, 17, 'Sumar figures · a jugar!', 'Suma, suma, suma!',
                'Cada compàs ha de sumar 4 temps. A veure si eres un bon comptador!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'QUINA FIGURA FALTA?', n=1)
    consigna(c, M + 14, yt - 40, 'Dibuixa la figura que falta perquè el compàs sumi 4 temps.', CW - 28)
    probs = [[('h', 2), ('h', 2)], [('q', 1), ('q', 1), ('h', 2)], [('h', 2), ('q', 1), ('q', 1)], [('w', 4)]]
    pb = [[('h', 2), None], [('q', 1), ('q', 1), None], [('h', 2), ('q', 1), None], [None]]
    for k, fg in enumerate(pb):
        yy = yt - 74 - k * 28
        unit = 330 / 4.0
        pos = 0
        for it in fg:
            if it is None:
                restant = 4 - sum(t for _, t in [x for x in fg if x])
                rr(c, M + 18 + pos * unit + 1, yy - 12, restant * unit - 2, 24, 5, fill=white, lw=1.5, col=MUTED, dash=(3, 2))
                txt(c, M + 18 + (pos + restant / 2) * unit, yy - 4, '?', 14, SANSB, MUTED, 'c')
                pos += restant
            else:
                rr(c, M + 18 + pos * unit + 1, yy - 12, it[1] * unit - 2, 24, 5, fill=WARM, lw=1.5, col=NAVY)
                icona_fig(c, it[0], M + 18 + (pos + it[1] / 2) * unit, yy - 3, 4.4)
                pos += it[1]
        txt(c, M + 372, yy - 4, '=  4 temps', 12, SANSB, NAVY_SOFT)
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'SUMA', n=2)
    consigna(c, M + 14, yt - 40, 'Escriu el total de cada compàs.', pw - 28)
    sums = [[('w', 4)], [('h', 2), ('q', 1)], [('q', 1), ('q', 1), ('h', 2)], [('h', 2), ('h', 2)]]
    for k, fg in enumerate(sums):
        yy = yt - 78 - k * 32
        pos = 0
        for it in fg:
            icona_fig(c, it[0], M + 24 + pos * 28 + 12, yy, 4.6)
            pos += 1
        rr(c, M + 18 + 112, yy - 10, 26, 22, 5, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 18 + 112 - 14, yy - 3, '=', 13, SANSB, OCRE, 'c')
    panell(c, x2, yt, pw, h, 'ES PASSA O NO HI ARRIBA?', n=3)
    consigna(c, x2 + 14, yt - 40, 'Posa ✓ si el compàs té exactament 4 temps.', pw - 28)
    chk = [[('h', 2), ('q', 1), ('q', 1)], [('w', 4), ('q', 1)], [('q', 1), ('q', 1), ('q', 1)], [('h', 2), ('h', 2)]]
    for k, fg in enumerate(chk):
        yy = yt - 82 - k * 32
        pos = 0
        for it in fg:
            icona_fig(c, it[0], x2 + 24 + pos * 30 + 12, yy, 4.6)
            pos += 1
        rr(c, x2 + pw - 46, yy - 10, 26, 24, 12, fill=white, lw=1.5, col=NAVY)
    h = 134
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'INVENTA EL TEU COMPÀS', n=4)
    consigna(c, M + 14, yt - 40, 'Dibuixa figures que sumin 4 temps. Pots fer-ne tres de diferents!', CW - 28)
    for k in range(3):
        rr(c, M + 14 + k * 162, yt - h + 14, 150, 52, 6, fill=white, lw=1.3, col=MUTED, dash=(3, 3))
    c.showPage()


# ======================================================================== TEMA 18 · El compàs
def t18_teoria(c):
    pagina_tema(c, 18, 'El compàs: 4/4, 3/4 i 2/4', 'El compàs agrupa els pulsos de la música en caixes iguals.', 'teoria')
    guia(c, M, Y(142), CW, 'Mira els dos números petits del començament! Ens diuen com es compta la música: de quatre en quatre, '
         'de tres en tres o de dos en dos.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 150
    panell(c, M, yt, CW, h, 'ELS DOS NÚMEROS')
    g = 14
    yb = pauta(c, M + 20, yt - 56, 150, g, 'treble', final=False)
    nt.draw_time_sig(c, M + 100, yb, g, '4', '4')
    trac(c, 2, OCRE)
    for (yy, tx, d) in ((yb + 3 * g, 'El de DALT: quants temps té cada compàs.', 1), (yb + 1 * g, 'El de BAIX: quina figura val un temps (el 4 és la negra).', 2)):
        c.line(M + 118, yy, M + 200, yy)
        c.setFillColor(OCRE)
        c.circle(M + 118, yy, 3, stroke=0, fill=1)
        par(c, M + 210, yy + 4, tx, 11.8, CW - 230, 14.5, SANS, INK)
    yt = Y(404)
    h = 240
    panell(c, M, yt, CW, h, 'TRES COMPASSOS')
    eixos = [((4, 4), 'C4 D4 E4 F4 | G4 F4 E4 D4', '4/4', 'quatre quarts', 'el més corrent: 1-2-3-4'),
             ((3, 4), 'C4 D4 E4 | F4 E4 D4', '3/4', 'tres quarts', 'el vals: 1-2-3'),
             ((2, 4), 'C4 D4 | E4 D4', '2/4', 'dos quarts', 'la marxa: 1-2')]
    for k, (cs, mt, num, nom, desc) in enumerate(eixos):
        yy = yt - 52 - k * 62
        sist(c, M + 16, yy, 310, 7.2, mt, 'treble', cs)
        txt(c, M + 346, yy - 8, num + '  ' + nom, 12.5, SANSB, NAVY)
        txt(c, M + 346, yy - 24, desc, 11, SANS, INK)
    franja(c, M, Y(664), CW, 44, 'RECORDA', 'La línia que separa els compassos és la barra de compàs.', 12.5)
    franja(c, M, Y(722), CW, 54, 'SABIES QUE?', 'El 3/4 és el ritme del vals: es balla tres passos per compàs, un-dos-tres, un-dos-tres…', 12)
    c.showPage()


def t18_jocs(c):
    pagina_jocs(c, 18, 'El compàs · a jugar!', 'Quatre, tres o dos temps?',
                'Els números ens diuen com comptar. Compta amb mi i trobaràs la resposta!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 218
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUIN COMPÀS ÉS?', n=1)
    consigna(c, M + 14, yt - 40, 'Compta les notes de cada compàs i marca-ho.', pw - 28)
    ex = ['C4 D4 E4 F4', 'G4 F4 E4', 'C4 D4']
    for k, t in enumerate(ex):
        yy = yt - 78 - k * 44
        sist(c, M + 14, yy, 100, 5.6, t, 'treble', (4, 4), show_time=False, show_clef=False)
        for j, l in enumerate(('2/4', '3/4', '4/4')):
            rr(c, M + 140 + j * 34 - 16, yy - 28, 32, 22, 11, fill=white, lw=1.4, col=NAVY)
            txt(c, M + 140 + j * 34, yy - 21, l, 10, SANSB, NAVY_SOFT, 'c')
    panell(c, x2, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=2)
    consigna(c, x2 + 14, yt - 40, 'Cada compàs amb la seva dansa.', pw - 28)

    def dib(c_, xr, yy, k):
        rr(c_, xr, yy - 14, 84, 28, 14, fill=white, lw=1.5, col=NAVY)
        txt(c_, xr + 42, yy - 5, ['la marxa', 'el vals', 'el rock'][k] if False else ['el vals', 'la marxa', 'una cançó'][k], 11.5, SANSB, INK, 'c')
    uneix(c, x2 + 14, yt - 80, pw - 28, ['3/4', '2/4', '4/4'], ['', '', ''], fila=46, ampl_esq=60, ampl_dre=84, dibuix_dre=dib, serif=True)
    h = 160
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'COMPLETA EL COMPÀS', n=3)
    consigna(c, M + 14, yt - 40, 'Dibuixa la nota que falta i després compta fins al final del compàs.', CW - 28)
    for k, (cs, t) in enumerate((((4, 4), 'C4 D4 E4'), ((3, 4), 'G4 F4'), ((2, 4), 'E4'))):
        x = M + 14 + k * 164
        sist(c, x, yt - 76, 150, 5.8, t, 'treble', cs, show_clef=True)
        rr(c, x + 100, yt - 76 - 24, 30, 24, 4, fill=white, lw=1.2, col=MUTED, dash=(2, 2)) if False else None
    h = 118
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['El 3/4 té tres temps.', 'En 4/4 comptem 1-2-3.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'PICA EL COMPÀS', n=5)
    consigna(c, x2 + 14, yt - 40, 'La profe diu un compàs i tu piques els temps fent un petó al primer!', pw - 28)
    c.showPage()


# ======================================================================== TEMA 19 · Puntet i lligadura
def t19_teoria(c):
    pagina_tema(c, 19, 'Allargar notes: puntet i lligadura', 'Dos trucs per fer que una nota duri una mica més.', 'teoria')
    guia(c, M, Y(142), CW, 'A vegades una nota necessita estirar-se! Per això tenim dos trucs: un puntet i una línia corba que '
         'es diu lligadura.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 196
    panell(c, M, yt, CW, h, 'EL PUNTET')
    txt(c, M + 16, yt - 46, 'Un puntet al costat de la nota li afegeix la MEITAT del que dura.', 12, SANSB, NAVY)
    for k, (t, a, b, eq) in enumerate((('h', 2, 1, 'blanca (2) + meitat (1)  =  3 temps'), ('q', 1, 0.5, 'negra (1) + meitat (½)  =  1½ temps'))):
        yy = yt - 78 - k * 54
        icona_fig(c, t + '.', M + 44, yy - 8, 8)
        tira_temps(c, M + 100, yy - 22, 110 if k == 0 else 56, 34, [(t, a)], total=a)
        rr(c, M + 100 + (a * (110 / 2.0 if k == 0 else 56)), yy - 22, (b * (110 / 2.0 if k == 0 else 56 / 1.0)) - 0, 34, 5, fill=white, lw=1.5, col=OCRE, dash=(3, 2))
        txt(c, M + 100 + (a + b) * (55 if k == 0 else 56) + 16, yy - 8, eq, 12, SANS, INK)
    franja(c, M, Y(448), CW, 44, 'RECORDA', 'Puntet = la nota + la seva meitat.', 12.5)
    yt = Y(508)
    h = 216
    panell(c, M, yt, CW, h, 'LA LLIGADURA')
    par(c, M + 16, yt - 46, 'Una línia corba que uneix DUES NOTES IGUALS: sona una sola vegada, i dura els temps de les dues.', 11.8, CW - 32, 15, SANSB, NAVY)
    sist(c, M + 16, yt - 100, 440, 7.5, 'E4:q E4:q~ E4:q E4:q | D4:h~ D4:q C4:q', 'treble', (4, 4))
    txt(c, M + 16, yt - 148, 'negra + negra lligades = 2 temps', 11.5, SANS, INK)
    txt(c, M + 16, yt - 166, 'blanca + negra lligades = 3 temps', 11.5, SANS, INK)
    txt(c, M + 16, yt - 184, 'Només es lliguen notes del mateix so!', 11.5, SANSB, OCRE)
    franja(c, M, Y(738), CW, 48, 'SABIES QUE?', 'Una blanca amb puntet és igual que una blanca lligada a una negra: tres temps!', 12)
    c.showPage()


def t19_jocs(c):
    pagina_jocs(c, 19, 'Puntet i lligadura · a jugar!', 'Estira les notes!',
                'Ara tens dos trucs per allargar notes: el puntet i la lligadura. Prova’ls!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 204
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUANTS TEMPS?', n=1)
    consigna(c, M + 14, yt - 40, 'Escriu els temps que dura cada nota.', pw - 28)
    for k, t in enumerate(['h.', 'q.', 'h', 'q']):
        col, fila = k % 2, k // 2
        xx = M + 24 + col * 110
        yy = yt - 92 - fila * 62
        icona_fig(c, t, xx + 16, yy, 6.5)
        rr(c, xx + 44, yy - 20, 36, 26, 6, fill=white, lw=1.5, col=NAVY)
    panell(c, x2, yt, pw, h, 'PUNTET O LLIGADURA?', n=2)
    consigna(c, x2 + 14, yt - 40, 'Escriu P (puntet) o L (lligadura).', pw - 28)
    exs = ['E4:h. R:q', 'E4:q~ E4:q R:h', 'G4:q. G4:e R:h']
    for k, e in enumerate(exs):
        yy = yt - 74 - k * 42
        sist(c, x2 + 14, yy, 150, 5, e, 'treble', (4, 4), show_clef=False, show_time=False)
        rr(c, x2 + pw - 46, yy - 20, 28, 24, 12, fill=white, lw=1.5, col=NAVY)
    h = 168
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'SUMA ELS TEMPS', n=3)
    consigna(c, M + 14, yt - 40, 'Suma tots els temps de cada compàs. Han de ser 4!', CW - 28)
    for k, t in enumerate(['E4:h. E4:q', 'C4:q~ C4:q D4:h', 'G4:q. G4:e A4:h']):
        xx = M + 14 + k * 164
        sist(c, xx, yt - 76, 150, 5.4, t, 'treble', (4, 4), show_clef=False, show_time=False)
        txt(c, xx + 30, yt - 128, 'total =', 12, SANSB, OCRE, 'c')
        rr(c, xx + 62, yt - 138, 36, 26, 5, fill=white, lw=1.5, col=NAVY)
    h = 138
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['El puntet afegeix la meitat.', 'La lligadura uneix notes diferents.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'DIBUIXA', n=5)
    consigna(c, x2 + 14, yt - 40, 'Dibuixa una blanca amb puntet i una lligadura entre dues negres.', pw - 28)
    casella_dibuix(c, x2 + 14, yt - h + 14, pw - 28, 50, None)
    c.showPage()
