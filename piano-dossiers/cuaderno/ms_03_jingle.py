# -*- coding: utf-8 -*-
"""Pieza 3 · Jingle Bell Rock a cuatro manos (Primo = parte I, Secondo = parte II).
   MEDIDO sobre el PDF (4 paginas A4, 7 sistemas de 4 compases = 28): una armadura de un
   sostenido (Sol mayor), 4/4, sin tempo impreso; «Suonare entrambe le mani un ottava sopra»
   sobre la parte I; la parte II va entera en clave de fa. Repeticion al final del c. 8 hacia el
   c. 1: casilla 1 = cc. 7-8, casilla 2 = cc. 9-10. Matices: mf (I) y mp (II) en el c. 1; f (I) c.
   10; mf (II) c. 11; mf (I) y mp (II) c. 19; cc. 25-27: f-p-f (I) y mf-pp-mf (II). Figura mas
   corta: semicorchea (corchea con puntillo + semicorchea). Tresillo de corcheas en el Secondo,
   c. 24. Alteraciones: D# (I, c. 7), Sib (I, c. 8), G#/becuadro/C# y otras en el Secondo."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_p = lambda d, b=None: ({'pitch': 'B4', 'dur': d} if b is None else
                        {'pitch': 'B4', 'dur': d, 'beam': b})
_r = lambda d: {'rest': True, 'dur': d}

SPEC = dict(
    num=3, slug='jingle', pdf='copia_de_jingle_bell_4_manos.pdf', time_sig=(4, 4),
    titulo='Jingle Bell Rock', autor='Joe Beal y Jim Boothe · a cuatro manos (Primo y Secondo)',
    kicker='Sharifa · pieza 3 · Jingle Bell Rock', mes='Diciembre',
    yt='https://www.youtube.com/results?search_query=bobby+helms+jingle+bell+rock',
    credito='Partitura: Jingle Bell Rock a 4 manos, arr. O. Litvichko (musescore.com). '
            'Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'), ('Tempo', 'No indicado'),
               ('Figura corta', 'Semicorchea'), ('Compases', '28')],
        total=28,
        secciones=[('A', 1, 8, 'El tema y la repetición', AZUL),
                   ('B', 9, 16, 'Casilla 2 · f', OCRE),
                   ('C', 17, 24, 'Vuelve el tema · tresillo', AZUL),
                   ('D', 25, 28, 'f · p · f y final', OCRE)],
        ideas=[('PRIMO · PARTE I', 'La melodía',
                'Corchea con puntillo, semicorchea y negra. Pide las dos manos una octava más '
                'aguda de lo escrito.'),
               ('SECONDO · PARTE II', 'Acordes y bajo',
                'Entera en clave de fa. Arriba, acordes en los tiempos 2 y 4; abajo, el bajo.'),
               ('LOS MATICES', 'Mucho contraste',
                'Empieza en mf (Primo) y mp (Secondo). En los cc. 25-27: f, p, f.'),
               ('LA REPETICIÓN', 'Casillas 1 y 2',
                'Al final del c. 8 vuelves al c. 1. La 2.ª vez, del c. 6 saltas al c. 9.')],
        especial=[
            'Armadura de un sostenido (Fa♯): Sol mayor. Compás 4/4, sin tempo escrito.',
            'Dos partes: I (Primo, melodía) y II (Secondo, acordes y bajo). Cada una usa las '
            'dos manos.',
            'Primo: «Suonare entrambe le mani un ottava sopra» = las dos manos una octava más '
            'aguda.',
            'Casilla 1 = cc. 7-8; casilla 2 = cc. 9-10. Al final de la casilla 1, de vuelta al '
            'c. 1.',
            'Hay alteraciones (♯, ♭ y becuadros), sobre todo en el Secondo.',
            'Semicorcheas en todo el tema y un tresillo en el Secondo (c. 24).'],
        reto='Tocar juntas: que el Primo no se adelante y el Secondo no se retrase. Los dos '
             'laten igual.',
        truco='Contad «1-2-3-4» en voz alta y empezad a la vez. Cambiad de parte para aprender '
              'las dos.',
        sabias='«Jingle Bell Rock» es de 1957: la grabó Bobby Helms y la compusieron Joe Beal y '
               'Jim Boothe. No es «Jingle Bells», otra canción mucho más antigua (1857).',
        qr_texto='Escúchala y cuenta 1-2-3-4 con la partitura delante.',
        ts=(4, 4),
        cuenta_titulo='Cómo se cuentan los cc. 1 y 2',
        cuenta_pie='Primo: corchea con puntillo, semicorchea y negra. Secondo: silencio y acorde '
                   'en el 2 y el 4. Aquí solo el ritmo.',
        ritmos=[('PRIMO', 'c. 1 · «jin-gle BELL»',
                 [_p('e.', 0), _p('s', 0), _p('q'), _p('e.', 1), _p('s', 1), _p('q')], AZUL,
                 'treble', None),
                ('SECONDO', 'c. 1 · acorde en el 2 y el 4',
                 [_r('q'), {'pitch': 'B3', 'dur': 'q'}, _r('q'), {'pitch': 'B3', 'dur': 'q'}],
                 OCRE, 'bass', None)]),
    manos=dict(
        titulo='Secondo y Primo',
        sub='Cada parte se aprende sola. Luego juntas, despacio, y os cambiáis de parte.',
        tit_izq='SECONDO · la parte II', tit_der='PRIMO · la parte I',
        izq=[('El bajo', 'Casi todo son blancas. Toca solo esa línea y cuenta 1-2-3-4.'),
             ('Acordes en el 2 y el 4', 'Arriba, acorde en el tiempo 2 y en el 4. En el 1 y en '
                                        'el 3, silencio.'),
             ('Las dos líneas', 'Une bajo y acordes en los cc. 1-4, suave (mp).'),
             ('Más movimiento', 'Desde el c. 11 los acordes son largos y el bajo va en '
                                'negras.')],
        der=[('El ritmo del tema', 'Corchea con puntillo, semicorchea y negra. Dalo primero con '
                                   'palmas.'),
             ('Melodía sola', 'Toca los cc. 1-4 con la derecha. Los cc. 2, 3 y 4 son iguales.'),
             ('La izquierda del Primo', 'En los cc. 1-4 toca casi solo blancas. Añádela a la '
                                        'derecha.'),
             ('El 8va', 'Toca las dos manos una octava más aguda de lo escrito. Busca la '
                        'posición antes de empezar.')],
        tecnica=['Contad 1-2-3-4 en voz alta y empezad a la vez.',
                 'El Secondo, más suave que el Primo: la melodía manda.',
                 'Mirad al compañero y cambiad de parte.']),
    bloques=[
        B(1, 'cc. 1-4', 'El tema', (0, 0),
          D('capas', 'Tres capas a la vez',
            [('Primo: melodía', 'puntos', AZUL, 6), ('Secondo: acordes', 'barras', OCRE),
             ('Secondo: bajo', 'barras', OCRE)]),
          [('SECONDO', 'Blancas abajo y acordes en el 2 y el 4. Todo en mp.'),
           ('PRIMO', 'Corchea con puntillo, semicorchea y negra (c. 1). Cc. 2-4 iguales. En mf.'),
           ('JUNTAS', 'Contad 1-2-3-4 y empezad a la vez.'),
           ('OJO', 'Primo: las dos manos una octava más aguda. El Secondo, más suave.')]),
        B(2, 'cc. 5-8', 'La repetición', (1, 1),
          D('cadena', 'El recorrido',
            [('cc. 1-6', False), ('casilla 1: 7-8', False), ('↩ c. 1', False),
             ('cc. 1-6', False), ('casilla 2: 9-10', True)]),
          [('SECONDO', 'Cc. 5-6 como el c. 4. Casilla 1: acorde largo (c. 7) y bajo en '
                       'movimiento (c. 8).'),
           ('PRIMO', 'Cc. 5-6: silencio y frase corta. Casilla 1: D♯ (c. 7) y Si♭ (c. 8).'),
           ('JUNTAS', 'Tocad los cc. 1-8; al final del c. 8, ¡al c. 1!'),
           ('OJO', 'La 2.ª vez saltáis del c. 6 a la casilla 2 (c. 9).')]),
        B(3, 'cc. 9-12', 'Casilla 2 y sube el sonido', (2, 2),
          D('cadena', 'Los matices del bloque',
            [('mf', False), ('f · Primo c. 10', False), ('mf · Secondo c. 11', True)]),
          [('SECONDO', 'Acordes con ♯ y becuadro (cc. 9-10). Desde el c. 11, acordes largos y '
                       'bajo en negras.'),
           ('PRIMO', 'C. 10: sube a f. C. 11: un acorde de dos notas en la derecha.'),
           ('JUNTAS', 'Los cuatro compases en bucle, con el cambio de matiz.'),
           ('OJO', 'Las alteraciones valen solo en su compás.')]),
        B(4, 'cc. 13-16', 'Acordes largos', (3, 3),
          D('cadena', 'La melodía del c. 13',
            [('Sol', False), ('Fa♯', False), ('Mi', False), ('Re', True)]),
          [('SECONDO', 'Acordes largos y bajo en negras. C. 16: blanca y dos negras.'),
           ('PRIMO', 'C. 13: cuatro negras que bajan. C. 16: dos blancas.'),
           ('JUNTAS', 'Cc. 13-16 seguidos, sin parar.'),
           ('OJO', 'Do♯ al final del bajo del c. 16 (Secondo).')]),
        B(5, 'cc. 17-20', 'Vuelve el tema', (4, 4),
          D('cadena', 'Los matices del c. 19',
            [('Primo mf', False), ('Secondo mp', True)]),
          [('SECONDO', 'Cc. 17-18: acordes seguidos y bajo que sube. C. 19: vuelve mp.'),
           ('PRIMO', 'Cc. 17-18: semicorcheas también en la izquierda. C. 19: el tema, en mf.'),
           ('JUNTAS', 'Dos compases cada vez: 17-18 y 19-20.'),
           ('OJO', 'Los cc. 19-20 son como los cc. 1-2.')]),
        B(6, 'cc. 21-24', 'Hacia el final', (5, 5),
          D('cuenta', 'Tresillo: tres notas iguales en un tiempo', [('c. 24 · tiempo 4', 1, 3)]),
          [('SECONDO', 'Cc. 21-22: acordes largos con ♭ y ♯. C. 24: tresillo en el 4.º '
                       'tiempo.'),
           ('PRIMO', 'C. 21: tema corto. C. 22: redonda (4 tiempos). C. 24: una alteración.'),
           ('JUNTAS', 'Practicad solo el tresillo del c. 24, y luego el compás entero.'),
           ('OJO', 'Tresillo = tres notas iguales en el tiempo de una negra.')]),
        B(7, 'cc. 25-28', 'Final: f, p, f', (6, 6),
          D('cadena', 'Primo · Secondo en los cc. 25, 26 y 27',
            [('f · mf', False), ('p · pp', False), ('f · mf', True)]),
          [('SECONDO', 'Acordes en el 2 y el 4 con ♯ y becuadro. Bajo en blancas y negras.'),
           ('PRIMO', 'Cc. 25-27: el mismo dibujo con tres matices. C. 28: Sol, Fa♯, Sol.'),
           ('JUNTAS', 'El c. 26 muy suave: los dos a la vez.'),
           ('A TEMPO', 'Toda la pieza con la repetición, sin parar.')]),
    ],
    inicio={1: 87, 2: 48, 3: 48, 4: 48},
    cortes={1: [390, 438], 2: [340, 390], 3: [342, 390]},
    fin={1: 735, 2: 690, 3: 678, 4: 354},
    burb={
        0: [('arriba', 262, 'AMB', 'mf (Primo) y mp (Secondo): la melodía suena un poco más. '
                                   'Contad 1-2-3-4.', 0.05),
            ('arriba', 262, 'PRIMO', 'Las dos manos, una octava más aguda. Los cc. 2, 3 y 4 son '
                                     'iguales.', 0.45),
            ('abajo', 262, 'SEC', 'Acordes en el 2 y el 4; abajo, blancas.', 0.3)],
        1: [('arriba', 520, 'OJO', 'Casilla 1 (cc. 7-8): al final vuelves al c. 1. La 2.ª vez '
                                   'saltas del c. 6 a la casilla 2 (c. 9).', 0.65),
            ('abajo', 262, 'PRIMO', 'C. 7: D♯. C. 8: Si♭ en la izquierda.', 0.7)],
        2: [('arriba', 262, 'AMB', 'Casilla 2 (cc. 9-10). C. 10: f en el Primo.', 0.4),
            ('arriba', 262, 'SEC', 'C. 11: mf. Acordes largos y bajo en negras.', 0.75)],
        3: [('arriba', 262, 'PRIMO', 'C. 13: cuatro negras que bajan: Sol-Fa♯-Mi-Re.', 0.05),
            ('arriba', 262, 'SEC', 'C. 16: Do♯ al final del bajo.', 0.95)],
        4: [('arriba', 262, 'SEC', 'C. 18: el bajo sube en negras.', 0.3),
            ('arriba', 262, 'AMB', 'C. 19: vuelve el tema del c. 1. Primo mf, Secondo mp.',
             0.65)],
        5: [('arriba', 262, 'PRIMO', 'C. 22: redonda, cuatro tiempos enteros.', 0.3),
            ('arriba', 262, 'SEC', 'C. 24: tresillo, tres notas iguales en un tiempo.', 0.95)],
        6: [('arriba', 520, 'AMB', 'Cc. 25-27: f, p, f en el Primo y mf, pp, mf en el Secondo. '
                                   'Contrastad bien.', 0.3),
            ('abajo', 262, 'OJO', 'Final: Sol, Fa♯, Sol en el Primo. Soltad a la vez.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_jingle.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
