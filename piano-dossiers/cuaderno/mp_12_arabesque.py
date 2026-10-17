# -*- coding: utf-8 -*-
"""Pieza 12 · Arabesque (Burgmuller, op. 100 n.º 2), a cuatro manos. MEDIDO sobre el PDF a zoom
   (4 pags, A4, 9 sistemas, 40 compases numerados): 2/4, Allegro scherzando sin metronomo, sin
   armadura; "Piano" (Primo: DOS pentagramas de sol con la misma melodia, el de arriba una octava
   mas aguda, con 8va) y "Piano 2" (Secondo: sol + fa); Primo en silencio en los cc.1-2; p (c.1),
   f (cc.6, 14, 30, 39), mf (cc.7 y 15), acentos (cc.8, 10, 16), barra de repeticion al empezar el
   c.19, casilla 1. (c.34) y 2. (c.35), "dim. e poco rit." (c.25), "a tempo" con p (c.27),
   "risoluto" (c.39), calderon con acento en el Primo (c.40), final sobre La-Mi; semicorchea."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=12, slug='arabesque', pdf='arabesque_burgmuller_4_manos.pdf', time_sig=(2, 4),
    titulo='Arabesque', autor='J. F. F. Burgmüller · op. 100 n.º 2 · a cuatro manos',
    kicker='Eva · pieza 12 · Arabesque (Burgmüller)', mes='Abril · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=burgmuller+arabesque+op+100+piano+4+hands',
    credito='Partitura: J. F. F. Burgmüller, Arabesque op. 100 (arr. a cuatro manos). '
            'Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'La menor'), ('Compás', '2/4'), ('Tempo', 'Allegro scherzando'),
               ('Figura corta', 'Semicorchea'), ('Compases', '40')],
        total=40,
        secciones=[('A', 1, 18, 'El tema', AZUL), ('B', 19, 26, 'Repetición · notas largas', OCRE),
                   ('C', 27, 35, 'a tempo · casillas', AZUL), ('D', 36, 40, 'Final', OCRE)],
        ideas=[('SECONDO', 'Acordes picados',
                'Empieza solo, con dos acordes cortos por compás. Más adelante toca semicorcheas '
                'ligadas en las dos claves.'),
               ('PRIMO', 'Semicorcheas ligeras',
                'Entra en el c. 3 con cuatro semicorcheas ligadas y una corchea corta. Dos '
                'pentagramas con la misma melodía.'),
               ('LA REPETICIÓN', 'Del c. 19 al c. 34',
                'Barra de repetición al empezar el c. 19; casilla 1 en el c. 34 y casilla 2 en el '
                'c. 35.'),
               ('LOS MATICES', 'p · f · mf · risoluto',
                'Empieza en p; f y mf alternan; "risoluto" en el c. 39 y calderón al final.')],
        especial=[
            'Pone "Allegro scherzando" y el compás es 2/4: dos negras por compás. Sin armadura.',
            'Es a cuatro manos: Primo ("Piano") arriba y Secondo ("Piano 2") debajo.',
            'El Primo calla en los cc. 1-2 y entra en el c. 3. Lleva dos pentagramas de sol: el '
            'de arriba suena una octava más aguda (8va).',
            'Barra de repetición al empezar el c. 19 y casillas 1. y 2. en los cc. 34-35.',
            'En el c. 25 pone "dim. e poco rit." y en el c. 27 "a tempo" (p).',
            'En el c. 39 pone "risoluto" (f) y el último compás lleva calderón y acorde final '
            'sobre La y Mi.'],
        reto='Que las semicorcheas y los acordes picados suenen ligeros y a la vez sin correr: es '
             'un scherzando, juguetón. En el c. 19 se cambian los papeles: melodía larga en el '
             'Primo y semicorcheas en el Secondo.',
        truco='Estudiad por turnos y contad "uno-dos" en voz alta. Antes de tocar, recorred con '
              'el dedo: 19 → 34 → 19 → 35 → 36.',
        sabias='Burgmüller escribió 25 estudios fáciles y progresivos, op. 100, pensados para alumnos. La «Arabesque» es el n.º 2.',
        qr_texto='Escúchala y cuenta "uno-dos": ¿notas el carácter juguetón?', ts=(2, 4)),
    manos=dict(
        titulo='Secondo y Primo', sub='Cada parte se aprende sola. Luego, juntas y despacio.',
        tit_izq='SECONDO · la parte grave', tit_der='PRIMO · la parte aguda',
        izq=[('Acordes picados', 'Al principio, dos acordes cortos por compás: tres notas en sol '
                                 'y dos en fa. Ligeros, contando "uno-dos".'),
             ('Las semicorcheas', 'En los cc. 19-24 y 27-28 las dos manos tocan la misma figura '
                                  'a una octava de distancia. Despacio y parejas.'),
             ('Los cambios de sonido', 'f en los cc. 6, 14 y 30; mf en los cc. 7 y 15; p en el '
                                       'c. 27. Tócalos antes por separado.'),
             ('Con el Primo', 'Juntas, despacio. El Secondo acompaña y escucha al Primo.')],
        der=[('Entrar en el c. 3', 'Los dos primeros compases son de silencio: cuéntalos y entra '
                                   'a tiempo.'),
             ('Semicorcheas ligadas', 'Cuatro semicorcheas ligadas y una corchea corta, ligero. '
                                      'Una sola idea por compás.'),
             ('La octava', 'Los dos pentagramas del Primo llevan la misma melodía; el de arriba '
                           'suena una octava más aguda (8va).'),
             ('Notas largas', 'En los cc. 19-24 canta notas largas ligadas; en los cc. 27-28 '
                              'toca acordes cortos.')],
        tecnica=['Muñeca suelta: ligero y juguetón.',
                 'Cuenta "uno-dos" en cada compás, sin correr.',
                 'Mirad primero el camino de las repeticiones.']),
    bloques=[
        B(1, 'cc. 1-4', 'Entra el Secondo', (0, 0),
          D('cadena', 'Los primeros compases', [('Secondo solo (cc. 1-2)', False),
                                                ('entra el Primo (c. 3)', True)]),
          [('SECONDO', 'Dos acordes cortos por compás, en p. Empieza solo.'),
           ('PRIMO', 'Cuenta dos compases y entra en el c. 3: cuatro semicorcheas y una corchea.'),
           ('JUNTAS', 'Contad "uno-dos" y mirad la primera nota del otro.'),
           ('OJO', 'Allegro scherzando: vivo y juguetón, sin correr.')]),
        B(2, 'cc. 5-9', 'f y mf', (1, 1),
          D('cadena', 'Los matices', [('f (c. 6)', False), ('mf (c. 7)', False), ('acento (c. 8)', True)]),
          [('SECONDO', 'Los acordes siguen picados; en el c. 7 cambian las notas del bajo.'),
           ('PRIMO', 'Empieza el 8va. Semicorcheas en los cc. 5-6 y corcheas ligadas en los cc. 7-9.'),
           ('JUNTAS', 'f en el c. 6 y mf en el c. 7: el sonido baja de golpe.'),
           ('OJO', 'El acento (>) del c. 8 va sobre la nota ligada.')]),
        B(3, 'cc. 10-18', 'f y mf otra vez', (2, 3),
          D('cadena', 'Como los cc. 5-9', [('acento (c. 10)', False), ('f (c. 14)', False),
                                           ('mf (c. 15)', True)]),
          [('SECONDO', 'Acordes picados; en el c. 18 acaba en un acorde largo con puntillo.'),
           ('PRIMO', 'Semicorcheas ligeras y silencios; acento en los cc. 10 y 16.'),
           ('JUNTAS', 'Un sistema cada día: cc. 10-13 y cc. 14-18.'),
           ('OJO', 'f en el c. 14 y mf en el c. 15, como en los cc. 6-7.')]),
        B(4, 'cc. 19-22', 'Empieza la repetición', (4, 4),
          D('capas', 'Dos capas a la vez',
            [('Primo: notas largas', 'barras', AZUL), ('Secondo: semicorcheas', 'puntos', OCRE)]),
          [('SECONDO', 'Ahora tocas semicorcheas ligadas, las dos manos a una octava.'),
           ('PRIMO', 'Notas largas ligadas con 8va: cántalas, el Secondo no tapa.'),
           ('JUNTAS', 'Cuatro compases cada vez, en bucle.'),
           ('OJO', 'Barra de repetición al empezar el c. 19; hay un sostenido en el Secondo.')]),
        B(5, 'cc. 23-26', 'dim. e poco rit.', (5, 5),
          D('cadena', 'El final de la frase', [('notas largas', False), ('dim. e poco rit. (c. 25)', False),
                                               ('corcheas que bajan', True)]),
          [('SECONDO', 'Semicorcheas en los cc. 23-24 y corcheas que bajan en los cc. 25-26.'),
           ('PRIMO', 'Notas largas y, en el c. 25, cuatro corcheas que bajan.'),
           ('JUNTAS', 'Bajad el sonido y frenad un poco a la vez.'),
           ('OJO', 'Hay sostenidos sueltos: léelos antes de tocar.')]),
        B(6, 'cc. 27-30', 'a tempo', (6, 6),
          D('cadena', 'Las indicaciones', [('a tempo y p (c. 27)', False), ('semicorcheas (c. 29)', False),
                                           ('f (c. 30)', True)]),
          [('SECONDO', 'Lleva las semicorcheas en p (cc. 27-28) y vuelve a los acordes (cc. 29-30).'),
           ('PRIMO', 'Solo el pentagrama de arriba, con acordes cortos (cc. 27-28); luego semicorcheas.'),
           ('JUNTAS', 'Recuperad el tempo juntas en el c. 27.'),
           ('A TEMPO', 'f en el c. 30.')]),
        B(7, 'cc. 31-35', 'Las casillas', (7, 7),
          D('cadena', 'El camino', [('c. 34: casilla 1', False), ('↩ al c. 19', False),
                                    ('c. 35: casilla 2', True)]),
          [('SECONDO', 'Acordes picados, igual en las dos casillas.'),
           ('PRIMO', 'Corcheas ligadas y acento en el c. 32; en la casilla 1 una blanca.'),
           ('JUNTAS', 'Recorred el camino con el dedo antes de tocar.'),
           ('OJO', '1.ª vez: casilla 1 y vuelta al c. 19. 2.ª vez: casilla 2, y sigues al c. 36.')]),
        B(8, 'cc. 36-40', 'El final', (8, 8),
          D('cadena', 'Hacia el final', [('semicorcheas que suben', False), ('risoluto en f (c. 39)', False),
                                         ('calderón (c. 40)', True)]),
          [('SECONDO', 'Acordes picados y, en el c. 39, semicorcheas que bajan en f.'),
           ('PRIMO', 'Semicorcheas que suben; en el c. 39 bajan, con f y "risoluto".'),
           ('JUNTAS', 'Los cinco compases seguidos, sin parar.'),
           ('A TEMPO', 'El último compás: acorde final y calderón; soltad a la vez.')]),
    ],
    cortes={1: [385.0], 2: [267.0, 534.0], 3: [264.0, 538.0]},
    corte_titulo=143.0, fin={2: 765.0, 3: 758.0},
    burb={
        0: [('arriba', 330, 'AMB', 'Allegro scherzando, 2/4 y p. Los cc. 1-2 toca solo el Secondo: '
                                   'acordes cortos.', 0.3),
            ('abajo', 330, 'PRIMO', 'Entras en el c. 3: cuatro semicorcheas ligadas y una '
                                    'corchea corta.', 0.62)],
        1: [('arriba', 330, 'PRIMO', 'Aquí empieza el 8va. f en el c. 6 y mf en el c. 7: el '
                                     'sonido baja de golpe.', 0.4)],
        3: [('arriba', 330, 'AMB', 'f en el c. 14 y mf en el c. 15, como en los cc. 6-7. Acento '
                                   'en el c. 16.', 0.3)],
        4: [('arriba', 330, 'OJO', 'Barra de repetición al empezar el c. 19. El Primo canta '
                                   'notas largas y el Secondo toca semicorcheas.', 0.1)],
        5: [('arriba', 300, 'OJO', '"dim. e poco rit." en el c. 25: baja el sonido y frena un '
                                   'poco.', 0.62)],
        6: [('arriba', 330, 'OJO', 'a tempo y p en el c. 27: ahora el Secondo lleva las '
                                   'semicorcheas y el Primo, acordes arriba.', 0.1)],
        7: [('arriba', 330, 'OJO', 'Casilla 1 (c. 34): vuelves al c. 19. Casilla 2 (c. 35): '
                                   'sigues al c. 36.', 0.62)],
        8: [('arriba', 300, 'AMB', 'risoluto y f en el c. 39. En el c. 40, acorde final con '
                                   'calderón.', 0.6)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o inventa dos compases en 2/4')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_arabesque.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
