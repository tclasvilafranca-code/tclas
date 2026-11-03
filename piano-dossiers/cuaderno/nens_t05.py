# -*- coding: utf-8 -*-
"""Capítols 5 i 6 · Els silencis i Les plicas — temes 20 a 23 (teoria + jocs)."""
from nens_t04 import *                                            # noqa: F401,F403
from nens_jocs2 import p_cruci, p_cami, p_intrus, p_mosaic, p_laberint, HEART, HOUSE
from nens_t01 import pagina_jocs
from nens_tclas import pauta, cap
import notation as nt


def silenci(c, cx, ytop, gap, dur):
    """Un silenci sobre un pentagrama (dibuixa el pentagrama de 5 línies)."""
    yb = pauta(c, cx - gap * 3, ytop, gap * 6, gap, None, final=False)
    nt.draw_rest(c, cx, yb, ytop, gap, dur)
    return yb


def silenci_sol(c, cx, yb, ytop, gap, dur):
    nt.draw_rest(c, cx, yb, ytop, gap, dur)


def nota_plica(c, cx, cy, gap, amunt, fill=NAVY, lw=1.5):
    """Nota negra amb plica cap amunt (a la dreta) o cap avall (a l'esquerra)."""
    trac(c, lw, NAVY)
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-20)
    c.setFillColor(fill)
    c.ellipse(-gap * 0.78, -gap * 0.55, gap * 0.78, gap * 0.55, stroke=1, fill=1)
    c.restoreState()
    trac(c, lw, NAVY)
    if amunt:
        c.line(cx + gap * 0.74, cy + gap * 0.1, cx + gap * 0.74, cy + gap * 3.4)
    else:
        c.line(cx - gap * 0.74, cy - gap * 0.1, cx - gap * 0.74, cy - gap * 3.4)


def nota_punts(c, cx, cy, gap, amunt=True, tipus='q'):
    """La mateixa nota en traç de punts (per repassar)."""
    c.saveState()
    c.setStrokeColor(MUTED)
    c.setLineWidth(1.1)
    c.setDash(1.8, 2.2)
    c.translate(cx, cy)
    c.rotate(-20)
    c.ellipse(-gap * 0.78, -gap * 0.55, gap * 0.78, gap * 0.55, stroke=1, fill=0)
    c.restoreState()
    c.saveState()
    c.setStrokeColor(MUTED)
    c.setLineWidth(1.1)
    c.setDash(1.8, 2.2)
    if tipus != 'w':
        if amunt:
            c.line(cx + gap * 0.74, cy + gap * 0.1, cx + gap * 0.74, cy + gap * 3.4)
        else:
            c.line(cx - gap * 0.74, cy - gap * 0.1, cx - gap * 0.74, cy - gap * 3.4)
    c.restoreState()


