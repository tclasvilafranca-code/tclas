# -*- coding: utf-8 -*-
"""Pieza 12 · Arabesque (Burgmuller, op. 100 n.º 2), a cuatro manos. MEDIDO sobre el PDF (4 pags,
   A4, 9 sistemas, 40 compases numerados): 2/4, Allegro scherzando sin metronomo, sin armadura;
   "Piano" (Primo, dos pentagramas con 8va) arriba y "Piano 2" (Secondo) debajo; p, f (c.6 y c.14),
   mf (c.7 y c.15), barra de repeticion al empezar el c.19 y casillas 1. (c.34) y 2. (c.35),
   "dim. e poco rit." (c.25), "a tempo" con p (c.27), f (c.30), "risoluto" con f (c.39), calderon
   final (c.40); semicorchea."""
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
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '2/4'), ('Tempo', 'Allegro scherzando'),
               ('Figura corta', 'Semicorchea'), ('Compases', '40')],
        total=40,
        secciones=[('A', 1, 18, 'El tema', AZUL), ('B', 19, 26, 'Repetición · notas largas', OCRE),
                   ('C', 27, 35, 'a tempo · casillas', AZUL), ('D', 36, 40, 'Final', OCRE)],
        ideas=[('SECONDO', 'Acordes picados',
                'Empieza solo, con dos acordes cortos por compás. Más adelante toca semicorcheas '
                'ligadas.'),
               ('PRIMO', 'Semicorcheas ligeras',
                'Entra en el c. 3 con grupos de semicorcheas ligadas y una corchea corta. Lleva '
                'el 8va.'),
               ('LA REPETICIÓN', 'Del c. 19 al c. 34',
                'Barra de repetición en el c. 19 y casillas 1 (c. 34) y 2 (c. 35).'),
               ('LOS MATICES', 'p · f · mf · risoluto',
                'Empieza en p; f y mf alternan; "risoluto" en el c. 39 y calderón al final.')],
        especial=[
            'Pone "Allegro scherzando" y el compás es 2/4: dos negras por compás.',
            'Es a cuatro manos: Primo ("Piano") arriba y Secondo ("Piano 2") debajo.',
            'Los cc. 1-2 los toca solo el Secondo; el Primo entra en el c. 3.',
            'Barra de repetición al empezar el c. 19 y casillas 1. y 2. en los cc. 34-35.',
            'En el c. 25 pone "dim. e poco rit." y en el c. 27 "a tempo".',
            'En el c. 39 pone "risoluto" y el último compás lleva calderón.'],
        reto='Que las semicorcheas del Primo y los acordes del Secondo suenen ligeros y a la vez '
             'sin correr: es un scherzando, juguetón.',
        truco='Estudiad por turnos y contad "uno-dos" en voz alta. Antes de tocar, recorred con '
              'el dedo: 19 → 34 → 19 → 35 → 36.',
        sabias='Burgmüller escribió 25 estudios fáciles, op. 100, para alumnos; esta pieza es el '
               'n.º 2. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchala y cuenta "uno-dos": ¿notas el carácter juguetón?', ts=(2, 4)),
    manos=dict(
        titulo='Secondo y Primo', sub='Cada parte se aprende sola. Luego, juntas y despacio.',
        tit_izq='SECONDO · la parte grave', tit_der='PRIMO · la parte aguda',
        izq=[('Acordes picados', 'Al principio, dos acordes cortos por compás. Tócalos ligeros '
                                 'y cuenta "uno-dos".'),
             ('Las semicorcheas del Secondo', 'En los cc. 19-22 y 27-28 tocas semicorcheas '
                                              'ligadas. Despacio y parejas.'),
             ('Los matices', 'f y mf en los cc. 6-7 y 14-15; p en el c. 27. Tócalos antes por '
                             'separado.'),
             ('Con el Primo', 'Juntas, despacio. El Secondo escucha al Primo.')],
        der=[('Entrar en el c. 3', 'Los dos primeros compases son de silencio: cuéntalos y entra '
                                   'a tiempo.'),
             ('Semicorcheas ligadas', 'Cuatro semicorcheas ligadas y una corchea corta, ligero. '
                                      'Una sola idea por compás.'),
             ('El 8va', 'En un pentagrama alto lleva 8va: se lee lo escrito y suena una octava '
                        'más aguda.'),
             ('Notas largas', 'En los cc. 19-22 y 23-26 canta notas largas ligadas.')],
        tecnica=['Muñeca suelta: ligero y juguetón.',
                 'Cuenta "uno-dos" en cada compás, sin correr.',
                 'Mirad primero el camino de las repeticiones.']),
    bloques=[
        B(1, 'cc. 1-9', 'El tema en p', (0, 1),
          D('cadena', 'Los primeros compases', [('Secondo solo', False), ('entra el Primo (c. 3)', False),
                                                ('f y mf', True)]),
          [('SECONDO', 'Dos acordes picados por compás. Empieza solo, en p.'),
           ('PRIMO', 'Entra en el c. 3 con semicorcheas ligadas. Aparece el 8va en el c. 5.'),
           ('JUNTAS', 'Cuatro compases y luego cinco.'),
           ('OJO', 'f en el c. 6 y mf en el c. 7.')]),
        B(2, 'cc. 10-18', 'f y mf otra vez', (2, 3),
          D('cadena', 'Como los cc. 5-9', [('f', False), ('mf', False), ('notas largas', True)]),
          [('SECONDO', 'Acordes picados, dos por compás, como al principio.'),
           ('PRIMO', 'Semicorcheas ligeras y silencios.'),
           ('JUNTAS', 'Un sistema cada día.'),
           ('OJO', 'f en el c. 14 y mf en el c. 15.')]),
        B(3, 'cc. 19-26', 'Empieza la repetición', (4, 5),
          D('capas', 'Dos capas a la vez',
            [('Primo: notas largas', 'barras', AZUL), ('Secondo: semicorcheas', 'puntos', OCRE)]),
          [('SECONDO', 'Ahora toca las semicorcheas ligadas, parejas.'),
           ('PRIMO', 'Notas largas ligadas con 8va: cántalas.'),
           ('JUNTAS', 'Cuatro compases cada vez.'),
           ('OJO', 'Barra de repetición al empezar el c. 19.')]),
        B(4, 'cc. 27-30', 'a tempo', (6, 6),
          D('cadena', 'Las indicaciones', [('dim. e poco rit.', False), ('a tempo (c. 27)', False),
                                           ('f (c. 30)', True)]),
          [('SECONDO', 'Semicorcheas en p; en el c. 29 vuelven los acordes.'),
           ('PRIMO', 'Acordes en los cc. 27-28 y luego semicorcheas.'),
           ('JUNTAS', 'Del c. 25 al c. 30, en bucle.'),
           ('A TEMPO', 'Frena en el c. 25 y recupera el tempo en el c. 27.')]),
        B(5, 'cc. 31-35', 'Las casillas', (7, 7),
          D('cadena', 'El camino', [('c. 34: casilla 1', False), ('↩ al c. 19', False),
                                    ('c. 35: casilla 2', True)]),
          [('SECONDO', 'Acordes picados, igual en las dos casillas.'),
           ('PRIMO', 'Notas ligadas hasta la casilla 1; en la 2 sigue el tema.'),
           ('JUNTAS', 'Recorred el camino con el dedo antes.'),
           ('OJO', '1.ª vez: casilla 1 y vuelta al c. 19. 2.ª vez: casilla 2.')]),
        B(6, 'cc. 36-40', 'El final', (8, 8),
          D('cadena', 'Hacia el final', [('semicorcheas', False), ('risoluto en f', False),
                                         ('calderón', True)]),
          [('SECONDO', 'Acordes picados y, en el c. 39, semicorcheas en f.'),
           ('PRIMO', 'Semicorcheas y, en el c. 39, risoluto en f.'),
           ('JUNTAS', 'Los cinco compases, sin parar.'),
           ('A TEMPO', 'El último compás lleva calderón: soltad juntas.')]),
    ],
    cortes={1: [385.0], 2: [267.0, 534.0], 3: [264.0, 538.0]},
    corte_titulo=143.0, fin={2: 765.0, 3: 758.0},
    burb={
        0: [('arriba', 330, 'AMB', 'Allegro scherzando, 2/4 y p. Los cc. 1-2 toca solo el Secondo: '
                                   'acordes cortos.', 0.3)],
        1: [('arriba', 300, 'PRIMO', 'f en el c. 6 y mf en el c. 7. El 8va suena una octava más '
                                     'aguda.', 0.3)],
        4: [('arriba', 330, 'OJO', 'Barra de repetición al empezar el c. 19. Aquí el Secondo '
                                   'toca las semicorcheas.', 0.1)],
        5: [('arriba', 300, 'OJO', '"dim. e poco rit." en el c. 25: baja el sonido y frena.',
             0.55)],
        7: [('arriba', 330, 'OJO', 'Casilla 1 (c. 34): vuelves al c. 19. Casilla 2 (c. 35): '
                                   'sigues al c. 36.', 0.6)],
        8: [('arriba', 300, 'AMB', 'risoluto y f en el c. 39. Calderón en el último compás.',
             0.55)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o inventa dos compases en 2/4')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_arabesque.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
