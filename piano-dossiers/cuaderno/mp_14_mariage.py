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
    titulo="Mariage d'amour", autor='Paul de Senneville · edición para piano',
    kicker="Eva · pieza 14 · Mariage d'amour", mes='Mayo · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=mariage+d%27amour+piano+tutorial',
    credito="Partitura: Mariage d'amour (copia escaneada). Anotaciones: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '4/4 con 5/4'), ('Tempo', '♩ = 78'),
               ('Figura corta', 'Semicorchea'), ('Compases', '83')],
        total=83,
        secciones=[('A', 1, 11, 'Primer tema', AZUL),
                   ('B', 12, 28, 'Con 8va y calderón', OCRE),
                   ('C', 29, 54, 'Tema, adornos y bajada', AZUL),
                   ('D', 55, 68, 'Notas altas y 3/8', OCRE),
                   ('E', 69, 83, 'Final', AZUL)],
        ideas=[('IZQUIERDA', 'Corcheas en vaivén',
                'Empieza sola con ocho corcheas por compás. Casi toda la pieza lleva este '
                'acompañamiento.'),
               ('DERECHA', 'Carreras de semicorcheas',
                'La carrera que sube y baja aparece muchas veces, sobre todo en los '
                'compases de 5/4.'),
               ('EL 8va', 'Una octava más aguda',
                'Desde el c. 12 hay líneas de puntos con "8": toca esas notas una octava más '
                'aguda.'),
               ('LOS COMPASES', '4/4, 5/4, 3/4 y 3/8',
                'El base es 4/4. El 5/4 se repite; el 3/4 sale en el c. 10 y el 3/8 en el '
                'c. 58.')],
        especial=[
            'Pone negra = 78 y el compás base es 4/4 (signo C).',
            'La armadura tiene dos bemoles (si♭ y mi♭): Sol menor.',
            'Los cc. 1 y 2 son de silencio en la derecha: la izquierda empieza sola.',
            'Compás de 5/4 impreso en los cc. 3, 7, 21, 25, 45, 50, 73, 77 y 80; 3/4 en el c. 10 y 3/8 en el c. 58.',
            'Líneas de 8va desde el c. 12. La izquierda cambia de clave dentro de algunos compases.',
            'Calderón en los cc. 20, 72 y 83. Matices: mp en el c. 12; p y mp en el c. 81.'],
        reto='Que las corcheas de la izquierda suenen siempre iguales y suaves mientras la '
             'derecha cambia de dibujo, de compás y de registro.',
        truco='Mira primero solo los compases con compás distinto de 4/4 (5/4, 3/4, 3/8) y '
              'cuéntalos en voz alta antes de tocar.',
        sabias='Esta melodía es muy conocida como "Mariage d\'amour" y la popularizó el '
               'pianista Richard Clayderman en los años 70. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchala con la partitura delante y cuenta los compases de 5/4.',
        ts=(4, 4), cuenta_titulo='Cómo se cuenta el 4/4 (el compás base)'),
    manos=dict(
        izq=[('Un compás, ocho corcheas', 'Los cc. 1-2 son ocho corcheas que suben y bajan. '
                                         'Tócalos solos, despacio, diez veces sin fallar.'),
             ('Cuenta el compás', 'Con 5/4 hay diez corcheas; con 4/4, ocho; con 3/4, seis. '
                                  'Cuenta negras en voz alta.'),
             ('Semicorcheas y claves', 'Desde el c. 12 hay semicorcheas y la izquierda cambia a '
                                       'clave de sol dentro del compás. Lee antes la clave.'),
             ('Negras y silencios', 'En los cc. 38-40 y 64-66 toca sobre todo negras. En el c. 63 '
                                    'casi calla: cuenta el silencio.')],
        der=[('Cantar antes de tocar', 'Escucha la melodía y cántala: así sabes adónde va cada '
                                       'frase antes de tocarla.'),
             ('La carrera', 'Estudia una carrera de semicorcheas sola (por ejemplo, c. 3), '
                            'despacio. Sube el metrónomo poco a poco.'),
             ('El 8va', 'Lee la nota escrita y toca una octava más aguda mientras dure la '
                        'línea de puntos.'),
             ('Con la izquierda', 'Une un sistema con la izquierda ya segura. Si se rompe, '
                                  'vuelve a una mano.')],
        tecnica=['Muñeca suelta: las carreras salen solas si no aprietas.',
                 'Cuenta negras, también en los compases de 5/4 y 3/4.',
                 'Sonido suave y parejo en la izquierda: la melodía manda.']),
    bloques=[
        B(1, 'cc. 1-3', 'La entrada', (0, 0),
          D('cuenta', 'Un compás de 4/4: ocho corcheas', [('un compás', 4, 2)]),
          [('IZQUIERDA', 'Empieza sola: ocho corcheas por compás, despacio y parejo.'),
           ('DERECHA', 'Dos compases de silencio. Entra en el c. 3 (5/4) con una carrera.'),
           ('JUNTAS', 'Dos compases de izquierda y, en el tercero, entra la derecha.'),
           ('A TEMPO', 'Negra = 78. Empieza más despacio.')]),
        B(2, 'cc. 4-11', 'El primer tema', (1, 3),
          D('cuenta', 'Tres compases distintos',
            [('c. 8 · 4/4', 4, 2), ('c. 7 · 5/4', 5, 2), ('c. 10 · 3/4', 3, 2)]),
          [('IZQUIERDA', 'Corcheas con saltos: en el c. 7 hay diez; el c. 10 dura tres negras.'),
           ('DERECHA', 'Carrera de semicorcheas y, después, notas más tranquilas.'),
           ('JUNTAS', 'Un sistema cada día: cc. 4-6, 7-8 y 9-11.'),
           ('OJO', 'Cuenta negras: 5/4 son cinco y 3/4 son tres.')]),
        B(3, 'cc. 12-21', 'Entra el 8va', (4, 8),
          D('cadena', 'El 8va',
            [('nota escrita', False), ('suena una octava más aguda', True)]),
          [('IZQUIERDA', 'Semicorcheas en los cc. 12-20, con cambio de clave. Lee la clave.'),
           ('DERECHA', 'Con 8va y matiz mp en el c. 12. Hay un adorno en el c. 18.'),
           ('JUNTAS', 'Un sistema cada día: cc. 12-13, 14-15, 16-17, 18-19 y 20-21.'),
           ('OJO', 'Calderón en el c. 20; en el c. 21 vuelve el 5/4.')]),
        B(4, 'cc. 22-28', 'Vuelve el tema', (9, 11),
          D('cuenta', 'Dos compases que se repiten',
            [('c. 25 · 5/4', 5, 2), ('c. 26 · 4/4', 4, 2)]),
          [('IZQUIERDA', 'Las corcheas del principio, otra vez. Ya las conoces.'),
           ('DERECHA', 'Carrera de 5/4 (cc. 21 y 25) y respuesta en 4/4. El 8va acaba en el c. 24.'),
           ('JUNTAS', 'Un sistema cada día: cc. 22-24, 25-26 y 27-28.'),
           ('OJO', 'Cuenta negras en los cambios de 4/4 a 5/4.')]),
        B(5, 'cc. 29-40', 'Melodía con adornos', (12, 16),
          D('cadena', 'Del 8va al registro normal',
            [('8va (cc. 29-37)', False), ('adornos (cc. 31 y 35)', False),
             ('sin 8va (c. 38)', True)]),
          [('IZQUIERDA', 'Semicorcheas con clave de sol dentro del compás; en los cc. 38-40, negras.'),
           ('DERECHA', 'La melodía con 8va; en los cc. 31 y 35 hay una nota adornada.'),
           ('JUNTAS', 'Un sistema cada día: cc. 29-30, 31-32, 33-34, 35-36 y 37-40.'),
           ('OJO', 'En el c. 37 la izquierda descansa: solo hay un silencio.')]),
        B(6, 'cc. 41-54', 'Negras y vuelta del tema', (17, 22),
          D('cadena', 'El recorrido',
            [('negras en la izq.', False), ('5/4 con carrera (c. 45)', False),
             ('el tema (cc. 47-54)', True)]),
          [('IZQUIERDA', 'Del c. 42 al 44, negras. En el c. 45 sube una carrera en clave de sol.'),
           ('DERECHA', 'Eco de lo que ya sabes; la carrera de los cc. 45-46 va con 8va.'),
           ('JUNTAS', 'Dos sistemas por sesión: cc. 41-46, 47-50 y 51-54.'),
           ('OJO', 'c. 45: 5/4; cc. 46 y 50, también. Cuenta cinco negras.')]),
        B(7, 'cc. 55-68', 'Notas altas y 3/8', (23, 28),
          D('grupos', 'c. 58 · 3/8: tres grupos de dos semicorcheas',
            (3, 2, ['1', '2', '3'])),
          [('IZQUIERDA', 'Semicorcheas en clave de sol (cc. 55-56 y 59-61); en el c. 58 solo una '
                         'nota larga.'),
           ('DERECHA', 'Notas altas con 8va en los cc. 55-62; adornos en el c. 61.'),
           ('JUNTAS', 'Un sistema cada día: cc. 55-56, 57-58, 59-60, 61-62, 63-65 y 66-68.'),
           ('OJO', 'c. 63: la izquierda casi calla. Cuenta el silencio.')]),
        B(8, 'cc. 69-83', 'El final', (29, 34),
          D('cadena', 'Hacia el final',
            [('calderón (c. 72)', False), ('vuelve el 5/4', False), ('p y mp (c. 81)', False),
             ('calderón final', True)]),
          [('IZQUIERDA', 'Corcheas del principio (cc. 73-79); en el c. 81 hay una carrera y '
                         'silencios.'),
           ('DERECHA', 'Cc. 73-79: carreras de 5/4 y notas dobles en el c. 75. Final con 8va.'),
           ('JUNTAS', 'Un sistema cada día; luego todo seguido.'),
           ('A TEMPO', 'Calderón en el c. 72 y en la nota final: alarga y escucha.')]),
    ],
    cortes={1: [227.8, 366.2, 504.5, 644.2], 2: [162.2, 289.5, 410, 530.5, 655.2],
            3: [162.2, 285, 409, 532, 652], 4: [159, 292, 409, 536, 654],
            5: [165, 292, 411, 530, 653], 6: [165, 286, 409, 532, 644]},
    corte_titulo=97.2,
    burb={
        0: [('abajo', 250, 'IZQ', 'Empiezas tú, sola: ocho corcheas por compás, parejas y '
                                  'suaves. Negra = 78.', 0.2),
            ('abajo', 290, 'DER', 'c. 3: 5/4. La derecha entra tras un silencio de semicorchea '
                                  'con una carrera.', 0.6)],
        2: [('arriba', 330, 'OJO', 'c. 7: 5/4, diez corcheas en la izquierda. En el c. 8 vuelve '
                                   'el 4/4 (signo C).', 0.1)],
        3: [('arriba', 330, 'OJO', 'c. 10: 3/4. Solo tres negras. En el c. 11 vuelve el 4/4.',
             0.45)],
        4: [('arriba', 330, 'AMB', 'c. 12: empieza el 8va y pone mp. La izquierda pasa a clave '
                                   'de sol: lee la clave.', 0.05)],
        5: [('arriba', 330, 'IZQ', 'La izquierda cambia de clave dentro del compás: fa, sol y '
                                   'fa otra vez.', 0.1)],
        7: [('arriba', 330, 'DER', 'c. 18: un adorno sobre la nota larga. Tócalo con ligereza '
                                   'y sin cortar la frase.', 0.45)],
        8: [('arriba', 330, 'OJO', 'c. 20: calderón sobre la nota aguda. Alárgala. En el c. 21 '
                                   'vuelve el 5/4.', 0.4)],
        16: [('arriba', 330, 'AMB', 'Desde el c. 38 la derecha ya no lleva 8va y la izquierda '
                                    'toca solo negras.', 0.2)],
        18: [('arriba', 330, 'OJO', 'cc. 45-46: 5/4. En el c. 45 corren las dos manos; en el '
                                    'c. 46, la derecha.', 0.1)],
        24: [('arriba', 330, 'OJO', 'c. 58: 3/8, seis semicorcheas. En el c. 59 vuelve el '
                                    '4/4.', 0.7)],
        29: [('arriba', 330, 'OJO', 'c. 72: calderón sobre un acorde en arpegio (línea '
                                    'ondulada). Alárgalo.', 0.75)],
        34: [('arriba', 330, 'AMB', 'c. 81: p y mp, con silencios. Calderón en el acorde final: '
                                    'déjalo sonar.', 0.5)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_mariage.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
