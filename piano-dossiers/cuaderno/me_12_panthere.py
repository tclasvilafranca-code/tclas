# -*- coding: utf-8 -*-
"""La Panthère rose — pieza 12 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("La Panthère rose
   (Première année)", 1 página; el mismo archivo que la pieza 12 de Luisa,
   byte a byte), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA, pero la pieza lleva sostenidos
       escritos delante de la nota a partir del quinto compás.
     - 4/4.
     - La derecha está callada TRES COMPASES ENTEROS y entra en el último
       tiempo del cuarto compás.
     - La izquierda toca desde el primer compás: blancas, alguna redonda.
     - Trae dedos impresos encima de la melodía.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from me_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=12, nivel='intermedio', slug='PanthereRose',
    formato='adulto',
    titulo_corto='La Panthère rose', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'La Pantera Rosa.pdf'),
    yt='https://www.youtube.com/results?search_query=pink+panther+easy+piano+beginner',

    ficha=dict(
        titulo='La Panthère rose',
        autor='Henry Mancini · edición Première année · con los dedos escritos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Teclas negras', 'Escritas'), ('Derecha', 'Entra en c. 4'),
               ('Trae', 'Dedos escritos')],
        titulo_ritmos='Tres compases de espera',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda toca desde el '
                   'primer compás y la derecha no entra hasta el cuarto.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('TRES COMPASES SIN TOCAR', 'Y contando',
                 'La derecha está callada los tres primeros compases y entra en el último tiempo '
                 'del cuarto: doce tiempos de espera contados uno a uno.'),
                ('LA TECLA NEGRA VA SUELTA', 'Delante de la nota',
                 'No hay armadura, pero hay sostenidos escritos delante de algunas notas. Valen '
                 'para esa nota y ese compás, no para toda la pieza.'),
                ('LA IZQUIERDA ABRE', 'Ella marca el pulso',
                 'Es la izquierda la que empieza. Si su pulso no es firme, la derecha no tiene '
                 'ninguna referencia para entrar a tiempo.'),
                ('DEDOS IMPRESOS', 'En la melodía',
                 'Con esos dedos escritos la mano no tiene que saltar en ningún momento de la '
                 'frase.'),
            ],
            pie='Es una melodía que todo el mundo reconoce y que está construida a base de silencios '
                'estratégicos: si se rellenan, pierde toda la gracia.',
        ),
        ritmos=[
            ('MANO DERECHA', 'entra en el último tiempo del compás 4 · literal',
             [sil('q'), sil('q'), sil('q'), n('E4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'blancas, y alguna redonda · literal',
             [n('C3', 'h'), n('G3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Dentro de la pieza hay sostenidos escritos delante de algunas notas.',
            'Compás de 4/4.',
            'La derecha está callada los tres primeros compases.',
            'La derecha entra en el último tiempo del cuarto compás.',
            'Los números encima de la melodía son los dedos.',
        ],
        reto='Contar doce tiempos con la derecha quieta y entrar justo en el trece. Perder la '
             'cuenta hace que la melodía entre a destiempo y ya no se reconozca.',
        truco='Toca los tres primeros compases solo con la izquierda mientras cuentas en voz alta, '
              'y en el tercer compás marca el número más fuerte. Deja la mano derecha apoyada en '
              'sus teclas desde el principio: entrar desde el aire es mucho más difícil que bajar '
              'un dedo que ya está puesto.',
        sabias='Henry Mancini escribió el tema en 1963 para los títulos de crédito, y ganó el '
               'Grammy ese mismo año. El saxo de la grabación original es de Plas Johnson, y Mancini '
               'compuso pensando en su sonido.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los compases de introducción antes de que entre la melodía. Esa '
                      'espera es exactamente lo que vas a hacer tú.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda abre y marca el pulso; la derecha espera y entra con precisión. Se '
              'estudia en ese orden, que es también el orden en que suena.',
        reglas=['LA IZQUIERDA MARCA EL PULSO', 'LA DERECHA, APOYADA Y CONTANDO',
                'LOS SOSTENIDOS VALEN SOLO EN SU COMPÁS'],
        bloques=[
            dict(num=1, titulo='La izquierda sola, los tres primeros compases',
                 pista='andamio en Do mayor · el reparto de figuras es el de tu partitura',
                 sistemas=[
                     dict(cap='a) blancas que se turnan, con el pulso siempre igual',
                          events=[n('C3', 'h'), n('G3', 'h'), n('A2', 'h'), n('E3', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y el compás con una redonda, que también aparece',
                          events=[n('F2', 'w'), n('C3', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: contar doce tiempos y entrar en el trece',
                 pista='andamio · lo que se practica es la espera, no las notas',
                 sistemas=[
                     dict(cap='a) tres tiempos callados y entras en el cuarto',
                          events=[sil('q'), sil('q'), sil('q'), n('E4'),
                                  n('G4'), n('A4'), n('G4'), sil('q')],
                          bars=2),
                     dict(cap='b) con un sostenido escrito delante de la nota',
                          events=[sil('q'), sil('q'), sil('q'), n('F#4'),
                                  n('A4'), n('F#4'), n('E4'), sil('q')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA MANO SE QUEDA APOYADA',
                 texto='Durante los compases callados, mantén la mano derecha encima de sus teclas '
                       'sin hundirlas. Entrar desde el aire obliga a buscar la tecla y a acertar en '
                       'el mismo instante; entrar desde arriba de la tecla solo obliga a bajar el '
                       'dedo. Es un truco que ya has usado en otras piezas de espera, y aquí importa '
                       'más porque la espera es más larga.'),
            dict(num=3, titulo='Las dos juntas, con la entrada de la derecha',
                 pista='andamio · la izquierda no cambia nada cuando la derecha entra · despacio',
                 sistemas=[
                     dict(cap='a) la izquierda sigue igual y la derecha aparece en el cuarto tiempo',
                          events=[n('C3', 'h'), n('G3', 'h'),
                                  n('A2', 'h'), n('E3'), ac(('E3', 'E4'))],
                          bars=2, clef='bass'),
                     dict(cap='b) y ya con las dos sonando',
                          events=[ac(('C3', 'E4')), n('G4'), n('A4'), n('G4'),
                                  ac(('G2', 'D4'), 'h'), n('E4'), n('D4')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 52, 'C4', 'C3',
                          'doce tiempos callado y entrar justo en el uno',
                          desde=4, time_sig=(4, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
