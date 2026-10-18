# -*- coding: utf-8 -*-
"""Pieza 2 · Romance (Diabelli, op. 163 n.º 1, mov. 2), a cuatro manos. MEDIDO sobre el PDF de
   free-scores (2 paginas, 24 compases en 6 sistemas de 4): sin armadura (Do mayor), 2/2 (¢),
   Andantino sin metronomo, Primo con 8va, barra de repeticion al final del c. 8, notas de adorno
   (cc. 3, 7...), matices p dolce, cresc., f, p, mf, mp, pp y calderon final; semicorchea."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_c = lambda n: {'pitch': 'B4', 'dur': 'e', 'beam': n // 4}
SPEC = dict(
    num=8, slug='romance', pdf='romance_4_manos.pdf', time_sig=(2, 2),
    titulo='Romance', autor='Anton Diabelli · op. 163 n.º 1, 2.º mov. · a cuatro manos',
    kicker='Sharifa · pieza 8 · Romance (Diabelli)', mes='Marzo · 2.ª quincena – Abril',
    yt='https://www.youtube.com/results?search_query=diabelli+romance+op+163+piano+4+hands',
    credito='Partitura: A. Diabelli, op. 163 n.º 1 (free-scores.com). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/2'), ('Tempo', 'Andantino'),
               ('Figura corta', 'Semicorchea'), ('Compases', '24')],
        total=24,
        secciones=[('A', 1, 8, 'Primera parte (se repite)', AZUL),
                   ('B', 9, 16, 'Cresc. y f', OCRE),
                   ('C', 17, 24, 'mf → pp y calderón', AZUL)],
        ideas=[('PRIMO', 'La melodía, arriba',
                'Notas largas ligadas, con alguna notita de adorno. Va con 8va: suena una octava '
                'más aguda de lo escrito.'),
               ('SECONDO', 'Corcheas y bajo',
                'Abajo hay una nota larga y, encima, ocho corcheas por compás que suben y bajan '
                'suaves y ligadas.'),
               ('LOS MATICES', 'p dolce → f → pp',
                'Empieza suave y dulce, crece hasta el f y acaba en pp con un calderón.'),
               ('LA REPETICIÓN', 'Los cc. 1-8, dos veces',
                'Una barra de repetición al final del c. 8 manda volver al principio.')],
        especial=[
            'Pone "Andantino" y "p dolce": paso tranquilo y sonido dulce.',
            'El compás es 2/2 (¢): dos golpes por compás, cada uno de blanca.',
            'Es a cuatro manos: Primo arriba y Secondo abajo.',
            'Los cc. 1-8 se tocan dos veces (barra de repetición en el c. 8).',
            'Hay notas de adorno (notitas pequeñas), por ejemplo en los cc. 3 y 7.',
            'Acaba con un calderón: el último acorde se alarga.'],
        reto='Tocar a dos como si fuera una sola persona: respirar juntas, crecer juntas en el '
             'cresc. y entrar juntas después de cada nota larga.',
        truco='Antes de empezar, contad en voz alta "uno-dos" las dos y mirad la primera nota del '
              'otro. Al final de cada frase, respirad a la vez.',
        sabias='Diabelli (1781-1858) fue editor de música en Viena. Beethoven escribió sus 33 variaciones, op. 120, sobre un vals suyo. Esta pieza es de sus seis sonatas a cuatro manos, op. 163.',
        qr_texto='Escúchala y fíjate en cómo el Secondo sostiene al Primo.', ts=(2, 2),
        cuenta_pie='Un compás de 2/2: dos golpes de blanca, cada uno con cuatro corcheas. Aquí '
                   'solo el ritmo, sobre una nota cualquiera.',
        ritmos=[('LA CUENTA', '2/2 · dos golpes', [_c(i) for i in range(8)], OCRE, 'treble',
                 None)]),
    manos=dict(
        titulo='Secondo y Primo',
        sub='Cada parte se aprende sola. Luego os cambiáis de parte y juntas, despacio.',
        tit_izq='SECONDO · la parte grave', tit_der='PRIMO · la parte aguda',
        izq=[('El bajo, primero', 'Abajo hay notas largas (redondas y blancas). Toca solo esa '
                                   'línea contando "uno-dos" por compás.'),
             ('Las corcheas que ruedan', 'Encima, ocho corcheas por compás, ligadas y suaves. '
                                          'Estúdialas solas, despacio y parejas.'),
             ('Las dos líneas juntas', 'Cuando cada línea salga sola, júntalas: las corcheas '
                                       'encima de la nota larga.'),
             ('Matices', 'Empieza p dolce y "sempre legato" (todo ligado). En el c. 7 llega el f: '
                         'no pierdas la calidad del sonido.')],
        der=[('Cantar la melodía', 'La melodía va en blancas y negras con ligaduras. Cántala por '
                                   'dentro antes de tocarla.'),
             ('Los adornos', 'En los cc. 3 y 7 hay una notita pequeña pegada a la principal: '
                             'rápida y ligera, justo antes del pulso.'),
             ('El 8va', 'Todo el Primo va con 8va: lees lo escrito, suena una octava más '
                        'aguda.'),
             ('Con el Secondo', 'Tocad juntas despacio. El Primo escucha al Secondo: la melodía '
                                'canta sobre el acompañamiento.')],
        tecnica=['Brazos sueltos y espalda recta: dos personas en un banco necesitan sitio.',
                 'Contad en voz alta "uno-dos" antes de empezar, juntas.',
                 'Cambiad de parte: así se aprenden las dos.']),
    bloques=[
        B(1, 'cc. 1-4', 'La frase de entrada', (0, 0),
          D('capas', 'Tres capas a la vez (un compás)',
            [('Primo: melodía', 'barras', AZUL), ('Secondo: corcheas', 'puntos', OCRE, 8),
             ('Secondo: bajo', 'barras', OCRE)]),
          [('SECONDO', 'Bajo largo y ocho corcheas por compás, p dolce y todo ligado.'),
           ('PRIMO', 'La melodía, en p dolce. Notas largas: cuéntalas enteras.'),
           ('JUNTAS', 'Empezad a la vez y respirad juntas al final del c. 4.'),
           ('OJO', 'El c. 3 lleva una notita de adorno: ligera y pegada.')]),
        B(2, 'cc. 5-8', 'Se repite: dolce → f', (1, 1),
          D('cadena', 'El recorrido', [('cc. 1-8', False), ('repite', False), ('luego cc. 9-24',
                                                                          True)]),
          [('SECONDO', 'Cresc.: más sonido poco a poco hasta el f del c. 7.'),
           ('PRIMO', 'En el c. 7, f y una notita de adorno antes de la nota principal.'),
           ('JUNTAS', 'Los cc. 5-8 y la barra de repetición: ¡volved al c. 1!'),
           ('OJO', 'La barra al final del c. 8 manda volver al principio.')]),
        B(3, 'cc. 9-12', 'Vuelve en p y crece', (2, 2),
          D('cadena', 'Los matices', [('p', False), ('cresc.', False), ('más sonido', True)]),
          [('SECONDO', 'Vuelve el p. En el c. 11 empieza el cresc.'),
           ('PRIMO', 'La melodía de los cc. 1-4 con notas cambiadas: léela con cuidado.'),
           ('JUNTAS', 'Dos compases cada vez, y luego los cuatro.'),
           ('OJO', 'El cresc. es poco a poco: no llegues al f antes de tiempo.')]),
        B(4, 'cc. 13-16', 'Cresc. y f', (3, 3),
          D('cadena', 'De fuerte a suave', [('cresc.', False), ('f', True), ('p', False)]),
          [('SECONDO', 'f en el c. 15 y p en el c. 16: el cambio es de golpe.'),
           ('PRIMO', 'La melodía sube con el cresc. y baja otra vez.'),
           ('JUNTAS', 'Tocad el c. 15 y el c. 16 en bucle: del f al p.'),
           ('OJO', 'Cuida la nota alterada (bemol y becuadro) de este sistema.')]),
        B(5, 'cc. 17-20', 'Sonido medio', (4, 4),
          D('cadena', 'Los matices', [('mf', True), ('mp', False)]),
          [('SECONDO', 'mf: sonido medio-fuerte; en el c. 20 baja a mp.'),
           ('PRIMO', 'Dos notas de adorno en los cc. 19-20: ligeras.'),
           ('JUNTAS', 'Dos compases cada vez, con el matiz.'),
           ('OJO', 'Los reguladores (< >) suben y bajan el sonido dentro del compás.')]),
        B(6, 'cc. 21-24', 'Final: p, pp y calderón', (5, 5),
          D('cadena', 'El final', [('p', False), ('pp', False), ('calderón', True)]),
          [('SECONDO', 'Las corcheas se acaban y quedan negras sueltas: espacio y calma.'),
           ('PRIMO', 'El último compás es una nota larga con calderón.'),
           ('JUNTAS', 'Mirad al compañero para soltar el último acorde a la vez.'),
           ('A TEMPO', 'Toda la pieza, con la repetición, sin parar.')]),
    ],
    cortes={1: [324.8, 574.8], 2: [299.5, 547.0]}, corte_titulo=105.2,
    fin={1: 798, 2: 798},
    burb={
        0: [('arriba', 330, 'AMB', 'Andantino, p dolce: tranquila y dulce. El compás es 2/2: '
                                   'cuenta un golpe por blanca.', 0.2),
            ('abajo', 300, 'SEC', 'Ocho corcheas por compás sobre una nota larga, ligado y suave.',
             0.3)],
        1: [('arriba', 330, 'OJO', 'La barra de repetición del c. 8 manda volver al c. 1: '
                                   'tocad dos veces los cc. 1-8.', 0.95),
            ('abajo', 300, 'PRIMO', 'La notita pequeña del c. 7 (adorno) va pegada a la '
                                    'principal: ligera.', 0.6)],
        2: [('arriba', 300, 'AMB', 'p y, desde el c. 11, cresc.: más sonido poco a poco.', 0.5)],
        3: [('arriba', 330, 'OJO', 'f en el c. 15 y p en el c. 16: el cambio es de golpe, no '
                                   'poco a poco.', 0.65)],
        4: [('arriba', 300, 'AMB', 'mf en los cc. 17 y 19, y mp en el c. 20.', 0.5)],
        5: [('arriba', 330, 'OJO', 'p, pp y calderón: el último acorde se alarga y se apaga '
                                   'solo.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_romance.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
