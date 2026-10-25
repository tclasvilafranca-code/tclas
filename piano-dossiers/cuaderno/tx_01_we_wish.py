# -*- coding: utf-8 -*-
"""Peça 1 · We Wish You a Merry Christmas (versió fàcil, arr. Gilbert DeBenedetti).
   MESURAT sobre el PDF (2 pàgines, carta; la 2.a és només la lletra): una armadura d'un
   sostingut (Sol major), 3/4, sense tempo ni matisos impresos, sense repeticions. Anacrusi
   d'una negra (Re) i 16 compassos en 4 sistemes de 4; l'últim compàs és de 2 temps i completa
   l'anacrusi. Xifrats impresos: G, C, A7, D, B7, Am, D7. «CHORUS» marcat al c. 8. Figura més
   curta: corxera. Única alteració: Do♯ del baix al c. 3 (La7)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=1, slug='we_wish', pdf='we_wish_you_a_merry_christmas.pdf', time_sig=(3, 4),
    titulo='We Wish You a Merry Christmas',
    autor='Nadala tradicional anglesa · versió fàcil de Gilbert DeBenedetti',
    kicker='Txell · peça 1 · We Wish You a Merry Christmas', mes='Novembre · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=we+wish+you+a+merry+christmas+piano+easy',
    credito='Partitura: arr. Gilbert DeBenedetti (gmajormusictheory.org). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol major'), ('Compàs', '3/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Corxera'), ('Compassos', '16 + anacrusi')],
        total=16,
        secciones=[('A', 1, 7, 'Vers: «We wish you…»', AZUL),
                   ('B', 8, 16, 'Tornada: «Good tidings…»', OCRE)],
        ideas=[('LA MELODIA', 'Cap en una octava',
                'La dreta va de Re a Re. Són negres i corxeres, sense gaires salts.'),
               ("L'ESQUERRA", 'Notes llargues',
                'Quasi un so per compàs. En cinc compassos sonen dues notes juntes.'),
               ('ELS ACORDS', 'Set en total',
                'Sol, Do, Re i La menor, més tres variants amb una nota extra: La7, Si7 i Re7.'),
               ('EL FINAL', 'Sona a «final»',
                'Les dues últimes notes de cada frase (cc. 7-8 i 15-16) fan que sembli que la frase s\'acaba.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='La partitura imprimeix xifrats: G = Sol, C = Do, D = Re, Am = La menor, '
                  'A7 = La7, B7 = Si7, D7 = Re7.',
        especial=[
            "Armadura d'un sostingut (Fa♯): Sol major.",
            "Comença amb anacrusi: una nota (Re) abans del c. 1. L'últim compàs dura 2 temps i "
            "la completa.",
            "Al c. 3 l'esquerra porta un Do♯: és l'única alteració.",
            'No hi ha tempo ni matisos escrits: tria un pas alegre i constant.',
            'No hi ha repeticions: 16 compassos seguits. Els versos 2-4 fan la mateixa música.',
            "La tornada («CHORUS») comença a l'última nota del c. 8."],
        reto="Toca els 16 compassos sense parar i cantant la lletra alhora. T'hi atreveixes?",
        truco="Canta la lletra mentre toques la dreta: la música entra més fàcil. Després, "
              "l'esquerra frase a frase.",
        sabias="Aquesta nadala tradicional és del sud-oest d'Anglaterra. A la lletra es demana un "
               "«figgy pudding», un púding de Nadal: els cantaires anaven de porta en porta i no "
               "se n'anaven fins a rebre'l.",
        qr_texto="Escolta-la i canta amb la partitura al davant.",
        ts=(3, 4),
        cuenta_titulo='Com es compta el c. 1',
        cuenta_pie='Una negra i quatre corxeres: «1, 2-i, 3-i». Aquí només el ritme; les notes, '
                   'a la teva partitura.',
        ritmos=[('EL COMPTE', '3/4 · negra + 4 corxeres',
                 [{'pitch': 'B4', 'dur': 'q'}, _e(0), _e(0), _e(1), _e(1)], OCRE, 'treble',
                 None)]),
    manos=dict(
        izq=[('Una nota llarga', 'Quasi un so per compàs. Toca els cc. 1-4 només amb '
                                 "l'esquerra i compta 1-2-3."),
             ('Dues notes juntes', 'Als cc. 1, 8, 9, 13 i 16 sonen dues notes alhora. '
                                   'Prem-les juntes.'),
             ('Mi, Fa♯, Sol', "Al c. 11 puja de pas, una nota per temps. El Fa és sostingut per "
                              "l'armadura."),
             ('Un Do♯', "Al c. 3 hi ha un Do amb sostingut: l'única alteració. Mira-ho abans de "
                        "tocar.")],
        der=[('Canta-la', "És una nadala que ja coneixes. Canta-la amb la lletra abans de "
                          "tocar-la."),
             ("Entra amb l'anacrusi", 'Comença amb una sola nota (Re). Compta 1-2 en silenci i '
                                      'entra al 3.'),
             ('Corxeres de dues en dues', 'Compta «1, 2-i, 3-i» als cc. 1, 3, 5, 6 i 14. Una '
                                          'parella cada cop.'),
             ("Salt d'octava", "Al c. 14 la mà salta de Re agut a Re greu. Practica'l sola.")],
        tecnica=['Canell solt i espatlles baixes.',
                 "La dreta canta; l'esquerra acompanya més fluix.",
                 "Compta 1-2-3 en veu alta i no paris quan canviï l'acord."]),
    bloques=[
        B(1, 'anacrusi + cc. 1-4', 'La primera frase', (0, 0),
          D('cadena', 'Què toca cada mà',
            [('anacrusi: Re', False), ('cc. 1-4: melodia', False), ('esq.: notes llargues', True)]),
          [('IZQUIERDA', 'Notes llargues. Do♯ al c. 3.'),
           ('DERECHA', "Entra al 3 amb l'anacrusi. Dos compassos de «We wish you…»."),
           ('JUNTAS', 'Compta 1-2 i entren les dues mans. Frase a frase.'),
           ('A TEMPO', 'A poc a poc, amb la lletra. Respira al final del c. 4.')]),
        B(2, 'cc. 5-8', "S'acaba el vers", (1, 1),
          D('cadena', 'Cap al final del vers',
            [('Si7', False), ('Do', False), ('La menor', False), ('Re7 → Sol', True)]),
          [('IZQUIERDA', 'Nota llarga i, al c. 8, dues notes juntes.'),
           ('DERECHA', 'Cc. 5-6: altra vegada «wish you a merry Christmas». Cc. 7-8: «happy New '
                       'Year».'),
           ('JUNTAS', 'Els quatre compassos en bucle, sense parar.'),
           ('OJO', "Al c. 8 s'acaba el vers i entra «Good»: aquí comença la tornada.")]),
        B(3, 'cc. 9-12', 'Comença la tornada', (2, 2),
          D('cadena', 'Cap al Re7',
            [('Sol', False), ('Re', False), ('Do', False), ('Re7', True)]),
          [('IZQUIERDA', 'Dues notes juntes al c. 9. Al c. 11, Mi-Fa♯-Sol de pas.'),
           ('DERECHA', 'Negres tranquil·les: «tidings we bring to you and your kin».'),
           ('JUNTAS', "Un compàs cada cop: compta 1-2-3 i mira l'acord."),
           ('OJO', "L'última nota del c. 12 (La) porta a la primera del c. 13.")]),
        B(4, 'cc. 13-16', 'Tancament i final', (3, 3),
          D('cadena', 'El final de la peça',
            [('Sol', False), ('Do', False), ('La menor', False), ('Re7 → Sol', True)]),
          [('IZQUIERDA', 'Dues notes juntes als cc. 13 i 16. Notes llargues al mig.'),
           ('DERECHA', "Al c. 14, salt d'octava: de Re agut a Re greu."),
           ('JUNTAS', 'Els cc. 15-16 en bucle: Re7 → Sol, el comiat.'),
           ('OJO', "El c. 16 dura només 2 temps: compta'ls i deixa anar.")]),
        B(5, 'cc. 1-8', 'El vers sencer', (0, 1),
          D('cadena', "De l'anacrusi a «Good»",
            [('bloc 1', False), ('bloc 2', True)]),
          [('IZQUIERDA', 'Els dos blocs seguits, de memòria.'),
           ('DERECHA', 'Els dos blocs seguits, cantant la lletra.'),
           ('JUNTAS', 'Del principi al c. 8 sense parar.'),
           ('A TEMPO', 'Amb la lletra i a pas alegre.')]),
        B(6, 'cc. 9-16', 'La tornada i tota la peça', (2, 3),
          D('cadena', 'Tota la peça',
            [('vers', False), ('tornada', False), ('final', True)]),
          [('IZQUIERDA', 'Tornada de memòria: notes llargues i dues notes juntes.'),
           ('DERECHA', "Tornada cantada, amb l'octava del c. 14."),
           ('JUNTAS', "Tornada i, després, tota la peça d'una tirada."),
           ('A TEMPO', 'Sencera, a pas constant i sense parar.')]),
    ],
    lista=["Toco la dreta de memòria, cantant la lletra.",
           "Faig bé el salt d'octava del c. 14.",
           "Compto l'anacrusi i entro a temps.",
           'Toco els 16 compassos sense parar.',
           "La gravo amb el mòbil i me l'escolto."],
    cortes={1: [279.0, 416.2, 560.2]}, inicio={1: 141.5, 2: 20}, fin={1: 693.2, 2: 24},
    burb={
        0: [('arriba', 262, 'DER', "Anacrusi: una sola nota (Re) abans del compàs 1. Compta 1-2 "
                                   "i entra al 3.", 0.155),
            ('arriba', 262, 'IZQ', "Notes llargues. Al c. 3, Do♯: l'única alteració.", 0.58)],
        1: [('arriba', 520, 'AMB', "Cc. 7-8: Re7 resol en Sol (la frase s'acaba). Aquí "
                                   "s'acaba el vers.", 0.78),
            ('abajo', 520, 'OJO', "Ep! El «Good» del c. 8 ja és la tornada: canvia d'ànim i "
                                  "canta amb ganes.", 0.88)],
        2: [('arriba', 262, 'DER', 'Negres tranquil·les. Als cc. 11-12 baixa de pas: Sol, Fa♯, '
                                   'Mi, Re.', 0.45),
            ('arriba', 262, 'IZQ', 'C. 11: Mi, Fa♯, Sol, una nota per temps.', 0.62)],
        3: [('arriba', 262, 'DER', "C. 14: salt d'octava, de Re agut a Re greu. Després, dues "
                                   "corxeres.", 0.4),
            ('arriba', 262, 'OJO', "L'últim compàs dura 2 temps i completa l'anacrusi. "
                                   "Compta'ls bé!", 0.93)],
    },
    misol=dict(
        manos="Canta la lletra mentre toques la dreta: la música s'enganxa al cap i els dits "
              "la segueixen.",
        guia="Si et perds, torna al principi de la frase, no al de la peça. Les frases són el "
             "teu mapa!",
        pauta="Inventa una frase de 4 compassos en Sol major i escriu-la aquí. Si la cantes, "
              "encara millor!"),
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de Sol major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tx_we_wish.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
