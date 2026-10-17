# -*- coding: utf-8 -*-
"""Pieza 3 · Melodische Uebungsstuecke n.º 3, op. 149 (Diabelli), a cuatro manos. MEDIDO: 3
   paginas (Secondo en las pp. 1-2, Primo en las pp. 2-3), 2/4, Moderato sin metronomo, sin
   armadura (Do mayor, con alteraciones), p, f, mf, sf, reguladores, barras de repeticion y un
   calderon final; semicorchea (ritmo con puntillo y notas de adorno en el Primo)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=3, slug='melodische', pdf='melodishe_diabelli_4_manos.pdf', time_sig=(2, 4),
    titulo='Melodische Übungsstücke n.º 3', autor='Anton Diabelli · op. 149 · a cuatro manos',
    kicker='Eva · pieza 3 · Diabelli, op. 149 n.º 3', mes='Diciembre · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=diabelli+melodische+ubungsstucke+op+149+piano+4+hands',
    credito='Partitura: A. Diabelli, op. 149 n.º 3 (Mutopia Project, BSD). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/4'), ('Tempo', 'Moderato'),
               ('Figura corta', 'Semicorchea'), ('Compases', '56')],
        total=56,
        secciones=[('A', 1, 22, 'Primera parte', AZUL), ('B', 23, 44, 'Parte central', OCRE),
                   ('C', 45, 56, 'Final', AZUL)],
        ideas=[('SECONDO', 'Acompaña',
                'Grupos de corcheas ligadas sobre notas sueltas con silencios. Es el '
                'acompañamiento.'),
               ('PRIMO', 'Canta',
                'Empieza con corcheas ligadas y pasa a un diseño de silencio y dos corcheas '
                'por compás.'),
               ('LOS MATICES', 'p · f · mf · sf',
                'Alterna pianos y fuertes, con reguladores y algún sf (acento fuerte).'),
               ('EL FINAL', 'Calderón',
                'Los dos acaban con un calderón en el último compás.')],
        especial=[
            'Pone "Moderato" y el compás es 2/4: dos negras por compás.',
            'Es a cuatro manos: el Secondo (pp. 1-2) y el Primo (pp. 2-3) tienen cada uno su '
            'parte completa.',
            'Hay barras de repetición: antes de tocar, localiza dónde empiezan y dónde acaban.',
            'El Primo lleva ritmo con puntillo y alguna notita de adorno.',
            'Los matices cambian de golpe (p, f, mf) y hay reguladores (< >).',
            'Acaba con un calderón en el último compás.'],
        reto='Que las dos partes encajen: el Primo canta y el Secondo acompaña sin taparlo. Si el '
             'Secondo suena fuerte, el Primo no se oye.',
        truco='Estudiad por turnos: una toca y la otra cuenta "uno-dos" en voz alta. Después '
              'cambiad. Solo cuando las dos sepáis las dos partes, juntas.',
        sabias='Es la n.º 3 de las 28 piezas melódicas a cuatro manos, op. 149, de Diabelli (1781-1858), el editor vienés del vals sobre el que Beethoven escribió sus 33 variaciones.',
        qr_texto='Escúchalo y sigue tu parte con el dedo: ¿dónde respira el Primo?', ts=(2, 4)),
    manos=dict(
        titulo='Secondo y Primo', sub='Cada parte se aprende sola. Luego, juntas y despacio.',
        tit_izq='SECONDO · la parte grave', tit_der='PRIMO · la parte aguda',
        izq=[('Un grupo cada vez', 'Aprende primero un compás de corcheas ligadas de tres en '
                                    'tres. Tócalo despacio, diez veces seguidas sin fallar.'),
             ('Las notas sueltas', 'Abajo hay notas sueltas con silencios. Toca solo esa línea '
                                    'y cuenta "uno-dos" en voz alta.'),
             ('Las dos líneas', 'Júntalas: corcheas encima, notas sueltas debajo, en p.'),
             ('Los cambios', 'Cuida los cambios de matiz: p, f, mf. Cambian de golpe.')],
        der=[('Ligaduras', 'Al principio van corcheas ligadas de dos en dos. Cada ligadura es un '
                           'gesto: sonido en la primera, suave en la segunda.'),
             ('Corchea-silencio', 'Más adelante cada compás empieza con un silencio de corchea. '
                                   'Cuéntalo: el silencio dura, no se salta.'),
             ('Puntillo y adornos', 'En los cc. 34-50 aparecen ritmos con puntillo y notitas de '
                                    'adorno. Estúdialos solos y despacio.'),
             ('Con el Secondo', 'Tocad juntas despacio. El Primo escucha al Secondo.')],
        tecnica=['Muñecas sueltas, dedos curvos y sonido parejo.',
                 'Cuenta en voz alta "uno-dos": cada compás, dos negras.',
                 'Cambiad de parte: así se aprenden las dos.']),
    bloques=[
        B(1, 'Secondo cc. 1-17', 'Primera parte', (0, 1),
          D('capas', 'Dos líneas a la vez',
            [('Corcheas ligadas', 'puntos', OCRE, 6), ('Notas sueltas', 'barras', OCRE)]),
          [('SECONDO', 'Empieza en p; en el c. 9 llega el f. Aprende cada línea sola.'),
           ('PRIMO', 'Escucha este bloque: tu parte lo adorna después.'),
           ('JUNTAS', 'Leed la partitura del otro mientras tocáis la vuestra.'),
           ('OJO', 'Hay barras de repetición: localizadlas antes de tocar.')]),
        B(2, 'Secondo cc. 18-36', 'Segunda parte', (2, 3),
          D('cadena', 'Los matices', [('p', False), ('sf', False), ('mf', False), ('f', True)]),
          [('SECONDO', 'El sf (acento fuerte) del c. 21 y los reguladores: sube y baja.'),
           ('PRIMO', 'Escucha cómo cambian los matices.'),
           ('JUNTAS', 'Un sistema cada día.'),
           ('OJO', 'Dos sostenidos y un becuadro en los cc. 21-22: léelos.')]),
        B(3, 'Secondo cc. 37-56', 'Final del Secondo', (4, 5),
          D('cadena', 'El final', [('p', False), ('regulador <', False), ('f', False),
                                  ('calderón', True)]),
          [('SECONDO', 'Notas repetidas y acordes: más sonido en el f.'),
           ('PRIMO', 'El Primo termina junto contigo.'),
           ('JUNTAS', 'Los dos últimos compases, en bucle.'),
           ('A TEMPO', 'El calderón: soltad el último acorde a la vez.')]),
        B(4, 'Primo cc. 1-22', 'La melodía', (6, 7),
          D('cadena', 'Dos diseños', [('corcheas ligadas', False), ('silencio + 2 corcheas', True)]),
          [('PRIMO', 'Cantar la melodía ligada de los cc. 1-11 y luego el diseño con silencio.'),
           ('SECONDO', 'Acompaña muy suave: p.'),
           ('JUNTAS', 'Primero el c. 1-11, después el c. 12-22.'),
           ('OJO', 'El 8va del Primo: suena una octava más aguda.')]),
        B(5, 'Primo cc. 23-44', 'La parte central', (8, 9),
          D('cadena', 'Lo nuevo', [('sf y mf', False), ('ritmo con puntillo', False),
                                  ('notita de adorno', True)]),
          [('PRIMO', 'Aparecen el puntillo y las notitas de adorno: despacio.'),
           ('SECONDO', 'No tapes al Primo cuando haya adornos.'),
           ('JUNTAS', 'Cada sistema por separado.'),
           ('OJO', 'Hay barras de repetición en este bloque.')]),
        B(6, 'Primo cc. 45-56', 'El final', (10, 10),
          D('cadena', 'El final', [('< f', False), ('sf', False), ('calderón', True)]),
          [('PRIMO', 'Notas largas al final y calderón: cuéntalas enteras.'),
           ('SECONDO', 'Os esperáis para el último acorde.'),
           ('JUNTAS', 'La pieza entera, sin parar.'),
           ('A TEMPO', 'Toda la pieza, una vez al día.')]),
    ],
    cortes={1: [319.5, 468.2, 611.5], 2: [219.5, 373.2, 548.0], 3: [203.2, 344.2]},
    corte_titulo=163.0, inicio={1: 60.5, 2: 60.5, 3: 62.8},
    burb={
        0: [('arriba', 330, 'AMB', 'Moderato, 2/4: dos negras por compás. Empieza en p; cuenta '
                                   '"uno-dos" antes de entrar.', 0.3)],
        1: [('arriba', 300, 'SEC', 'f en el c. 9. Fíjate en las barras de repetición de este '
                                   'sistema.', 0.1)],
        3: [('arriba', 300, 'OJO', 'sf (acento fuerte) y reguladores < >: el sonido sube y baja '
                                   'dentro del compás.', 0.7)],
        5: [('arriba', 300, 'AMB', 'p, f y un calderón al final: el último acorde se alarga.',
             0.9)],
        6: [('arriba', 330, 'PRIMO', 'Empiezas tú, con el 8va: lees lo escrito y suena una octava '
                                     'más aguda. Ligado y cantado.', 0.2)],
        7: [('arriba', 300, 'PRIMO', 'Cada compás empieza con un silencio de corchea: cuéntalo, '
                                     'no lo saltes.', 0.3)],
        9: [('arriba', 300, 'PRIMO', 'Ritmo con puntillo y notita de adorno: despacio y ligero.',
             0.5)],
        10: [('arriba', 300, 'AMB', 'Fin: calderón. Soltad el último acorde juntas.', 0.95)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_melodische.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