# ======================================================================== TEMA 20 · Silenci de rodona i blanca
def t20_teoria(c):
    pagina_tema(c, 20, 'Silenci de rodona i de blanca', 'Quan la música fa silenci, nosaltres també… però continuem comptant!', 'teoria')
    guia(c, M, Y(142), CW, 'Shhh! Els silencis són moments en què no sona res. Duren igual que les notes que ja coneixes, però no es toquen: '
         'només es compten.', color=False, size=12.5, h=80)
    pw, x2 = meitats()
    yt = Y(238)
    h = 200
    for k, (nom, dur, temps, frase) in enumerate((('SILENCI DE RODONA', 'w', 4, 'penja de la línia'), ('SILENCI DE BLANCA', 'h', 2, 's’asseu sobre la línia'))):
        x = M + k * (pw + 18)
        panell(c, x, yt, pw, h, nom)
        g = 17
        ytop = yt - 56
        yb = pauta(c, x + 20, ytop, pw - 40, g, None, final=False)
        nt.draw_rest(c, x + pw / 2, yb, ytop, g, dur)
        txt(c, x + pw / 2, yt - 150, '%d temps de silenci' % temps, 13, SANSB, NAVY, 'c')
        txt(c, x + pw / 2, yt - 168, 'El silenci ' + frase + '.', 11.5, SANS, INK, 'c')
        txt(c, x + pw / 2, yt - 184, ('Com un barret que penja!' if k == 0 else 'Com un barret assegut!'), 11.5, SANS, MUTED, 'c')
    yt = Y(456)
    h = 150
    panell(c, M, yt, CW, h, 'NOTA I SILENCI, MATEIXA DURADA')
    files = [('w', 'RODONA', 4), ('h', 'BLANCA', 2)]
    for k, (t, nom, n) in enumerate(files):
        yy = yt - 48 - k * 48
        txt(c, M + 16, yy - 14, nom, 11.5, SANSB, NAVY)
        figura(c, t, M + 112, yy - 8, 6.5 if t != 'w' else 8.5)
        tira_temps(c, M + 150, yy - 22, 160, 30, [(t, n)] if False else [('q', 1)] * 0 + [(t, n)], total=4) if False else None
        for j in range(4):
            rr(c, M + 150 + j * 40, yy - 22, 38, 30, 4, fill=WARM2 if j < n else white, lw=1.4, col=NAVY)
        txt(c, M + 340, yy - 8, 'sona %d temps' % n, 11.5, SANS, INK)
        txt(c, M + 340, yy - 24, 'silenci de %d temps' % n, 11.5, SANS, MUTED)
    franja(c, M, Y(622), CW, 44, 'RECORDA', 'La rodona penja de la línia; la blanca s’asseu a sobre.', 12.5)
    yt = Y(682)
    h = 98
    panell(c, M, yt, CW, h, 'UN COMPÀS AMB SILENCI')
    sist(c, M + 16, yt - 48, 380, 7, 'C4:h R:h | E4:q E4:q R:h', 'treble', (4, 4))
    txt(c, M + CW - 14, yt - 50, 'Toca-ho', 12, SANSB, NAVY, 'r')
    txt(c, M + CW - 14, yt - 66, 'i compta-ho!', 12, SANSB, NAVY, 'r')
    c.showPage()


def t20_jocs(c):
    pagina_jocs(c, 20, 'Els silencis · a jugar!', 'Shhh…',
                'Sense silencis la música seria un soroll! Jugarem amb ells.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 180
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'PENJA O S’ASSEU?', n=1)
    consigna(c, M + 14, yt - 40, 'Encercla com és cada silenci.', pw - 28)
    for k, d in enumerate(['w', 'h', 'h', 'w']):
        col, fila = k % 2, k // 2
        xx = M + 14 + col * 116
        yy = yt - 82 - fila * 50
        g = 6.4
        yb = pauta(c, xx, yy, 100, g, None, final=False)
        nt.draw_rest(c, xx + 50, yb, yy, g, d)
        for j, l in enumerate(('penja', 'seu')):
            txt(c, xx + 22 + j * 54, yb - 11, l, 9.5, SANSB, NAVY_SOFT, 'c')
    panell(c, x2, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=2)
    consigna(c, x2 + 14, yt - 40, 'Cada silenci amb els seus temps.', pw - 28)

    def dib(c_, xr, yy, k):
        g = 5.6
        yb_ = pauta(c_, xr, yy + 12, 90, g, None, final=False)
        nt.draw_rest(c_, xr + 45, yb_, yy + 12, g, ['h', 'w'][k])
    uneix(c, x2 + 14, yt - 84, pw - 28, ['4 temps', '2 temps'], ['', ''], fila=52, ampl_esq=70, ampl_dre=90, dibuix_dre=dib, serif=False)
    h = 198
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'COMPTA ELS SILENCIS', n=3)
    consigna(c, M + 14, yt - 40, 'Quants temps de silenci hi ha a cada compàs? Escriu-ho a la caseta.', CW - 28)
    for k, t in enumerate(['C4:h R:h', 'E4:q R:q R:h', 'R:w', 'D4:h R:q E4:q']):
        col, fila = k % 2, k // 2
        xx = M + 14 + col * 246
        yy = yt - 80 - fila * 52
        sist(c, xx, yy, 190, 5.6, t, 'treble', (4, 4), show_clef=False, show_time=False)
        rr(c, xx + 202, yy - 22, 30, 24, 5, fill=white, lw=1.5, col=NAVY)
    h = 136
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'DIBUIXA', n=4)
    consigna(c, M + 14, yt - 40, 'Dibuixa un silenci de rodona i un de blanca.', pw - 28)
    for k in range(2):
        pauta(c, M + 14 + k * 112, yt - 82, 100, 7, None, final=False)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=5)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['El silenci de blanca dura 2 temps.', 'En un silenci no es compta.'], 12, 14.5)
    c.showPage()


