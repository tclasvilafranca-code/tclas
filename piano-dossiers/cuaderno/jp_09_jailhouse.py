# -*- coding: utf-8 -*-
"""Jailhouse Rock — pieza 9 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arreglo de
   Sadie King, Musescore, 1 página):

     - Detrás de la clave no hay nada, pero la pieza no es Do mayor limpio:
       lleva Si bemol y Fa sostenido escritos DELANTE de las notas, uno a uno.
       Es blues, y el Si bemol es la nota que le da el color.
     - 4/4, y pone "♩ = 150  Swing" y "mf".
     - EMPIEZA CON SILENCIO: silencio de blanca, de negra y de corchea, y
       entonces la primera nota. La pieza no arranca en el uno.
     - La izquierda hace redondas de dos notas los primeros compases, y en el
       c. 12 entra una figura ASCENDENTE de cuatro negras con la digitación
       IMPRESA debajo: 5 · 3 · 2 · 1.
     - MEDIDO nota a nota (200 dpi, `cabezas.py`): esas cuatro notas son
       **Fa · La · Do · Re** (índices 1,96 · -0,06 · -2,08 · -2,78 contra las
       líneas del pentagrama de fa). En la digitación de la mano izquierda el
       5 es el meñique, así que 5·3·2·1 sube: no baja, como decía antes esta
       ficha.
     - Al final pone "ritardando".

   El archivo es EL MISMO que el de José María (md5 idéntico). Allí el trabajo
   iba por la entrada y el Si bemol; aquí, que ya trae el swing de la pieza 6,
   va por la VELOCIDAD: es la primera vez que el cuaderno pide ♩ = 150.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, sil, reto, plan, metronomo, escribir, diferencias,
                      acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=9, nivel='intermedio', slug='JailhouseRock',
    formato='adulto',
    titulo_corto='Jailhouse Rock', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'jailhouse-rock-elvis-presley-.pdf'),
    yt='https://www.youtube.com/results?search_query=jailhouse+rock+piano+easy',

    ficha=dict(
        titulo='Jailhouse Rock',
        autor='Elvis Presley · arreglo de Sadie King',
        datos=[('Tonalidad', 'Do · con blues'), ('Compás', '4/4'),
               ('Tempo', '♩ = 150 Swing'), ('Empieza', 'Con silencio'),
               ('Páginas', 'Una')],
        titulo_ritmos='Cómo entra y cómo acompaña',
        pie_ritmos='Andamio en Do mayor. Lo literal es la entrada con silencios y el Si bemol '
                   'escrito delante de la nota. Las alturas exactas, en tu partitura.',
        armonia=dict(
            titulo='La pieza rápida del cuaderno',
            tarjetas=[
                ('♩ = 150', 'Y con swing',
                 'Es el tempo más alto que te ha pedido el cuaderno hasta ahora, y encima balanceado. '
                 'Las notas son fáciles; lo que no lo es, es llegar ahí sin atropellarse.'),
                ('EL SI BEMOL', 'La nota de blues',
                 'Va escrito delante de la nota, no en la armadura. Es lo que hace que suene a rock '
                 'y no a canción de cuna.'),
                ('LA ENTRADA', 'Casi un compás',
                 'Silencio de blanca, de negra y de corchea, y entonces entras. Contar ese compás a '
                 '150 es medio ejercicio de la semana.'),
                ('EL C. 12', 'La izquierda sube',
                 'Cuatro negras que suben —Fa, La, Do, Re, medidas— con los dedos 5 · 3 · 2 · 1 '
                 'impresos debajo. Es el único sitio de la pieza con digitación escrita.'),
            ],
            pie='El swing ya lo trabajaste en Heart and Soul, así que aquí no es nuevo. Lo nuevo es '
                'la velocidad, y la velocidad no se estudia tocando rápido: se estudia tocando '
                'lento sin fallos y subiendo de cinco en cinco.',
        ),
        ritmos=[
            ('MANO DERECHA', 'entra tras el silencio, con Si bemol · literal',
             [sil('h'), sil('q'), sil('e'), n('Bb4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda de dos notas y a esperar · andamio',
             [ac(('C3', 'G3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero hay Si bemoles y Fa sostenidos escritos delante '
            'de las notas.',
            'Pone "♩ = 150 Swing": rápido, y con las corcheas balanceadas.',
            'La pieza empieza con casi un compás de silencio: no se toca en el uno.',
            'La izquierda hace redondas de dos notas los primeros compases.',
            'En el compás 12 la izquierda SUBE con los dedos 5 · 3 · 2 · 1: Fa, La, Do, Re (medido).',
            'Al final pone "ritardando": frenar poco a poco.',
        ],
        reto='Llegar a ♩ = 150 sin haber ensuciado nada por el camino. La tentación es empezar por '
             'ahí porque la canción se conoce rápida, y ese es exactamente el modo de no llegar '
             'nunca.',
        truco='Pon el metrónomo donde te salga la pieza ENTERA sin pararte, aunque sea a 70. Tócala '
              'tres veces limpias y sube cinco. Si al subir empiezas a fallar, baja cinco y quédate '
              'ahí ese día. En dos semanas estás en 150 sin haberte peleado ni una vez.',
        sabias='Elvis la grabó en 1957 para una película y la coreografía de la escena la montó él '
               'mismo. La grabación original dura menos de dos minutos y medio: era lo que cabía '
               'cómodo en un single de la época.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en las parejas de notas: la primera dura más que la segunda. Es el '
                      'mismo swing que trabajaste en Heart and Soul, pero al doble de velocidad.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza es fácil de notas y difícil de reloj: hay que entrar tarde, ir rápido y '
              'balancear. Las tres se trabajan por separado y ninguna a la velocidad final.',
        reglas=['NO SE EMPIEZA EN EL UNO', 'EL SI BEMOL, EN LA TECLA NEGRA',
                'LA VELOCIDAD, LA ÚLTIMA'],
        bloques=[
            dict(num=1, titulo='La entrada: casi un compás sin tocar',
                 pista='c. 1 · los silencios son literales, la altura es andamio',
                 sistemas=[
                     dict(cap='a) cuenta los cuatro golpes y entra en el "y" del cuatro · a 150 ese '
                              'compás dura dos segundos, así que hay que contarlo, no sentirlo',
                          events=[sil('h'), sil('q'), {'rest': True, 'dur': 'e'},
                                  {'pitch': 'Bb4', 'dur': 'e'}, n('C5', 'w')],
                          bars=2),
                 ]),
            dict(num=2, titulo='El Si bemol, y el Si natural al lado',
                 pista='andamio en Do mayor · el Si bemol está escrito delante de la nota',
                 sistemas=[
                     dict(cap='a) los dos alternando · escucha la diferencia hasta que la reconozcas '
                              'sin mirar la partitura',
                          events=[n('Bb4'), n('B4'), n('Bb4'), n('G4'),
                                  n('Bb4'), n('B4'), n('Bb4'), n('C5')],
                          bars=2),
                     dict(cap='b) y bajando desde el Si bemol, que es lo que hace la pieza · en '
                              'parejas balanceadas, larga-corta',
                          events=[n('Bb4', 'e'), n('A4', 'e'), n('G4', 'e'), n('E4', 'e'),
                                  n('G4', 'e'), n('E4', 'e'), n('C4', 'e'), n('E4', 'e'),
                                  n('G4', 'h'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE SUBE LA VELOCIDAD',
                 texto='No se sube tocando la pieza cada día un poco más rápido: se sube por '
                       'escalones fijos y con una regla. La regla es tres veces limpias antes de '
                       'subir cinco. Si fallas al subir, bajas cinco y ese día se acabó. Parece '
                       'lento y es lo más rápido que hay, porque nunca practicas los fallos.'),
            dict(num=3, titulo='La izquierda del c. 12: cuatro dedos que suben', clef='bass',
                 pista='c. 12 · MEDIDO: Fa, La, Do, Re · la digitación 5 3 2 1 viene impresa',
                 sistemas=[
                     dict(cap='a) escribe tú los dedos encima · el 5 es el meñique, así que '
                              'la mano se abre hacia arriba y no hacia abajo',
                          events=[dict(pitch='F3', dur='q'),
                                  dict(pitch='A3', dur='q'),
                                  dict(pitch='C4', dur='q'),
                                  dict(pitch='D4', dur='q'),
                                  n('D4', 'h'), n('F3', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y bajando por las mismas cuatro notas, para que la mano no aprenda '
                              'solo un sentido · andamio',
                          events=[n('D4'), n('C4'), n('A3'), n('F3'),
                                  n('A3'), n('F3'), n('D3', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, y el frenazo del final',
                 pista='andamio · el ritardando escrito empieza antes de lo que parece',
                 sistemas=[
                     dict(cap='a) la melodía sobre la figura de la izquierda · a la mitad de tu '
                              'velocidad de hoy, no a la final',
                          events=[ac(('C3', 'Bb4'), 'e'), n('A4', 'e'), ac(('E3', 'G4'), 'e'),
                                  n('E4', 'e'), ac(('G3', 'G4'), 'h'),
                                  n('E4'), n('C4'), ac(('C3', 'C4'), 'h')],
                          bars=2),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Jailhouse Rock · para casa',
            intro='Veinte minutos al día, y ni uno a 150. Esta semana se sube por escalones.',
            bloques=[
                reto('Subir de tu velocidad de hoy a ♩ = 150 sin practicar ni un fallo.',
                     'Tres veces limpias y subes cinco. Un fallo y bajas cinco. Apunta cada día el '
                     'número al que te has quedado: la semana que viene se empieza ahí, no más '
                     'arriba.'),
                plan((4, 'Contar el compás de entrada y entrar, diez veces'),
                     (5, 'Si natural y Si bemol alternando, sin mirar'),
                     (6, 'La melodía por escalones de metrónomo'),
                     (5, 'La figura de la izquierda con los dedos 5 3 2 1')),
                metronomo('Empieza donde te salga la pieza entera sin pararte, aunque sea a ♩ = 70.',
                          'Tres limpias y subes cinco; un fallo y bajas cinco. Apunta el número final.'),
                escribir(titulo='Copia el compás que peor te sale',
                         pista='cópialo tal cual de tu partitura y tócalo diez veces solo'),
                diferencias([sil('h'), sil('q'), sil('e'), n('Bb4', 'e'), n('C5', 'w')],
                            [sil('h'), sil('q'), n('Bb4'), n('C5', 'w'), sil('q')],
                            2,
                            titulo='Busca las diferencias en la entrada',
                            pista='el de arriba es tu compás 1 · el de abajo entra en otro sitio'),
                acuerdate('El "ritardando" del final no es opcional ni es adorno: la pieza acaba '
                          'frenando. Si llegas a 150 y terminas de golpe, has tocado las notas y no '
                          'la pieza.',
                          etiqueta='EL FINAL FRENA'),
                para_clase('El número de metrónomo al que te has quedado, y la entrada. Si la '
                           'figura de la izquierda del c. 12 te descoloca, tráela: se arregla '
                           'mirando los dedos impresos una vez.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
