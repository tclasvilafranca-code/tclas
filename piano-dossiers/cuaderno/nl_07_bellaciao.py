# -*- coding: utf-8 -*-
"""Bella Ciao (a cuatro manos) — pieza 7 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Bella Ciao 4 mains",
   Musescore, 1 página, 19 compases; el mismo archivo que la pieza 10 de
   Josep, byte a byte):

     - Dos bemoles detrás de la clave, y la melodía gira alrededor de Sol:
       Sol menor.
     - 4/4.
     - Es a cuatro manos. El Piano 1 lleva clave de sol y clave de fa, y la
       melodía va arriba, en negras y blancas.
     - El Piano 2 hace acordes repetidos en corcheas: es el motor rítmico.
     - Aparecen Fa sostenidos escritos delante de las notas, no en la
       armadura: es la sensible del tono menor.
     - Hay barra de repetición y casilla de segunda vez.
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
SOLm = 'Sol menor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=7, nivel='avanzado', slug='BellaCiao',
    formato='adulto',
    titulo_corto='Bella Ciao', time_sig=(4, 4), key_sig=SOLm,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'bella-ciao-piano( 4 manos).pdf'),
    yt='https://www.youtube.com/results?search_query=bella+ciao+piano+4+manos',

    ficha=dict(
        titulo='Bella Ciao',
        autor='Canción popular italiana · versión a cuatro manos · parte del Piano 1',
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Alteración', 'Fa sostenido'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Melodía arriba, motor abajo',
        pie_ritmos='Andamio en Sol menor. Lo literal es el reparto: tu melodía en negras y blancas, '
                   'y el Piano 2 con acordes repetidos en corcheas debajo.',
        armonia=dict(
            titulo='El primer tono menor de tu repertorio',
            tarjetas=[
                ('DOS BEMOLES', 'Sol menor',
                 'Si bemol y Mi bemol: la misma armadura que Si bemol mayor, pero la melodía descansa '
                 'en Sol y suena a otra cosa distinta.'),
                ('EL FA SOSTENIDO', 'La sensible',
                 'Escrito delante de la nota, no en la armadura: es la que empuja hacia Sol y hace '
                 'que la pieza suene a menor de verdad.'),
                ('EL MOTOR', 'Piano 2',
                 'La otra parte hace acordes repetidos en corcheas de principio a fin: tú llevas la '
                 'melodía y no tienes que marcar el pulso, ya está marcado.'),
                ('LA REPETICIÓN', 'Con segunda vez',
                 'Hay barra de repetición y una casilla "2.": la segunda vuelta no acaba igual que la '
                 'primera.'),
            ],
            pie='La melodía es más antigua que la letra política: se cantaba en los arrozales del '
                'norte de Italia con otra letra bien distinta, mucho antes de la guerra.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, en negras y blancas · andamio',
             [n('D4'), n('G4'), n('G4'), n('G4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'sostiene por debajo · andamio',
             [n('G2', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Dos bemoles detrás de la clave: Si bemol y Mi bemol.',
            'La melodía gira alrededor de Sol: es Sol menor, no Si bemol mayor.',
            'Hay Fa sostenidos escritos delante de las notas: son la sensible.',
            'Compás de 4/4.',
            'El Piano 2 hace acordes repetidos en corcheas todo el rato.',
            'Hay barra de repetición y casilla de segunda vez.',
        ],
        reto='El Fa sostenido, que aparece y desaparece: no está en la armadura, así que unos '
             'compases lo llevan y otros no, y el oído todavía no lo distingue solo.',
        truco='Toca la escala de Sol menor entera, subiendo con el Fa sostenido y bajando con el Fa '
              'natural, diez veces. Cuando el oído reconozca las dos versiones, ya no hace falta mirar '
              'si está escrito.',
        sabias='La versión que hoy conoce todo el mundo se difundió después de la Segunda Guerra '
               'Mundial, aunque la melodía es mucho más vieja que esa historia.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el acompañamiento no para nunca: tu parte puede respirar porque '
                      'la de abajo no lo hace.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas: un tono menor con dos bemoles y una sensible que va y viene. El oído '
              'tiene que aprender a reconocer el Fa sostenido sin mirarlo.',
        reglas=['DOS BEMOLES: SI Y MI', 'EL FA SOSTENIDO VA Y VIENE',
                'CON METRÓNOMO SIEMPRE'],
        bloques=[
            dict(num=1, titulo='La escala de Sol menor, con la sensible y sin ella',
                 pista='andamio en Sol menor · es exactamente lo que hace la pieza',
                 sistemas=[
                     dict(cap='a) en terceras, subiendo con el Fa sostenido',
                          events=[n('G3'), n('Bb3'), n('A3'), n('C4'),
                                  n('Bb3'), n('D4'), n('C4'), n('F#4')],
                          bars=2, key_sig=SOLm),
                     dict(cap='b) y en terceras bajando, con el Fa natural',
                          events=[n('G4'), n('Eb4'), n('F4'), n('D4'),
                                  n('Eb4'), n('C4'), n('D4'), n('Bb3')],
                          bars=2, key_sig=SOLm, show_time=False),
                 ]),
            dict(num=2, titulo='La melodía, en negras y blancas',
                 pista='andamio en Sol menor · fíjate en dónde descansa: siempre en Sol',
                 sistemas=[
                     dict(cap='a) una frase distinta que también sube y se detiene',
                          events=[n('Bb4'), n('A4'), n('G4'), n('F#4'),
                                  n('G4'), n('A4', 'h'), n('Bb4')],
                          bars=2, key_sig=SOLm),
                     dict(cap='b) y vuelve a caer en Sol desde arriba del todo',
                          events=[n('D5'), n('Eb5'), n('D5'), n('C5'),
                                  n('A4', 'h'), n('G4', 'h')],
                          bars=2, key_sig=SOLm, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ESTUDIA CON METRÓNOMO',
                 texto='Cuando la otra parte lleva el pulso, tú no pones el tuyo: cabes en el suyo. '
                       'Estudiar en casa sin metrónomo enseña una versión propia del tempo que luego '
                       'hay que desaprender. Ponlo desde el primer día.'),
            dict(num=3, titulo='Las dos manos, con la izquierda sosteniendo',
                 pista='andamio en Sol menor · tu izquierda no es el motor: el motor es el Piano 2',
                 sistemas=[
                     dict(cap='a) melodía arriba y una nota larga abajo, distinta de la de la clase',
                          events=[ac(('D3', 'Bb4')), n('A4'), n('G4'), n('F#4'),
                                  ac(('G2', 'A4')), n('Bb4', 'h'), n('G4')],
                          bars=2, key_sig=SOLm),
                     dict(cap='b) y con el Fa sostenido dentro de la frase',
                          events=[ac(('G2', 'D5')), n('Eb5'), n('D5'), n('C5'),
                                  ac(('D3', 'F#4'), 'h'), n('G4', 'h')],
                          bars=2, key_sig=SOLm, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
