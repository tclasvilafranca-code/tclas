# -*- coding: utf-8 -*-
"""Pieza 9 · Scherzo (Diabelli, op. 149 n.º 6), a cuatro manos. MEDIDO sobre el PDF (2 paginas,
   48 compases en 6 sistemas de 8): 3/4, Allegro sin metronomo, Do mayor sin armadura; Trio desde
   el c. 33 con tres bemoles (bajo y acordes sobre Do: Do menor). Primo en dos pentagramas (el de
   arriba con 8va), Secondo en dos. Repeticiones: :| al final del c. 16 (vuelve al c. 1); |: en el
   c. 17 y :| en el c. 32 (con 'Fine'); Trio |: c. 33 y :| c. 48 con 'Scherzo D.C. al Fine'. Las
   barras finales de los cc. 24 y 40 salen cortadas en el PDF. Figura corta: corchea (las notitas
   de adorno de los cc. 14 y 30 llevan doble barra). Matices p, f, reguladores, acentos >."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=13, slug='scherzo', pdf='scherzo_4_manos.pdf', time_sig=(3, 4),
    titulo='Scherzo', autor='Anton Diabelli · op. 149 n.º 6 · a quatre mans',
    kicker='Alba · peça 13 · Scherzo (Diabelli)', mes='Juny · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=diabelli+scherzo+op+149+no+6+piano+4+hands',
    credito='Partitura: A. Diabelli, op. 149 n.º 6 (free-scores.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '3/4'), ('Tempo', 'Allegro'),
               ('Figura curta', 'Corxera'), ('Compassos', '48')],
        total=48,
        secciones=[('A', 1, 16, 'Scherzo, 1.a part (es repeteix)', AZUL),
                   ('B', 17, 32, 'Scherzo, 2.a part (es repeteix) i Fine', OCRE),
                   ('T', 33, 48, 'Trio, amb tres bemolls (es repeteix)', VERDE)],
        ideas=[('PRIMO', 'La melodia, a dalt',
                'Els dos pentagrames del Primo porten les mateixes notes; el de dalt, amb 8va.'),
               ('SECONDO', 'Baix i acords',
                'Cada compàs: una nota greu al 1 (Do, Si, Fa, Sol...) i dos acords curts '
                'al 2 i al 3.'),
               ('EL RECORREGUT', 'Scherzo, Trio, D.C.',
                'Cc. 1-16 dues vegades, cc. 17-32 dues vegades, Trio (cc. 33-48) dues vegades i '
                'D.C. al Fine.'),
               ('ELS MATISOS', 'p · f · < > · accents',
                'p en començar, f als cc. 9 i 25; al Trio, p i f (cc. 33 i 37, 41 i 46).')],
        especial=[
            'Posa "Allegro" i el compàs és 3/4: tres negres per compàs.',
            'És a quatre mans: Primo a dalt i Secondo a baix.',
            'Barres de repetició: al final del c. 16 i entre els cc. 17 i 32; Trio, cc. 33-48.',
            'Al c. 32 posa "Fine" i al c. 48 "Scherzo D.C. al Fine".',
            "El Trio canvia l'armadura a tres bemolls (si, mi i la bemoll).",
            "Notetes d'adorn (cc. 14 i 30) i mi bemoll a l'Scherzo (cc. 19 i 22)."],
        reto='Tocar el recorregut sense perdre-us: Scherzo amb les seves repeticions, Trio i tornada al '
             "principi fins a \"Fine\".",
        truco='Abans de tocar, seguiu el camí amb el dit sobre la partitura, dient en veu '
              'alta on es torna i on s\'acaba.',
        sabias='«Scherzo» vol dir «broma» en italià. És una peça viva i lleugera, de les 28 peces melòdiques a quatre mans, op. 149, de Diabelli.',
        qr_texto='Escolta-ho i segueix el camí: Scherzo, Trio i tornada a l\'Scherzo.', ts=(3, 4),
        cuenta_pie='Un compàs de 3/4: tres cops, cadascun amb dues corxeres. Aquí només el '
                   'ritme, sobre una nota qualsevol.'),
    manos=dict(
        titulo='Secondo i Primo',
        sub='Cada part s\'aprèn sola. Després us canvieu de part i, juntes, a poc a poc.',
        tit_izq='SECONDO · la part greu', tit_der='PRIMO · la part aguda',
        izq=[('El baix, primer', 'Cada compàs comença amb una nota greu i dos silencis. '
                                 'Toca-la comptant "un-dos-tres".'),
             ('Els acords', 'A sobre, dos acords per compàs després d\'un silenci. Estudia\'ls sols, '
                            'curtets i a tempo.'),
             ('Les dues línies', 'Uneix-los: baix al 1 i acords al 2 i al 3.'),
             ('El Trio', 'Canvien els bemolls (tres). Llegeix l\'armadura abans de començar.')],
        der=[('Cantar la melodia', 'Canta-la per dins: notes llargues i grups de corxeres '
                                   'lligades.'),
             ('El picat', 'Moltes notes porten una marca de picat: curtes i lleugeres.'),
             ('El 8va', 'El pentagrama de dalt va amb 8va: llegeixes el que hi ha escrit i sona una '
                        'octava més aguda.'),
             ('Amb el Secondo', 'Toqueu juntes a poc a poc: el Primo escolta el Secondo.')],
        tecnica=['Canells solts: acords curts i lleugers, sense apretar.',
                 'Compteu en veu alta "un-dos-tres" abans de començar, juntes.',
                 'Canvieu de part: així s\'aprenen les dues.']),
    bloques=[
        B(1, 'cc. 1-8', 'El tema, en p', (0, 0),
          D('capas', 'Tres capes alhora (un compàs)',
            [('Primo: melodia', 'barras', AZUL), ('Secondo: acords', 'puntos', OCRE, 2),
             ('Secondo: baix', 'barras', OCRE)]),
          [('SECONDO', 'Baix al 1 i dos acords en p. Suaus i curts.'),
           ('PRIMO', 'La melodia en p, amb corxeres lligades i marques de picat.'),
           ('JUNTAS', 'Compteu "un-dos-tres" i comenceu alhora.'),
           ('OJO', 'Reguladors < > als cc. 2-4.')]),
        B(2, 'cc. 9-16', 'En f, i es repeteix', (1, 1),
          D('cadena', 'El recorregut', [('cc. 1-16', False), ('repeteix', False),
                                        ('després cc. 17-32', True)]),
          [('SECONDO', 'f al c. 9. El baix baixa fins a un fa sostingut al c. 13.'),
           ('PRIMO', 'Accents (>) als cc. 11-12; notetes d\'adorn al c. 14.'),
           ('JUNTAS', 'Al final del c. 16 hi ha una barra de repetició: torneu al c. 1.'),
           ('OJO', 'Fa sostingut del baix (c. 13): un sostingut que no és a l\'armadura.')]),
        B(3, 'cc. 17-24', 'Part central, en p', (2, 2),
          D('cadena', 'Els matisos', [('p', False), ('accent >', False), ('regulador <', True)]),
          [('SECONDO', 'Torna el p. Acords amb mi bemoll als cc. 19-20 i 22-23.'),
           ('PRIMO', 'Notes llargues amb accent (>) i mi bemoll als cc. 19 i 22.'),
           ('JUNTAS', 'Una barra |: marca l\'inici de la repetició del c. 17.'),
           ('OJO', 'El regulador < dels cc. 23-24 porta al f del c. 25.')]),
        B(4, 'cc. 25-32', 'Torna el tema i "Fine"', (3, 3),
          D('cadena', 'La repetició', [('c. 25 f', False), ('c. 32 :| ', False),
                                       ('tornada al c. 17', True)]),
          [('SECONDO', 'f des del c. 25. Mateix disseny que els cc. 9-16.'),
           ('PRIMO', 'Els reguladors > dels cc. 27-28 i la noteta d\'adorn del c. 30.'),
           ('JUNTAS', 'Al final del c. 32 hi ha :| i "Fine": es repeteix i després passeu al Trio.'),
           ('OJO', '"Fine" marca on s\'acaba en tornar del D.C.')]),
        B(5, 'cc. 33-40', 'Trio: tres bemolls', (4, 4),
          D('cadena', 'Allò nou', [('3 bemolls', False), ('p', False), ('f al c. 37', True)]),
          [('SECONDO', 'Baix llarg als cc. 37-39 i acords amb sostinguts i becaires.'),
           ('PRIMO', 'Melodia lligada i suau; al c. 37 arriba el f amb accents.'),
           ('JUNTAS', 'Llegiu l\'armadura: tres bemolls. A poc a poc, quatre compassos cada cop.'),
           ('OJO', 'Barra |: al c. 33: el Trio es repeteix.')]),
        B(6, 'cc. 41-48', 'Final del Trio i D.C.', (5, 5),
          D('cadena', 'Després del Trio', [('c. 48 :|', False), ('D.C.', False),
                                           ('c. 1 → Fine', True)]),
          [('SECONDO', 'Acords amb mi bemoll i un regulador abans del f del c. 46.'),
           ('PRIMO', 'p, regulador < (cc. 44-45) i f al c. 46. Acaba en nota llarga i silencis.'),
           ('JUNTAS', '"Scherzo D.C. al Fine": torneu al c. 1 i toqueu fins a "Fine".'),
           ('A TEMPO', 'Tota la peça amb el seu recorregut, sense parar.')]),
    ],
    cortes={1: [315.0, 569.2], 2: [271.0, 522.5]}, corte_titulo=86.9,
    fin={1: 802, 2: 790},
    burb={
        0: [('arriba', 200, 'AMB', 'Allegro, 3/4, en p: compta "un-dos-tres".', 77),
            ('arriba', 270, 'PRIMO', 'Reguladors < > als cc. 2-4 i marques de picat sobre '
                                     'moltes notes: lleugeres.', 230),
            ('abajo', 330, 'SEC', 'Baix (Do) a l\'1 i dos acords curts al 2 i al 3, en p. '
                                  'Els acords no pesen.', 139)],
        1: [('arriba', 250, 'PRIMO', 'f al c. 9 i accents (>) als cc. 11-12: toca\'ls amb '
                                     'pes.', 205),
            ('arriba', 270, 'PRIMO', 'c. 14: dues notetes d\'adorn, petites i enganxades a la '
                                     'principal.', 403),
            ('abajo', 520, 'OJO', 'Barra :| al final del c. 16: torneu al c. 1. Ull: al c. 13 '
                                  'el baix baixa a un fa sostingut (♯).', 559)],
        2: [('arriba', 150, 'OJO', '|: al c. 17: aquí comença la repetició.', 62),
            ('arriba', 330, 'PRIMO', 'Notes llargues amb accent (>) als cc. 18 i 20 i mi bemoll '
                                     'als cc. 19 i 22. Regulador < al final.', 194)],
        3: [('arriba', 330, 'AMB', 'f al c. 25 i reguladors > als cc. 27-28: baixa el '
                                   'so dins del compàs.', 66),
            ('abajo', 520, 'OJO', 'c. 32: barra :| i "Fine". Es repeteixen els cc. 17-32 i després '
                                  'passeu al Trio.', 551)],
        4: [('arriba', 270, 'AMB', 'Trio: tres bemolls (si, mi i la bemoll) i |: al c. 33. '
                                   'Comença en p, lligat.', 52),
            ('arriba', 260, 'PRIMO', 'f al c. 37 i accent (^) als fa♯: el Primo canta '
                                     'fort.', 321)],
        5: [('arriba', 540, 'OJO', '"Scherzo D.C. al Fine" després del c. 48: torneu al c. 1 i '
                                   'toqueu fins a "Fine" (c. 32). Abans: f al c. 46.', 506)],
    },
    marcas=[(1, 562, 445, 14, 185, 2, 1, 'caja'), (1, 62, 688, 14, 185, 3, 1, 'caja'),
            (2, 551, 150, 16, 192, 4, 1, 'caja'), (2, 510, 152, 36, 14, 4, 2, 'caja'),
            (2, 52, 397, 56, 182, 5, 1, 'caja'),
            (2, 506, 647, 128, 15, 6, 1, 'caja'), (2, 560, 650, 14, 205, 6, 2, 'caja')],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_scherzo.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
