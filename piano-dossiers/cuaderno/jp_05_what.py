# -*- coding: utf-8 -*-
"""What Was I Made For? (Billie Eilish) — pieza 5 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, 2 páginas,
   50 compases, con letra debajo):

     - Do mayor: detrás de la clave no hay nada.
     - 4/4, y pone "♩ = 78".
     - CIFRADO IMPRESO encima del pentagrama, compás a compás: C · Em · F · Am ·
       Dm · G. Se repite el mismo ciclo casi toda la pieza.
     - La izquierda hace DOS acordes de blanca por compás, no uno.
     - Los cuatro primeros compases la derecha calla (silencios de redonda), y
       la melodía entra en el c. 4 con anacrusa.
     - Muchas frases empiezan con silencio o a mitad de tiempo: la melodía va
       a contratiempo de la izquierda casi todo el rato.
     - Hay barras de repetición y casillas de primera y segunda vez.

   Esta es la primera hoja del cuaderno con el bloque de CIFRADO, y se pone
   aquí porque su partitura lo trae impreso de verdad (`jp_recetas.CON_CIFRADO`).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, sil, reto, plan, escalera, cifrado, colorear,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=5, nivel='intermedio', slug='WhatWasIMadeFor',
    formato='adulto',
    titulo_corto='What Was I Made For?', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'what-was-i-made-for-billie-eilish.pdf'),
    yt='https://www.youtube.com/results?search_query=what+was+i+made+for+piano+easy',

    ficha=dict(
        titulo='What Was I Made For?',
        autor='Billie Eilish · de la película Barbie',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 78'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Dos')],
        titulo_ritmos='La derecha entra donde la izquierda no está',
        pie_ritmos='Andamio en Do mayor. Lo literal es la relación: dos acordes de blanca abajo y '
                   'una melodía que casi nunca cae con ellos. Las notas exactas, en tu partitura.',
        armonia=dict(
            titulo='Notas fáciles, sitio difícil',
            tarjetas=[
                ('EL CIFRADO', 'C Em F Am Dm G',
                 'Está impreso encima del pentagrama, compás a compás, y se repite casi toda la '
                 'pieza. Seis acordes: si los sabes, sabes la armonía entera.'),
                ('DOS POR COMPÁS', 'La izquierda',
                 'Dos acordes de blanca en cada compás, no uno. Marcan el uno y el tres, y son el '
                 'reloj contra el que la melodía va a contratiempo.'),
                ('A CONTRATIEMPO', 'La derecha',
                 'La mayoría de las frases empiezan con silencio o a mitad de tiempo. Ninguna nota '
                 'es difícil; lo difícil es el sitio exacto donde cae.'),
                ('CUATRO COMPASES', 'De introducción',
                 'La derecha no toca hasta el cuarto compás. Hay que contarlos, y contarlos sin '
                 'tocar es más difícil que contarlos tocando.'),
            ],
            pie='Es la pieza del cuaderno con las notas más fáciles y el ritmo más incómodo. Por eso '
                'está en la primera mitad del curso: se puede trabajar el sitio de las notas sin '
                'pelearse a la vez con las notas.',
        ),
        ritmos=[
            ('MANO DERECHA', 'entra tarde y a contratiempo · andamio',
             [sil('q'), n('C4', 'e'), n('E4', 'e'), n('G4', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos acordes de blanca por compás · literal',
             [ac(('C3', 'E3', 'G3'), 'h'), ac(('C3', 'E3', 'G3'), 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay armadura: ni sostenidos ni bemoles.',
            'Pone "♩ = 78": tempo con número.',
            'El cifrado está impreso encima del pentagrama: C, Em, F, Am, Dm y G.',
            'La izquierda hace dos acordes de blanca en cada compás.',
            'La derecha no entra hasta el compás 4, y entra antes del tiempo fuerte.',
            'Hay repeticiones con casilla de primera y de segunda vez.',
        ],
        reto='Entrar en el sitio exacto. Las notas de esta pieza las tocarías a la primera; lo que '
             'no sale a la primera es CUÁNDO entra cada una, porque casi ninguna cae con la '
             'izquierda.',
        truco='Toca la izquierda sola contando "un-y-dos-y-tres-y-cuatro-y" en voz alta, y luego, '
              'sin dejar de contar, canta la melodía encima sin tocarla. Cuando sepas decir en qué '
              'sílaba entra cada frase, la mano ya no se equivoca.',
        sabias='La canción se escribió para la película de Barbie y ganó el Óscar y el Grammy a la '
               'mejor canción. Billie Eilish contó que la escribió en un día en el que no le salía '
               'nada, y que la letra habla justo de eso.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la voz casi nunca entra a la vez que el piano. Ese desfase es '
                      'la canción entera, y es lo que estás estudiando.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí no hay notas difíciles: hay sitios difíciles. Todo el trabajo de la semana es '
              'de reloj, así que se hace contando en voz alta y con la izquierda de referencia.',
        reglas=['CONTAR "UN-Y-DOS-Y" SIEMPRE', 'LA IZQUIERDA ES EL RELOJ',
                'LA MELODÍA CASI NUNCA CAE CON ELLA'],
        bloques=[
            dict(num=1, titulo='La izquierda: dos acordes por compás', clef='bass',
                 pista='la FORMA es literal (dos blancas por compás); las notas, andamio en Do mayor',
                 sistemas=[
                     dict(cap='a) el uno y el tres, iguales de fuerza · esto es tu reloj, y un reloj '
                              'no hace crescendo',
                          events=[ac(('C3', 'E3', 'G3'), 'h'), ac(('C3', 'E3', 'G3'), 'h'),
                                  ac(('E3', 'G3', 'B3'), 'h'), ac(('E3', 'G3', 'B3'), 'h')],
                          cresc=4,
                          bars=2, clef='bass'),
                     dict(cap='b) con el ciclo que trae impreso el cifrado · Fa y La menor, que son '
                              'los dos siguientes',
                          events=[ac(('F2', 'A2', 'C3'), 'h'), ac(('F2', 'A2', 'C3'), 'h'),
                                  ac(('A2', 'C3', 'E3'), 'h'), ac(('A2', 'C3', 'E3'), 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Entrar a contratiempo, sin la izquierda',
                 pista='andamio · cuenta en voz alta y entra donde dice, no donde te apetece',
                 sistemas=[
                     dict(cap='a) entrar en el "y" del uno · el silencio de corchea es tan '
                              'importante como las notas',
                          events=[{'rest': True, 'dur': 'e'}, n('C4', 'e'), n('D4', 'e'), n('E4', 'e'),
                                  n('G4', 'h'), sil('h'), sil('h')],
                          bars=2),
                     dict(cap='b) y entrar en el cuatro, que es de donde salen casi todas sus '
                              'frases · la nota larga cae en el uno del compás siguiente',
                          events=[sil('h'), sil('q'), n('E4'),
                                  n('G4', 'h'), n('F4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LOS CUATRO COMPASES DE ESPERA',
                 texto='La derecha no toca hasta el cuarto compás. Contar cuatro compases sin tocar '
                       'nada es más difícil de lo que parece: sin nada que hacer, la cabeza se '
                       'adelanta. Cuéntalos con la mano apoyada en las teclas, no en el regazo, y '
                       'en voz alta hasta que la entrada salga sola.'),
            dict(num=3, titulo='Las dos manos, con la melodía a contratiempo',
                 pista='andamio · muy despacio, y sin dejar de contar en voz alta',
                 sistemas=[
                     dict(cap='a) la izquierda en el uno y el tres, la derecha entre medias · si la '
                              'derecha se te pega al acorde, ve más lento',
                          events=[ac(('C3', 'E3', 'G3'), 'h'), ac(('C3', 'E3', 'G3'), 'e'),
                                  n('C4', 'e'), n('D4', 'e'), n('E4', 'e'),
                                  ac(('E3', 'G3', 'B3'), 'h'), n('G4', 'h')],
                          bars=2, manos='dobla', dos_pentagramas=True),
                     dict(cap='b) y con la entrada en el cuatro, que es la que más sale · la '
                              'izquierda no se mueve de su sitio pase lo que pase arriba',
                          events=[ac(('F2', 'A2', 'C3'), 'h'), ac(('F2', 'A2', 'C3'), 'q'),
                                  n('E4'), ac(('G2', 'B2', 'D3'), 'h'), n('G4'), n('F4')],
                          bars=2, show_time=False, manos='dobla', dos_pentagramas=True),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='What Was I Made For? · para casa',
            intro='Veinte minutos, y todos contando en voz alta. Sin contar, esta pieza no se '
                  'arregla.',
            bloques=[
                reto('Que ninguna entrada de la derecha se te pegue al acorde de la izquierda.',
                     'Toca la izquierda sola contando "un-y-dos-y-tres-y-cuatro-y", y canta la '
                     'melodía encima SIN tocarla hasta que sepas decir en qué sílaba entra cada '
                     'frase. Solo entonces la tocas.'),
                plan((5, 'La izquierda sola, contando en voz alta'),
                     (5, 'Cantar la melodía encima, sin tocarla'),
                     (6, 'La derecha sola, entrando donde toca'),
                     (4, 'Las dos juntas, de dos en dos compases')),
                escalera((50, 'la izquierda sola, en su sitio'),
                         (60, 'las dos manos, dos compases seguidos'),
                         (70, 'la primera página entera'),
                         (78, 'su velocidad'),
                         meta='♩ = 78, que es lo que pone tu partitura',
                         notas=['A 78 la melodía va a parecer que llega tarde. Es que llega tarde: '
                                'está escrita así.']),
                cifrado(['C', 'Em', 'F', 'Am', 'Dm', 'G'],
                        ['Escribe las tres notas de cada acorde, de grave a agudo.',
                         'Son los seis que tu partitura lleva impresos encima del pentagrama.'],
                        pista='dos de ellos comparten dos notas: cuando lo veas, ya no se te olvidan'),
                colorear([sil('q'), n('C4', 'e'), n('D4', 'e'), n('E4', 'h'),
                          sil('e'), n('G4', 'e'), n('F4'), n('E4', 'h')],
                         ['Los silencios, de rojo.',
                          'Las corcheas, de azul.',
                          'Las notas que caen en un golpe fuerte, de verde.'],
                         titulo='Colorea el ritmo',
                         pista='y luego cuéntalo en voz alta mirando los colores'),
                para_clase('La izquierda sola a ♩ = 78 y las cuatro primeras frases de la derecha '
                           'en su sitio. Si hay una entrada que se te resiste siempre, tráela '
                           'marcada: la contamos juntos y se acaba.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
