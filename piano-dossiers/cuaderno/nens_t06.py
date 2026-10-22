# -*- coding: utf-8 -*-
"""Capítol 7 · Toquem! — temes 24 a 30 (teoria + jocs)."""
from nens_t05 import *                                            # noqa: F401,F403
from nens_jocs2 import p_cruci, p_cami, p_intrus, p_mosaic, p_laberint, HEART, HOUSE
from nens_t01 import pagina_jocs
from nens_tclas import pauta, cap, gran_pauta
import notation as nt
from nens_dib import punts_dits

HCB = 'E4 D4 C4:h | E4 D4 C4:h | C4:e C4:e C4:e C4:e D4:e D4:e D4:e D4:e | E4 D4 C4:h'
HCB_E = 'E3 D3 C3:h | E3 D3 C3:h | C3:e C3:e C3:e C3:e D3:e D3:e D3:e D3:e | E3 D3 C3:h'
MARY = 'E4 D4 C4 D4 | E4 E4 E4:h | D4 D4 D4:h | E4 G4 G4:h | E4 D4 C4 D4 | E4 E4 E4 E4 | D4 D4 E4 D4 | C4:w'
AU = 'G4 G4 G4 A4 | B4:h A4:h | G4 B4 A4 A4 | G4:w'
ODA = 'E4 E4 F4 G4 | G4 F4 E4 D4 | C4 C4 D4 E4 | E4 D4 D4:h | E4 E4 F4 G4 | G4 F4 E4 D4 | C4 C4 D4 E4 | D4 C4 C4:h'


def mans_sobre_tecles(c, x, ytop, w, esq=False, h_ma=0.47, kh=62):
    """Una mà vista de dalt amb línies cap a les cinc tecles de la posició (DO-SOL)."""
    cw_ = w
    kb_y = ytop - 236
    nb = 5
    dits = {i: (5 - i if esq else i + 1) for i in range(5)}
    kx, kwid = x + 20, cw_ - 40
    teclat(c, kx, kb_y, kwid, kh, nb=nb, resalta={i: ORDRE[i] for i in range(5)}, noms='resalta', color=True, dits=dits)
    cx = x + cw_ / 2
    cy = ytop - 104
    ma_real(c, cx, cy, h_ma, esq=esq, dits=True, color=False)
    kw = kwid / float(nb)
    pts = punts_dits(cx, cy, h_ma, esq)
    for n in range(1, 6):
        px, py = pts[n]
        idx = (n - 1) if not esq else (5 - n)
        tx = kx + idx * kw + kw / 2
        trac(c, 1.2, OCRE, (2, 3))
        c.line(px, py - 8, tx, kb_y + kh + 8)
        c.setDash()


def gran_sist(c, x, ytop, w, gap, rh, lh, compas=(4, 4)):
    """Dos pentagrames alineats (clau de sol dalt, clau de fa baix) amb la seva clau."""
    sep = gap * 8.6
    sist(c, x, ytop, w, gap, rh, 'treble', compas)
    sist(c, x, ytop - sep, w, gap, lh, 'bass', compas)
    yt_ = ytop
    yb_ = ytop - sep - 4 * gap
    trac(c, 2.4, NAVY)
    p = c.beginPath()
    bx = x - 6
    ym = (yt_ + yb_) / 2.0
    p.moveTo(bx + 5, yt_)
    p.curveTo(bx - 7, yt_ - (yt_ - ym) * 0.25, bx + 6, ym + (yt_ - ym) * 0.35, bx - 8, ym)
    p.curveTo(bx + 6, ym - (yt_ - ym) * 0.35, bx - 7, yb_ + (yt_ - ym) * 0.25, bx + 5, yb_)
    c.drawPath(p, stroke=1, fill=0)
    trac(c, 1.3, NAVY)
    c.line(x, yt_, x, yb_)
    return yb_


