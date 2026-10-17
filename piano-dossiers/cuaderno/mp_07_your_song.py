# -*- coding: utf-8 -*-
"""Pieza 7 · Your Song (Elton John), edicion de musicaparadisfrutar.com. MEDIDO sobre el PDF
   (2 paginas carta, 9 sistemas, 29 compases): tres bemoles (Mi bemol mayor), 4/4 con compases
   sueltos de 2/4 (cc. 11, 13, 22 y 27), negra = 66 impresa, sin matices, semicorchea la figura
   mas corta (con tresillos en los cc. 8, 9, 15 y 17), cifrado americano encima, signo de segno
   y barra de repeticion en el c. 3, casillas 1 (cc. 10-11) y 2 (c. 12), "D.S. al Coda" tras el
   c. 22, Coda (signo) en el c. 23 con repeticion y casillas 1 (cc. 26-27) y 2 (cc. 28-29),
   calderones en los cc. 19, 24 y 29. No imprime "To Coda"."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=7, slug='your_song', pdf='your_song_elton_john_mi_b_m.pdf', time_sig=(4, 4),
    titulo='Your Song', autor='Elton John · arreglo para piano (musicaparadisfrutar.com)',
    kicker='Eva · pieza 7 · Your Song', mes='Febrero · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=your+song+elton+john+piano+tutorial',
    credito='Partitura: Elton John, Your Song (musicaparadisfrutar.com). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Mi♭ mayor'), ('Compás', '4/4 · algún 2/4'), ('Tempo', '♩ = 66'),
               ('Figura corta', 'Semicorchea'), ('Compases', '29')],
        total=29,
        secciones=[('A', 1, 12, 'Primera parte · segno · casillas', AZUL),
                   ('B', 13, 22, 'Sigue · D.S. al Coda', OCRE), ('C', 23, 29, 'Coda · final', AZUL)],
        ideas_titulo='Los acordes, de un vistazo',
        ideas=[('CC. 1-2', 'Mi♭ · La♭ · Mi♭ · La♭',
                'Mi♭ mayor (tónica) y La♭ mayor, alternando cada dos tiempos. En tu partitura: '
                'E♭ y A♭.'),
               ('CC. 3-12', 'Mi♭ · La♭ · Si♭ · Do m',
                'Mi♭, La♭ con séptima mayor, Si♭, Sol menor, Do menor y Fa menor. En los cc. 5-6 '
                'el bajo baja: Do, Si♭, La, La♭ (cifrado).'),
               ('CC. 13-22', 'Do m · Fa m7 · La♭',
                'Do menor, Fa menor con séptima, La♭ con sexta, y Si♭ y Mi♭ con otra nota en el '
                'bajo (Si♭/Re, Mi♭/Sol).'),
               ('CC. 23-29', 'La Coda · Mi♭',
                'Las mismas notas de los cc. 18-21, con el cifrado casi igual, y final en Mi♭ '
                '(c. 29).')],
        ideas_pie='Encima de la partitura los acordes vienen en cifrado americano (A = La, B = Si, '
                  'C = Do, D = Re, E = Mi, F = Fa, G = Sol; ♭ = bemol; "m" = menor; la barra '
                  'indica la nota del bajo). Aquí los llamamos como siempre.',
        especial=[
            'Pone ♩ = 66 (lento) y no trae ningún matiz impreso (ni p, ni f).',
            'Tres bemoles (si♭, mi♭, la♭) al principio de cada pentagrama: Mi♭ mayor.',
            'Segno y barra |: en el c. 3; casilla 1 en los cc. 10-11 y casilla 2 en el c. 12.',
            'Tras el c. 22 pone "D.S. al Coda"; la Coda son los cc. 23-29, con su repetición.',
            'La izquierda toca casi siempre dos notas juntas, en blancas.',
            'Compases de 2/4: cc. 11, 13, 22 y 27. Calderones: cc. 19, 24 y 29.'],
        reto='Entrar sin prisa tras los silencios de corchea, con semicorcheas parejas, y no '
             'perderse en el recorrido (segno, casillas, D.S. y Coda).',
        truco='Antes de tocar, sigue el recorrido con el dedo y dilo en voz alta. La partitura no '
              'imprime "To Coda": acuerda con tu profesora dónde se salta.',
        sabias='Elton John publicó «Your Song» en 1970, con letra de su compañero Bernie Taupin. Fue su primer gran éxito.',
        qr_texto='Escúchala con la partitura delante: sigue las repeticiones con el dedo.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Dos notas a la vez', 'La izquierda toca casi siempre dos notas juntas, largas. '
                                    'Practica el par: colócalo sin mirar y suéltalo despacio.'),
             ('El cifrado te guía', 'La letra de encima (E♭ = Mi♭, A♭ = La♭) te dice en qué acorde '
                                    'estás. Léela antes de cada cambio.'),
             ('Los becuadros', 'En los cc. 6, 8, 19 y 24 hay becuadros en la izquierda: esa nota va '
                               'sin bemol. Léela dos veces antes de tocar.'),
             ('Compases de 2/4', 'En los cc. 11, 13, 22 y 27 solo hay dos tiempos: cuenta 1-2 y '
                                 'sigue.')],
        der=[('Entrar tras el silencio', 'Muchas frases empiezan con silencio de corchea (cc. 3, 4 '
                                         'y 6): cuéntalo y no entres antes.'),
             ('Semicorcheas ligadas', 'Cuenta cuatro semicorcheas por golpe. En cada ligadura toca '
                                      'la primera nota y mantén la segunda.'),
             ('El tresillo', 'En los cc. 8, 9, 15 y 17 el "3" marca tres notas en el tiempo de '
                             'dos. Dilo "tre-si-llo" mientras tocas.'),
             ('Con la izquierda', 'Une despacio una frase con la izquierda ya segura. Si se rompe, '
                                  'vuelve a una mano.')],
        tecnica=['Muñeca suelta: las semicorcheas salen cantadas, no apretadas.',
                 'Cuenta 1-2-3-4 sin prisa: ♩ = 66 es lento.',
                 'Mira el recorrido (segno, casillas, Coda) antes de tocar.']),
    bloques=[
        B(1, 'cc. 1-2', 'El arranque', (0, 0),
          D('cuenta', '4/4 en semicorcheas: cuatro por golpe', [('un compás', 4, 4)]),
          [('IZQUIERDA', 'Dos blancas de dos notas por compás: Mi♭ y La♭ según el cifrado.'),
           ('DERECHA', 'Corcheas y semicorcheas ligadas; entra ya en el primer tiempo.'),
           ('JUNTAS', 'Cuenta 1-2-3-4 y toca solo estos dos compases hasta no pararte.'),
           ('A TEMPO', '♩ = 66: empieza más despacio y sube poco a poco.')]),
        B(2, 'cc. 3-5', 'Segno y repetición', (1, 1),
          D('cadena', 'Desde el c. 3 se repite', [('segno y |: en el c. 3', False),
                                                  ('tocas hasta la casilla', True)]),
          [('IZQUIERDA', 'Mismas blancas de dos notas: el acorde cambia cada dos tiempos.'),
           ('DERECHA', 'Entra tras un silencio de corchea (cc. 3-4) o de corchea con puntillo '
                       '(c. 5).'),
           ('JUNTAS', 'Cuenta el silencio en voz alta y entra con la izquierda ya puesta.'),
           ('OJO', 'La barra |: del c. 3 marca adónde se vuelve cada vez.')]),
        B(3, 'cc. 6-8', 'Becuadros y tresillo', (2, 2),
          D('fichas', 'Alteraciones de estos compases',
            ['c. 6: La natural (izq.)', 'c. 8: Si natural (izq.)', 'cc. 6 y 8: un bemol suelto (der.)']),
          [('IZQUIERDA', 'Becuadro en el c. 6 (La) y en el c. 8 (Si): sin el bemol de la armadura.'),
           ('DERECHA', 'Un bemol suelto en los cc. 6 y 8; tresillo en el c. 8: tres notas en el '
                       'tiempo de dos.'),
           ('JUNTAS', 'Primero solo las notas alteradas; luego, el compás entero.'),
           ('OJO', 'El cifrado ya lo dice: Do m con La en el bajo (c. 6) y Sol con Si (c. 8).')]),
        B(4, 'cc. 9-12', 'Las casillas', (3, 3),
          D('cadena', 'Las dos vueltas', [('casilla 1 (cc. 10-11)', False), ('↩ al c. 3', False),
                                         ('casilla 2 (c. 12)', True)]),
          [('IZQUIERDA', 'Blancas de dos notas; el c. 11 es de 2/4 y solo lleva una.'),
           ('DERECHA', 'Tresillo en el c. 9. En el c. 11 hay un compás entero de silencio.'),
           ('JUNTAS', '1.ª vez: cc. 9-11 y vuelta al c. 3. 2.ª vez: c. 9 y salto al c. 12.'),
           ('OJO', 'La casilla 1 acaba con :|; la casilla 2 sigue al c. 13.')]),
        B(5, 'cc. 13-19', 'Más semicorcheas', (4, 5),
          D('capas', 'Dos capas a la vez',
            [('Derecha: semicorcheas', 'puntos', AZUL, 8), ('Izquierda: blancas', 'barras', OCRE)]),
          [('IZQUIERDA', 'El c. 13 (2/4) lleva una sola blanca; del c. 14 al 19, dos por compás.'),
           ('DERECHA', 'Semicorcheas ligadas desde el c. 14; tresillo en los cc. 15 y 17.'),
           ('JUNTAS', 'Dos tramos en bucle: cc. 13-16 y cc. 17-19.'),
           ('OJO', 'c. 19: becuadro en las dos manos y calderón sobre la negra del tercer tiempo.')]),
        B(6, 'cc. 20-22', 'D.S. al Coda', (6, 6),
          D('cadena', 'El salto', [('c. 22: D.S. al Coda', False), ('vuelves al segno (c. 3)', False),
                                  ('Coda: c. 23', True)]),
          [('IZQUIERDA', 'Dos blancas por compás; el c. 22 es de 2/4 y lleva una sola.'),
           ('DERECHA', 'Corchea con puntillo y semicorchea (cc. 20-21); bemol suelto al empezar el '
                       'c. 21.'),
           ('JUNTAS', 'Toca los cc. 20-22 y vuelve al c. 3 sin parar: ensaya el salto.'),
           ('OJO', 'No hay "To Coda" impreso: acordad con tu profe dónde se salta.')]),
        B(7, 'cc. 23-29', 'La Coda y el final', (7, 8),
          D('cadena', 'La Coda', [('c. 23: |: y signo de Coda', False),
                                  ('casilla 1 (cc. 26-27)', False), ('casilla 2 (cc. 28-29)', True)]),
          [('IZQUIERDA', 'Los cc. 23-26 repiten las notas de los cc. 18-21; el c. 29, tres notas '
                         'en redonda.'),
           ('DERECHA', 'Las mismas semicorcheas de los cc. 18-21; la última nota viene ligada '
                       'del c. 28.'),
           ('JUNTAS', 'Primero cc. 23-27 y vuelta al c. 23; luego cc. 23-26 y casilla 2.'),
           ('A TEMPO', 'Calderones: c. 24 y c. 29 (en este último, en las dos manos).')]),
    ],
    cortes={1: [269.8, 399.5, 519.0, 634.0], 2: [166.0, 285.8, 423.0]},
    corte_titulo=140.0,
    burb={
        0: [('arriba', 270, 'IZQ', 'Dos notas juntas, en blancas, y el cifrado encima: E♭ = Mi♭, '
                                   'A♭ = La♭.', 0.1),
            ('arriba', 270, 'AMB', 'Tres bemoles: Mi♭ mayor. ♩ = 66 y ningún matiz impreso.', 0.7)],
        1: [('arriba', 300, 'OJO', 'Segno y barra |: en el c. 3: desde aquí se repite. Entra tras '
                                   'el silencio de corchea.', 0.05)],
        2: [('arriba', 270, 'IZQ', 'Becuadros en la izquierda (cc. 6 y 8): La y Si naturales, sin '
                                   'bemol.', 0.1),
            ('arriba', 270, 'DER', 'Bemol suelto en los cc. 6 y 8 y tresillo en el c. 8.', 0.75)],
        3: [('arriba', 330, 'OJO', 'Casilla 1 (cc. 10-11) y vuelta al c. 3; la 2.ª vez, casilla 2 '
                                   '(c. 12). Tresillo en el c. 9.', 0.45)],
        5: [('arriba', 270, 'DER', 'Tresillo en el c. 17 y silencio de semicorchea al empezar el '
                                   'c. 18.', 0.2),
            ('arriba', 270, 'OJO', 'c. 19: becuadro en las dos manos y calderón: aguanta esa '
                                   'negra.', 0.8)],
        6: [('arriba', 300, 'OJO', 'D.S. al Coda tras el c. 22: vuelves al segno del c. 3. No hay '
                                   '"To Coda" impreso.', 0.85)],
        7: [('arriba', 300, 'OJO', 'Signo de Coda y barra |: en el c. 23. Estos compases son '
                                   'iguales a los cc. 18-20.', 0.05)],
        8: [('arriba', 270, 'OJO', 'Casilla 1 (cc. 26-27) y vuelta al c. 23; la 2.ª vez, casilla 2 '
                                   '(cc. 28-29).', 0.1),
            ('arriba', 270, 'AMB', 'Acorde final: redonda con calderón en las dos manos.', 0.85)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Mi♭ mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_your_song.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
