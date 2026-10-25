# -*- coding: utf-8 -*-
"""Pàgines extra de pràctica i repassos de capítol del Quadern PEKES."""
from nens_annex import *                                          # noqa: F401,F403
from nens_t01 import pagina_jocs
from nens_tclas import pagina, pauta, gran_pauta, cap
import nens_pla as pla
import notation as nt
from nens_dib import ma_real, punts_dits, tortuga, coet, petjades
from nens_t07 import notes_linia, dinamica, regulador, arc_frase
from nens_t05 import silenci, nota_plica
from nens_t06 import gran_sist, mans_sobre_tecles, icona_ull


# ------------------------------------------------------------------ capçaleres
def cap_extra(c, key, titol, intro, desplaça=0, guia_txt=None):
    e = pla.EXTRA[key]
    pagina(c, pla.kicker_cap(e['cap']), titol, 'Pràctica', intro, e['pag'] + desplaça, False)
    if guia_txt:
        guia(c, M, Y(122), CW, guia_txt, color=False, size=12.5, h=66)


def cap_repas(c, cap_, intro, guia_txt):
    r = pla.REPAS[cap_]
    pagina(c, pla.kicker_cap(cap_), 'Repàs del capítol %d' % cap_, 'Repàs', intro, r['pag'], False)
    guia(c, M, Y(122), CW, guia_txt, color=False, size=12.5, h=66)


def medalla(c, cx, cy, r, n):
    """Medalla per pintar: cinta + cercle amb el número del capítol."""
    c.setFillColor(white)
    trac(c, 1.8, NAVY)
    for sg in (-1, 1):
        c.poly([(cx + sg * 4, cy + r * 0.6), (cx + sg * (r * 0.95), cy + r * 1.7), (cx + sg * (r * 0.95 - r * 0.6), cy + r * 1.95),
                (cx + sg * 0, cy + r * 1.0)], 1, 1)
    c.circle(cx, cy, r, stroke=1, fill=1)
    trac(c, 1.2, NAVY, (2, 2))
    c.circle(cx, cy, r * 0.76, stroke=1, fill=0)
    c.setDash()
    for k in range(5):
        a = math.radians(90 + k * 72)
        pass
    txt(c, cx, cy - r * 0.34, str(n), r * 1.05, SERIFB, NAVY, 'c')


def p_vf(c, x, yt, w, h, n, frases, titol='VERITAT O FALS?'):
    panell(c, x, yt, w, h, titol, n=n)
    capcalera_vf(c, x + 14, yt - 34, w - 14)
    veritat_fals(c, x + 14, yt - 50, w - 14, frases, 11.8, 14)


def p_uneix(c, x, yt, w, h, n, titol, consigna_t, esq, dre, fila=40, ampl_esq=84):
    panell(c, x, yt, w, h, titol, n=n)
    consigna(c, x + 14, yt - 40, consigna_t, w - 28)
    uneix(c, x + 14, yt - 82, w - 28, esq, dre, fila=fila, ampl_esq=ampl_esq, ampl_dre=w - 28 - ampl_esq - 36, fs=11.5, serif=False)


def p_crucigrama(c, x, yt, w, h, n, spec, pistes_l, cs=19, titol='CRUCIGRAMA'):
    panell(c, x, yt, w, h, titol, n=n)
    consigna(c, x + 14, yt - 40, 'Una lletra a cada quadret.', w - 28)
    cel = crucigrama(c, x + 12, yt - 54, spec, cs)
    ncol = max(k for (_, k) in cel) + 1
    pistes(c, x + 12 + ncol * cs + 12, yt - 70, w - (ncol * cs + 36), pistes_l, 11, 13.5)


def p_noms(c, x, yt, w, h, n, pitches, clau='treble', titol='ESCRIU EL NOM', consigna_t='Escriu el nom de cada nota.'):
    panell(c, x, yt, w, h, titol, n=n)
    consigna(c, x + 14, yt - 40, consigna_t, w - 28)
    g = 6.2
    per = 4 if w > 300 else 3
    cw_ = (w - 28) / per
    for k, p_ in enumerate(pitches):
        col, fila = k % per, k // per
        xx = x + 14 + col * cw_
        yy = yt - 84 - fila * 50
        yb = pauta(c, xx, yy, cw_ - 6, g, clau, final=False)
        cap(c, xx + cw_ - 24, nt.note_y(yb, g, p_, clau), g, 'w', white)
        if p_ == 'C4':
            trac(c, 1.0, NAVY)
            cy_ = nt.note_y(yb, g, p_, clau)
            c.line(xx + cw_ - 24 - g * 1.3, cy_, xx + cw_ - 24 + g * 1.3, cy_)
        linia(c, xx + 12, yb - 12, cw_ - 40)


def p_medalla(c, x, yt, w, h, cap_):
    panell(c, x, yt, w, h, 'LA TEVA MEDALLA')
    medalla(c, x + w / 2, yt - h / 2 - 6, 26, cap_)
    txt(c, x + w / 2, yt - h + 14, 'Has acabat el capítol! Pinta la medalla.', 10.5, SANSB, NAVY, 'c')


