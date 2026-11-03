# -*- coding: utf-8 -*-
"""Fulls per pintar en blanc i negre, en català, amb traç fet a mà (A4 apaïsat).

   1  El teclat de les notes      4  Pinta el ritme
   2  Les tecles del piano        5  Presentem en Mussol Misol
   3  Pinta la melodia

   Les altures de les notes surten de `engine/notation.note_y`, no a ull.
   Es genera amb:  python3 pintar_cat.py  ->  ../output/Pintar_Catala_BN.pdf
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
sys.path.insert(0, HERE)
import notation as nt                                           # noqa: E402
from reportlab.lib.colors import black, white                  # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth           # noqa: E402

from mussol import mussol                                       # noqa: E402
from dibujo_mano import (W, H, ManoCanvas, trazo, texto, letras_huecas, caja, marco,  # noqa: E402
                         estrella, cabeza, negra_deco, pareja_deco, pareja_plana, corchete,
                         sol, nube, arcoiris, pentagrama, cabeza_redonda, rayita,
                         subrayado_ondulado, flecha, lineas_texto)

OUT = os.path.join(HERE, '..', 'output', 'Pintar_Catala_BN.pdf')
SK, HA = 'Sketch', 'Hand'

# (nom, altura, color amb què es pinta la tecla)
NOTES = [('DO', 'C4', 'VERMELL'), ('RE', 'D4', 'TARONJA'), ('MI', 'E4', 'GROC'),
         ('FA', 'F4', 'VERD'), ('SOL', 'G4', 'BLAU'), ('LA', 'A4', 'MORAT'),
         ('SI', 'B4', 'GRIS'), ('DO', 'C5', 'VERMELL')]


def nom_peu(c, extra=''):
    texto(c, 40, 30, 'Nom:', 15, HA)
    trazo(c, 1.2, cap=0)
    c.setDash(1, 3)
    c.line(80, 28, 250, 28)
    c.setDash()
    if extra:
        texto(c, W - 40, 30, extra, 11, HA, 'r')


# ---------------------------------------------------------------- full 1: el teclat
def full_teclat(c):
    marco(c)
    c.saveState()
    c.translate(W / 2, 480)
    c.rotate(-1.2)
    letras_huecas(c, 0, 26, 'EL TECLAT DE', 50, semilla=5)
    letras_huecas(c, 0, -24, 'LES NOTES', 50, semilla=9)
    c.restoreState()
    sol(c, 98, 498, 36)
    nube(c, 752, 494, 1.05)
    estrella(c, 190, 446, 16)
    estrella(c, 668, 452, 13, 0.3)
    negra_deco(c, 62, 396, 1.0, corchea=True)
    pareja_deco(c, 112, 420, 0.8)
    negra_deco(c, 735, 398, 1.0)
    negra_deco(c, 785, 404, 0.9, corchea=True)

    arcoiris(c, W / 2, 296, 372, 128, bandas=6, paso=17)

    kw, gp = 88, 8.7
    x0 = (W - (8 * kw + 7 * gp)) / 2
    ytop, ybot = 292, 128
    for i, (nom, alt, color) in enumerate(NOTES):
        x = x0 + i * (kw + gp)
        caja(c, x, ybot - 8, kw, ytop - ybot, r=11, lw=2.6)
        caja(c, x, ybot, kw, ytop - ybot, r=11, lw=2.8)
        letras_huecas(c, x + kw / 2, ytop - 54, nom, 32 if len(nom) < 3 else 27, rim=1.5, fat=1.1,
                      sep=1.6, giro=3, semilla=20 + i)
        gap = 7.4
        yb = pentagrama(c, x + 10, ybot + 56, kw - 20, gap)
        nt.draw_clef(c, x + 11, yb, gap)
        ny = nt.note_y(yb, gap, alt)
        nx = x + kw - 27
        if alt == 'C4':
            rayita(c, nx, ny, gap * 0.95)
        cabeza_redonda(c, nx, ny, gap * 1.15)
        caja(c, x + 6, 84, kw - 12, 24, r=9, lw=1.8)
        texto(c, x + kw / 2, 91, color, 12.5, HA, 'c')

    estrella(c, 48, 66, 13)
    estrella(c, W - 50, 62, 15, 0.2)
    texto(c, W / 2, 58, 'Pinta cada tecla del color que diu l’etiqueta... i l’arc de Sant Martí també!',
          15, HA, 'c')
    nom_peu(c)
    c.showPage()


# ------------------------------------------------------ full 2: les tecles del piano
def full_piano(c):
    marco(c)
    c.saveState()
    c.translate(W / 2, 512)
    c.rotate(-0.8)
    letras_huecas(c, 0, 0, 'LES TECLES DEL PIANO', 40, semilla=4)
    c.restoreState()
    subrayado_ondulado(c, 240, 600, 494)
    estrella(c, 70, 500, 15)
    estrella(c, W - 70, 505, 13, 0.3)
    pareja_deco(c, W - 130, 430, 0.8)
    negra_deco(c, 50, 392, 0.85)

    pasos = [('1', 'Pinta de BLAU els grups de DUES tecles negres.'),
             ('2', 'Pinta de VERD els grups de TRES tecles negres.'),
             ('3', 'Pinta de VERMELL totes les tecles DO (a l’esquerra de les dues negres).'),
             ('4', 'Escriu a cada casella el nom de la nota.')]
    yy = 468
    for n_, t in pasos:
        trazo(c, 2.2)
        c.setFillColor(white)
        c.circle(86, yy + 4, 11, stroke=1, fill=1)
        texto(c, 86, yy, n_, 15, HA, 'c')
        texto(c, 106, yy - 1, t, 16, HA)
        yy -= 29

    nb = 14
    kx0, kw = 40, (W - 80) / nb
    ytop, ybot = 330, 190
    trazo(c, 2.2)
    for i in range(nb):
        c.setFillColor(white)
        c.roundRect(kx0 + i * kw, ybot, kw, ytop - ybot, 5, stroke=1, fill=1)
    for octv in range(2):
        for p_ in (0, 1, 3, 4, 5):
            i = octv * 7 + p_
            bx = kx0 + (i + 1) * kw - 0.31 * kw
            trazo(c, 2.4)
            c.setFillColor(white)
            c.roundRect(bx, ytop - 92, 0.62 * kw, 92, 4, stroke=1, fill=1)
    noms = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'] * 2
    for i, nm in enumerate(noms):
        x = kx0 + i * kw + 4
        caja(c, x, 150, kw - 8, 30, r=8, lw=1.6, dash=(3, 2))
        if nm == 'DO':
            letras_huecas(c, x + (kw - 8) / 2, 158, 'DO', 15, rim=1.0, fat=0.9, sep=1.0, giro=3,
                          semilla=40 + i)
    texto(c, W / 2, 128, 'El DO ja està escrit! Continua tu: RE, MI, FA, SOL, LA, SI... i un altre cop DO, RE, MI.',
          13, HA, 'c')
    flecha(c, 150, 138, 82, 168, curva=-10)

    caja(c, 40, 50, 590, 66, r=12, lw=2.0)
    texto(c, 100, 97, 'El truc d’en Mussol Misol', 16, HA)
    texto(c, 100, 80, 'Al piano les tecles negres van en grups de DUES i de TRES.', 13, HA)
    texto(c, 100, 64, 'El DO és sempre la tecla blanca just ABANS de les dues negres.', 13, HA)
    mussol(c, 70, 86, 0.2)
    estrella(c, 700, 92, 14)
    estrella(c, 752, 70, 10, 0.4)
    negra_deco(c, 790, 60, 0.9)
    nom_peu(c)
    c.showPage()


# --------------------------------------------------------- full 3: pinta la melodia
def full_melodia(c):
    marco(c)
    c.saveState()
    c.translate(W / 2, 526)
    c.rotate(0.9)
    letras_huecas(c, 0, 0, 'PINTA LA MELODIA', 40, semilla=8)
    c.restoreState()
    sol(c, 80, 520, 22)
    nube(c, W - 90, 516, 0.7)

    texto(c, W / 2, 484, 'Pinta cada nota del color de la seva tecla i escriu-ne el nom a la casella.',
          15, HA, 'c')
    tw, tg = 84, 7
    tx0 = (W - (8 * tw + 7 * tg)) / 2
    for i, (nm, alt, color) in enumerate(NOTES):
        x = tx0 + i * (tw + tg)
        caja(c, x, 436, tw, 42, r=9, lw=1.8)
        texto(c, x + tw / 2, 460, nm, 15, HA, 'c')
        texto(c, x + tw / 2, 443, color, 10.5, HA, 'c')

    gap = 9.5
    linies = [
        (396, ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'], 'Puja per l’escala'),
        (276, ['E4', 'D4', 'C4', 'D4', 'E4', 'E4', 'E4'], 'Baixa i puja'),
        (150, ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4'], 'Quina cançó és?'),
    ]
    for k, (ytop, notes, etiqueta) in enumerate(linies):
        texto(c, 44, ytop + 15, '%d · %s' % (k + 1, etiqueta), 16, HA)
        if k == 2:
            trazo(c, 1.2, cap=0)
            c.setDash(1, 3)
            c.line(250, ytop + 13, 440, ytop + 13)
            c.setDash()
            texto(c, 452, ytop + 15, 'Pista: es canta de nit, mirant el cel.', 14, HA)
        yb = pentagrama(c, 44, ytop, W - 88, gap)
        nt.draw_clef(c, 50, yb, gap)
        pas = (W - 88 - 90) / 8.0
        for kk, alt in enumerate(notes):
            nx = 44 + 96 + kk * pas + pas / 2 - 10
            ny = nt.note_y(yb, gap, alt)
            if alt == 'C4':
                rayita(c, nx, ny, gap)
            cabeza_redonda(c, nx, ny, gap * 1.1)
            caja(c, nx - 22, yb - 47, 44, 22, r=7, lw=1.4, dash=(3, 2))
    estrella(c, W - 60, 60, 14)
    negra_deco(c, W - 120, 46, 0.7, corchea=True)
    pareja_deco(c, 300, 40, 0.65)
    nom_peu(c)
    c.showPage()


# ------------------------------------------------------------ full 4: pinta el ritme
def figura(c, tipus, cx, base, s=1.0):
    if tipus == 'w':
        cabeza_redonda(c, cx, base, 13 * s)
        return
    cabeza(c, cx, base, 11 * s, 7.8 * s, giro=-20, grosor=2.2, rayada=(tipus in ('q', 'e')))
    trazo(c, 2.6, cap=0)
    c.line(cx + 10 * s, base + 2 * s, cx + 10 * s, base + 46 * s)
    if tipus == 'e':
        corchete(c, cx + 10 * s, base + 46 * s, 1.3 * s)


def linia_ritme(c, x0, yc, bw, compassos, titol):
    trazo(c, 1.6, cap=0)
    c.line(x0, yc, x0 + 4 * bw, yc)
    for b in range(5):
        c.line(x0 + b * bw, yc + 20, x0 + b * bw, yc - 20)
    trazo(c, 3.2, cap=0)
    c.line(x0 + 4 * bw - 4, yc + 20, x0 + 4 * bw - 4, yc - 20)
    texto(c, x0, yc + 54, titol, 16, HA)
    temps = {'w': 4, 'h': 2, 'q': 1, 'ee': 1}
    for b, comp in enumerate(compassos):
        total = sum(temps[f] for f in comp)
        ample = bw - 40
        xx = x0 + b * bw + 22
        for f in comp:
            dur = temps[f]
            tam = dur * ample / total
            if f == 'ee':
                pareja_plana(c, xx + tam / 2 - 25, yc, 0.9)
            else:
                figura(c, f, xx + tam / 2 - 4, yc, 0.95)
            xx += tam


def full_ritme(c):
    marco(c)
    c.saveState()
    c.translate(W / 2, 524)
    c.rotate(-0.8)
    letras_huecas(c, 0, 0, 'PINTA EL RITME', 40, semilla=2)
    c.restoreState()
    sol(c, 80, 520, 22)
    mussol(c, W - 62, 496, 0.22)
    texto(c, W / 2, 486, 'Tria un color per a cada figura, pinta’n la rodona i després les figures de sota.',
          15, HA, 'c')

    figs = [('w', 'RODONA', '4 temps'), ('h', 'BLANCA', '2 temps'),
            ('q', 'NEGRA', '1 temps'), ('e', 'CORXERA', 'mig temps')]
    cw, cg = 180, 14
    cx0 = (W - (4 * cw + 3 * cg)) / 2
    for i, (tp, nm, gl) in enumerate(figs):
        x = cx0 + i * (cw + cg)
        caja(c, x, 346, cw, 124, r=12, lw=2.2)
        texto(c, x + 14, 446, nm, 18, HA)
        texto(c, x + 14, 428, gl, 13, HA)
        figura(c, tp, x + 36, 370, 1.0)
        nb = {'w': 4, 'h': 2, 'q': 1, 'e': 1}[tp]
        for k in range(nb):
            trazo(c, 1.6)
            c.setFillColor(white)
            if tp == 'e':
                c.circle(x + 78, 378, 6, stroke=1, fill=1)
                c.line(x + 78, 372, x + 78, 384)
            else:
                c.circle(x + 78 + k * 15, 378, 6, stroke=1, fill=1)
        trazo(c, 2.0)
        c.setFillColor(white)
        c.circle(x + cw - 30, 392, 13, stroke=1, fill=1)
        texto(c, x + cw - 34, 366, 'el meu color', 10, HA, 'c')

    ritmes = [
        [['q', 'q', 'h'], ['w'], ['h', 'q', 'q'], ['ee', 'ee', 'h']],
        [['ee', 'ee', 'q', 'q'], ['h', 'q', 'q'], ['q', 'ee', 'q', 'q'], ['w']],
    ]
    bw = (W - 100) / 4.0
    linia_ritme(c, 50, 272, bw, ritmes[0], 'Ritme 1')
    linia_ritme(c, 50, 168, bw, ritmes[1], 'Ritme 2')

    yc = 66
    trazo(c, 1.6, cap=0)
    c.line(50, yc, 50 + 4 * bw, yc)
    for b in range(5):
        c.line(50 + b * bw, yc + 20, 50 + b * bw, yc - 20)
    trazo(c, 3.2, cap=0)
    c.line(50 + 4 * bw - 4, yc + 20, 50 + 4 * bw - 4, yc - 20)
    texto(c, 50, yc + 28, 'Ritme 3 · Inventa el teu! Dibuixa figures (cada compàs suma QUATRE temps) i pinta-les.',
          15, HA)
    nom_peu(c)
    c.showPage()


# ------------------------------------------------- full 5: presentem en Mussol Misol
def full_mussol(c):
    marco(c)
    c.saveState()
    c.translate(W / 2, 520)
    c.rotate(-1.0)
    letras_huecas(c, 0, 0, 'EN MUSSOL MISOL', 46, semilla=6)
    c.restoreState()
    texto(c, W / 2, 490, 'el teu amic del piano', 19, HA, 'c')
    subrayado_ondulado(c, 330, 512, 482)

    # el mussol, gran, a l'esquerra
    mussol(c, 205, 262, 1.2)
    estrella(c, 60, 420, 15)
    estrella(c, 342, 330, 11, 0.3)
    negra_deco(c, 62, 130, 1.1, corchea=True)
    pareja_deco(c, 330, 150, 0.9)
    estrella(c, 44, 300, 10, 0.5)
    flecha(c, 118, 82, 148, 112, curva=14)
    texto(c, 40, 66, 'Pinta’l com tu vulguis!', 17, HA)

    # globus de conversa
    bx, by, bw_, bh = 392, 392, 400, 78
    caja(c, bx, by, bw_, bh, r=22, lw=2.4)
    c.setFillColor(white)
    trazo(c, 2.4)
    c.poly([(bx + 24, by + 3), (bx + 72, by + 3), (bx - 12, by - 24)], 1, 1)
    c.setStrokeColor(white)
    c.setLineWidth(3.2)
    c.line(bx + 28, by + 3, bx + 68, by + 3)
    texto(c, bx + 24, by + 50, 'Hola, colla! Sóc en Mussol Misol', 20, HA)
    texto(c, bx + 24, by + 26, 'i us ensenyaré a tocar el piano.', 17, HA)

    # fitxa
    fx, fy, fw, fh = 392, 100, 400, 256
    caja(c, fx, fy, fw, fh, r=14, lw=2.4)
    texto(c, fx + 20, fy + fh - 34, 'LA MEVA FITXA', 24, SK)
    subrayado_ondulado(c, fx + 20, fx + 200, fy + fh - 44, amp=2, lam=16, lw=1.8)
    files = [('Em dic:', 'Mussol Misol'),
             ('Sóc:', 'un mussol que adora la música'),
             ('El meu instrument:', 'el piano')]
    yy = fy + fh - 74
    for et, val in files:
        texto(c, fx + 20, yy, et, 16, HA)
        texto(c, fx + 20 + stringWidth(et, HA, 16) + 8, yy, val, 15, HA)
        trazo(c, 1.0, cap=0)
        c.setDash(1, 3)
        c.line(fx + 20, yy - 6, fx + fw - 20, yy - 6)
        c.setDash()
        yy -= 30
    # el seu nom, fet de notes
    texto(c, fx + 20, yy - 6, 'El meu nom sona com dues notes:', 16, HA)
    gap = 6.6
    yb = pentagrama(c, fx + 20, fy + 70, 188, gap)
    nt.draw_clef(c, fx + 22, yb, gap)
    for k, alt in enumerate(['E4', 'G4']):
        nx = fx + 98 + k * 52
        cabeza_redonda(c, nx, nt.note_y(yb, gap, alt), gap * 1.1)
    for k, (nm, xk) in enumerate([('MI', fx + 98), ('SOL', fx + 150)]):
        letras_huecas(c, xk, fy + 12, nm, 21, rim=1.2, fat=1.0, sep=1.4, giro=3, semilla=70 + k)
    texto(c, fx + 218, fy + 50, 'MI + SOL = MISOL!', 16, HA)
    nom_peu(c)
    c.showPage()


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    c = ManoCanvas(OUT, pagesize=(W, H), seed=17, amp=0.9)
    c.setTitle('Fulls per pintar · El teclat de les notes')
    for f in (full_teclat, full_piano, full_melodia, full_ritme, full_mussol):
        f(c)
    c.save()
    print('generat', OUT)


if __name__ == '__main__':
    main()
