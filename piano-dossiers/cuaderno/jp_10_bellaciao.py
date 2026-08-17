# -*- coding: utf-8 -*-
"""Bella Ciao (a cuatro manos) — pieza 10 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Bella Ciao 4 mains",
   Musescore, 1 página, 19 compases):

     - DOS BEMOLES detrás de la clave, y la melodía gira alrededor de Sol: es
       Sol menor. Primer tono menor del cuaderno.
     - 4/4. (A baja resolución parecía 3/4; ampliando a 250 dpi se ve el 4/4
       con claridad. Ver TRANSCRIPCION_JOSEP_FUENTES.)
     - Es a cuatro manos. El Piano 1 lleva clave de sol y clave de fa, y la
       melodía va arriba, en negras y blancas.
     - El Piano 2 hace acordes repetidos en corcheas: es el motor rítmico.
     - Aparecen Fa sostenidos escritos delante de las notas, no en la
       armadura: es la sensible del tono menor.
     - Hay barra de repetición y casilla de segunda vez.

   El material inventado va como ANDAMIO en Sol menor y remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, reto, plan, a_cuatro_manos, ordenar, nombres,
                      figuras, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=10, nivel='intermedio', slug='BellaCiao',
    formato='adulto',
    titulo_corto='Bella Ciao', time_sig=(4, 4), key_sig='Sol menor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'bella-ciao-piano-(4 MANOS).pdf'),
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
            titulo='El primer tono menor del cuaderno',
            tarjetas=[
                ('DOS BEMOLES', 'Sol menor',
                 'Si bemol y Mi bemol. La misma armadura que Si bemol mayor, pero la melodía gira '
                 'alrededor de Sol y suena a otra cosa: la armadura no decide el tono, lo decide '
                 'dónde descansa la música.'),
                ('EL FA SOSTENIDO', 'La sensible',
                 'Escrito delante de la nota, no en la armadura. Es la nota que empuja hacia Sol: '
                 'quítala y la pieza deja de sonar a menor de verdad.'),
                ('EL MOTOR', 'Piano 2',
                 'La otra parte hace acordes repetidos en corcheas de principio a fin. Tú llevas la '
                 'melodía encima y no tienes que marcar el pulso: ya está marcado.'),
                ('LA REPETICIÓN', 'Con segunda vez',
                 'Hay barra de repetición y una casilla "2.". La segunda vuelta no acaba igual que '
                 'la primera: hay que mirar dónde se separan.'),
            ],
            pie='Que la otra parte lleve el pulso cambia cómo se estudia: en casa hay que tocar con '
                'metrónomo sí o sí, porque en clase el metrónomo va a ser la profesora y no espera.',
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
        reto='El Fa sostenido, que aparece y desaparece. No está en la armadura, así que unos '
             'compases lo llevan y otros no, y el oído todavía no te avisa porque es tu primer '
             'tono menor.',
        truco='Toca la escala de Sol menor entera, subiendo con el Fa sostenido y bajando con el Fa '
              'natural, diez veces. Es exactamente lo que hace la pieza, y cuando el oído reconozca '
              'las dos versiones ya no necesitas mirar si está escrito o no.',
        sabias='La melodía es más antigua que la letra política: se cantaba en los arrozales del '
               'norte de Italia con otra letra, la de las trabajadoras que pasaban el día metidas '
               'en el agua. La versión que todo el mundo conoce se difundió después de la guerra.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el acompañamiento no para nunca. Tu parte puede respirar '
                      'porque la de abajo no lo hace.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas: un tono menor con dos bemoles y una sensible que va y viene. La '
              'melodía es fácil; lo que hay que hacer es que el oído aprenda a reconocer el Fa '
              'sostenido sin mirarlo.',
        reglas=['DOS BEMOLES: SI Y MI', 'EL FA SOSTENIDO VA Y VIENE',
                'CON METRÓNOMO SIEMPRE'],
        bloques=[
            dict(num=1, titulo='La escala de Sol menor, con la sensible y sin ella',
                 pista='andamio en Sol menor · es exactamente lo que hace la pieza',
                 sistemas=[
                     dict(cap='a) subiendo con el Fa sostenido: es el que empuja hacia el Sol de '
                              'arriba · escúchalo, no lo mires',
                          events=[n('G3'), n('A3'), n('Bb3'), n('C4'),
                                  n('D4'), n('Eb4'), n('F#4'), n('G4')],
                          bars=2, key_sig='Sol menor'),
                     dict(cap='b) y bajando con el Fa natural, que es como baja la pieza · las dos '
                              'versiones son correctas y suenan distinto',
                          events=[n('G4'), n('F4'), n('Eb4'), n('D4'),
                                  n('C4'), n('Bb3'), n('A3'), n('G3')],
                          bars=2, key_sig='Sol menor', show_time=False),
                 ]),
            dict(num=2, titulo='La melodía, en negras y blancas',
                 pista='andamio en Sol menor · fíjate en dónde descansa: siempre en Sol',
                 sistemas=[
                     dict(cap='a) la frase sube y se para arriba · las blancas duran los dos golpes '
                              'enteros aunque el acompañamiento siga moviéndose debajo',
                          events=[n('D4'), n('G4'), n('G4'), n('G4'),
                                  n('A4'), n('Bb4', 'h'), n('G4')],
                          bars=2, key_sig='Sol menor'),
                     dict(cap='b) y vuelve a caer en Sol, que es lo que hace que suene a menor · '
                              'aquí el Fa sostenido empuja hacia el final',
                          events=[n('D5'), n('C5'), n('Bb4'), n('A4'),
                                  n('F#4', 'h'), n('G4', 'h')],
                          bars=2, key_sig='Sol menor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ESTUDIA CON METRÓNOMO',
                 texto='Cuando la otra parte lleva el pulso, tú no pones el tuyo: cabes en el suyo. '
                       'Si estudias en casa sin metrónomo aprendes tu propia versión del tempo, y '
                       'luego hay que desaprenderla. Ponlo desde el primer día.'),
            dict(num=3, titulo='Las dos manos, con la izquierda sosteniendo',
                 pista='andamio en Sol menor · tu izquierda no es el motor: el motor es el Piano 2',
                 sistemas=[
                     dict(cap='a) melodía arriba y una nota larga abajo · si tu izquierda empieza a '
                              'marcar el pulso, estás haciendo el trabajo del otro',
                          events=[ac(('G2', 'D4')), n('G4'), n('G4'), n('G4'),
                                  ac(('D3', 'A4')), n('Bb4', 'h'), n('G4')],
                          bars=2, key_sig='Sol menor'),
                     dict(cap='b) y con el Fa sostenido metido en la frase · la nota larga del '
                              'final cae justo cuando el Piano 2 sigue moviéndose',
                          events=[ac(('D3', 'D5')), n('C5'), n('Bb4'), n('A4'),
                                  ac(('G2', 'F#4'), 'h'), n('G4', 'h')],
                          bars=2, key_sig='Sol menor', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Bella Ciao · para casa',
            intro='Veinte minutos, con metrónomo desde el primer día.',
            bloques=[
                reto('Reconocer el Fa sostenido de oído, sin mirar si está escrito.',
                     'Toca la escala de Sol menor subiendo con Fa sostenido y bajando con Fa '
                     'natural, diez veces al día. Cuando notes la diferencia sin pensarla, la pieza '
                     'se toca sola.'),
                plan((4, 'La escala de Sol menor, subiendo y bajando'),
                     (6, 'La melodía sola, con metrónomo'),
                     (5, 'La izquierda sola, sosteniendo'),
                     (5, 'Las dos juntas, hasta la barra de repetición')),
                a_cuatro_manos('El Piano 2 no para: hace acordes en corcheas de principio a fin. '
                               'Tú puedes respirar porque él no lo hace, pero eso significa que el '
                               'tempo lo pone él. Acordad la velocidad antes de empezar.'),
                ordenar(['La melodía con metrónomo, hasta la repetición.',
                         'La escala de Sol menor, con y sin sensible.',
                         'Las dos manos juntas, muy lento.',
                         'Mirar dónde se separan la primera y la segunda vuelta.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='uno de ellos es de lápiz y no de piano'),
                nombres(['G3', 'Bb3', 'D4', 'Eb4', 'F#4', 'G4', 'A4'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='estamos en Sol menor: dos bemoles, y ojo con la quinta'),
                figuras([('w', 'redonda'), ('h', 'blanca'), ('q', 'negra'), ('e', 'corchea')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='la corchea es la del acompañamiento del Piano 2'),
                para_clase('La melodía con metrónomo y a qué número la llevas. Y una pregunta que '
                           'sí merece la pena traer: en qué compases exactos aparece el Fa '
                           'sostenido, si los has marcado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
