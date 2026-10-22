# -*- coding: utf-8 -*-
"""Peça 15 · Perfect (Ed Sheeran · arr. Nicki Allan, versió fàcil, MuseScore).
   MESURAT sobre el PDF (1 pàgina, A4; notes pintades amb colorear_notas.py): sense armadura, 12/8, sense tempo,
   amb digitació impresa (alguns números dins d'un cercle). Anacrusi de tres corxeres (Mi Re Do, dits 3-2-1) i
   14 compassos numerats en 4 sistemes (4+4+4+2). Repetició: «|:» després de l'anacrusi i «:|» al c. 4;
   caselles 1 (c. 4) i 2 (c. 5). Dreta: tres negres amb puntet + tres corxeres (Mi. Mi. Mi. Mi♪ Re♪ Do♪) als cc. 1-3;
   negres amb puntet i corxeres a la resta. Esquerra: acords de dues notes de blanca amb puntet
   (Do3+Sol3, Fa3+La3, Do3+Mi3...) en 12/8. Figura curta: corxera."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}
_qd = {'pitch': 'B4', 'dur': 'q.'}

SPEC = dict(
    num=15, slug='perfect', pdf='perfect.pdf', time_sig=(12, 8),
    titulo='Perfect',
    autor='Ed Sheeran · arr. Nicki Allan',
    kicker=kick(15, 'Perfect'), mes=MESES[15],
    yt=yt('perfect ed sheeran piano easy'),
    credito='Partitura: arr. Nicki Allan (MuseScore). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '12/8'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Corxera'), ('Compassos', '14 + anacrusi')],
        total=14,
        secciones=[('A', 1, 4, 'Primera vegada', AZUL),
                   ('B', 5, 8, 'Segona vegada: continua', OCRE),
                   ('C', 9, 12, 'Part central amb digitació', AZUL),
                   ('D', 13, 14, 'Final', OCRE)],
        ideas=[('EL COMPÀS', '4 vegades «1-2-3»',
                'Cada compàs té 12 corxeres, agrupades de tres en tres: es compten com quatre temps de «1-2-3».'),
               ('LA REPETICIÓ', 'Dues cases',
                'La primera vegada toques el c. 4 (casella 1) i repeteixes. La segona, salta al c. 5 (casella 2).'),
               ("L'ESQUERRA", 'Acords de dues notes',
                'Do+Sol, Fa+La… llargs i tranquils. Una mica de pes i res més.'),
               ('LA DIGITACIÓ', 'Números impresos',
                'Els dits són a la partitura. Alguns números estan dins d\'un cercle: segueix-los, són ajuda.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            "No hi ha armadura ni alteracions: només notes blanques.",
            'Compàs de 12/8: quatre grups de tres corxeres. Compta «1-2-3, 2-2-3, 3-2-3, 4-2-3».',
            'Comença amb una anacrusi: tres corxeres (Mi Re Do, dits 3-2-1).',
            'Hi ha una repetició amb dues cases: c. 4 (casella 1) i c. 5 (casella 2).',
            'La partitura porta dits impresos, alguns dins d\'un cercle.'],
        reto='Toca el compàs de 12/8 amb la mà esquerra suau i la dreta que canta.',
        truco="Compta «un-dos-tres, dos-dos-tres, tres-dos-tres, quatre-dos-tres» i no t'embolicaràs amb el 12/8.",
        sabias="«Perfect» és d'Ed Sheeran i va sortir l'any 2017. És una cançó d'amor que molta gent ha ballat en casaments.",
        qr_texto='Escolta-la i imagina un vals lent amb la partitura al davant.',
        ts=(12, 8),
        cuenta_titulo='Com es compta el 12/8',
        cuenta_pie="Tres negres amb puntet + tres corxeres: «1-2-3, 2-2-3, 3-2-3, 4-i-5». Aquí només el ritme.",
        ritmos=[('EL COMPÀS 1', '12/8 · tres negres amb puntet + tres corxeres',
                 [_qd, _qd, _qd, _e(0), _e(0), _e(0)], OCRE, 'treble', None),
                ("L'ANACRUSI", 'tres corxeres: 2-i-3',
                 [_e(0), _e(0), _e(0)], AZUL, 'treble', None)]),
    manos=dict(
        izq=[('Do+Sol junts', "Dit 5 al Do i dit 1 al Sol (o dits 3 i 1): prem tots dos alhora."),
             ('Fa+La', 'Un altre acord de dues notes: dits 5 i 2 (o 3 i 1). Mira la digitació impresa.'),
             ('Notes de blanca amb puntet', 'Cada acord dura sis corxeres: «1-2-3, 4-5-6». Aguanta!'),
             ('Canvis suaus', "Quan canvia l'acord, la mà es mou suaument, sense salts.")],
        der=[('Mi Re Do', 'Anacrusi: tres corxeres que baixen amb els dits 3-2-1.'),
             ('Mi. Mi. Mi. Mi♪ Re♪ Do♪', 'Cc. 1-3: tres negres amb puntet i tres corxeres. Compta «1-2-3, 2-2-3, 3-2-3, 4-i-5».'),
             ('Les cases', 'La primera vegada, toca la casella 1 i torna al «|:». La segona, salta a la casella 2.'),
             ('Els números en cercle', 'Segueix els dits impresos: són els que ajuden a canviar de posició.')],
        tecnica=['Compta sempre els quatre temps de «1-2-3».',
                 "La mà esquerra suau: la melodia de la dreta ha de cantar.",
                 'Mira els dits impresos abans de tocar.']),
    bloques=[
        B(1, 'anacrusi + cc. 1-4', 'La primera frase', (0, 0),
          D('cadena', 'Entra i repeteix',
            [('anacrusi: Mi Re Do', False), ('cc. 1-3', False), ('c. 4: casella 1', False), (':| torna', True)]),
          [('IZQUIERDA', 'Do+Sol, Do+Fa... Un acord per compàs. La mà esquerra comença al c. 1.'),
           ('DERECHA', 'Anacrusi: Mi Re Do. Cc. 1-3: Mi. Mi. Mi. Mi♪ Re♪ Do♪. C. 4: Fa Mi Do...'),
           ('JUNTAS', 'Compta «1-2-3» quatre cops per compàs. Les dues mans junts.'),
           ('OJO', 'Al final del c. 4 hi ha «:|»: torna al «|:» del principi.')]),
        B(2, 'cc. 5-8', 'Segona vegada', (1, 1),
          D('cadena', 'Casella 2 → nova melodia',
            [('c. 5: casella 2', False), ('c. 6', False), ('c. 7', False), ('c. 8', True)]),
          [('IZQUIERDA', 'Acords de dues notes: Do+Fa, Do+Sol, Fa+La. Segueix els dits impresos.'),
           ('DERECHA', 'C. 5: Mi... C. 6: La Do i corxeres. Cc. 7-8: la melodia puja amb ritme de negra amb puntet.'),
           ('JUNTAS', 'La dreta puja, l\'esquerra aguanta l\'acord.'),
           ('OJO', 'La casella 2 substitueix el c. 4. Només la segona vegada!')]),
        B(3, 'cc. 9-12', 'La part central', (2, 2),
          D('cadena', 'Digitació i canvis',
            [('c. 9', False), ('c. 10', False), ('c. 11', False), ('c. 12', True)]),
          [('IZQUIERDA', 'Acords més variats: Do+Mi, Do+Sol, Si+Sol... Sempre dues notes.'),
           ('DERECHA', 'Notes llargues i corxeres. Segueix els dits en cercle.'),
           ('JUNTAS', 'La dreta fa la melodia i l\'esquerra marca els acords. Mira els números!'),
           ('OJO', 'Els números dins d\'un cercle són ajudes: segueix-los.')]),
        B(4, 'cc. 13-14', 'Final i tota la peça', (3, 3),
          D('cadena', 'El final',
            [('c. 13', False), ('c. 14: final', True)]),
          [('IZQUIERDA', 'Acord final: Do+Mi+Sol llarg. Deixa que soni.'),
           ('DERECHA', 'Cc. 13-14: la melodia baixa i acaba amb una nota llarga (Do).'),
           ('JUNTAS', 'Toca tota la peça des de l\'anacrusi, amb la repetició.'),
           ('A TEMPO', 'Lent i tendre, com una cançó d\'amor. Només al final, respira.')]),
    ],
    lista=['Compto el 12/8 de «1-2-3» en veu alta.',
           "Toco l'anacrusi (Mi Re Do).",
           'Faig la repetició amb les dues cases.',
           "Segueixo els dits impresos.",
           'Toco tota la peça sense parar.'],
    cortes={1: [214.5, 363.0, 514.2]}, inicio={1: 88}, fin={1: 665},
    burb={
        0: [('arriba', 262, 'DER', 'Anacrusi: Mi Re Do (dits 3-2-1). Compta «2-3» i entra.', 0.07),
            ('arriba', 262, 'OJO', 'Repetició: de «|:» a «:|». Casella 1 a la primera vegada.', 0.55)],
        1: [('arriba', 262, 'OJO', 'Casella 2: només a la segona vegada, en lloc del c. 4.', 0.1),
            ('arriba', 262, 'DER', 'Les corxeres pugen: «1-i-2». Mira els dits impresos.', 0.55)],
        2: [('arriba', 262, 'AMB', 'Dits en cercle: ajuda per a canviar de posició.', 0.1)],
        3: [('arriba', 262, 'OJO', 'Final: l\'acord Do+Mi+Sol, quatre temps de «1-2-3». Deixa sonar!', 0.5)],
    },
    misol=dict(
        manos="El 12/8 sona com un balanceig suau: un-dos-tres, dos-dos-tres... com si algú et gronxés.",
        guia="Les dues cases (1. i 2.) són dues sortides de la repetició. La primera vegada, per la 1; la segona, per la 2.",
        pauta="Escriu a la pauta un compàs de 12/8 amb tres negres amb puntet, i pinta les notes."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu tres negres amb puntet i tres corxeres")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_perfect.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