# ======================================================================== EXTRA · Gimnàstica de dits
def x_dits(c):
    cap_extra(c, 'dits', 'Gimnàstica de dits', 'Abans de tocar, els dits s’escalfen com els futbolistes.', 0,
              'Escalfem les mans! Fes aquests sis jocs sobre la taula, sense piano. Quan en facis un, marca la casella.')
    exs = [('1 · ELS DITS CAMINEN', 'Aixeca i baixa cada dit, un darrere l’altre: 1-2-3-4-5 i després 5-4-3-2-1.', {}),
           ('2 · EL POLZE I EL PETIT', 'Toca la taula amb el polze (1) i el petit (5) alhora. Després, un i un altre: 1-5-1-5.', {1: '#D9C79C', 5: '#D9C79C'}),
           ('3 · LES PARELLES', 'Aixeca només l’índex (2) i el del mig (3). Fes-los saltar junts, com dos conillets.', {2: '#D9C79C', 3: '#D9C79C'}),
           ('4 · LA PILOTA', 'Tanca la mà com si agafessis una pilota i obre-la ben a poc a poc. Repeteix-ho cinc cops.', {}),
           ('5 · DE DOS EN DOS', 'Toca 1-3-5 i després 5-3-1, amb força suau. Fixa’t que els dits 2 i 4 es queden quiets.', {1: '#D9C79C', 3: '#D9C79C', 5: '#D9C79C'}),
           ('6 · LA PLUJA SUAU', 'Fes caure els cinc dits sobre la taula com la pluja: primer a poc a poc i després més de pressa.', {})]
    cw = (CW - 14) / 2.0
    for k, (t, d, mc) in enumerate(exs):
        col, fila = k % 2, k // 2
        x = M + col * (cw + 14)
        yt = Y(204) - fila * 190
        h = 172
        panell(c, x, yt, cw, h, t)
        ma_real(c, x + 66, yt - 112, 0.46, esq=False, dits=True, color=False, marca=mc)
        par(c, x + 132, yt - 50, d, 11.5, cw - 146, 14.5, SANS, INK)
        rr(c, x + cw - 40, yt - h + 12, 22, 22, 4, fill=white, lw=1.5, col=NAVY)
        txt(c, x + cw - 48, yt - h + 18, 'fet', 10.5, SANSB, MUTED, 'r')
    c.showPage()


# ======================================================================== EXTRA · Llegim notes (2 pàgines)
def x_llegim(c):
    cap_extra(c, 'llegim', 'Llegim notes (1): clau de sol', 'Practica llegint les notes de la mà dreta, de fàcil a més difícil.', 0,
              'Per llegir bé no cal saber-ho tot: busca una nota que coneguis i compta des d’allà! El SOL és a la 2a línia.')
    yt = Y(204)
    panell(c, M, yt, CW, 118, 'TRUCS PER LLEGIR')
    tr = [('El SOL', 'viu a la 2a línia: la de la clau!'), ('El DO', 'dins del pentagrama no hi viu: té ratlleta a sota.'), ('Les altres', 'es compten de línia a espai: DO RE MI FA SOL…')]
    for k, (a, b) in enumerate(tr):
        xx = M + 14 + k * 164
        rr(c, xx, yt - 108, 154, 66, 8, fill=WARM, lw=1.4, col=OCRE)
        txt(c, xx + 10, yt - 62, a, 13, SERIFB, NAVY)
        par(c, xx + 10, yt - 78, b, 10.8, 134, 13, SANS, INK)
    ex = [['C4', 'D4', 'E4', 'D4', 'C4'], ['E4', 'F4', 'G4', 'F4', 'E4'], ['G4', 'A4', 'B4', 'A4', 'G4'],
          ['C4', 'E4', 'G4', 'E4', 'C4'], ['G4', 'F4', 'E4', 'D4', 'C4'], ['D4', 'F4', 'A4', 'F4', 'D4'], ['E4', 'G4', 'B4', 'G4', 'E4']]
    yt = Y(342)
    panell(c, M, yt, CW, 440, 'LLEGEIX, DIGUES ELS NOMS I TOCA', n=None) if False else panell(c, M, yt, CW, 440, 'LLEGEIX, DIGUES ELS NOMS I TOCA')
    for k, ps in enumerate(ex):
        yy = yt - 62 - k * 56
        txt(c, M + 16, yy - 12, str(k + 1), 14, SANSB, OCRE)
        yb, _ = notes_linia(c, M + 38, yy, CW - 110, 7, ps, None, 'treble', dx0=52)
        rr(c, M + CW - 56, yy - 28, 22, 22, 4, fill=white, lw=1.5, col=NAVY)
    c.showPage()
    cap_extra(c, 'llegim', 'Llegim notes (2): clau de fa', 'Ara la mà esquerra, que llegeix a la clau de fa.', 1,
              'El FA viu a la 4a línia: a la clau de fa hi ha dos puntets al seu voltant. Busca’l primer!')
    yt = Y(204)
    panell(c, M, yt, CW, 118, 'TRUCS PER LLEGIR')
    tr = [('El FA', 'viu a la 4a línia, entre els dos puntets.'), ('El DO central', 'és a sobre del pentagrama, amb ratlleta.'), ('Les altres', 'es compten pujant: SOL LA SI DO…')]
    for k, (a, b) in enumerate(tr):
        xx = M + 14 + k * 164
        rr(c, xx, yt - 108, 154, 66, 8, fill=WARM, lw=1.4, col=OCRE)
        txt(c, xx + 10, yt - 62, a, 13, SERIFB, NAVY)
        par(c, xx + 10, yt - 78, b, 10.8, 134, 13, SANS, INK)
    ex = [['C3', 'D3', 'E3', 'D3', 'C3'], ['E3', 'F3', 'G3', 'F3', 'E3'], ['G3', 'F3', 'E3', 'D3', 'C3'],
          ['C3', 'E3', 'G3', 'E3', 'C3'], ['A2', 'B2', 'C3', 'B2', 'A2'], ['G2', 'A2', 'B2', 'C3', 'D3'], ['D3', 'F3', 'A3', 'F3', 'D3']]
    yt = Y(342)
    panell(c, M, yt, CW, 440, 'LLEGEIX, DIGUES ELS NOMS I TOCA')
    for k, ps in enumerate(ex):
        yy = yt - 62 - k * 56
        txt(c, M + 16, yy - 12, str(k + 1), 14, SANSB, OCRE)
        notes_linia(c, M + 38, yy, CW - 110, 7, ps, None, 'bass', dx0=52)
        rr(c, M + CW - 56, yy - 28, 22, 22, 4, fill=white, lw=1.5, col=NAVY)
    c.showPage()


# ======================================================================== EXTRA · Les notes amb lletres
LLETRA = {'DO': 'C', 'RE': 'D', 'MI': 'E', 'FA': 'F', 'SOL': 'G', 'LA': 'A', 'SI': 'B'}