# ======================================================================== TEMA 24 · Posició de Do, mà dreta
def t24_teoria(c):
    pagina_tema(c, 24, 'Posició de Do: mà dreta', 'Posem la mà al piano i fem sonar les cinc primeres notes.', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Per fi toquem! Posa la mà dreta sobre el teclat: el polze al DO i cada dit sobre la seva tecla. '
         'Tindràs DO, RE, MI, FA i SOL sota els dits.', color=True, size=12.5, h=80)
    yt = Y(238)
    h = 248
    panell(c, M, yt, 300, h, 'LA MÀ DRETA AL TECLAT')
    mans_sobre_tecles(c, M, yt, 300, esq=False)
    xx = M + 300 + 18
    panell(c, xx, yt, CW - 318, h, 'COM POSAR LA MÀ')
    items = ['Dits arrodonits, com si sostinguessis una pilota.', 'Polze al costat, no pla.', 'Canell relaxat, a l’altura del teclat.',
             'Cada dit, una tecla.']
    yy = yt - 50
    for k, t in enumerate(items):
        bola(c, xx + 18, yy - 4, k + 1, 10)
        yy = par(c, xx + 36, yy, t, 11.2, CW - 318 - 50, 13.5, SANS, INK) - 12
    yt = Y(504)
    h = 148
    panell(c, M, yt, CW, h, 'EL PRIMER EXERCICI')
    sist(c, M + 16, yt - 58, 440, 7.5, 'C4 D4 E4 F4 | G4 F4 E4 D4 | C4:w', 'treble', (4, 4))
    txt(c, M + 16, yt - h + 14, 'Digues els noms de les notes mentre les toques: DO, RE, MI, FA, SOL, FA, MI, RE, DO.', 11.5, SANS, INK)
    franja(c, M, Y(668), CW, 44, 'RECORDA', 'La mà dreta comença amb el polze (1) al DO i acaba amb el petit (5) al SOL.', 12)
    franja(c, M, Y(726), CW, 52, 'ESCOLTO', 'Toca DO-RE-MI-FA-SOL pujant i baixant: sents com el so va de greu a agut?', 12)
    c.showPage()


