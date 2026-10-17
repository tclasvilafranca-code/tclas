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
        secciones=[('A', 1, 2, 'Entrada', AZUL), ('B', 3, 12, 'Segno · repetición · casillas', OCRE),
                   ('C', 13, 22, 'Sigue · D.S. al Coda', AZUL), ('D', 23, 29, 'Coda · final', OCRE)],
        ideas_titulo='Los acordes, de un vistazo',
        ideas=[('CC. 1-2', 'Mi♭ · La♭ · Mi♭ · La♭',
                'Mi♭ mayor (tónica) y La♭ mayor, alternando. En tu partitura: E♭ y A♭.'),
               ('CC. 3-8', 'Mi♭ · La♭ · Si♭ · Do m',
                'Mi♭, La♭ con séptima mayor, Si♭, Sol menor y Do menor. Según el cifrado, el bajo '
                'baja: Do, Si♭, La, La♭ (cc. 5-6).'),
               ('CC. 9-12', 'Mi♭ · Fa m · La♭ · Si♭',
                'Casilla 1: La♭ → Si♭ (dominante, que pide volver). Casilla 2: La♭ → Mi♭, '
                'que descansa.'),
               ('CC. 13-29', 'Do m · Fa m7 · La♭',
                'Do menor, Fa menor con séptima y La♭ con sexta. La Coda repite casi igual los '
                'acordes de los cc. 18-21 y acaba en Mi♭.')],
        ideas_pie='Encima de la partitura los acordes vienen en cifrado americano (A = La, B = Si, '
                  'C = Do, D = Re, E = Mi, F = Fa, G = Sol; ♭ = bemol; "m" = menor; la barra '
                  'indica la nota del bajo). Aquí los llamamos como siempre.',
        especial=[
            'Pone ♩ = 66 (lento) y no trae ningún matiz impreso (ni p, ni f).',
            'Tres bemoles (si♭, mi♭, la♭) al principio de cada pentagrama: Mi♭ mayor.',
            'Segno y barra de repetición en el c. 3; casilla 1 (cc. 10-11) y casilla 2 (c. 12).',
            'Al final del c. 22 pone "D.S. al Coda"; el c. 23 es la Coda, con su repetición.',
            'Hay compases sueltos de 2/4 (cc. 11, 13, 22 y 27) y calderones (cc. 19, 24 y 29).',
            'Semicorcheas con ligaduras, y tresillos en los cc. 8, 9, 15 y 17.'],
        reto='Entrar sin prisa tras los silencios de corchea, con semicorcheas parejas, y no '
             'perderse en el recorrido (segno, casillas, D.S. y Coda).',
        truco='Antes de tocar, sigue el recorrido con el dedo sobre la partitura y dilo en voz '
              'alta. La partitura no imprime "To Coda": acuerda con tu profesora dónde saltas.',
        sabias='Elton John publicó "Your Song" en 1970, con letra de su compañero Bernie Taupin, '
               'y fue su primer gran éxito. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchala con la partitura delante: sigue las repeticiones con el dedo.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Dos notas a la vez', 'La izquierda toca casi siempre dos notas juntas, largas. '
                                    'Practica el par: colócalo sin mirar y suéltalo despacio.'),
             ('El cifrado te guía', 'La letra de encima (E♭ = Mi♭, A♭ = La♭) te dice en qué acorde '
                                    'estás. Léela antes de cada cambio.'),
             ('Los becuadros', 'En los cc. 6 y 8 hay becuadros en la izquierda: esa nota va sin '
                               'bemol. Léela dos veces antes de tocar.'),
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
        B(1, 'cc. 1-2', 'La entrada', (0, 0),
          D('cuenta', '4/4 en semicorcheas: cuatro por golpe', [('un compás', 4, 4)]),
          [('IZQUIERDA', 'Dos notas largas por compás: Mi♭ y La♭ según el cifrado.'),
           ('DERECHA', 'Empieza ya en el c. 1, con corcheas y semicorcheas ligadas.'),
           ('JUNTAS', 'Compás a compás, y después los dos.'),
           ('A TEMPO', '♩ = 66: empieza más despacio.')]),
        B(2, 'cc. 3-8', 'Segno y repetición', (1, 2),
          D('cadena', 'Desde el c. 3 se repite', [('segno y |: en el c. 3', False),
                                                  ('tocas hasta la casilla', True)]),
          [('IZQUIERDA', 'Becuadros en los cc. 6 y 8: la nota va sin bemol.'),
           ('DERECHA', 'Silencio de corchea al empezar; nota de adorno en el c. 5; tresillo en el '
                       'c. 8.'),
           ('JUNTAS', 'Un sistema cada día: cc. 3-5 y cc. 6-8.'),
           ('OJO', 'La barra con puntos del c. 3 marca dónde se vuelve.')]),
        B(3, 'cc. 9-12', 'Las casillas', (3, 3),
          D('cadena', 'Las dos vueltas', [('casilla 1 (cc. 10-11)', False), ('↩ al c. 3', False),
                                         ('casilla 2 (c. 12)', True)]),
          [('IZQUIERDA', 'Los mismos pares largos; en el c. 11 el compás es de 2/4.'),
           ('DERECHA', 'Tresillo en el c. 9; en el c. 11 hay un compás de silencio.'),
           ('JUNTAS', 'Recorre el camino con el dedo antes de tocar.'),
           ('OJO', 'La primera vez, casilla 1 y vuelta; la segunda, casilla 2 y sigues.')]),
        B(4, 'cc. 13-19', 'Sigue la melodía', (4, 5),
          D('capas', 'Dos capas a la vez',
            [('Derecha: semicorcheas', 'puntos', AZUL, 8), ('Izquierda: notas largas', 'barras',
                                                            OCRE)]),
          [('IZQUIERDA', 'El c. 13 es de 2/4: un solo par largo.'),
           ('DERECHA', 'Semicorcheas seguidas con ligaduras; becuadro en el c. 18. Parejo.'),
           ('JUNTAS', 'Dos sistemas: cc. 13-16 y cc. 17-19.'),
           ('OJO', 'Calderón en el c. 19: aguanta esa nota.')]),
        B(5, 'cc. 20-22', 'Hacia la Coda', (6, 6),
          D('cadena', 'El salto', [('c. 22: D.S. al Coda', False), ('vuelves al segno (c. 3)', False),
                                  ('Coda: c. 23', True)]),
          [('IZQUIERDA', 'Pares largos; el c. 22 es de 2/4.'),
           ('DERECHA', 'Notas más largas y ligadas; el c. 22 es un silencio.'),
           ('JUNTAS', 'Estos tres compases en bucle.'),
           ('OJO', 'No hay "To Coda" impreso: acordad el salto en clase.')]),
        B(6, 'cc. 23-29', 'La Coda y el final', (7, 8),
          D('cadena', 'La Coda', [('c. 23: |: y signo de Coda', False),
                                  ('casilla 1 (cc. 26-27)', False), ('casilla 2 (cc. 28-29)', True)]),
          [('IZQUIERDA', 'Pares largos; el último compás es un acorde con calderón.'),
           ('DERECHA', 'Los cc. 23-25 se parecen a los cc. 18-20: reconócelos.'),
           ('JUNTAS', 'Dos sistemas: cc. 23-25 y cc. 26-29.'),
           ('A TEMPO', 'Calderón en los cc. 24 y 29: alarga el último acorde.')]),
    ],
    cortes={1: [269.8, 399.5, 519.0, 634.0], 2: [166.0, 285.8, 423.0]},
    corte_titulo=140.0,
    burb={
        0: [('arriba', 270, 'AMB', 'Tres bemoles: Mi♭ mayor. ♩ = 66, lento, sin matices impresos.', 0.1),
            ('abajo', 270, 'IZQ', 'Dos notas largas por compás. Arriba, el cifrado: E♭ = Mi♭, '
                                  'A♭ = La♭.', 0.25)],
        1: [('arriba', 300, 'OJO', 'Segno y barra de repetición: aquí empieza lo que se repite.',
             0.05)],
        2: [('arriba', 300, 'IZQ', 'Becuadros en la izquierda (cc. 6 y 8): esa nota va sin bemol.',
             0.1)],
        3: [('arriba', 300, 'OJO', 'Casillas: la 1.ª vez toca la casilla 1 y vuelve al c. 3; la 2.ª, '
                                   'la casilla 2.', 0.6)],
        4: [('arriba', 300, 'AMB', 'El c. 13 es de 2/4: cuenta 1-2 y entra.', 0.05)],
        6: [('arriba', 300, 'OJO', 'Al final del c. 22: D.S. al Coda. Vuelves al segno del c. 3.',
             0.8)],
        7: [('arriba', 300, 'OJO', 'Aquí empieza la Coda (signo sobre el c. 23). No hay "To Coda" '
                                   'impreso.', 0.05)],
        8: [('arriba', 300, 'AMB', 'Casillas de la Coda; el último acorde lleva calderón.', 0.8)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Mi♭ mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_your_song.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
