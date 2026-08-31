# -*- coding: utf-8 -*-
"""The Beginner, de Gurlitt — pieza 8 de Eduard. Formato ADULTO. A CUATRO MANOS.

   Medido sobre el PDF de su carpeta (vectorial, CUATRO pentagramas por
   sistema: dos pianos):

     - 3/4 y detras de la clave no hay nada.
     - Los dos pentagramas de ARRIBA son el Primo, y los dos llevan CLAVE DE
       SOL. Se comprobo nota a nota: **son identicos**, la misma melodia en los
       dos. El de arriba lleva encima un **8va**, asi que la mano derecha suena
       una octava mas alta de lo que esta escrito. El resultado es la melodia
       en octavas.
     - Los dos de ABAJO son el Secondo (clave de sol y clave de fa), y llevan
       el acompanamiento. Los toca la profesora.
     - Pone **mf** y trae **reguladores** dibujados: uno que abre en el c. 1 y
       otro que cierra en el c. 2.
     - La melodia, medida a 300 ppp (alturas tal como estan ESCRITAS, en el
       pentagrama de abajo del Primo):

         c. 1   Mi5 · Mi5 · Mi5              tres negras
         c. 2   Sol5 · Fa5                    blanca y negra
         c. 3   Mi5 · Re5 · Do5               negra con puntillo, corchea, negra
         c. 4   Re5                           blanca

   POR QUE VA AQUI. Es la UNICA pieza del cuaderno en la que las dos manos
   hacen LO MISMO, y va justo detras de las dos primeras en que cada mano lleva
   lo suyo (la Pantera y el Nocturno). Es un descanso con sentido: se aprende a
   mover las dos manos juntas sin tener que leer dos cosas distintas a la vez,
   y de ahi se sale a Puff, donde vuelven a separarse.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, plan, escalera, verdadero_falso, dibujar,
                      a_cuatro_manos, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los compases 1 y 2, medidos. Cita literal (alturas escritas).
MELODIA = [n('E5'), n('E5'), n('E5'), n('G5', 'h'), n('F5')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=8, nivel='iniciación',
    slug='TheBeginner', formato='adulto',
    titulo_corto='The Beginner · Gurlitt', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'The Beginner Gurlitt 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=gurlitt+the+beginner+piano+duet',

    ficha=dict(
        titulo='The Beginner',
        autor='Cornelius Gurlitt · a cuatro manos · parte del Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Manos', 'Las dos, al unísono'), ('Volumen', 'mf'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura: los compases 1 y 2 arriba, el 3 abajo. Las dos manos '
                   'tocan esto mismo, la derecha una octava más alta por el 8va.',
        armonia=dict(
            titulo='Dos manos, una sola melodía',
            tarjetas=[
                ('LAS DOS IGUALES', 'Al unísono',
                 'Tus dos pentagramas llevan clave de sol y traen lo mismo nota por nota. Lees una '
                 'melodía y la tocas con las dos manos.'),
                ('EL 8VA', 'Una octava arriba',
                 'Encima del pentagrama de la derecha hay un "8va": eso quiere decir que esa mano '
                 'suena una octava más alta de lo escrito. El dibujo es el mismo; el sitio del '
                 'teclado, no.'),
                ('LOS REGULADORES', 'Abrir y cerrar',
                 'Esas dos cuñas dibujadas dicen que el sonido crece y luego vuelve a bajar. Es la '
                 'primera pieza del cuaderno que te lo pide por escrito.'),
                ('NO ESTÁS SOLO', 'A cuatro manos',
                 'La otra parte, el Secondo, la toca la profesora en los dos pentagramas de abajo. '
                 'Tú llevas la melodía.'),
            ],
            pie='Gurlitt escribió cuadernos enteros de piezas como esta para el primer año. El '
                'título no es casualidad: está pensada para que suene bien tocándola muy despacio.',
        ),
        ritmos=[
            ('LA MELODÍA', 'cc. 1 y 2, medidos · las dos manos tocan esto',
             MELODIA, OCRE, 'treble', None),
            ('Y EL SIGUIENTE', 'c. 3, medido · aquí aparece la primera corchea',
             [n('E5', 'q.'), n('D5', 'e'), n('C5')], AZUL, 'treble', None),
        ],
        especial=[
            'Cuatro pentagramas: los dos de arriba son tuyos.',
            'Tus dos pentagramas llevan clave de sol, y traen lo mismo.',
            'Encima del de la derecha hay un 8va: suena una octava más alta.',
            'Compás de 3/4, y no hay ni un sostenido ni un bemol.',
            'Pone "mf" al principio: ni fuerte ni suave.',
            'Hay reguladores dibujados: el sonido crece y decrece.',
        ],
        reto='Que las dos manos caigan EXACTAMENTE a la vez. Cuando tocan lo mismo, cualquier '
             'desfase se oye como un eco, y es el defecto más típico al empezar con las dos.',
        truco='Toca solo la primera nota de cada compás, las dos manos juntas, y escucha si suena '
              'un golpe o dos. Si oyes dos, para y vuelve a intentarlo hasta que suene uno solo. '
              'Con eso resuelto, el resto de la pieza sale.',
        sabias='Cornelius Gurlitt fue profesor de piano en Hamburgo hace siglo y medio y escribió '
               'centenares de piezas cortas para alumnos que empezaban. Muchas se siguen usando '
               'hoy exactamente igual, porque nadie las ha mejorado.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que las dos manos del Primo suenan como una sola voz, más gorda: '
                      'eso es tocar en octavas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Como las dos manos tocan lo mismo, aquí no hay dos cosas que leer: hay una, tocada '
              'dos veces a la vez. Todo el trabajo es que caigan juntas.',
        reglas=['UNA SOLA MELODÍA, DOS MANOS', 'QUE SUENE UN GOLPE, NO DOS',
                'LA DERECHA, UNA OCTAVA MÁS ARRIBA'],
        bloques=[
            dict(num=1, titulo='La melodía sola, con la mano derecha',
                 pista='cc. 1–3 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) el compás 1 tres veces seguidas · la misma tecla, sin acelerar',
                          events=[n('E5'), n('E5'), n('E5'), n('E5'), n('E5'), n('E5'),
                                  n('E5'), n('E5'), n('E5')],
                          matiz='mf',
                          bars=3),
                     dict(cap='b) y los compases 2 y 3 enlazados, con los reguladores de tu '
                              'partitura: crece y vuelve a bajar',
                          events=[dict(n('G5', 'h'), cresc=2), n('F5'),
                                  dict(n('E5', 'q.'), dim=3), n('D5', 'e'), n('C5'),
                                  n('D5', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UN 8VA Y POR QUÉ SE USA',
                 texto='Escribir muy agudo obliga a dibujar la nota colgando de un montón de '
                       'líneas adicionales, y eso no se lee. La solución de siempre es escribirla '
                       'una octava más abajo y poner encima un "8va": el dibujo queda cómodo y el '
                       'pianista sabe que tiene que subir una octava. Aquí sirve además para que '
                       'las dos manos lean lo mismo aunque toquen en sitios distintos.'),
            dict(num=2, titulo='La izquierda sola, en su octava',
                 pista='andamio en Do mayor · el mismo dibujo, una octava más abajo',
                 sistemas=[
                     dict(cap='a) sube y baja en la posición de cinco dedos, sin mirar la mano',
                          events=[n('C4'), n('E4'), n('D4'), n('F4'), n('E4'), n('G4')],
                          bars=2),
                     dict(cap='b) y con una nota larga al final de cada compás',
                          events=[n('G4'), n('F4', 'h'), n('E4'), n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Y ahora las dos a la vez',
                 pista='andamio · es el paso de verdad · un golpe, no dos',
                 sistemas=[
                     dict(cap='a) las dos manos con la misma nota, a distancia de octava',
                          events=[ac(('C4', 'C5'), 'h'), ac(('C4', 'C5')),
                                  ac(('D4', 'D5'), 'h'), ac(('D4', 'D5'))],
                          bars=2),
                     dict(cap='b) y moviéndose · escucha si suena un golpe o dos',
                          events=[ac(('E4', 'E5')), ac(('F4', 'F5')), ac(('G4', 'G5')),
                                  ac(('F4', 'F5'), 'h'), ac(('E4', 'E5'))],
                          bars=2, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='The Beginner · para casa',
            intro='Quince minutos al día. Es una pieza corta y lenta: la semana no se va en notas, '
                  'se va en conseguir que las dos manos suenen como una.',
            bloques=[
                plan((4, 'La melodía con la derecha sola, cc. 1–4'),
                     (4, 'La misma melodía con la izquierda sola'),
                     (4, 'Las dos juntas, solo la primera nota de cada compás'),
                     (3, 'Las dos juntas, los cuatro compases seguidos')),
                escalera((50, 'las dos manos, la primera nota de cada compás'),
                         (63, 'los cuatro primeros compases seguidos'),
                         (76, 'la primera línea entera, en mf y con los reguladores'),
                         meta='la primera línea con las dos manos juntas · tu partitura no trae '
                              'número de metrónomo, estos son de trabajo',
                         notas=['Apunta cada día hasta qué escalón has llegado.']),
                verdadero_falso([
                    ('Mis dos pentagramas llevan clave de sol.', True),
                    ('Las dos manos tocan cosas distintas.', False),
                    ('El 8va hace que la derecha suene una octava más alta.', True),
                    ('La pieza va en compás de cuatro tiempos.', False),
                    ('"mf" quiere decir muy fuerte.', False),
                ],
                    titulo='Verdadero o falso, mirando tu partitura',
                    pista='marca la casilla · todas se contestan con la primera página'),
                dibujar(['Mi', 'Sol', 'Fa', 'Mi', 'Re', 'Do'],
                        titulo='Dibuja tú estas notas en clave de sol',
                        pista='son las de tus tres primeros compases · solo el óvalo'),
                a_cuatro_manos('Antes de empezar, acordad tres cosas con quien toque el Secondo: '
                               'quién cuenta la entrada, a qué velocidad, y qué hacéis si alguien '
                               'se pierde (lo normal es seguir contando y volver a entrar en el '
                               'compás siguiente, no parar).'),
                para_clase('La primera línea con las dos manos. Si te suena a eco, tráelo así: es '
                           'lo que hay que arreglar en clase y se arregla en cinco minutos.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 69, 'E5', 'C4',
    'las dos manos al unísono: lo difícil es que caigan juntas',
    desde=4, time_sig=(3, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