def t24_jocs(c):
    pagina_jocs(c, 24, 'La mà dreta · a jugar!', 'Cada dit, la seva nota.',
                'Ara que tens la mà al lloc, juguem a trobar notes i dits. Pots provar-ho al piano mentre ho fas!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 200
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUIN DIT?', n=1)
    consigna(c, M + 14, yt - 40, 'Escriu el dit de cada nota.', pw - 28)
    for k, nm in enumerate(['DO', 'MI', 'SOL', 'RE', 'FA']):
        yy = yt - 80 - (k // 3) * 54
        xx = M + 20 + (k % 3) * 76
        rr(c, xx, yy - 2, 62, 24, 12, fill=HexColor(COL[nm]) if False else WARM, lw=1.5, col=NAVY)
        txt(c, xx + 31, yy + 5, nm, 12.5, SERIFB, NAVY, 'c')
        rr(c, xx + 16, yy - 32, 30, 24, 6, fill=white, lw=1.5, col=NAVY)
    p_cruci(c, x2, yt, pw, h, 2, [('DITS', 2, 0, 'h', 1), ('TECLA', 2, 2, 'v', 2), ('DO', 2, 0, 'v', 3)], [('1 →', 'Cada mà en té cinc.'), ('2 ↓', 'Es prem per fer sonar la nota.'), ('3 ↓', 'La nota del polze de la mà dreta.')], 21)
    h = 178
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'LLEGEIX I TOCA', n=3)
    consigna(c, M + 14, yt - 40, 'Mira cada línia, digues els noms i toca-la amb la mà dreta.', CW - 28)
    sist(c, M + 16, yt - 76, 440, 6.8, 'C4 C4 D4 D4 | E4 E4 F4 F4 | G4:w', 'treble', (4, 4))
    sist(c, M + 16, yt - 130, 440, 6.8, 'G4 F4 E4 D4 | C4 D4 E4:h | G4 E4 C4:h', 'treble', (4, 4))
    h = 138
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['El polze és el dit 1.', 'El dit petit toca el DO.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'EL MEU EXERCICI', n=5)
    consigna(c, x2 + 14, yt - 40, 'Escriu 4 notes de la posició de Do. Les pots tocar!', pw - 28)
    pauta(c, x2 + 14, yt - 84, pw - 28, 6, 'treble', final=True)
    c.showPage()


# ======================================================================== TEMA 25 · Mà esquerra i clau de fa
def t25_teoria(c):
    pagina_tema(c, 25, 'Mà esquerra i clau de fa', 'La mà esquerra toca les notes greus i les llegeix a la clau de fa.', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Ara li toca a la mà esquerra! Ella viu a la banda greu del piano i llegeix amb la clau de fa. '
         'Comença pel dit petit!', color=True, size=12.5, h=80)
    yt = Y(238)
    h = 248
    panell(c, M, yt, 300, h, 'LA MÀ ESQUERRA AL TECLAT')
    mans_sobre_tecles(c, M, yt, 300, esq=True)
    xx = M + 300 + 18
    panell(c, xx, yt, CW - 318, h, 'ELS DITS DE LA MÀ ESQUERRA')
    items = ['Del 5 (el petit) al 1 (el polze).', 'El DO és el dit petit: el 5.', 'Aquí és el polze qui toca el SOL.', 'La mà també va arrodonida.']
    yy = yt - 50
    for k, t in enumerate(items):
        bola(c, xx + 18, yy - 4, k + 1, 10)
        yy = par(c, xx + 36, yy, t, 11.2, CW - 318 - 50, 13.5, SANS, INK) - 12
    yt = Y(504)
    h = 148
    panell(c, M, yt, CW, h, 'EL PRIMER EXERCICI')
    sist(c, M + 16, yt - 58, 440, 7.5, 'C3 D3 E3 F3 | G3 F3 E3 D3 | C3:w', 'bass', (4, 4))
    txt(c, M + 16, yt - h + 14, 'Són les mateixes notes de la mà dreta, però una octava més greu.', 11.5, SANS, INK)
    franja(c, M, Y(668), CW, 44, 'RECORDA', 'La mà esquerra comença pel dit petit (5) al DO i acaba amb el polze (1) al SOL.', 12)
    franja(c, M, Y(726), CW, 52, 'ESCOLTO', 'Toca la mateixa melodia amb la mà dreta i amb l’esquerra: quina sona més greu?', 12)
    c.showPage()


def t25_jocs(c):
    pagina_jocs(c, 25, 'La mà esquerra · a jugar!', 'Cap als greus!',
                'La mà esquerra viu a baix, a la clau de fa. Anem a trobar-la!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 200
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'MÀ DRETA O ESQUERRA?', n=1)
    consigna(c, M + 14, yt - 40, 'Marca D o E: quina mà toca cada línia?', pw - 28)
    for k, (cl, t) in enumerate((('treble', 'C4 E4 G4'), ('bass', 'C3 D3 E3'), ('bass', 'G3 F3 E3'), ('treble', 'G4 F4 E4'))):
        col, fila = k % 2, k // 2
        xx = M + 14 + col * 116
        yy = yt - 86 - fila * 54
        sist(c, xx, yy, 100, 5.4, t, cl, (4, 4), show_time=False)
        for j, l in enumerate(('D', 'E')):
            rr(c, xx + 24 + j * 30, yy - 44, 24, 20, 10, fill=white, lw=1.4, col=NAVY)
            txt(c, xx + 36 + j * 30, yy - 38, l, 10.5, SANSB, NAVY_SOFT, 'c')
    panell(c, x2, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=2)
    consigna(c, x2 + 14, yt - 40, 'Cada nota amb el seu dit de la mà esquerra.', pw - 28)
    uneix(c, x2 + 14, yt - 84, pw - 28, ['DO', 'RE', 'MI', 'SOL'], ['', '', '', ''], fila=36, ampl_esq=60, ampl_dre=58, serif=True,
          dibuix_dre=lambda c_, xr, yy, k: (rr(c_, xr, yy - 13, 50, 26, 13, fill=white, lw=1.5, col=NAVY),
                                          txt(c_, xr + 25, yy - 5, ['dit 5', 'dit 1', 'dit 4', 'dit 3'][k], 11.5, SANSB, INK, 'c')))
    h = 178
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'LLEGEIX I TOCA', n=3)
    consigna(c, M + 14, yt - 40, 'Digues els noms i toca-ho amb la mà esquerra.', CW - 28)
    sist(c, M + 16, yt - 80, 440, 6.8, 'C3 D3 E3 F3 | G3 F3 E3 D3 | C3:w', 'bass', (4, 4))
    sist(c, M + 16, yt - 132, 440, 6.8, 'G3 E3 C3 E3 | G3 G3 G3:h', 'bass', (4, 4))
    h = 130
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['La mà esquerra llegeix la clau de fa.', 'El polze esquerre toca el DO.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'DIBUIXA', n=5)
    consigna(c, x2 + 14, yt - 40, 'Escriu el DO que toca el dit petit de la mà esquerra.', pw - 28)
    pauta(c, x2 + 14, yt - 82, pw - 28, 6, 'bass', final=True)
    c.showPage()


# ======================================================================== TEMA 26 · Les dues mans juntes
def t26_teoria(c):
    pagina_tema(c, 26, 'Les dues mans juntes', 'Ara toquem amb les dues mans alhora, cada una al seu pentagrama.', 'teoria', color=False)
    guia(c, M, Y(142), CW, 'Dues mans, dos pentagrames! Les notes que van una sobre l’altra sonen alhora. Mira bé les barres: '
         'serveixen per saber què toca cada mà en cada moment.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 420
    panell(c, M, yt, CW, h, 'TRES MANERES DE TOCAR JUNTES')
    exs = [('1 · Mans iguals', 'C4 D4 E4 F4 | G4:w', 'C3 D3 E3 F3 | G3:w', 'Les dues mans fan el mateix, una octava de diferència.'),
           ('2 · Una canta, l’altra acompanya', 'E4 D4 C4 D4 | E4:h E4:h', 'C3:w | C3:w', 'La mà dreta fa la melodia i l’esquerra aguanta una nota llarga.'),
           ('3 · Mans contràries', 'C4 D4 E4 F4 | G4:w', 'G3 F3 E3 D3 | C3:w', 'Una puja i l’altra baixa, com al mirall.')]
    for k, (t, rh, lh, d) in enumerate(exs):
        top = yt - 58 - k * 124
        txt(c, M + 16, top + 10, t, 12, SANSB, NAVY)
        gran_sist(c, M + 30, top - 8, CW - 56, 6, rh, lh)
        txt(c, M + 16, top - 100, d, 11, SANS, INK)
    franja(c, M, Y(678), CW, 44, 'RECORDA', 'Les notes una sobre l’altra es toquen alhora.', 12.5)
    franja(c, M, Y(734), CW, 52, 'SABIES QUE?', 'Els pianistes fan servir cada mà per a una cosa diferent: tenen dos cervells a les mans!', 11.8) if False else None
    c.showPage()


def t26_jocs(c):
    pagina_jocs(c, 26, 'Les dues mans juntes · a jugar!', 'Una mà, una altra mà…',
                'Tocar amb dues mans és com fregar-se la panxa i donar-se copets al cap: cal pràctica! Comencem fàcil.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'TOCA JUNT', n=1)
    consigna(c, M + 14, yt - 40, 'Primer una mà, després l’altra i finalment les dues juntes!', CW - 28)
    gran_sist(c, M + 30, yt - 74, CW - 56, 6.4, 'C4 C4 G4 G4 | A4 A4 G4:h', 'C3:w | C3:w')
    h = 148
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'COMPLETA', n=2)
    consigna(c, M + 14, yt - 40, 'La mà dreta fa DO RE MI FA. Escriu el mateix amb l’esquerra, més greu.', pw - 28)
    sist(c, M + 14, yt - 80, pw - 28, 5.8, 'C4 D4 E4 F4', 'treble', (4, 4), show_time=False)
    pauta(c, M + 14, yt - 124, pw - 28, 5.8, 'bass', final=True)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=3)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['Les notes una sobre l’altra sonen alhora.', 'Cada mà toca el seu pentagrama.'], 11.8, 14)
    h = 150
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'EL JOC DE L’ECO', n=4)
    par(c, M + 14, yt - 44, 'La profe toca tres notes amb una mà i tu les repeteixes amb la mateixa mà, com un eco. Després canvieu de mà i, finalment, ho feu a dos.', 12, CW - 28, 16, SANS, INK)
    for k, t in enumerate(['mà dreta', 'mà esquerra', 'les dues']):
        rr(c, M + 24 + k * 160, yt - h + 18, 22, 22, 4, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 54 + k * 160, yt - h + 24, t, 12, SANSB, NAVY)
    c.showPage()


