# -*- coding: utf-8 -*-
"""Pieza 5 · Counting Stars (OneRepublic), Easy Version, arr. Becky Messer. MEDIDO sobre el PDF
   de Musescore (2 paginas, 55 compases en 12 sistemas): sin armadura (La menor: la izquierda
   gira La menor - Do - Sol - Fa y el final cae en La), 4/4, sin tempo ni matices impresos;
   repeticiones en los cc. 1-4, 6-9, 10-29 (con casillas 1.a cc. 22-29 y 2.a cc. 30-33) y 43-46;
   semicorchea como figura mas corta (cc. 10, 14 y 34-39). Izquierda en dos notas largas
   (quintas vacias). La partitura trae digitacion impresa: no se menciona."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=5, slug='counting_stars', pdf='counting_stars.pdf', time_sig=(4, 4),
    titulo='Counting Stars', autor='OneRepublic · Easy Version, arranjament de Becky Messer',
    kicker='Txell · peça 5 · Counting Stars', mes='Febrer · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=onerepublic+counting+stars+piano+easy',
    credito='Partitura: OneRepublic, arr. Becky Messer, Easy Version (Musescore.com). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'La menor'), ('Compàs', '4/4'), ('Tempo', 'Sense indicar'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '55')],
        total=55,
        secciones=[('A', 1, 9, "L'entrada", AZUL), ('B', 10, 21, "L'estrofa", OCRE),
                   ('C', 22, 33, 'Cases 1.a i 2.a', AZUL), ('D', 34, 42, 'La part nova', OCRE),
                   ('E', 43, 55, 'Torna i final', AZUL)],
        ideas=[('ESQUERRA', 'Acords que giren',
                'Dues notes llargues alhora, una volta cada quatre compassos: La-Mi, Do-Sol, '
                'Sol-Re, Fa-Do (quintes buides).'),
               ('DRETA', 'Una frase que torna',
                'Quatre compassos curts (Re-Mi-Sol-Mi...) que es repeteixen gairebé iguals.'),
               ('EL RITME', 'Negres i corxeres',
                "Silencis de corxera a l'inici del compàs i, poques vegades, notes molt ràpides "
                '(semicorxeres).'),
               ('EL RECORREGUT', 'Repeticions',
                'Quatre barres de repetició i una casella 1.a i 2.a. Cal saber per on vas.')],
        especial=[
            'No porta armadura ni tempo: no hi ha sostinguts ni bemolls escrits.',
            'Compàs de 4/4: quatre negres per compàs.',
            'Repeticions: cc. 1-4, cc. 6-9, cc. 43-46 i la gran, del c. 10 al c. 29.',
            'Cases: la 1.a vegada toca els cc. 22-29; la 2.a salta als cc. 30-33.',
            "Semicorxeres als cc. 10, 14 i 34-39: és l'únic ràpid de la peça.",
            "Als cc. 30-33 la dreta calla i només toca l'esquerra."],
        reto="Els quatre acords de l'esquerra sempre a temps, mentre la dreta canvia de ritme. "
             'Ho aconseguiràs?',
        truco="Aprèn l'esquerra de memòria: són només quatre acords, sempre en el mateix ordre. "
              'Així només has de mirar la dreta.',
        sabias="«Counting Stars» és del 2013, de l'àlbum Native d'OneRepublic. La va escriure Ryan "
               'Tedder, el cantant del grup, i va arribar al número 2 de la llista Billboard Hot '
               '100 dels Estats Units.',
        qr_texto="Escolta-la i compta 1-2-3-4: quan canvia l'acord?", ts=(4, 4)),
    manos=dict(
        izq=[('Els quatre acords', 'Un acord per compàs, dues notes alhora: La-Mi, Do-Sol, '
                                   'Sol-Re, Fa-Do. Compta 1-2-3-4 a cada un.'),
             ('Tota la volta', 'Toca els quatre acords seguits, quatre vegades, sense parar. '
                               'Sempre en el mateix ordre.'),
             ('De memòria', "Repeteix la volta mirant la partitura de la dreta. L'esquerra ha de "
                            'sortir sola.'),
             ('Quan canvia', 'Cc. 34-37: una sola nota llarga, La aguda i La greu. Al c. 21 '
                             'entren dues corxeres al final.')],
        der=[('Una frase', 'Aprèn els cc. 1-4: Re-Mi-Sol-Mi i corxeres que baixen. És la frase '
                           'que més torna.'),
             ('Les corxeres', 'Compta «1-i-2-i». Al c. 3 comença un silenci de corxera: '
                              "compta'l, no te'l saltis."),
             ('El que és nou', 'Cc. 10-13: ritme amb puntet. Cc. 18-21: notes repetides. Cc. '
                               '34-39: notes ràpides.'),
             ("Amb l'esquerra", 'Ajunta cada frase amb el seu acord. Si et perds, torna a una '
                                'sola mà.')],
        tecnica=['Canell solt i dits corbats: acords sense prémer.',
                 "L'esquerra sona suau i la dreta canta per sobre.",
                 "Compta en veu alta i no paris si t'equivoques: continua."]),
    bloques=[
        B(1, 'cc. 1-5', 'El motiu', (0, 0),
          D('cadena', "Els acords de l'esquerra",
            [('La menor', False), ('Do', False), ('Sol', False), ('Fa', True)]),
          [('IZQUIERDA', 'La-Mi, Do-Sol, Sol-Re, Fa-Do: un acord per compàs, notes llargues.'),
           ('DERECHA', 'Re-Mi-Sol-Mi i després corxeres que baixen. És la frase més repetida.'),
           ('JUNTAS', 'Els quatre compassos junts. Es toquen dues vegades (barra del c. 4).'),
           ('OJO', 'El c. 5 és només la nota llarga que tanca: deixa-la sonar!')]),
        B(2, 'cc. 6-9', 'Silenci i corxeres', (1, 1),
          D('cadena', 'Un compàs del c. 6',
            [('negra', False), ('silenci de corxera', False), ('corxeres', False),
             ('negra', True)]),
          [('IZQUIERDA', 'Els mateixos quatre acords: La menor, Do, Sol, Fa.'),
           ('DERECHA', 'Mi repetit amb un silenci de corxera. Als cc. 8-9: Mi-Re-Do-La.'),
           ('JUNTAS', 'Quatre compassos junts. Es toquen dues vegades (barra del c. 9).'),
           ('OJO', 'El silenci de corxera dura: compta-ho en veu alta!')]),
        B(3, 'cc. 10-17', "L'estrofa", (2, 3),
          D('cadena', 'Un ritme nou',
            [('negra', False), ('corxera amb puntet', False), ('semicorxera', True)]),
          [('IZQUIERDA', 'Els quatre acords de sempre, un compàs cada un.'),
           ('DERECHA', 'Al c. 10: corxera amb puntet i semicorxera. A poc a poc.'),
           ('JUNTAS', 'Els cc. 10-13 i els cc. 14-17 són iguals: n\'aprens quatre i en valen vuit.'),
           ('OJO', 'Lligadura dels cc. 12-13: la corxera es toca una vegada i s\'allarga.')]),
        B(4, 'cc. 18-21', 'Notes repetides', (4, 4),
          D('cadena', 'La dreta als cc. 18-19',
            [('silenci', False), ('La-Sol', False), ('La', False), ('La-Sol', True)]),
          [('IZQUIERDA', 'Fa-Do llarg als cc. 18-20 (els dos primers lligats). No el repeteixis.'),
           ('DERECHA', 'La-Sol i La repetits. Al c. 20 baixa: La, Sol, Mi-Re, Do.'),
           ('JUNTAS', "L'esquerra aguanta i la dreta porta el ritme."),
           ('OJO', "Al c. 21 l'esquerra entra amb dues corxeres, La-Sol, al final.")]),
        B(5, 'cc. 22-33', 'Primera i segona vegada', (5, 6),
          D('cadena', 'El recorregut',
            [('22-29 (1.a)', False), ('↩ al c. 10', True), ('10-21', False),
             ('30-33 (2.a)', True)]),
          [('IZQUIERDA', 'Cc. 22-29: els quatre acords. Cc. 30-33: una sola nota, La greu i '
                         'La aguda.'),
           ('DERECHA', 'Cc. 22-29: la frase del principi, dues vegades. Cc. 30-33: en silenci.'),
           ('JUNTAS', 'Toca els cc. 22-29 i torna al c. 10 (barra del c. 29).'),
           ('OJO', 'La 2.a vegada et saltes la casella 1.a: del c. 21 passes al c. 30.')]),
        B(6, 'cc. 34-42', 'La part nova', (7, 8),
          D('capas', 'Dues capes alhora',
            [('Dreta: corxeres', 'puntos', AZUL, 6), ('Esquerra: una nota', 'barras', OCRE)]),
          [('IZQUIERDA', 'Cc. 34-37: una nota llarga per compàs, La aguda i La greu. Cc. 38-39: '
                         'tornen els acords.'),
           ('DERECHA', 'Do-Si-La i notes ràpides. Els cc. 34-35 es repeteixen als 36-37 i 38-39.'),
           ('JUNTAS', 'De dos en dos compassos: 34-35, 36-37, 38-39.'),
           ('OJO', 'Cc. 40-42: la baixada final i una nota llarga lligada.')]),
        B(7, 'cc. 43-55', 'Torna el tema i el final', (9, 11),
          D('cadena', 'El recorregut',
            [('43-46 (x2)', False), ('47-50', False), ('51-54', False), ('55 FINAL', True)]),
          [('IZQUIERDA', "Un altre cop La-Mi, Do-Sol, Sol-Re, Fa-Do. Al c. 55 l'esquerra calla."),
           ('DERECHA', 'És la frase del principi. El c. 54 acaba amb Mi-Re-Re-Do.'),
           ('JUNTAS', "Els cc. 51-55 sense parar fins a l'última nota."),
           ('A TEMPO', 'La peça sencera, un cop al dia, amb repeticions i cases.')]),
    ],
    cortes={1: [184.0, 296.2, 413.0, 529.2, 648.2], 2: [145.2, 264.0, 395.5, 521.0, 646.0]},
    corte_titulo=76.0, inicio={1: 18.5, 2: 30.0}, fin={1: 762.0, 2: 762.0},
    burb={
        0: [('arriba', 250, 'DER', 'Comences aquí: Re-Mi-Sol-Mi. Compta 1-2-3-4.', 0.1),
            ('abajo', 330, 'IZQ', 'Quatre acords, un per compàs: La-Mi, Do-Sol, Sol-Re, Fa-Do. '
                                  'La barra del c. 4 et torna al c. 1.', 0.2)],
        1: [('arriba', 300, 'OJO', 'Cc. 6-9: es toquen dues vegades. Compta el silenci de '
                                   'corxera abans de les corxeres!', 0.1)],
        2: [('arriba', 300, 'DER', 'Corxera amb puntet i semicorxera: la segona nota és molt '
                                   'curta. A poc a poc.', 0.12)],
        4: [('arriba', 300, 'AMB', "L'esquerra aguanta Fa-Do (lligats): no la toquis un altre cop. "
                                   'La dreta repeteix La-Sol.', 0.15)],
        5: [('arriba', 300, 'OJO', 'Casella 1.a: toca els cc. 22-29 i torna al c. 10. No et '
                                   'perdis!', 0.1)],
        6: [('abajo', 300, 'OJO', "Casella 2.a (cc. 30-33): dreta en silenci, esquerra sola. "
                                  'La 2.a vegada hi arribes des del c. 21.', 0.8)],
        7: [('arriba', 250, 'DER', 'Part nova. Les notes molt ràpides són semicorxeres: quatre '
                                   'per temps.', 0.1),
            ('abajo', 250, 'IZQ', 'Una sola nota llarga per compàs: La aguda i La greu.', 0.2)],
        8: [('arriba', 300, 'AMB', 'Cc. 38-39 repeteixen 34-35, ara amb acords. Cc. 40-42: La, '
                                   'Sol, Mi-Re, Do i nota llarga.', 0.2)],
        9: [('arriba', 300, 'OJO', 'Torna el tema! Els cc. 43-46 es toquen dues vegades (barra '
                                   'del c. 46).', 0.1)],
        11: [('arriba', 300, 'OJO', "Últim compàs: La llarga a la dreta i silenci a l'esquerra. "
                                    'Deixa-la sonar!', 0.9)],
    },
    marcas=[],
    misol=dict(manos="Truc: posa nom a cada acord (La menor, Do, Sol, Fa) i recita'ls mentre toques. "
                     "Així te'ls grava el cap.",
               guia="Ànim! Compta només 1-2-3-4. Quan els quatre acords et surtin sols, la resta "
                    "és cosa de la dreta.",
               pauta="Escriu els quatre acords de l'esquerra (La-Mi, Do-Sol, Sol-Re, Fa-Do) i "
                     "inventa't una melodia de quatre compassos!"),
    pie_pauta="la clau la poses tu · copia els quatre acords de l'esquerra")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tx_counting_stars.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
