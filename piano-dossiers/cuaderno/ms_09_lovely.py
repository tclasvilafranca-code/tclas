# -*- coding: utf-8 -*-
"""Pieza 9 · Lovely (Billie Eilish y Khalid), arreglo de Amy Kieran. MEDIDO sobre el PDF de Drive:
   2 paginas A4, 44 compases (numeracion impresa, 5 sistemas + 4), una armadura de un sostenido
   (Mi menor: la melodia empieza y acaba en Mi-Sol), 4/4, negra = 115, sin matices impresos,
   barra de repeticion al abrir el c. 11 y al cerrar el c. 44, semicorchea como figura mas corta
   (cc. 35-37 y 39-40), izquierda en acordes de tres notas (c. 3: Do-Mi-Sol)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=9, slug='lovely', pdf='copia_de_lovely.pdf', time_sig=(4, 4),
    titulo='Lovely', autor='Billie Eilish con Khalid · arreglo de Amy Kieran',
    kicker='Sharifa · pieza 9 · Lovely', mes='Abril · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=billie+eilish+khalid+lovely+piano+tutorial',
    credito='Partitura: arreglo de Amy Kieran (copia de Drive). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'), ('Tempo', '♩ = 115'),
               ('Figura corta', 'Semicorchea'), ('Compases', '44')],
        total=44,
        secciones=[('A', 1, 10, 'Introducción', AZUL),
                   ('B', 11, 18, 'Primera parte (se repite)', OCRE),
                   ('C', 19, 25, 'La melodía sube', AZUL),
                   ('D', 26, 34, 'Segunda parte', OCRE),
                   ('E', 35, 44, 'Final y vuelta', AZUL)],
        ideas=[('DERECHA', 'Mi-Sol sin parar',
                'En la introducción la derecha repite Mi-Sol, Mi-Sol… Es el "reloj" de la canción.'),
               ('IZQUIERDA', 'Acordes largos',
                'La izquierda toca acordes de tres notas, casi siempre redondas o blancas. '
                'Empieza en el c. 3.'),
               ('LA MELODÍA', 'Notas que cantan',
                'Desde el c. 11 la derecha canta con negras y blancas. Hacia el final hay notas '
                'rápidas (semicorcheas, cc. 35-40).'),
               ('LA REPETICIÓN', 'Dos veces',
                'Una barra de repetición abre el c. 11 y otra cierra el c. 44.')],
        especial=[
            'Pone negra = 115: un pulso tranquilo y constante.',
            'La armadura lleva un sostenido (Fa♯): la pieza está en Mi menor.',
            'Los cc. 1 y 2 son solo derecha; la izquierda entra en el c. 3.',
            'Hay ligaduras de unión entre compases: la nota larga no se vuelve a tocar.',
            'Hay una repetición: cc. 11-44 (barras de repetición en el c. 11 y en el c. 44).',
            'No hay matices escritos: elige tú dónde suena más suave y más fuerte.'],
        reto='Que la derecha de la introducción suene pareja, como un reloj, y que la izquierda '
             'entre en el c. 3 sin que se te rompa.',
        truco='Aprende la introducción de memoria (cc. 1-2). Con ella segura, la izquierda y las '
              'notas largas son lo único nuevo.',
        sabias='«Lovely» se publicó en 2018, dentro de la banda sonora de la serie «Por trece '
               'razones» (13 Reasons Why). Billie Eilish la escribió con su hermano Finneas.',
        qr_texto='Escúchala con la partitura delante: sigue la derecha con el dedo.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Solo acordes', 'La izquierda toca acordes de tres notas. Empieza en el c. 3 con '
                              'una redonda ligada: cuenta 1-2-3-4.'),
             ('Un acorde, un golpe', 'Cada acorde se toca con las tres notas a la vez. Pon la mano '
                                     'en la forma y baja las tres juntas.'),
             ('Ligaduras', 'Si hay una ligadura entre dos acordes iguales, no se toca el segundo: '
                           'se deja sonar.'),
             ('De memoria', 'Casi todos los compases tienen un solo acorde. Apréndelos sin '
                            'mirar.')],
        der=[('Mi-Sol, Mi-Sol', 'En los cc. 1-2 la derecha alterna dos notas, en corcheas. '
                                'Toca sin prisa y todas iguales.'),
             ('Una nota más alta', 'En los cc. 4-5 aparece una nota más alta dentro del dibujo. '
                                   'Míralo antes de tocar.'),
             ('La melodía', 'Desde el c. 11, notas largas ligadas. Cántalas por dentro y '
                            'cuéntalas enteras.'),
             ('Notas rápidas', 'En los cc. 35-37 y 39-40 hay semicorcheas: tócalas despacio '
                               'antes de ir a tempo.')],
        tecnica=['Muñeca suelta: en las corcheas de la introducción el sonido sale parejo.',
                 'Pulso de 115 por minuto: usa el metrónomo, empieza más lenta.',
                 'Mira las barras de repetición: la pieza se toca dos veces desde el c. 11.']),
    bloques=[
        B(1, 'cc. 1-5', 'La introducción', (0, 0),
          D('cuenta', 'Un compás de 4/4: 8 corcheas', [('derecha', 4, 2)]),
          [('DERECHA', 'Mi-Sol alternando, en corcheas. En el c. 4 aparece una nota más alta.'),
           ('IZQUIERDA', 'Silencio en los cc. 1-2. En el c. 3 entra un acorde de redonda.'),
           ('JUNTAS', 'Cuenta 1-2-3-4 y entra la izquierda en el c. 3, sin parar.'),
           ('A TEMPO', 'Negra = 115. Empieza mucho más lenta.')]),
        B(2, 'cc. 6-10', 'Sigue el balanceo', (1, 1),
          D('cadena', 'La izquierda', [('acorde largo', False), ('ligado', False),
                                       ('acorde nuevo', True)]),
          [('DERECHA', 'Mismo dibujo que antes: ya lo conoces. Fíjate en cuándo sube.'),
           ('IZQUIERDA', 'Un acorde por compás, algunos ligados al siguiente.'),
           ('JUNTAS', 'Los cinco compases en bucle, sin parar.'),
           ('OJO', 'Al acabar el c. 10 empieza la parte que se repite.')]),
        B(3, 'cc. 11-18', 'Entra la melodía', (2, 3),
          D('cadena', 'La repetición', [('c. 11', False), ('... c. 44', False),
                                        ('vuelve al c. 11', True)]),
          [('DERECHA', 'Cuatro corcheas y una blanca ligada. Cantas antes de tocar.'),
           ('IZQUIERDA', 'Un acorde de redonda por compás, algunos ligados.'),
           ('JUNTAS', 'Una frase de cuatro compases cada vez: cc. 11-14, luego 15-18.'),
           ('OJO', 'La barra de repetición del c. 11 abre la parte que se toca dos veces.')]),
        B(4, 'cc. 19-25', 'La melodía sube', (4, 4),
          D('cadena', 'La melodía', [('blancas', False), ('sube', False), ('nota más alta', True)]),
          [('DERECHA', 'Blancas y negras. Las notas más altas de la frase están en el c. 21.'),
           ('IZQUIERDA', 'Acordes de dos blancas por compás. En los cc. 21 y 25 suben un poco.'),
           ('JUNTAS', 'Un compás cada vez, y luego la frase entera.'),
           ('A TEMPO', 'Cuenta 1-2-3-4: dos blancas por compás.')]),
        B(5, 'cc. 26-36', 'Segunda parte', (5, 6),
          D('cadena', 'Mismo camino', [('c. 26', False), ('parecido a 19-25', False),
                                       ('c. 35 cambia', True)]),
          [('DERECHA', 'Las frases se parecen a las de los cc. 19-25. Reconoce lo que ya sabes.'),
           ('IZQUIERDA', 'Acordes de blancas y de redonda, como en la frase anterior.'),
           ('JUNTAS', 'Dos tramos: cc. 26-30 y cc. 31-36.'),
           ('OJO', 'En el c. 35 llega la parte nueva, con notas más rápidas.')]),
        B(6, 'cc. 37-40', 'Notas rápidas', (7, 7),
          D('cadena', 'En el compás', [('nota larga', False), ('semicorcheas', True),
                                       ('ligadura', False)]),
          [('DERECHA', 'Hay semicorcheas (dos barras). Toca primero solo el dibujo, despacio.'),
           ('IZQUIERDA', 'Un acorde de redonda por compás, a veces ligado.'),
           ('JUNTAS', 'Dos compases cada vez y luego los cuatro.'),
           ('OJO', 'Las ligaduras de unión: la nota ligada no se toca otra vez.')]),
        B(7, 'cc. 41-44', 'Final y vuelta', (8, 8),
          D('cadena', 'El recorrido', [('cc. 41-42', False), ('vuelve la intro', False),
                                       ('repite desde c. 11', True)]),
          [('DERECHA', 'En los cc. 43-44 vuelve el dibujo del principio.'),
           ('IZQUIERDA', 'Silencio en los cc. 43-44: solo suena la derecha.'),
           ('JUNTAS', 'Toca los cc. 41-44 y salta otra vez al c. 11.'),
           ('A TEMPO', 'Tras la segunda vez, acabas en el c. 44.')]),
    ],
    cortes={1: [244.0, 386.0, 527.8, 673.2], 2: [209.2, 375.0, 525.8]},
    corte_titulo=112.8, fin={1: 818.0},
    burb={
        0: [('arriba', 330, 'DER', 'Mi-Sol alternando: ocho corcheas por compás. Parejas y '
                                   'suaves; en el c. 4 aparece una nota más alta.', 0.25),
            ('abajo', 330, 'IZQ', 'La izquierda entra en el c. 3 con un acorde largo ligado: '
                                  'cuenta 1-2-3-4.', 0.6)],
        1: [('arriba', 330, 'AMB', 'Un acorde por compás en la izquierda y el mismo balanceo en la '
                                   'derecha.', 0.4)],
        2: [('arriba', 330, 'OJO', 'La barra de repetición abre el c. 11: de aquí al c. 44 se '
                                   'toca dos veces.', 0.1),
            ('abajo', 270, 'IZQ', 'Acorde de redonda ligado entre los cc. 11 y 12.', 0.2)],
        3: [('arriba', 330, 'DER', 'Frase de cuatro compases: cuenta las notas largas enteras.',
             0.3)],
        4: [('arriba', 330, 'AMB', 'Blancas y negras: dos golpes por compás en la izquierda. '
                                   'La melodía llega a lo más alto en el c. 21.', 0.4)],
        5: [('arriba', 330, 'DER', 'Se parece a la frase de los cc. 19-25: reconoce lo que ya sabes.', 0.2)],
        6: [('arriba', 330, 'OJO', 'En el c. 35 la derecha sube y baja con notas rápidas. '
                                   'Estúdialo sola, despacio.', 0.65)],
        7: [('arriba', 330, 'DER', 'Semicorcheas otra vez (dos barras): como en el '
                                   'c. 35.', 0.1)],
        8: [('arriba', 330, 'OJO', 'La barra de repetición del c. 44 manda volver al c. 11. '
                                   'Después de la segunda vez, acabas aquí.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Mi menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lovely.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
