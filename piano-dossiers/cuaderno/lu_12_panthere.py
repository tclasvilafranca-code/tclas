# -*- coding: utf-8 -*-
"""La Panthère rose — pieza 12 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("La Panthère rose
   (Première année)", 1 página, con un dibujo de la pantera), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA, pero la pieza lleva SOSTENIDOS ESCRITOS
       DELANTE DE LAS NOTAS a partir del quinto compás.
     - 4/4.
     - La derecha está CALLADA TRES COMPASES ENTEROS y en el cuarto entra en el
       último tiempo: tres silencios de negra y una negra.
     - La izquierda toca desde el primer compás: blanca + blanca, redonda,
       blanca + blanca, blanca con puntillo + silencio, redonda.
     - Trae DIGITACIÓN IMPRESA encima de la melodía (1, 2, 3, 4).

   Lo nuevo: aguantar tres compases sin tocar, y las teclas negras escritas
   delante de la nota en vez de al principio del pentagrama.
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
    alumno='Luisa', carpeta='Luisa', num=12, nivel='iniciación', slug='PanthereRose',
    formato='adulto',
    titulo_corto='La Panthère rose', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'la-panthere-rose-easy.pdf'),
    yt='https://www.youtube.com/results?search_query=pink+panther+easy+piano+beginner',

    ficha=dict(
        titulo='La Panthère rose',
        autor='Henry Mancini · edición Première année · con los dedos escritos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Teclas negras', 'Escritas'), ('Derecha', 'Entra en el c. 4'),
               ('Trae', 'Dedos escritos')],
        titulo_ritmos='La izquierda empieza sola',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda toca desde el '
                   'primer compás y la derecha no entra hasta el cuarto.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('TRES COMPASES SIN TOCAR', 'Y contando',
                 'La mano derecha está callada los tres primeros compases y entra en el último '
                 'tiempo del cuarto. Doce tiempos de espera contados uno a uno.'),
                ('LA TECLA NEGRA VA SUELTA', 'Delante de la nota',
                 'Detrás de la clave no hay nada, pero dentro de la pieza hay sostenidos escritos '
                 'delante de algunas notas. Valen para esa nota y ese compás, no para toda la pieza.'),
                ('LA IZQUIERDA MANDA', 'Ella empieza',
                 'Por primera vez es la izquierda la que abre. Si ella no lleva un pulso firme, la '
                 'derecha no sabe cuándo entrar.'),
                ('DEDOS ESCRITOS', 'Números impresos',
                 'La melodía trae 1, 2, 3 y 4 escritos. Con esos dedos la mano no tiene que saltar '
                 'ni una vez.'),
            ],
            pie='Es una melodía que todo el mundo reconoce y que está hecha de notas sueltas con '
                'huecos. Los huecos son parte de la broma: si los rellenas, deja de tener gracia.',
        ),
        ritmos=[
            ('MANO DERECHA', 'entra en el último tiempo del cuarto compás · literal',
             [sil('q'), sil('q'), sil('q'), n('C4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos blancas y una redonda · literal',
             [n('C3', 'h'), n('G3', 'h'), n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Dentro de la pieza hay sostenidos escritos delante de algunas notas.',
            'Compás de 4/4.',
            'La derecha está callada los tres primeros compases.',
            'La derecha entra en el cuarto tiempo del compás cuatro.',
            'Los números encima de la melodía son los dedos.',
        ],
        reto='Contar doce tiempos con la mano derecha quieta y entrar justo en el trece. Si la '
             'cuenta se pierde, la melodía entra a destiempo y ya no se reconoce.',
        truco='Toca los tres primeros compases con la izquierda mientras cuentas en voz alta, y en '
              'el tercero empieza a decir el número más fuerte. Deja la mano derecha apoyada en sus '
              'teclas desde el principio: entrar desde el aire es mucho más difícil.',
        sabias='Henry Mancini escribió el tema en 1963 para los títulos de crédito, y ganó el Grammy '
               'ese año. El saxo que lo toca en la grabación original es de Plas Johnson, y Mancini '
               'lo escribió pensando en él.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los compases de la introducción antes de que entre la melodía. Esa '
                      'espera es exactamente lo que vas a hacer tú.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda abre y la derecha espera. Se estudia en ese orden, que es también el '
              'orden en que suena.',
        reglas=['LA IZQUIERDA MARCA EL PULSO', 'LA DERECHA, APOYADA Y CONTANDO',
                'LOS SOSTENIDOS VALEN SOLO EN SU COMPÁS'],
        bloques=[
            dict(num=1, titulo='La izquierda sola, los tres primeros compases',
                 pista='andamio en Do mayor · el reparto de figuras es el de tu partitura',
                 sistemas=[
                     dict(cap='a) dos blancas y una redonda · el pulso tiene que ser el mismo en '
                              'los tres compases',
                          events=[n('C3', 'h'), n('G3', 'h'), n('C3', 'w'),
                                  n('A2', 'h'), n('E3', 'h')],
                          bars=4, clef='bass'),
                     dict(cap='b) y el compás que acaba con silencio · la mano se levanta, la '
                              'cuenta no se para',
                          events=[n('F2', 'h.'), sil('q'), n('C3', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: contar doce tiempos y entrar en el trece',
                 pista='andamio · lo que se practica es la espera, no las notas',
                 sistemas=[
                     dict(cap='a) tres tiempos callados y entras en el cuarto · cuenta en voz alta '
                              'y no mires el reloj',
                          events=[sil('q'), sil('q'), sil('q'), n('C4'),
                                  n('E4'), n('F4'), n('E4'), sil('q')],
                          bars=2),
                     dict(cap='b) con un sostenido escrito delante de la nota · vale para esa nota '
                              'y ese compás, no para el resto',
                          events=[sil('q'), sil('q'), sil('q'), n('F#4'),
                                  n('G4'), n('F#4'), n('E4'), sil('q')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA MANO SE QUEDA APOYADA',
                 texto='Durante los compases callados, deja la mano derecha encima de sus teclas sin '
                       'hundirlas. Entrar desde el aire obliga a buscar la tecla y a acertar en el '
                       'mismo instante; entrar desde arriba de la tecla solo obliga a bajar el dedo. '
                       'Es el mismo truco de las tres piezas anteriores, y aquí importa más porque '
                       'la espera es más larga.'),
            dict(num=3, titulo='Las dos juntas, con la entrada de la derecha',
                 pista='andamio · la izquierda no cambia nada cuando la derecha entra · despacio',
                 sistemas=[
                     dict(cap='a) la izquierda sigue igual y la derecha aparece en el cuarto tiempo',
                          events=[n('C3', 'h'), n('G3', 'h'),
                                  n('C3', 'h'), n('G3'), ac(('C3', 'C4'))],
                          bars=2, clef='bass'),
                     dict(cap='b) y ya con las dos sonando · el uno lo sigue marcando la izquierda',
                          events=[ac(('C3', 'E4')), n('F4'), n('E4'), n('C4'),
                                  ac(('G2', 'D4'), 'h'), n('E4'), n('D4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Do mayor', 'C4', 'G2', time_sig=(4, 4), variante=16,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1 + [
    # Su dificultad medida: doce tiempos callado y entrar justo. Contarlos sobre
    # el papel, con los silencios dibujados, es distinto de contarlos de memoria.
    dict(cap='e) los doce tiempos de espera, contados · tres compases callado y '
             'entrar en el uno, ni antes ni después',
         events=[{'rest': True, 'dur': 'w'}, {'rest': True, 'dur': 'w'},
                 {'rest': True, 'dur': 'w'},
                 {'pitch': 'C4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'},
                 {'pitch': 'G4', 'dur': 'h'}],
         bars=4, show_time=False),
]
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
