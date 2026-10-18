# -*- coding: utf-8 -*-
"""Pieza 2 · Silent Night (Gruber), version facil de sheetmusic-free.com. MEDIDO sobre el PDF
   (2 paginas A4, 7 sistemas): sin armadura (Do mayor), 3/4, «Gently», mp; 26 compases impresos
   (cc. 1-22 y las casillas: 1.ª cc. 23-24 con barra de repeticion hacia el c. 1, 2.ª cc. 25-26);
   dos letras (2 versos); calderon en el c. 20 (ambas manos) y en el ultimo; «rit. e dim.» en la
   casilla 2; figura mas corta: corchea. Alteraciones solo en la izquierda: Si bemol (c. 8),
   Fa# (cc. 10, 14, 20), Sol# (c. 18), La bemol y Sol becuadro (c. 19), La becuadro (c. 20)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=2, slug='silent_night', pdf='silent_night.pdf', time_sig=(3, 4),
    titulo='Silent Night', autor='Franz X. Gruber (música) · Joseph Mohr (letra) · versión fácil',
    kicker='Sharifa · pieza 2 · Silent Night', mes='Noviembre · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=silent+night+piano+easy',
    credito='Partitura: F. X. Gruber, versión fácil (sheetmusic-free.com). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'), ('Tempo', 'Gently · mp'),
               ('Figura corta', 'Corchea'), ('Compases', '26')],
        total=26,
        secciones=[('A', 1, 8, 'Silent night… all is bright', AZUL),
                   ('B', 9, 16, 'Round yon Virgin…', OCRE),
                   ('C', 17, 22, 'Sleep in heavenly peace', AZUL),
                   ('D', 23, 26, 'Casillas 1 y 2', OCRE)],
        ideas=[('LA MELODÍA', 'Ritmo de nana',
                'Negra con puntillo, corchea y negra: un balanceo que vuelve en muchas frases.'),
               ('LA IZQUIERDA', 'Camina en negras',
                'Tres negras, o una negra y una blanca. Al final, notas largas.'),
               ('LAS ALTERACIONES', 'Solo en la izquierda',
                'Si♭ (c. 8), Fa♯ (cc. 10, 14, 20), Sol♯ (c. 18) y La♭ (c. 19).'),
               ('EL FINAL', 'Calderones y rit.',
                'Calderón en el c. 20 y en el último. En la casilla 2: rit. e dim.')],
        ideas_pie='Cifrados de la partitura: C = Do, F = Fa, G = Sol, E = Mi, Am = La menor, '
                  'Bm = Si menor. G/B = Sol con Si en el bajo (inversión). dim = disminuido; '
                  '7 = con séptima.',
        especial=[
            'Sin armadura: Do mayor. Pone «Gently» (suave) y mp.',
            'Dos letras: la de arriba, 1.ª vez; la de abajo, 2.ª vez.',
            'Repetición: al final del c. 24 vuelves al c. 1. La 2.ª vez saltas a la casilla 2 '
            '(cc. 25-26).',
            'Calderón en el c. 20 (las dos manos) y en el último compás.',
            'La casilla 2 lleva «rit. e dim.»: más lenta y más suave.',
            'Las alteraciones están en la izquierda: míralas antes de tocar.'],
        reto='Que la melodía cante ligada mientras la izquierda camina pareja, también en los '
             'cc. 19-20.',
        truco='Toca la izquierda sola hasta que salga mirando la derecha. Luego añade la melodía '
              'frase a frase.',
        sabias='«Stille Nacht» se estrenó en la Nochebuena de 1818 en la iglesia de San Nicolás de '
               'Oberndorf, en Austria. La letra es del sacerdote Joseph Mohr y la música, del '
               'maestro Franz Xaver Gruber.',
        qr_texto='Escúchala y sigue la partitura con el dedo.',
        ts=(3, 4),
        cuenta_titulo='Cómo se cuenta el c. 1',
        cuenta_pie='Negra con puntillo, corchea y negra: «1, 2, y, 3». Aquí solo el ritmo; las '
                   'notas, en tu partitura.',
        ritmos=[('LA CUENTA', '3/4 · balanceo de nana',
                 [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'},
                  {'pitch': 'B4', 'dur': 'q'}], OCRE, 'treble', None)]),
    manos=dict(
        izq=[('Tres pulsos', 'Casi todo son negras. Toca los cc. 1-4 y cuenta 1-2-3.'),
             ('Bajar de paso', 'En los cc. 5 y 6 baja de paso: Si-La-Sol y Fa-Mi-Re. Dilo en '
                               'voz alta.'),
             ('Las alteraciones', 'Si♭ (c. 8), Fa♯ (cc. 10, 14) y Sol♯ (c. 18). Dilas antes de '
                                  'tocar.'),
             ('Los cc. 19-20', 'Seis notas con alteraciones, una por pulso. Acaban en el Do '
                               'central, con calderón.')],
        der=[('Cántala', 'Es una nana. Cántala por dentro y respira donde acaba cada frase.'),
             ('El balanceo', 'Cuenta «1, 2, y, 3»: la corchea cae en el «y» y la negra, en el '
                             '3.'),
             ('Notas largas', 'Los cc. 2, 4, 6, 12 y 16 son una blanca con puntillo: tres tiempos '
                              'enteros.'),
             ('Calderón y rit.', 'En el c. 20 y al final alarga la nota. En la casilla 2, más '
                                 'lenta y más suave.')],
        tecnica=['Brazo suelto: la melodía se canta, no se golpea.',
                 'La izquierda, siempre más suave que la melodía.',
                 'Cuenta 1-2-3 despacio: es una nana.']),
    bloques=[
        B(1, 'cc. 1-3', 'La nana', (0, 0),
          D('cadena', 'El ritmo de la melodía (c. 1)',
            [('negra con puntillo', False), ('corchea', False), ('negra', True)]),
          [('IZQUIERDA', 'Cc. 1 y 3: Do y Mi (blanca). C. 2: Do-La-Sol.'),
           ('DERECHA', 'Sol con puntillo, La y Sol. Luego una nota larga, ligada.'),
           ('JUNTAS', 'Un compás cada vez; después los tres.'),
           ('A TEMPO', 'Gently: despacio y suave (mp).')]),
        B(2, 'cc. 4-7', 'Tres acordes nuevos', (1, 1),
          D('cadena', 'Acordes de los cc. 5 y 7 (con otra nota en el bajo)',
            [('Sol / Si abajo', False), ('La menor / Do abajo', True)]),
          [('IZQUIERDA', 'Do-La-Sol, Si-La-Sol, Fa-Mi-Re y Do-Mi-Sol.'),
           ('DERECHA', 'C. 4: Mi largo. Cc. 5-7: blanca y negra, nota larga, blanca y negra.'),
           ('JUNTAS', 'Los cuatro compases en bucle, contando 1-2-3.'),
           ('OJO', 'Sol/Si y La menor/Do: el mismo acorde con otra nota abajo (inversión).')]),
        B(3, 'cc. 8-10', 'Primeras alteraciones', (2, 2),
          D('cadena', 'Acordes del bloque',
            [('Do7 / Si♭', False), ('Fa', False), ('Fa♯ dim.', True)]),
          [('IZQUIERDA', 'Si♭ en el c. 8 y Fa♯ en el c. 10. Dilas en voz alta.'),
           ('DERECHA', 'C. 10: negra con puntillo, corchea y negra, ligadas.'),
           ('JUNTAS', 'Cc. 8-9 primero; después el 10.'),
           ('OJO', 'Cada alteración vale solo en su compás.')]),
        B(4, 'cc. 11-14', 'Vuelve la melodía', (3, 3),
          D('cadena', 'La melodía repite',
            [('c. 11 = c. 1', False), ('c. 12 = c. 2', False), ('cc. 13-14 = 9-10', True)]),
          [('IZQUIERDA', 'C. 11 empieza en Mi. C. 12 es como el c. 2. Fa♯ en el c. 14.'),
           ('DERECHA', 'La melodía de los cc. 1-2 y 9-10: ya la sabes.'),
           ('JUNTAS', 'Los cuatro compases en bucle.'),
           ('OJO', 'El Fa♯ del c. 14 es el mismo del c. 10.')]),
        B(5, 'cc. 15-18', 'Sube con Si menor', (4, 4),
          D('cadena', 'Acordes del bloque',
            [('Do', False), ('Si menor', False), ('Mi / Sol♯ abajo', True)]),
          [('IZQUIERDA', 'C. 15 como el c. 11. C. 17: Si-La-Sol. C. 18: Sol♯ y Si.'),
           ('DERECHA', 'Cc. 15-16 repiten el principio. En el c. 18 sube: «heav-».'),
           ('JUNTAS', 'Dos compases cada vez: 15-16 y 17-18.'),
           ('OJO', 'Sol♯ (c. 18): sostenido solo en ese compás.')]),
        B(6, 'cc. 19-22', 'Calderón y pausa', (5, 5),
          D('cadena', 'La izquierda, cc. 19-20',
            [('La', False), ('La♭', False), ('Sol', False), ('Fa♯', False), ('La', False),
             ('Do', True)]),
          [('IZQUIERDA', 'Cc. 19-20: seis notas con alteraciones. Cc. 21-22: Sol y Fa largos.'),
           ('DERECHA', 'Cc. 19-20: dos notas largas ligadas. C. 21: tres negras. C. 22: nana.'),
           ('JUNTAS', 'Cc. 19-20 en bucle, despacio.'),
           ('OJO', 'Calderón (c. 20): la nota dura más de lo escrito.')]),
        B(7, 'cc. 23-26', 'Casillas y final', (6, 6),
          D('cadena', 'El recorrido',
            [('cc. 1-22', False), ('casilla 1', False), ('↩ c. 1', False), ('cc. 1-22', False),
             ('casilla 2', True)]),
          [('IZQUIERDA', 'Casilla 1: Sol-Si-La, Sol-Fa-Re. Casilla 2: Mi-Fa-Re y Do largo.'),
           ('DERECHA', 'Do largo ligado. En la casilla 2, al final, nota aguda con calderón.'),
           ('JUNTAS', 'Toca la pieza con repetición: 1.ª vez casilla 1, 2.ª vez casilla 2.'),
           ('A TEMPO', 'rit. e dim.: más lenta y más suave hasta el calderón.')]),
    ],
    cortes={1: [238, 320, 473, 545], 2: [186, 225, 384, 416, 586, 610]},
    burb={
        0: [('arriba', 262, 'AMB', 'Gently y mp: suave y despacio. Compás de 3/4: cuenta '
                                   '1-2-3.', 0.06),
            ('arriba', 262, 'IZQ', 'Cc. 1 y 3: Do y Mi (blanca). C. 2: tres negras, Do-La-Sol.',
             0.45)],
        1: [('arriba', 262, 'IZQ', 'Cc. 5 y 6 bajan de paso: Si-La-Sol y Fa-Mi-Re. Dilo en voz '
                                   'alta.', 0.4),
            ('arriba', 262, 'OJO', 'Sol/Si y La menor/Do: el mismo acorde con otra nota en el '
                                   'bajo (inversión).', 0.85)],
        2: [('arriba', 262, 'IZQ', 'Si♭ (c. 8) y Fa♯ (c. 10): alteraciones, valen solo en su '
                                   'compás.', 0.12),
            ('arriba', 262, 'DER', 'C. 10: negra con puntillo, corchea y negra: el ritmo del c. '
                                   '1.', 0.8)],
        3: [('arriba', 262, 'DER', 'La melodía repite los cc. 1-2 y 9-10: ya la sabes.', 0.2),
            ('arriba', 262, 'IZQ', 'C. 11 empieza en Mi, no en Do. Fa♯ en el c. 14.', 0.8)],
        4: [('arriba', 262, 'IZQ', 'C. 18: Sol♯ en el bajo y Si largo.', 0.85),
            ('arriba', 262, 'DER', 'En el c. 18 la melodía sube: «heav-».', 0.8)],
        5: [('arriba', 262, 'IZQ', 'Cc. 19-20: seis notas con alteraciones, hasta el Do '
                                   'central.', 0.2),
            ('arriba', 262, 'OJO', 'Calderón (c. 20): alarga la nota; tú decides cuánto.', 0.5)],
        6: [('arriba', 520, 'OJO', 'Al final de la casilla 1 hay una repetición: vuelves al c. 1. '
                                   'La 2.ª vez saltas a la casilla 2.', 0.4),
            ('abajo', 520, 'AMB', 'rit. e dim.: cada vez más lenta y más suave. El último '
                                  'compás lleva calderón.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_silent_night.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
