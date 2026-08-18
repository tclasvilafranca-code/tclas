# -*- coding: utf-8 -*-
"""Silent Night, a cuatro manos — pieza 11 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Silent Night — 4
   hands", Piano 1 + Piano 2, 1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 3/4.
     - Tu parte es el Piano 1: la melodía en negra con puntillo y corchea, y
       la izquierda en BLANCAS CON PUNTILLO, una por compás.
     - El Piano 2 (la profesora) hace silencios en la derecha y lleva el bajo
       con notas más largas.

   Es la segunda versión de Silent Night de tu carpeta, y aquí lo nuevo no es
   el ritmo —muy parecido al de la otra— sino que se toca de verdad a dos,
   cada parte con su papel bien diferenciado.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=11, nivel='intermedio', slug='SilentNight4Hands',
    formato='adulto',
    titulo_corto='Silent Night · a cuatro manos', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'silent-night-4-hands.'),
    yt='https://www.youtube.com/results?search_query=silent+night+piano+duet+4+hands',

    ficha=dict(
        titulo='Silent Night · a cuatro manos',
        autor='Franz Xaver Gruber · versión a cuatro manos, Piano 1 + Piano 2',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Izquierda', 'Blanca con puntillo'), ('Derecha', 'Largo-corto'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Una nota que dura el compás entero',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda toca una sola nota '
                   'por compás y la aguanta entera, y la derecha lleva el ritmo largo-corto.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('OTRA VEZ SILENT NIGHT', 'Pero a dos',
                 'El ritmo de la melodía es parecido al de la otra versión de tu carpeta; lo que '
                 'cambia de verdad es que ahora se toca con otra persona, cada uno con su papel.'),
                ('TU PARTE ES EL PIANO 1', 'La melodía',
                 'Llevas la voz principal. El Piano 2, que toca la profesora, sostiene por debajo '
                 'con notas más largas.'),
                ('UNA BLANCA CON PUNTILLO', 'El compás entero',
                 'Tu izquierda toca una sola vez por compás y no vuelve a tocar hasta el siguiente: '
                 'una nota, tres tiempos completos.'),
                ('ESCUCHAR AL OTRO', 'Parte del ejercicio',
                 'En un dueto, entrar a tiempo depende tanto de contar como de escuchar lo que hace '
                 'la otra parte.'),
            ],
            pie='Es la misma melodía que ya conoces de la otra versión, pero pensada para sonar '
                'junto a otro instrumento, no sola.',
        ),
        ritmos=[
            ('MANO DERECHA', 'largo, corto y una negra · literal',
             [n('D4', 'q.'), n('E4', 'e'), n('D4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una blanca con puntillo, el compás entero · literal',
             [n('C3', 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 3/4.',
            'Tu parte es el Piano 1, con la melodía.',
            'La izquierda toca una blanca con puntillo por compás y la sostiene entera.',
            'La derecha hace el ritmo largo-corto seguido de una negra.',
            'La otra parte, el Piano 2, lleva el bajo y la toca la profesora.',
        ],
        reto='Aguantar la nota de la izquierda el compás entero mientras escuchas al Piano 2. En un '
             'dueto no basta con contar bien: hay que encajar con lo que suena al lado.',
        truco='Practica primero contando en voz alta con un metrónomo suave, y solo cuando la '
              'izquierda aguante sin acortarse, añade la idea de tocar "con alguien", aunque sea '
              'imaginando la otra parte.',
        sabias='Las versiones a cuatro manos de villancicos son muy antiguas: en el siglo XIX era '
               'habitual que las familias con piano en casa tocaran juntas estas piezas en Navidad, '
               'antes de que existiera la radio.',
        qr=dict(titulo='Escúchala',
                texto='Escucha una grabación a dos pianos y fíjate en qué parte suena más grave: '
                      'esa es la que hace el papel de tu Piano 2.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El ritmo ya lo conoces de la otra versión; lo nuevo es sostener la nota entera '
              'pensando en una segunda parte que no está escrita en tu papel.',
        reglas=['LA IZQUIERDA AGUANTA EL COMPÁS ENTERO', 'CUENTA CON UN METRÓNOMO SUAVE',
                'ESCUCHA LA OTRA PARTE MIENTRAS TOCAS'],
        bloques=[
            dict(num=1, titulo='La izquierda: una nota, tres tiempos',
                 pista='andamio en Do mayor · el reparto es el de tu partitura',
                 sistemas=[
                     dict(cap='a) toca en el uno y no sueltes hasta el compás siguiente',
                          events=[n('C3', 'h.'), n('F2', 'h.')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de nota, con la misma sujeción',
                          events=[n('G2', 'h.'), n('C3', 'h.')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: largo-corto y una negra',
                 pista='andamio · el mismo dibujo de la otra versión, aplicado aquí',
                 sistemas=[
                     dict(cap='a) larga, corta y una negra que cierra el compás',
                          events=[n('D4', 'q.'), n('E4', 'e'), n('D4'), n('C4', 'h.')],
                          bars=2),
                     dict(cap='b) y la frase que sigue, un poco más arriba',
                          events=[n('F4', 'q.'), n('G4', 'e'), n('F4'), n('E4', 'h.')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ CAMBIA DE TOCAR SOLA A TOCAR CON ALGUIEN',
                 texto='Cuando se toca sola, una nota larga se sostiene por su propia cuenta interna. '
                       'En un dueto, esa misma nota tiene que encajar con lo que está pasando en la '
                       'otra parte, aunque no la veas escrita. Escuchar mientras se sostiene la '
                       'blanca con puntillo, en vez de limitarse a contar, es lo que hace que las dos '
                       'partes suenen como una sola pieza.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda no se mueve mientras la derecha respira · despacio',
                 sistemas=[
                     dict(cap='a) la blanca con puntillo sostiene toda la frase de la derecha',
                          events=[ac(('C3', 'D4'), 'q.'), n('E4', 'e'), n('D4'),
                                  ac(('F2', 'C4'), 'h.')],
                          bars=2),
                     dict(cap='b) y con la frase que sube',
                          events=[ac(('G2', 'F4'), 'q.'), n('G4', 'e'), n('F4'),
                                  ac(('C3', 'E4'), 'h.')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
