# -*- coding: utf-8 -*-
"""Peaches — pieza 5 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Peaches (The Super
   Mario Bros. Movie)", Jack Black, 2 páginas):

     - Do mayor: detrás de la clave no hay nada. Compás de 4/4.
     - LA IZQUIERDA TOCA REDONDAS todo el principio: una nota que dura el
       compás entero, compás tras compás. En el c. 11 aparece la primera con
       sostenido.
     - La derecha lleva corcheas y silencios de corchea, y algún grupo de
       cuatro notas por golpe a partir del c. 13.
     - Los números de compás vienen impresos (5, 9, 13, 15) y hay barras de
       repetición a partir del c. 13.

   Lo que NO se cita nota a nota: la melodía va en corcheas y semicorcheas
   muy juntas; el material melódico va como ANDAMIO en Do mayor y remite a la
   partitura.

   Aviso pedagógico que va escrito en la hoja: a partir del c. 13 la cosa se
   pone mucho más rápida. Esta semana la pieza son los doce primeros compases,
   y eso está dicho en el objetivo para que no parezca que se ha dejado a
   medias.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, corch, objetivo, plan, ordenar, contar,
                      teclado, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=5, nivel='iniciación',
    slug='Peaches', formato='adulto',
    titulo_corto='Peaches', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           '-PEACHES.'),
    yt='https://www.youtube.com/results?search_query=peaches+super+mario+movie+piano',

    ficha=dict(
        titulo='Peaches',
        autor='Jack Black · de la película de Super Mario Bros.',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Mano izq.', 'Redondas'), ('Esta semana', 'cc. 1-12'),
               ('Compases', 'Numerados')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Do mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Lo literal es que la izquierda dura el compás entero.',
        armonia=dict(
            titulo='La pieza se parte en dos por el compás 13',
            tarjetas=[
                ('COMPASES 1-12', 'Lo de esta semana',
                 'La izquierda hace redondas y la derecha canta la melodía. Es lo mismo que en '
                 'Counting Stars, así que ya sabes el gesto.'),
                ('COMPÁS 11', 'El primer sostenido',
                 'Aparece una tecla negra en la izquierda, escrita delante de la nota. Vale solo para '
                 'ese compás.'),
                ('COMPÁS 13', 'Cambia el paso',
                 'A partir de ahí entran grupos de cuatro notas por golpe. Es otra pieza, y no es la '
                 'de esta semana.'),
                ('LA REPETICIÓN', 'Con barras',
                 'Del 13 en adelante hay barras de repetición. Cuando llegues, mira el camino con el '
                 'lápiz antes de tocar.'),
            ],
            pie='Que una pieza se estudie por trozos no es hacer trampa: es lo normal. Doce compases '
                'que suenan bien valen más que veinte a medias, y el resto llega solo cuando estos '
                'estén.',
        ),
        ritmos=[
            ('MANO DERECHA', 'corcheas y algún hueco · andamio',
             corch(['E4', 'G4']) + [n('A4')] + corch(['G4', 'E4']) + [n('D4')],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una nota que dura el compás entero · andamio',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'En los doce primeros compases no hay ni un sostenido ni un bemol, salvo uno suelto en '
            'el compás 11.',
            'La izquierda toca UNA nota por compás y la aguanta los cuatro golpes.',
            'La derecha lleva corcheas y silencios de corchea.',
            'Los números de compás vienen impresos: 5, 9, 13 y 15.',
            'A partir del compás 13 aparecen grupos de cuatro notas por golpe, y la pieza se vuelve '
            'bastante más rápida.',
            'Hay barras de repetición a partir del compás 13.',
        ],
        reto='No arrancar a tocar la página entera. El compás 13 no está a tu nivel todavía, y si lo '
             'intentas ahora lo que se estropea es lo de antes, que sí lo está.',
        truco='Marca con lápiz una raya gorda en el compás 12 y trata la pieza como si se acabara ahí. '
              'Cuando los doce salgan seguidos, sin parar y a tempo, lo hablamos y seguimos. Es la '
              'forma más rápida de acabar tocándola entera.',
        sabias='La canta Bowser en la película, y es una balada de amor a la princesa Peach cantada '
               'por un dragón gigante al piano. Jack Black la grabó de verdad y llegó a la lista de '
               'los cien más escuchados: una canción de dos minutos escrita para hacer gracia.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo el primer minuto: es justo la parte que vas a tocar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El reparto es el mismo que en la pieza anterior: izquierda quieta, derecha en '
              'movimiento. Así que esta semana no hay gesto nuevo que aprender, y por eso se puede '
              'ir un poco más deprisa. Lo único que hay que respetar es dónde acaba la pieza: en el '
              'compás 12.',
        reglas=['LA PIEZA ACABA EN EL COMPÁS 12', 'LA IZQUIERDA AGUANTA CUATRO GOLPES',
                'LOS HUECOS DURAN'],
        bloques=[
            dict(num=1, titulo='La izquierda: una nota por compás', clef='bass',
                 pista='andamio en Do mayor · una redonda y a esperar',
                 sistemas=[
                     dict(cap='a) tocar en el uno y contar cuatro en voz alta sin soltar',
                          events=[n('C3', 'w'), n('A2', 'w'), n('F2', 'w'), n('G2', 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y con el sostenido que aparece en el c. 11 · una sola nota negra en '
                              'doce compases',
                          events=[n('F2', 'w'), n('F#2', 'w'), n('G2', 'w'), n('C3', 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: la melodía, sin correr',
                 pista='andamio · el dibujo de corcheas y huecos es el de tu partitura',
                 sistemas=[
                     dict(cap='a) primero en negras: solo las notas, sin ritmo',
                          events=[n('E4'), n('G4'), n('A4'), n('G4'),
                                  n('E4'), n('D4'), n('C4'), n('E4')],
                          bars=2),
                     dict(cap='b) y ahora con las cortas y el hueco · el hueco es medio golpe y se '
                              'cuenta',
                          events=corch(['E4', 'G4']) + [n('A4')] + corch(['G4', 'E4']) +
                                 [n('D4')] + [{'rest': True, 'dur': 'e'}] + corch(['C4']) +
                                 [n('E4'), n('D4'), n('C4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ PARAMOS EN EL COMPÁS 12',
                 texto='Del 13 en adelante hay grupos de cuatro notas en el tiempo de un golpe. Eso no '
                       'es "un poco más difícil": es otro nivel de velocidad de dedos, y necesita un '
                       'trabajo que todavía no toca. Los doce primeros compases son una pieza entera '
                       'y suenan a la canción. Cuando los tengas, seguimos desde el 13 sin haber '
                       'perdido nada por el camino.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='muy despacio · cuenta los cuatro golpes en voz alta',
                 sistemas=[
                     dict(cap='a) lo que hace la derecha mientras la izquierda aguanta',
                          events=corch(['E4', 'G4']) + [n('A4')] + corch(['G4', 'E4']) +
                                 [n('D4'), n('C4', 'h'), n('E4', 'h')],
                          bars=2),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · dos redondas y nada más',
                          events=[n('C3', 'w'), n('A2', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Peaches · para casa',
            intro='Veinte minutos al día, y solo hasta el compás 12. Lo de después no es de esta '
                  'semana.',
            bloques=[
                objetivo('Los doce primeros compases seguidos, sin pararte, con las dos manos. Del '
                         'compás 13 en adelante, esta semana ni mirarlo.'),
                plan((5, 'La izquierda sola, doce compases, contando cuatro'),
                     (5, 'La derecha en negras, sin el ritmo'),
                     (5, 'La derecha con las corcheas y los huecos'),
                     (5, 'Las dos manos, de cuatro compases en cuatro compases')),
                ordenar(['Las dos manos, cuatro compases seguidos.',
                         'Marcar con lápiz dónde acaba lo de esta semana.',
                         'La izquierda sola, contando cuatro golpes por compás.',
                         'La derecha sola, primero en negras y luego con su ritmo.'],
                        titulo='Pon los pasos en el orden bueno',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                contar([n('E4'), n('G4'), n('A4'), n('G4'), n('E4'), n('D4'), n('C4'), n('E4')],
                       ['¿Cuántos Mi hay?', '¿Cuántas notas hay en total?',
                        '¿Cuál es la nota más grave?'],
                       titulo='Mira y cuenta',
                       pista='es el ejercicio 2a de la hoja de al lado'),
                teclado({0: 1, 2: 2, 4: 3, 5: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'Y pinta la tecla negra que hay justo después de la número 3: es el '
                         'sostenido del compás 11.'],
                        titulo='En el teclado',
                        pista='cuatro blancas y la primera negra del cuaderno'),
                para_clase('Los doce primeros compases con las dos manos, y a qué velocidad te han '
                           'salido sin pararte.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
