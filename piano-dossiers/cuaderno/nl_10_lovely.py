# -*- coding: utf-8 -*-
"""Lovely (Billie Eilish con Khalid) — pieza 10 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Amy Kieran,
   2 páginas, 44 compases, con letra; el mismo archivo que la pieza 12 de
   Josep, byte a byte):

     - Un sostenido detrás de la clave, y la música descansa en Mi: Mi menor.
     - 4/4, y pone "♩ = 115".
     - La derecha va en corcheas seguidas desde el primer compás y casi sin
       parar: es una pieza de resistencia, no de dificultad.
     - La izquierda hace acordes de redonda, uno por compás, sosteniendo.
     - Los dos primeros compases la izquierda calla (silencios de redonda).
     - En el c. 11 hay barra de repetición y entra la letra.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import escala, cadencia, arpegio, giro, encajar
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
MIm = 'Mi menor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=10, nivel='avanzado', slug='Lovely',
    formato='adulto',
    titulo_corto='Lovely', time_sig=(4, 4), key_sig=MIm,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source', 'LOVELY.'),
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
                 'La derecha hace ocho corcheas seguidas en casi todos los compases: ninguna es '
                 'difícil, lo difícil es que la última suene igual que la primera.'),
                ('UN SOSTENIDO', 'Mi menor',
                 'Fa sostenido detrás de la clave: la música descansa en Mi, no en Sol, aunque la '
                 'armadura sea la misma que Sol mayor.'),
                ('LA IZQUIERDA', 'Redondas',
                 'Un acorde por compás, aguantado entero. Los dos primeros compases ni siquiera '
                 'toca: la derecha empieza sola.'),
                ('♩ = 115', 'Resistencia',
                 'A 115 las ocho corcheas del compás caen muy seguidas: el problema aquí es aguantar, '
                 'no leer.'),
            ],
            pie='La canción se hizo famosa por la serie "13 Reasons Why". Billie Eilish tenía '
                'dieciséis años al grabarla, escrita con su hermano en el dormitorio de casa.',
        ),
        ritmos=[
            ('MANO DERECHA', 'ocho corcheas seguidas · andamio',
             [n('D5', 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e'),
              n('D5', 'e'), n('G4', 'e'), n('B4', 'e'), n('G4', 'e')], OCRE, 'treble', None),
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
        reto='Que la última corchea suene igual que la primera: no es un problema de notas, es que '
             'la mano se agarrota a los veinte compases y el dibujo empieza a cojear sin notarlo.',
        truco='Toca cuatro compases y para. Suelta la mano del todo, y sigue. Si estudias la pieza '
              'entera de una vez, lo que practicas media pieza es la mano cansada.',
        sabias='El piano de esta pieza no para nunca y la voz sí: ese contraste entre las dos capas '
               'es una de las razones por las que la canción funciona tan bien.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el piano no se detiene en ningún momento mientras la voz sí '
                      'respira entre frases.'),
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
                     dict(cap='a) el dibujo en forma de arco, subiendo y bajando dentro del acorde',
                          events=[n('G4', 'e'), n('B4', 'e'), n('D5', 'e'), n('B4', 'e'),
                                  n('G4', 'e'), n('E4', 'e'), n('G4', 'e'), n('B4', 'e'),
                                  n('A4', 'e'), n('C5', 'e'), n('E5', 'e'), n('C5', 'e'),
                                  n('A4', 'e'), n('F#4', 'e'), n('A4', 'e'), n('C5', 'e')],
                          bars=2, key_sig=MIm),
                     dict(cap='b) y con el acorde cambiando otra vez, un peldaño distinto',
                          events=encajar([n('G3', 'e'), n('B3', 'e'), n('D4', 'e'), n('B3', 'e'),
                                          n('G3', 'e'), n('E4', 'e'), n('G3', 'e'), n('B3', 'e'),
                                          n('F#3', 'e'), n('A3', 'e'), n('D4', 'e'), n('A3', 'e'),
                                          n('F#3', 'e'), n('B3', 'e'), n('F#3', 'e'), n('A3', 'e')], 'treble'),
                          bars=2, key_sig=MIm, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: un acorde y aguantar', clef='bass',
                 pista='la FORMA es literal (una redonda por compás); las notas, andamio en Mi menor',
                 sistemas=[
                     dict(cap='a) cae y se queda · comprueba en el cuarto golpe que sigue sonando',
                          events=[ac(('G2', 'D3', 'G3'), 'w'), ac(('F#2', 'C3', 'F#3'), 'w')],
                          bars=2, clef='bass', key_sig=MIm),
                     dict(cap='b) y con otros dos acordes de la pieza, distintos de los de la clase',
                          events=[ac(('A1', 'E2', 'A2'), 'w'), ac(('D2', 'A2', 'D3'), 'w')],
                          bars=2, clef='bass', key_sig=MIm, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ CUATRO COMPASES Y PARAR',
                 texto='La mano se cansa antes de que lo notes, y cuando lo notas ya llevas un rato '
                       'tocando desigual. Lo que se aprende tocando cansado es a tocar cansado: por '
                       'eso el descanso forma parte del ejercicio, no es una pausa fuera de él.'),
            dict(num=3, titulo='La escala de Mi menor, para no perder el sostenido',
                 pista='andamio en Mi menor · un sostenido, el Fa, y vale para toda la pieza',
                 sistemas=[
                     dict(cap='a) los siete grados desde Mi · el segundo es Fa sostenido, tecla '
                              'negra, y va sin dudar',
                          events=escala('Mi menor', 'E4'), bars=2),
                     dict(cap='b) y de vuelta · si el Fa te sale natural aquí, es que lo estabas '
                              'tocando de memoria y no leyendo',
                          events=escala('Mi menor', 'E5', sentido='baja'),
                          bars=2, show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, con la izquierda debajo',
                 pista='andamio en Mi menor · empieza a la mitad de 115 y no subas esta semana',
                 sistemas=[
                     dict(cap='a) el acorde entra en el uno y no se mueve más',
                          events=[ac(('G2', 'G4'), 'e'), n('B4', 'e'), n('D5', 'e'), n('B4', 'e'),
                                  n('G4', 'e'), n('E4', 'e'), n('G4', 'e'), n('B4', 'e'),
                                  ac(('F#2', 'F#4'), 'e'), n('A4', 'e'), n('C5', 'e'), n('A4', 'e'),
                                  n('F#4', 'e'), n('B4', 'e'), n('F#4', 'e'), n('A4', 'e')],
                          bars=2, key_sig=MIm),
                     dict(cap='b) y con el acorde de la izquierda cambiando cada compás',
                          events=[ac(('A1', 'A3'), 'e'), n('E4', 'e'), n('A4', 'e'), n('E4', 'e'),
                                  n('A3', 'e'), n('E4', 'e'), n('A3', 'e'), n('E4', 'e'),
                                  ac(('D2', 'D4'), 'e'), n('A4', 'e'), n('D5', 'e'), n('A4', 'e'),
                                  n('D4', 'e'), n('A4', 'e'), n('D4', 'e'), n('A4', 'e')],
                          bars=2, key_sig=MIm, show_time=False),
                 ]),
            dict(num=5, titulo='Los acordes que aguantan debajo',
                 pista='andamio en Mi menor · lo que hace la izquierda toda la canción, en cuatro '
                       'acordes',
                 sistemas=[
                     dict(cap='a) i - iv - v - i, una redonda cada uno · el brazo cae una vez y '
                              'se queda, que es justo lo que pide la pieza',
                          events=cadencia('Mi menor', 'E2'), bars=4, clef='bass'),
                 ]),
            dict(num=6, titulo='El acorde de Mi menor y el giro',
                 pista='andamio en Mi menor · la mano quieta y los dedos sueltos',
                 sistemas=[
                     dict(cap='a) el acorde desplegado, sube y baja',
                          events=arpegio('Mi menor', 'E4'), bars=2),
                     dict(cap='b) y el giro alrededor del Si · las cuatro notas del mismo peso, '
                              'que es el reto entero de esta pieza',
                          events=giro('Mi menor', 'B4'), bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
