# -*- coding: utf-8 -*-
"""Pieza 2 · Romance (Diabelli, op. 163 n.º 1, mov. 2), a cuatro manos. MEDIDO sobre el PDF de
   free-scores (2 paginas, 24 compases en 6 sistemas de 4): sin armadura (Do mayor), 2/2 (¢),
   Andantino sin metronomo, Primo con 8va, barra de repeticion al final del c. 8, notas de adorno
   (cc. 3, 7...), matices p dolce, cresc., f, p, mf, mp, pp y calderon final; semicorchea."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_c = lambda n: {'pitch': 'B4', 'dur': 'e', 'beam': n // 4}
SPEC = dict(
    num=2, slug='romance', pdf='romance_4_manos.pdf', time_sig=(2, 2),
    titulo='Romança', autor='Anton Diabelli · op. 163 n.º 1, 2.n mov. · a quatre mans',
    kicker='Eva · peça 2 · Romança (Diabelli)', mes='Novembre · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=diabelli+romance+op+163+piano+4+hands',
    credito='Partitura: A. Diabelli, op. 163 n.º 1 (free-scores.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '2/2'), ('Tempo', 'Andantino'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '24')],
        total=24,
        secciones=[('A', 1, 8, 'Primera part (es repeteix)', AZUL),
                   ('B', 9, 16, 'Cresc. i f', OCRE),
                   ('C', 17, 24, 'mf → pp i calderó', AZUL)],
        ideas=[('PRIMO', 'La melodia, a dalt',
                'Notes llargues lligades, amb alguna noteta d\'adorn. Va amb 8va: sona una octava '
                'més aguda del que està escrit.'),
               ('SECONDO', 'Corxeres i baix',
                'A baix hi ha una nota llarga i, a sobre, vuit corxeres per compàs que pugen i '
                'baixen suaus i lligades.'),
               ('ELS MATISOS', 'p dolce → f → pp',
                'Comença suau i dolça, creix fins a la f i acaba en pp amb un calderó.'),
               ('LA REPETICIÓ', 'Els cc. 1-8, dues vegades',
                'Una barra de repetició al final del c. 8 mana tornar al principi.')],
        especial=[
            'Hi diu "Andantino" i "p dolce": pas tranquil i so dolç.',
            'El compàs és 2/2 (¢): dos temps per compàs, cadascun de blanca.',
            'És a quatre mans: Primo a dalt i Secondo a baix.',
            'Els cc. 1-8 es toquen dues vegades (barra de repetició al c. 8).',
            'Hi ha notes d\'adorn (notetes petites), per exemple als cc. 3 i 7.',
            'Acaba amb un calderó: l\'últim acord s\'allarga.'],
        reto='Tocar a dues com si fóssiu una sola persona: respirar juntes, créixer juntes al '
             'cresc. i entrar juntes després de cada nota llarga.',
        truco='Abans de començar, compteu en veu alta "un-dos" les dues i mireu la primera nota de '
              'l\'altra. Al final de cada frase, respireu alhora.',
        sabias='Diabelli (1781-1858) va ser editor de música a Viena. Beethoven va escriure les seves 33 variacions, op. 120, sobre un vals seu. Aquesta peça és de les seves sis sonates a quatre mans, op. 163.',
        qr_texto='Escolta-la i fixa\'t com el Secondo sosté el Primo.', ts=(2, 2),
        cuenta_pie='Un compàs de 2/2: dos temps de blanca, cadascun amb quatre corxeres. Aquí '
                   'només el ritme, sobre una nota qualsevol.',
        ritmos=[('EL COMPTE', '2/2 · dos temps', [_c(i) for i in range(8)], OCRE, 'treble',
                 None)]),
    manos=dict(
        titulo='Secondo i Primo',
        sub='Cada part s\'aprèn sola. Després canvieu de part i, juntes, a poc a poc.',
        tit_izq='SECONDO · la part greu', tit_der='PRIMO · la part aguda',
        izq=[('El baix, primer', 'A baix hi ha notes llargues (rodones i blanques). Toca només '
                                 'aquesta línia comptant "un-dos" per compàs.'),
             ('Les corxeres que roden', 'A sobre, vuit corxeres per compàs, lligades i suaus. '
                                        'Estudia-les soles, a poc a poc i regulars.'),
             ('Les dues línies juntes', 'Quan cada línia surti sola, ajunta-les: les corxeres '
                                        'sobre la nota llarga.'),
             ('Matisos', 'Comença p dolce i "sempre legato" (tot lligat). Al c. 7 arriba la f: '
                         'no perdis la qualitat del so.')],
        der=[('Cantar la melodia', 'La melodia va en blanques i negres amb lligadures. Canta-la '
                                   'per dins abans de tocar-la.'),
             ('Els adorns', 'Als cc. 3 i 7 hi ha una noteta petita enganxada a la principal: '
                            'ràpida i lleugera, just abans del pols.'),
             ('El 8va', 'Tot el Primo va amb 8va: llegeixes el que està escrit, sona una octava '
                        'més aguda.'),
             ('Amb el Secondo', 'Toqueu juntes a poc a poc. El Primo escolta el Secondo: la melodia '
                                'canta sobre l\'acompanyament.')],
        tecnica=['Braços solts i esquena recta: dues persones en un banc necessiten lloc.',
                 'Compteu en veu alta "un-dos" abans de començar, juntes.',
                 'Canvieu de part: així s\'aprenen les dues.']),
    bloques=[
        B(1, 'cc. 1-4', 'La frase d\'entrada', (0, 0),
          D('capas', 'Tres capes alhora (un compàs)',
            [('Primo: melodia', 'barras', AZUL), ('Secondo: corxeres', 'puntos', OCRE, 8),
             ('Secondo: baix', 'barras', OCRE)]),
          [('SECONDO', 'Baix llarg i vuit corxeres per compàs, p dolce i tot lligat.'),
           ('PRIMO', 'La melodia, en p dolce. Notes llargues: compta-les senceres.'),
           ('JUNTAS', 'Comenceu alhora i respireu juntes al final del c. 4.'),
           ('OJO', 'El c. 3 porta una noteta d\'adorn: lleugera i enganxada.')]),
        B(2, 'cc. 5-8', 'Es repeteix: dolce → f', (1, 1),
          D('cadena', 'El recorregut', [('cc. 1-8', False), ('repeteix', False), ('després cc. 9-24',
                                                                           True)]),
          [('SECONDO', 'Cresc.: més so a poc a poc fins a la f del c. 7.'),
           ('PRIMO', 'Al c. 7, f i una noteta d\'adorn abans de la nota principal.'),
           ('JUNTAS', 'Els cc. 5-8 i la barra de repetició: torneu al c. 1!'),
           ('OJO', 'La barra al final del c. 8 mana tornar al principi.')]),
        B(3, 'cc. 9-12', 'Torna en p i creix', (2, 2),
          D('cadena', 'Els matisos', [('p', False), ('cresc.', False), ('més so', True)]),
          [('SECONDO', 'Torna el p. Al c. 11 comença el cresc.'),
           ('PRIMO', 'La melodia dels cc. 1-4 amb notes canviades: llegeix-la amb cura.'),
           ('JUNTAS', 'Dos compassos cada cop, i després els quatre.'),
           ('OJO', 'El cresc. és a poc a poc: no arribis a la f abans d\'hora.')]),
        B(4, 'cc. 13-16', 'Cresc. i f', (3, 3),
          D('cadena', 'De fort a suau', [('cresc.', False), ('f', True), ('p', False)]),
          [('SECONDO', 'f al c. 15 i p al c. 16: el canvi és de cop.'),
           ('PRIMO', 'La melodia puja amb el cresc. i torna a baixar.'),
           ('JUNTAS', 'Toqueu el c. 15 i el c. 16 en bucle: de la f a la p.'),
           ('OJO', 'Vigila la nota alterada (bemoll i becaire) d\'aquest sistema.')]),
        B(5, 'cc. 17-20', 'So mitjà', (4, 4),
          D('cadena', 'Els matisos', [('mf', True), ('mp', False)]),
          [('SECONDO', 'mf: so mitjà-fort; al c. 20 baixa a mp.'),
           ('PRIMO', 'Dues notes d\'adorn als cc. 19-20: lleugeres.'),
           ('JUNTAS', 'Dos compassos cada cop, amb el matís.'),
           ('OJO', 'Els reguladors (< >) pugen i baixen el so dins del compàs.')]),
        B(6, 'cc. 21-24', 'Final: p, pp i calderó', (5, 5),
          D('cadena', 'El final', [('p', False), ('pp', False), ('calderó', True)]),
          [('SECONDO', 'Les corxeres s\'acaben i queden negres soltes: espai i calma.'),
           ('PRIMO', 'L\'últim compàs és una nota llarga amb calderó.'),
           ('JUNTAS', 'Mireu la companya per deixar anar l\'últim acord alhora.'),
           ('A TEMPO', 'Tota la peça, amb la repetició, sense parar.')]),
    ],
    cortes={1: [324.8, 574.8], 2: [299.5, 547.0]}, corte_titulo=105.2,
    fin={1: 798, 2: 798},
    burb={
        0: [('arriba', 330, 'AMB', 'Andantino, p dolce: tranquil·la i dolça. El compàs és 2/2: '
                                   'compta un temps per blanca.', 0.2),
            ('abajo', 300, 'SEC', 'Vuit corxeres per compàs sobre una nota llarga, lligat i suau.',
             0.3)],
        1: [('arriba', 330, 'OJO', 'La barra de repetició del c. 8 mana tornar al c. 1: '
                                   'toqueu dues vegades els cc. 1-8.', 0.95),
            ('abajo', 300, 'PRIMO', 'La noteta petita del c. 7 (adorn) va enganxada a la '
                                    'principal: lleugera.', 0.6)],
        2: [('arriba', 300, 'AMB', 'p i, des del c. 11, cresc.: més so a poc a poc.', 0.5)],
        3: [('arriba', 330, 'OJO', 'f al c. 15 i p al c. 16: el canvi és de cop, no '
                                   'a poc a poc.', 0.65)],
        4: [('arriba', 300, 'AMB', 'mf als cc. 17 i 19, i mp al c. 20.', 0.5)],
        5: [('arriba', 330, 'OJO', 'p, pp i calderó: l\'últim acord s\'allarga i s\'apaga '
                                   'sol.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_romance.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
