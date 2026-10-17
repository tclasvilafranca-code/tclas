# -*- coding: utf-8 -*-
"""Pieza 10 · La dispute (Yann Tiersen, de «Amelie»; transcripcion de Michael Jordan). MEDIDO sobre
   el PDF (4 pag. carta; la 1 es portada, la partitura ocupa las pp. 2-4: 14 sistemas, 99 compases;
   el c. 1 es un compas de silencio): 3/4, «Rubato (negra = 120)», tres bemoles; acaba con calderon
   (rit. en el c. 96). Izquierda: nota grave larga y dos acordes (cc. 2-50), arpegios de seis corcheas
   desde el c. 51. Derecha: notas largas (cc. 2-26), dos notas a la vez (cc. 27-50), notas largas
   (51-74), seis corcheas por compas (75-96). Dobles barras tras los cc. 26, 50 y 74. Matices: mp
   cc. 2, 27, 49; mf cc. 11, 35, 67, 83; f cc. 19, 43, 91; p cc. 51, 74, 99. Semicorcheas en el
   c. 5. Sin repeticiones ni casillas. El pentagrama de abajo lleva el rotulo «Accordion»."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=10, slug='la_dispute', pdf='yann_tiersen_la_dispute_amelie_pdf.pdf', time_sig=(3, 4),
    titulo='La dispute', autor='Yann Tiersen · de la película «Amélie» · transcr. M. Jordan',
    kicker='Eva · pieza 10 · La dispute (Tiersen)', mes='Marzo · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=yann+tiersen+la+dispute+amelie+piano',
    credito='Partitura: Y. Tiersen, La dispute, transcr. M. Jordan. Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do menor'), ('Compás', '3/4'), ('Tempo', 'Rubato'),
               ('Figura corta', 'Semicorchea'), ('Compases', '99')],
        total=99,
        secciones=[('A', 1, 26, 'Melodía y vals', AZUL),
                   ('B', 27, 50, 'Dos notas a la vez', OCRE),
                   ('C', 51, 74, 'Arpegios', VERDE),
                   ('D', 75, 99, 'Corcheas y final', AZUL)],
        ideas=[('IZQUIERDA', 'Vals y arpegio',
                'Cc. 2-50: nota grave larga y dos acordes (en 2 y 3). Desde el c. 51: arpegios '
                'de seis corcheas.'),
               ('DERECHA', 'Melodía y acordes',
                'Notas largas ligadas; dos notas a la vez (cc. 27-50); corcheas (cc. 75-96).'),
               ('RUBATO', 'Negra = 120',
                'El pulso es flexible: se frena y se acelera un poco. La base la marca la '
                'izquierda.'),
               ('LOS MATICES', 'mp · mf · f · p',
                'mp cc. 2, 27, 49 · mf cc. 11, 35, 67, 83 · f cc. 19, 43, 91 · p cc. 51, 74, 99.')],
        especial=[
            'Pone "Rubato" con la negra a 120, y el compás es 3/4: tres negras por compás.',
            'Tres bemoles en la armadura (si, mi y la bemol); acaba en un acorde de Do menor.',
            'El c. 1 es un compás de silencio: cuéntalo.',
            'Dobles barras tras los cc. 26, 50 y 74: cambia la textura.',
            'Becuadros en la melodía y en los acordes; semicorcheas ligadas en el c. 5.',
            'Acaba con rit. (c. 96) y un calderón en el c. 99. No hay repeticiones.'],
        reto='Tocar con rubato sin perder la base: la izquierda marca el pulso y la derecha canta '
             'con libertad.',
        truco='Los cc. 33-48 llevan en la izquierda lo mismo que los cc. 9-24: aprende uno y '
              'tendrás el otro. Estudia por sistemas, no compás a compás.',
        sabias='(No verificado) La partitura dice que es de la película «Amélie». «La dispute» '
               'significa «la disputa» en francés.',
        qr_texto='Escúchala y fíjate en cómo la melodía respira con el rubato.', ts=(3, 4),
        cuenta_pie='Un compás de 3/4: tres golpes, cada uno con dos corcheas. Aquí solo el '
                   'ritmo, sobre una nota cualquiera.'),
    manos=dict(
        titulo='Mano izquierda y mano derecha',
        sub='Cada mano sola, por bloques. Después juntas y despacio.',
        izq=[('Nota larga y dos acordes', 'Cc. 2-50: una nota grave larga en el 1 y dos acordes '
                                          'cortos en el 2 y el 3. Cuenta "uno-dos-tres".'),
             ('Cambiar de nota grave', 'La nota grave cambia cada dos compases (Mi bemol, Re, Fa, '
                                       'Do...). Mira la que viene y coloca ya la mano.'),
             ('El arpegio', 'Desde el c. 51, seis corcheas ligadas por compás. Un compás, '
                            'despacio, diez veces seguidas.'),
             ('Parejo y suave', 'Todas las corcheas iguales y en p: la melodía manda.')],
        der=[('Cantar la melodía', 'Notas largas con ligaduras: cántalas por dentro antes de '
                                   'tocarlas.'),
             ('Dos notas a la vez', 'Cc. 27-50: dos notas juntas. Toca las dos con el mismo '
                                    'peso y cuida los becuadros.'),
             ('Las corcheas', 'Cc. 75-96: seis corcheas ligadas por compás, como la izquierda. '
                              'Primero sola y despacio.'),
             ('Con rubato', 'Cuando salga con la izquierda, deja respirar la frase al acabar '
                            'cada ligadura.')],
        tecnica=['Muñeca suelta: el arpegio sale solo si no aprietas.',
                 'Cuenta "uno-dos-tres" con la izquierda antes de añadir la derecha.',
                 'Estudia por sistemas: hay muchos compases parecidos.']),
    bloques=[
        B(1, 'cc. 1-8', 'Entrada en mp', (0, 0),
          D('cadena', 'Cómo empieza', [('c. 1 silencio', False), ('c. 2 mp', False),
                                       ('c. 5 semicorcheas', True)]),
          [('IZQUIERDA', 'Nota grave larga y dos acordes cortos por compás. Cuenta 1-2-3.'),
           ('DERECHA', 'Notas largas ligadas. En el c. 5, becuadro y semicorcheas ligadas.'),
           ('JUNTAS', 'Contad el compás de silencio y entrad a la vez, en mp.'),
           ('OJO', 'Becuadros en los acordes de la izquierda (cc. 4-5).')]),
        B(2, 'cc. 9-24', 'mf y f', (1, 2),
          D('cadena', 'Los matices', [('c. 11 mf', False), ('c. 19 f', True)]),
          [('IZQUIERDA', 'Misma figura. La nota grave sube a Fa en los cc. 11-12 y 19-20.'),
           ('DERECHA', 'Frases de dos compases con ligadura: respira entre una y otra.'),
           ('JUNTAS', 'Un sistema cada día, y después los dos seguidos.'),
           ('OJO', 'El sonido crece: mf en el c. 11 y f en el c. 19.')]),
        B(3, 'cc. 25-32', 'Doble barra y mp', (3, 3),
          D('cadena', 'Cambia la textura', [('c. 26 doble barra', False), ('c. 27 mp', False),
                                            ('dos notas a la vez', True)]),
          [('IZQUIERDA', 'Sigue el vals: nota grave larga y dos acordes.'),
           ('DERECHA', 'Desde el c. 27 toca dos notas a la vez; cuida los becuadros.'),
           ('JUNTAS', 'Cuatro compases cada vez, en mp.'),
           ('OJO', 'La doble barra entre los cc. 26 y 27 marca otra parte.')]),
        B(4, 'cc. 33-48', 'Otra vez mf y f', (4, 5),
          D('cadena', 'Los matices', [('c. 35 mf', False), ('c. 43 f', True)]),
          [('IZQUIERDA', 'Es la misma que en los cc. 9-24: aprendida una, tienes la otra.'),
           ('DERECHA', 'Dos notas a la vez, ligadas; reguladores largos en los cc. 43-48.'),
           ('JUNTAS', 'Comparad con los cc. 9-24: cambia la derecha.'),
           ('OJO', 'mf en el c. 35 y f en el c. 43.')]),
        B(5, 'cc. 49-69', 'Llegan los arpegios', (6, 8),
          D('capas', 'Dos capas a la vez',
            [('Derecha: notas largas', 'barras', AZUL),
             ('Izquierda: arpegio', 'puntos', OCRE, 6)]),
          [('IZQUIERDA', 'Desde el c. 51, seis corcheas ligadas por compás. Un compás, diez '
                         'veces.'),
           ('DERECHA', 'Notas largas ligadas sobre el arpegio: cuéntalas enteras.'),
           ('JUNTAS', 'Primero el arpegio solo; añade la melodía de dos en dos compases.'),
           ('OJO', 'mp en el c. 49, p en el c. 51 y mf en el c. 67.')]),
        B(6, 'cc. 70-88', 'Corcheas en las dos manos', (9, 11),
          D('capas', 'Dos capas a la vez',
            [('Derecha: corcheas', 'puntos', AZUL, 6), ('Izquierda: arpegio', 'puntos', OCRE, 6)]),
          [('IZQUIERDA', 'El arpegio sigue; cambia de acorde cada uno o dos compases.'),
           ('DERECHA', 'Desde el c. 75, seis corcheas ligadas por compás: parejas, sin prisa.'),
           ('JUNTAS', 'Un sistema cada día: no frenes al cambiar de compás.'),
           ('OJO', 'Doble barra tras el c. 74 (p) y mf en el c. 83.')]),
        B(7, 'cc. 89-99', 'f, rit. y calderón', (12, 13),
          D('cadena', 'El final', [('c. 91 f', False), ('c. 96 rit.', False),
                                   ('c. 99 p + calderón', True)]),
          [('IZQUIERDA', 'Arpegio hasta el c. 96; en los cc. 97-99, notas largas ligadas.'),
           ('DERECHA', 'Corcheas hasta el c. 96; luego notas largas y un acorde con calderón.'),
           ('JUNTAS', 'Los cuatro últimos compases, en bucle.'),
           ('A TEMPO', 'rit.: frena poco a poco. Alarga el último acorde en p.')]),
    ],
    cortes={2: [278.8, 411.0, 543.0], 3: [184.5, 317.5, 450.0, 582.2],
            4: [177.2, 310.2, 442.5, 576.2]},
    inicio={1: 700, 2: 152.2, 4: 38},
    burb={
        0: [('arriba', 200, 'AMB', 'Rubato, negra = 120, en 3/4. El c. 1 es un compás de '
                                   'silencio: cuéntalo.', 120),
            ('arriba', 230, 'DER', 'c. 5: becuadro y semicorcheas ligadas, la figura más rápida '
                                   'de la pieza.', 421),
            ('abajo', 330, 'IZQ', 'Nota grave larga en el 1 y dos acordes cortos en el 2 y el 3. '
                                  'Los acordes, suaves.', 277)],
        1: [('arriba', 330, 'AMB', 'mf en el c. 11 (y f en el c. 19). Los reguladores < > hacen '
                                   'subir y bajar el sonido.', 213)],
        3: [('arriba', 250, 'OJO', 'Doble barra entre los cc. 26 y 27: otra parte, en mp.', 209),
            ('arriba', 300, 'DER', 'Desde el c. 27 la derecha toca dos notas a la vez: mismo '
                                   'peso en las dos.', 332)],
        5: [('arriba', 330, 'AMB', 'f en el c. 43 con un regulador largo: no te apresures al '
                                   'llegar al final del sistema.', 215)],
        6: [('arriba', 250, 'OJO', 'Doble barra tras el c. 50 y p en el c. 51: cambia la '
                                   'textura.', 209),
            ('abajo', 330, 'IZQ', 'Desde el c. 51: seis corcheas ligadas por compás, en arpegio. '
                                  'Parejo y suave.', 266)],
        7: [('arriba', 330, 'IZQ', 'En el c. 59 el arpegio cambia de posición y empieza en Fa: '
                                   'mira antes dónde pones la mano.', 330)],
        9: [('arriba', 330, 'OJO', 'Doble barra tras el c. 74, con p: desde el c. 75 la derecha '
                                   'toca corcheas.', 439)],
        10: [('arriba', 330, 'DER', 'Seis corcheas ligadas por compás, como la izquierda. '
                                    'Parejas y sin prisa.', 200)],
        12: [('arriba', 330, 'AMB', 'Regulador en los cc. 89-90 y f en el c. 91: el punto más '
                                    'fuerte del final.', 227)],
        13: [('arriba', 330, 'AMB', 'rit. en el c. 96: frena poco a poco. En el c. 99, p y '
                                    'calderón.', 90),
             ('abajo', 330, 'AMB', 'El último acorde se alarga: suéltalo juntas, con calma.',
              532)],
    },
    marcas=[(2, 421, 186, 28, 22, 1, 1, 'ovalo'), (2, 210, 609, 14, 100, 3, 1, 'caja'),
            (3, 209, 383, 14, 95, 5, 1, 'caja'), (4, 439, 122, 14, 85, 6, 1, 'caja'),
            (4, 95, 658, 36, 11, 7, 1, 'caja'), (4, 532, 645, 80, 85, 7, 2, 'caja')],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_la_dispute.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
