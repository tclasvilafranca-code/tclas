# -*- coding: utf-8 -*-
"""Puff the Magic Dragon — pieza 5 de Luisa. Formato adulto, iniciación.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Eric Moore,
   1 página):

     - Detrás de la clave no hay nada: Do mayor.
     - 4/4. No imprime tempo.
     - La MANO IZQUIERDA HACE UNA REDONDA DE DOS NOTAS por compás: el mismo
       trabajo que en la pieza 4, pero con dos dedos a la vez.
     - La derecha va en negras, blancas y alguna negra con puntillo seguida de
       corchea.
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
    alumno='Luisa', carpeta='Luisa', num=5, nivel='iniciación', slug='PuffTheMagicDragon',
    formato='adulto',
    titulo_corto='Puff the Magic Dragon', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'puff-the-magic-dragon.'),
    yt='https://www.youtube.com/results?search_query=puff+the+magic+dragon+piano+easy',

    ficha=dict(
        titulo='Puff the Magic Dragon',
        autor='Peter, Paul and Mary · arreglo de Eric Moore',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Izquierda', 'Dos notas'), ('Carácter', 'Sin tempo escrito'),
               ('Páginas', 'Una')],
        titulo_ritmos='Dos dedos abajo, la melodía arriba',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: una redonda de dos notas abajo, '
                   'una por compás, y la melodía arriba.',
        armonia=dict(
            titulo='Lo nuevo: dos dedos a la vez',
            tarjetas=[
                ('DOS NOTAS', 'A la vez',
                 'La izquierda hace lo mismo que la semana pasada, pero con dos dedos en vez de '
                 'uno. Los dos bajan juntos y se quedan los cuatro golpes.'),
                ('SE OYE SI FALLA', 'Un solo golpe',
                 'Si un dedo llega antes que el otro se oye un ruidito de más. Fuerte y corto es '
                 'donde mejor se nota, y por eso se practica así.'),
                ('LA NEGRA CON PUNTO', 'Larga y corta',
                 'En la melodía hay una figura que va larga-corta. El punto al lado de la negra le '
                 'añade la mitad, y la nota pequeña que viene detrás cae muy pegada.'),
                ('SIN TEMPO', 'Lo eliges tú',
                 'La edición no dice a qué velocidad va. Elige una en la que te salga todo y no la '
                 'cambies de un día para otro.'),
            ],
            pie='La canción es de 1963 y todo el mundo la ha oído alguna vez. Aquí lo que se '
                'estudia es la mano izquierda: dos dedos juntos, sonando a la vez.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, larga y corta · andamio',
             [n('E4', 'q.'), n('D4', 'e'), n('E4'), n('G4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas, una redonda por compás · literal',
             [ac(('C3', 'G3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4.',
            'La izquierda hace una redonda de DOS notas en cada compás.',
            'Las dos notas de la izquierda bajan a la vez y se aguantan los cuatro golpes.',
            'En la melodía hay negras con puntillo seguidas de una nota corta.',
            'La edición no dice a qué velocidad tocarla.',
        ],
        reto='Que las dos notas de la izquierda suenen como un solo golpe. Siempre hay un dedo que '
             'llega antes, y casi siempre es el pulgar.',
        truco='Toca las dos notas muy fuerte y muy cortas, como un pellizco, veinte veces seguidas. '
              'Fuerte y corto es donde se oye si un dedo se adelanta. Cuando suene un solo golpe, '
              'bájalo a normal y ya no se separa.',
        sabias='La canción la escribieron dos estudiantes en 1959 a partir de un poema, y se hizo '
               'famosa cuatro años después. Habla de un niño que crece y deja de jugar, aunque casi '
               'todo el mundo la recuerda solo como una canción de dragones.',
        qr=dict(titulo='Escúchala',
                texto='Escucha lo quieto que está el acompañamiento. No se mueve casi nunca: solo '
                      'cambia de acorde y espera.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Otra vez la izquierda primero, y esta semana con dos dedos. El resto ya lo sabes '
              'hacer.',
        reglas=['LOS DOS DEDOS, A LA VEZ', 'FUERTE Y CORTO PARA COMPROBAR',
                'LA REDONDA DURA CUATRO GOLPES'],
        bloques=[
            dict(num=1, titulo='Las dos notas juntas, como un pellizco', clef='bass',
                 pista='andamio en Do mayor · fuerte y corto: así se oye si un dedo se adelanta',
                 sistemas=[
                     dict(cap='a) los dos dedos bajan a la vez · un solo golpe, no dos',
                          events=[ac(('C3', 'G3')), ac(('C3', 'G3')), ac(('C3', 'G3')),
                                  ac(('C3', 'G3')), ac(('A2', 'E3'), 'h'), ac(('A2', 'E3'), 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y ahora como en la pieza: una redonda por compás, aguantada entera',
                          events=[ac(('F2', 'C3'), 'w'), ac(('G2', 'D3'), 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ FUERTE Y CORTO',
                 texto='Tocando flojo y largo, un dedo que se adelanta no se oye: el sonido tapa el '
                       'fallo. Tocando fuerte y corto se oye todo. Por eso se practica al revés de '
                       'como suena la pieza: primero se busca el fallo, y después se toca bonito.'),
            dict(num=2, titulo='La melodía: larga y corta',
                 pista='andamio en Do mayor · la corta va muy pegada a la siguiente',
                 sistemas=[
                     dict(cap='a) cuenta "un-dos-tres-Y" · la nota corta cae en la "y" del tres',
                          events=[n('E4', 'q.'), n('D4', 'e'), n('E4'), n('G4'),
                                  n('A4', 'q.'), n('G4', 'e'), n('E4', 'h')],
                          bars=2),
                     dict(cap='b) y con la misma figura bajando · si la corta se te alarga, la '
                              'frase deja de sonar a canción',
                          events=[n('G4', 'q.'), n('F4', 'e'), n('E4'), n('D4'),
                                  n('E4', 'q.'), n('D4', 'e'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio · muy despacio · la izquierda no se mueve mientras la derecha va',
                 sistemas=[
                     dict(cap='a) las dos notas abajo aguantando, y la melodía por encima',
                          events=[ac(('C3', 'G3', 'E4'), 'q.'), n('D4', 'e'), n('E4'), n('G4'),
                                  ac(('A2', 'E3', 'A4'), 'h'), n('G4'), n('E4')],
                          bars=2),
                     dict(cap='b) y cambiando de acorde abajo · el cambio se prepara mientras suena '
                              'el anterior',
                          events=[ac(('F2', 'C3', 'F4')), n('E4'), n('D4'), n('C4'),
                                  ac(('G2', 'D3', 'D4'), 'h'), n('E4'), n('C4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
