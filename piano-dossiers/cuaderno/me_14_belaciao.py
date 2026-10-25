# -*- coding: utf-8 -*-
"""Bela Ciao (La Casa de Papel) — pieza 14 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive (1 página, Musescore; el
   mismo archivo que la pieza 13 de Luisa, byte a byte), leído a 230 dpi:

     - Detrás de la clave hay UN SOSTENIDO: Mi menor.
     - 2/4, con barra de repetición al principio.
     - La derecha empieza con silencio de corchea y sigue con corcheas.
     - El primer compás de la izquierda está callado entero; después hace
       dos negras por compás.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from me_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=14, nivel='intermedio', slug='BelaCiao',
    formato='adulto',
    titulo_corto='Bela Ciao', time_sig=(2, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'bela-ciao.pdf'),
    yt='https://www.youtube.com/results?search_query=bella+ciao+easy+piano+la+casa+de+papel',

    ficha=dict(
        titulo='Bela Ciao',
        autor='Canción popular italiana · conocida por La Casa de Papel',
        datos=[('Tonalidad', 'Mi menor'), ('Armadura', 'Un sostenido'),
               ('Compás', '2/4'), ('Empieza', 'Media parte tarde'),
               ('Izquierda', 'Dos negras')],
        titulo_ritmos='Compás de dos, con entrada retrasada',
        pie_ritmos='Andamio en Mi menor. Lo literal es el arranque: silencio de corchea y corcheas '
                   'seguidas. El primer compás de la izquierda está callado entero.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('MI MENOR', 'Con un sostenido',
                 'Es tu primera pieza en menor con armadura de verdad: todos los Fa son negros, '
                 'escritos una sola vez al principio de la línea.'),
                ('COMPÁS DE DOS', 'Rápido de contar',
                 'Con solo dos tiempos por compás, se cuenta más deprisa que en 3/4 o 4/4, aunque el '
                 'tempo real no cambie.'),
                ('MEDIA PARTE TARDE', 'Silencio de corchea',
                 'La melodía no entra en el golpe: entra justo después. Es el primer silencio de tu '
                 'cuaderno que dura menos de un tiempo entero.'),
                ('LA IZQUIERDA ESPERA', 'Un compás entero',
                 'El primer compás está callado del todo; a partir del segundo hace dos negras y ya '
                 'no para.'),
            ],
            pie='La cantaban las trabajadoras de los arrozales del norte de Italia mucho antes de la '
                'guerra, con otra letra completamente distinta a la que la hizo famosa después.',
        ),
        ritmos=[
            ('MANO DERECHA', 'silencio de corchea y corcheas · literal',
             [sil('e')] + corch(['B4', 'E5']) + [n('F#5', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos negras por compás · literal',
             [n('E3'), n('B3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa son teclas negras.',
            'La tonalidad es Mi menor.',
            'Compás de 2/4: dos tiempos por compás.',
            'La melodía entra media parte tarde, tras un silencio de corchea.',
            'El primer compás de la izquierda está callado entero.',
            'A partir del segundo compás la izquierda hace dos negras.',
        ],
        reto='Entrar media parte tarde sin adelantarse. No es esperar un tiempo entero: es esperar '
             'la mitad, y al principio la mano tiende a entrar antes de tiempo.',
        truco='Cuenta "un-y, dos-y" en voz alta y toca solo en las "y". Cuando eso salga bien, toca '
              'la primera nota en la "y" del uno y sigue la melodía: la palabra "y" es el sitio '
              'exacto donde entra.',
        sabias='La letra que la hizo famosa en todo el mundo es de origen partisano, de la Segunda '
               'Guerra Mundial, pero la melodía es mucho más antigua y viajó por Europa del Este '
               'antes de llegar a Italia.',
        qr=dict(titulo='Escúchala',
                texto='Da palmas en el "uno, dos" y fíjate en que la voz nunca entra con la palmada: '
                      'entra justo después. Ese pequeño retraso es toda la pieza.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas pequeñas y nuevas: un sostenido que vale siempre, y una entrada media '
              'parte tarde. Un paso para cada una, y el tercero las junta.',
        reglas=['TODOS LOS FA SON NEGROS', 'CUENTA "UN-Y, DOS-Y" EN VOZ ALTA',
                'LA MELODÍA ENTRA EN LA "Y"'],
        bloques=[
            dict(num=1, titulo='La mano en Mi menor',
                 pista='andamio · el sostenido está en la armadura, no hay que escribirlo',
                 sistemas=[
                     dict(cap='a) saltos de tercera por las notas de la tonalidad',
                          events=[n('E4'), n('G4'), n('F#4'), n('A4'),
                                  n('G4'), n('B4'), n('A4'), n('G4')],
                          bars=4),
                     dict(cap='b) y la izquierda, con saltos de cuarta',
                          events=[n('B3'), n('E3'), n('A3'), n('D3'),
                                  n('G3'), n('B3'), n('E3'), n('A3')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Entrar media parte tarde',
                 pista='andamio · el silencio de corchea es el de tu partitura',
                 sistemas=[
                     dict(cap='a) callas media parte y entras',
                          events=[sil('e')] + corch(['F#4', 'A4']) + [n('B4', 'e')]
                                 + corch(['A4', 'G4']) + corch(['F#4', 'D4']),
                          bars=2),
                     dict(cap='b) lo mismo empezando más abajo',
                          events=[sil('e')] + corch(['A3', 'D4']) + [n('E4', 'e')]
                                 + corch(['F#4', 'E4']) + corch(['D4', 'B3']),
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ CAMBIA UN SOSTENIDO EN LA ARMADURA',
                 texto='Está escrito una sola vez, al principio de cada línea, y manda sobre TODOS '
                       'los Fa de la pieza, estén donde estén. No hay que revisarlo compás a compás: '
                       'se toca una vez despacio buscando la tecla negra, y a la tercera repetición '
                       'la mano ya va sola sin pensarlo.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda entra en el segundo compás · muy despacio',
                 sistemas=[
                     dict(cap='a) primer compás la derecha sola, y en el segundo aparece la '
                              'izquierda',
                          events=[sil('e')] + corch(['A4', 'B4']) + [n('C#5', 'e')]
                                 + [ac(('A3', 'B4')), ac(('E3', 'A4'))],
                          bars=2),
                     dict(cap='b) y las dos ya andando',
                          events=[ac(('B3', 'A4')), ac(('F#3', 'G4'))]
                                 + [ac(('B3', 'F#4'))] + corch(['G4', 'A4']),
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Mi menor', 7, 'E4', 'E2',
                          'se entra media parte tarde, no un tiempo entero',
                          desde=4, time_sig=(2, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