# ======================================================================== TEMA 21 · Silenci de negra i corxera
def t21_teoria(c):
    pagina_tema(c, 21, 'Silenci de negra i de corxera', 'Cada figura té el seu silenci, amb el mateix temps de durada.', 'teoria')
    guia(c, M, Y(142), CW, 'Hi ha un silenci per a cada figura! Aquests són els de la negra i la corxera, que són els més curts: '
         'els trobaràs a tot arreu.', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 232
    panell(c, M, yt, CW, h, 'CADA FIGURA, EL SEU SILENCI')
    cw = (CW - 28) / 4.0
    dades = [('w', 'rodona', '4'), ('h', 'blanca', '2'), ('q', 'negra', '1'), ('e', 'corxera', '½')]
    for k, (t, nm, v) in enumerate(dades):
        x = M + 14 + k * cw
        rr(c, x + 2, yt - h + 14, cw - 8, h - 50, 8, fill=WARM, lw=1.5, col=NAVY)
        cx_ = x + cw / 2 - 3
        txt(c, cx_, yt - 62, nm.upper(), 11.5, ETQ, NAVY, 'c')
        figura(c, t, cx_, yt - 100 if t != 'w' else yt - 94, 9 if t != 'w' else 11)
        g = 8.5
        ytop = yt - 138
        yb = pauta(c, x + 10, ytop, cw - 24, g, None, final=False)
        nt.draw_rest(c, cx_, yb, ytop, g, t)
        txt(c, cx_, yt - 200, v + (' temps' if v not in ('1',) else ' temps'), 13, SANSB, OCRE, 'c')
    franja(c, M, Y(494), CW, 44, 'RECORDA', 'El silenci de negra és com un rull; el de corxera, com un 7 amb un punt.', 12)
    yt = Y(558)
    h = 142
    panell(c, M, yt, CW, h, 'ALGUNS COMPASSOS AMB SILENCIS')
    sist(c, M + 16, yt - 50, 440, 7, 'C4:q R:q E4:q R:q | G4:q R:h R:q', 'treble', (4, 4))
    sist(c, M + 16, yt - 100, 440, 7, 'C4:e R:e C4:e R:e E4:h | E4:q R:e E4:e G4:h', 'treble', (4, 4))
    franja(c, M, Y(716), CW, 56, 'SABIES QUE?', 'En música, el silenci és tan important com el so: fins i tot les cançons més famoses en porten!', 12)
    c.showPage()


def t21_jocs(c):
    pagina_jocs(c, 21, 'Silenci de negra i corxera · a jugar!', 'Cada figura, el seu silenci.',
                'Ara que coneixes tots els silencis, juguem a trobar-los. Aquí i allà n’hi ha d’amagats!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 188
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'UNEIX NOTA I SILENCI', n=1)
    consigna(c, M + 14, yt - 40, 'Cada figura amb el seu silenci.', CW - 28)
    ordre = ['e', 'q', 'h', 'w']
    ordre_sil = ['q', 'w', 'e', 'h']
    for k in range(4):
        yy = yt - 86 - k * 0
    for k in range(4):
        xx = M + 40 + k * 118
        figura(c, ordre[k], xx, yt - 92 if ordre[k] != 'w' else yt - 86, 6.5 if ordre[k] != 'w' else 8)
        c.setFillColor(NAVY)
        c.circle(xx, yt - 112, 4, stroke=0, fill=1)
        c.circle(xx, yt - 138, 4, stroke=0, fill=1)
        g = 5.6
        ytop = yt - 148
        yb = pauta(c, xx - 36, ytop, 72, g, None, final=False)
        nt.draw_rest(c, xx, yb, ytop, g, ordre_sil[k])
    h = 212
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'COMPTA ELS TEMPS', n=2)
    consigna(c, M + 14, yt - 40, 'Quants temps dura cada compàs? Han de ser 4.', pw - 28)
    for k, t in enumerate(['C4:q R:q D4:q R:q', 'E4:h R:q R:q', 'G4:q R:e E4:e R:h', 'R:h R:q C4:q']):
        yy = yt - 80 - k * 33
        sist(c, M + 14, yy, 150, 4.6, t, 'treble', (4, 4), show_clef=False, show_time=False)
        rr(c, M + pw - 48, yy - 19, 28, 24, 12, fill=white, lw=1.5, col=NAVY)
    p_intrus(c, x2, yt, pw, h, 3, [['rodona', 'blanca', 'negra', 'pedal'], ['shh', 'silenci', 'no sona', 'ti-ti'], ['1 temps', '2 temps', '4 temps', 'ràpid']], consigna_t='Encercla el que no hi pinta.')
    h = 120
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['El silenci de negra dura 1 temps.', 'Els silencis fan soroll.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'EL JOC DEL MUSSOL DORMILEGA', n=5)
    par(c, x2 + 14, yt - 44, 'La profe toca una cançó. Quan s’atura, ets una estàtua! Fins que torna a tocar.', 11.5, pw - 28, 14.5, SANS, INK)
    c.showPage()


# ======================================================================== TEMA 22 · La plica
def t22_teoria(c):
    pagina_tema(c, 22, 'Plica amunt o avall', 'El palet de la nota va cap amunt o cap avall, segons on viu la nota.', 'teoria')
    guia(c, M, Y(142), CW, 'Fixa’t en el palet de les notes: es diu plica! A vegades mira cap amunt i a vegades cap avall. '
         'Descobreix la norma!', color=False, size=12.5, h=80)
    yt = Y(238)
    h = 226
    panell(c, M, yt, CW, h, 'LA LÍNIA DEL MIG MANA')
    g = 12
    ytop = yt - 64
    yb = pauta(c, M + 24, ytop, CW - 48, g, 'treble', final=True)
    mid = yb + 2 * g
    rr(c, M + 24, mid - 2, CW - 48, 4, 0, fill=OCRE, lw=0)
    pit = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
    for j, p_ in enumerate(pit):
        cy_ = nt.note_y(yb, g, p_)
        xx = M + 90 + j * 36
        amunt = (j + 0 < 6) and nt._abs_idx(p_) < nt._abs_idx('B4')
        if p_ == 'C4':
            trac(c, 1.2, NAVY)
            c.line(xx - g * 1.3, cy_, xx + g * 1.3, cy_)
        nota_plica(c, xx, cy_, g, amunt)
    txt(c, M + 24, yt - h + 54, 'Per sota de la línia del mig  →  plica AMUNT, a la dreta de la nota.', 12, SANSB, NAVY)
    txt(c, M + 24, yt - h + 34, 'A la línia del mig i per sobre  →  plica AVALL, a l’esquerra de la nota.', 12, SANSB, NAVY)
    txt(c, M + 24, yt - h + 14, '(La línia ocre és la línia del mig.)', 10.5, SANS, MUTED)
    yt = Y(480)
    h = 138
    panell(c, M, yt, CW, h, 'ZOOM A UNA NOTA')
    for k, (am, t) in enumerate(((True, 'plica amunt: surt per la dreta'), (False, 'plica avall: surt per l’esquerra'))):
        x = M + 14 + k * (CW - 28) / 2.0
        gap = 14
        cx_ = x + 80
        cy_ = yt - (96 if am else 52)
        nota_plica(c, cx_, cy_, gap, am)
        txt(c, x + 150, yt - 74, t, 11.5, SANS, INK) if False else None
        par(c, x + 130, yt - 70, t, 11.5, (CW - 28) / 2.0 - 134, 14, SANS, INK)
    franja(c, M, Y(634), CW, 44, 'RECORDA', 'Notes baixes: plica cap amunt. Notes altes: plica cap avall.', 12.5)
    franja(c, M, Y(692), CW, 56, 'SABIES QUE?', 'Si una nota és exactament a la línia del mig, la plica pot anar cap a on vulguis. Normalment la fem cap avall.', 11.8)
    c.showPage()


def t22_jocs(c):
    pagina_jocs(c, 22, 'La plica · a jugar!', 'Amunt o avall?',
                'Mira on viu cada nota i decideix cap a on mira la plica. Compta les línies del mig!')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 190
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'DIBUIXA LA PLICA', n=1)
    consigna(c, M + 14, yt - 40, 'Posa la plica a cada nota: amunt o avall?', CW - 28)
    g = 8
    yb = pauta(c, M + 20, yt - 70, CW - 40, g, 'treble', final=True)
    for j, p_ in enumerate(['C4', 'F4', 'A4', 'D5', 'E4', 'G4', 'B4', 'C5']):
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
    g = 8
    yb = pauta(c, M + 20, yt - 134, CW - 40, g, 'bass', final=True)
    for j, p_ in enumerate(['E3', 'C3', 'G3', 'B2', 'D3', 'A3', 'F3', 'G2']):
        cy_ = nt.note_y(yb, g, p_, 'bass')
        xx = M + 90 + j * 48
        trac(c, 1.5, NAVY)
        c.saveState()
        c.translate(xx, cy_)
        c.rotate(-20)
        c.setFillColor(NAVY)
        c.ellipse(-g * 0.78, -g * 0.55, g * 0.78, g * 0.55, stroke=1, fill=1)
        c.restoreState()
    h = 178
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'TROBA L’ERROR', n=2)
    consigna(c, M + 14, yt - 40, 'Una plica està al revés. Encercla-la!', pw - 28)
    g = 7.5
    yb = pauta(c, M + 14, yt - 82, pw - 28, g, 'treble', final=True)
    for j, (p_, am) in enumerate([('D4', True), ('A4', False), ('F4', True), ('G4', False), ('E5', True)]):
        xx = M + 64 + j * 36
        nota_plica(c, xx, nt.note_y(yb, g, p_), g, am)
    panell(c, x2, yt, pw, h, 'VERITAT O FALS?', n=3)
    capcalera_vf(c, x2 + 14, yt - 34, pw - 14)
    veritat_fals(c, x2 + 14, yt - 50, pw - 14, ['Les notes baixes tenen la plica cap amunt.', 'La plica d’una nota alta va cap amunt.', 'Una nota pot no tenir plica (la rodona).'], 11.8, 14)
    h = 126
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'ENDEVINA', n=4)
    consigna(c, M + 14, yt - 40, 'La profe diu una nota (per exemple, SOL) i tu dibuixes a la pauta la nota amb la plica correcta.', CW - 28)
    for k in range(3):
        pauta(c, M + 14 + k * 164, yt - 84, 150, 6, 'treble', final=False)
    c.showPage()


