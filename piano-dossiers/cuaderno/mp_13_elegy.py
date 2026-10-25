# -*- coding: utf-8 -*-
"""Pieza 13 · Elegy for the Arctic (Ludovico Einaudi). MEDIDO sobre el PDF (2 paginas carta,
   12 sistemas, 26 compases numerados): cuatro bemoles (si, mi, la, re bemol), "Con rubato" sin
   metronomo, semicorchea como figura mas corta; compases cambiantes impresos: 11/4 (c. 1), 10/4
   (c. 2), 7/4 (c. 3), 4/4 (c. 4), 6/4 (c. 7), 4/4 (c. 8), 5/4 (c. 9), 4/4 (c. 10), 6/4 (c. 25),
   13/4 (c. 26); matices mp, pp, mf, f, ff, mp, mp."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=13, slug='elegy', pdf='elegy_for_the_arctic_ludovico_einaudi_pd.pdf', time_sig=(4, 4),
    titulo='Elegy for the Arctic', autor='Ludovico Einaudi · edició de musicaparadisfrutar.com',
    kicker='Eva · peça 13 · Elegy for the Arctic', mes='Maig · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=einaudi+elegy+for+the+arctic+piano+tutorial',
    credito='Partitura: L. Einaudi, Elegy for the Arctic (musicaparadisfrutar.com). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Armadura', '4 bemolls'), ('Compàs', 'Canvia molt'), ('Tempo', 'Con rubato'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '26')],
        total=26,
        secciones=[('A', 1, 11, 'Primera part · fins a la doble barra', AZUL),
                   ('B', 12, 15, 'mf → f → ff', OCRE),
                   ('C', 16, 26, 'Vaivé en mp i final', AZUL)],
        ideas=[('ELS COMPASSOS', 'Canvien molt',
                '11/4, 10/4, 7/4, 4/4, 6/4, 5/4 i 13/4. El normal és el 4/4.'),
               ('DRETA', 'Grups de quatre',
                'Des del c. 3, grups de quatre semicorxeres. Als cc. 1-2 i 26, notes dobles.'),
               ('ESQUERRA', 'Baixos llargs',
                'Notes i acords llargs, quasi sempre lligats. Als cc. 14-15, semicorxeres.'),
               ('ELS MATISOS', 'mp · pp · mf · f · ff',
                'pp al c. 3, mf al 12, f al 14, ff al 15 i mp als cc. 17 i 26.')],
        especial=[
            'Diu "Con rubato" i no té metrònom: el tempo és lliure.',
            'L\'armadura té quatre bemolls: si♭, mi♭, la♭ i re♭.',
            'Compàs d\'11/4 al c. 1, 10/4 al c. 2 i 13/4 al c. 26.',
            'Hi ha doble barra entre els cc. 3 i 4 i entre els cc. 11 i 12.',
            'Apareix un becaire als cc. 19, 21, 23 i 25 (tercer grup).',
            'El ff cau al tercer temps del c. 15: el punt més fort.'],
        reto='Mantenir els grups de semicorxeres iguals i suaus mentre canvia el nombre '
             'de temps per compàs. Compta sempre en negres.',
        truco='Abans de tocar, repassa només els compassos diferents del 4/4 (cc. 1-3, 7, '
              '9, 25 i 26) i compta\'n les negres en veu alta.',
        sabias='Einaudi la va tocar el 2016 sobre una plataforma flotant al costat d\'una glacera de Svalbard, a l\'Àrtic, en una campanya de Greenpeace.',
        qr_texto='Escolta-la amb la partitura al davant: fixa\'t en quan canvia el compàs.',
        ts=(4, 4), cuenta_titulo='Com es compta el 4/4 (el compàs més habitual)',
        cuenta_pie='Un compàs de 4/4 comptat en corxeres. En aquesta peça cada temps es reparteix '
                   'en quatre semicorxeres. Aquí només el ritme, sobre una nota qualsevol.'),
    manos=dict(
        izq=[('Notes llargues', 'Als cc. 1-11 són notes i acords llargs. Compta\'n les negres i '
                              'mantén cada un sencer.'),
             ('Dos ritmes d\'acord', 'Als cc. 4 i 6 l\'esquerra toca una blanca i dues '
                                      'negres. Als cc. 3 i 5, un sol acord.'),
             ('La baixada', 'Als cc. 14-15 l\'esquerra toca semicorxeres que baixen, com la '
                           'dreta. Toca-les a poc a poc.'),
             ('Negres i blanques', 'Del c. 18 al c. 24: quatre negres als compassos parells i '
                                  'dues blanques als senars.')],
        der=[('Un grup, quatre notes', 'Aprèn un sol grup de quatre semicorxeres, a poc a poc, '
                                        'deu cops seguits sense fallar.'),
             ('Igual i suau', 'Metrònom molt lent, les quatre notes iguals. Cap no ha de '
                               'sobresortir.'),
             ('Quan canvia', 'El dibuix canvia als cc. 9 i 12. Als cc. 5 i 7 hi ha una '
                               'lligadura i un silenci de semicorxera.'),
             ('Amb l\'esquerra', 'Uneix un sistema amb l\'esquerra ja segura. Si es trenca, '
                                  'torna a una mà.')],
        tecnica=['Canell solt: les semicorxeres surten soles si no fas força.',
                 'Compta sempre en negres, encara que canviï el nombre de temps del compàs.',
                 'El so va de pp a ff: guarda la força per al c. 15.']),
    bloques=[
        B(1, 'cc. 1-2', 'L\'entrada', (0, 0),
          D('cuenta', 'Dos compassos llargs · compta negres',
            [('c. 1 · 11/4', 11, 1), ('c. 2 · 10/4', 10, 1)]),
          [('IZQUIERDA', 'Una sola nota molt greu a cada compàs. Compta-la sencera.'),
           ('DERECHA', 'Notes dobles lligades: una frase que acaba en nota llarga i es repeteix.'),
           ('JUNTAS', 'L\'esquerra sona mentre la dreta diu la seva frase.'),
           ('A TEMPO', 'Amb rubato: lliure. El mp està imprès al c. 2.')]),
        B(2, 'cc. 3-8', 'Semicorxeres i acords', (1, 3),
          D('cuenta', '4/4 en semicorxeres · 4 temps de 4 notes', [('un compàs', 4, 4)]),
          [('IZQUIERDA', 'Acord llarg al c. 3 i acord de blanca i dues negres al c. 4.'),
           ('DERECHA', 'Grups de quatre semicorxeres, en pp. Mateix dibuix als cc. 3 i 4.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 3-4, 5-6 i 7-8.'),
           ('OJO', 'Compàs: 7/4, 4/4, 6/4 i 4/4. Compta negres sense pressa.')]),
        B(3, 'cc. 9-11', 'Canvia el dibuix', (4, 4),
          D('cuenta', 'Els compassos d\'aquest bloc',
            [('c. 9 · 5/4', 5, 4), ('c. 10 · 4/4', 4, 4)]),
          [('IZQUIERDA', 'Acords llargs amb una lligadura gran de diversos compassos.'),
           ('DERECHA', 'Un altre dibuix de quatre semicorxeres, repetit als tres compassos.'),
           ('JUNTAS', 'Els tres compassos en bucle, sense parar.'),
           ('OJO', 'Doble barra al final del c. 11: aquí acaba la primera part.')]),
        B(4, 'cc. 12-13', 'mf: baixa la dreta', (5, 5),
          D('cadena', 'Un compàs de la dreta',
            [('3 grups iguals', False), ('el quart baixa', True)]),
          [('IZQUIERDA', 'Un acord de quatre notes, lligat d\'un compàs a l\'altre.'),
           ('DERECHA', 'Cada grup baixa de quatre en quatre. Tres d\'iguals i un quart més baix.'),
           ('JUNTAS', 'Els dos compassos en bucle, en mf.'),
           ('OJO', 'La lligadura uneix tot el compàs: toca amb un gest del braç.')]),
        B(5, 'cc. 14-15', 'f i ff', (6, 6),
          D('cadena', 'El so puja',
            [('mf (c. 12)', False), ('f (c. 14)', False), ('ff (c. 15)', True)]),
          [('IZQUIERDA', 'Semicorxeres que baixen, igual que la dreta. Toca-les a poc a poc.'),
           ('DERECHA', 'Baixen en grups de quatre; al c. 15 hi ha una nota llarga amb ff.'),
           ('JUNTAS', 'Compta quatre negres i arriba al ff al tercer temps del c. 15.'),
           ('OJO', 'El ff és el moment més fort de tota la peça.')]),
        B(6, 'cc. 16-24', 'Torna el vaivé', (7, 10),
          D('capas', 'Dues capes alhora',
            [('Dreta: semicorxeres', 'puntos', AZUL), ('Esquerra: negres', 'barras', OCRE)]),
          [('IZQUIERDA', 'Del c. 18 al 24: quatre negres o dues blanques per compàs.'),
           ('DERECHA', 'Mateix dibuix en grups de quatre, amb una lligadura de dos compassos.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 16-18, 19-20, 21-22 i 23-24.'),
           ('OJO', 'Becaire al tercer grup dels cc. 19, 21 i 23.')]),
        B(7, 'cc. 25-26', 'El final', (11, 11),
          D('cuenta', 'Dos compassos · compta negres',
            [('c. 25 · 6/4', 6, 1), ('c. 26 · 13/4', 13, 1)]),
          [('IZQUIERDA', 'Notes llargues: compta-les senceres.'),
           ('DERECHA', 'Al c. 26 torna la frase de l\'entrada, en mp, fins a una nota llarga.'),
           ('JUNTAS', 'Els dos compassos, a poc a poc, fins a la barra final.'),
           ('OJO', 'Compàs de 13/4: compta tretze negres sense pressa.')]),
    ],
    cortes={1: [238.8, 332.8, 428.8, 545.0, 654.5], 2: [196.0, 309.8, 420.0, 531.0, 632.5]},
    corte_titulo=131.8,
    burb={
        0: [('abajo', 330, 'AMB', 'Amb rubato: lliure. L\'esquerra té una nota llarguíssima per '
                                   'compàs (11/4 i 10/4).', 0.2)],
        1: [('arriba', 330, 'DER', 'Aquí comencen els grups de quatre semicorxeres, en pp. '
                                   'A poc a poc i regular.', 0.3)],
        2: [('arriba', 330, 'DER', 'c. 5: una lligadura i un silenci de semicorxera abans dels '
                                   'tres últims sons. Compta\'l.', 0.45)],
        3: [('arriba', 330, 'OJO', 'c. 7: 6/4 (sis negres). Al final del c. 7 hi ha una altra lligadura '
                                   'i un altre silenci de semicorxera.', 0.1)],
        4: [('arriba', 330, 'OJO', 'c. 9: 5/4; cc. 10 i 11: 4/4. Doble barra al final del c. 11.',
             0.1)],
        5: [('arriba', 300, 'AMB', 'mf: la dreta baixa de quatre en quatre i l\'esquerra '
                                   'sosté un acord lligat.', 0.15)],
        6: [('arriba', 330, 'OJO', 'f al c. 14 i ff al c. 15 (tercer temps). L\'esquerra '
                                   'copia la baixada de la dreta.', 0.4)],
        7: [('arriba', 330, 'AMB', 'mp al c. 17. Des del c. 18 l\'esquerra toca negres '
                                   'regulars i suaus.', 0.5)],
        8: [('arriba', 330, 'OJO', 'Becaire al tercer grup del c. 19 (també a l\'esquerra). '
                                   'Es repeteix als cc. 21, 23 i 25.', 0.25)],
        11: [('arriba', 330, 'OJO', 'c. 26: 13/4 i mp. Torna la frase de l\'entrada. L\'última '
                                    'nota porta becaire.', 0.65)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu una escala amb 4 bemolls')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_elegy.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
