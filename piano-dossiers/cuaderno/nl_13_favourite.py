# -*- coding: utf-8 -*-
"""My Favourite Things (The Sound of Music) — pieza 13 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (Rodgers y Hammerstein,
   arreglo de Kaitlin, Musescore, 1 página, 55 compases; el mismo archivo
   que la pieza 15 de Josep, byte a byte):

     - Un sostenido detrás de la clave, y la música empieza y descansa en
       Mi: Mi menor, con el estribillo pasando a Sol mayor.
     - 3/4, y pone "♩ = 160".
     - Cifrado impreso encima del pentagrama: Em · C · Am · D · G · B.
     - La izquierda hace acordes con puntillo, uno por compás, y luego pasa
       a tres golpes por compás.
     - Hay barras de repetición, casilla de primera y segunda vez, calderón
       y acentos escritos (>) en la última parte.
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
MIm = 'Mi menor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=13, nivel='avanzado', slug='MyFavouriteThings',
    formato='adulto',
    titulo_corto='My Favourite Things', time_sig=(3, 4), key_sig=MIm,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'my-favourite-things-the-sound-.pdf'),
    yt='https://www.youtube.com/results?search_query=my+favourite+things+piano+easy',

    ficha=dict(
        titulo='My Favourite Things',
        autor='Richard Rodgers y Oscar Hammerstein II · arreglo de Kaitlin',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '3/4'),
               ('Tempo', '♩ = 160'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Una · 55 compases')],
        titulo_ritmos='Un vals rápido',
        pie_ritmos='Andamio en Mi menor. Lo literal es el reparto: melodía en negras arriba y un '
                   'acorde por compás abajo, en compás de tres y a ♩ = 160.',
        armonia=dict(
            titulo='Rápida, larga y apretada',
            tarjetas=[
                ('♩ = 160', 'Muy rápida',
                 'Casi 55 compases por minuto: la pieza entera dura poco más de un minuto de reloj.'),
                ('SEIS ACORDES', 'El cifrado',
                 'Em, C, Am, D, G y B impresos encima del pentagrama. El B es mayor en medio de una '
                 'pieza menor: es el que empuja de vuelta al Mi.'),
                ('55 COMPASES', 'En una página',
                 'Muy apretada de leer, no de tocar: se arregla con lápiz marcando las frases, no '
                 'con más horas de dedos.'),
                ('LOS ACENTOS', 'Escritos',
                 'En la última parte hay acentos (>) sobre algunas notas, y un calderón: no son '
                 'adorno, están escritos.'),
            ],
            pie='La canción es de 1959, cantada en la película durante una tormenta. Diez años '
                'después John Coltrane la convirtió en un estándar de jazz de catorce minutos.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, en negras · andamio',
             [n('E4'), n('G4'), n('G4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'un acorde por compás · andamio',
             [ac(('E2', 'B2', 'E3'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Un sostenido detrás de la clave: Fa sostenido.',
            'La pieza empieza y descansa en Mi: es Mi menor.',
            'Compás de 3/4 y "♩ = 160": muy rápido.',
            'El cifrado viene impreso: Em, C, Am, D, G y B.',
            'Hay repeticiones, casillas de primera y segunda vez y un calderón.',
            'En la última parte hay acentos (>) escritos sobre algunas notas.',
        ],
        reto='Leer 55 compases a ♩ = 160 sin perder el renglón: la dificultad no está en las manos, '
             'está en el ojo, que a esa velocidad no tiene tiempo de volver a buscar dónde iba.',
        truco='Marca a lápiz dónde empieza cada frase de cuatro compases, con una rayita vertical: '
              'cuando el ojo se pierda, vuelve a la rayita más cercana, no al principio de la línea.',
        sabias='La misma melodía suena completamente distinta según quién la toque: hay versiones de '
               'jazz, de villancico e incluso de heavy metal, todas reconocibles y todas muy '
               'diferentes entre sí.',
        qr=dict(titulo='Escúchala',
                texto='Busca dos versiones muy distintas de la misma canción y compara qué cambia y '
                      'qué se mantiene igual.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo primero de esta semana no es tocar: es coger el lápiz y marcar las frases. A 160 '
              'la pieza se estudia leyendo por grupos, no nota a nota.',
        reglas=['MARCAR LAS FRASES A LÁPIZ', 'LEER POR ACORDES, NO POR NOTAS',
                'EL PRIMER GOLPE PESA, LOS OTROS DOS NO'],
        bloques=[
            dict(num=1, titulo='Los seis acordes del cifrado, de un vistazo', clef='bass',
                 pista='son los que trae impresos tu partitura · el objetivo es reconocerlos sin leer',
                 sistemas=[
                     dict(cap='a) en otro orden: G, D y Am · fíjate en cuáles comparten notas',
                          events=[ac(('G2', 'D3', 'G3'), 'h.'), ac(('D2', 'A2', 'D3'), 'h.'),
                                  ac(('A2', 'E3', 'A3'), 'h.')],
                          acento=True,
                          bars=3, clef='bass', key_sig=MIm, time_sig=(3, 4)),
                     dict(cap='b) y C, B y Em · el B es mayor en medio de una pieza menor',
                          events=[ac(('C2', 'G2', 'C3'), 'h.'), ac(('B2', 'D#3', 'F#3'), 'h.'),
                                  ac(('E2', 'B2', 'E3'), 'h.')],
                          calderon=True,
                          bars=3, clef='bass', key_sig=MIm, time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=2, titulo='El vals: el primero pesa y los otros dos no',
                 pista='andamio en Mi menor · a 160 el compás dura poco más de un segundo',
                 sistemas=[
                     dict(cap='a) una frase distinta que también sube y se para',
                          events=[n('B4'), n('D5'), n('D5'),
                                  n('E5'), n('F#5'), n('F#5'),
                                  n('B5'), n('A5'), n('F#5'),
                                  n('D5', 'h.')],
                          bars=4, key_sig=MIm, time_sig=(3, 4)),
                     dict(cap='b) y bajando en una frase de tres compases, distinta de la de clase',
                          events=[n('F#5'), n('E5'), n('D5'),
                                  n('B4'), n('D5'), n('E5'),
                                  n('B4', 'h.')],
                          bars=3, key_sig=MIm, time_sig=(3, 4), show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LAS RAYITAS DE LÁPIZ',
                 texto='Marca con una rayita el principio de cada frase de cuatro compases. Cuando el '
                       'ojo se pierda —y a 160 se va a perder— vuelves a la rayita más cercana, no '
                       'al principio de la línea.'),
            dict(num=3, titulo='Las dos manos, cuatro compases',
                 pista='andamio en Mi menor · empieza a 90, no a 160',
                 sistemas=[
                     dict(cap='a) el acorde en el uno y la melodía por encima, distinta de la de '
                              'clase · el acorde no se repite en el dos ni en el tres',
                          events=[ac(('G2', 'B4')), n('D5'), n('D5'),
                                  ac(('D2', 'F#5')), n('F#5'), n('F#5')],
                          bars=2, key_sig=MIm, time_sig=(3, 4)),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
