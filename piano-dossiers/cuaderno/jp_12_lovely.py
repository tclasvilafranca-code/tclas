# -*- coding: utf-8 -*-
"""Lovely (Billie Eilish con Khalid) — pieza 12 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Amy Kieran,
   2 páginas, 44 compases, con letra):

     - UN SOSTENIDO detrás de la clave, y la música descansa en Mi: Mi menor.
     - 4/4, y pone "♩ = 115".
     - La derecha va en CORCHEAS SEGUIDAS desde el primer compás y casi sin
       parar: es una pieza de resistencia, no de dificultad.
     - La izquierda hace acordes de redonda, uno por compás, sosteniendo.
     - Los dos primeros compases la izquierda calla (silencios de redonda).
     - En el c. 11 hay barra de repetición y entra la letra.
     - Al final vuelve el dibujo de corcheas del principio.

   El material inventado va como ANDAMIO en Mi menor y remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jp_comun import (n, ac, sil, reto, plan, rodear, unir, colorear,
                      acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=12, nivel='intermedio', slug='Lovely',
    formato='adulto',
    titulo_corto='Lovely', time_sig=(4, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source', '-LOVELY.pdf'),
    yt='https://www.youtube.com/results?search_query=lovely+billie+eilish+piano+easy',

    ficha=dict(
        titulo='Lovely',
        autor='Billie Eilish con Khalid · arreglo de Amy Kieran',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 115'), ('Derecha', 'Corcheas seguidas'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Ocho corcheas arriba, una redonda abajo',
        pie_ritmos='Andamio en Mi menor. Lo literal es el reparto: corcheas sin parar en la derecha '
                   'y acordes de redonda en la izquierda, compás tras compás.',
        armonia=dict(
            titulo='Una pieza de aguante',
            tarjetas=[
                ('OCHO POR COMPÁS', 'Sin parar',
                 'La derecha hace ocho corcheas en cada compás durante casi toda la pieza. Ninguna '
                 'es difícil; lo difícil es que la número doscientas suene igual que la primera.'),
                ('UN SOSTENIDO', 'Mi menor',
                 'Fa sostenido detrás de la clave. La música descansa en Mi, no en Sol: por eso es '
                 'menor y no mayor, aunque la armadura sea la misma.'),
                ('LA IZQUIERDA', 'Redondas',
                 'Un acorde por compás y aguantarlo entero. Los dos primeros compases ni siquiera '
                 'toca: la derecha empieza sola.'),
                ('♩ = 115', 'Con número',
                 'A 115 las ocho corcheas del compás caen muy seguidas. Es la primera pieza del '
                 'cuaderno donde el problema es de resistencia y no de lectura.'),
            ],
            pie='En una pieza así el error no aparece al principio: aparece en el compás veinte, '
                'cuando la mano se cansa y las corcheas empiezan a no ser iguales. Por eso se '
                'estudia en trozos cortos y con la mano suelta, no repitiéndola entera.',
        ),
        ritmos=[
            ('MANO DERECHA', 'ocho corcheas seguidas · andamio',
             [n('B4', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e'),
              n('B4', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'un acorde de redonda por compás · andamio',
             [ac(('E2', 'B2', 'E3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Un sostenido detrás de la clave: Fa sostenido.',
            'La música descansa en Mi: es Mi menor.',
            'Pone "♩ = 115".',
            'La derecha va en corcheas seguidas desde el primer compás.',
            'Los dos primeros compases la izquierda no toca.',
            'La izquierda hace acordes de redonda, uno por compás.',
        ],
        reto='Que la corchea número doscientas suene igual que la primera. No es un problema de '
             'notas: es que la mano se agarrota a los veinte compases y el dibujo empieza a cojear '
             'sin que te des cuenta.',
        truco='Toca cuatro compases y PARA. Suelta la mano, déjala caer del todo, y sigue. Cuatro y '
              'parar, cuatro y parar. Si estudias la pieza entera de una vez, lo que practicas '
              'durante la mitad del tiempo es la mano cansada.',
        sabias='La canción se hizo famosa por la serie "13 Reasons Why" y no por un disco. Billie '
               'Eilish tenía dieciséis años al grabarla, y la escribió con su hermano en el '
               'dormitorio de casa de sus padres, que es donde grabaron casi todo el primer álbum.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el piano no para nunca y la voz sí. Ese contraste es la '
                      'canción: tú vas a hacer la parte que no para.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí no hay nada difícil de leer y sí mucho que aguantar: trozos cortos y mano suelta.',
        reglas=['CUATRO COMPASES Y PARAR', 'LA MANO SUELTA, NO AGARROTADA',
                'UN SOSTENIDO: EL FA'],
        bloques=[
            dict(num=1, titulo='El dibujo de corcheas, cuatro compases y parar',
                 pista='andamio en Mi menor · para de verdad al final, y suelta la mano',
                 sistemas=[
                     dict(cap='a) el dibujo sube y baja dentro del acorde · sin acentuar ninguna, '
                              'todas iguales de fuerza',
                          events=[n('E4', 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e'),
                                  n('E4', 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e'),
                                  n('D4', 'e'), n('F#4', 'e'), n('A4', 'e'), n('F#4', 'e'),
                                  n('D4', 'e'), n('F#4', 'e'), n('A4', 'e'), n('F#4', 'e')],
                          bars=2, key_sig='Mi menor'),
                     dict(cap='b) y con el acorde cambiando, que es lo que hace la pieza · el dedo '
                              'que se mueve es solo uno, los otros se quedan',
                          events=[n('C4', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e'),
                                  n('C4', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e'),
                                  n('B3', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e'),
                                  n('B3', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e')],
                          bars=2, key_sig='Mi menor', show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: un acorde y aguantar', clef='bass',
                 pista='la FORMA es literal (una redonda por compás); las notas, andamio en Mi menor',
                 sistemas=[
                     dict(cap='a) cae y se queda · comprueba en el cuarto golpe que sigue sonando, '
                              'que es donde todo el mundo la suelta',
                          events=[ac(('E2', 'B2', 'E3'), 'w'), ac(('D2', 'A2', 'D3'), 'w')],
                          bars=2, clef='bass', key_sig='Mi menor'),
                     dict(cap='b) y con los otros dos acordes de la pieza · el cambio se prepara '
                              'mientras suena el anterior',
                          events=[ac(('C2', 'G2', 'C3'), 'w'), ac(('B1', 'F#2', 'B2'), 'w')],
                          bars=2, clef='bass', key_sig='Mi menor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ CUATRO COMPASES Y PARAR',
                 texto='La mano se cansa antes de que tú lo notes, y cuando lo notas ya llevas un '
                       'rato tocando desigual. Lo que se aprende tocando cansado es a tocar '
                       'cansado.'),
            dict(num=3, titulo='Las dos manos, con la izquierda debajo',
                 pista='andamio en Mi menor · empieza a la mitad de 115 y no subas esta semana',
                 sistemas=[
                     dict(cap='a) el acorde entra en el uno y no se mueve más · las corcheas de '
                              'arriba pasan por encima sin apoyarse en él',
                          events=[ac(('E2', 'E4'), 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e'),
                                  n('E4', 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e'),
                                  ac(('C2', 'C4'), 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e'),
                                  n('C4', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e')],
                          bars=2, key_sig='Mi menor'),
                     dict(cap='b) y con el acorde de la izquierda cambiando cada compás · el brazo '
                              'izquierdo cae una vez y se queda; el derecho no para',
                          events=[ac(('D2', 'D4'), 'e'), n('F#4', 'e'), n('A4', 'e'), n('F#4', 'e'),
                                  n('D4', 'e'), n('F#4', 'e'), n('A4', 'e'), n('F#4', 'e'),
                                  ac(('B1', 'B3'), 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e'),
                                  n('B3', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e')],
                          bars=2, key_sig='Mi menor', show_time=False),
                 ]),
        ] + bloques_extra('Mi menor', 21, 'E4', 'E2',
                          'la última corchea suena igual que la primera',
                          desde=4, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Lovely · para casa',
            intro='Veinte minutos, en trozos de cuatro compases. Parar es parte del ejercicio.',
            bloques=[
                reto('Tocar veinte compases seguidos con todas las corcheas iguales.',
                     'Estúdialos de cuatro en cuatro, soltando la mano entre trozo y trozo. Solo el '
                     'último día de la semana los juntas: si los juntas antes, lo que practicas es '
                     'la mano cansada.'),
                plan((5, 'Cuatro compases y parar, soltando la mano'),
                     (5, 'Otros cuatro, y así hasta el compás 12'),
                     (5, 'La izquierda sola, comprobando las redondas'),
                     (5, 'Las dos juntas, de cuatro en cuatro')),
                rodear([[n('E4', 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e')],
                        [n('D4', 'e'), n('F#4', 'e'), n('A4', 'e'), n('F#4', 'e')],
                        [n('E4', 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e')],
                        [n('C4', 'e'), n('E4', 'e'), n('G4', 'e'), n('E4', 'e')]],
                       titulo='Rodea los dos medios compases iguales',
                       pista='andamio en Mi menor · el dibujo es siempre el mismo y cambian las notas'),
                unir([('Mi menor', 'un sostenido, y descansa en Mi'),
                      ('Redonda', 'dura los cuatro golpes del compás'),
                      ('Corchea', 'media negra: caben ocho en un compás de 4/4'),
                      ('♩ = 115', 'ciento quince negras por minuto')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de la ficha de esta pieza'),
                colorear([n('E4', 'e'), n('G4', 'e'), n('B4', 'w'), n('F#4', 'h'),
                          n('A4', 'e'), n('E4', 'e'), n('G4', 'h'), n('E4', 'w')],
                         ['Las corcheas, de azul.',
                          'Las redondas, de verde.',
                          'Y rodea el Fa sostenido: es la única alteración de la armadura.'],
                         titulo='Colorea según la figura',
                         pista='y luego di en voz alta cuánto dura cada una'),
                acuerdate('Esta semana no se sube la velocidad. Se toca a la mitad de 115 y se '
                          'busca que las corcheas sean iguales; la velocidad viene sola cuando el '
                          'dibujo está limpio, y no al revés.',
                          etiqueta='LA VELOCIDAD, LA SEMANA QUE VIENE'),
                para_clase('Doce compases con las corcheas iguales, aunque sea lento. Y dime en qué '
                           'compás notas que la mano empieza a cansarse: ese número es el que nos '
                           'dice cuánto podemos alargar el trozo la semana que viene.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
