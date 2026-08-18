# -*- coding: utf-8 -*-
"""Bela Ciao (La Casa de Papel) — pieza 13 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive (1 página, Musescore),
   leído a 230 dpi:

     - Detrás de la clave hay UN SOSTENIDO: Mi menor.
     - **2/4**, con barra de repetición al principio.
     - La derecha empieza con SILENCIO DE CORCHEA y sigue con corcheas: media
       parte callada y entra en el medio del primer tiempo.
     - El primer compás de la izquierda está callado entero; a partir del
       segundo hace dos negras por compás.

   Es la primera pieza en tono menor del cuaderno de Luisa, y el primer
   silencio que no ocupa un tiempo entero.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from lu_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=13, nivel='iniciación', slug='BelaCiao',
    formato='adulto',
    titulo_corto='Bela Ciao', time_sig=(2, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'bela-ciao.easy'),
    yt='https://www.youtube.com/results?search_query=bella+ciao+easy+piano+la+casa+de+papel',

    ficha=dict(
        titulo='Bela Ciao',
        autor='Canción popular italiana · conocida por La Casa de Papel',
        datos=[('Tonalidad', 'Mi menor'), ('Armadura', 'Un sostenido'),
               ('Compás', '2/4'), ('Empieza', 'Media parte tarde'),
               ('Izquierda', 'Dos negras')],
        titulo_ritmos='Un sostenido para toda la pieza',
        pie_ritmos='Andamio en Mi menor. Lo literal es el arranque: silencio de corchea y corcheas '
                   'seguidas. Las notas exactas están en tu partitura.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('LA PRIMERA EN MENOR', 'Mi menor',
                 'Suena más seria que las anteriores, y no es cosa de tocarla más triste: es que '
                 'las notas son otras. Con un sostenido en la armadura, todos los Fa son negros.'),
                ('UN SOSTENIDO FIJO', 'Al lado de la clave',
                 'Está escrito al principio de cada línea, así que vale para toda la pieza. No hay '
                 'que acordarse compás a compás: se acuerda la mano.'),
                ('MEDIA PARTE CALLADA', 'Silencio de corchea',
                 'La melodía no entra en el golpe: entra justo después. Es el primer silencio de tu '
                 'cuaderno que dura menos de un tiempo entero.'),
                ('DOS NEGRAS ABAJO', 'Una por tiempo',
                 'En compás de dos, eso es una nota en cada tiempo. Sencillo de contar, y es lo que '
                 'sostiene toda la pieza.'),
            ],
            pie='El primer compás de la izquierda está callado entero, así que la melodía arranca '
                'sola. Entra a partir del segundo y ya no para.',
        ),
        ritmos=[
            ('MANO DERECHA', 'silencio de corchea y corcheas · literal',
             [sil('e')] + corch(['E4', 'A4']) + [n('B4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos negras por compás · literal',
             [n('E3'), n('B3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa son teclas negras.',
            'La tonalidad es Mi menor.',
            'Compás de 2/4: dos tiempos por compás.',
            'La melodía entra media parte tarde, después de un silencio de corchea.',
            'El primer compás de la izquierda está callado entero.',
            'A partir del segundo compás la izquierda hace dos negras.',
        ],
        reto='Entrar media parte tarde. No es esperar un tiempo entero, es esperar la mitad, y al '
             'principio la mano siempre se adelanta.',
        truco='Cuenta "un-y, dos-y" en voz alta y toca solo en las "y". Cuando eso salga, toca la '
              'primera nota en la "y" del uno y sigue con la melodía. La palabra "y" es el sitio '
              'exacto donde entra.',
        sabias='La cantaban las trabajadoras de los arrozales del norte de Italia mucho antes de la '
               'guerra, con otra letra: hablaba de mosquitos y de jornadas de doce horas. La letra '
               'partisana llegó después.',
        qr=dict(titulo='Escúchala',
                texto='Da palmas en el "un, dos" y fíjate en que la voz nunca entra con la palmada, '
                      'sino justo después. Ese retraso es la pieza entera.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas y las dos pequeñas: un sostenido que vale siempre, y una entrada '
              'media parte tarde. Un paso para cada una, y el tercero para juntarlas.',
        reglas=['TODOS LOS FA SON NEGROS', 'CUENTA "UN-Y, DOS-Y" EN VOZ ALTA',
                'LA MELODÍA ENTRA EN LA "Y"'],
        bloques=[
            dict(num=1, titulo='La mano en Mi menor, con el Fa sostenido puesto',
                 pista='andamio en Mi menor · el sostenido está en la armadura, no hay que escribirlo',
                 sistemas=[
                     dict(cap='a) subiendo por las notas de la tonalidad · el Fa cae en tecla negra '
                              'y la mano lo aprende sola',
                          events=[n('E4'), n('F#4'), n('G4'), n('A4'),
                                  n('B4'), n('A4'), n('G4'), n('F#4')],
                          bars=4),
                     dict(cap='b) y la izquierda, dos negras por compás · una en cada tiempo',
                          events=[n('E3'), n('B3'), n('E3'), n('B3'),
                                  n('D3'), n('A3'), n('E3'), n('B3')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Entrar media parte tarde',
                 pista='andamio · el silencio de corchea es el de tu partitura',
                 sistemas=[
                     dict(cap='a) callas media parte y entras · di "un-y" y toca en la "y"',
                          events=[sil('e')] + corch(['E4', 'G4']) + [n('A4', 'e')]
                                 + corch(['B4', 'A4']) + corch(['G4', 'E4']),
                          bars=2),
                     dict(cap='b) lo mismo empezando más abajo · si te adelantas, es que has dejado '
                              'de contar la "y"',
                          events=[sil('e')] + corch(['B3', 'E4']) + [n('F#4', 'e')]
                                 + corch(['G4', 'F#4']) + corch(['E4', 'D4']),
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ CAMBIA UN SOSTENIDO EN LA ARMADURA',
                 texto='Está escrito una sola vez, al principio de cada línea, y manda sobre TODOS '
                       'los Fa de la pieza, estén donde estén. No hay que ir mirando compás por '
                       'compás: se toca una vez despacio buscando la tecla negra y a la tercera la '
                       'mano ya va sola. Es distinto de los sostenidos de la pieza anterior, que '
                       'valían solo para su compás.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda entra en el segundo compás · muy despacio',
                 sistemas=[
                     dict(cap='a) primer compás la derecha sola, y en el segundo aparece la izquierda',
                          events=[sil('e')] + corch(['E4', 'G4']) + [n('A4', 'e')]
                                 + [ac(('E3', 'B4')), ac(('B3', 'A4'))],
                          bars=2),
                     dict(cap='b) y las dos ya andando · la izquierda cae en los golpes y la derecha '
                              'entre ellos',
                          events=[ac(('D3', 'G4')), ac(('A3', 'F#4'))]
                                 + [ac(('E3', 'E4'))] + corch(['F#4', 'G4']),
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
