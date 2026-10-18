# -*- coding: utf-8 -*-
"""Pieza 1 · We Wish You a Merry Christmas (version facil, arr. Gilbert DeBenedetti).
   MEDIDO sobre el PDF (2 paginas, carta; la 2.ª es solo la letra): una armadura de un sostenido
   (Sol mayor), 3/4, sin tempo ni matices impresos, sin repeticiones. Anacrusa de una negra (Re)
   y 16 compases en 4 sistemas de 4; el ultimo compas es de 2 tiempos y completa la anacrusa.
   Cifrados impresos: G, C, A7, D, B7, Am, D7. «CHORUS» marcado en el c. 8. Figura mas corta:
   corchea. Unica alteracion: Do# del bajo en el c. 3 (La7)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=1, slug='we_wish', pdf='we_wish_you_a_merry_christmas.pdf', time_sig=(3, 4),
    titulo='We Wish You a Merry Christmas',
    autor='Villancico tradicional inglés · versión fácil de Gilbert DeBenedetti',
    kicker='Sharifa · pieza 1 · We Wish You a Merry Christmas', mes='Noviembre · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=we+wish+you+a+merry+christmas+piano+easy',
    credito='Partitura: arr. Gilbert DeBenedetti (gmajormusictheory.org). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '3/4'), ('Tempo', 'No indicado'),
               ('Figura corta', 'Corchea'), ('Compases', '16 + anacrusa')],
        total=16,
        secciones=[('A', 1, 7, 'Verso: «We wish you…»', AZUL),
                   ('B', 8, 16, 'Estribillo: «Good tidings…»', OCRE)],
        ideas=[('LA MELODÍA', 'Cabe en una octava',
                'La derecha va de Re a Re. Son negras y corcheas, y casi todo se mueve de paso.'),
               ('LA IZQUIERDA', 'Notas largas',
                'Casi un sonido por compás. En cinco compases suenan dos notas juntas.'),
               ('LOS ACORDES', 'Siete en total',
                'Sol, Do, Re y La menor, más La7, Si7 y Re7 (acordes con séptima).'),
               ('EL FINAL', 'Dominante → tónica',
                'Re7 resuelve en Sol al cerrar cada frase (cc. 7-8 y 15-16): suena a «final».')],
        ideas_titulo='La pieza en cuatro ideas',
        ideas_pie='La partitura imprime cifrados: G = Sol, C = Do, D = Re, Am = La menor, '
                  'A7 = La7, B7 = Si7, D7 = Re7.',
        especial=[
            'Armadura de un sostenido (Fa♯): Sol mayor.',
            'Empieza con anacrusa: una nota (Re) antes del c. 1. El último compás dura 2 tiempos '
            'y la completa.',
            'En el c. 3 la izquierda lleva un Do♯: es la única alteración.',
            'No hay tempo ni matices escritos: elige un paso alegre y constante.',
            'No hay repeticiones: 16 compases seguidos. Los versos 2-4 usan la misma música.',
            'El estribillo («CHORUS») empieza en la última nota del c. 8.'],
        reto='Tocar los 16 compases sin parar y cantando la letra a la vez.',
        truco='Aprende la derecha cantando. Luego añade la izquierda una frase cada vez.',
        sabias='«We Wish You a Merry Christmas» es un villancico tradicional del suroeste de '
               'Inglaterra. En la letra se pide un «figgy pudding», un pudín navideño: los '
               'cantantes iban de puerta en puerta y no se marchaban hasta recibirlo.',
        qr_texto='Escúchala y canta con la partitura delante.',
        ts=(3, 4),
        cuenta_titulo='Cómo se cuenta el c. 1',
        cuenta_pie='Una negra y cuatro corcheas: «1, 2-y, 3-y». Aquí solo el ritmo; las notas, '
                   'en tu partitura.',
        ritmos=[('LA CUENTA', '3/4 · negra + 4 corcheas',
                 [{'pitch': 'B4', 'dur': 'q'}, _e(0), _e(0), _e(1), _e(1)], OCRE, 'treble',
                 None)]),
    manos=dict(
        izq=[('Una nota larga', 'Casi un sonido por compás. Toca los cc. 1-4 solo con la '
                                'izquierda y cuenta 1-2-3.'),
             ('Dos notas juntas', 'En los cc. 1, 8, 9, 13 y 16 suenan dos notas a la vez. '
                                  'Púlsalas juntas.'),
             ('Mi, Fa♯, Sol', 'En el c. 11 sube de paso, una nota por tiempo. El Fa es sostenido '
                              'por la armadura.'),
             ('Un Do♯', 'En el c. 3 hay un Do con sostenido. Es la única alteración: míralo antes '
                        'de tocar.')],
        der=[('Cántala', 'Es un villancico que ya conoces. Cántalo con la letra antes de '
                         'tocarlo.'),
             ('Entra con la anacrusa', 'Empieza con una sola nota (Re). Cuenta 1-2 en silencio y '
                                       'entra en el 3.'),
             ('Corcheas de dos en dos', 'Cuenta «1, 2-y, 3-y» en los cc. 1, 3, 5, 6 y 14. Una '
                                        'pareja cada vez.'),
             ('Salto de octava', 'En el c. 14 la mano salta de Re agudo a Re grave. Practícalo '
                                 'sola.')],
        tecnica=['Muñeca suelta y hombros bajos.',
                 'La derecha canta; la izquierda acompaña más suave.',
                 'Cuenta 1-2-3 en voz alta y no pares al cambiar de acorde.']),
    bloques=[
        B(1, 'anacrusa + cc. 1-4', 'La primera frase', (0, 0),
          D('cadena', 'Qué toca cada mano',
            [('anacrusa: Re', False), ('cc. 1-4: melodía', False), ('izq: notas largas', True)]),
          [('IZQUIERDA', 'Notas largas. Do♯ en el c. 3.'),
           ('DERECHA', 'Entra en el 3 con la anacrusa. Dos compases de «We wish you…».'),
           ('JUNTAS', 'Cuenta 1-2 y entran las dos manos. Frase a frase.'),
           ('A TEMPO', 'Despacio, con la letra. Respira al final del c. 4.')]),
        B(2, 'cc. 5-8', 'Termina el verso', (1, 1),
          D('cadena', 'Hacia el final del verso',
            [('Si7', False), ('Do', False), ('La menor', False), ('Re7 → Sol', True)]),
          [('IZQUIERDA', 'Nota larga y, en el c. 8, dos notas juntas.'),
           ('DERECHA', 'Cc. 5-6: otra vez «wish you a merry Christmas». Cc. 7-8: «happy New Year».'),
           ('JUNTAS', 'Los cuatro compases en bucle, sin parar.'),
           ('OJO', 'En el c. 8 acaba el verso y entra «Good»: ahí empieza el estribillo.')]),
        B(3, 'cc. 9-12', 'Empieza el estribillo', (2, 2),
          D('cadena', 'Hacia el Re7',
            [('Sol', False), ('Re', False), ('Do', False), ('Re7', True)]),
          [('IZQUIERDA', 'Dos notas juntas en el c. 9. En el c. 11, Mi-Fa♯-Sol de paso.'),
           ('DERECHA', 'Negras tranquilas: «tidings we bring to you and your kin».'),
           ('JUNTAS', 'Cada compás, una cosa: cuenta 1-2-3 y mira el acorde.'),
           ('OJO', 'La última nota del c. 12 (La) lleva a la primera del c. 13.')]),
        B(4, 'cc. 13-16', 'Cierre y final', (3, 3),
          D('cadena', 'El final de la pieza',
            [('Sol', False), ('Do', False), ('La menor', False), ('Re7 → Sol', True)]),
          [('IZQUIERDA', 'Dos notas juntas en los cc. 13 y 16. Notas largas en medio.'),
           ('DERECHA', 'En el c. 14, salto de octava: de Re agudo a Re grave.'),
           ('JUNTAS', 'Los cc. 15-16 en bucle: Re7 → Sol, la despedida.'),
           ('OJO', 'El c. 16 dura solo 2 tiempos: cuéntalos y suelta.')]),
        B(5, 'cc. 1-8', 'El verso entero', (0, 1),
          D('cadena', 'De la anacrusa a «Good»',
            [('bloque 1', False), ('bloque 2', True)]),
          [('IZQUIERDA', 'Los dos bloques seguidos, de memoria.'),
           ('DERECHA', 'Los dos bloques seguidos, cantando la letra.'),
           ('JUNTAS', 'Del principio al c. 8 sin parar.'),
           ('A TEMPO', 'Con la letra y a paso alegre.')]),
        B(6, 'cc. 9-16', 'El estribillo y toda la pieza', (2, 3),
          D('cadena', 'Toda la pieza',
            [('verso', False), ('estribillo', False), ('final', True)]),
          [('IZQUIERDA', 'Estribillo de memoria, notas largas y acordes.'),
           ('DERECHA', 'Estribillo cantado, con la octava del c. 14.'),
           ('JUNTAS', 'Estribillo y, después, toda la pieza de una vez.'),
           ('A TEMPO', 'Entera, a paso constante y sin parar.')]),
    ],
    cortes={1: [279.0, 416.2, 560.2]}, inicio={1: 141.5, 2: 20}, fin={1: 693.2, 2: 24},
    burb={
        0: [('arriba', 262, 'DER', 'Anacrusa: una sola nota (Re) antes del compás 1. Cuenta 1-2 '
                                   'y entra en el 3.', 0.155),
            ('arriba', 262, 'IZQ', 'Notas largas. En el c. 3, Do♯: la única '
                                   'alteración.', 0.58)],
        1: [('arriba', 520, 'AMB', 'Cc. 7-8: Re7 resuelve en Sol (dominante → tónica). Aquí '
                                   'acaba el verso.', 0.78),
            ('abajo', 520, 'OJO', 'En el c. 8, «Good» (la última nota) ya es el estribillo.',
             0.88)],
        2: [('arriba', 262, 'DER', 'Negras tranquilas. En los cc. 11-12 baja de paso: '
                                   'Sol, Fa♯, Mi, Re.', 0.45),
            ('arriba', 262, 'IZQ', 'C. 11: Mi, Fa♯, Sol, una nota por tiempo.', 0.62)],
        3: [('arriba', 262, 'DER', 'C. 14: salto de octava, de Re agudo a Re grave. Después, dos '
                                   'corcheas.', 0.4),
            ('arriba', 262, 'OJO', 'El último compás dura 2 tiempos y completa la anacrusa.',
             0.93)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_we_wish.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
