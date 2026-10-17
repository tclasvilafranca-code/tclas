# -*- coding: utf-8 -*-
"""Pieza 10 · La dispute (Yann Tiersen, de «Amelie»; transcripcion de Michael Jordan). MEDIDO sobre
   el PDF (4 pag. carta; la 1 es portada, la partitura ocupa las pp. 2-4: 14 sistemas, 99 compases,
   el c. 1 es un compas de silencio): 3/4, «Rubato (negra = 120)», tres bemoles (acaba en acorde de
   Do menor con calderon), mp, mf, f, p, reguladores, rit. en el c. 96; izquierda: nota larga y dos
   acordes hasta el c. 50, arpegios de corcheas desde el c. 51; semicorcheas (c. 5). El pentagrama
   de abajo lleva el rotulo «Accordion». Sin repeticiones ni casillas."""
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
        datos=[('Tonalidad', 'Do menor'), ('Compás', '3/4'), ('Tempo', 'Rubato · ♩ = 120'),
               ('Figura corta', 'Semicorchea'), ('Compases', '99')],
        total=99,
        secciones=[('A', 1, 48, 'Vals: nota larga y dos acordes', AZUL),
                   ('B', 49, 88, 'Arpegios en la izquierda', OCRE),
                   ('C', 89, 99, 'Final', VERDE)],
        ideas=[('IZQUIERDA', 'Vals y arpegio',
                'Hasta el c. 50: una nota larga y dos acordes. Desde el c. 51: corcheas en '
                'arpegio.'),
               ('DERECHA', 'La melodía',
                'Notas largas y ligaduras; más adelante, corcheas y alguna semicorchea.'),
               ('RUBATO', '♩ = 120, con libertad',
                'Rubato: el pulso es flexible; puedes frenar y acelerar un poco.'),
               ('LOS MATICES', 'mp · mf · f · p',
                'Sube y baja varias veces; al final, rit. y calderón.')],
        especial=[
            'Pone "Rubato (♩ = 120)" y el compás es 3/4: tres negras por compás.',
            'Tres bemoles en la armadura; acaba en un acorde de Do menor.',
            'El c. 1 es un compás de silencio: cuéntalo.',
            'Hay becuadros (alteraciones) en la melodía y en los acordes.',
            'La izquierda cambia en el c. 51: de acordes a arpegios de corcheas.',
            'Acaba con rit. (c. 96) y un calderón en el c. 99.'],
        reto='Tocar con rubato sin perder la base: la izquierda marca el pulso y la derecha canta '
             'con libertad.',
        truco='Aprende cada mano sola por bloques de un sistema. La partitura repite mucho: '
              'estudia los cambios, no todos los compases.',
        sabias='(No verificado) La partitura dice que es de la película «Amélie». «La dispute» '
               'significa «la disputa» en francés.',
        qr_texto='Escúchala y fíjate en cómo la melodía respira con el rubato.', ts=(3, 4),
        cuenta_pie='Un compás de 3/4: tres golpes, cada uno con dos corcheas. Aquí solo el '
                   'ritmo, sobre una nota cualquiera.'),
    manos=dict(
        titulo='Mano izquierda y mano derecha',
        sub='Cada mano sola, por bloques. Después juntas y despacio.',
        izq=[('Nota larga y dos acordes', 'Hasta el c. 50: una nota grave larga y dos acordes '
                                          'cortos. Cuenta "uno-dos-tres".'),
             ('Cambiar de acorde', 'Mira el acorde que viene y coloca ya la mano.'),
             ('El arpegio', 'Desde el c. 51, corcheas en arpegio. Un compás, despacio, diez '
                            'veces seguidas.'),
             ('Parejo y suave', 'En mp, todas las corcheas iguales: la melodía manda.')],
        der=[('Cantar la melodía', 'Notas largas y ligaduras: cántala por dentro antes de '
                                   'tocarla.'),
             ('Los becuadros', 'Hay alteraciones sueltas: léelas antes de tocar.'),
             ('Las corcheas', 'Más adelante la derecha corre en corcheas. Primero sola y '
                              'despacio.'),
             ('Con rubato', 'Cuando salga con la izquierda, deja respirar la frase al final de '
                            'cada ligadura.')],
        tecnica=['Muñeca suelta: el arpegio sale solo si no aprietas.',
                 'Cuenta "uno-dos-tres" con la izquierda antes de añadir la derecha.',
                 'Estudia por sistemas: hay muchos compases parecidos.']),
    bloques=[
        B(1, 'cc. 1-8', 'Entrada en mp', (0, 0),
          D('cadena', 'Cómo empieza', [('c. 1 silencio', False), ('c. 2 mp', True)]),
          [('IZQUIERDA', 'Una nota larga y dos acordes por compás. Suaves.'),
           ('DERECHA', 'Melodía de notas largas y ligadas.'),
           ('JUNTAS', 'Contad el compás de silencio y entrad a la vez.'),
           ('OJO', 'Un becuadro en la melodía (c. 5).')]),
        B(2, 'cc. 9-32', 'Mf, f y vuelta a mp', (1, 3),
          D('cadena', 'Los matices', [('mf', False), ('f', False), ('mp', True)]),
          [('IZQUIERDA', 'Mismo diseño de nota larga y dos acordes.'),
           ('DERECHA', 'La melodía sube con los reguladores < >.'),
           ('JUNTAS', 'Un sistema cada día.'),
           ('OJO', 'Cambios de matiz: mf, f y mp.')]),
        B(3, 'cc. 33-48', 'Otra vuelta, mf y f', (4, 5),
          D('cadena', 'Los matices', [('mf', False), ('f', True)]),
          [('IZQUIERDA', 'Sigue el vals: nota larga y dos acordes.'),
           ('DERECHA', 'Notas largas y pequeños grupos de corcheas.'),
           ('JUNTAS', 'Un sistema cada vez.'),
           ('OJO', 'Acordes con becuadros: léelos con calma.')]),
        B(4, 'cc. 49-62', 'Llegan los arpegios', (6, 7),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: arpegio', 'puntos', OCRE, 6)]),
          [('IZQUIERDA', 'Desde el c. 51, corcheas en arpegio, en mp y p.'),
           ('DERECHA', 'Notas largas ligadas sobre el arpegio.'),
           ('JUNTAS', 'Primero el arpegio solo, luego la melodía.'),
           ('OJO', 'Lo nuevo: el cambio de acordes a arpegio.')]),
        B(5, 'cc. 63-88', 'Las dos manos en corcheas', (8, 11),
          D('cadena', 'Los matices', [('mf', False), ('p', False), ('mf', True)]),
          [('IZQUIERDA', 'El arpegio continúa; cambia el acorde cada compás.'),
           ('DERECHA', 'Aparecen corcheas ligadas: parejas y suaves.'),
           ('JUNTAS', 'Un sistema cada día; es el tramo más largo.'),
           ('OJO', 'Mucho se parece: fíjate en dónde cambia.')]),
        B(6, 'cc. 89-99', 'f, rit. y calderón', (12, 13),
          D('cadena', 'El final', [('f', False), ('rit.', False), ('p + calderón', True)]),
          [('IZQUIERDA', 'Arpegio hasta el c. 96; luego notas largas.'),
           ('DERECHA', 'Acordes largos ligados al final: cuéntalos enteros.'),
           ('JUNTAS', 'Los dos últimos sistemas, en bucle.'),
           ('A TEMPO', 'rit.: frena poco a poco. Alarga el último acorde.')]),
    ],
    cortes={2: [278.8, 411.0, 543.0], 3: [184.5, 317.5, 450.0, 582.2],
            4: [177.2, 310.2, 442.5, 576.2]},
    inicio={1: 700, 2: 152.2, 4: 38},
    burb={
        0: [('arriba', 330, 'AMB', 'Rubato (♩ = 120), 3/4, en mp. El c. 1 es un compás de '
                                   'silencio: cuéntalo.', 0.1)],
        6: [('arriba', 330, 'IZQ', 'Desde el c. 51 la izquierda toca corcheas en arpegio en vez '
                                   'de acordes.', 0.3)],
        10: [('arriba', 330, 'DER', 'Aquí la derecha también toca corcheas: ligadas, parejas y '
                                    'sin prisa.', 0.3)],
        12: [('arriba', 300, 'AMB', 'f en este sistema.', 0.2)],
        13: [('arriba', 330, 'AMB', 'rit. en el c. 96; p y calderón en el c. 99: el último '
                                    'acorde se alarga.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_la_dispute.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
