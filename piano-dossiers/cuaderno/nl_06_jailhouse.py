# -*- coding: utf-8 -*-
"""Jailhouse Rock — pieza 6 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arreglo
   de Sadie King, descarga de Musescore, 1 página, unos 20 compases; el mismo
   archivo que la pieza 8 de José María y piezas de Josep y Mercè, byte a
   byte):

     - Detrás de la clave no hay nada, pero lleva Si bemol y Fa sostenido
       escritos delante de las notas: es blues, y el Si bemol da el color.
     - Compás de 4/4. Pone "♩ = 150 Swing", y "mf".
     - Empieza con silencio de blanca, negra y corchea, y entonces entra.
     - La izquierda hace redondas de dos notas al principio, y en el c. 12
       entra una figura ascendente de cuatro negras (Fa · La · Do · Re) con
       la digitación impresa 5 · 3 · 2 · 1.
     - Al final pone "ritardando".
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from nl_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=6, nivel='avanzado', slug='JailhouseRock',
    formato='adulto',
    titulo_corto='Jailhouse Rock', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'jailhouse-rock-elvis-presley-.pdf'),
    yt='https://www.youtube.com/results?search_query=jailhouse+rock+piano+easy',

    ficha=dict(
        titulo='Jailhouse Rock',
        autor='Elvis Presley · arreglo de Sadie King',
        datos=[('Tonalidad', 'Do · con blues'), ('Compás', '4/4'),
               ('Tempo', '♩ = 150 Swing'), ('Empieza', 'Con silencio'),
               ('Páginas', 'Una')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Do mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Lo literal es la entrada con silencio y el Si bemol.',
        armonia=dict(
            titulo='Por qué suena distinta a todo lo anterior',
            tarjetas=[
                ('EL SI BEMOL', 'La nota de blues',
                 'Va escrito delante de la nota, no en la armadura: es la que le da el color de rock '
                 'y no de canción de cuna.'),
                ('EL SWING', 'No es cuadrado',
                 'Las parejas de corcheas no valen igual: la primera dura más. Es un balanceo, no '
                 'una cuenta matemática.'),
                ('LA ENTRADA', 'Casi un compás',
                 'Silencio de blanca, negra y corchea, y entonces entras. Contar ese hueco es medio '
                 'ejercicio de la semana.'),
                ('EL C. 12', 'La izquierda sube',
                 'Cuatro negras ascendentes con los dedos 5 · 3 · 2 · 1 impresos debajo: el único '
                 'sitio de la pieza con digitación escrita.'),
            ],
            pie='Elvis la grabó en 1957 para una película, y el baile de la escena lo coreografió él '
                'mismo. La grabación original dura menos de dos minutos y medio.',
        ),
        ritmos=[
            ('MANO DERECHA', 'entra tras el silencio, con Si bemol',
             [sil('h'), sil('q'), {'rest': True, 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'}],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda de dos notas, y a esperar · andamio',
             [ac(('C3', 'G3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero hay Si bemoles y Fa sostenidos escritos delante de '
            'las notas.',
            'Pone "♩ = 150 Swing": rápido, con las corcheas balanceadas.',
            'La pieza empieza con casi un compás de silencio.',
            'La izquierda hace redondas de dos notas al principio.',
            'En el compás 12 la izquierda sube con los dedos 5 · 3 · 2 · 1: Fa, La, Do, Re.',
            'Al final pone "ritardando".',
        ],
        reto='La velocidad: ♩=150 es más del doble de rápido que lo que has tocado hasta ahora, y la '
             'tentación es empezar por ahí en vez de subir poco a poco desde lento.',
        truco='Pon el metrónomo a la velocidad a la que te sale la pieza entera sin pararte, aunque '
              'sea baja. Tócala tres veces seguidas limpia y sube cinco. Si fallas al subir, baja.',
        sabias='Casi todos los grandes éxitos de esa época duraban menos de dos minutos y medio, '
               'porque era lo que cabía cómodo en la cara de un single de vinilo.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en las parejas de notas: la primera dura más que la segunda. Eso es el '
                      'swing, y se copia de oído, no se escribe.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Fácil de notas, difícil de reloj: hay que entrar tarde, ir rápido y balancear las '
              'corcheas. Se trabajan las tres cosas por separado, y ninguna a la velocidad final.',
        reglas=['NO SE EMPIEZA EN EL UNO', 'EL SI BEMOL, EN LA TECLA NEGRA',
                'LA VELOCIDAD, LA ÚLTIMA'],
        bloques=[
            dict(num=1, titulo='La entrada: casi un compás sin tocar',
                 pista='c. 1 · los silencios son literales, la nota es andamio',
                 sistemas=[
                     dict(cap='a) cuenta los cuatro golpes y entra en el "y" del cuatro',
                          events=[sil('h'), sil('q'), {'rest': True, 'dur': 'e'},
                                  {'pitch': 'Bb4', 'dur': 'e'},
                                  n('C5', 'w')],
                          matiz='mf',
                          bars=2),
                 ]),
            dict(num=2, titulo='El Si bemol: dónde vive el blues',
                 pista='andamio en Do mayor · el Si bemol está escrito delante de la nota',
                 sistemas=[
                     dict(cap='a) el salto de octava con el Si bemol de paso',
                          events=[n('C5'), n('Bb4'), n('G4'), n('E4'),
                                  n('C4'), n('E4'), n('G4'), n('Bb4')],
                          bars=2),
                     dict(cap='b) y en zigzag alrededor del Si bemol, que es lo difícil',
                          events=[n('A4'), n('Bb4'), n('A4'), n('G4'),
                                  n('Bb4'), n('G4'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL SWING',
                 texto='Cuando pone "Swing", las parejas de corcheas no se tocan iguales: la primera '
                       'dura como dos tercios del golpe y la segunda como uno. Escrito así parece '
                       'complicado, y en realidad es lo que hace cualquiera al decir "PAA-pa, '
                       'PAA-pa". Escucha la grabación dos veces y sale solo.'),
            dict(num=3, titulo='La izquierda del c. 12: cuatro dedos que suben', clef='bass',
                 pista='c. 12 · MEDIDO: Fa, La, Do, Re · en tu partitura esos cuatro '
                       'compases llevan impresa la digitación 5 3 2 1',
                 sistemas=[
                     dict(cap='a) escribe tú el dedo encima de cada nota y tócalo sin mirarte la mano',
                          events=[dict(pitch='F3', dur='q'),
                                  dict(pitch='A3', dur='q'),
                                  dict(pitch='C4', dur='q'),
                                  dict(pitch='D4', dur='q'),
                                  n('F3'), n('A3'), n('C4'), n('D4')],
                          bars=2, clef='bass'),
                     dict(cap='b) y movido de sitio, dos peldaños más arriba',
                          events=[n('A2'), n('C3'), n('E3'), n('F3'),
                                  n('D2'), n('F2'), n('A2'), n('B2')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, dos compases',
                 pista='andamio · muy despacio, y con el metrónomo puesto',
                 sistemas=[
                     dict(cap='a) la derecha, con la izquierda aguantando debajo',
                          events=[n('A4'), n('Bb4'), n('A4'), n('G4'),
                                  n('Bb4'), n('G4'), n('E4', 'h')],
                          bars=2),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
