# -*- coding: utf-8 -*-
"""Greensleeves — pieza 13 de Eduard. Formato ADULTO.

   Medido sobre el PDF de su carpeta (vectorial, dos pentagramas por sistema):

     - 3/4 y detras de la clave **no hay nada**. Es La menor, el primer tono
       menor del cuaderno, y no lleva ninguna alteracion en la armadura.
     - Pone **mp** y trae **cifrado** encima del pentagrama: Am, G...
     - Trae digitacion impresa (se ven un 1 y un 2 al principio).
     - Empieza con ANACRUSA de un tiempo, y esta vez la toca la DERECHA.
     - Medido a 300 ppp:

         DERECHA    anacrusa   La4                  negra
                    c. 1       Do5 · Re5            blanca y negra
                    c. 2       Mi5 · Fa5 · Mi5      negra con puntillo,
                                                    corchea y negra
         IZQUIERDA  c. 1       La3 · Do4 · Mi4      tres negras
                    c. 2       La3 · Do4 · Mi4      igual

     - La izquierda no acompana con notas largas, como en todas las anteriores:
       toca el acorde DESPLEGADO, nota a nota. La3, Do4 y Mi4 son las tres
       notas del acorde de La menor, una detras de otra. Eso es lo nuevo aqui.

   OJO CON EL FA. La version que todo el mundo conoce de *Greensleeves* lleva
   Fa sostenido en ese sitio. Esta edicion NO lo lleva: se miro ampliado y
   delante del Fa5 del c. 2 no hay ninguna alteracion, y la armadura esta
   vacia. Se escribe lo que trae el papel.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, sil, plan, metronomo, cifrado, contar, colorear,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# La anacrusa y el c. 1 de la DERECHA, medidos. Cita literal. Delante van los
# dos tiempos del compas de anacrusa que no suenan, para que la fila sume
# compases enteros.
ARRANQUE = [sil('h'), n('A4'), n('C5', 'h'), n('D5')]

# Los compases 1 y 2 de la IZQUIERDA, medidos: el acorde de La menor desplegado.
BAJO = [n('A3'), n('C4'), n('E4'), n('A3'), n('C4'), n('E4')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=13, nivel='iniciación',
    slug='Greensleeves', formato='adulto',
    titulo_corto='Greensleeves', time_sig=(3, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Greensleeves.pdf'),
    yt='https://www.youtube.com/results?search_query=greensleeves+piano+easy',

    ficha=dict(
        titulo='Greensleeves',
        autor='canción inglesa del siglo XVI · arreglo fácil',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Manos', 'Las dos, distintas'), ('Volumen', 'mp'),
               ('Acordes', 'Am · G')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, la anacrusa y el compás 1 de la derecha. Abajo, '
                   'la izquierda de los compases 1 y 2: el acorde, nota a nota.',
        armonia=dict(
            titulo='El primer tono menor, y la izquierda que se mueve',
            tarjetas=[
                ('LA MENOR', 'Sin alteraciones',
                 'Detrás de la clave no hay nada, igual que en Do mayor, pero la música descansa en '
                 'La y por eso suena distinta: más oscura. Las teclas son las mismas.'),
                ('EL ACORDE ROTO', 'La · Do · Mi',
                 'La izquierda ya no aguanta una nota: toca las tres del acorde una detrás de otra. '
                 'Es la primera vez que se mueve de verdad en todo el cuaderno.'),
                ('EL CIFRADO', 'Am · G',
                 'Esas letras de encima son acordes. La "m" pequeña de Am quiere decir menor, y es '
                 'justo el acorde que está tocando tu mano izquierda.'),
                ('LA ANACRUSA', 'Una nota antes',
                 'La melodía entra en el último tiempo del compás anterior. Cuenta un compás entero '
                 'de tres antes de tocar y entra en el TRES.'),
            ],
            pie='Fíjate en que las tres notas de la izquierda son las mismas que las letras de '
                'arriba anuncian. Cuando el cifrado cambia a G, las notas de abajo cambian con él: '
                'esa es toda la lógica del acompañamiento.',
        ),
        ritmos=[
            ('LA DERECHA', 'la anacrusa y el c. 1, medidos · entra en el tres',
             ARRANQUE, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · el acorde de La menor, roto',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Compás de 3/4: tres golpes, y el primero es el fuerte.',
            'Detrás de la clave no hay nada, pero la pieza es en La menor.',
            'Empieza con una nota antes del primer compás.',
            'La izquierda toca las tres notas del acorde, una a una.',
            'Encima del pentagrama hay letras de acorde: Am, G.',
            'Pone "mp": medio suave.',
        ],
        reto='Que la izquierda suene pareja. Al tocar tres notas seguidas con dedos distintos, casi '
             'siempre hay una que suena más fuerte que las otras dos, y se oye enseguida.',
        truco='Toca las tres notas de la izquierda muy despacio y escucha cuál se te escapa. Suele '
              'ser la del pulgar. Hazla a propósito más floja durante unos días hasta que las tres '
              'suenen iguales.',
        sabias='La letra habla de una dama vestida de verde y se cantaba en Inglaterra hace más de '
               'cuatrocientos años. Circuló la leyenda de que la escribió Enrique VIII para Ana '
               'Bolena, pero el estilo es posterior: no pudo ser él.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta un-dos-tres con el pie y fíjate en que la melodía entra en el tres, '
                      'antes del primer golpe fuerte.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo está abajo: la izquierda toca tres notas por compás en vez de una larga. Se '
              'trabaja sola hasta que las tres suenen iguales.',
        reglas=['LAS TRES NOTAS DE ABAJO, IGUALES', 'ENTRAS EN EL TRES, NO EN EL UNO',
                'MP: NI FUERTE NI TÍMIDO'],
        bloques=[
            dict(num=1, titulo='El acorde de La menor, roto', clef='bass',
                 pista='cc. 1–2 · medidos en tu partitura · las tres notas del acorde',
                 sistemas=[
                     dict(cap='a) las tres notas subiendo, cuatro compases seguidos',
                          events=[n('A3'), n('C4'), n('E4'), n('A3'), n('C4'), n('E4'),
                                  n('A3'), n('C4'), n('E4'), n('A3', 'h.')],
                          matiz='mp',
                          bars=4, clef='bass'),
                     dict(cap='b) y ahora bajando, que es lo que cuesta',
                          events=[n('E4'), n('C4'), n('A3'), n('E4'), n('C4'), n('A3')],
                          bars=2, clef='bass', show_time=False),
                     dict(cap='c) y subiendo y bajando seguido, sin parar entre los dos compases',
                          events=[n('A3'), n('C4'), n('E4'), n('C4'), n('A3'), n('C4'),
                                  n('E4'), n('C4'), n('A3'), n('A3', 'h.')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UN ACORDE ROTO Y POR QUÉ SE USA TANTO',
                 texto='Un acorde son tres notas que suenan a la vez. Si en vez de darlas juntas se '
                       'tocan una detrás de otra, se llama acorde roto o desplegado, y suena a '
                       'acompañamiento en movimiento en lugar de a bloque. Está en media música que '
                       'conoces, desde una balada de piano hasta una guitarra rasgueando. Aquí es, '
                       'además, la manera más cómoda de aprenderse un acorde: los dedos lo memorizan '
                       'nota a nota.'),
            dict(num=2, titulo='La melodía, con su entrada',
                 pista='anacrusa y cc. 1–2 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) cuenta un-dos-tres y entra en el tres · la nota larga dura dos',
                          events=[sil('h'), n('A4'), n('C5', 'h'), n('D5'), n('C5', 'h.')],
                          bars=3),
                     dict(cap='b) y el compás 2, con la negra con puntillo y su corchea',
                          events=[n('E5', 'q.'), n('F5', 'e'), n('E5'), n('D5', 'h.')],
                          bars=2, show_time=False),
                     dict(cap='c) y los dos compases enlazados, que es la primera frase entera',
                          events=[n('C5', 'h'), n('D5'), n('E5', 'q.'), n('F5', 'e'), n('E5'),
                                  n('D5', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con la izquierda una octava más abajo',
                 pista='andamio en La menor · el mismo dibujo, colocado donde se puede escribir',
                 sistemas=[
                     dict(cap='a) la derecha toca en el uno y en el tres, y la izquierda no para',
                          events=[ac(('A2', 'C5')), ac(('C3',)), ac(('E3', 'D5')),
                                  ac(('A2', 'E5')), ac(('C3',)), ac(('E3',))],
                          bars=2, manos='dobla'),
                     dict(cap='b) y una vez más, terminando la frase con la mano quieta',
                          events=[ac(('A2', 'E5')), ac(('C3', 'F5')), ac(('E3', 'E5')),
                                  ac(('A2', 'D5'), 'h.')],
                          bars=2, manos='dobla', show_time=False),
                     dict(cap='c) y con la anacrusa delante: cuenta un compás y entra en el tres',
                          events=[sil('h'), ac(('A4',)),
                                  ac(('A2', 'C5')), ac(('C3',)), ac(('E3', 'D5'))],
                          bars=2, manos='dobla', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ AQUÍ LA IZQUIERDA ESTÁ MÁS ABAJO QUE EN TU PARTITURA',
                 texto='En tu edición el acorde de la izquierda sube hasta el Mi que está por '
                       'encima del do central: las dos manos quedan muy cerca. Para que este '
                       'ejercicio se pueda escribir en clave de fa sin llenarlo de líneas '
                       'adicionales, aquí está una octava más abajo. El dibujo de los dedos es '
                       'exactamente el mismo; solo cambia la zona del teclado. Cuando lo tengas, '
                       'súbelo a su sitio mirando la partitura.'),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Greensleeves · para casa',
            intro='Quince minutos al día, y la mitad para la izquierda sola. Cuando el acorde roto '
                  'salga parejo, esta pieza está hecha.',
            bloques=[
                plan((5, 'La izquierda sola: La-Do-Mi, subiendo y bajando'),
                     (4, 'La melodía con su anacrusa, contando un-dos-tres'),
                     (3, 'El compás 2, con la negra con puntillo'),
                     (3, 'Los dos primeros compases con las dos manos')),
                metronomo('Empieza a ♩ = 63 con la izquierda sola.',
                          'Tu partitura no trae número de metrónomo: estos son de trabajo. '
                          'Greensleeves admite ir despacio y suena bien igual.'),
                cifrado(['Am', 'G'],
                        ['¿Cuál de los dos es menor, y en qué se nota al mirarlo?',
                         '¿Qué tres notas está tocando tu izquierda en el compás 1?'],
                        titulo='Las letras que trae tu partitura',
                        pista='escribe las tres notas de cada acorde, de grave a agudo'),
                contar([n('A3'), n('C4'), n('E4'), n('A3'), n('C4'), n('E4')],
                       ['¿Cuántas notas hay en total?', '¿Cuántas veces aparece el La?',
                        '¿Cuántos compases de tres tiempos son?'],
                       titulo='Mira la izquierda y cuenta',
                       pista='son los dos primeros compases de tu mano izquierda'),
                colorear([n('A4'), n('C5', 'h'), n('D5'), n('E5', 'q.'), n('F5', 'e'), n('E5')],
                         [('q', 'las negras'), ('h', 'las largas')],
                         titulo='Colorea las negras de un color y las largas de otro',
                         pista='es la melodía de tu anacrusa y tus dos primeros compases'),
                para_clase('La izquierda sola, y los dos primeros compases con las dos manos. Di en '
                           'clase cuál de las tres notas del acorde se te sale más fuerte.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'La menor', 74, 'A4', 'A3',
    'el acorde roto de la izquierda: tres notas que tienen que sonar iguales',
    desde=4, time_sig=(3, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
