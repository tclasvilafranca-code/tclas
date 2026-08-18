# -*- coding: utf-8 -*-
"""You've Got a Friend in Me — pieza 4 de Luisa. Formato adulto, iniciación.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Megan Harper,
   marcado "Easy", 1 página):

     - Detrás de la clave no hay nada: Do mayor.
     - 4/4. No imprime tempo.
     - La MANO IZQUIERDA HACE UNA REDONDA DE UNA SOLA NOTA por compás. Es lo
       más sencillo que puede hacer una mano izquierda.
     - Aparece un Si bemol escrito delante de la nota en el c. 2, no en la
       armadura.
     - La derecha va en negras y corcheas, con alguna redonda.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from lu_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=4, nivel='iniciación', slug='FriendInMe',
    formato='adulto',
    titulo_corto="You've Got a Friend in Me", time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'youve-got-a-friend-in-me-easy-piano-.pdf'),
    yt='https://www.youtube.com/results?search_query=youve+got+a+friend+in+me+piano+easy',

    ficha=dict(
        titulo="You've Got a Friend in Me",
        autor='Randy Newman · de Toy Story · arreglo de Megan Harper',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Izquierda', 'Una redonda'), ('Carácter', 'Sin tempo escrito'),
               ('Páginas', 'Una')],
        titulo_ritmos='Cómo se reparten las dos manos',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: una sola nota larga abajo y la '
                   'melodía arriba. Las notas exactas están en tu partitura.',
        armonia=dict(
            titulo='La primera con cada mano haciendo algo distinto',
            tarjetas=[
                ('LA IZQUIERDA', 'Una nota',
                 'Una sola nota por compás, y aguantarla los cuatro golpes. Nada más. Es lo más '
                 'fácil que va a hacer tu mano izquierda en todo el curso.'),
                ('LA DERECHA', 'La melodía',
                 'Arriba va la canción. Ahí sí hay que moverse, pero abajo no pasa nada.'),
                ('YA NO IGUAL', 'Cada una lo suyo',
                 'Las tres primeras piezas las dos manos hacían lo mismo. Esta es la primera en la '
                 'que no, y por eso la izquierda es tan sencilla.'),
                ('UN SI BEMOL', 'Escrito',
                 'En el segundo compás hay un signo delante de una nota: ese Si se toca en la tecla '
                 'negra, y solo en ese compás.'),
            ],
            pie='El salto de verdad de esta semana no son las notas: es que cada mano hace una cosa '
                'distinta. Por eso la de abajo hace lo mínimo, para que puedas mirar solo la de '
                'arriba.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía · andamio',
             [n('C4'), n('E4'), n('D4'), n('E4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda, y aguantar · literal',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4.',
            'La mano izquierda hace UNA redonda de UNA nota en cada compás.',
            'Una redonda dura los cuatro golpes del compás.',
            'En el compás 2 hay un Si bemol escrito delante de la nota.',
            'La edición no dice a qué velocidad hay que tocarla.',
        ],
        reto='Que la nota de la izquierda siga sonando cuando llegas al cuarto golpe. Lo normal al '
             'empezar es soltarla sin darse cuenta en cuanto la derecha se mueve.',
        truco='Toca la nota de la izquierda y cuenta los cuatro golpes en voz alta mirando el dedo. '
              'Si en el "cuatro" la tecla sigue abajo, está bien. Hazlo cinco veces antes de poner '
              'la derecha encima.',
        sabias='Randy Newman escribió esta canción para la primera película de Toy Story, en 1995, '
               'y la canta él mismo. Ha compuesto la música de casi todas las de Pixar.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en el piano de abajo: casi no se mueve. Eso es exactamente lo que va '
                      'a hacer tu mano izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda primero, aunque parezca que no hay nada que estudiar. Es justo lo que '
              'hay que estudiar.',
        reglas=['LA REDONDA DURA CUATRO GOLPES', 'LA IZQUIERDA, SIN MIRARLA',
                'Y SOLO AL FINAL, LAS DOS'],
        bloques=[
            dict(num=1, titulo='La izquierda: poner el dedo y no soltarlo', clef='bass',
                 pista='andamio en Do mayor · la forma es la de tu partitura',
                 sistemas=[
                     dict(cap='a) una redonda por compás · cuenta los cuatro golpes y mira si en el '
                              'cuarto la tecla sigue abajo',
                          events=[n('C3', 'w'), n('A2', 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de nota · el dedo nuevo se prepara mientras suena la '
                              'anterior, no cuando le toca',
                          events=[n('F2', 'w'), n('G2', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UNA REDONDA',
                 texto='Es la nota más larga que vas a ver: dura los cuatro golpes del compás. Se '
                       'dibuja como un óvalo vacío, sin palito. Cuando la veas, baja la tecla y '
                       'cuenta hasta cuatro antes de soltarla.'),
            dict(num=2, titulo='La derecha, con la melodía',
                 pista='andamio en Do mayor · negras, y alguna nota larga',
                 sistemas=[
                     dict(cap='a) la melodía, con notas seguidas · sin correr',
                          events=[n('C4'), n('D4'), n('E4'), n('F4'), n('E4'), n('D4'), n('C4', 'h')],
                          bars=2),
                     dict(cap='b) y con la nota larga del final de la frase · aguántala entera',
                          events=[n('E4'), n('F4'), n('G4'), n('E4'), n('C4', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos, dos compases',
                 pista='andamio · muy despacio · si la izquierda se levanta, vuelve al paso 1',
                 sistemas=[
                     dict(cap='a) la nota larga abajo y la melodía arriba, por encima',
                          events=[ac(('C3', 'C4')), n('D4'), n('E4'), n('F4'),
                                  ac(('A2', 'E4')), n('D4'), n('C4', 'h')],
                          bars=2),
                     dict(cap='b) y con el Si bemol del compás 2 · el signo vale solo para ese '
                              'compás, no para toda la pieza',
                          events=[ac(('F2', 'A4')), n('Bb4'), n('A4'), n('G4'),
                                  ac(('G2', 'E4')), n('D4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
