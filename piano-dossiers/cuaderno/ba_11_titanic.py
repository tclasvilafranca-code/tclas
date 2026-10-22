# -*- coding: utf-8 -*-
"""Peça 11 · Titanic (My Heart Will Go On), James Horner; arranjament d'Ana Cristina Escobés.
   MESURAT sobre el PDF (1 pagina A4 vertical, vectorial; 23 compassos en 5 sistemes de 4, 6, 4, 4
   i 5): cap armadura ni alteracio (Do major: acaba en Do), 2/4, «Adagio» sense metronom, matisos
   mp al c. 1 i mf al c. 11, crescendo cc. 9-10 i diminuendo cc. 21-23, semicorxera com a figura
   mes curta (corxera amb puntet + semicorxera als cc. 1 i 5). Repeticions: barra de repeticio al
   final del c. 8 (torna al c. 1; casella 1 = cc. 7-8, casella 2 = cc. 9-10) i una altra al final
   del c. 18 (torna al |: del c. 11; casella 1 = cc. 16-18, casella 2 = cc. 19-23): se'n toquen 34.
   Dreta: Sol4-Sol5, corxeres i negres, blanques lligades als cc. 7-8 i 22-23. Esquerra: blanques
   Do3-Sol3-Fa3-Sol3 (cc. 1-10) i, des del c. 11, parelles de negres nota greu + quinta (La3-Mi4,
   Sol3-Re4, Fa3-Do4), amb Do4, Re4 i Mi4 sobre la pauta; c. 22 Do4 i c. 23 Do3. Sense digitacio."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_RITMO_C1 = [{'pitch': 'C5', 'dur': 'e.', 'beam': 0}, {'pitch': 'C5', 'dur': 's', 'beam': 0},
             {'pitch': 'C5', 'dur': 'e', 'beam': 1}, {'pitch': 'C5', 'dur': 'e', 'beam': 1}]
_QUINTA = [{'pitch': 'A3', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}]

SPEC = dict(
    num=11, slug='titanic', pdf='titanic.pdf', time_sig=(2, 4),
    titulo='Titanic',
    autor="James Horner · «My Heart Will Go On» · arranjament d'Ana Cristina Escobés",
    kicker='Alba · peça 11 · Titanic', mes='Maig · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=titanic+my+heart+will+go+on+piano+easy',
    credito="Partitura: arr. Ana Cristina Escobés (El Cuarto del Piano). Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '2/4'), ('Caràcter', 'Adagio'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '23')],
        total=23,
        secciones=[('A', 1, 10, 'El tema', AZUL), ('B', 11, 23, 'La part que puja', OCRE)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('LA DRETA', 'La melodia',
                'Corxeres i negres, i dues blanques lligades. Va de Sol a Sol agut.'),
               ("L'ESQUERRA", 'Blanques i quintes',
                'Una blanca per compàs. Des del c. 11, una nota greu i la seva quinta.'),
               ('EL BAIX', 'Do · Sol · Fa · Sol',
                'Quatre notes greus que tornen sempre. Als cc. 11-14 el Do canvia per un La.'),
               ('LES REPETICIONS', 'Dues vegades',
                'El c. 8 torna al c. 1 i el c. 18 torna al c. 11. Cada cop, una casella.')],
        ideas_pie='Matisos impresos: mp (c. 1) = una mica suau; mf (c. 11) = una mica fort.',
        especial=[
            'Sense armadura ni alteracions: només tecles blanques (Do major).',
            'Compàs de 2/4: dos temps. «Adagio» vol dir molt lent; no porta metrònom.',
            'Al c. 1: corxera amb puntet i semicorxera. És el ritme més difícil.',
            'Matisos: mp (c. 1), crescendo (cc. 9-10), mf (c. 11), diminuendo (cc. 21-23).',
            'Repeticions: el c. 8 torna al c. 1 i el c. 18 torna al c. 11. Se\'n toquen 34.',
            "L'esquerra puja sobre la pauta: Do, Re i Mi amb ratlletes addicionals."],
        reto='Que el crescendo dels cc. 9-10 arribi suau al mf del c. 11, sense córrer. '
             "T'hi atreveixes?",
        truco="Primer la dreta, cantant la melodia. Després l'esquerra, nota a nota. Les dues "
              'mans, al final.',
        sabias='«My Heart Will Go On» és la cançó de la pel·lícula «Titanic» (1997). La va '
               "cantar Céline Dion, la va compondre James Horner i va guanyar l'Oscar a la "
               'millor cançó original.',
        qr_texto='Escolta-la amb la partitura al davant i segueix el ritme de la dreta.',
        ts=(2, 4), cuenta_titulo='Un compàs de cada mà',
        cuenta_pie='Dreta: el ritme del c. 1, sobre un Do. Esquerra: nota greu i quinta, com '
                   'al c. 11.',
        ritmos=[('LA DRETA', 'c. 1 · corxera amb puntet + semicorxera', _RITMO_C1, AZUL,
                 'treble', None),
                ("L'ESQUERRA", 'c. 11 · nota i quinta', _QUINTA, OCRE, 'bass', None)]),
    manos=dict(
        izq=[('Blanques', 'Cc. 1-10: una blanca per compàs. Do, Sol, Fa, Sol. Compta 1-2 i '
                          'aguanta-la.'),
             ('Nota i quinta', 'Des del c. 11: La-Mi, Sol-Re, Fa-Do. Toca la greu i, tot seguit, '
                               'la de dalt.'),
             ('Notes amb ratlletes', 'Do, Re i Mi de dalt (cc. 11-22) van per sobre de la '
                                     'pauta. Mira-ho abans de tocar.'),
             ('El final', 'C. 22: Do (de dalt). C. 23: Do (de baix). Acaba sense pressa.')],
        der=[('Canta-la', "És la melodia d'una cançó que coneixes. Canta-la abans de tocar-la."),
             ('Corxera amb puntet', 'Cc. 1 i 5: la corxera amb puntet i la semicorxera valen un '
                                    'temps. Toca el Do a poc a poc.'),
             ('Silenci i salt', 'Cc. 2, 3, 6, 16, 19 i 20: compta 1-i-2-i. El silenci cau al 2 i '
                                'la nota entra a la «i».'),
             ('Blanques lligades', 'Cc. 7-8 (Sol) i 22-23 (Do): toca la primera i aguanta quatre '
                                   'temps.')],
        tecnica=['Adagio: molt a poc a poc i amb el braç relaxat.',
                 "La dreta canta (mp) i l'esquerra acompanya més fluix.",
                 'Compta 1-2 en veu alta i respira a cada frase.']),
    bloques=[
        B(1, 'cc. 1-4', "La frase d'entrada", (0, 0),
          D('cadena', 'El ritme del c. 1',
            [('corxera amb puntet', False), ('semicorxera', False), ('2 corxeres', True)]),
          [('IZQUIERDA', 'Una blanca per compàs: Do, Sol, Fa, Sol. Compta 1-2.'),
           ('DERECHA', 'C. 1: quatre Do seguits. C. 2: Si-Do, silenci i Do. C. 4: Mi, Re.'),
           ('JUNTAS', 'Compta 1-2 i entren les dues mans. Un compàs cada cop.'),
           ('OJO', 'Mp al c. 1: toca suau. Als cc. 2 i 3 el silenci cau al 2.')]),
        B(2, 'cc. 5-10', 'Repetició i caselles', (1, 1),
          D('cadena', 'Les dues caselles',
            [('cc. 5-6', False), ('casella 1: cc. 7-8', False), ('torna al c. 1', False),
             ('casella 2: cc. 9-10', True)]),
          [('IZQUIERDA', 'Do, Sol, Fa, Sol (cc. 5-8) i Fa, Sol (cc. 9-10). Blanques.'),
           ('DERECHA', 'Cc. 5-6 com el principi. Cc. 7-8: Sol lligat. Cc. 9-10: Sol, La, Si.'),
           ('JUNTAS', 'Cc. 5-8, torna al c. 1 i la segona vegada salta als cc. 9-10.'),
           ('OJO', 'Crescendo als cc. 9-10: puja el volum fins al mf del c. 11.')]),
        B(3, 'cc. 11-14', 'La part que puja', (2, 2),
          D('cadena', "L'esquerra: nota i quinta",
            [('La - Mi', False), ('Sol - Re', False), ('Fa - Do', False), ('Sol - Re', True)]),
          [('IZQUIERDA', 'La-Mi, Sol-Re, Fa-Do, Sol-Re: nota greu i la seva quinta, en negres.'),
           ('DERECHA', 'C. 11: Do. C. 12: Re i Sol. Cc. 13-14: Sol-Fa-Mi i Re-Mi-Fa.'),
           ('JUNTAS', 'Un compàs cada cop. A l\'esquerra, dos temps: greu i quinta.'),
           ('OJO', 'Mf al c. 11: més volum! El Sol del c. 13 és la nota més aguda.')]),
        B(4, 'cc. 15-18', 'Torna i primera casella', (3, 3),
          D('cadena', 'El camí',
            [('c. 15', False), ('casella 1: cc. 16-18', False), ('torna al c. 11', True)]),
          [('IZQUIERDA', 'La-Mi, Sol-Re, Fa-Do, Sol-Re: igual que els cc. 11-14.'),
           ('DERECHA', 'C. 15: Mi, Re, Do. C. 16: Si-Do, silenci i Si. Cc. 17-18: La i Sol.'),
           ('JUNTAS', 'Els cc. 15-18 en bucle, fins a tornar al c. 11.'),
           ('OJO', 'La barra del c. 18 torna al c. 11. La segona vegada, salta la casella 1.')]),
        B(5, 'cc. 19-23', 'Segona casella i final', (4, 4),
          D('cadena', 'El final',
            [('cc. 19-21', False), ('cc. 22-23', False), ('Do lligat: FINAL', True)]),
          [('IZQUIERDA', 'Cc. 19-21: Sol-Re, Fa-Do, Sol-Re. C. 22: Do de dalt. C. 23: Do de baix.'),
           ('DERECHA', 'Cc. 19-21 són els cc. 2-4. Cc. 22-23: Do lligat, quatre temps.'),
           ('JUNTAS', "Els cinc compassos d'una tirada. Aguanta el Do final."),
           ('OJO', 'Diminuendo (cc. 21-23): baixa el volum a poc a poc fins que s\'apagui.')]),
        B(6, 'cc. 1-23', 'Tota la peça, amb repeticions', (0, 4),
          D('cadena', 'El recorregut',
            [('cc. 1-8', False), ('cc. 1-6 + 9-10', False), ('cc. 11-18', False),
             ('cc. 11-15 + 19-23', True)]),
          [('IZQUIERDA', 'Tota l\'esquerra de memòria: blanques i, des del c. 11, nota i quinta.'),
           ('DERECHA', 'Tota la dreta, cantant la melodia.'),
           ('JUNTAS', 'Dues parts: cc. 1-10 amb la seva repetició i cc. 11-23 amb la seva.'),
           ('A TEMPO', 'Adagio, de mp a mf. Se\'n toquen 34, sense parar!')]),
    ],
    lista=['Toco la dreta de memòria, cantant la melodia.',
           'Faig bé el ritme del c. 1 (corxera amb puntet i semicorxera).',
           'Sé quina casella toco cada vegada.',
           'Toco els cc. 11-18 amb nota greu i quinta.',
           'Faig el crescendo i el diminuendo.'],
    cortes={1: [232.0, 375.0, 514.5, 654.5]}, corte_titulo=114.8, fin={1: 769.0},
    burb={
        0: [('arriba', 265, 'DER', 'C. 1: corxera amb puntet i semicorxera, tot al Do. Mp: toca '
                                   'suau. Compta 1-2.', 0.1),
            ('arriba', 265, 'IZQ', 'Una blanca per compàs: Do, Sol, Fa, Sol.', 0.6)],
        1: [('arriba', 265, 'OJO', 'El c. 8 torna al c. 1. La 2a vegada, salta del c. 6 al c. 9 '
                                   '(casella 2).', 0.55),
            ('abajo', 265, 'AMB', 'Crescendo als cc. 9-10: puja el volum fins al mf del c. 11.',
             0.9)],
        2: [('arriba', 265, 'IZQ', 'Nota greu i la seva quinta: La-Mi, Sol-Re, Fa-Do, Sol-Re. '
                                   'Mi, Re i Do de dalt, amb ratlletes.', 0.2),
            ('abajo', 265, 'DER', 'C. 13: Sol agut, la nota més alta de la peça. Mf: més '
                                  'volum.', 0.7)],
        3: [('arriba', 265, 'AMB', "L'esquerra repeteix els cc. 11-14. Casella 1: cc. 16-18.",
             0.4),
            ('abajo', 265, 'OJO', 'C. 18: barra de repetició. Torna al c. 11; la 2a vegada, '
                                  'salta al c. 19.', 0.95)],
        4: [('arriba', 265, 'DER', 'Cc. 19-21: com els cc. 2-4. Cc. 22-23: Do lligat, quatre '
                                   'temps.', 0.55),
            ('abajo', 265, 'OJO', 'Diminuendo (cc. 21-23): baixa el volum fins a apagar-lo. '
                                  'Bravo!', 0.85)],
    },
    marcas=[],
    misol=dict(
        manos="Canta la melodia abans de tocar-la: si la cantes, els dits ja saben on van.",
        guia="Un bloc cada dia. Quan et surti tres cops seguits, passa al següent. Les "
             "repeticions, al final!",
        pauta="Escriu el ritme del c. 1: corxera amb puntet i semicorxera. Compta 1-2 en veu "
              "alta!"),
    pie_pauta="la clau la poses tu · copia el c. 1 o escriu l'escala de Do major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_titanic.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
