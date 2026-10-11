# -*- coding: utf-8 -*-
"""Eye of the Tiger (Survivor) — pieza 11 de Alan. ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Sadie King,
   1 página, imagen a 54 ppp), mirado a 220 ppp. Es un escaneo flojo: las
   figuras se ven, las alturas no se distinguen con seguridad, así que todo lo
   que lleva notas va como ANDAMIO y solo el ritmo se cita:

     - Detrás de la clave no hay nada. 4/4. No trae número de metrónomo.
       Intensidad: f al principio, mf en el c. 5, f en el c. 12 y una indicación
       suave al final.
     - 21 compases en una página. Los cuatro primeros llevan barra de repetición
       al final del c. 4.
     - La derecha del principio es una tríada tocada en bloque. Ritmo del c. 1:
       negra · silencio de negra · tres acordes de corchea con puntillo,
       corchea con puntillo y corchea. El c. 2 empieza con silencio de blanca
       y repite los tres acordes. El c. 3 los repite y el último queda ligado a un
       acorde largo del c. 4.
     - La izquierda de los cc. 1-3 es una negra y una blanca con puntillo, graves.
       El c. 4 son cuatro negras.
     - c. 5: silencio de negra · corchea · dos semicorcheas · blanca ligada.
       c. 6: cuatro corcheas y una blanca. c. 7: silencio de negra, dos
       corcheas, negra, dos corcheas. c. 8: negra y blanca con puntillo.
     - Hay semicorcheas y corcheas con puntillo repartidas por toda la página.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, plan, metronomo, nombres, colorear, diferencias,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

TRIADA = ('A4', 'C5', 'E5')

# MEDIDO (solo el ritmo): c. 1 y c. 2 de la derecha, con acordes de andamio
C1 = [ac(TRIADA), sil('q'), ac(TRIADA, 'e.'), ac(TRIADA, 'e.'), ac(TRIADA, 'e')]
C2 = [sil('h'), ac(TRIADA, 'e.'), ac(TRIADA, 'e.'), ac(TRIADA, 'e')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=11, nivel='intermedio', slug='EyeOfTheTiger',
    formato='adulto',
    titulo_corto='Eye of the Tiger', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'EYE OF THE TIGER.'),
    yt='https://www.youtube.com/results?search_query=eye+of+the+tiger+piano+easy',

    ficha=dict(
        titulo='Eye of the Tiger',
        autor='Survivor · arreglo de Sadie King',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Repetición', 'cc. 1-4'),
               ('Páginas', 'Una')],
        titulo_ritmos='El ritmo de los cc. 1 y 2, y la izquierda',
        pie_ritmos='Arriba, el ritmo de tu partitura con acordes de andamio: negra, silencio y tres '
                   'golpes largo-largo-corto. Abajo, andamio: la izquierda, grave y larga.',
        armonia=dict(
            titulo='Un ritmo que lo es todo, y dos semicorcheas para remate',
            tarjetas=[
                ('EL RITMO', 'Largo-largo-corto',
                 'Tres acordes seguidos: corchea con puntillo, corchea con puntillo y corchea. '
                 'Es el golpe que todo el mundo reconoce, y es lo primero que hay que clavar.'),
                ('LA REPETICIÓN', 'cc. 1-4',
                 'Una barra de repetición cierra el c. 4: se tocan dos veces los cuatro primeros '
                 'compases antes de seguir. La segunda no se improvisa: se toca igual.'),
                ('LAS SEMICORCHEAS', 'En el c. 5',
                 'Después de un silencio de negra entran una corchea y dos semicorcheas pegadas, '
                 'y la última se liga a una blanca. Son notas muy cortas, pero salen solas si '
                 'se cuentan.'),
                ('LA INTENSIDAD', 'f y mf',
                 'La pieza empieza fuerte, baja a mf en el c. 5 y vuelve a subir. Con el '
                 'mismo ritmo, el cambio de volumen hace de dos frases una sola historia.'),
            ],
            pie='Una página y 21 compases: una pieza corta que se toca a toda velocidad. La '
                'partitura no trae número de metrónomo: la velocidad la decides tú, pero ha de '
                'ser siempre la misma de principio a fin.',
        ),
        ritmos=[
            ('MANO DERECHA', 'andamio sobre el ritmo de los cc. 1-2', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · negra y blanca con puntillo',
             [n('A2'), n('A2', 'h.'), n('A2'), n('A2', 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 4/4 y no trae número de metrónomo.',
            'Los cc. 1-4 llevan barra de repetición al final.',
            'La derecha empieza con acordes de tres notas.',
            'El c. 5 mezcla una corchea y dos semicorcheas.',
            'La partitura cambia de intensidad: empieza fuerte y baja en el c. 5.',
        ],
        reto='El ritmo largo-largo-corto de los cc. 1-3 tiene que salir igual las seis veces '
             'que aparece, sin que la corchea final se apresure ni se arrastre.',
        truco='Di en voz alta "pa-ra-pa" mientras tocas: dos sílabas largas y una corta. Si lo '
              'dices a la vez que tocas y coinciden, el ritmo está bien.',
        sabias='Survivor la escribió en 1982 para la película Rocky III, porque Sylvester Stallone '
               'no consiguió los derechos de otra canción que quería. Fue número uno en '
               'Estados Unidos seis semanas.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el golpe de los acordes cae siempre en el mismo sitio del '
                      'compás. Cuando lo oigas, di el ritmo en voz alta antes de tocarlo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo difícil de esta pieza es el ritmo, no las notas. Se estudia el ritmo solo, '
              'con una nota o un acorde cualquiera, hasta que sale sin pensar.',
        reglas=['EL RITMO ANTES QUE LAS NOTAS', 'LA CORCHEA FINAL, SIN PRISA',
                'LAS SEMICORCHEAS SE CUENTAN'],
        bloques=[
            dict(num=1, titulo='El golpe del c. 1',
                 pista='c. 1 · el ritmo es el de tu partitura · las notas son andamio',
                 sistemas=[
                     dict(cap='a) negra, silencio y tres acordes: largo-largo-corto · cuenta '
                              '"uno, dos, tres-y-cuatro-y"',
                          events=C1, bars=1),
                     dict(cap='b) el mismo ritmo sobre una sola nota · andamio · para oír solo '
                              'la rítmica',
                          events=[n('C5'), sil('q'), n('C5', 'e.'), n('C5', 'e.'), n('C5', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='Dos semicorcheas pegadas, el c. 5',
                 pista='c. 5 · el ritmo es el de tu partitura · una corchea, dos semicorcheas, y la '
                       'última ligada a una blanca',
                 sistemas=[
                     dict(cap='a) las dos semicorcheas caben donde cabría una corchea · la última '
                              'se queda ligada a la blanca: no se vuelve a pulsar',
                          events=[sil('q'), n('E5', 'e'), n('G5', 's'),
                                  dict(pitch='E5', dur='s', lig=True), n('E5', 'h')],
                          bars=1, matiz='mf'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ESTUDIA EL RITMO SIN NOTAS',
                 texto='El cerebro no puede cuidar a la vez las notas y la duración. Si '
                       'practicas el ritmo sobre una sola tecla, la mano aprende el golpe sin '
                       'distraerse. Cuando las notas llegan, el ritmo ya está hecho.'),
            dict(num=3, titulo='Cuatro corcheas y una blanca, el c. 6',
                 pista='cc. 6-8 · el ritmo es el de tu partitura · las notas son andamio',
                 sistemas=[
                     dict(cap='a) cuatro corcheas seguidas y una blanca · las corcheas son parejas '
                              'y sin prisa',
                          events=[n('D5', 'e'), n('C5', 'e'), n('D5', 'e'), n('E5', 'e'),
                                  n('C5', 'h')],
                          bars=1),
                     dict(cap='b) el c. 7: silencio de negra, dos corcheas, una negra y otras dos '
                              'corcheas',
                          events=[sil('q'), n('D5', 'e'), n('D5', 'e'), n('C5'),
                                  n('D5', 'e'), n('E5', 'e')],
                          bars=1, show_time=False),
                     dict(cap='c) y el c. 8: una negra y una blanca con puntillo',
                          events=[n('D5'), n('C5', 'h.')], bars=1, show_time=False),
                 ]),
            dict(num=4, titulo='La izquierda, grave y larga',
                 pista='andamio · la izquierda del principio es una negra y una blanca con puntillo',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) una negra y una blanca con puntillo · el sonido grave se deja '
                              'sonar entero antes de cambiar',
                          events=[n('F2'), n('F2', 'h.'), n('G2'), n('G2', 'h.')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=5, titulo='La repetición de los cuatro primeros compases',
                 pista='andamio · la barra de repetición cierra el c. 4 de tu partitura',
                 sistemas=[
                     dict(cap='a) dos compases con barra de repetición al final · se vuelve al '
                              'principio y se toca otra vez igual',
                          events=[n('E5'), n('D5'), n('C5'), n('D5'),
                                  n('C5', 'h'), n('A4', 'h')],
                          bars=2, repetir='cierra'),
                 ]),
        ] + bloques_extra('La menor', 11, 'A4', 'A2',
                          'el ritmo largo-largo-corto y las dos semicorcheas',
                          desde=6, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Eye of the Tiger · para casa',
            intro='Veinte minutos al día. La pieza dura dos minutos, pero el ritmo hay que '
                  'dejarlo clavado antes de añadir nada.',
            bloques=[
                plan((5, 'El golpe del c. 1 sobre una sola tecla, hasta que salga solo'),
                     (4, 'El c. 5 con las dos semicorcheas, contado en voz alta'),
                     (4, 'La izquierda sola: una negra y una blanca con puntillo'),
                     (7, 'Los cc. 1-8 con las dos manos, sin parar')),
                metronomo('Empieza a ♩ = 60 con el golpe del c. 1 sobre una sola nota y sube de '
                          'cinco en cinco mientras te salga igual.',
                          'Tu partitura no trae tempo: el número lo decides tú y lo apuntas a '
                          'lápiz. Cuanto más alto, más tiene que sonar el golpe al unísono.',
                          titulo='A qué velocidad te sale'),
                nombres(['A4', 'C5', 'E5', 'G5', 'D5', 'B4', 'F5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son las notas del andamio de esta semana · dos son de la tríada de '
                              'La menor'),
                colorear([n('E5', 'e'), n('G5', 's'), n('E5', 's'), n('E5', 'h'),
                          n('D5', 'e'), n('C5', 'e'), n('D5', 'e'), n('E5', 'e'), n('C5', 'h')],
                         ['Las corcheas, de azul.',
                          'Las semicorcheas, de rojo.',
                          'Las blancas, de verde.'],
                         titulo='Colorea según la figura',
                         pista='son los ritmos de los cc. 5 y 6 de tu partitura, en notas nuestras'),
                diferencias([sil('q'), n('E5', 'e'), n('G5', 's'), n('E5', 's'), n('E5', 'h')],
                            [sil('q'), n('E5', 'e'), n('E5', 'e'), n('E5', 'h')],
                            cuantas=2,
                            titulo='Busca las diferencias',
                            pista='arriba, el c. 5 de tu partitura en notas nuestras · abajo, con '
                                  'una figura cambiada'),
                para_clase('El ritmo del c. 1 a la velocidad que te salga sin fallo, y los cc. 5-8 '
                           'despacio con las dos semicorcheas bien separadas. Si me dices a '
                           'cuánto lo tocas, buscamos el siguiente número.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
