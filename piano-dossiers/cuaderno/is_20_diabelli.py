# -*- coding: utf-8 -*-
"""28 melodische Übungsstücke nº 3, de Diabelli — pieza 20 de Isaac. El reto
   final del álbum.

   Lo comprobado sobre el PDF de su carpeta de Drive (Anton Diabelli, Op.
   149, edición Mutopia/MutopiaBSD, 3 páginas; medida de cero, no coincide
   con ninguna otra partitura del proyecto):

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 2/4, y pone "Moderato." (sin número de metrónomo impreso).
     - Es a cuatro manos. Tu parte es el Primo (páginas 2-3): LOS DOS
       PENTAGRAMAS EN CLAVE DE SOL, con un "8va" al principio — se toca una
       octava más alto de lo escrito.
     - La derecha y la izquierda se mueven con dibujos parecidos: corcheas
       con silencios de por medio, en staccato.
     - Hay ligaduras, algún adorno (apoyatura) y acentos (>).
     - Hay una repetición hacia el compás 15, y la pieza termina con un
       acorde con calderón.

   Es la pieza más exigente de tu carpeta: por eso cierra el álbum, como
   Für Elise cierra el de Mercè. El Secondo (páginas 1-2), con arpegios
   rápidos en clave de fa, lo toca la profesora.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from is_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=20, nivel='intermedio', slug='Diabelli',
    formato='adulto',
    titulo_corto='Diabelli · Op. 149 nº 3', time_sig=(2, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source',
                           'DIABELLI ( cuatro manos).pdf'),
    yt='https://www.youtube.com/results?search_query=diabelli+op+149+melodische+ubungsstucke+piano+4+hands',

    ficha=dict(
        titulo='28 melodische Übungsstücke nº 3',
        autor='Anton Diabelli · Op. 149 · a cuatro manos · tu parte es el Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/4'),
               ('Carácter', 'Moderato'), ('Las dos manos', 'Clave de sol'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Corcheas con silencios, en staccato',
        pie_ritmos='Andamio en Do mayor, inspirado en el dibujo de tu partitura: corcheas cortas '
                   'separadas por silencios, en las dos manos.',
        armonia=dict(
            titulo='El cierre del álbum, a propósito',
            tarjetas=[
                ('EL 8va', 'Una octava más alto',
                 'Encima del primer compás hay una raya de puntos con "8va": todo lo que hay debajo '
                 'suena una octava por encima de lo escrito, hasta que la raya termina.'),
                ('LAS DOS EN CLAVE DE SOL', 'Sin clave de fa',
                 'Tu parte entera va en clave de sol, arriba y abajo, con dibujos parecidos en las '
                 'dos manos: no hay una que sostenga y otra que corra.'),
                ('CORCHEAS Y SILENCIOS', 'Staccato',
                 'El dibujo se repite: una corchea corta, un hueco, otra corchea. Nada se sostiene '
                 'ni se liga por defecto.'),
                ('LA MÁS EXIGENTE', 'De toda tu carpeta',
                 'Cierra el álbum a propósito, igual que otros compañeros cierran el suyo con la '
                 'pieza más difícil que tienen.'),
            ],
            pie='Diabelli escribió estos 28 estudios como escalones progresivos para alumnos que ya '
                'dominaban lo básico: cada uno mete una dificultad nueva sin avisar demasiado.',
        ),
        ritmos=[
            ('MANO DERECHA', 'corcheas cortas con silencio detrás · andamio',
             [n('C5', 'e'), sil('e'), n('E5', 'e'), sil('e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'el mismo tipo de dibujo, más grave · andamio',
             [n('C4', 'e'), sil('e'), n('E4', 'e'), sil('e')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: Do mayor.',
            'Compás de 2/4.',
            'Pone "Moderato.", sin número de metrónomo impreso.',
            'Tus dos pentagramas van en clave de sol, con un "8va" al principio.',
            'Las dos manos se mueven en corcheas con silencios, en staccato.',
            'Hay una repetición hacia la mitad de la pieza, y acaba con un acorde con calderón.',
        ],
        reto='Que las corcheas suenen realmente cortas y separadas, sin que el silencio de detrás '
             'se coma o se alargue: en staccato de verdad, la nota y el silencio duran exactamente '
             'lo mismo.',
        truco='Toca cada corchea levantando el dedo justo después de pulsarla, como si la tecla '
              'quemara. Cuenta el silencio en voz alta ("corchea-Y") para que dure lo mismo que la '
              'nota, ni más ni menos.',
        sabias='Diabelli es más conocido hoy por el vals que le compró a Beethoven para pedirle una '
               'variación, y que acabó convirtiéndose en las 33 Variaciones Diabelli: una de las '
               'obras más ambiciosas de toda la música para piano.',
        qr=dict(titulo='Escúchala',
                texto='Busca una grabación de las "28 melodische Übungsstücke" y escucha lo separado '
                      'que suena cada corchea: ese hueco de silencio es la clave del estilo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El reto final del álbum. El staccato con silencio real es lo nuevo: cada nota se '
              'suelta antes de que llegue la siguiente, en las dos manos por igual.',
        reglas=['LA CORCHEA Y EL SILENCIO DURAN LO MISMO', 'LAS DOS MANOS EN CLAVE DE SOL',
                'EL 8va CAMBIA TODO UN COMPÁS ENTERO'],
        bloques=[
            dict(num=1, titulo='El dibujo de corcheas con silencio, aislado',
                 pista='andamio en Do mayor · el mismo tipo de patrón que trae tu partitura',
                 sistemas=[
                     dict(cap='a) subiendo con un hueco detrás de cada nota',
                          events=[n('C5', 'e'), sil('e'), n('D5', 'e'), sil('e'),
                                  n('E5', 'e'), sil('e'), n('F5', 'e'), sil('e')],
                          bars=4),
                     dict(cap='b) y bajando, con el mismo hueco',
                          events=[n('G5', 'e'), sil('e'), n('F5', 'e'), sil('e'),
                                  n('E5', 'e'), sil('e'), n('D5', 'e'), sil('e')],
                          bars=4, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: el mismo dibujo, en su registro',
                 pista='andamio · las dos manos comparten el mismo tipo de patrón',
                 sistemas=[
                     dict(cap='a) subiendo, con el hueco de silencio',
                          events=[n('C4', 'e'), sil('e'), n('D4', 'e'), sil('e'),
                                  n('E4', 'e'), sil('e'), n('F4', 'e'), sil('e')],
                          bars=4, clef='bass'),
                     dict(cap='b) y bajando',
                          events=[n('G4', 'e'), sil('e'), n('F4', 'e'), sil('e'),
                                  n('E4', 'e'), sil('e'), n('D4', 'e'), sil('e')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ QUIERE DECIR EL 8va',
                 texto='La raya de puntos que sigue a "8va" marca hasta dónde llega su efecto: todo '
                       'lo que está debajo de esa raya suena una octava más agudo de lo que está '
                       'escrito en el papel. No cambia ninguna nota ni ningún dedo: cambia solo '
                       'dónde suena, y hay que recordarlo mientras dura la raya.'),
            dict(num=3, titulo='Las dos manos juntas, en staccato',
                 pista='andamio · las dos sueltan la nota exactamente igual de rápido · despacio',
                 sistemas=[
                     dict(cap='a) subiendo juntas, con el mismo hueco en las dos manos',
                          events=[ac(('C4', 'C5'), 'e'), sil('e'), ac(('D4', 'D5'), 'e'), sil('e'),
                                  ac(('E4', 'E5'), 'e'), sil('e'), ac(('F4', 'F5'), 'e'), sil('e')],
                          bars=4),
                     dict(cap='b) y bajando, con la misma separación',
                          events=[ac(('G4', 'G5'), 'e'), sil('e'), ac(('F4', 'F5'), 'e'), sil('e'),
                                  ac(('E4', 'E5'), 'e'), sil('e'), ac(('D4', 'D5'), 'e'), sil('e')],
                          bars=4, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
