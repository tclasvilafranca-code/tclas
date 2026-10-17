# -*- coding: utf-8 -*-
"""Villancicos a cuatro manos — pieza 12 de Eduard. Formato ADULTO.

   El PDF de su carpeta se llama "Christmas Songs 4 manos" y dentro pone
   *Christmas Songs for Four Little Hands · Jingle Bells + We Wish You A Merry
   Christmas · Beginner Version*. Son dos villancicos seguidos en el mismo
   arreglo.

   Medido sobre ESE PDF (vectorial, CUATRO pentagramas por sistema):

     - 4/4, y arriba, impreso, **♩ = 100**.
     - Detras de la clave no hay nada.
     - Los dos pentagramas de ARRIBA son el Primo —lo que toca Eduard— y los
       DOS llevan **clave de sol**. No es un error de lectura: se comprobo con
       el recorte ampliado. Las dos manos tocan en la mitad derecha del
       teclado, muy juntas.
     - Los dos de ABAJO son el Secondo, que toca la profesora.
     - Medido a 300 ppp:

         DERECHA    c. 1   Mi5 · Mi5 · Mi5      negra, negra y blanca
                    c. 2   igual que el 1
                    c. 3   Mi5 · Sol5 · Do5 · Re5   cuatro negras
         IZQUIERDA  c. 1   Sol4 · Mi4           dos blancas
                    c. 2   Sol4 · Mi4           igual
                    c. 3   Sol4 · Mi4           igual

     - O sea: es *Jingle Bells*, y la izquierda hace el mismo acompanamiento
       tres compases seguidos.

   POR QUE VA EN DICIEMBRE Y POR QUE VA AQUI. Es la unica pieza del cuaderno
   en la que la izquierda repite exactamente lo mismo compas tras compas: se
   aprende en cinco minutos y deja toda la atencion libre para la derecha. Y
   es un dueto, asi que se puede tocar en clase el ultimo dia antes de
   Navidad.

   UNA NOTA SOBRE LA MEDICION. `medir_arranque` no encuentra aqui la divisoria
   del primer compas: en una partitura a cuatro manos las barras de compas no
   unen los dos pianos, y en esta edicion tampoco unen los dos pentagramas del
   Primo. La lectura del c. 1 esta anotada a mano en `auditar_alturas.MIRADAS`.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, plan, escalera, ordenar, escribir, a_cuatro_manos,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 de la DERECHA, medido. Cita literal.
ARRANQUE = [n('E5'), n('E5'), n('E5', 'h')]

# Los compases 1 y 2 de la IZQUIERDA, medidos. En CLAVE DE SOL, como en la
# partitura: las dos manos del Primo van juntas en la mitad derecha.
BAJO = [n('G4', 'h'), n('E4', 'h'), n('G4', 'h'), n('E4', 'h')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=12, nivel='iniciación',
    slug='VillancicosCuatroManos', formato='adulto',
    titulo_corto='Villancicos a cuatro manos', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Christmas Songs 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=jingle+bells+piano+duet+easy',

    ficha=dict(
        titulo='Villancicos a cuatro manos',
        autor='Jingle Bells + We Wish You a Merry Christmas · versión de iniciación',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 100'), ('Manos', 'Dos claves de sol'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, el compás 1 de la derecha. Abajo, los compases '
                   '1 y 2 de la izquierda, que van escritos también en clave de sol.',
        armonia=dict(
            titulo='La izquierda que no cambia nunca',
            tarjetas=[
                ('DOS CLAVES DE SOL', 'Las dos manos arriba',
                 'Tus dos pentagramas llevan clave de sol. Las dos manos tocan en la mitad derecha '
                 'del teclado, muy cerca la una de la otra.'),
                ('LA IZQUIERDA', 'Sol y Mi',
                 'Dos notas largas por compás, y las mismas dos en los tres primeros compases. Se '
                 'aprende de memoria en cinco minutos.'),
                ('LA DERECHA', 'Jingle Bells',
                 'Tres veces la misma nota: dos cortas y una larga. Es la melodía que todo el mundo '
                 'reconoce desde el primer compás.'),
                ('EL TEMPO', '♩ = 100',
                 'Viene impreso en la partitura. Es rápido para una pieza de este curso, así que se '
                 'estudia mucho más lento y se sube al final.'),
            ],
            pie='Son dos villancicos seguidos: primero Jingle Bells y después We Wish You a Merry '
                'Christmas. Con el Secondo suena a orquesta entera, aunque tú estés tocando cinco '
                'notas distintas.',
        ),
        ritmos=[
            ('LA DERECHA', 'el compás 1, medido · dos cortas y una larga',
             ARRANQUE, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · siempre las mismas dos notas',
             BAJO, AZUL, 'treble', None),
        ],
        especial=[
            'Cuatro pentagramas: los dos de arriba son tuyos.',
            'Tus dos pentagramas llevan clave de sol.',
            'Compás de 4/4, y no hay ni un sostenido ni un bemol.',
            'Arriba pone ♩ = 100: el número de metrónomo.',
            'La izquierda hace lo mismo tres compases seguidos.',
            'Son dos villancicos, uno detrás del otro.',
        ],
        reto='Que la izquierda siga sonando igual de tranquila cuando la derecha se pone a correr. '
             'Como se repite tanto, es fácil acelerarla sin darse cuenta.',
        truco='Toca la izquierda sola con el metrónomo, mirando a otro lado, veinte compases '
              'seguidos. Cuando puedas hacerlo sin mirar y sin acelerar, añade la derecha: la '
              'izquierda ya no se va a mover de sitio.',
        sabias='"Jingle Bells" no se escribió para Navidad: era una canción de carreras de trineos '
               'de 1857 que se cantaba por Acción de Gracias. Fue, además, la primera canción que '
               'se emitió desde el espacio, en 1965, desde la nave Gemini 6.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo la mano de abajo: dos notas que se repiten sin parar. Esa es la '
                      'que tienes que poder tocar sin pensar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda de esta pieza se aprende antes de terminar de leer esta frase. Todo el '
              'tiempo que sobra es para la derecha y para tocarla con alguien.',
        reglas=['LAS DOS MANOS EN CLAVE DE SOL', 'LA IZQUIERDA NO CAMBIA NUNCA',
                'DESPACIO PRIMERO, ♩ = 100 AL FINAL'],
        bloques=[
            dict(num=1, titulo='La izquierda, que es siempre igual',
                 pista='cc. 1–3 · medidos en tu partitura · en clave de sol',
                 sistemas=[
                     dict(cap='a) las dos notas, tres compases seguidos, sin acelerar',
                          events=[n('G4', 'h'), n('E4', 'h'), n('G4', 'h'), n('E4', 'h'),
                                  n('G4', 'h'), n('E4', 'h')],
                          bars=3),
                     dict(cap='b) y ahora con los ojos en otro sitio: la mano ya sabe dónde está',
                          events=[n('G4', 'h'), n('E4', 'h'), n('G4', 'w'),
                                  n('E4', 'h'), n('G4', 'h')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ AQUÍ LAS DOS MANOS VAN EN CLAVE DE SOL',
                 texto='En un dueto, el que se sienta a la derecha —el Primo— toca en la zona aguda '
                       'del teclado, y ahí las dos manos caen por encima del do central. Escribir '
                       'la izquierda en clave de fa obligaría a llenarla de líneas adicionales. Por '
                       'eso el arreglista pone clave de sol en los dos pentagramas: no es un error, '
                       'es lo cómodo.'),
            dict(num=2, titulo='La melodía de Jingle Bells',
                 pista='cc. 1–3 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) los compases 1 y 2, que son iguales · dos cortas y una larga',
                          events=[n('E5'), n('E5'), n('E5', 'h'),
                                  n('E5'), n('E5'), n('E5', 'h')],
                          bars=2),
                     dict(cap='b) y el compás 3, que es donde por fin se mueve',
                          events=[n('E5'), n('G5'), n('C5'), n('D5'), n('E5', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, que están muy cerca',
                 pista='cc. 1–2 · medidos · cuidado con chocar',
                 sistemas=[
                     dict(cap='a) las dos juntas, solo el primer compás, dos veces',
                          events=[ac(('E4', 'G4', 'E5')), ac(('E5',)),
                                  ac(('E4', 'G4', 'E5'), 'h'),
                                  ac(('E4', 'G4', 'E5')), ac(('E5',)),
                                  ac(('E4', 'G4', 'E5'), 'h')],
                          bars=2, manos='sostiene'),
                     dict(cap='b) y con el compás 3, donde la derecha baja y se cruza de zona',
                          events=[ac(('E4', 'G4', 'E5')), ac(('G5',)),
                                  ac(('E4', 'G4', 'C5')), ac(('D5',))],
                          bars=1, manos='sostiene', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Villancicos · para casa',
            intro='Quince minutos al día. Esta es la pieza de tocar con alguien: merece la pena '
                  'llegar a clase con tu parte tan sabida que puedas mirar a la otra persona.',
            bloques=[
                plan((3, 'La izquierda sola, sin mirar las teclas'),
                     (4, 'La melodía de la derecha, cc. 1–4'),
                     (4, 'Las dos manos, muy despacio'),
                     (4, 'Las dos manos con el metrónomo, subiendo poco a poco')),
                escalera((60, 'las dos manos, los tres primeros compases'),
                         (80, 'la primera línea entera, sin parar'),
                         (100, 'la primera línea a la velocidad que pide la partitura'),
                         meta='llegar a ♩ = 100, que es el número impreso en tu partitura',
                         notas=['Apunta cada día a qué escalón te has quedado.']),
                ordenar(['Toco la izquierda sola hasta no tener que mirarla.',
                         'Leo la melodía de la derecha, despacio y sin la izquierda.',
                         'Junto las dos manos en el compás 1.',
                         'Subo la velocidad con el metrónomo.',
                         'Lo toco con la otra persona.'],
                        titulo='Pon en orden el plan de la semana',
                        pista='escribe 1, 2, 3, 4 y 5 en las casillas'),
                escribir(titulo='Copia aquí el compás 3, el que se mueve',
                         pista='son cuatro negras · y luego tócalo cinco veces'),
                a_cuatro_manos('Con quien toque el Secondo, acordad tres cosas antes de empezar: '
                               'quién cuenta el "un, dos, tres, cuatro" de entrada, a qué velocidad '
                               'vais a tocarlo hoy —no siempre a 100—, y en qué compás volvéis a '
                               'entrar si alguien se pierde.'),
                para_clase('Tu parte sola, de memoria si puede ser. En clase se toca entera con el '
                           'Secondo, y eso solo sale bien si no tienes que ir leyendo.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 73, 'E5', 'C3',
    'las dos manos muy juntas, las dos en clave de sol',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