def x_lletres(c):
    cap_extra(c, 'lletres', 'Les notes amb lletres', 'En molts països les notes no es diuen DO, RE, MI: es diuen amb lletres.', 0,
              'A Anglaterra i a Alemanya les notes són lletres de l’abecedari! Així podem escriure paraules amb notes. Mira com!')
    yt = Y(204)
    panell(c, M, yt, CW, 170, 'LA TAULA DE LES LLETRES')
    kw = (CW - 28) / 7.0
    for k, nm in enumerate(NOTES7):
        x = M + 14 + k * kw
        rr(c, x + 2, yt - 112, kw - 4, 54, 8, fill=HexColor(COL[nm]), lw=1.6, col=NAVY)
        txt(c, x + kw / 2, yt - 80, nm, 14, SERIFB, INK if nm == 'MI' else white, 'c')
        rr(c, x + 2, yt - 160, kw - 4, 40, 8, fill=white, lw=1.6, col=NAVY)
        txt(c, x + kw / 2, yt - 148, LLETRA[nm], 24, SERIFB, NAVY, 'c')
    yt = Y(392)
    panell(c, M, yt, CW, 400, 'MISSATGES SECRETS')
    consigna(c, M + 14, yt - 40, 'Escriu la lletra de cada nota i descobriràs la paraula. Les lletres són: C D E F G A B.', CW - 28)
    mots = [(['E4', 'D4', 'A4', 'D4'], 'DEAD?', False), (['C4', 'A4', 'F4', 'E4'], 'CAFE', True), (['F4', 'A4', 'C4', 'E4'], 'FACE', True),
            (['B4', 'E4', 'A4', 'D4'], 'BEAD', True)]
    mots = [(['C4', 'A4', 'F4', 'E4'], 'CAFE'), (['F4', 'A4', 'C4', 'E4'], 'FACE'), (['B4', 'E4', 'A4', 'D4'], 'BEAD'), (['D4', 'A4', 'D4'], 'DAD')]
    g = 7
    for k, (ps, w_) in enumerate(mots):
        yy = yt - 88 - k * 70
        txt(c, M + 16, yy - 6, str(k + 1), 14, SANSB, OCRE)
        yb = pauta(c, M + 36, yy, 270, g, 'treble', final=False)
        for j, p_ in enumerate(ps):
            xx = M + 100 + j * 52
            cy_ = nt.note_y(yb, g, p_)
            cap(c, xx, cy_, g, 'w', white)
            if p_ == 'C4':
                trac(c, 1.0, NAVY)
                c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
            quadres(c, xx - 11, yb - 14, 1, 22, 0)
        txt(c, M + 340, yy - 18, '→  la paraula és:', 11.5, SANS, INK)
        linia(c, M + 438, yy - 20, 60)
    txt(c, M + 16, yt - 376, 'Els noms són d’origen anglès: CAFE = cafè, FACE = cara, BEAD = comptes d’un collaret, DAD = pare.', 10.8, SANS, MUTED)
    c.showPage()


# ======================================================================== EXTRA · Piquem ritmes (2 pàgines)
def fila_ritme(c, x, yt, w, text, sil=None, gap=6.4):
    sist(c, x, yt, w, gap, text, 'treble', (4, 4), show_clef=False, show_time=False)