# ======================================================================== TEMA 23 · Dibuixo notes perfectes
def t23_teoria(c):
    pagina_tema(c, 23, 'Dibuixo notes perfectes', 'Quatre passos per dibuixar una nota que sembli de llibre.', 'teoria')
    guia(c, M, Y(142), CW, 'Vols escriure música tu mateix? Doncs fixa’t com es dibuixa una nota! Té quatre passos molt fàcils.',
         color=False, size=12.5, h=80)
    yt = Y(238)
    h = 238
    panell(c, M, yt, CW, h, 'ELS QUATRE PASSOS')
    cw = (CW - 28) / 4.0
    textos = ['Dibuixa un ou una mica inclinat, que ocupi un espai.', 'Afegeix la plica: tres espais d’alçada.', 'Pinta’l de negre (si és una negra).', 'Comprova que toca la línia o l’espai correcte!']
    for k in range(4):
        x = M + 14 + k * cw
        rr(c, x + 2, yt - h + 14, cw - 8, h - 50, 8, fill=WARM, lw=1.4, col=NAVY)
        bola(c, x + 18, yt - 62, k + 1, 11)
        g = 12
        yb = pauta(c, x + 8, yt - 98, cw - 20, g, None, final=False)
        cy_ = yb + 1.5 * g
        cx_ = x + cw / 2 - 4
        c.saveState()
        c.translate(cx_, cy_)
        c.rotate(-20)
        trac(c, 1.6, NAVY)
        c.setFillColor(NAVY if k >= 2 else white)
        c.ellipse(-g * 0.78, -g * 0.55, g * 0.78, g * 0.55, stroke=1, fill=1)
        c.restoreState()
        if k >= 1:
            trac(c, 1.6, NAVY)
            c.line(cx_ + g * 0.74, cy_ + g * 0.1, cx_ + g * 0.74, cy_ + g * 3.4)
        par(c, x + 8, yt - 168, textos[k], 10.6, cw - 22, 13, SANS, INK)
    yt = Y(494)
    h = 150
    panell(c, M, yt, CW, h, 'BEN FETA I MAL FETA')
    ex = [(True, 'bé', 0), (False, 'massa petita', 1), (False, 'plica pel mig', 2), (False, 'creua dues línies', 3)]
    cw = (CW - 28) / 4.0
    for k, (ok, t, kind) in enumerate(ex):
        x = M + 14 + k * cw
        g = 9
        yb = pauta(c, x + 4, yt - 64, cw - 16, g, None, final=False)
        cx_ = x + cw / 2 - 4
        if kind == 0:
            nota_plica(c, cx_, yb + 1.5 * g, g, True)
        elif kind == 1:
            nota_plica(c, cx_, yb + 1.5 * g, g * 0.5, True)
        elif kind == 2:
            c.saveState()
            c.translate(cx_, yb + 1.5 * g)
            c.rotate(-20)
            trac(c, 1.5, NAVY)
            c.setFillColor(NAVY)
            c.ellipse(-g * 0.78, -g * 0.55, g * 0.78, g * 0.55, stroke=1, fill=1)
            c.restoreState()
            trac(c, 1.5, NAVY)
            c.line(cx_, yb + 1.5 * g, cx_, yb + 1.5 * g + g * 3.4)
        else:
            nota_plica(c, cx_, yb + 2 * g, g * 1.5, True)
        rr(c, x + cw / 2 - 40, yt - h + 12, 80, 22, 11, fill=NAVY if ok else white, lw=1.4, col=NAVY)
        txt(c, x + cw / 2, yt - h + 19, ('✓ ' if ok else '✗ ') + t, 10.2, SANSB, white if ok else NAVY, 'c')
    franja(c, M, Y(660), CW, 44, 'RECORDA', 'La nota s’asseu a la línia o dins de l’espai, i la plica fa tres espais.', 12)
    franja(c, M, Y(718), CW, 56, 'SABIES QUE?', 'La música escrita més antiga que es coneix té més de 3.000 anys: la van escriure sobre una tauleta d’argila!', 11.8)
    c.showPage()