# ======================================================================== TEMA 27 · Les primeres cançons
def pagina_extra(c, n, titol, intro, desplaça):
    from nens_tclas import pagina, mapa, pla
    t = pla.TEMES[n]
    pagina(c, pla.kicker(n), titol, 'Tema %d  ·  teoria' % n, intro, t['pag'] + desplaça, False)
    items, act = pla.pagines_cap(n)
    mapa(c, Y(124), items, act)


def panell_canco(c, x, yt, w, h, titol, origen, sistemes, pistes_, mes=None):
    panell(c, x, yt, w, h, titol)
    txt(c, x + 16, yt - 42, origen, 11, SANS, MUTED)
    yy = yt - 76
    for (txt_m, gap_) in sistemes:
        sist(c, x + 16, yy, w - 32, gap_, txt_m, 'treble', (4, 4))
        yy -= 76
    yy -= 4
    for t in pistes_:
        c.setFillColor(OCRE)
        c.circle(x + 22, yy + 4, 3.2, stroke=0, fill=1)
        yy = par(c, x + 32, yy, t, 11.2, w - 50, 13.5, SANS, INK) - 3


def t27_teoria(c):
    pagina_tema(c, 27, 'Les primeres cançons', 'Ja tens les notes, els ritmes i les mans: és hora de tocar cançons de veritat!', 'teoria', color=False)
    guia(c, M, Y(142), CW, 'Quatre cançons que coneix tot el món! Les pots tocar amb les notes DO, RE, MI, FA i SOL. '
         'Primer les cantem i després les toquem.', color=False, size=12.5, h=80)
    panell_canco(c, M, Y(238), CW, 214, 'HOT CROSS BUNS', 'Cançó popular anglesa · mà dreta, posició de Do',
                 [(HCB, 9)], ['Canta-la: «Hot cross buns, hot cross buns…»', 'Les corxeres del compàs 3 són «ti-ti»: DO DO DO DO i RE RE RE RE.',
                                'Toca-la també amb la mà esquerra, una octava més greu.'])
    panell_canco(c, M, Y(468), CW, 292, 'MARY HAD A LITTLE LAMB', 'Cançó infantil · mà dreta, posició de Do',
                 [('E4 D4 C4 D4 | E4 E4 E4:h | D4 D4 D4:h | E4 G4 G4:h', 9), ('E4 D4 C4 D4 | E4 E4 E4 E4 | D4 D4 E4 D4 | C4:w', 9)],
                 ['Fixa’t: la melodia baixa, puja i es repeteix. Ho recordes?', 'Les notes llargues són blanques: duren 2 temps.'])
    c.showPage()
    pagina_extra(c, 27, 'Les primeres cançons (2)', 'Dues cançons més, una de francesa i una de Beethoven!', 1)
    panell_canco(c, M, Y(150), CW, 200, 'AU CLAIR DE LA LUNE', 'Cançó popular francesa · mà dreta, posició de Sol (SOL LA SI)',
                 [(AU, 9)], ['Aquesta cançó va per SOL, LA i SI: posa el polze al SOL.', 'Explica la història d’en Pierrot i la llum de la lluna.'])
    panell_canco(c, M, Y(374), CW, 296, 'L’ODA A L’ALEGRIA', 'Ludwig van Beethoven (1824) · simplificada · mà dreta, posició de Do',
                 [('E4 E4 F4 G4 | G4 F4 E4 D4 | C4 C4 D4 E4 | E4 D4 D4:h', 9), ('E4 E4 F4 G4 | G4 F4 E4 D4 | C4 C4 D4 E4 | D4 C4 C4:h', 9)],
                 ['Beethoven la va escriure per a una simfonia molt gran.', 'Aquí només en toquem la melodia: la pots taral·lejar a casa!'])
    franja(c, M, Y(690), CW, 56, 'RECORDA', 'Una cançó es toca a poc a poc: primer ben fet, després més ràpid.', 12.5)
    c.showPage()