def x_ritmes(c):
    cap_extra(c, 'ritmes', 'Piquem ritmes (1)', 'Cada figura té el seu nom: ta, ti-ti, ta-a… Pica de mans mentre ho dius!', 0,
              'Tots els ritmes es poden picar de mans! Mira com es diuen les figures i després llegeix cada línia.')
    yt = Y(204)
    panell(c, M, yt, CW, 126, 'COM ES DIUEN')
    cw = (CW - 28) / 5.0
    for k, (t, nom, sil) in enumerate((('q', 'negra', 'ta'), ('ee', 'dues corxeres', 'ti-ti'), ('h', 'blanca', 'ta-a'), ('w', 'rodona', 'ta-a-a-a'), ('r', 'silenci', 'shh'))):
        x = M + 14 + k * cw
        rr(c, x + 2, yt - 112, cw - 6, 84, 8, fill=WARM, lw=1.4, col=NAVY)
        if t == 'r':
            g = 5
            ytop = yt - 58
            yb = pauta(c, x + 10, ytop, cw - 26, g, None, final=False)
            nt.draw_rest(c, x + cw / 2 - 2, yb, ytop, g, 'q')
        else:
            figura(c, t, x + cw / 2 - 2 - (8 if t == 'ee' else 0), yt - 66 if t != 'w' else yt - 60, 6 if t != 'w' else 8)
        txt(c, x + cw / 2 - 2, yt - 98, sil, 14, SERIFB, NAVY, 'c')
        txt(c, x + cw / 2 - 2, yt - 118 + 4, nom, 9.8, SANS, MUTED, 'c') if False else None
    rit = ['q q q q', 'q q h', 'h h', 'e e q q q', 'q q R:q q', 'h q q', 'e e e e h', 'q R:q q q', 'e e q e e q', 'w']
    yt = Y(344)
    panell(c, M, yt, CW, 434, 'LLEGEIX I PICA')
    for k in range(8):
        pass
    textos = ['C4:q C4:q C4:q C4:q', 'C4:q C4:q C4:h', 'C4:h C4:h', 'C4:e C4:e C4:q C4:q C4:q', 'C4:q C4:q R:q C4:q',
              'C4:h C4:q C4:q', 'C4:e C4:e C4:e C4:e C4:h', 'C4:q R:q C4:q C4:q']
    sils = ['ta ta ta ta', 'ta ta ta-a', 'ta-a ta-a', 'ti-ti ta ta', 'ta ta shh ta', 'ta-a ta ta', 'ti-ti ti-ti ta-a', 'ta shh ta ta']
    for k, (t, s_) in enumerate(zip(textos, sils)):
        yy = yt - 68 - k * 49
        txt(c, M + 16, yy - 12, str(k + 1), 13, SANSB, OCRE)
        sist(c, M + 36, yy, 330, 6.2, t.replace('C4', 'B4'), 'treble', (4, 4), show_clef=False)
        if k < 4:
            txt(c, M + 384, yy - 16, s_, 12, SERIFB, NAVY)
        else:
            linia(c, M + 384, yy - 16, 110)
            txt(c, M + 384, yy - 6, 'escriu-ho:', 8.5, SANS, MUTED)
    c.showPage()
    cap_extra(c, 'ritmes', 'Piquem ritmes (2)', 'Els ritmes també s’amaguen dins de les paraules!', 1,
              'Les paraules tenen ritme! Cada síl·laba és un cop. Digues cada paraula picant les síl·labes.')
    yt = Y(204)
    panell(c, M, yt, CW, 246, 'PARAULES AMB RITME')
    pals = [('pa', 'q', 'ta'), ('poma', 'ee', 'ti-ti'), ('taronja', 'q ee', 'ta ti-ti'), ('xocolata', 'ee ee', 'ti-ti ti-ti'), ('gelat', 'ee', 'ti-ti'), ('mussol', 'ee', 'ti-ti')]
    cw = (CW - 28) / 3.0
    for k, (p_, f_, s_) in enumerate(pals):
        col, fila = k % 3, k // 3
        x = M + 14 + col * cw
        y0 = yt - 56 - fila * 84
        rr(c, x + 2, y0 - 70, cw - 8, 74, 8, fill=WARM, lw=1.4, col=NAVY)
        txt(c, x + cw / 2 - 2, y0 - 16, p_, 14, SANSB, NAVY, 'c')
        xs0 = x + cw / 2 - 2
        parts = f_.split()
        if len(parts) == 1:
            figura(c, parts[0], xs0 - (10 if parts[0] == 'ee' else 0), y0 - 50, 5.6)
        else:
            figura(c, parts[0], xs0 - 24, y0 - 50, 5.6)
            figura(c, parts[1], xs0 + 4, y0 - 50, 5.6)
        txt(c, xs0, y0 - 66, s_, 10.5, SERIFB, OCRE, 'c') if False else None
    txt(c, M + 14, yt - 222, 'Una síl·laba sola és una negra (ta). Dues síl·labes ràpides seguides són dues corxeres (ti-ti).', 10.8, SANS, MUTED)
    yt = Y(466)
    panell(c, M, yt, CW, 314, 'EL RITME DEL TEU NOM')
    consigna(c, M + 14, yt - 40, 'Escriu el teu nom i les síl·labes, i dibuixa la figura que correspon a cada una (negra o dues corxeres).', CW - 28)
    for k, t in enumerate(['el meu nom', 'el nom d’algú de casa', 'el meu animal preferit', 'el meu menjar preferit']):
        yy = yt - 100 - k * 56
        txt(c, M + 16, yy, t, 11.5, SANSB, NAVY)
        linia(c, M + 16, yy - 6, 190)
        rr(c, M + 230, yy - 24, CW - 250, 40, 6, fill=white, lw=1.3, col=MUTED, dash=(3, 3))
    c.showPage()


# ======================================================================== EXTRA · Més cançons
JB = 'E4 E4 E4:h | E4 E4 E4:h | E4 G4 C4:q. D4:e | E4:w'


def x_mescancons(c):
    cap_extra(c, 'mescancons', 'Més cançons', 'Una cançó de Nadal i les cançons de sempre amb una mà dreta i una d’esquerra.', 0,
              'Quantes cançons ja saps tocar! Aquí en tens una de nova, i una altra amb les dues mans. Toca-les a poc a poc.')
    yt = Y(204)
    h = 238
    panell(c, M, yt, CW, h, 'JINGLE BELLS (EL REFRÀ)')
    txt(c, M + 16, yt - 42, 'Cançó de Nadal · mà dreta, posició de Do', 11, SANS, MUTED)
    sist(c, M + 16, yt - 82, CW - 32, 9.6, JB, 'treble', (4, 4))
    for k, t in enumerate(['Els tres primers compassos són fàcils: E E E, E E E…', 'El compàs 3 té una negra amb puntet i una corxera: «ta-a ti».',
                           'Canta-la mentre la toques: «Jin-gle bells, jin-gle bells…»']):
        c.setFillColor(OCRE)
        c.circle(M + 22, yt - 138 - k * 22 + 4, 3.2, stroke=0, fill=1)
        par(c, M + 32, yt - 138 - k * 22, t, 11.2, CW - 50, 13.5, SANS, INK)
    yt = Y(458)
    h = 322
    panell(c, M, yt, CW, h, 'HOT CROSS BUNS A DUES MANS')
    txt(c, M + 16, yt - 42, 'La dreta fa la cançó i l’esquerra aguanta el DO.', 11, SANS, MUTED)
    gran_sist(c, M + 30, yt - 78, CW - 56, 7.6, 'E4 D4 C4:h | E4 D4 C4:h | C4:e C4:e C4:e C4:e D4:e D4:e D4:e D4:e | E4 D4 C4:h',
              'C3:w | C3:w | C3:w | C3:w')
    for k, t in enumerate(['Primer la mà dreta sola, després l’esquerra i, al final, les dues juntes.', 'L’esquerra només ha de tocar una nota per compàs: pensa en el pols!']):
        c.setFillColor(OCRE)
        c.circle(M + 22, yt - 218 - k * 22 + 4, 3.2, stroke=0, fill=1)
        par(c, M + 32, yt - 218 - k * 22, t, 11.2, CW - 50, 13.5, SANS, INK)
    c.showPage()


