# -*- coding: utf-8 -*-
"""Lliçó de prova del llibre «El meu llibre de piano, amb en Mussol Misol»:
   TEMA 3 · «Conec el DO, el RE i el MI» (4 pàgines A4 apaïsades, en català).

   Es genera en COLOR i en BLANC I NEGRE:  python3 llibre_prova.py
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from reportlab.lib.colors import HexColor, white               # noqa: E402

from dibujo_mano import W, H, ManoCanvas, texto, lineas_texto, letras_huecas      # noqa: E402
from llibre import (Estil, fons, titol, pestanya, peu, targeta, globus, caseta, numero,   # noqa: E402
                    par_text, teclat, pent_notes, ma_dreta, forma, traç, cap_nota, HA, FAT,
                    INK, NOTA_COLOR)
from mussol import mussol                                       # noqa: E402

TEMA = 'TEMA 3 · LES NOTES'
OUT = os.path.join(HERE, '..', 'output')


def estrella_f(c, st, cx, cy, r, nom='groc'):
    pts = []
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.46
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    traç(c, 2.0)
    c.setFillColor(st.f(nom))
    c.poly(pts, 1, 1)


def xip(c, st, x, y, w, nom, text, h=22, mida=13):
    forma(c, 'roundRect', x, y, w, h, 9, fill=st.f(NOTA_COLOR[nom]), lw=2.0)
    texto(c, x + w / 2, y + 6, text, mida, FAT if st.color else HA, 'c', col=white if st.color and nom not in ('groc',) else INK)


# ======================================================================== pàgina 1
def pag1(c, st):
    fons(c, st)
    pestanya(c, st, 'APRENC', TEMA)
    titol(c, st, 'CONEC EL DO, EL RE I EL MI', 498, 34)

    # en Mussol i la seva frase
    globus(c, 36, 376, 180, 78, ['Avui coneixerem', 'tres notes amigues!'], cua=(122, 344), mida=15, lead=19)
    mussol(c, 122, 240, 0.98, color=st.color)

    # A · on són al teclat
    targeta(c, st, 226, 318, 580, 154, 'On són al teclat?', 'blau')
    teclat(c, st, 244, 332, 270, 78, nb=7, resalta={0: 'vermell', 1: 'taronja', 2: 'groc'}, noms=True)
    items = [('vermell', 'El DO és la tecla blanca de l’esquerra de les DUES tecles negres.'),
             ('taronja', 'El RE és al mig de les dues tecles negres.'),
             ('groc', 'El MI és a la dreta de les dues tecles negres.')]
    yy = 432
    for nom, t in items:
        forma(c, 'circle', 540, yy + 4, 6.5, fill=st.f(nom), lw=1.8)
        yy = par_text(c, 554, yy, t, 12.5, 242, 14.5) - 8

    # B · on viuen al pentagrama
    targeta(c, st, 226, 126, 282, 180, 'On viuen al pentagrama?', 'verd')
    pos, yb = pent_notes(c, st, 240, 268, 254, 9, [('C4', 'w', 'DO'), ('D4', 'w', 'RE'), ('E4', 'w', 'MI')])
    for (nom, (cx, cy)) in zip(('DO', 'RE', 'MI'), pos):
        xip(c, st, cx - 24, 186, 48, nom, nom, 22, 14)
    for k, t in enumerate(['DO · sota el pentagrama, amb ratlleta', 'RE · just sota de la 1a línia',
                           'MI · a la 1a línia']):
        texto(c, 240, 166 - k * 17, t, 12.5, HA)

    # C · pugen com escalons
    targeta(c, st, 522, 126, 284, 180, 'Pugen com escalons', 'taronja')
    par_text(c, 536, 268, 'Cada nota és un escaló més amunt: el so es fa més AGUT.', 12.5, 130, 15)
    for k, (nom, hh) in enumerate((('DO', 30), ('RE', 52), ('MI', 74))):
        forma(c, 'rect', 682 + k * 38, 142, 38, hh, fill=st.f(NOTA_COLOR[nom]), lw=2.2)
        texto(c, 682 + k * 38 + 19, 148, nom, 12.5, FAT if st.color else HA, 'c', col=white if st.color and nom != 'MI' else INK)
    # sabies que?
    c.saveState()
    c.translate(600, 168)
    c.rotate(2.5)
    forma(c, 'roundRect', -62, -34, 128, 78, 10, fill=st.f('groc') if st.color else white, lw=2.2)
    texto(c, 2, 28, 'Sabies que?', 14, FAT if st.color else HA, 'c', col=INK)
    texto(c, 2, 12, 'Amb DO, RE i MI', 11.5, HA, 'c')
    texto(c, 2, -3, 'ja pots tocar', 11.5, HA, 'c')
    texto(c, 2, -18, 'cançons de veritat!', 11.5, HA, 'c')
    c.restoreState()

    # truc del Mussol
    forma(c, 'roundRect', 36, 58, 770, 56, 14, fill=white, lw=2.4)
    texto(c, 56, 92, 'El truc del Mussol', 15, FAT if st.color else HA)
    texto(c, 56, 72, 'Busca les DUES tecles negres que van juntes. El DO és la blanca que té just a l’esquerra.  Després, cap a la dreta: RE, MI!',
          12.5, HA)
    peu(c, st, 1)
    c.showPage()


# ======================================================================== pàgina 2
def pag2(c, st):
    fons(c, st)
    pestanya(c, st, 'PRACTICO', TEMA)
    titol(c, st, 'PRACTICO EL DO, EL RE I EL MI', 498, 34)

    # 1 · pinta les tecles
    targeta(c, st, 36, 266, 372, 198, 'Pinta les tecles', 'verd')
    numero(c, st, 392, 449, 1, 'verd')
    par_text(c, 50, 432, 'Pinta els DO de vermell, els RE de taronja i els MI de groc.', 12.5, 340, 15)
    teclat(c, st, 52, 306, 338, 88, nb=14)
    for k, (nom, t) in enumerate((('DO', 'DO'), ('RE', 'RE'), ('MI', 'MI'))):
        xip(c, st, 60 + k * 100, 276, 86, nom, t, 22, 13)

    # 2 · quina nota és
    targeta(c, st, 434, 266, 372, 198, 'Quina nota és?', 'blau')
    numero(c, st, 790, 449, 2, 'blau')
    texto(c, 448, 428, 'Escriu el nom de cada nota a la caseta.', 12.5, HA)
    pos, yb = pent_notes(c, st, 448, 408, 344, 8.5, [('E4', 'w', 'MI'), ('C4', 'w', 'DO'), ('D4', 'w', 'RE'),
                                                   ('C4', 'w', 'DO'), ('E4', 'w', 'MI'), ('D4', 'w', 'RE')])
    for (cx, cy) in pos:
        caseta(c, cx - 20, 318, 40, 24)
    texto(c, 448, 292, 'Ajuda:', 12.5, FAT if st.color else HA)
    for k, nom in enumerate(('DO', 'RE', 'MI')):
        xip(c, st, 500 + k * 64, 284, 56, nom, nom, 22, 13)

    # 3 · uneix amb fletxes
    targeta(c, st, 36, 56, 372, 198, 'Uneix amb fletxes', 'taronja')
    numero(c, st, 392, 239, 3, 'taronja')
    texto(c, 50, 222, 'Uneix cada nom amb la seva nota.', 12.5, HA)
    for k, nom in enumerate(('DO', 'RE', 'MI')):
        xip(c, st, 56, 168 - k * 52, 70, nom, nom, 28, 16)
    ordre = ['MI', 'DO', 'RE']
    alt = {'DO': 'C4', 'RE': 'D4', 'MI': 'E4'}
    for k, nom in enumerate(ordre):
        pent_notes(c, st, 250, 190 - k * 52 + 8, 130, 6.6, [(alt[nom], 'w', nom)], clau=False)
        forma(c, 'circle', 240, 177 - k * 52 + 8, 5, fill=white, lw=1.8)
    for k in range(3):
        forma(c, 'circle', 140, 182 - k * 52, 5, fill=white, lw=1.8)

    # 4 · veritat o falsedat
    targeta(c, st, 434, 56, 372, 198, 'Veritat o falsedat?', 'vermell')
    numero(c, st, 790, 239, 4, 'vermell')
    afirm = ["El DO és a l’esquerra de les dues tecles negres.", 'El MI viu a la 1a línia del pentagrama.',
             'El RE és més greu que el DO.', 'DO, RE, MI van pujant.']
    texto(c, 706, 220, 'V', 14, FAT if st.color else HA, 'c')
    texto(c, 760, 220, 'F', 14, FAT if st.color else HA, 'c')
    for k, t in enumerate(afirm):
        yy = 192 - k * 38
        par_text(c, 450, yy, t, 12, 244, 14)
        forma(c, 'circle', 706, yy - 2, 11, fill=white, lw=2.0)
        forma(c, 'circle', 760, yy - 2, 11, fill=white, lw=2.0)
    peu(c, st, 2)
    c.showPage()


# ======================================================================== pàgina 3
def pag3(c, st):
    fons(c, st)
    pestanya(c, st, 'TOCO', TEMA)
    titol(c, st, 'TOQUEM LES TRES NOTES!', 498, 34)

    # mà dreta
    targeta(c, st, 36, 282, 250, 188, 'La mà dreta', 'vermell')
    ma_dreta(c, st, 150, 348, 0.7)
    texto(c, 50, 300, '1 polze · 2 índex · 3 mig', 12, HA)
    texto(c, 50, 287, '4 anular · 5 menut', 12, HA)

    # teclat amb els dits
    targeta(c, st, 300, 282, 506, 188, 'Posa els dits al teclat', 'blau')
    par_text(c, 316, 432, 'Dit 1 sobre el DO, dit 2 sobre el RE i dit 3 sobre el MI. Els dits, rodonets, com si tinguessis una pilota a la mà!',
             12.5, 474, 15)
    teclat(c, st, 318, 298, 470, 88, nb=8, resalta={0: 'vermell', 1: 'taronja', 2: 'groc'}, noms=True,
           dits={0: '1', 1: '2', 2: '3'})

    # la cançó dels tres escalons
    targeta(c, st, 36, 56, 770, 214, 'La cançó dels tres escalons', 'taronja')
    notes = [('C4', 'q', 'DO'), ('D4', 'q', 'RE'), ('E4', 'q', 'MI'), ('D4', 'q', 'RE'),
             ('C4', 'q', 'DO'), ('D4', 'q', 'RE'), ('E4', 'h', 'MI'),
             ('E4', 'q', 'MI'), ('D4', 'q', 'RE'), ('C4', 'q', 'DO'), ('D4', 'q', 'RE'),
             ('C4', 'w', 'DO')]
    pos, yb = pent_notes(c, st, 100, 224, 500, 10, notes, compas=True, barres=(3, 6, 10))
    texto(c, 48, 160, 'dit', 13, FAT if st.color else HA)
    texto(c, 48, 128, 'nota', 13, FAT if st.color else HA)
    for (cx, cy) in pos:
        caseta(c, cx - 11, 152, 22, 22, 11)
        caseta(c, cx - 17, 118, 34, 24, 7)
    # com es toca
    par_text(c, 626, 226, 'Com es toca?', 15, 170, 16)
    pas = ['Compta 1-2-3-4 en veu alta.', 'Toca-la a poc a poc.', 'Repeteix-la una mica més ràpid!']
    yy = 204
    for k, t in enumerate(pas):
        numero(c, st, 636, yy + 4, k + 1, 'taronja', 9)
        yy = par_text(c, 652, yy, t, 12, 140, 14) - 12
    mussol(c, 740, 110, 0.3, color=st.color)
    peu(c, st, 3)
    c.showPage()


# ======================================================================== pàgina 4
def pag4(c, st):
    fons(c, st)
    pestanya(c, st, 'JUGUEM', TEMA)
    titol(c, st, 'JUGUEM I REPASSEM', 498, 34)

    # el joc
    targeta(c, st, 36, 262, 372, 208, 'El semàfor musical', 'taronja')
    passos = ['Fes tres targetes: DO vermell, RE taronja i MI groc (retalla les d’aquí sota!).',
              'Posa-les a terra, una mica separades.',
              'Algú toca una nota al piano. Corre i pisa la targeta que toca!',
              'Si encertes, guanyes un punt. Qui arriba a 5 guanya!']
    yy = 432
    for k, t in enumerate(passos):
        numero(c, st, 54, yy + 4, k + 1, 'taronja', 9)
        yy = par_text(c, 72, yy, t, 12, 318, 14.5) - 10

    # el repte
    targeta(c, st, 424, 262, 382, 208, 'El repte del Mussol', 'morat')
    par_text(c, 440, 432, 'Inventa la teva melodia amb DO, RE i MI. Escriu-hi les notes i toca-la!', 12.5, 350, 15)
    pent_notes(c, st, 440, 388, 350, 8.5, [], compas=True)
    traç(c, 1.6)
    for k in (1, 2, 3):
        bx = 440 + 70 + (350 - 70) * k / 4.0
        c.line(bx, 388, bx, 388 - 34)
    texto(c, 440, 316, 'Es diu:', 12.5, FAT if st.color else HA)
    traç(c, 1.2)
    c.setDash(1, 3)
    c.line(490, 314, 720, 314)
    c.setDash()
    mussol(c, 760, 304, 0.22, color=st.color)

    # targetes per retallar
    texto(c, 36, 232, '✂  Retalla per la línia de punts', 13, FAT if st.color else HA) if False else \
        texto(c, 36, 232, 'Retalla les targetes per la línia de punts', 13, FAT if st.color else HA)
    alt = {'DO': 'C4', 'RE': 'D4', 'MI': 'E4'}
    for k, nom in enumerate(('DO', 'RE', 'MI')):
        x = 36 + k * 124
        forma(c, 'roundRect', x, 64, 114, 152, 10, fill=white, lw=1.8, dash=(4, 3))
        forma(c, 'roundRect', x + 8, 72, 98, 136, 8, fill=st.f(NOTA_COLOR[nom]), lw=2.4)
        if st.color:
            from color_cat import lletres_blanques
            lletres_blanques(c, x + 57, 164, nom, 36)
        else:
            letras_huecas(c, x + 57, 164, nom, 36, rim=1.4, fat=1.1, giro=2, semilla=30 + k)
        pent_notes(c, st, x + 16, 140, 82, 5.4, [(alt[nom], 'w', nom)], clau=False)

    # ja ho sé
    targeta(c, st, 408, 56, 398, 190, 'Ja ho sé!', 'verd')
    llista = ['Sé trobar el DO, el RE i el MI al teclat.', 'Sé dir on viuen al pentagrama.',
              'Sé tocar la cançó dels tres escalons.']
    yy = 200
    for t in llista:
        yy2 = par_text(c, 426, yy, t, 12.5, 290, 15)
        estrella_f(c, st, 770, yy - 4, 14, 'groc')
        yy = yy2 - 18
    par_text(c, 426, 90, 'Pinta una estrella cada vegada que sàpigues fer-ho!', 12, 330, 14)
    peu(c, st, 4)
    c.showPage()


def genera(color):
    st = Estil(color)
    nom = os.path.join(OUT, 'Llibre_Prova_%s.pdf' % ('Color' if color else 'BN'))
    c = ManoCanvas(nom, pagesize=(W, H), seed=31, amp=0.8)
    c.setTitle('El meu llibre de piano · lliçó de prova')
    for f in (pag1, pag2, pag3, pag4):
        f(c, st)
    c.save()
    print('generat', nom)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    genera(True)
    genera(False)
