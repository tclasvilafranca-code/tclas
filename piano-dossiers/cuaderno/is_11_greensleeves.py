# -*- coding: utf-8 -*-
"""Greensleeves — pieza 11 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Greensleeves —
   Traditional English folk song", 2 páginas; el mismo archivo que la pieza
   16 de Mercè y la 15 de Luisa, byte a byte):

     - Detrás de la clave NO HAY NADA: La menor, con sostenidos escritos
       delante de la nota.
     - 3/4, "Moderato" y "mp".
     - ANACRUSA de verdad: el primer compás tiene una sola negra en la
       derecha y está incompleto.
     - La izquierda hace tres negras por compás, subiendo.
     - Trae letras de acorde (Am, G…) y digitación.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from is_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
LAm = 'La menor'

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=11, nivel='intermedio', slug='Greensleeves',
    formato='adulto',
    titulo_corto='Greensleeves', time_sig=(3, 4), key_sig=LAm,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', '-Greensleeves.'),
    yt='https://www.youtube.com/results?search_query=greensleeves+piano+intermediate',

    ficha=dict(
        titulo='Greensleeves',
        autor='Tradicional inglesa · siglo XVI · con cifrado y digitación',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Carácter', 'Moderato'), ('Empieza', 'Antes del compás'),
               ('Izquierda', 'Tres negras')],
        titulo_ritmos='La izquierda no espera',
        pie_ritmos='Andamio en La menor. Lo literal es el reparto: la izquierda hace tres negras '
                   'por compás y la melodía entra antes del primer compás.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('EMPIEZA ANTES', 'Anacrusa',
                 'El primer compás no está entero: tiene una sola nota. La melodía entra antes de '
                 'que empiece el compás de verdad.'),
                ('TRES NEGRAS ABAJO', 'Una en cada tiempo',
                 'La izquierda se mueve en los tres tiempos del compás. No aguanta ni sostiene: '
                 'camina todo el rato.'),
                ('LETRAS DE ACORDE', 'Am, G…',
                 'Encima del pentagrama hay letras que nombran lo que está tocando la izquierda.'),
                ('SIN ARMADURA', 'Sostenidos sueltos',
                 'Detrás de la clave no hay nada, pero dentro de la pieza hay teclas negras '
                 'escritas delante de la nota.'),
            ],
            pie='Es una melodía de más de cuatrocientos años que sigue sonando actual. Al ir '
                'despacio, se oye cada nota: no hay donde esconder un error.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la frase, ya dentro del compás · andamio',
             [n('C5'), n('D5'), n('E5')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'tres negras por compás, subiendo · literal',
             [n('A2'), n('E3'), n('A3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero hay sostenidos escritos dentro de la pieza.',
            'La tonalidad es La menor.',
            'Compás de 3/4, "Moderato" y "mp".',
            'La melodía entra antes del primer compás: una sola negra.',
            'La izquierda hace tres negras por compás, sin pararse.',
            'Encima del pentagrama hay letras de acorde: Am, G…',
        ],
        reto='La izquierda. Tres notas por compás, siempre iguales de largas y suaves.',
        truco='Toca la izquierda sola contando "un, dos, tres" y grábate con el móvil: lo normal es '
              'que la tercera nota llegue antes de tiempo.',
        sabias='Se imprimió por primera vez en 1580. La leyenda de que la escribió Enrique VIII para '
               'Ana Bolena es falsa: el estilo musical es italiano.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo el acompañamiento: tres notas por compás, iguales y sin prisa.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos novedades: entrar antes del compás, y una izquierda que camina en vez de '
              'sostener.',
        reglas=['LA MELODÍA ENTRA ANTES DEL COMPÁS', 'TRES NEGRAS IGUALES, SIN ACELERAR',
                'MODERATO: NI DEPRISA NI ARRASTRANDO'],
        bloques=[
            dict(num=1, titulo='La izquierda: tres negras por compás',
                 pista='andamio en La menor · otro dibujo de figuras',
                 sistemas=[
                     dict(cap='a) tres notas iguales, bajando esta vez',
                          events=[n('A3'), n('E3'), n('A2'), n('G3'), n('D3'), n('G2')],
                          matiz='mp',
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde cada compás',
                          events=[n('F3'), n('C3'), n('F2'), n('E3'), n('B2'), n('E2')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Entrar antes del compás',
                 pista='andamio · los silencios están puestos para contar la espera; en tu '
                       'partitura el compás está incompleto',
                 sistemas=[
                     dict(cap='a) una sola nota y ya empieza el compás de verdad, subiendo distinto',
                          events=[sil('h'), n('E4'), n('G4'), n('A4'), n('B4')],
                          bars=2),
                     dict(cap='b) y la frase que baja después',
                          events=[sil('h'), n('B4'), n('A4'), n('G4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UNA ANACRUSA',
                 texto='Una nota que suena antes de que empiece el primer compás completo. Suena '
                       'siempre más floja que la que viene después: es impulso, no golpe.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda no para de caminar · muy despacio',
                 sistemas=[
                     dict(cap='a) la melodía encima de las tres negras, con otro dibujo',
                          events=[ac(('A3', 'E4')), n('E3'), n('A2'),
                                  ac(('G3', 'G4')), n('D3'), n('G2')],
                          bars=2),
                     dict(cap='b) y con la melodía aguantando mientras la izquierda sigue',
                          events=[ac(('F3', 'B4')), n('C3'), n('F2'),
                                  ac(('E3', 'A4')), n('B2'), n('E2')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('La menor', 59, 'A3', 'A2',
                          'tres notas por compás, todas iguales de largas',
                          desde=4, time_sig=(3, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