# ======================================================================== EXTRA · Exercicis per a les mans (2 pàgines)
def x_exmans(c):
    cap_extra(c, 'exmans', 'Exercicis per a les mans (1)', 'Cada exercici va una mica més lluny: tria el ritme que et va bé!', 0,
              'Els pianistes fan exercicis cada dia. Són curts i ens fan tenir les mans àgils! Fes-los sempre a poc a poc.')
    ex = [('1 · PUJEM I BAIXEM', 'C4 D4 E4 F4 | G4 F4 E4 D4 | C4:w', 'treble', 'Mà dreta. Una nota cada dit.'),
          ('2 · DE DOS EN DOS', 'C4 E4 G4 E4 | C4 E4 G4 E4 | C4:w', 'treble', 'Mà dreta. Salta una tecla cada cop.'),
          ('3 · ELS GRUPS', 'C4 C4 D4 D4 | E4 E4 F4 F4 | G4:h G4:h', 'treble', 'Mà dreta. Cada nota, dues vegades.'),
          ('4 · LA GRAVE', 'C3 D3 E3 F3 | G3 F3 E3 D3 | C3:w', 'bass', 'Mà esquerra. Del dit petit al polze.'),
          ('5 · EL SALT', 'G3 E3 C3 E3 | G3 E3 C3:h | C3:w', 'bass', 'Mà esquerra. Baixa i puja de dos en dos.')]
    yt = Y(204)
    for k, (t, m_, cl, d) in enumerate(ex):
        yy = yt - k * 116
        panell(c, M, yy, CW, 104, t)
        txt(c, M + 16, yy - 40, d, 11, SANS, MUTED)
        sist(c, M + 16, yy - 52, CW - 70, 5.8, m_, cl, (4, 4))
        rr(c, M + CW - 40, yy - 70, 22, 22, 4, fill=white, lw=1.4, col=NAVY)
    c.showPage()
    cap_extra(c, 'exmans', 'Exercicis per a les mans (2)', 'Ara les dues mans juntes: una canta i l’altra acompanya.', 1,
              'Quan toquem amb dues mans, cada una té la seva feina. Fixa’t bé què fa cada pentagrama!')
    ex = [('6 · MANS IGUALS', 'C4 D4 E4 F4 | G4:w', 'C3 D3 E3 F3 | G3:w', 'Les dues mans fan el mateix, una octava de diferència.'),
          ('7 · MANS CONTRÀRIES', 'C4 D4 E4 F4 | G4:w', 'G3 F3 E3 D3 | C3:w', 'Una puja i l’altra baixa. Com un mirall!'),
          ('8 · AMB ACORD', 'E4 D4 C4 D4 | E4:h E4:h', '[C3+E3+G3]:w | [C3+E3+G3]:w', 'La dreta fa la melodia i l’esquerra l’acord de DO.')]
    yt = Y(204)
    for k, (t, rh, lh, d) in enumerate(ex):
        yy = yt - k * 192
        panell(c, M, yy, CW, 178, t)
        txt(c, M + 16, yy - 40, d, 11, SANS, MUTED)
        gran_sist(c, M + 34, yy - 62, CW - 90, 6.4, rh, lh)
        rr(c, M + CW - 40, yy - 160, 22, 22, 4, fill=white, lw=1.4, col=NAVY)
    c.showPage()


# ======================================================================== EXTRA · Una peça amb tot
def x_peca(c):
    cap_extra(c, 'peca', 'Una peça amb tot', 'Una cançoneta nova amb tots els senyals que has après.', 0,
              'Aquesta peça és meva! Porta repetició, frases, volum, lligats, picats i un calderó. Troba tots els senyals.')
    yt = Y(204)
    h = 300
    panell(c, M, yt, CW, h, 'EL MUSSOL I LA LLUNA')
    g = 8.4
    ytop = yt - 80
    yb, xs = notes_linia(c, M + 14, ytop, CW - 28, g, ['C4', 'D4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4'], ['q', 'q', 'q', 'q', 'h', 'h', 'q', 'q'], 'treble',
                         staccato=[6, 7], dx0=56)
    arc_frase(c, xs[0][0], xs[3][0], ytop + 8, True, 16)
    dinamica(c, xs[0][0], yb - 28, 'p', 20)
    regulador(c, xs[1][0] + 8, xs[3][0] + 4, yb - 24, True, 12)
    dinamica(c, xs[4][0], yb - 28, 'mf', 20)
    yb2, xs2 = notes_linia(c, M + 14, ytop - 100, CW - 28, g, ['D4', 'C4', 'D4', 'E4', 'D4', 'C4', 'C4'], ['q', 'q', 'q', 'q', 'q', 'q', 'h'], 'treble', dx0=56)
    arc_frase(c, xs2[0][0], xs2[3][0], ytop - 100 + 8, True, 16)
    dinamica(c, xs2[0][0], yb2 - 28, 'f', 20)
    regulador(c, xs2[4][0] - 8, xs2[5][0] + 8, yb2 - 24, False, 12)
    dinamica(c, xs2[6][0], yb2 - 28, 'p', 20)
    nt.draw_repeticion(c, M + 14 + CW - 28 - 2, yb2 + 4 * g, yb2, g, abre=False)
    # calderó
    cx_, cy_ = xs2[6][0], nt.note_y(yb2, g, 'C4')
    trac(c, 2, NAVY)
    pth = c.beginPath()
    pth.moveTo(cx_ - 8, ytop - 100 + 16)
    pth.curveTo(cx_ - 7, ytop - 100 + 28, cx_ + 7, ytop - 100 + 28, cx_ + 8, ytop - 100 + 16)
    c.drawPath(pth, stroke=1, fill=0)
    c.setFillColor(NAVY)
    c.circle(cx_, ytop - 100 + 18, 1.8, stroke=0, fill=1)
    par(c, M + 14, yt - h + 36, 'Toca-la a poc a poc. Primer mira tots els senyals, després toca-la i, al final, afegeix el volum!', 11.5, CW - 28, 14.5, SANS, INK)
    yt = Y(520)
    h = 258
    panell(c, M, yt, CW, h, 'ELS SENYALS DE LA PEÇA')
    sig = [('arc sobre les notes', 'frase (lligat)'), ('p · mf · f', 'volum'), ('<  >', 'cada cop més fort · cada cop més suau'),
           ('puntets', 'notes picades'), ('𝄐', 'calderó'), ('cap', 'cap')]
    sig = [('arc sobre les notes', 'una frase, tocada lligada'), ('p, mf, f', 'suau, una mica fort, fort'), ('< i >', 'cada cop més fort · cada cop més suau'),
           ('puntets sota les notes', 'notes curtes: picades'), ('la barra amb dos punts', 'repetició: torna al principi'), ('el signe sobre l’última nota', 'calderó: queda’t una mica més')]
    for k, (a, b) in enumerate(sig):
        yy = yt - 52 - k * 38
        rr(c, M + 14, yy - 14, 170, 30, 15, fill=WARM, lw=1.4, col=OCRE)
        txt(c, M + 99, yy - 5, a, 10.2, SANSB, NAVY, 'c')
        txt(c, M + 196, yy - 5, '→', 14, SANSB, OCRE)
        txt(c, M + 220, yy - 5, b, 11.5, SANS, INK)
    c.showPage()


