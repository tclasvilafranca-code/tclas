# -*- coding: utf-8 -*-
"""Jailhouse Rock — pieza 8 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arreglo
   de Sadie King, descarga de Musescore, 1 página, unos 20 compases):

     - Detrás de la clave NO HAY NADA, pero la pieza no es Do mayor "limpio":
       lleva Si bemol y Fa sostenido escritos DELANTE de las notas, uno a uno.
       Es blues, y el Si bemol es la nota que le da ese color.
     - Compás de 4/4. Pone "♩ = 150  Swing", y "mf".
     - EMPIEZA CON SILENCIO Y ENTRADA: silencio de blanca, silencio de negra,
       silencio de corchea y la primera nota. La pieza no arranca en el uno.
     - La izquierda hace redondas de dos notas los primeros compases, y en el
       c. 12 entra una figura ASCENDENTE de cuatro negras con la digitacion
       IMPRESA debajo: 5 · 3 · 2 · 1.
     - CORREGIDO tras medirlo (200 dpi, `cabezas.py`, al preparar el cuaderno
       de Josep, que tiene la misma partitura): esas cuatro notas son
       **Fa · La · Do · Re** y SUBEN. Esta ficha decia antes que bajaban, y era
       falso: en la mano izquierda el 5 es el menique, asi que 5·3·2·1 sube.
     - Al final pone "ritardando".

   Lo que NO se cita nota a nota: la melodía va en corcheas con alteraciones
   sueltas. El material va como ANDAMIO en Do mayor y remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, corch, plan, teclado, inventa, rodear,
                      metronomo, para_clase, escalera)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=8, nivel='iniciación',
    slug='JailhouseRock', formato='adulto',
    titulo_corto='Jailhouse Rock', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
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
            titulo='Por qué esta suena distinta a todas las anteriores',
            tarjetas=[
                ('EL SI BEMOL', 'La nota de blues',
                 'Va escrito delante de la nota, no en la armadura. Es la que hace que suene a rock y '
                 'no a canción de cuna.'),
                ('EL SWING', 'No es cuadrado',
                 'Pone "Swing" al lado del tempo: las parejas de corcheas no se tocan iguales, la '
                 'primera dura más. Es un balanceo, no una matemática.'),
                ('LA ENTRADA', 'Casi un compás',
                 'Silencio de blanca, de negra y de corchea, y entonces entras. Contar ese compás es '
                 'medio ejercicio de la semana.'),
                ('EL C. 12', 'La izquierda sube',
                 'Cuatro negras que suben —Fa, La, Do, Re— con los dedos 5 · 3 · 2 · 1 impresos '
                 'debajo. Es el único sitio de la pieza con digitación escrita: úsala.'),
            ],
            pie='Es la primera pieza rápida del cuaderno, pero cabe en una página y la izquierda hace '
                'poquísimo hasta el compás 12. Lo que hay que trabajar es entrar a tiempo y no '
                'atropellarse: las notas son fáciles.',
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
            'Pone "♩ = 150 Swing": rápido, y con las corcheas balanceadas.',
            'La pieza empieza con casi un compás de silencio: no se toca en el uno.',
            'La izquierda hace redondas de dos notas los primeros compases.',
            'En el compás 12 la izquierda SUBE con los dedos 5 · 3 · 2 · 1: Fa, La, Do, Re (medido).',
            'Al final pone "ritardando": frenar poco a poco.',
        ],
        reto='La velocidad. ♩=150 es más del doble de rápido que todo lo que has tocado hasta ahora, y '
             'la tentación es empezar por ahí. No se llega tocando rápido: se llega tocando lento sin '
             'fallos y subiendo poco a poco.',
        truco='Ponte el metrónomo a la velocidad a la que te sale la pieza entera SIN pararte, aunque '
              'sea a 70. Tócala tres veces seguidas limpia y sube cinco. Si al subir empiezas a '
              'fallar, baja. En dos semanas estás en 150 y no te habrás peleado ni un día.',
        sabias='Elvis grabó la canción en 1957 para una película, y el baile de la escena lo coreografió '
               'él mismo. La grabación original dura menos de dos minutos y medio: casi todos los '
               'grandes éxitos de esa época duraban eso, porque era lo que cabía cómodo en un single.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en las parejas de notas: la primera dura más que la segunda. Eso es el '
                      'swing, y no se puede escribir; se copia de oído.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza es fácil de notas y difícil de reloj: hay que entrar tarde, ir rápido y '
              'balancear las corcheas. Trabaja las tres cosas por separado, y ninguna de ellas a la '
              'velocidad final.',
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
                          bars=2),
                 ]),
            dict(num=2, titulo='El Si bemol: dónde vive el blues',
                 pista='andamio en Do mayor · el Si bemol está escrito delante de la nota',
                 sistemas=[
                     dict(cap='a) Si natural y Si bemol, uno detrás de otro · escucha la diferencia',
                          events=[n('B4'), n('Bb4'), n('B4'), n('Bb4'),
                                  n('C5'), n('Bb4'), n('A4'), n('G4')],
                          bars=2),
                     dict(cap='b) y bajando desde el Si bemol, que es lo que hace la pieza',
                          events=[n('Bb4'), n('A4'), n('G4'), n('E4'),
                                  n('G4'), n('E4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL SWING',
                 texto='Cuando pone "Swing", las parejas de corcheas no se tocan iguales: la primera '
                       'dura como dos tercios del golpe y la segunda como uno. Escrito así queda '
                       'complicadísimo, y en realidad es lo que hace cualquiera al decir "PAA-pa, '
                       'PAA-pa". Escucha la grabación dos veces y sale solo. No intentes contarlo.'),
            dict(num=3, titulo='La izquierda del c. 12: cuatro dedos que suben', clef='bass',
                 pista='c. 12 · MEDIDO: Fa, La, Do, Re · la digitación 5 3 2 1 viene impresa',
                 sistemas=[
                     dict(cap='a) escribe tú el dedo encima de cada nota y tócalo sin mirarte la mano',
                          events=[dict(pitch='F3', dur='q'),
                                  dict(pitch='A3', dur='q'),
                                  dict(pitch='C4', dur='q'),
                                  dict(pitch='D4', dur='q'),
                                  n('F3'), n('A3'), n('C4'), n('D4')],
                          bars=2, clef='bass'),
                     dict(cap='b) y movido de sitio, que es lo que hace la pieza · el dibujo de los '
                              'dedos no cambia, solo dónde empieza',
                          events=[n('F2'), n('A2'), n('C3'), n('D3'),
                                  n('G2'), n('B2'), n('D3'), n('E3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, dos compases',
                 pista='andamio · muy despacio, y con el metrónomo puesto',
                 sistemas=[
                     dict(cap='a) la derecha, con la izquierda aguantando debajo',
                          events=[n('Bb4'), n('A4'), n('G4'), n('E4'),
                                  n('G4'), n('E4'), n('C4', 'h')],
                          bars=2),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Jailhouse Rock · para casa',
            intro='Veinte minutos al día. Esta semana importa entrar bien, no ir rápido.',
            bloques=[
                plan((5, 'Contar el compás de entrada y entrar, diez veces'),
                     (5, 'Si natural y Si bemol, alternando, sin mirar'),
                     (5, 'La melodía muy despacio, con el Si bemol puesto'),
                     (5, 'La figura de la izquierda con los dedos 5 3 2 1')),
                teclado({6: 1, 0: 2, 4: 3, 3: 4},
                        ['Escribe el nombre de las cuatro teclas blancas marcadas.',
                         'Y pinta la negra que hay justo a la izquierda de la número 1: ese es el '
                         'Si bemol de esta pieza.'],
                        titulo='En el teclado',
                        pista='la número 1 es el Si'),
                inventa(['Solo Do, Mi, Sol y Si bemol.',
                         'Dos compases de cuatro golpes.',
                         'Que el primer compás empiece con un silencio de negra.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases con sabor de blues',
                        pista='el Si bemol es el que da el color'),
                rodear([[sil('h'), sil('q'), {'rest': True, 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'}],
                        [n('Bb4'), n('A4'), n('G4'), n('E4')],
                        [sil('h'), sil('q'), {'rest': True, 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'}],
                        [n('C5'), n('Bb4'), n('G4'), n('E4')]],
                       titulo='Rodea los dos compases iguales',
                       pista='andamio · fíjate en cuáles llevan silencios'),
                escalera((70, 'la entrada y la melodía, sin pararte'),
                         (110, 'la pieza entera seguida, con el swing puesto'),
                         (150, 'su velocidad'),
                         meta='♩ = 150, que es lo que pone tu partitura',
                         notas=['Tres limpias antes de subir; un fallo y bajas.']),
                para_clase('La entrada, y a qué velocidad has llegado esta semana. El swing lo '
                           'miramos juntos: es más fácil copiarlo que explicarlo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
