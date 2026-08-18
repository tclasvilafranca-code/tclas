# -*- coding: utf-8 -*-
"""Honor Him, de Gladiator — pieza 22 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Honor Him - Gladiator
   (Easy Version)", Hans Zimmer, 1 página), leído a 230 dpi:

     - Detrás de la clave hay TRES SOSTENIDOS: La mayor.
     - 3/4, y pone "♩ = 70" y "mp".
     - La derecha está callada DOS COMPASES ENTEROS y entra en el tercero.
     - La izquierda sostiene blancas con puntillo, ligadas de un compás a
       otro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=22, nivel='intermedio', slug='HonorHim',
    formato='adulto',
    titulo_corto='Honor Him · Gladiator', time_sig=(3, 4), key_sig='La mayor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'Gladyator.pdf'),
    yt='https://www.youtube.com/results?search_query=honor+him+gladiator+piano+easy',

    ficha=dict(
        titulo='Honor Him · Gladiator',
        autor='Hans Zimmer · versión fácil',
        datos=[('Tonalidad', 'La mayor'), ('Armadura', 'Tres sostenidos'),
               ('Compás', '3/4'), ('Tempo', '♩ = 70'),
               ('Izquierda', 'Blanca con puntillo')],
        titulo_ritmos='Dos compases de espera',
        pie_ritmos='Andamio en La mayor. Lo literal es el arranque: la izquierda sostiene desde el '
                   'primer compás y la derecha no entra hasta el tercero.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('TRES SOSTENIDOS', 'Fa, Do y Sol',
                 'Fa, Do y Sol son sostenidos en toda la pieza. Es la armadura con más alteraciones '
                 'de tu cuaderno hasta ahora.'),
                ('DOS COMPASES SIN TOCAR', 'La derecha espera',
                 'Igual que en La Panthère rose, hay que contar en silencio antes de entrar, aquí '
                 'seis tiempos completos.'),
                ('LA IZQUIERDA SOSTIENE', 'Una nota larga',
                 'Toca una blanca con puntillo por compás y la mantiene, marcando el pulso de fondo '
                 'mientras la derecha calla.'),
                ('♩ = 70 Y mp', 'Lento y suave',
                 'El carácter pide calma: no hay prisa en ningún momento de la pieza.'),
            ],
            pie='Es la música de los créditos finales de la película, pensada para acompañar el '
                'último tramo de la historia con solemnidad, no con acción.',
        ),
        ritmos=[
            ('MANO DERECHA', 'entra en el tercer compás · literal',
             [sil('h.'), sil('h.'), n('C#5', 'h.')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'blanca con puntillo, ligada · literal',
             [n('D2', 'h.'), n('D2', 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay tres sostenidos: Fa, Do y Sol.',
            'La tonalidad es La mayor.',
            'Compás de 3/4, con "♩ = 70" y "mp" escritos arriba.',
            'La derecha está callada los dos primeros compases.',
            'La derecha entra en el tercer compás.',
            'La izquierda sostiene blancas con puntillo, ligadas de un compás a otro.',
        ],
        reto='Contar seis tiempos completos con la derecha quieta, sin perder ni ganar ninguno. Es '
             'la espera más larga de tu cuaderno hasta ahora.',
        truco='Toca los dos primeros compases solo con la izquierda mientras cuentas en voz alta '
              'del uno al seis, y marca mentalmente el número seis como aviso de que la derecha '
              'entra a continuación. Mantén la mano derecha apoyada en sus teclas todo el tiempo.',
        sabias='Hans Zimmer compuso la banda sonora de Gladiator en 1999 junto con Lisa Gerrard, y '
               'ganó varios premios internacionales. El propio Zimmer dijo que quería que sonara '
               '"antigua y moderna a la vez".',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los primeros compases de silencio antes de que entre la melodía. Esa '
                      'espera solemne es exactamente lo que vas a hacer tú al piano.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda marca el pulso; la derecha espera y entra con calma.',
        reglas=['FA, DO Y SOL SON SIEMPRE SOSTENIDOS', 'LA IZQUIERDA SOSTIENE, LA DERECHA CUENTA',
                '♩ = 70: SIN NINGUNA PRISA'],
        bloques=[
            dict(num=1, titulo='La mano en La mayor',
                 pista='andamio · los tres sostenidos están en la armadura',
                 sistemas=[
                     dict(cap='a) subiendo por las notas de la tonalidad',
                          events=[n('A4'), n('B4'), n('C#5'), n('D5'),
                                  n('E5'), n('D5'), n('C#5'), n('B4'), n('A4')],
                          bars=3),
                     dict(cap='b) y la izquierda, con el mismo sostenido de Do',
                          events=[n('A2'), n('C#3'), n('E3'),
                                  n('F#2'), n('C#3'), n('F#3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: sostener a través del compás',
                 pista='andamio · una nota que dura un compás y medio',
                 sistemas=[
                     dict(cap='a) toca en el uno y no sueltes hasta el siguiente compás',
                          events=[n('A2', 'h.'), n('A2', 'h.')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de nota, con la misma sujeción',
                          events=[n('E2', 'h.'), n('E2', 'h.')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA EN SEIS, NO EN DOS COMPASES',
                 texto='Contar "compás uno, compás dos" es fácil perderlo si la mente se '
                       'distrae. Contar los seis tiempos uno a uno deja mucho menos margen de '
                       'error: al llegar al "seis" sabes con certeza que la derecha entra después.'),
            dict(num=3, titulo='Las dos juntas, con la entrada de la derecha',
                 pista='andamio · la izquierda no cambia nada cuando la derecha entra · despacio',
                 sistemas=[
                     dict(cap='a) la izquierda sigue igual y entra la derecha',
                          events=[n('A2', 'h.'), n('A2', 'h.'), ac(('A2', 'C#5'), 'h.')],
                          bars=3, clef='bass'),
                     dict(cap='b) y con la frase que sigue',
                          events=[ac(('A2', 'D5'), 'h.'), ac(('A2', 'C#5'), 'h.')],
                          bars=2, clef='bass', show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
