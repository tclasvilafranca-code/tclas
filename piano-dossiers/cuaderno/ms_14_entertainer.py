# -*- coding: utf-8 -*-
"""Pieza 14 · The Entertainer (Scott Joplin, arr. Gilbert DeBenedetti, nivel 3, gradimi.com).
   MEDIDO sobre el PDF (2 paginas, tamano carta, 9 sistemas): 40 compases (4+4+4+5 en la pagina 1,
   4+5+4+5+5 en la 2), sin armadura (Do mayor), 2/2 (¢), "Not fast" sin metronomo, figura mas corta
   la negra, 8va en la derecha de los cc. 1-2, izquierda en silencio hasta el c. 8, calderon sobre el
   silencio del c. 8, matices p (c. 1), f (c. 8), p (c. 8), f (c. 12), p (c. 16), f (c. 20), p (c. 24),
   f (c. 28); alteraciones: la bemol (c. 6), re sostenido (cc. 8, 12, 16, 24, 28), fa sostenido (c. 21),
   si bemol (izquierda cc. 10, 18, 34) y la bemol (izquierda c. 36); final en staccato."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=14, slug='entertainer', pdf='el_golpe.pdf', time_sig=(2, 2),
    titulo='The Entertainer', autor='Scott Joplin · arr. Gilbert DeBenedetti',
    kicker='Sharifa · pieza 14 · The Entertainer', mes='Julio · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=scott+joplin+the+entertainer+piano',
    credito='Partitura: S. Joplin, arr. G. DeBenedetti, nivel 3 (gradimi.com). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/2 (¢)'), ('Tempo', 'Not fast: sin prisa'),
               ('Figura corta', 'Negra'), ('Compases', '40')],
        total=40,
        secciones=[('A', 1, 8, 'Entrada', AZUL),
                   ('B', 9, 17, 'Entra la izquierda', OCRE),
                   ('C', 18, 26, 'Fa♯ y vuelve el tema', AZUL),
                   ('D', 27, 35, 'Tema y bajada', OCRE),
                   ('E', 36, 40, 'Final', AZUL)],
        ideas=[('IZQUIERDA', 'Bajo y acorde',
                'Desde el c. 9: una nota grave, un silencio, un acorde, otro silencio. Es el paso '
                'de marcha del ragtime.'),
               ('DERECHA', 'Notas atadas',
                'Muchas notas se atan por encima de la barra y caen entre pulsos. Eso es el '
                'ragtime: tiempo «roto».'),
               ('LOS ACORDES', 'Do · Fa · Sol',
                'Do mayor; Do con séptima (el si♭ del c. 10); Fa mayor (c. 11); Sol con séptima, '
                'la dominante (c. 8).'),
               ('LOS MATICES', 'p ↔ f',
                'p en el c. 1, f en el c. 8 y luego p y f cada cuatro compases: cc. 12, 16, 20, '
                '24 y 28.')],
        especial=[
            'Pone «Not fast»: sin prisa. No trae metrónomo.',
            'Es 2/2 (¢): dos golpes por compás, cada uno de blanca.',
            'La izquierda no toca hasta el c. 8; antes, la derecha va sola.',
            'Los cc. 1-2 llevan 8va: suenan una octava más agudos de lo escrito.',
            'Alteraciones: la♭ (c. 6), re♯ (cc. 8, 12, 16, 24 y 28), fa♯ (c. 21) y, en la '
            'izquierda, si♭ y la♭.',
            'Hay un calderón sobre el silencio del c. 8 y acaba con notas cortas (staccato).'],
        reto='Mantener la izquierda «bajo-acorde» firme y pareja mientras la derecha juega con '
             'las ligaduras.',
        truco='Aprende la izquierda de los cc. 9-12 de memoria. Cuenta «uno-dos» (una blanca cada '
              'número) y toca la derecha encima.',
        sabias='Scott Joplin, el «rey del ragtime», publicó The Entertainer en 1902. Se hizo '
               'famosa en todo el mundo en 1973 con la película «El golpe» (The Sting). Joplin '
               'avisaba: «nunca es correcto tocar ragtime deprisa».',
        qr_texto='Escúchala y busca el «bajo-acorde» de la izquierda.', ts=(2, 2),
        cuenta_titulo='Dos compases de la pieza',
        cuenta_pie='Arriba, la derecha (c. 1): cuatro negras. Abajo, la izquierda (c. 9): bajo, '
                   'silencio, acorde, silencio. En 2/2 hay dos golpes de blanca.',
        ritmos=[('MD', 'c. 1 · el motivo',
                 [{'pitch': 'D5', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'q'},
                  {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}],
                 AZUL, 'treble', None),
                ('MI', 'c. 9 · bajo y acorde',
                 [{'pitch': 'C3', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
                  {'pitches': ['E3', 'G3'], 'dur': 'q'}, {'rest': True, 'dur': 'q'}],
                 OCRE, 'bass', None)]),
    manos=dict(
        izq=[('Cuenta antes de entrar', 'La izquierda calla hasta el c. 8. Cuenta «uno-dos» en '
                                        'voz alta siete compases y entra con el Sol grave.'),
             ('Bajo y acorde', 'Cc. 9-12: nota grave, silencio, acorde, silencio. Primero solo el '
                               'bajo; luego, el acorde.'),
             ('Los acordes cambian', 'C. 10: el acorde lleva un si♭ (Do con séptima). C. 11: '
                                     'Fa mayor. C. 12: Do mayor.'),
             ('La bajada', 'En los cc. 34-37 la nota de arriba baja por semitonos: si♭, la, la♭, '
                           'sol, sobre un do que no cambia.')],
        der=[('El motivo', 'Cc. 1-4: re, mi, do, la / la, si, sol. Tócalo despacio, sabiendo que '
                           'con el 8va suena una octava más aguda.'),
             ('La atadura', 'El la del c. 1 está atado al c. 2: se toca una vez y se aguanta. '
                            'Cuenta «uno-dos» sin parar.'),
             ('Re, re♯, mi', 'Cc. 8, 12 y 16: la mano sube por semitonos (re, re♯) y llega al '
                             'mi. Despacio y ligera.'),
             ('Con la izquierda', 'Une los cc. 9-12 a dos manos, muy despacio. Si te pierdes, '
                                  'vuelve a una mano.')],
        tecnica=['Muñeca suelta: el ragtime se toca ligero, sin golpear.',
                 'La izquierda marca el pulso: el bajo, algo más fuerte que el acorde.',
                 'No corras: pone «Not fast».']),
    bloques=[
        B(1, 'cc. 1-4', 'La entrada', (0, 0),
          D('cuenta', 'Un compás de 2/2: dos golpes de blanca',
            [('un compás', 2, 2)]),
          [('IZQUIERDA', 'Calla. Cuenta «uno-dos» en voz alta con ella.'),
           ('DERECHA', 'Re, mi, do, la. El la se ata al c. 2. Luego la, si, sol.'),
           ('OJO', 'El 8va: lo lees donde está, suena una octava más aguda.'),
           ('A TEMPO', '«Not fast»: pulso tranquilo, sin prisa.')]),
        B(2, 'cc. 5-8', 'La♭ y calderón', (1, 1),
          D('cadena', 'Del silencio al tema',
            [('f', False), ('calderón', False), ('p: re, re♯', True)]),
          [('IZQUIERDA', 'Entra por fin: Sol grave con acento, a la vez que el acorde.'),
           ('DERECHA', 'Como el c. 1; en el c. 6 sale un la♭. El c. 8, acorde con f.'),
           ('OJO', 'El calderón está sobre el silencio: espera y sigue en p.'),
           ('JUNTAS', 'Toca solo el c. 8 muchas veces: acorde, silencio, re, re♯.')]),
        B(3, 'cc. 9-12', 'Entra el tema', (2, 2),
          D('cadena', 'Izquierda, compás a compás',
            [('bajo', False), ('silencio', False), ('acorde', False), ('silencio', True)]),
          [('IZQUIERDA', 'Bajo, silencio, acorde, silencio. En el c. 10 el acorde lleva si♭.'),
           ('DERECHA', 'Mi, do (larga), mi. Do (larga), mi, do atado. Do, re, re♯ con f.'),
           ('JUNTAS', 'Dos compases cada vez: 9-10, 11-12 y luego los cuatro.'),
           ('OJO', 'En el c. 11 el acorde es de Fa, con el do abajo. C. 12: acorde corto.')]),
        B(4, 'cc. 13-17', 'Segunda frase', (3, 3),
          D('cadena', 'El camino de la frase',
            [('cc. 13-15', False), ('c. 16: p', False), ('c. 17 = c. 9', True)]),
          [('IZQUIERDA', 'Do y acorde (c. 13); Sol largo (c. 14); do y sol cortos (c. 15).'),
           ('DERECHA', 'Mi, do, re, mi atado; mi, si, re. En el c. 15, un do largo.'),
           ('JUNTAS', 'Cc. 13-14 y 15-16 por separado; luego los cinco compases.'),
           ('OJO', 'C. 16: p, otra vez re, re♯. En el c. 17 vuelve el tema.')]),
        B(5, 'cc. 18-21', 'Aparece el fa♯', (4, 4),
          D('cadena', 'La izquierda, compás a compás',
            [('Do con si♭', False), ('Fa', False), ('Do', False), ('Re', True)]),
          [('IZQUIERDA', 'Do con si♭, Fa y Do. En el c. 21: Re grave y acorde con fa♯.'),
           ('DERECHA', 'Como los cc. 10-11. Luego la, sol con f; y fa♯, la, do, mi en el c. 21.'),
           ('JUNTAS', 'Haz el c. 21 solo: es nuevo. Después, de c. 18 a 21.'),
           ('OJO', 'El fa♯ del c. 21 está en las dos manos: léelo antes de tocar.')]),
        B(6, 'cc. 22-26', 'Vuelve el tema', (5, 5),
          D('cadena', 'Hacia el tema',
            [('Re y Sol', False), ('p: re, re♯', False), ('la, si, do', False), ('tema', True)]),
          [('IZQUIERDA', 'Re (c. 22), Sol alto y Sol grave (c. 23); sube la, si, do (cc. 24-25).'),
           ('DERECHA', 'Mi, re, do, la; re larga; en el c. 24, p: re, re♯.'),
           ('JUNTAS', 'Toca la subida la-si-do de la izquierda y entra en el tema.'),
           ('OJO', 'Los cc. 25-26 son como los cc. 9-10: ya los sabes.')]),
        B(7, 'cc. 27-35', 'El tema y la bajada', (6, 7),
          D('cadena', 'Qué se repite',
            [('cc. 27-30 = 11-14', False), ('c. 32: do, re', False), ('mi, do, re', True)]),
          [('IZQUIERDA', 'Cc. 27-32 como los cc. 11-16. Desde el c. 33, acordes largos.'),
           ('DERECHA', 'Cc. 27-30 = cc. 11-14. En el c. 32, solo do-re (sin re♯).'),
           ('JUNTAS', 'Estudia los cc. 27-30; luego 31-35 en dos mitades.'),
           ('OJO', '«Mi, do, re, mi» se repite en los cc. 33 a 37: no pierdas la cuenta.')]),
        B(8, 'cc. 36-40', 'El final', (8, 8),
          D('cadena', 'La izquierda al final',
            [('Do + la♭', False), ('Do + sol', False), ('Sol largo', False),
             ('do, sol, do', True)]),
          [('IZQUIERDA', 'Do + la♭, Do + sol, Sol largo; y do, sol, do grave cortos.'),
           ('DERECHA', 'Dos frases «mi, do, re»; mi, si, re (c. 38); do corto (c. 39).'),
           ('JUNTAS', 'Cc. 36-38 a dos manos; después, los dos últimos compases.'),
           ('A TEMPO', 'Termina corto (staccato). El c. 40 es solo la izquierda.')]),
    ],
    cortes={1: [259.5, 293.5, 417.4, 442.9, 574.0, 592.0],
            2: [180.5, 196.5, 326.9, 345.4, 474.5, 489.5, 608.0, 619.5]},
    corte_titulo=154.8,
    fin={1: 717.8, 2: 750.0},
    burb={
        0: [('abajo', 262, 'DER', '8va en los cc. 1-2: suenan una octava más agudos de lo escrito. '
                                  'El la del c. 1 se ata al c. 2.', 0.3),
            ('abajo', 262, 'IZQ', 'La izquierda no toca hasta el c. 8: cuenta «uno-dos» con ella.',
             0.6)],
        1: [('arriba', 470, 'OJO', 'Calderón sobre el silencio del c. 8: espera y sigue con p, '
                                   're, re♯.', 0.85),
            ('abajo', 262, 'IZQ', 'Entra con un Sol grave (acento) a la vez que el acorde.',
             0.9)],
        2: [('abajo', 300, 'IZQ', 'Bajo, silencio, acorde, silencio. En el c. 10 lleva si♭ (Do con '
                                  'séptima); en el c. 11, Fa.', 0.4)],
        3: [('abajo', 300, 'IZQ', 'C. 14: Sol grave largo. C. 15: do y sol cortos (staccato).',
             0.5)],
        4: [('arriba', 480, 'OJO', 'Fa♯ en el c. 21: nuevo en las dos manos. A la izquierda, '
                                   'Re mayor.', 0.9)],
        5: [('abajo', 300, 'IZQ', 'Cc. 24-25: la, si, do suben hasta el tema.', 0.45)],
        6: [('arriba', 300, 'AMB', 'Cc. 27-30 = cc. 11-14: ya lo sabes. El f está en el c. 28.',
             0.3)],
        7: [('abajo', 440, 'IZQ', 'La nota de arriba baja: si♭ (c. 34), la (c. 35), la♭ y sol '
                                  '(cc. 36-37).', 0.7)],
        8: [('abajo', 440, 'AMB', 'Final corto: do, sol y do grave. El último compás es solo la '
                                  'izquierda.', 0.7)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_entertainer.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
