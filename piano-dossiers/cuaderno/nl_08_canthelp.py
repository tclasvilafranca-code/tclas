# -*- coding: utf-8 -*-
"""Can't Help Falling in Love — pieza 8 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arreglo
   de Seb Alejandro, descarga de Musescore, "Piano ~ Chords ~ Lyrics",
   2 páginas; el mismo archivo que la pieza 11 de José María y de Josep,
   byte a byte):

     - Re mayor: dos sostenidos detrás de la clave (Fa y Do).
     - Compás de 3/4.
     - Lleva las letras de los acordes impresas encima (D, F♯m, Bm…) y la
       letra de la canción debajo.
     - La izquierda va en corcheas, no en notas largas: se mueve todo el rato.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
RE = 'Re mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=8, nivel='avanzado', slug='CantHelpFalling',
    formato='adulto',
    titulo_corto="Can't Help Falling in Love", time_sig=(3, 4), key_sig=RE,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'Cant-Falling-in-love-elvis-presley.'),
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
                 'Dos sostenidos: todos los Fa y todos los Do van a la tecla negra de su derecha.'),
                ('LA IZQUIERDA', 'Se mueve',
                 'Corcheas todo el rato, no notas largas: aquí anda de verdad, y necesita su propio '
                 'tiempo de estudio.'),
                ('EL CIFRADO', 'D, F♯m, Bm',
                 'Las letras de encima son los acordes: no se tocan, sirven para entender por dónde '
                 'va la armonía.'),
                ('EL COMPÁS', 'Tres golpes',
                 'Un vals lento, apoyado en el primer golpe de cada compás.'),
            ],
            pie='La melodía no es de los años sesenta: viene de una canción francesa de 1784, '
                '"Plaisir d\'amour". Elvis la grabó en 1961 casi igual, solo que más lenta y en tres '
                'tiempos.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, tranquila · andamio',
             [n('D4', 'h.'), n('F#4', 'h.')], OCRE, 'treble', RE),
            ('MANO IZQUIERDA', 'corcheas, y no para · andamio',
             corch(['A2', 'E3']) + corch(['A3', 'E3']) + corch(['A2', 'E3']),
             AZUL, 'bass', RE),
        ],
        especial=[
            'Hay dos sostenidos detrás de la clave: todos los Fa y todos los Do van a la tecla negra.',
            'Compás de 3/4: tres golpes por compás, como un vals lento.',
            'Las letras de encima del pentagrama son los acordes, no notas para tocar.',
            'La letra de la canción va debajo, sílaba a sílaba.',
            'La mano izquierda va en corcheas casi todo el rato.',
            'Son dos páginas.',
        ],
        reto='La izquierda: es la primera pieza en la que no descansa, y encima le tocan dos teclas '
             'negras nuevas para esa mano.',
        truco='Trabaja la izquierda sola y de memoria, cuatro compases, hasta poder hacerla mirando a '
              'otro lado. Tiene menos notas y más repetición que la derecha, así que se memoriza rápido.',
        sabias='Elvis grabó la canción en 1961 para la película "Blue Hawaii", y desde entonces se ha '
               'versionado cientos de veces en géneros que van del reggae al heavy metal.',
        qr=dict(titulo='Escúchala',
                texto='Busca también "Plaisir d\'amour": es la misma melodía con doscientos años de '
                      'diferencia.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La protagonista de esta semana es la mano izquierda: dedícale más minutos que a la '
              'derecha. La melodía la tienes de oído y sale sola; la izquierda no.',
        reglas=['LOS FA Y LOS DO, EN TECLA NEGRA', 'LA IZQUIERDA, DE MEMORIA',
                'EL PESO, EN EL PRIMER GOLPE'],
        bloques=[
            dict(num=1, titulo='Los dos sostenidos: dónde caen',
                 pista='andamio en Re mayor · arpegios sobre la tonalidad',
                 sistemas=[
                     dict(cap='a) el arpegio de Re, con las dos teclas negras dentro',
                          events=[n('D4'), n('F#4'), n('A4'),
                                  n('D5'), n('A4'), n('F#4'),
                                  n('D4'), n('C#4'), n('D4'),
                                  n('F#4'), n('A4'), n('D5')],
                          bars=4, key_sig=RE),
                     dict(cap='b) y bajando desde arriba, pasando siempre por las dos negras',
                          events=[n('D5'), n('C#5'), n('B4'),
                                  n('A4'), n('G4'), n('F#4'),
                                  n('E4'), n('D4'), n('C#4')],
                          bars=3, key_sig=RE, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda, sola y de memoria', clef='bass',
                 pista='andamio en Re mayor · corcheas, y no descansa',
                 sistemas=[
                     dict(cap='a) primero en negras, para ver el dibujo',
                          events=[n('E3'), n('B3'), n('E4'),
                                  n('B2'), n('F#3'), n('B3')],
                          bars=2, clef='bass', key_sig=RE),
                     dict(cap='b) y ahora en corcheas, con el peso en la primera de cada compás',
                          events=corch(['E3', 'B3']) + corch(['E4', 'B3']) + corch(['E3', 'B3']),
                          bars=1, clef='bass', key_sig=RE, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA PRIMERO',
                 texto='La melodía de esta canción la tienes de oído, así que tu cabeza la corrige '
                       'sola si te equivocas. Con la izquierda no pasa eso, porque nadie se sabe el '
                       'acompañamiento de memoria. Si la dejas para el final, se queda a medias y es '
                       'la que sostiene la pieza entera.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio · muy despacio, apoyando el primer golpe',
                 sistemas=[
                     dict(cap='a) la derecha, larga y tranquila, encima del vaivén de la izquierda',
                          events=[n('A4', 'h.'), n('D5', 'h.'),
                                  n('F#4', 'h.'), n('A4', 'h.')],
                          bars=4, key_sig=RE),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · una nota larga arriba y '
                              'seis cortas debajo: ese es todo el reparto de la pieza',
                          events=(corch(['E3', 'B3']) + corch(['E4', 'B3']) +
                                  corch(['E3', 'B3']) + corch(['B2', 'F#3']) +
                                  corch(['B3', 'F#3']) + corch(['B2', 'F#3'])),
                          bars=2, clef='bass', key_sig=RE, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