def t27_jocs(c):
    from nens_tclas import pagina
    pagina(c, pla.kicker(27), 'Les cançons · a jugar!', 'Tema 27  ·  jocs', 'Cançons amagades, notes que falten i molta música.',
           pla.TEMES[27]['pag'] + 2, False)
    guia(c, M, Y(122), CW, 'Quina cançó és? A veure si les reconeixes pel principi! Després dibuixa i completa.',
         color=False, size=12.5, h=66)
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUINA CANÇÓ ÉS?', n=1)
    consigna(c, M + 14, yt - 40, 'Uneix cada principi amb la seva cançó.', pw - 28)
    inicis = ['E4 D4 C4', 'G4 G4 G4 A4', 'E4 E4 F4 G4']
    for k, t in enumerate(inicis):
        yy = yt - 78 - k * 44
        sist(c, M + 14, yy, 96, 5.2, t, 'treble', (4, 4), show_time=False)
        c.setFillColor(NAVY)
        c.circle(M + 120, yy - 10, 3.6, stroke=0, fill=1)
    for k, t in enumerate(['Oda a l’alegria', 'Hot Cross Buns', 'Au clair de la lune']):
        yy = yt - 78 - k * 44
        rr(c, M + 134, yy - 24, pw - 148, 28, 14, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 134 + (pw - 148) / 2, yy - 15, t, 10.2, SANSB, INK, 'c')
        c.setFillColor(NAVY)
        c.circle(M + 128, yy - 10, 3.6, stroke=0, fill=1)
    panell(c, x2, yt, pw, h, 'COMPLETA LA NOTA', n=2)
    consigna(c, x2 + 14, yt - 40, 'A «Hot Cross Buns» li falta l’última nota del compàs. Dibuixa-la!', pw - 28)
    sist(c, x2 + 14, yt - 96, pw - 28, 6.4, 'E4 D4', 'treble', (4, 4))
    par(c, x2 + 14, yt - 150, 'Pista: és una blanca i viu a la ratlleta addicional.', 11.2, pw - 28, 13.5, SANS, MUTED)
    h = 214
    yt = pila.pren(h)
    p_mosaic(c, M, yt, pw, h, 3, HEART)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['Beethoven va escriure l’Oda a l’alegria.', 'Mary tenia un cavall.', 'Hot Cross Buns té corxeres.'], 11.8, 14)
    h = 106
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'LA MEVA CANÇÓ PREFERIDA', n=5)
    consigna(c, M + 14, yt - 40, 'Quina és la que més t’agrada i per què?', CW - 28)
    linia(c, M + 16, yt - 78, CW - 32)
    c.showPage()


# ======================================================================== TEMA 28 · Llegir a primer cop d'ull
def icona_ull(c, cx, cy, s=1.0):
    trac(c, 1.8, NAVY)
    c.setFillColor(white)
    p = c.beginPath()
    p.moveTo(cx - 22 * s, cy)
    p.curveTo(cx - 10 * s, cy + 18 * s, cx + 10 * s, cy + 18 * s, cx + 22 * s, cy)
    p.curveTo(cx + 10 * s, cy - 18 * s, cx - 10 * s, cy - 18 * s, cx - 22 * s, cy)
    p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(NAVY)
    c.circle(cx, cy, 8 * s, stroke=0, fill=1)
    c.setFillColor(white)
    c.circle(cx + 2.4 * s, cy + 2.4 * s, 2.4 * s, stroke=0, fill=1)