# ======================================================================== REPASSOS
def repas1(c):
    cap_repas(c, 1, 'Piano, mans, greus i aguts, i el teclat: ho recordes tot?', 'Has acabat el primer capítol! Mira què en recordes: aquí tens un repàs ben divertit amb els jocs que més t’han agradat.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 250
    yt = pila.pren(h)
    spec = [('TECLA', 0, 2, 'v', 1), ('PIANO', 4, 0, 'h', 2), ('PEDAL', 4, 0, 'v', 3), ('OS', 4, 4, 'v', 4)]
    p_crucigrama(c, M, yt, pw, h, 1, spec, [('1 ↓', 'Es prem amb el dit.'), ('2 →', 'L’instrument que toquem.'), ('3 ↓', 'Es prem amb el peu.'), ('4 ↓', 'Fa sons greus.')], cs=18)
    p_uneix(c, x2, yt, pw, h, 2, 'UNEIX AMB UNA LÍNIA', 'Cada cosa amb el que fa.', ['tecla', 'pedal', 'atril'], ['es prem amb el peu', 'porta la partitura', 'es toca amb el dit'], fila=56, ampl_esq=70)
    h = 146
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'EL TECLAT', n=3)
    consigna(c, M + 14, yt - 40, 'Pinta de vermell tots els DO i encercla el DO central.', CW - 28)
    teclat(c, M + 14, yt - h + 14, CW - 28, 60, nb=22)
    h = 136
    yt = pila.pren(h)
    p_vf(c, M, yt, pw, h, 4, ['Els sons greus són a la dreta.', 'Les tecles negres van de 2 en 2 i de 3 en 3.'])
    p_medalla(c, x2, yt, pw, h, 1)
    c.showPage()


def repas2(c):
    cap_repas(c, 2, 'Línies, espais, claus i el DO central.', 'Ja saps llegir el pentagrama! Aquest repàs et fa recordar les línies, els espais i les dues claus.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 172
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'PINTA LES LÍNIES I ELS ESPAIS', n=1)
    consigna(c, M + 14, yt - 40, 'Línies de blau, espais de groc.', pw - 28)
    for k in range(4):
        pass
    g = 14
    yb = pauta(c, M + 14, yt - 70, pw - 28, g, None, final=False)
    for k in range(5):
        _bolet(c, M + 14 + 12, yb + k * g, '%da' % (k + 1), OCRE, 24) if False else None
    p_vf(c, x2, yt, pw, h, 2, ['El pentagrama té 5 línies i 4 espais.', 'Les línies es compten de dalt cap a baix.', 'La clau de fa és per a la mà esquerra.'])
    h = 172
    yt = pila.pren(h)
    p_noms(c, M, yt, CW, h, 3, ['C4', 'E4', 'G4', 'F4', 'D4', 'A4', 'B4', 'C4'], 'treble', 'ESCRIU EL NOM', 'Escriu el nom de cada nota de la clau de sol.')
    h = 172
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'LES DUES CLAUS', n=4)
    consigna(c, M + 14, yt - 40, 'Quina és quina? Escriu SOL o FA.', pw - 28)
    for k, cl in enumerate(('treble', 'bass')):
        yb = pauta(c, M + 14, yt - 80 - k * 50, 120, 6.4, cl, final=False)
        quadres(c, M + 150, yb - 6, 1, 26, 0)
        linia(c, M + 188, yb - 6, 40)
    panell(c, x2, yt, pw, h, 'EL DO CENTRAL', n=5)
    consigna(c, x2 + 14, yt - 40, 'Dibuixa el DO central entre els dos pentagrames.', pw - 28)
    gran_pauta(c, x2 + 34, yt - 62, pw - 52, 8.5)
    c.showPage()


