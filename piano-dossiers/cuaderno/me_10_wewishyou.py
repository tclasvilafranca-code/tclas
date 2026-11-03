# -*- coding: utf-8 -*-
"""We Wish You a Merry Christmas — pieza 10 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("We Wish You a Merry
   Christmas — more words on next page", arr. Gilbert DeBenedetti, 2 páginas),
   leído a 230 dpi:

     - Detrás de la clave hay UN SOSTENIDO: Sol mayor.
     - 3/4.
     - **ANACRUSA de un solo tiempo**: la primera palabra ("We") se canta con
       una sola negra antes de que empiece el primer compás completo.
     - Encima del pentagrama hay letras de acorde impresas: G, C, A7, D.
     - La izquierda toca acordes (dobles notas) siguiendo esas letras.
     - Trae dedos escritos (1, 3, 4, 2).

   Es la primera pieza de Mercè con letras de acorde de verdad impresas en la
   partitura, y con una anacrusa clara de un solo tiempo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra, encajar
from me_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=10, nivel='intermedio', slug='WeWishYou',
    formato='adulto',
    titulo_corto='We Wish You a Merry Christmas', time_sig=(3, 4), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source',
                           'WE WISH YOU A MERRY CHRISTMAS.pdf'),
    yt='https://www.youtube.com/results?search_query=we+wish+you+a+merry+christmas+easy+piano',

    ficha=dict(
        titulo='We Wish You a Merry Christmas',
        autor='Tradicional inglesa · arr. Gilbert DeBenedetti · con letras de acorde',
        datos=[('Tonalidad', 'Sol mayor'), ('Armadura', 'Un sostenido'),
               ('Compás', '3/4'), ('Empieza', 'Antes del compás'),
               ('Trae', 'Letras de acorde')],
        titulo_ritmos='Letras de acorde encima de la melodía',
        pie_ritmos='MEDIDO en tu partitura a 300 puntos por pulgada, y comprobado contra la letra '
                   'impresa debajo: cada sílaba tiene su nota. Arriba, la anacrusa y los dos '
                   'primeros compases. Abajo, andamio en Sol mayor sobre las letras de acorde.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('LETRAS DE ACORDE', 'G, C, A7, D',
                 'Están impresas encima del pentagrama y te dicen qué notas suenan debajo, aunque '
                 'la mano izquierda solo toque dos de ellas a la vez.'),
                ('EMPIEZA ANTES', 'Un tiempo antes',
                 'La primera palabra se canta con una sola negra antes de que arranque el compás de '
                 'verdad, como cuando una frase empieza con "y…".'),
                ('UN SOSTENIDO FIJO', 'Todos los Fa',
                 'Está en la armadura, así que vale para toda la pieza y no hace falta acordarse '
                 'compás a compás.'),
                ('DEDOS ESCRITOS', 'En cada cambio',
                 'Aparecen justo donde la mano tiene que reorganizarse para el siguiente acorde.'),
            ],
            pie='Es un villancico inglés tradicional, del tipo que se canta de puerta en puerta '
                'pidiendo un "pudin de Navidad" a cambio de la canción.',
        ),
        ritmos=[
            ('MANO DERECHA', 'los cc. 1 y 2 · MEDIDO · antes va la anacrusa',
             [n('G4')] + corch(['G4', 'A4']) + corch(['G4', 'F#4'])
             + [n('E4'), n('E4'), n('E4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio sobre las letras de acorde impresas',
             [ac(('E2', 'G2'), 'h.'), ac(('F2', 'A2'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa son teclas negras.',
            'La tonalidad es Sol mayor.',
            'Compás de 3/4.',
            'La pieza empieza con una sola negra antes del primer compás completo.',
            'Encima del pentagrama hay letras de acorde impresas: G, C, A7, D.',
            'Los dedos vienen escritos en cada cambio de acorde.',
        ],
        reto='Que la anacrusa no se cuente como si fuera un compás entero. Es solo un tiempo, y el '
             'compás de verdad empieza justo después.',
        truco='Cuenta "tres" en voz alta antes de tocar la primera nota, como si ya estuvieras a '
              'mitad de compás, y entra justo en el "y" siguiente. Repítelo hasta que la entrada '
              'salga siempre igual de corta.',
        sabias='Cantar de puerta en puerta a cambio de comida y bebida era una tradición inglesa '
               'llamada "wassailing", mucho más antigua que la propia canción, que se hizo popular '
               'en el siglo XIX.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo la primera palabra y fíjate en que suena antes de que entre el '
                      'acompañamiento de verdad. Ese adelanto es la anacrusa.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas: la anacrusa y las letras de acorde. Cada una se aprende por '
              'separado antes de tocar la pieza entera.',
        reglas=['LA ANACRUSA DURA UN SOLO TIEMPO', 'EL FA SIEMPRE ES SOSTENIDO',
                'LAS LETRAS DICEN QUÉ TOCA LA IZQUIERDA'],
        bloques=[
            dict(num=1, titulo='Entrar con la anacrusa',
                 pista='andamio en Sol mayor · en tu partitura el primer compás está incompleto',
                 sistemas=[
                     dict(cap='a) dos tiempos callados y entras en el tercero',
                          events=[sil('h'), n('D4'), n('G4'), n('A4'), n('B4'), n('C5', 'h.')],
                          bars=3),
                     dict(cap='b) lo mismo empezando más abajo',
                          events=encajar([sil('h'), n('G3'), n('D4'), n('E4'), n('F#4'), n('G4', 'h.')], 'treble'),
                          bars=3, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: los acordes de las letras',
                 pista='andamio · cada letra es una combinación fija de dos notas',
                 sistemas=[
                     dict(cap='a) G y C, sostenidos el compás entero',
                          events=[ac(('G2', 'B2'), 'h.'), ac(('C3', 'E3'), 'h.')],
                          bars=2, clef='bass'),
                     dict(cap='b) A7 y D, con el sostenido de la armadura',
                          events=[ac(('A2', 'C#3'), 'h.'), ac(('D3', 'F#3'), 'h.')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='PARA QUÉ SIRVEN LAS LETRAS DE ACORDE',
                 texto='Una letra como "G" no es un adorno: te dice que en ese compás la izquierda '
                       'toca notas del acorde de Sol. Aunque tu mano solo pulse dos de esas notas, '
                       'saber el nombre del acorde ayuda a anticipar el sonido antes de tocarlo, y '
                       'es la misma letra que usarías si algún día acompañas a alguien de oído.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la anacrusa va sola, y luego las dos manos entran juntas',
                 sistemas=[
                     dict(cap='a) la melodía entra sola y la izquierda se une después',
                          events=[sil('h'), n('D4'), ac(('G2', 'B2')), n('G4'), n('A4'),
                                  ac(('C3', 'E3', 'B4'), 'h.')],
                          bars=3),
                     dict(cap='b) y con el cambio a A7 y D',
                          events=[sil('h'), n('G3'), ac(('A2', 'C#3')), n('D4'), n('E4'),
                                  ac(('D3', 'F#3', 'F#4'), 'h.')],
                          bars=3, show_time=False),
                 ]),
        ] + bloques_extra('Sol mayor', 12, 'G3', 'G2',
                          'el Fa es negro también cuando la melodía corre',
                          desde=4, time_sig=(3, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
