# -*- coding: utf-8 -*-
"""Pieza 14 · Mariage d'amour (Paul de Senneville). MEDIDO sobre el PDF (6 paginas A4, imagen
   escaneada, 35 sistemas, 83 compases con numeracion impresa al inicio de cada sistema):
   negra = 78, armadura de DOS bemoles (si y mi bemol; Sol menor), 4/4 con compases de 5/4
   (cc. 3, 7, 25, 45, 50, 73, 77), 3/4 en el c. 10 y 3/8 en el c. 58; 8va sobre la derecha desde
   el c. 12; calderones en el c. 20 y en el ultimo compas; mp en el c. 12 y p / mp en el c. 81;
   semicorchea como figura corta en las carreras de la derecha."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=14, slug='mariage', pdf='mariage_damour.pdf', time_sig=(4, 4),
    titulo="Mariage d'amour", autor='Paul de Senneville · edició per a piano',
    kicker="Eva · peça 14 · Mariage d'amour", mes='Maig · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=mariage+d%27amour+piano+tutorial',
    credito="Partitura: Mariage d'amour (còpia escanejada). Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol menor'), ('Compàs', '4/4 amb 5/4'), ('Tempo', '♩ = 78'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '83')],
        total=83,
        secciones=[('A', 1, 11, 'Primer tema', AZUL),
                   ('B', 12, 28, 'Amb 8va i calderó', OCRE),
                   ('C', 29, 54, 'Tema, adorns i baixada', AZUL),
                   ('D', 55, 68, 'Notes altes i 3/8', OCRE),
                   ('E', 69, 83, 'Final', AZUL)],
        ideas=[('ESQUERRA', 'Corxeres de vaivé',
                'Comença sola amb vuit corxeres per compàs. Quasi tota la peça porta aquest '
                'acompanyament.'),
               ('DRETA', 'Curses de semicorxeres',
                'La cursa que puja i baixa apareix moltes vegades, sobretot als '
                'compassos de 5/4.'),
               ('L\'8va', 'Una octava més aguda',
                'Des del c. 12 hi ha línies de punts amb "8": toca aquestes notes una octava més '
                'aguda.'),
               ('ELS COMPASSOS', '4/4, 5/4, 3/4 i 3/8',
                'El base és 4/4. El 5/4 es repeteix; el 3/4 surt al c. 10 i el 3/8 al '
                'c. 58.')],
        especial=[
            'Diu negra = 78 i el compàs base és 4/4 (signe C).',
            'L\'armadura té dos bemolls (si♭ i mi♭): Sol menor.',
            'Els cc. 1 i 2 són de silenci a la dreta: l\'esquerra comença sola.',
            'Compàs de 5/4 imprès als cc. 3, 7, 21, 25, 45, 50, 73, 77 i 80; 3/4 al c. 10 i 3/8 al c. 58.',
            'Línies de 8va des del c. 12. L\'esquerra canvia de clau dins d\'alguns compassos.',
            'Calderó als cc. 20, 72 i 83. Matisos: mp al c. 12; p i mp al c. 81.'],
        reto='Que les corxeres de l\'esquerra sonin sempre iguals i suaus mentre la '
             'dreta canvia de dibuix, de compàs i de registre.',
        truco='Mira primer només els compassos diferents del 4/4 (5/4, 3/4, 3/8) i '
              'compta\'ls en veu alta abans de tocar.',
        sabias='«Mariage d\'amour» és una peça de Paul de Senneville que va fer famosa arreu del món el pianista Richard Clayderman.',
        qr_texto='Escolta-la amb la partitura al davant i compta els compassos de 5/4.',
        ts=(4, 4), cuenta_titulo='Com es compta el 4/4 (el compàs base)'),
    manos=dict(
        izq=[('Un compàs, vuit corxeres', 'Els cc. 1-2 són vuit corxeres que pugen i baixen. '
                                         'Toca\'ls sols, a poc a poc, deu cops sense fallar.'),
             ('Compta el compàs', 'Amb 5/4 hi ha deu corxeres; amb 4/4, vuit; amb 3/4, sis. '
                                  'Compta negres en veu alta.'),
             ('Semicorxeres i claus', 'Des del c. 12 hi ha semicorxeres i l\'esquerra canvia a '
                                       'clau de sol dins del compàs. Llegeix abans la clau.'),
             ('Negres i silencis', 'Als cc. 38-40 i 64-66 toca sobretot negres. Al c. 63 '
                                    'gairebé calla: compta el silenci.')],
        der=[('Cantar abans de tocar', 'Escolta la melodia i canta-la: així saps on va cada '
                                       'frase abans de tocar-la.'),
             ('La cursa', 'Estudia una cursa de semicorxeres sola (per exemple, c. 3), '
                            'a poc a poc. Puja el metrònom a poc a poc.'),
             ('L\'8va', 'Llegeix la nota escrita i toca una octava més aguda mentre duri la '
                        'línia de punts.'),
             ('Amb l\'esquerra', 'Uneix un sistema amb l\'esquerra ja segura. Si es trenca, '
                                  'torna a una mà.')],
        tecnica=['Canell solt: les curses surten soles si no fas força.',
                 'Compta negres, també als compassos de 5/4 i 3/4.',
                 'So suau i regular a l\'esquerra: la melodia mana.']),
    bloques=[
        B(1, 'cc. 1-3', 'L\'entrada', (0, 0),
          D('cuenta', 'Un compàs de 4/4: vuit corxeres', [('un compàs', 4, 2)]),
          [('IZQUIERDA', 'Comença sola: vuit corxeres per compàs, a poc a poc i regular.'),
           ('DERECHA', 'Dos compassos de silenci. Entra al c. 3 (5/4) amb una cursa.'),
           ('JUNTAS', 'Dos compassos d\'esquerra i, al tercer, entra la dreta.'),
           ('A TEMPO', 'Negra = 78. Comença més a poc a poc.')]),
        B(2, 'cc. 4-11', 'El primer tema', (1, 3),
          D('cuenta', 'Tres compassos diferents',
            [('c. 8 · 4/4', 4, 2), ('c. 7 · 5/4', 5, 2), ('c. 10 · 3/4', 3, 2)]),
          [('IZQUIERDA', 'Corxeres amb salts: al c. 7 n\'hi ha deu; el c. 10 dura tres negres.'),
           ('DERECHA', 'Cursa de semicorxeres i, després, notes més tranquil·les.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 4-6, 7-8 i 9-11.'),
           ('OJO', 'Compta negres: 5/4 són cinc i 3/4 són tres.')]),
        B(3, 'cc. 12-21', 'Entra l\'8va', (4, 8),
          D('cadena', 'El 8va',
            [('nota escrita', False), ('sona una octava més aguda', True)]),
          [('IZQUIERDA', 'Semicorxeres als cc. 12-20, amb canvi de clau. Llegeix la clau.'),
           ('DERECHA', 'Amb 8va i matís mp al c. 12. Hi ha un adorn al c. 18.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 12-13, 14-15, 16-17, 18-19 i 20-21.'),
           ('OJO', 'Calderó al c. 20; al c. 21 torna el 5/4.')]),
        B(4, 'cc. 22-28', 'Torna el tema', (9, 11),
          D('cuenta', 'Dos compassos que es repeteixen',
            [('c. 25 · 5/4', 5, 2), ('c. 26 · 4/4', 4, 2)]),
          [('IZQUIERDA', 'Les corxeres del principi, una altra vegada. Ja les coneixes.'),
           ('DERECHA', 'Cursa de 5/4 (cc. 21 i 25) i resposta en 4/4. L\'8va acaba al c. 24.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 22-24, 25-26 i 27-28.'),
           ('OJO', 'Compta negres als canvis de 4/4 a 5/4.')]),
        B(5, 'cc. 29-40', 'Melodia amb adorns', (12, 16),
          D('cadena', 'De l\'8va al registre normal',
            [('8va (cc. 29-37)', False), ('adorns (cc. 31 i 35)', False),
             ('sense 8va (c. 38)', True)]),
          [('IZQUIERDA', 'Semicorxeres amb clau de sol dins del compàs; als cc. 38-40, negres.'),
           ('DERECHA', 'La melodia amb 8va; als cc. 31 i 35 hi ha una nota adornada.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 29-30, 31-32, 33-34, 35-36 i 37-40.'),
           ('OJO', 'Al c. 37 l\'esquerra descansa: només hi ha un silenci.')]),
        B(6, 'cc. 41-54', 'Negres i tornada del tema', (17, 22),
          D('cadena', 'El recorregut',
            [('negres a l\'esq.', False), ('5/4 amb cursa (c. 45)', False),
             ('el tema (cc. 47-54)', True)]),
          [('IZQUIERDA', 'Del c. 42 al 44, negres. Al c. 45 puja una cursa en clau de sol.'),
           ('DERECHA', 'Eco del que ja saps; la cursa dels cc. 45-46 va amb 8va.'),
           ('JUNTAS', 'Dos sistemes per sessió: cc. 41-46, 47-50 i 51-54.'),
           ('OJO', 'c. 45: 5/4; cc. 46 i 50, també. Compta cinc negres.')]),
        B(7, 'cc. 55-68', 'Notes altes i 3/8', (23, 28),
          D('grupos', 'c. 58 · 3/8: tres grups de dues semicorxeres',
            (3, 2, ['1', '2', '3'])),
          [('IZQUIERDA', 'Semicorxeres en clau de sol (cc. 55-56 i 59-61); al c. 58 només una '
                         'nota llarga.'),
           ('DERECHA', 'Notes altes amb 8va als cc. 55-62; adorns al c. 61.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 55-56, 57-58, 59-60, 61-62, 63-65 i 66-68.'),
           ('OJO', 'c. 63: l\'esquerra gairebé calla. Compta el silenci.')]),
        B(8, 'cc. 69-83', 'El final', (29, 34),
          D('cadena', 'Cap al final',
            [('calderó (c. 72)', False), ('torna el 5/4', False), ('p i mp (c. 81)', False),
             ('calderó final', True)]),
          [('IZQUIERDA', 'Corxeres del principi (cc. 73-79); al c. 81 hi ha una cursa i '
                         'silencis.'),
           ('DERECHA', 'Cc. 73-79: curses de 5/4 i notes dobles al c. 75. Final amb 8va.'),
           ('JUNTAS', 'Un sistema cada dia; després tot seguit.'),
           ('A TEMPO', 'Calderó al c. 72 i a la nota final: allarga i escolta.')]),
    ],
    cortes={1: [227.8, 366.2, 504.5, 644.2], 2: [162.2, 289.5, 403.5, 530.5, 655.2],
            3: [162.2, 285, 409, 532, 652], 4: [159, 292, 409, 536, 654],
            5: [165, 292, 411, 530, 653], 6: [165, 286, 409, 532, 644]},
    corte_titulo=97.2,
    burb={
        0: [('abajo', 250, 'IZQ', 'Comences tu, sola: vuit corxeres per compàs, regulars i '
                                  'suaus. Negra = 78.', 0.2),
            ('abajo', 290, 'DER', 'c. 3: 5/4. La dreta entra després d\'un silenci de semicorxera '
                                  'amb una cursa.', 0.6)],
        2: [('arriba', 330, 'OJO', 'c. 7: 5/4, deu corxeres a l\'esquerra. Al c. 8 torna '
                                   'el 4/4 (signe C).', 0.1)],
        3: [('arriba', 330, 'OJO', 'c. 10: 3/4. Només tres negres. Al c. 11 torna el 4/4.',
             0.45)],
        4: [('arriba', 330, 'AMB', 'c. 12: comença l\'8va i diu mp. L\'esquerra passa a clau '
                                   'de sol: llegeix la clau.', 0.05)],
        5: [('arriba', 330, 'IZQ', 'L\'esquerra canvia de clau dins del compàs: fa, sol i '
                                   'fa un altre cop.', 0.1)],
        7: [('arriba', 330, 'DER', 'c. 18: un adorn sobre la nota llarga. Toca\'l amb lleugeresa '
                                   'i sense tallar la frase.', 0.45)],
        8: [('arriba', 330, 'OJO', 'c. 20: calderó sobre la nota aguda. Allarga-la. Al c. 21 '
                                   'torna el 5/4.', 0.4)],
        16: [('arriba', 330, 'AMB', 'Des del c. 38 la dreta ja no porta 8va i l\'esquerra '
                                    'toca només negres.', 0.2)],
        18: [('arriba', 330, 'OJO', 'cc. 45-46: 5/4. Al c. 45 corren les dues mans; al '
                                    'c. 46, la dreta.', 0.1)],
        24: [('arriba', 330, 'OJO', 'c. 58: 3/8, sis semicorxeres. Al c. 59 torna el '
                                    '4/4.', 0.7)],
        29: [('arriba', 330, 'OJO', 'c. 72: calderó sobre un acord en arpegi (línia '
                                    'ondulada). Allarga\'l.', 0.75)],
        34: [('arriba', 330, 'AMB', 'c. 81: p i mp, amb silencis. Calderó a l\'acord final: '
                                    'deixa\'l sonar.', 0.25)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Sol menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_mariage.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