def repas3(c):
    cap_repas(c, 3, 'Les set notes, els colors, l’octava i la melodia.', 'Aquest és el capítol més gran! Ara que ja coneixes les set notes, repassem-les amb colors i dibuixos.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 140
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PINTA EL TECLAT', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta cada tecla del color de la seva nota: DO vermell, RE taronja, MI groc, FA verd, SOL blau, LA lila, SI gris.', CW - 28)
    teclat(c, M + 14, yt - h + 12, CW - 28, 44, nb=14, noms='totes')
    h = 202
    yt = pila.pren(h)
    p_noms(c, M, yt, pw, h, 2, ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'][:6], 'treble', 'ESCRIU EL NOM', 'Quina nota és?')
    panell(c, x2, yt, pw, h, 'PUJA O BAIXA?', n=3)
    consigna(c, x2 + 14, yt - 40, 'Mira cada parella i posa una fletxa.', pw - 28)
    for k, (a, b) in enumerate((('C4', 'G4'), ('A4', 'E4'), ('D4', 'D4'))):
        yy = yt - 84 - k * 36
        yb = pauta(c, x2 + 14, yy, 110, 5.2, 'treble', final=False)
        for j, p_ in enumerate((a, b)):
            xx = x2 + 70 + j * 24
            cy_ = nt.note_y(yb, 5.2, p_)
            cap(c, xx, cy_, 5.2, 'w', white)
            if p_ == 'C4':
                trac(c, 1.0, NAVY)
                c.line(xx - 7, cy_, xx + 7, cy_)
        rr(c, x2 + pw - 76, yy - 20, 54, 24, 12, fill=white, lw=1.5, col=NAVY)
    h = 190
    yt = pila.pren(h)
    spec = [('MISOL', 0, 0, 'h', 1)]
    panell(c, M, yt, pw, h, 'QUANTES NOTES?', n=4)
    consigna(c, M + 14, yt - 40, 'Respon amb un número.', pw - 28)
    for k, q in enumerate(['Notes amb nom diferent:', 'Notes d’una octava (DO a DO):', 'Colors que té l’arc de Sant Martí de les notes:']):
        yy = yt - 80 - k * 42
        par(c, M + 14, yy, q, 11.5, pw - 84, 14, SANS, INK)
        rr(c, M + pw - 56, yy - 14, 40, 26, 6, fill=white, lw=1.6, col=NAVY)
    p_medalla(c, x2, yt, pw, h, 3)
    c.showPage()


def repas4(c):
    cap_repas(c, 4, 'Pols, figures, compàs, puntet i lligadura.', 'Ets ja un mestre del ritme! Repassem els temps de cada figura, els compassos i els trucs d’allargar notes.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'QUANTS TEMPS?', n=1)
    consigna(c, M + 14, yt - 40, 'Escriu els temps de cada compàs. Han de ser 4!', CW - 28)
    for k, t in enumerate(['C4:h C4:q C4:q', 'C4:q. C4:e C4:h', 'C4:e C4:e C4:q C4:h', 'C4:h~ C4:h']):
        col, fila = k % 2, k // 2
        xx = M + 14 + col * 246
        yy = yt - 84 - fila * 52
        sist(c, xx, yy, 190, 5.6, t.replace('C4', 'B4'), 'treble', (4, 4), show_clef=False, show_time=False)
        rr(c, xx + 202, yy - 22, 30, 24, 5, fill=white, lw=1.5, col=NAVY)
    h = 190
    yt = pila.pren(h)
    p_uneix(c, M, yt, pw, h, 2, 'UNEIX AMB UNA LÍNIA', 'Cada compàs amb el seu nom.', ['4/4', '3/4', '2/4'], ['el vals', 'la marxa', 'quatre quarts'], fila=44, ampl_esq=60)
    p_vf(c, x2, yt, pw, h, 3, ['El pols va igual tota la cançó.', 'La corxera dura 2 temps.', 'El puntet afegeix la meitat.'])
    h = 150
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'PICA I DIGUES', n=4)
    consigna(c, M + 14, yt - 40, 'Pica aquest ritme i escriu-ne les paraules (ta o ti-ti).', pw - 28)
    sist(c, M + 14, yt - 84, pw - 28, 5.6, 'B4:q B4:e B4:e B4:q B4:q', 'treble', (4, 4), show_clef=False, show_time=False)
    linia(c, M + 14, yt - h + 18, pw - 28)
    p_medalla(c, x2, yt, pw, h, 4)
    c.showPage()


def repas5(c):
    cap_repas(c, 5, 'Els silencis de rodona, blanca, negra i corxera.', 'Ja saps comptar el silenci! Repassem com són i què duren.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 210
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'ESCRIU EL NOM DEL SILENCI', n=1)
    consigna(c, M + 14, yt - 40, 'Escriu quin silenci és cada un i quants temps dura.', CW - 28)
    for k, d in enumerate(['w', 'h', 'q', 'e']):
        x = M + 14 + k * 122
        g = 6
        ytop = yt - 84
        yb = pauta(c, x, ytop, 108, g, None, final=False)
        nt.draw_rest(c, x + 54, yb, ytop, g, d)
        linia(c, x, yb - 18, 100)
        txt(c, x + 54, yb - 34, '… temps', 10.5, SANS, MUTED, 'c')
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'QUANTS TEMPS DE SILENCI?', n=2)
    consigna(c, M + 14, yt - 40, 'Escriu els temps.', pw - 28)
    for k, t in enumerate(['C4:h R:h', 'C4:q R:q R:h', 'R:w']):
        yy = yt - 84 - k * 34
        sist(c, M + 14, yy, 150, 4.8, t, 'treble', (4, 4), show_clef=False, show_time=False)
        rr(c, M + pw - 48, yy - 20, 28, 22, 11, fill=white, lw=1.5, col=NAVY)
    p_vf(c, x2, yt, pw, h, 3, ['Els silencis també es compten.', 'El silenci de blanca dura 4 temps.', 'El silenci de negra dura 1 temps.'])
    h = 130
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'EL MUSSOL DORMILEGA', n=4)
    par(c, M + 14, yt - 44, 'Quan la profe toca un silenci, tu et converteixes en estàtua. Quants silencis has fet?', 11.5, pw - 28, 14.5, SANS, INK)
    p_medalla(c, x2, yt, pw, h, 5)
    c.showPage()


