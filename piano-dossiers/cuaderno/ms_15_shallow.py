# -*- coding: utf-8 -*-
"""Pieza 15 · Shallow (Lady Gaga y Bradley Cooper), arreglo de Campamento Musical Bye Bye Beethoven.
   MEDIDO sobre el PDF (3 paginas, tamano carta, 14 sistemas): 55 compases (5 sistemas de 4 en la
   pagina 1, 4+4+4+4+3 en la 2, 4+4+4+4 en la 3), armadura de un sostenido (Sol mayor), 4/4,
   negra = 96, sin matices escritos ni alteraciones, semicorchea como figura mas corta (cc. 20, 24,
   43), dobles barras tras los cc. 16, 24, 32, 39 y 47; izquierda en parejas de notas (casi todas
   quintas vacias), acaba en Mi (c. 55: derecha si, izquierda mi-si)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=15, slug='shallow', pdf='shallow.pdf', time_sig=(4, 4),
    titulo='Shallow', autor='Lady Gaga y Bradley Cooper · arr. Bye Bye Beethoven',
    kicker='Sharifa · pieza 15 · Shallow', mes='Julio · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=lady+gaga+bradley+cooper+shallow',
    credito='Partitura: Shallow, arreglo de Campamento Musical Bye Bye Beethoven '
            '(byebyebeethoven.es). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'), ('Tempo', 'Negra = 96'),
               ('Figura corta', 'Semicorchea'), ('Compases', '55')],
        total=55,
        secciones=[('A', 1, 16, 'Estrofa', AZUL),
                   ('B', 17, 24, 'La melodía sube', OCRE),
                   ('C', 25, 32, 'Nota repetida', AZUL),
                   ('D', 33, 39, 'Frases cortas', OCRE),
                   ('E', 40, 47, 'Vuelve la subida', AZUL),
                   ('F', 48, 55, 'Final en Mi', OCRE)],
        ideas=[('IZQUIERDA', 'Dos notas a la vez',
                'Casi siempre una quinta vacía (sol-re, la-mi, mi-si): dos notas que suenan '
                'huecas y limpias.'),
               ('DERECHA', 'Nota repetida',
                'Repite una nota (do, sol, fa♯) en corcheas y luego da un paso. Hay que contar '
                'bien.'),
               ('EL RITMO', 'Notas atadas',
                'Muchas notas empiezan a mitad de pulso y se atan al compás siguiente: cc. 1-2, '
                '9-10…'),
               ('LOS ACORDES', 'Mi · Re · Sol · Do',
                'Son los de los cc. 1-4. Después llegan La y Si. Una vez aprendidos, se repiten.')],
        especial=[
            'Un sostenido en la armadura (fa♯): Sol mayor. No hay más alteraciones.',
            'Negra = 96. No trae matices escritos: tú eliges cómo suena.',
            'Los cc. 1-4 y 5-8 son idénticos: se aprenden una sola vez.',
            'Los cc. 17-24 y 40-47 son casi iguales: la melodía sube y vuelve.',
            'Hay semicorcheas en los cc. 20, 24 y 43: sol-la muy rápidos.',
            'Empieza y acaba en Mi: el último compás es mi-si en la izquierda y un si en la '
            'derecha.'],
        reto='Contar bien las notas repetidas: la derecha repite y la izquierda cambia de acorde '
             'en medio.',
        truco='Aprende las parejas de la izquierda de los cc. 1-4 como un dibujo de la mano y '
              'toca la melodía encima.',
        sabias='«Shallow» es de la película «Ha nacido una estrella» (2018) y ganó el Óscar a la '
               'mejor canción original en 2019. La escribieron Lady Gaga, Mark Ronson, Anthony '
               'Rossomando y Andrew Wyatt.',
        qr_texto='Escúchala y marca el pulso (negra = 96) con el pie.', ts=(4, 4),
        cuenta_titulo='Dos compases de la pieza',
        cuenta_pie='Arriba, la derecha (cc. 1-2). Abajo, la izquierda (cc. 1-2): parejas de '
                   'notas. Fíjate en la ligadura: el si se ata al c. 2.',
        ritmos=[('MD', 'cc. 1-2 · la melodía',
                 [{'rest': True, 'dur': 'q'}, {'pitch': 'E4', 'dur': 'e', 'beam': 0},
                  {'pitch': 'E4', 'dur': 'e', 'beam': 0}, {'pitch': 'E4', 'dur': 'e'},
                  {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'B3', 'dur': 'e', 'lig': True},
                  {'pitch': 'B3', 'dur': 'h'}, {'rest': True, 'dur': 'h'}],
                 AZUL, 'treble', 'Sol mayor'),
                ('MI', 'cc. 1-2 · parejas de notas',
                 [{'pitches': ['E2', 'B2'], 'dur': 'h'}, {'pitches': ['F#2', 'D3'], 'dur': 'q.'},
                  {'pitches': ['G2', 'D3'], 'dur': 'e', 'lig': True},
                  {'pitches': ['G2', 'D3'], 'dur': 'w'}],
                 OCRE, 'bass', 'Sol mayor')]),
    manos=dict(
        izq=[('Parejas de notas', 'La izquierda casi siempre toca dos notas a la vez (una '
                                  'quinta): mi-si, sol-re, do-sol, la-mi. Aprende cada pareja.'),
             ('Los cc. 1-4', 'Cc. 1-2: mi-si, fa♯-re, sol-re. Cc. 3-4: do-sol, sol-re, re-fa♯. '
                             'En bucle, con el pulso.'),
             ('Notas atadas', 'Muchas parejas se alargan con una ligadura: se tocan una vez y se '
                              'aguantan.'),
             ('Los cc. 38-39', 'C. 38: cuatro acordes de negra (re-fa♯). C. 39: siete corcheas '
                               'con la-mi.')],
        der=[('Notas repetidas', 'En los cc. 3 y 17 la misma nota suena seis y cinco veces. '
                                 'Pulsa ligera, sin golpear, y cuenta «1 y 2 y».'),
             ('La estrofa', 'Los cc. 1-16 se mueven entre sol y re. Tócalos sola hasta saberlos '
                            'de memoria.'),
             ('La subida', 'En el c. 17 la mano sube: do agudo repetido y si. En el c. 19 llega '
                           'la nota más aguda, re.'),
             ('Semicorcheas', 'En los cc. 20, 24 y 43: sol-la muy rápidos y un si largo. El sol '
                              'viene atado del compás anterior.')],
        tecnica=['Muñeca suelta: el pulso se siente en el brazo, no en los dedos.',
                 'La melodía manda: la izquierda, más suave y siempre igual.',
                 'Cuenta en voz alta «1 y 2 y 3 y 4 y»: casi todo son corcheas.']),
    bloques=[
        B(1, 'cc. 1-8', 'La estrofa, dos veces', (0, 1),
          D('cadena', 'Se toca igual dos veces',
            [('cc. 1-4', False), ('= cc. 5-8', True)]),
          [('IZQUIERDA', 'Mi-si, fa♯-re, sol-re / do-sol, sol-re, re-fa♯. Despacio.'),
           ('DERECHA', 'Silencio de negra y entra: mi, mi, mi, re, si (atado).'),
           ('JUNTAS', 'Un compás cada vez: 1, 2, 3, 4. Luego los cuatro, y repite.'),
           ('A TEMPO', 'Negra = 96. Empieza más lenta y sube poco a poco.')]),
        B(2, 'cc. 9-16', 'Segunda parte de la estrofa', (2, 3),
          D('cadena', 'Qué se repite',
            [('cc. 9-10 = 13-14', False), ('c. 11 = c. 15', False), ('c. 16 cierra', True)]),
          [('IZQUIERDA', 'Las mismas parejas de los cc. 1-4: ya las sabes.'),
           ('DERECHA', 'Melodía más grave: sol, la, si. En el c. 11 sube a re.'),
           ('JUNTAS', 'Cc. 9-12 primero; luego 13-16, que casi es igual.'),
           ('OJO', 'Tras el c. 16 hay doble barra: acaba la estrofa.')]),
        B(3, 'cc. 17-24', 'La melodía sube', (4, 5),
          D('cadena', 'El dibujo de cada compás',
            [('c. 17: do', False), ('c. 18: la', False), ('c. 19: re', False),
             ('c. 20: sol-la', True)]),
          [('IZQUIERDA', 'Parejas nuevas: la-mi y sol solo (c. 17), fa♯-re (c. 18), mi-si '
                         '(c. 20).'),
           ('DERECHA', 'C. 17: do repetido y si. C. 19: llega al re, lo más agudo.'),
           ('JUNTAS', 'Los cc. 21-24 repiten los 17-20; el c. 22 añade un re.'),
           ('OJO', 'Semicorcheas del c. 20: sol-la rápidos y si largo.')]),
        B(4, 'cc. 25-32', 'Una nota, muchas veces', (6, 7),
          D('cadena', 'La nota que se repite',
            [('sol', False), ('fa♯', False), ('mi', True)]),
          [('IZQUIERDA', 'Parejas nuevas: sol-mi (c. 25) y re-la (c. 27). Léelas antes.'),
           ('DERECHA', 'Sol repetido (c. 25), fa♯ (c. 26) y mi (c. 28): baja escalón a escalón.'),
           ('JUNTAS', 'Los cc. 29-32 repiten los 25-28; el final baja a re y si.'),
           ('OJO', 'El c. 32 queda en un si largo y llega la doble barra.')]),
        B(5, 'cc. 33-39', 'Frases cortas', (8, 9),
          D('cadena', 'Se toca, se respira, se toca',
            [('frase', False), ('silencio', False), ('frase', False), ('si largo', True)]),
          [('IZQUIERDA', 'Parejas largas: si-fa♯, re-fa♯, la-mi, mi-si. C. 38: negras. C. 39: '
                         'corcheas.'),
           ('DERECHA', 'Fa♯, sol, fa♯, mi. Cuenta los silencios y no corras.'),
           ('JUNTAS', 'De cuatro en cuatro compases: 33-36 y 37-39.'),
           ('OJO', 'Cc. 38-39: un si de siete tiempos (redonda y blanca con puntillo atadas).')]),
        B(6, 'cc. 40-47', 'Vuelve la subida', (10, 11),
          D('cadena', 'Qué se repite',
            [('cc. 40-43 = 17-20', False), ('cc. 44-45 = 21-22', False), ('cc. 46-47 cambian',
                                                                           True)]),
          [('IZQUIERDA', 'Igual que los cc. 17-24: la-mi, fa♯-re, sol-re, mi-si.'),
           ('DERECHA', 'Igual que los cc. 17-22. En el c. 46 cambia el final: sol, re, si.'),
           ('JUNTAS', 'Si sabes los cc. 17-24, solo aprende los cc. 46-47.'),
           ('OJO', 'El c. 47 acaba en si largo y llega la doble barra.')]),
        B(7, 'cc. 48-55', 'El final', (12, 13),
          D('cadena', 'Hacia el final',
            [('cc. 48-51 ≈ 25-28', False), ('mi repetido', False), ('si largo', True)]),
          [('IZQUIERDA', 'Parejas de los cc. 25-28. El último compás: mi-si, una redonda.'),
           ('DERECHA', 'Cc. 52-55: mi repetido, re-mi-fa♯, sol repetido y si final.'),
           ('JUNTAS', 'Toca los cc. 52-55 varias veces: es lo que se oye al final.'),
           ('A TEMPO', 'Toda la pieza, sin parar, negra = 96. Cuando salga, grábala.')]),
    ],
    cortes={1: [242.5, 261.5, 368.5, 387.5, 497.0, 516.0, 626.5, 645.5],
            2: [153.4, 172.9, 278.4, 297.9, 405.4, 424.9, 532.0, 551.5],
            3: [153.0, 173.0, 277.1, 296.6, 401.5, 421.5]},
    corte_titulo=119.0,
    fin={1: 748.0},
    burb={
        0: [('arriba', 262, 'AMB', 'Negra = 96. Empieza con un silencio de negra: cuenta «1» y '
                                   'entra en el «2».', 0.1),
            ('abajo', 262, 'IZQ', 'Parejas de notas a la vez: mi-si, fa♯-re, sol-re. Mano '
                                  'quieta.', 0.3)],
        2: [('arriba', 300, 'DER', 'Melodía más grave: sol, la, si. En el c. 11 sube a re.',
             0.5)],
        3: [('abajo', 500, 'OJO', 'Doble barra tras el c. 16: acaba la estrofa. Respira.', 0.97)],
        4: [('arriba', 262, 'DER', 'La melodía sube: do agudo repetido. El c. 19 llega al re, la '
                                   'nota más aguda.', 0.35),
            ('abajo', 262, 'IZQ', 'Parejas nuevas: la-mi (c. 17), fa♯-re (c. 18).', 0.2)],
        6: [('arriba', 300, 'DER', 'Sol repetido cuatro veces; luego baja: fa♯, mi.', 0.3)],
        8: [('arriba', 300, 'OJO', 'Frases cortas con silencios: cuéntalos y no corras.', 0.3)],
        9: [('abajo', 300, 'AMB', 'Un si de siete tiempos: redonda y blanca con puntillo atadas. '
                                  'Izquierda: negras y corcheas.', 0.6)],
        10: [('arriba', 300, 'AMB', 'Vuelve la subida de los cc. 17-20. Ya la sabes.', 0.4)],
        11: [('abajo', 300, 'OJO', 'C. 46: cambia el final: sol repetido, re y si largo.', 0.7)],
        13: [('arriba', 300, 'AMB', 'Final: mi repetido y un si largo; mi-si en la izquierda.',
              0.5)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_shallow.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