def t28_teoria(c):
    pagina_tema(c, 28, 'Llegir a primer cop d’ull', 'Un bon músic mira abans de tocar. Aprèn a fer-ho en quatre passos!', 'teoria')
    guia(c, M, Y(142), CW, 'Abans de tocar una cançó nova, jo la miro amb els meus ulls de mussol! Ens fixem en quatre coses, '
         'sempre en el mateix ordre.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 250
    panell(c, M, yt, CW, h, 'ELS QUATRE PASSOS DEL MUSSOL')
    passos = [('LA CLAU I EL COMPÀS', 'Quina mà? Quants temps?'), ('LA DIRECCIÓ', 'La melodia puja, baixa o es repeteix?'),
              ('EL RITME', 'Hi ha silencis, blanques o corxeres?'), ('ELS DITS', 'On poso el polze al començament?')]
    cw = (CW - 28) / 4.0
    for k, (t, d) in enumerate(passos):
        x = M + 14 + k * cw
        rr(c, x + 2, yt - h + 14, cw - 8, h - 50, 8, fill=WARM, lw=1.5, col=NAVY)
        bola(c, x + 20, yt - 62, k + 1, 11)
        icona_ull(c, x + cw / 2 - 3, yt - 106, 1.0)
        par(c, x + 12, yt - 146, t, 11.6, cw - 28, 14, SANSB, NAVY)
        par(c, x + 12, yt - 184, d, 10.8, cw - 28, 13.2, SANS, INK)
    yt = Y(504)
    h = 160
    panell(c, M, yt, CW, h, 'PROVA-HO AMB AQUESTA MELODIA')
    sist(c, M + 16, yt - 66, 440, 7.6, 'C4 D4 E4 F4 | G4:h G4:h | F4 E4 D4 C4 | C4:w', 'treble', (4, 4))
    txt(c, M + 16, yt - h + 28, '1) clau de sol, 4/4  ·  2) puja i després baixa  ·  3) dues blanques i una rodona  ·  4) polze al DO', 11, SANS, INK)
    franja(c, M, Y(678), CW, 44, 'RECORDA', 'Mira primer, toca després: així t’equivoques menys!', 12.5)
    franja(c, M, Y(736), CW, 48, 'SABIES QUE?', 'Els músics professionals llegeixen una partitura nova en uns minuts: ho fan sempre amb aquests passos!', 11.5)
    c.showPage()


def t28_jocs(c):
    pagina_jocs(c, 28, 'Llegir · a jugar!', 'Ulls de mussol!',
                'Fixa’t molt bé en cada pentagrama: hi ha trampes amagades. Tu pots descobrir-les!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'TROBA LES 3 DIFERÈNCIES', n=1)
    consigna(c, M + 14, yt - 40, 'Les dues melodies són gairebé iguals. Encercla el que canvia a la segona.', CW - 28)
    sist(c, M + 16, yt - 80, 440, 7.4, 'C4 D4 E4 F4 | G4 F4 E4 D4 | C4:w', 'treble', (4, 4))
    sist(c, M + 16, yt - 150, 440, 7.4, 'C4 D4 E4 G4 | G4 E4 E4 D4 | C4:h C4:h', 'treble', (4, 4))
    h = 202
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUINA ÉS L’ÚLTIMA NOTA?', n=2)
    consigna(c, M + 14, yt - 40, 'Mira la melodia 5 segons i escriu l’última nota.', pw - 28)
    sist(c, M + 14, yt - 82, pw - 28, 6.4, 'E4 E4 F4 G4 | G4 F4 E4 D4 | C4:w', 'treble', (4, 4))
    rr(c, M + 14, yt - h + 14, 70, 26, 6, fill=white, lw=1.5, col=NAVY)
    panell(c, x2, yt, pw, h, 'SOPA DE LLETRES', n=3)
    consigna(c, x2 + 14, yt - 40, 'Troba 6 paraules (→ i ↓).', pw - 28)
    pal = ['MIRA', 'CLAU', 'RITME', 'DITS', 'PUJA', 'BAIXA']
    dibuixa_sopa(c, x2 + 14, yt - 52, sopa(pal, 8, seed=81), 17, 12.5)
    h = 118
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['Primer toquem i després mirem.', 'Cal mirar la clau i el compàs.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'EL REPTE DEL MUSSOL', n=5)
    par(c, x2 + 14, yt - 44, 'La profe mostra una melodia uns segons i la tapa. Pots tocar-ne el principi de memòria?', 11.5, pw - 28, 14.5, SANS, INK)
    c.showPage()


# ======================================================================== TEMA 29 · L'acord de Do
def t29_teoria(c):
    pagina_tema(c, 29, 'L’acord de Do', 'Tres notes que sonen alhora fan un acord.', 'teoria', color=True)
    guia(c, M, Y(142), CW, 'Fins ara hem tocat notes d’una en una. Si en toquem tres alhora, fem un acord! El de DO té tres notes: '
         'DO, MI i SOL.', color=True, size=12.5, h=80)
    yt = Y(238)
    h = 224
    panell(c, M, yt, 300, h, 'AL TECLAT')
    teclat(c, M + 16, yt - h + 22, 268, 90, nb=5, resalta={0: 'DO', 2: 'MI', 4: 'SOL'}, noms='resalta', color=True, dits={0: 1, 2: 3, 4: 5})
    txt(c, M + 16, yt - 52, 'Saltem una tecla entre nota i nota:', 11.8, SANS, INK)
    txt(c, M + 16, yt - 70, 'DO  (RE)  MI  (FA)  SOL', 14, SERIFB, NAVY)
    xx = M + 318
    panell(c, xx, yt, CW - 318, h, 'AL PENTAGRAMA')
    sist(c, xx + 10, yt - 80, CW - 338, 8.4, '[C4+E4+G4]:w', 'treble', (4, 4), show_time=False)
    par(c, xx + 12, yt - 156, 'Les tres notes van una sobre l’altra: una a la ratlleta, una a la 1a línia i una a la 2a.', 11, CW - 342, 13.5, SANS, INK)
    yt = Y(478)
    h = 150
    panell(c, M, yt, CW, h, 'ELS DITS DE L’ACORD')
    par(c, M + 16, yt - 50, 'La mà dreta toca l’acord amb els dits 1, 3 i 5: el polze, el del mig i el petit. Els dits 2 i 4 es queden quiets, a la vora.', 12, CW - 32, 16, SANS, INK)
    teclat(c, M + 16, yt - h + 16, 220, 50, nb=5, resalta={0: 'DO', 2: 'MI', 4: 'SOL'}, noms='resalta', color=True, dits={0: 1, 2: 3, 4: 5})
    sist(c, M + 260, yt - 100, 220, 6.6, '[C4+E4+G4]:h [C4+E4+G4]:h', 'treble', (4, 4), show_time=False)
    franja(c, M, Y(644), CW, 44, 'RECORDA', 'Acord de DO = DO + MI + SOL, tocats alhora.', 12.5)
    franja(c, M, Y(702), CW, 62, 'ESCOLTO', 'Toca DO, MI i SOL un darrere l’altre i després els tres alhora: sents com se sumen en un sol so?', 12)
    c.showPage()


def t29_jocs(c):
    pagina_jocs(c, 29, 'L’acord de Do · a jugar!', 'Tres notes, un acord.',
                'Un acord és com un equip de tres amics que sonen junts. Anem a formar el de DO!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 160
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA L’ACORD', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta de vermell el DO, de groc el MI i de blau el SOL. Són les tres notes de l’acord de DO.', CW - 28)
    teclat(c, M + 14, yt - h + 14, 300, 66, nb=8)
    h = 188
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUINES NOTES FAN L’ACORD?', n=2)
    consigna(c, M + 14, yt - 40, 'Encercla les tres notes de l’acord de DO.', pw - 28)
    noms = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
    for k, nm in enumerate(noms):
        xx = M + 18 + (k % 4) * 54
        yy = yt - 84 - (k // 4) * 54
        rr(c, xx, yy - 18, 44, 36, 18, fill=white, lw=1.5, col=NAVY)
        txt(c, xx + 22, yy - 4, nm, 13, SERIFB, NAVY, 'c')
    panell(c, x2, yt, pw, h, 'DIBUIXA L’ACORD', n=3)
    consigna(c, x2 + 14, yt - 40, 'Escriu les tres notes de l’acord de DO amb una blanca cada una.', pw - 28)
    pauta(c, x2 + 14, yt - 100, pw - 28, 8, 'treble', final=True)
    h = 156
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['Un acord són tres notes alhora.', 'L’acord de DO porta SI.', 'Es toca amb els dits 1, 3 i 5.'], 11.8, 14)
    p_intrus(c, x2, yt, pw, h, 5, [['DO', 'MI', 'SOL', 'RE'], ['1', '3', '5', '2']], consigna_t='Encercla el que no és de l’acord de DO.')
    c.showPage()


# ======================================================================== TEMA 30 · Com estudio una cançó
def t30_teoria(c):
    pagina_tema(c, 30, 'Com estudio una cançó', 'Tres passos per aprendre qualsevol cançó sense angoixes.', 'teoria')
    guia(c, M, Y(142), CW, 'Una cançó es construeix com una escala: esglaó a esglaó! No cal fer-ho tot de cop. '
         'Mira el pla de tres passos.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 292
    panell(c, M, yt, CW, h, 'ELS TRES PASSOS')
    pas = [('1', 'MIRO I CANTO', 'Mira la partitura (ulls de mussol) i canta-la o pica’n el ritme.', 'ull'),
           ('2', 'TOCO CADA MÀ', 'Toca la mà dreta i després l’esquerra, a poc a poc i per frases curtes.', 'ma'),
           ('3', 'AJUNTO I POLEIXO', 'Toca amb les dues mans de principi a fi, cada cop una mica millor.', 'mans')]
    for k, (n, t, d, ic) in enumerate(pas):
        x = M + 14 + k * 168
        base = yt - h + 20
        top = base + 108 + k * 34
        rr(c, x, base, 160, 108 + k * 34, 8, fill=WARM, lw=1.6, col=NAVY)
        bola(c, x + 24, top - 24, n, 13)
        txt(c, x + 46, top - 29, t, 12, ETQ, NAVY)
        par(c, x + 12, top - 52, d, 11, 138, 13.5, SANS, INK)
        cx_ = x + 80
        cy_ = top + 26
        if ic == 'ull':
            icona_ull(c, cx_, cy_, 1.0)
        elif ic == 'ma':
            ma_real(c, cx_, cy_ - 14, 0.2, esq=False, dits=False, color=False)
        else:
            ma_real(c, cx_ - 22, cy_ - 14, 0.2, esq=True, dits=False, color=False)
            ma_real(c, cx_ + 22, cy_ - 14, 0.2, esq=False, dits=False, color=False)
    franja(c, M, Y(544), CW, 44, 'RECORDA', 'Poc a poc i bé val més que de pressa i malament.', 12.5)
    yt = Y(606)
    h = 170
    panell(c, M, yt, CW, h, 'TRUCS DEL MUSSOL')
    trucs = ['Pocs minuts, però tots els dies, són millor que molts minuts un sol dia.', 'Equivocar-se és normal: torna a començar el compàs.',
             'Toca sempre a poc a poc: la velocitat arriba sola.', 'Si et cansa, descansa i torna-hi.']
    yy = yt - 46
    for t in trucs:
        c.setFillColor(OCRE)
        c.circle(M + 22, yy + 4, 3.4, stroke=0, fill=1)
        yy = par(c, M + 34, yy, t, 12, CW - 54, 15, SANS, INK) - 6
    c.showPage()


def t30_jocs(c):
    pagina_jocs(c, 30, 'Com estudio · a jugar!', 'Tres passos, una cançó.',
                'Un pianista de veritat sap com estudiar. A veure si ho has entès!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'ORDENA ELS PASSOS', n=1)
    consigna(c, M + 14, yt - 40, 'Escriu 1, 2 o 3 a cada targeta per posar-los en ordre.', CW - 28)
    cart = ['Toco amb les dues mans de principi a fi.', 'Miro la partitura i la canto.', 'Toco la mà dreta i després l’esquerra.']
    for k, t in enumerate(cart):
        x = M + 14 + k * 164
        rr(c, x, yt - h + 22, 152, 100, 8, fill=WARM, lw=1.5, col=NAVY)
        par(c, x + 12, yt - 92, t, 11.5, 130, 14, SANS, INK)
        rr(c, x + 56, yt - h + 28, 40, 28, 14, fill=white, lw=1.6, col=NAVY)
    h = 170
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=2)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['Cal tocar de pressa des del primer dia.', 'Equivocar-se és normal.', 'És millor estudiar una mica cada dia.'], 11.8, 14)
    p_cruci(c, x2, yt, pw, h, 3, [('ESTUDIAR', 0, 0, 'h', 1), ('TOCO', 0, 2, 'v', 2), ('DOS', 0, 4, 'v', 3)], [('1 →', 'Aprendre una cançó.'), ('2 ↓', 'Jo … les tecles.'), ('3 ↓', 'Les mans són…')], 13)
    h = 160
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'EL MEU TRUC', n=4)
    consigna(c, M + 14, yt - 40, 'Acaba les frases amb les teves paraules.', CW - 28)
    for k, t in enumerate(['La cançó que vull aprendre és…', 'Una cosa que em surt bé és…', 'Una cosa que vull millorar és…']):
        yy = yt - 76 - k * 28
        txt(c, M + 16, yy, t, 12, SANSB, NAVY)
        linia(c, M + 16 + stringWidth(t, SANSB, 12) + 8, yy - 2, CW - 40 - stringWidth(t, SANSB, 12))
    c.showPage()