def repas6(c):
    cap_repas(c, 6, 'Les plicas i com dibuixar notes perfectes.', 'Ja saps escriure notes de llibre! Un petit repàs de plicas i dibuixos.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 200
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'AMUNT O AVALL?', n=1)
    consigna(c, M + 14, yt - 40, 'Posa la plica correcta a cada nota.', CW - 28)
    g = 8
    yb = pauta(c, M + 20, yt - 72, CW - 40, g, 'treble', final=True)
    for j, p_ in enumerate(['C4', 'G4', 'B4', 'E5', 'F4', 'A4', 'D5', 'E4']):
        cy_ = nt.note_y(yb, g, p_)
        xx = M + 90 + j * 48
        if p_ == 'C4':
            trac(c, 1.0, NAVY)
            c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
        trac(c, 1.5, NAVY)
        c.saveState()
        c.translate(xx, cy_)
        c.rotate(-20)
        c.setFillColor(NAVY)
        c.ellipse(-g * 0.78, -g * 0.55, g * 0.78, g * 0.55, stroke=1, fill=1)
        c.restoreState()
    yb = pauta(c, M + 20, yt - 140, CW - 40, g, 'bass', final=True)
    for j, p_ in enumerate(['F3', 'C3', 'E3', 'B2', 'A3', 'D3', 'G2', 'G3']):
        cy_ = nt.note_y(yb, g, p_, 'bass')
        xx = M + 90 + j * 48
        trac(c, 1.5, NAVY)
        c.saveState()
        c.translate(xx, cy_)
        c.rotate(-20)
        c.setFillColor(NAVY)
        c.ellipse(-g * 0.78, -g * 0.55, g * 0.78, g * 0.55, stroke=1, fill=1)
        c.restoreState()
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'LA LÍNIA DEL MIG', n=2)
    consigna(c, M + 14, yt - 40, 'Pinta la línia del mig de color i diu cap a on va la plica de cada nota.', pw - 28)
    g = 9
    yb = pauta(c, M + 14, yt - 84, pw - 28, g, 'treble', final=True)
    rr(c, M + 14, yb + 2 * g - 2, pw - 28, 4, 0, fill=HexColor('#D9C79C'), lw=0)
    for j, p_ in enumerate(['D4', 'B4', 'A4', 'F4']):
        nota_plica(c, M + 50 + j * 44, nt.note_y(yb, g, p_), g, nt._abs_idx(p_) < nt._abs_idx('B4'))
    p_vf(c, x2, yt, pw, h, 3, ['Les notes baixes tenen la plica cap amunt.', 'La plica és tan llarga com tres espais.'])
    h = 130
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'LA TEVA MELODIA', n=4)
    pauta(c, M + 14, yt - 72, pw - 28, 6.4, 'treble', final=True)
    p_medalla(c, x2, yt, pw, h, 6)
    c.showPage()


def repas7(c):
    cap_repas(c, 7, 'Mans, cançons, acords i com estudiar.', 'Ja toques de veritat! Repassem les mans, les cançons i l’acord de DO.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 176
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'LLEGEIX I TOCA', n=1)
    consigna(c, M + 14, yt - 40, 'Digues els noms i toca-ho: primer la mà dreta, després l’esquerra.', CW - 28)
    sist(c, M + 16, yt - 76, 440, 6.6, 'G4 F4 E4 D4 | C4 D4 E4 F4 | G4:h G4:h', 'treble', (4, 4))
    sist(c, M + 16, yt - 126, 440, 6.6, 'G3 F3 E3 D3 | C3 D3 E3 F3 | G3:h G3:h', 'bass', (4, 4))
    h = 190
    yt = pila.pren(h)
    p_uneix(c, M, yt, pw, h, 2, 'UNEIX AMB UNA LÍNIA', 'Cada cosa amb la seva clau o notes.', ['mà dreta', 'mà esquerra', 'acord de DO'], ['clau de fa', 'DO MI SOL', 'clau de sol'], fila=42, ampl_esq=84)
    p_vf(c, x2, yt, pw, h, 3, ['L’acord de DO té tres notes alhora.', 'L’Oda a l’alegria és de Beethoven.', 'Estudiar és començar per tocar-ho tot ràpid.'])
    h = 170
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'ELS TRES PASSOS', n=4)
    consigna(c, M + 14, yt - 40, 'Escriu els tres passos per estudiar.', pw - 28)
    for k in range(3):
        bola(c, M + 24, yt - 84 - k * 28 + 4, k + 1, 9)
        linia(c, M + 44, yt - 84 - k * 28, pw - 62)
    p_medalla(c, x2, yt, pw, h, 7)
    c.showPage()


def repas8(c):
    cap_repas(c, 8, 'Fort i suau, ràpid i lent, lligat i picat, frases.', 'Últim repàs! Ara ja saps fer sonar la música amb expressió.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 190
    yt = pila.pren(h)
    p_uneix(c, M, yt, pw, h, 1, 'UNEIX AMB UNA LÍNIA', 'Cada paraula amb el que vol dir.', ['allegro', 'piano', 'staccato'], ['suau', 'ràpid', 'curt i separat'], fila=42, ampl_esq=70)
    panell(c, x2, yt, pw, h, 'ORDENA', n=2)
    consigna(c, x2 + 14, yt - 40, 'Escriu 1, 2, 3, 4 de més suau a més fort.', pw - 28)
    for k, s_ in enumerate(['mf', 'pp', 'f', 'p']):
        xx = x2 + 14 + (k % 2) * 112
        yy = yt - 84 - (k // 2) * 52
        rr(c, xx, yy - 14, 100, 28, 8, fill=WARM, lw=1.5, col=NAVY)
        dinamica(c, xx + 36, yy - 6, s_, 19)
        rr(c, xx + 64, yy - 11, 30, 22, 11, fill=white, lw=1.6, col=NAVY)
    h = 176
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'LLIGAT O PICAT?', n=3)
    consigna(c, M + 14, yt - 40, 'Posa una línia corba (lligat) a la primera i puntets (picat) a la segona.', CW - 28)
    notes_linia(c, M + 14, yt - 80, CW / 2 - 28, 6.4, ['C4', 'D4', 'E4', 'F4'], None, 'treble', dx0=46)
    notes_linia(c, M + CW / 2 + 6, yt - 80, CW / 2 - 28, 6.4, ['G4', 'F4', 'E4', 'D4'], None, 'treble', dx0=46)
    h = 170
    yt = pila.pren(h)
    p_vf(c, M, yt, pw, h, 4, ['La repetició et fa tornar al principi.', 'El calderó fa la nota més curta.', 'Una frase és un tros de música amb sentit.'])
    p_medalla(c, x2, yt, pw, h, 8)
    c.showPage()