def t23_jocs(c):
    pagina_jocs(c, 23, 'Dibuixo notes perfectes · a jugar!', 'Repassa amb el llapis.',
                'Ara toca practicar! Primer repassa els puntets i després dibuixa tu tot sol.')
    pila = Pila(Y(204))
    pw, x2 = meitats()
    h = 184
    yt = pila.pren(h)
    panell(c, M, yt, CW, h, 'REPASSA ELS PUNTETS', n=1)
    consigna(c, M + 14, yt - 40, 'Passa el llapis per sobre dels puntets, de dreta a esquerra i de dalt a baix.', CW - 28)
    g = 9
    yb = pauta(c, M + 20, yt - 86, CW - 40, g, None, final=True)
    for j in range(9):
        xx = M + 50 + j * 50
        pos = [1, 1.5, 2, 2.5, 3, 3.5, 4, 3, 2][j]
        nota_punts(c, xx, yb + (pos - 1) * g, g, amunt=pos < 3)
    g = 9
    yb = pauta(c, M + 20, yt - 146, CW - 40, g, None, final=True)
    for j in range(9):
        xx = M + 50 + j * 50
        pos = [2, 1.5, 3, 2.5, 1, 4, 3.5, 2, 1][j]
        nota_punts(c, xx, yb + (pos - 1) * g, g, amunt=pos < 3)
    h = 188
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'ESCRIU TU SOL', n=2)
    consigna(c, M + 14, yt - 40, 'Dibuixa 4 notes negres amb plica cap amunt i 4 amb plica cap avall.', pw - 28)
    pauta(c, M + 14, yt - 98, pw - 28, 8, None, final=True)
    pauta(c, M + 14, yt - 150, pw - 28, 8, None, final=True)
    panell(c, x2, yt, pw, h, 'QUIN ÉS L’ERROR?', n=3)
    consigna(c, x2 + 14, yt - 40, 'Marca amb una creu la nota mal dibuixada.', pw - 28)
    g = 8
    yb = pauta(c, x2 + 14, yt - 96, pw - 28, g, None, final=True)
    for j, (pos, am, mida) in enumerate([(2, True, 1.0), (3, True, 0.55), (2.5, False, 1.0), (4, False, 1.0)]):
        nota_plica(c, x2 + 54 + j * 44, yb + (pos - 1) * g, g * mida, am)
    h = 126
    yt = pila.pren(h)
    panell(c, M, yt, pw, h, 'VERITAT O FALS?', n=4)
    capcalera_vf(c, M + 14, yt - 34, pw - 14)
    veritat_fals(c, M + 14, yt - 50, pw - 14, ['La plica fa tres espais.', 'La nota creua dues línies.'], 12, 14.5)
    panell(c, x2, yt, pw, h, 'LA TEVA PRIMERA CANÇÓ', n=5)
    consigna(c, x2 + 14, yt - 40, 'Inventa una melodia de quatre notes i escriu-la aquí.', pw - 28)
    pauta(c, x2 + 14, yt - 84, pw - 28, 6, 'treble', final=True)
    c.showPage()
