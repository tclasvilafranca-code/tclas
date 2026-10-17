# -*- coding: utf-8 -*-
"""Capítol 8 · Expressem la música — temes 31 a 34 (teoria + jocs)."""
from nens_t06 import *                                            # noqa: F401,F403
from nens_t01 import pagina_jocs
from nens_tclas import pauta, cap
from nens_dib import tortuga, coet, petjades
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import notation as nt
import math

pdfmetrics.registerFont(TTFont('FreeSerifBI', '/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf'))


def dinamica(c, x, y, t, size=24, col=NAVY):
    txt(c, x, y, t, size, 'FreeSerifBI', col, 'c')


def regulador(c, x1, x2, y, obrint=True, h=12, lw=1.8):
    trac(c, lw, NAVY)
    if obrint:
        c.line(x1, y, x2, y + h / 2.0)
        c.line(x1, y, x2, y - h / 2.0)
    else:
        c.line(x1, y + h / 2.0, x2, y)
        c.line(x1, y - h / 2.0, x2, y)


def arc_frase(c, x1, x2, y, amunt=True, h=12, lw=1.6, dash=None):
    trac(c, lw, NAVY, dash)
    d = h if amunt else -h
    p = c.beginPath()
    p.moveTo(x1, y)
    p.curveTo(x1 + (x2 - x1) * 0.2, y + d, x2 - (x2 - x1) * 0.2, y + d, x2, y)
    c.drawPath(p, stroke=1, fill=0)
    c.setDash()


def notes_linia(c, x, ytop, w, gap, pitches, durs=None, clau='treble', final=True, staccato=(), lliga=(), nom_sota=None, dx0=58, estil='plena'):
    """Pentagrama amb notes equiespaiades (només altures; la durada dibuixa la cabeça i la plica)."""
    yb = pauta(c, x, ytop, w, gap, clau, final=final)
    n = len(pitches)
    dx = (w - dx0 - 24) / max(1, n - 1) if n > 1 else 0
    durs = durs or ['q'] * n
    xs = []
    for j, p_ in enumerate(pitches):
        xx = x + dx0 + j * dx
        cy_ = nt.note_y(yb, gap, p_, clau)
        if p_ == 'C4' and clau == 'treble' or p_ == 'C4' and clau == 'bass':
            trac(c, 1.0, NAVY)
            c.line(xx - gap * 1.3, cy_, xx + gap * 1.3, cy_)
        amunt = nt._abs_idx(p_) < nt._abs_idx('B4') if clau == 'treble' else nt._abs_idx(p_) < nt._abs_idx('D3')
        if durs[j] == 'w':
            cap(c, xx, cy_, gap, 'w', white)
        elif durs[j] == 'h':
            trac(c, 1.5, NAVY)
            c.saveState()
            c.translate(xx, cy_)
            c.rotate(-20)
            c.setFillColor(white)
            c.ellipse(-gap * 0.78, -gap * 0.55, gap * 0.78, gap * 0.55, stroke=1, fill=1)
            c.restoreState()
            c.line(xx + (gap * 0.74 if amunt else -gap * 0.74), cy_ + (gap * 0.1 if amunt else -gap * 0.1),
                   xx + (gap * 0.74 if amunt else -gap * 0.74), cy_ + (gap * 3.4 if amunt else -gap * 3.4))
        else:
            nota_plica(c, xx, cy_, gap, amunt)
        if j in staccato:
            c.setFillColor(NAVY)
            c.circle(xx, cy_ - gap * 1.25 if amunt else cy_ + gap * 1.25, gap * 0.2, stroke=0, fill=1)
        xs.append((xx, cy_, amunt))
    for (a, b) in lliga:
        xa, ya, _ = xs[a]
        xb, yb2, _ = xs[b]
        low = min(ya, yb2) - gap * 1.2
        arc_frase(c, xa, xb, low, amunt=False, h=gap * 1.4)
    return yb, xs


