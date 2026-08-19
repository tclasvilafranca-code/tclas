# -*- coding: utf-8 -*-
"""Peaches (Super Mario Bros. Movie) — pieza 3 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (2 páginas, sin arreglista
   impreso, "Jack Black" como autor):

     - Do mayor: detrás de la clave no hay nada.
     - 4/4. No imprime tempo, así que en la ficha va "Carácter", no "Tempo".
     - Los doce primeros compases: la IZQUIERDA HACE REDONDAS, una por compás,
       y nada más. Todo el trabajo es de la derecha.
     - En el c. 11 aparece un sostenido escrito delante del acorde de la
       izquierda: la única alteración de esa página.
     - En el c. 13 hay barra de repetición y la escritura cambia: la derecha
       pasa a corcheas y semicorcheas seguidas y la izquierda empieza a andar.

   El archivo es EL MISMO que el de José María (md5 idéntico). Lo literal
   coincide; lo inventado no: aquí el andamio de la derecha se mueve por grados
   conjuntos y en el de José María va por saltos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, semi, reto, plan, rodear, unir, colorear, acuerdate,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=3, nivel='intermedio', slug='Peaches',
    formato='adulto',
    titulo_corto='Peaches', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source', '-PEACHES.'),
    yt='https://www.youtube.com/results?search_query=peaches+super+mario+piano+easy',

    ficha=dict(
        titulo='Peaches',
        autor='Jack Black · de la película de Super Mario Bros.',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Izquierda', 'Redondas'),
               ('Páginas', 'Dos')],
        titulo_ritmos='El reparto de las dos manos',
        pie_ritmos='Andamio en Do mayor. Lo literal es la forma: una redonda por compás en la '
                   'izquierda durante doce compases. Las notas concretas están en tu partitura.',
        armonia=dict(
            titulo='Una pieza partida en dos mitades',
            tarjetas=[
                ('HASTA EL C. 12', 'La izquierda espera',
                 'Una redonda por compás y ya está. Doce compases en los que la mano izquierda '
                 'solo tiene que llegar a tiempo y aguantar.'),
                ('DESDE EL C. 13', 'Cambia todo',
                 'Hay barra de repetición y la escritura se aprieta: corcheas y semicorcheas '
                 'seguidas en la derecha, y la izquierda empieza a moverse.'),
                ('EL C. 11', 'La única alteración',
                 'Un sostenido escrito delante del acorde de la izquierda. Es la única tecla negra '
                 'de la primera página: márcala.'),
                ('SIN TEMPO', 'Lo eliges tú',
                 'La edición no imprime velocidad. Eso no es libertad total: elige una y anótala, '
                 'porque si cada día la tocas a una distinta no avanzas.'),
            ],
            pie='La primera mitad es cómoda a propósito y la segunda no lo es. Trabajar las dos como '
                'si fueran la misma pieza es el error clásico aquí: son dos piezas pegadas, y la '
                'segunda necesita el triple de tiempo.',
        ),
        ritmos=[
            ('MANO DERECHA', 'se mueve por notas seguidas · andamio',
             [n('E4'), n('F4'), n('G4'), n('A4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda y a esperar · literal en los cc. 1-12',
             [ac(('C3', 'G3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay armadura: ni sostenidos ni bemoles detrás de la clave.',
            'La izquierda hace UNA redonda por compás durante los doce primeros compases.',
            'En el compás 11 hay un sostenido escrito delante del acorde de la izquierda.',
            'En el compás 13 hay barra de repetición: ahí empieza otra cosa.',
            'De ahí en adelante la derecha va en corcheas y semicorcheas seguidas.',
            'La edición no imprime ninguna indicación de velocidad.',
        ],
        reto='Que los doce primeros compases no se te aceleren. Con la izquierda haciendo redondas '
             'no hay nada que te marque el pulso, y sin nada que lo marque la mano derecha corre.',
        truco='Cuenta los cuatro golpes en voz alta durante toda la primera mitad, aunque te parezca '
              'ridículo. La redonda de la izquierda no te va a avisar de que has acortado el compás; '
              'tu voz sí.',
        sabias='La canción la canta Bowser en la película, y se publicó como single de verdad: llegó '
               'a entrar en las listas de éxitos de varios países. Dura poco más de un minuto, que '
               'para un número de una película de animación es una anomalía.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los compases hasta que la cosa se aprieta. Ahí es donde empieza tu '
                      'segunda mitad, y por eso las dos se estudian por separado.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza son dos piezas pegadas por una barra de repetición. Esta semana solo se '
              'trabaja la primera, la de las redondas, y se trabaja bien: es la que te va a dar el '
              'pulso para la segunda.',
        reglas=['CONTAR LOS CUATRO GOLPES EN VOZ ALTA', 'LA REDONDA DURA HASTA EL FINAL',
                'HASTA EL C. 12 Y PARAR'],
        bloques=[
            dict(num=1, titulo='La izquierda: una redonda y aguantar', clef='bass',
                 pista='cc. 1-4 · la FORMA es literal; las notas, andamio en Do mayor',
                 sistemas=[
                     dict(cap='a) una por compás, y no la sueltes antes de tiempo · cuenta los '
                              'cuatro golpes y mira si sigue sonando en el cuarto',
                          events=[ac(('C3', 'G3'), 'w'), ac(('A2', 'E3'), 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=semi(['E4', 'F4', 'G4', 'F4']) + semi(['A4', 'G4', 'F4', 'E4']) + [n('E4'), n('F4')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='La derecha por encima, sin acelerar',
                 pista='andamio en Do mayor · el dibujo va por notas seguidas',
                 sistemas=[
                     dict(cap='a) subiendo y bajando por notas seguidas · cuenta en voz alta',
                          events=[n('E4'), n('F4'), n('G4'), n('F4'),
                                  n('A4'), n('G4'), n('F4'), n('E4')],
                          bars=2),
                     dict(cap='b) con la nota larga al final de la frase, que es donde se acelera '
                              'todo el mundo · aguántala entera',
                          events=[n('C4'), n('D4'), n('E4'), n('F4'), n('G4', 'h'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL SOSTENIDO DEL C. 11',
                 texto='Es la única tecla negra de toda la primera página, y está escrita delante '
                       'del acorde de la izquierda, no en la armadura. Eso quiere decir que vale '
                       'para ese compás y nada más. Márcalo con lápiz en tu partitura: en un compás '
                       'suelto, lo que falla no es la mano, es que se te olvida que está.'),
            dict(num=3, titulo='Las dos manos, cuatro compases',
                 pista='andamio · a la velocidad que puedas contar en voz alta',
                 sistemas=[
                     dict(cap='a) la derecha se mueve y la izquierda aguanta debajo · si la redonda '
                              'se te corta al cambiar de nota arriba, ve más lento',
                          events=[ac(('C3', 'E4')), n('F4'), n('G4'), n('A4'),
                                  ac(('A2', 'G4')), n('F4'), n('E4'), n('D4')],
                          bars=2),
                     dict(cap='b) y con el acorde de la izquierda cambiando cada compás · el oído '
                              'tiene que notar el cambio aunque la derecha siga igual',
                          events=[ac(('F2', 'C4')), n('D4'), n('E4'), n('F4'),
                                  ac(('G2', 'G4')), n('F4'), n('E4'), n('C4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Peaches · para casa',
            intro='Veinte minutos, y solo hasta el compás 12. La segunda mitad, la semana que viene.',
            bloques=[
                reto('Llegar al compás 12 sin haber acelerado ni una vez.',
                     'Cuenta los cuatro golpes en voz alta de principio a fin. Si al llegar al 12 '
                     'te has quedado sin voz o has dejado de contar en algún sitio, ahí está el '
                     'compás donde corres.'),
                plan((5, 'La izquierda sola, cc. 1-12, contando los cuatro golpes'),
                     (5, 'La derecha sola, cc. 1-12, con el metrónomo puesto'),
                     (6, 'Las dos juntas, de cuatro en cuatro compases'),
                     (4, 'El compás 11 solo, con su sostenido, diez veces')),
                dict(rodear([[ac(('C3', 'G3'), 'w')],
                             [ac(('A2', 'E3'), 'w')],
                             [ac(('C3', 'G3'), 'w')],
                             [ac(('F2', 'C3'), 'w')]],
                            titulo='Rodea los dos compases iguales',
                            pista='andamio en clave de fa · así es como se lee la izquierda aquí'),
                     clef='bass'),
                unir([('Redonda', 'dura cuatro golpes'),
                      ('Barra de repetición', 'se vuelve atrás y se repite'),
                      ('Sostenido escrito delante', 'vale solo para ese compás'),
                      ('Sin tempo impreso', 'la velocidad la eliges tú y la anotas')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                colorear([n('C4', 'w'), n('E4'), n('G4', 'h'), n('F4'),
                          n('A4', 'w'), n('G4'), n('E4', 'h'), n('D4')],
                         ['Las redondas, de azul.',
                          'Las blancas, de verde.',
                          'Las negras, de rojo.'],
                         titulo='Colorea según la figura',
                         pista='son las tres figuras que usa esta pieza en la primera mitad'),
                acuerdate('La pieza no lleva tempo impreso: la velocidad la eliges tú. Elígela una '
                          'vez, apúntala a lápiz en la partitura y no la muevas en toda la semana.',
                          etiqueta='ELIGE LA VELOCIDAD Y APÚNTALA'),
                para_clase('Los doce primeros compases con las dos manos, y la velocidad que hayas '
                           'elegido. La segunda mitad ni la mires: la repartimos en clase.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
