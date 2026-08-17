# -*- coding: utf-8 -*-
"""Can't Help Falling in Love — pieza 11 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arreglo
   de Seb Alejandro, descarga de Musescore, "Piano ~ Chords ~ Lyrics",
   2 páginas):

     - RE MAYOR: DOS sostenidos detrás de la clave. Es la primera pieza del
       cuaderno con dos alteraciones en la armadura: van al Fa y al Do.
     - Compás de 3/4.
     - Lleva las letras de los acordes impresas encima (D, F♯m, Bm…) y la
       letra de la canción debajo.
     - La izquierda va en corcheas, no en notas largas: es la primera vez en
       el cuaderno que la mano izquierda se mueve de verdad todo el rato.

   Lo que NO se cita nota a nota: la medición no sale limpia con la letra y el
   cifrado encima. El material va como ANDAMIO en Re mayor y remite a la
   partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, corch, objetivo, plan, teclado, contar,
                      figuras, acuerdate)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
RE = 'Re mayor'

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=11, nivel='iniciación',
    slug='CantHelpFalling', formato='adulto',
    titulo_corto="Can't Help Falling in Love", time_sig=(3, 4), key_sig=RE,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'cant-help-falling-in-love-elvis-presley.'),
    yt='https://www.youtube.com/results?search_query=cant+help+falling+in+love+piano+easy',

    ficha=dict(
        titulo="Can't Help Falling in Love",
        autor='Elvis Presley · arreglo de Seb Alejandro · piano, cifrado y letra',
        datos=[('Tonalidad', 'Re mayor'), ('Novedad', 'Dos sostenidos'),
               ('Compás', '3/4'), ('Mano izq.', 'En corcheas'),
               ('Encima', 'El cifrado')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Re mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Los Fa y los Do van todos a la tecla negra.',
        armonia=dict(
            titulo='Dos sostenidos, y una izquierda que ya no descansa',
            tarjetas=[
                ('LA ARMADURA', 'Fa y Do',
                 'Dos sostenidos: todos los Fa y todos los Do van a la tecla negra de su derecha. Es '
                 'el primer sitio del cuaderno con dos.'),
                ('LA IZQUIERDA', 'Se mueve',
                 'Corcheas todo el rato, no notas largas. Hasta ahora aguantaba; aquí anda, y hay que '
                 'darle tiempo propio de estudio.'),
                ('EL CIFRADO', 'D, F♯m, Bm',
                 'Las letras de encima son los acordes. No se tocan: sirven para acompañar y para '
                 'entender por dónde va la armonía.'),
                ('EL COMPÁS', 'Tres golpes',
                 'Un vals lento. La canción se apoya en el primer golpe de cada compás, y eso es lo '
                 'que hay que hacer sonar.'),
            ],
            pie='La pieza es conocidísima y eso ayuda: cuando la melodía la llevas en la cabeza, los '
                'errores se oyen solos y no hace falta que nadie te los diga.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, tranquila · andamio',
             [n('D4', 'h.'), n('F#4', 'h.')], OCRE, 'treble', RE),
            ('MANO IZQUIERDA', 'corcheas, y no para · andamio',
             corch(['A2', 'E3']) + corch(['A3', 'E3']) + corch(['A2', 'E3']),
             AZUL, 'bass', RE),
        ],
        especial=[
            'Hay DOS sostenidos detrás de la clave: todos los Fa y todos los Do van a la tecla negra.',
            'Compás de 3/4: tres golpes por compás, como un vals lento.',
            'Las letras de encima del pentagrama son los acordes, no notas para tocar.',
            'La letra de la canción va debajo, sílaba a sílaba.',
            'La mano izquierda va en corcheas casi todo el rato.',
            'Son dos páginas.',
        ],
        reto='La izquierda. Es la primera pieza en la que no descansa, y encima le tocan dos teclas '
             'negras que hasta ahora no habías usado con esa mano.',
        truco='Trabaja la izquierda SOLA y de memoria, cuatro compases, hasta que puedas hacerla '
              'mirando a otro lado. La izquierda tiene menos notas y más repetición que la derecha, '
              'así que se memoriza rápido; y una vez memorizada, deja de robarte atención cuando '
              'juntes las manos.',
        sabias='La melodía no es de los años sesenta: es de una canción francesa de 1784, "Plaisir '
               'd\'amour". Elvis la grabó en 1961 casi igual, solo que más lenta y en tres tiempos.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la de Elvis y luego busca "Plaisir d\'amour": es la misma melodía con '
                      'doscientos años de diferencia.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana la protagonista es la mano izquierda, y no es una forma de hablar: dedícale '
              'más minutos que a la derecha. La melodía te la sabes de oído y va a salir sola; la '
              'izquierda no.',
        reglas=['LOS FA Y LOS DO, EN TECLA NEGRA', 'LA IZQUIERDA, DE MEMORIA',
                'EL PESO, EN EL PRIMER GOLPE'],
        bloques=[
            dict(num=1, titulo='Los dos sostenidos: dónde caen',
                 pista='andamio en Re mayor · la escala de la pieza',
                 sistemas=[
                     dict(cap='a) la escala de Re, subiendo y bajando · las teclas negras son la '
                              'tercera y la séptima',
                          events=[n('D4'), n('E4'), n('F#4'),
                                  n('G4'), n('A4'), n('B4'),
                                  n('C#5'), n('D5'), n('C#5'),
                                  n('B4'), n('A4'), n('G4')],
                          bars=4, key_sig=RE),
                     dict(cap='b) y saltando entre las dos negras · sin mirarse la mano',
                          events=[n('F#4'), n('C#5'), n('F#4'),
                                  n('A4'), n('C#5'), n('A4'),
                                  n('F#4'), n('D4'), n('F#4')],
                          bars=3, key_sig=RE, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda, sola y de memoria', clef='bass',
                 pista='andamio en Re mayor · corcheas, y no descansa',
                 sistemas=[
                     dict(cap='a) primero en negras, para ver el dibujo',
                          events=[n('D3'), n('A3'), n('D4'),
                                  n('A2'), n('E3'), n('A3')],
                          bars=2, clef='bass', key_sig=RE),
                     dict(cap='b) y ahora en corcheas, que es como está escrito · el peso en la '
                              'primera de cada compás',
                          events=corch(['D3', 'A3']) + corch(['D4', 'A3']) + corch(['D3', 'A3']),
                          bars=1, clef='bass', key_sig=RE, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA PRIMERO',
                 texto='La melodía de esta canción la conoces de oído, así que tu cabeza la corrige '
                       'sola: si te equivocas, lo oyes. Con la izquierda no pasa eso, porque nadie se '
                       'sabe el acompañamiento. Si la dejas para el final, se queda a medias y es la '
                       'que sostiene la pieza entera. Dale los cinco minutos buenos del día.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio · muy despacio, apoyando el primer golpe',
                 sistemas=[
                     dict(cap='a) la derecha, larga y tranquila, encima del vaivén de la izquierda',
                          events=[n('D4', 'h.'), n('F#4', 'h.'),
                                  n('A4', 'h.'), n('F#4', 'h.')],
                          bars=4, key_sig=RE),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · una nota larga arriba y '
                              'seis cortas debajo: ese es todo el reparto de la pieza',
                          events=(corch(['D3', 'A3']) + corch(['D4', 'A3']) +
                                  corch(['D3', 'A3']) + corch(['A2', 'E3']) +
                                  corch(['A3', 'E3']) + corch(['A2', 'E3'])),
                          bars=2, clef='bass', key_sig=RE, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="Can't Help Falling in Love · para casa",
            intro='Veinte minutos al día, y más de la mitad para la mano izquierda.',
            bloques=[
                objetivo('La mano izquierda sola, cuatro compases, de memoria y sin mirarse la mano.'),
                plan((4, 'La escala de Re, subiendo y bajando'),
                     (4, 'Saltos entre el Fa♯ y el Do♯, sin mirar'),
                     (7, 'La izquierda sola, hasta poder hacerla de memoria'),
                     (5, 'Las dos manos, dos compases muy despacio')),
                teclado({1: 1, 3: 2, 5: 3, 0: 4},
                        ['Escribe el nombre de las cuatro teclas blancas marcadas.',
                         'Y pinta las dos negras de esta pieza: la de la derecha de la número 1 y la '
                         'de la derecha de la número 4.'],
                        titulo='En el teclado',
                        pista='Re mayor tiene dos teclas negras'),
                contar([n('D4'), n('E4'), n('F#4'), n('G4'), n('A4'), n('B4'), n('C#5'), n('D5')],
                       ['¿Cuántas notas hay en total?', '¿Cuántas van en tecla negra?',
                        '¿Cuál es la nota más grave?'],
                       titulo='Mira y cuenta',
                       pista='es la escala de Re mayor, la de esta pieza'),
                figuras([('h.', 'blanca con puntillo'), ('q', 'negra'), ('e', 'corchea'),
                         ('h', 'blanca')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='la blanca con puntillo llena un compás entero de 3/4'),
                acuerdate('En un compás de tres, el peso va en el primer golpe y los otros dos van '
                          'detrás, más ligeros. Si los tres suenan iguales, deja de ser un vals y se '
                          'convierte en un ejercicio. Es lo único que separa esta pieza de sonar bien '
                          'o sonar a deberes.',
                          etiqueta='UN-dos-tres, NO un-dos-tres'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