# ======================================================================== TEMA 31 · Fort i suau
def t31_teoria(c):
    pagina_tema(c, 31, 'Fort i suau', 'La música pot xiuxiuejar o cridar: cada cançó té el seu volum.', 'teoria')
    guia(c, M, Y(142), CW, 'Mira les lletres petites que hi ha sota les notes: ens diuen amb quina força toquem. '
         'Són paraules italianes escrites amb una sola lletra!', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 232
    panell(c, M, yt, CW, h, 'DE MOLT SUAU A MOLT FORT')
    noms = [('pp', 'pianíssim', 'molt suau'), ('p', 'piano', 'suau'), ('mp', 'mezzopiano', 'una mica suau'),
            ('mf', 'mezzoforte', 'una mica fort'), ('f', 'forte', 'fort'), ('ff', 'fortíssim', 'molt fort')]
    cw = (CW - 28) / 6.0
    for k, (s_, n_, d_) in enumerate(noms):
        x = M + 14 + k * cw
        hh = 22 + k * 15
        rr(c, x + 3, yt - 74 - 96 + 0, cw - 8, hh, 3, fill=WARM2 if k < 3 else HexColor('#D9C79C'), lw=1.5, col=NAVY)
        dinamica(c, x + cw / 2 - 1, yt - 74 - 96 + hh + 8, s_, 24)
        txt(c, x + cw / 2 - 1, yt - 188, n_, 9.6, SANSB, NAVY, 'c')
        txt(c, x + cw / 2 - 1, yt - 204, d_, 10, SANS, INK, 'c')
    txt(c, M + 16, yt - 48, 'Cada lletra té el seu volum, de menys a més:', 12, SANS, NAVY_SOFT)
    yt = Y(486)
    h = 150
    panell(c, M, yt, CW, h, 'CADA COP MÉS FORT, CADA COP MÉS SUAU')
    for k, (obr, t) in enumerate(((True, 'crescendo: cada vegada més fort'), (False, 'diminuendo: cada vegada més suau'))):
        yy = yt - 62 - k * 42
        regulador(c, M + 24, M + 24 + 190, yy, obr, 20)
        txt(c, M + 238, yy - 4, t, 12, SANSB, NAVY)
    franja(c, M, Y(656), CW, 44, 'RECORDA', 'p = piano = suau.   f = forte = fort.', 12.5)
    franja(c, M, Y(714), CW, 66, 'SABIES QUE?', 'El piano es diu així perquè va ser el primer teclat que podia tocar suau (piano) i fort (forte). Al principi es deia «pianoforte».', 11.5)
    c.showPage()


def t31_jocs(c):
    pagina_jocs(c, 31, 'Fort i suau · a jugar!', 'Més fort, més suau…',
                'Atenció, orelles de mussol! Aquí tot va de volum. Pots tocar-ho o cantar-ho a veure com sona.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=1)
    consigna(c, M + 14, yt - 40, 'Cada signe amb el seu significat.', pw - 28)

    def dib(c_, xr, yy, k):
        rr(c_, xr, yy - 14, 90, 28, 14, fill=white, lw=1.5, col=NAVY)
        txt(c_, xr + 45, yy - 5, ['molt fort', 'suau', 'fort'][k], 12, SANSB, INK, 'c')
    for k, s_ in enumerate(['p', 'ff', 'f']):
        yy = yt - 84 - k * 44
        rr(c, M + 14, yy - 14, 56, 30, 15, fill=white, lw=1.5, col=NAVY)
        dinamica(c, M + 42, yy - 6, s_, 20)
        c.setFillColor(NAVY)
        c.circle(M + 82, yy, 4, stroke=0, fill=1)
    ordre_ = ['suau', 'molt fort', 'fort']
    for k, t in enumerate(['molt fort', 'suau', 'fort']):
        yy = yt - 84 - k * 44
        rr(c, M + pw - 114, yy - 14, 90, 30, 15, fill=white, lw=1.5, col=NAVY)
        txt(c, M + pw - 69, yy - 6, t, 12, SANSB, INK, 'c')
        c.setFillColor(NAVY)
        c.circle(M + pw - 124, yy, 4, stroke=0, fill=1)
    panell(c, x2, yt, pw, h, 'ORDENA DE SUAU A FORT', n=2)
    consigna(c, x2 + 14, yt - 40, 'Escriu 1, 2, 3 i 4 sota cada lletra.', pw - 28)
    for k, s_ in enumerate(['f', 'pp', 'mf', 'p']):
        xx = x2 + 14 + (k % 2) * 112
        yy = yt - 88 - (k // 2) * 76
        rr(c, xx, yy - 18, 100, 36, 8, fill=WARM, lw=1.5, col=NAVY)
        dinamica(c, xx + 50, yy - 8, s_, 22)
        rr(c, xx + 34, yy - 52, 32, 24, 12, fill=white, lw=1.6, col=NAVY)
    h = 192
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'ESCRIU EL VOLUM', n=3)
    consigna(c, M + 14, yt - 40, 'Posa una dinàmica sota cada nota: p, mf o f. Després toca-ho!', CW - 28)
    notes_linia(c, M + 20, yt - 82, CW - 40, 8, ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4'], None, 'treble')
    for j in range(9):
        rr(c, M + 20 + 58 + j * ((CW - 40 - 58 - 24) / 8.0) - 14, yt - 146, 28, 22, 4, fill=white, lw=1.2, col=MUTED, dash=(2, 2))
    h = 130
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['La lletra f vol dir fort.', 'p vol dir molt fort.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'EL JOC DEL VOLUM', n=5)
    par(c, x2 + 14, yt - 44, 'Canteu junts una cançó: la profe aixeca la mà i us feu més forts; l’abaixa i us feu més suaus!', 11.5, pw - 28, 14.5, SANS, INK)
    c.showPage()


# ======================================================================== TEMA 32 · Ràpid i lent
def t32_teoria(c):
    pagina_tema(c, 32, 'Ràpid i lent', 'Una cançó pot anar lenta com una tortuga o ràpida com un coet.', 'teoria')
    guia(c, M, Y(142), CW, 'La velocitat de la música es diu tempo. El mateix pols pot anar a poc a poc, a un pas normal o '
         'molt de pressa.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 262
    panell(c, M, yt, CW, h, 'TRES VELOCITATS')
    cw = (CW - 28) / 3.0
    dades = [('LENT', 'adagio', '60', tortuga, 1.0), ('MODERAT', 'andante', '90', petjades, 1.2), ('RÀPID', 'allegro', '140', coet, 0.9)]
    for k, (t, it, bpm, f, sc) in enumerate(dades):
        x = M + 14 + k * cw
        rr(c, x + 2, yt - h + 14, cw - 8, h - 50, 8, fill=WARM, lw=1.5, col=NAVY)
        f(c, x + cw / 2 - 3, yt - (108 if f is not coet else 100), sc, color=False)
        txt(c, x + cw / 2 - 3, yt - 176, t, 16, ETQ, NAVY, 'c')
        txt(c, x + cw / 2 - 3, yt - 196, it, 13, 'FreeSerifBI', OCRE, 'c')
        txt(c, x + cw / 2 - 20, yt - 220, '♩', 15, 'DejaVuSans-Bold', NAVY_SOFT, 'c')
        txt(c, x + cw / 2 + 10, yt - 220, '= ' + bpm, 12.5, SANSB, NAVY_SOFT, 'c')
    yt = Y(518)
    h = 130
    panell(c, M, yt, CW, h, 'EL MATEIX POLS, TRES VELOCITATS')
    for k, (t, d) in enumerate((('lent', 70), ('moderat', 44), ('ràpid', 24))):
        yy = yt - 52 - k * 28
        txt(c, M + 16, yy - 4, t, 11.5, SANSB, NAVY)
        for j in range(int((CW - 150) / d)):
            c.setFillColor(NAVY)
            c.circle(M + 110 + j * d, yy, 6 if k == 0 else (5 if k == 1 else 4), stroke=0, fill=1)
    franja(c, M, Y(666), CW, 44, 'RECORDA', 'Lent = adagio · moderat = andante · ràpid = allegro.', 12.5)
    franja(c, M, Y(724), CW, 56, 'SABIES QUE?', 'El metrònom diu quants pulsos hi ha cada minut: com més gran és el número, més ràpida és la música.', 11.8)
    c.showPage()


def t32_jocs(c):
    pagina_jocs(c, 32, 'Ràpid i lent · a jugar!', 'Com una tortuga o com un coet?',
                'Posa-t’hi i imagina quina velocitat té cada cosa. Escoltant música ho notaràs molt fàcil!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 202
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'LENT O RÀPID?', n=1)
    consigna(c, M + 14, yt - 40, 'Marca com va cada cosa.', pw - 28)
    coses = ['una tortuga', 'un coet', 'un caragol', 'un guepard']
    for k, t in enumerate(coses):
        yy = yt - 84 - k * 28
        txt(c, M + 16, yy, t, 12.5, SANSB, NAVY)
        for j, l in enumerate(('lent', 'ràpid')):
            rr(c, M + pw - 112 + j * 52, yy - 8, 48, 22, 11, fill=white, lw=1.4, col=NAVY)
            txt(c, M + pw - 88 + j * 52, yy - 1, l, 10.5, SANSB, NAVY_SOFT, 'c')
    panell(c, x2, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=2)
    consigna(c, x2 + 14, yt - 40, 'Cada paraula italiana amb el seu significat.', pw - 28)
    for k, s_ in enumerate(['allegro', 'adagio', 'andante']):
        yy = yt - 84 - k * 44
        rr(c, x2 + 14, yy - 14, 76, 28, 14, fill=white, lw=1.5, col=NAVY)
        txt(c, x2 + 52, yy - 5, s_, 12, 'FreeSerifBI', INK, 'c')
        c.setFillColor(NAVY)
        c.circle(x2 + 102, yy, 4, stroke=0, fill=1)
    for k, t in enumerate(['moderat', 'ràpid', 'lent']):
        yy = yt - 84 - k * 44
        rr(c, x2 + pw - 98, yy - 14, 84, 28, 14, fill=white, lw=1.5, col=NAVY)
        txt(c, x2 + pw - 56, yy - 5, t, 12, SANSB, INK, 'c')
        c.setFillColor(NAVY)
        c.circle(x2 + pw - 108, yy, 4, stroke=0, fill=1)
    h = 170
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'PICA I MIRA’L', n=3)
    consigna(c, M + 14, yt - 40, 'Pica de mans lent, normal i ràpid. Pinta els cercles quan hagis picat cada fila.', CW - 28)
    for k, (t, d) in enumerate((('lent', 62), ('normal', 40), ('ràpid', 22))):
        yy = yt - 84 - k * 28
        txt(c, M + 16, yy - 4, t, 11.5, SANSB, NAVY)
        for j in range(int((CW - 150) / d)):
            trac(c, 1.4, NAVY)
            c.setFillColor(white)
            c.circle(M + 110 + j * d, yy, 8, stroke=1, fill=1)
    h = 100
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['Allegro vol dir ràpid.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'EL MUSSOL PERESÓS', n=5)
    par(c, x2 + 14, yt - 44, 'Camina lent, normal i ràpid pel pols de la profe!', 11.5, pw - 28, 14.5, SANS, INK)
    c.showPage()


# ======================================================================== TEMA 33 · Lligat i picat
def t33_teoria(c):
    pagina_tema(c, 33, 'Lligat i picat', 'Les notes es poden tocar enllaçades o com petits botets.', 'teoria')
    guia(c, M, Y(142), CW, 'Les mateixes notes poden sonar de dues maneres! Enllaçades, com si anéssim lliscant, '
         'o separades, com si saltéssim.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 200
    panell(c, M, yt, CW, h, 'LLIGAT (LEGATO)')
    notes_linia(c, M + 20, yt - 70, CW - 40, 8.4, ['C4', 'D4', 'E4', 'F4', 'G4'], None, 'treble', lliga=[(0, 4)])
    arc_frase(c, M + 20 + 58, M + 20 + (CW - 40) - 24, yt - 62, True, 18)
    par(c, M + 20, yt - 150, 'Una línia corba sobre les notes vol dir: toca-les enllaçades, sense espais enmig, com si lliscessis!', 12, CW - 40, 16, SANS, INK)
    txt(c, M + 20, yt - h + 14, 'Penses en caminar arrossegant els peus suaument.', 11.2, SANS, MUTED)
    yt = Y(458)
    h = 190
    panell(c, M, yt, CW, h, 'PICAT (STACCATO)')
    notes_linia(c, M + 20, yt - 70, CW - 40, 8.4, ['C4', 'D4', 'E4', 'F4', 'G4'], None, 'treble', staccato=[0, 1, 2, 3, 4])
    par(c, M + 20, yt - 144, 'Un puntet a sobre o a sota de la nota vol dir: toca-la curta i separada, com un botet!', 12, CW - 40, 16, SANS, INK)
    txt(c, M + 20, yt - h + 14, 'Penses en saltar com una pilota.', 11.2, SANS, MUTED)
    franja(c, M, Y(666), CW, 44, 'RECORDA', 'Línia corba = enllaçat.   Puntet = curt i separat.', 12.5)
    franja(c, M, Y(724), CW, 56, 'SABIES QUE?', 'La línia corba sobre notes diferents és germana de la lligadura de valor, però aquesta només uneix notes iguals.', 11.5)
    c.showPage()


def t33_jocs(c):
    pagina_jocs(c, 33, 'Lligat i picat · a jugar!', 'Lliscar o botar?',
                'Mira bé els signes que hi ha a les notes i decideix com les has de tocar.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 214
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'LLIGAT O PICAT?', n=1)
    consigna(c, M + 14, yt - 40, 'Mira cada línia i marca com s’ha de tocar.', CW - 28)
    for k, (st, lg) in enumerate(((range(4), []), ([], [(0, 3)]), (range(4), []))):
        yy = yt - 78 - k * 50
        notes_linia(c, M + 14, yy, 300, 5.6, ['C4', 'D4', 'E4', 'F4'], None, 'treble', staccato=list(st), lliga=lg, dx0=46)
        if lg:
            arc_frase(c, M + 14 + 46, M + 14 + 300 - 24, yy + 8, True, 14)
        for j, l in enumerate(('lligat', 'picat')):
            rr(c, M + 336 + j * 78, yy - 24, 70, 24, 12, fill=white, lw=1.5, col=NAVY)
            txt(c, M + 371 + j * 78, yy - 17, l, 11.5, SANSB, NAVY_SOFT, 'c')
    h = 178
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'DIBUIXA EL SIGNE', n=2)
    consigna(c, M + 14, yt - 40, 'Posa una línia corba perquè sigui lligat.', pw - 28)
    notes_linia(c, M + 14, yt - 90, pw - 28, 6.4, ['E4', 'F4', 'G4', 'A4'], None, 'treble', dx0=44)
    panell(c, x2, yt, pw, h, 'DIBUIXA ELS PUNTETS', n=3)
    consigna(c, x2 + 14, yt - 40, 'Posa puntets perquè sigui picat.', pw - 28)
    notes_linia(c, x2 + 14, yt - 90, pw - 28, 6.4, ['G4', 'F4', 'E4', 'D4'], None, 'treble', dx0=44)
    h = 120
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['Els puntets són notes curtes.', 'Lligat és tocar a trossos.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'EL JOC DEL GAT I LA PILOTA', n=5)
    par(c, x2 + 14, yt - 44, 'Mou la mà com un gat que llisca (lligat) o com una pilota que bota (picat).', 11.5, pw - 28, 14.5, SANS, INK)
    c.showPage()


# ======================================================================== TEMA 34 · Repeticions, frases i calderó
def t34_teoria(c):
    pagina_tema(c, 34, 'Repeticions, frases i calderó', 'Tres senyals que ens diuen com respirar la música.', 'teoria')
    guia(c, M, Y(142), CW, 'Una cançó és com una conversa: té frases, repeticions i algun moment per aturar-se. '
         'Aquests tres senyals ens ajuden.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 152
    panell(c, M, yt, CW, h, 'LA REPETICIÓ')
    sist(c, M + 16, yt - 60, 440, 7.4, 'C4 D4 E4 F4 | G4 F4 E4 D4', 'treble', (4, 4), repetir='cierra')
    txt(c, M + 16, yt - h + 14, 'Les dues barres amb punts diuen: torna al principi i repeteix-ho!', 11.8, SANS, INK)
    yt = Y(406)
    h = 160
    panell(c, M, yt, CW, h, 'LA FRASE')
    yb, xs = notes_linia(c, M + 20, yt - 82, CW - 40, 8, ['C4', 'D4', 'E4', 'D4', 'E4', 'F4', 'G4', 'F4'], None, 'treble')
    arc_frase(c, xs[0][0], xs[3][0], yt - 70, True, 14)
    arc_frase(c, xs[4][0], xs[7][0], yt - 70, True, 14)
    txt(c, (xs[0][0] + xs[3][0]) / 2, yt - 46, 'frase 1', 11, SANSB, OCRE, 'c')
    txt(c, (xs[4][0] + xs[7][0]) / 2, yt - 46, 'frase 2', 11, SANSB, OCRE, 'c')
    txt(c, M + 16, yt - h + 14, 'Una frase és com una frase del llenguatge: té un principi, un final i un moment per agafar aire.', 11.5, SANS, INK)
    yt = Y(584)
    h = 130
    panell(c, M, yt, CW, h, 'EL CALDERÓ')
    sist(c, M + 16, yt - 58, 300, 7.4, 'C4:q D4:q E4:h!', 'treble', (4, 4))
    par(c, M + 330, yt - 54, 'Aquest signe sobre la nota vol dir: queda’t una mica més del que diu la figura!', 11.5, CW - 346, 14, SANS, INK)
    franja(c, M, Y(728), CW, 56, 'RECORDA', 'Repetició = tornar al principi · frase = unitat de música · calderó = aturar-se una mica més.', 11.5)
    c.showPage()


def t34_jocs(c):
    pagina_jocs(c, 34, 'Repeticions, frases i calderó · a jugar!', 'Torna a començar!',
                'Aquests senyals són com semàfors: et diuen quan tornar, quan respirar i quan esperar.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 160
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'UNEIX SENYAL I SIGNIFICAT', n=1)
    consigna(c, M + 14, yt - 40, 'Cada senyal amb el que vol dir.', CW - 28)
    sig = [('rep', 'torna al principi'), ('cald', 'quedar-se més temps'), ('arc', 'una frase')]
    for k in range(3):
        yy = yt - 84 - k * 0
    xs_ = [M + 80, M + 242, M + 404]
    for k, (t, d) in enumerate(sig):
        cx_ = xs_[k]
        if t == 'rep':
            trac(c, 3.2, NAVY)
            c.line(cx_ + 8, yt - 70, cx_ + 8, yt - 104)
            trac(c, 1.6, NAVY)
            c.line(cx_ + 14, yt - 70, cx_ + 14, yt - 104)
            c.setFillColor(NAVY)
            c.circle(cx_ + 1, yt - 82, 2.2, stroke=0, fill=1)
            c.circle(cx_ + 1, yt - 92, 2.2, stroke=0, fill=1)
        elif t == 'cald':
            c.setFillColor(NAVY)
            c.circle(cx_, yt - 96, 2.4, stroke=0, fill=1)
            trac(c, 2.2, NAVY)
            p = c.beginPath()
            p.moveTo(cx_ - 16, yt - 96)
            p.curveTo(cx_ - 14, yt - 70, cx_ + 14, yt - 70, cx_ + 16, yt - 96)
            c.drawPath(p, stroke=1, fill=0)
        else:
            arc_frase(c, cx_ - 24, cx_ + 24, yt - 90, True, 18)
        c.setFillColor(NAVY)
        c.circle(cx_, yt - 112, 4, stroke=0, fill=1)
        rr(c, cx_ - 66, yt - 148, 132, 24, 12, fill=white, lw=1.5, col=NAVY)
        txt(c, cx_, yt - 140, ['una frase', 'torna al principi', 'quedar-se més temps'][k], 11.2, SANSB, INK, 'c')
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'POSA LES FRASES', n=2)
    consigna(c, M + 14, yt - 40, 'Dibuixa un arc per cada frase.', pw - 28)
    notes_linia(c, M + 14, yt - 96, pw - 28, 6.8, ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4'], None, 'treble', dx0=44)
    panell(c, x2, yt, pw, h, 'SOPA DE LLETRES', n=3)
    consigna(c, x2 + 14, yt - 40, 'Troba 5 paraules.', pw - 28)
    pal = ['FRASE', 'REPETIR', 'CALDERO', 'ARC', 'RESPIRA']
    dibuixa_sopa(c, x2 + 14, yt - 52, sopa(pal, 8, seed=111), 15.5, 11.5)
    h = 170
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['El calderó fa la nota més curta.', 'Una frase és com una frase parlada.', 'La repetició torna al principi.'], 11.8, 14)
    panell(c, x2, yt, pw, h, 'EL TEU FINAL', n=5)
    consigna(c, x2 + 14, yt - 40, 'Escriu una nota amb calderó per acabar la teva cançó.', pw - 28)
    pauta(c, x2 + 14, yt - 90, pw - 28, 6.4, 'treble', final=True)
    c.showPage()
