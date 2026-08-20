# -*- coding: utf-8 -*-
"""Greensleeves — pieza 15 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Greensleeves —
   Traditional English folk song", 2 páginas), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: La menor. Los sostenidos que necesita la
       pieza van escritos delante de la nota.
     - 3/4, "Moderato" y "mp". No trae número de metrónomo.
     - **ANACRUSA de verdad**: el primer compás tiene una sola negra en la
       derecha, y la izquierda un silencio de negra. No es un compás entero
       relleno de silencios como en Vivaldi: está incompleto.
     - La izquierda hace TRES NEGRAS por compás, subiendo.
     - Trae LETRAS DE ACORDE impresas (Am, G…) y digitación (1, 2).

   Lo nuevo: entrar antes del primer compás, y una izquierda que se mueve en
   los tres tiempos en vez de aguantar.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra
from lu_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=15, nivel='iniciación', slug='Greensleeves',
    formato='adulto',
    titulo_corto='Greensleeves', time_sig=(3, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'Copia de 1-----Greensleeves.pdf'),
    yt='https://www.youtube.com/results?search_query=greensleeves+easy+piano',

    ficha=dict(
        titulo='Greensleeves',
        autor='Tradicional inglesa · siglo XVI · con cifrado y digitación',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Carácter', 'Moderato'), ('Empieza', 'Antes del compás'),
               ('Izquierda', 'Tres negras')],
        titulo_ritmos='La izquierda ya no espera',
        pie_ritmos='Andamio en La menor. Lo literal es el reparto: la izquierda hace tres negras '
                   'por compás y la melodía entra antes del primer compás.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('EMPIEZA ANTES', 'Anacrusa',
                 'El primer compás no está entero: tiene una sola nota. La melodía entra antes de '
                 'que empiece el compás de verdad, como cuando una frase arranca con "y…".'),
                ('TRES NEGRAS ABAJO', 'Una en cada tiempo',
                 'Es la primera vez que la izquierda se mueve en los tres tiempos. Hasta ahora '
                 'aguantaba o hacía dos notas.'),
                ('LETRAS DE ACORDE', 'Am, G…',
                 'Encima del pentagrama hay letras. Am quiere decir La menor y G quiere decir Sol. '
                 'Son las notas que la izquierda está tocando de una en una.'),
                ('SIN ARMADURA', 'Y con sostenidos',
                 'Detrás de la clave no hay nada, pero dentro sí hay teclas negras escritas delante '
                 'de la nota. Valen para su compás.'),
            ],
            pie='Es una melodía de hace más de cuatrocientos años y sigue sonando moderna. Va lenta, '
                'así que lo que se oye es cada nota: no hay donde esconderse.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la primera frase, ya dentro del compás · andamio',
             [n('C5'), n('D5'), n('E5')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'tres negras por compás, subiendo · literal',
             [n('A2'), n('E3'), n('A3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero hay sostenidos escritos dentro de la pieza.',
            'La tonalidad es La menor.',
            'Compás de 3/4, "Moderato" y "mp".',
            'La melodía entra antes del primer compás: una sola negra.',
            'La izquierda hace tres negras por compás.',
            'Encima del pentagrama hay letras de acorde: Am, G…',
        ],
        reto='La izquierda. Tres notas por compás, siempre iguales de largas y siempre igual de '
             'suaves. Si la tercera se acelera, la melodía pierde el suelo.',
        truco='Toca la izquierda sola contando "un, dos, tres" y grábate con el móvil. Escúchalo: lo '
              'que vas a oír es que la tercera nota llega antes de tiempo. Repítelo hasta que las '
              'tres suenen igual de separadas.',
        sabias='Se imprimió por primera vez en 1580. La leyenda de que la escribió Enrique VIII para '
               'Ana Bolena es falsa: el estilo es italiano y llegó a Inglaterra después de su '
               'muerte.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo el acompañamiento. Vas a oír tres notas por compás, iguales y '
                      'sin prisa. Eso es lo que tienes que copiar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Entrar antes del compás, y una izquierda que se mueve todo el rato.',
        reglas=['LA MELODÍA ENTRA ANTES DEL COMPÁS', 'TRES NEGRAS IGUALES, SIN ACELERAR',
                'MODERATO: NI DEPRISA NI ARRASTRANDO'],
        bloques=[
            dict(num=1, titulo='La izquierda: tres negras por compás',
                 pista='andamio en La menor · el reparto de figuras es el de tu partitura',
                 sistemas=[
                     dict(cap='a) tres notas iguales, subiendo · que las tres duren lo mismo',
                          events=[n('A2'), n('E3'), n('A3'), n('G2'), n('D3'), n('G3')],
                          matiz='mp',
                          acento=True,
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde cada compás · el salto va entre compases',
                          events=[n('F2'), n('C3'), n('F3'), n('E2'), n('B2'), n('E3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Entrar antes del compás',
                 pista='andamio · el primer compás está incompleto, y así es en tu partitura',
                 sistemas=[
                     dict(cap='a) los silencios de aquí sirven para contar la espera · en tu '
                              'partitura el compás está incompleto',
                          events=[sil('h'), n('A4'), n('C5'), n('D5'), n('E5')],
                          bars=2),
                     dict(cap='b) y la frase que baja · la nota de antes del compás nunca lleva '
                              'acento, lo lleva la de después',
                          events=[sil('h'), n('E5'), n('D5'), n('C5'), n('B4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UNA ANACRUSA',
                 texto='Una nota que suena antes de que empiece el primer compás completo. En '
                       'Vivaldi el compás estaba entero y relleno de silencios; aquí está de verdad '
                       'incompleto. Esa nota suena más floja que la siguiente: es impulso.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda no para de moverse · muy despacio',
                 sistemas=[
                     dict(cap='a) la melodía encima de las tres negras · las dos coinciden en el uno',
                          events=[ac(('A2', 'C5')), n('E3'), n('A3'),
                                  ac(('G2', 'D5')), n('D3'), n('G3')],
                          bars=2),
                     dict(cap='b) y con la melodía aguantando mientras la izquierda sigue andando',
                          events=[ac(('F2', 'E5')), n('C3'), n('F3'),
                                  ac(('E2', 'D5')), n('B2'), n('E3')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('La menor', 'A3', 'A2', time_sig=(3, 4), variante=50,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
