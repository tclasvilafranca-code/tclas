# -*- coding: utf-8 -*-
"""White Christmas (Irving Berlin) — pieza 9 de Martina. ADULTO exigente, con cifrado.

   NAVIDAD. Lo comprobado sobre el PDF de su carpeta de Drive ("Blanca Navidad",
   Musescore, 1 página, vectorial, 31 compases), a 250-300 ppp:

     - Detrás de la clave no hay nada: DO MAYOR. 4/4. No trae tempo ni
       intensidad. La letra va impresa debajo de la melodía.
     - Trae el CIFRADO IMPRESO encima del pentagrama, con la menor escrita "D-":
       C, D-, G, F, F-, C7, G7 y F7 (cc. 1-7: C · C · D- · G · F · G · C).
     - La izquierda toca acordes de tres notas en redonda, uno por compás.
     - MEDIDO, mano derecha:
       c. 1: Mi4 (redonda)
       c. 2: Fa4 · Mi4 · Mi♭4 · Mi4 con becuadro (negras)
       c. 3: La4 (redonda)
       c. 4: Fa♯4 (negra) y Sol4 (blanca con puntillo)
       c. 5: silencio de negra y La4 · Si4 · Do5 (negras)
       c. 6: Re5 · Do5 · Si4 · La4 (negras)
       c. 7: Sol4 (redonda)
     - Nada más corto que la negra: solo negras, blancas, blancas con puntillo y redondas.
   El cifrado se estudia con las letras: la partitura las trae.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, plan, escalera, cifrado, unir, nombres,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: cc. 1-2
C1 = [n('E4', 'w')]
C2 = [n('F4'), n('E4'), n('Eb4'), n('En4')]
# MEDIDO: cc. 3-7
C3 = [n('A4', 'w')]
C4 = [n('F#4'), n('G4', 'h.')]
C5 = [sil('q'), n('A4'), n('B4'), n('C5')]
C6 = [n('D5'), n('C5'), n('B4'), n('A4')]
C7 = [n('G4', 'w')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=9, nivel='iniciación', slug='WhiteChristmas',
    formato='adulto',
    titulo_corto='White Christmas', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'Blanca Navidad'),
    yt='https://www.youtube.com/results?search_query=white+christmas+irving+berlin+piano+easy',

    ficha=dict(
        titulo='White Christmas',
        autor='Irving Berlin · versión de Musescore · NAVIDAD',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Una')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: una redonda y las cuatro negras del giro '
                   'cromático. Abajo, andamio: la izquierda toca un acorde de tres notas por '
                   'compás.',
        armonia=dict(
            titulo='Una melodía cantable con un giro de bemol y becuadro',
            tarjetas=[
                ('LA MELODÍA', 'Largas y negras',
                 'Casi todo son redondas y negras: es una melodía hecha para cantarse. El '
                 'trabajo no está en la mano, está en respirar la frase.'),
                ('EL GIRO', 'Mi, Fa, Mi, Mi♭, Mi',
                 'En el c. 2 aparecen un Mi♭ y un Mi con becuadro seguidos: es la nota que da '
                 'el tono de Navidad. El becuadro anula el bemol.'),
                ('EL CIFRADO', 'C · D- · G · F…',
                 'Tu partitura trae las letras encima: C, D-, G, F, F-, C7, G7 y F7. La "-" es '
                 'menor: D- es Re menor. Con las letras se acompaña sin leer.'),
                ('LA LETRA', 'Debajo de las notas',
                 'La letra va impresa y ayuda a ver dónde respira cada frase: una sílaba, una '
                 'nota, casi siempre.'),
            ],
            pie='Son 31 compases en una sola página. Con las ocho letras del cifrado puedes '
                'acompañarla sin leer la clave de fa.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1 y 2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · un acorde por compás',
             [ac(('C3', 'G3', 'E4'), 'w'), ac(('C3', 'G3', 'E4'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: Do mayor. El compás es 4/4.',
            'No trae tempo ni intensidad. La letra va impresa debajo de las notas.',
            'Encima del pentagrama va el cifrado: C, D-, G, F, F-, C7, G7 y F7.',
            'La menor se escribe con un guion: D- es Re menor.',
            'El c. 2 trae un Mi♭ y un Mi con becuadro, seguidos.',
            'La izquierda toca un acorde de tres notas en redonda por compás.',
        ],
        reto='Cantar la frase mientras la tocas. Con una melodía tan larga y tan quieta, lo '
             'difícil es que no suene a ejercicio: tiene que sonar a canción.',
        truco='Canta la letra en voz baja con la derecha y mira cada letra del cifrado antes de '
              'llegar al compás. Los acordes se anticipan: el ojo siempre un compás por '
              'delante.',
        sabias='White Christmas la escribió Irving Berlin y la cantó Bing Crosby en 1942. Se '
               'considera el disco sencillo más vendido de la historia: más de cincuenta '
               'millones de copias.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo Crosby respira entre frases: cada frase de tu partitura '
                      'acaba en una redonda y esa redonda es el sitio para tomar aire.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La melodía va despacio: se estudia cantando. Primero las letras de acorde con la '
              'izquierda, después la derecha con la letra, y al final las dos juntas.',
        reglas=['LAS LETRAS ANTES QUE LAS NOTAS', 'CANTAR LA FRASE', 'EL BEMOL Y SU BECUADRO'],
        bloques=[
            dict(num=1, titulo='El giro del c. 2: Fa, Mi, Mi♭, Mi',
                 pista='c. 2 · medido sobre tu partitura · el bemol y el becuadro, uno detrás del '
                       'otro',
                 sistemas=[
                     dict(cap='a) cuatro negras seguidas · el Mi♭ es la tecla negra de abajo y el '
                              'Mi con becuadro vuelve a la blanca',
                          events=C2, bars=1),
                     dict(cap='b) el mismo giro una nota más arriba · andamio · Fa♯ en lugar del '
                              'bemol, para ver que el signo cambia la dirección',
                          events=[n('A4'), n('G#4'), n('G4'), n('Gn4')], bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='Los cc. 3 y 4: la nota larga y el Fa♯',
                 pista='cc. 3-4 · medidos sobre tu partitura · una redonda, una negra y una '
                       'blanca con puntillo',
                 sistemas=[
                     dict(cap='a) La de redonda, y después Fa♯ de negra y Sol de blanca con '
                              'puntillo · el Fa♯ está escrito delante de la nota',
                          events=C3 + C4, bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ESTUDIA CANTANDO',
                 texto='Una melodía de redondas y negras no tiene ritmo difícil, tiene aire. Si '
                       'la tocas sin cantar, las notas largas se cortan antes de tiempo. Si la '
                       'cantas, el cuerpo te pide mantenerlas: es la mejor manera de contar la '
                       'duración sin contar.'),
            dict(num=3, titulo='Los cc. 5-6: subir y bajar por grados',
                 pista='cc. 5-6 · medidos sobre tu partitura · cuatro negras que suben y cuatro '
                       'que bajan',
                 sistemas=[
                     dict(cap='a) silencio de negra y La, Si, Do · después Re, Do, Si, La · es '
                              'una escala corta, y el silencio del principio se cuenta',
                          events=C5 + C6, bars=2),
                 ]),
            dict(num=4, titulo='Los acordes del cifrado: C, Dm, G y F',
                 pista='andamio sobre las letras IMPRESAS en tu partitura · la "-" es menor',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) uno por compás, en la posición más cerca del anterior · Do, '
                              'Re menor, Sol y Fa',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('A2', 'D3', 'F3'), 'w'),
                                  ac(('G2', 'B2', 'D3'), 'w'), ac(('A2', 'C3', 'F3'), 'w')],
                          bars=4, clef='bass'),
                 ]),
            dict(num=5, titulo='Las dos manos: los cc. 5-6 con el cifrado',
                 pista='la derecha es la de los cc. 5-6 MEDIDA sobre tu partitura · los acordes '
                       'son andamio sobre las letras F y G',
                 sistemas=[
                     dict(cap='a) la derecha medida sobre tu partitura (cc. 5-6) y la izquierda '
                              'sosteniendo un acorde por compás · F y G',
                          events=[ac(('F2', 'A2', 'C3'), 'q'), ac(('A4',)), ac(('B4',)), ac(('C5',)),
                                  ac(('G2', 'B2', 'D3', 'D5'), 'q'), ac(('C5',)), ac(('B4',)),
                                  ac(('A4',))],
                          bars=2, manos='sostiene'),
                 ]),
        ] + bloques_extra('Do mayor', 9, 'E4', 'C3',
                          'una melodía de notas largas: se cuenta cantando',
                          desde=6, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='White Christmas · para casa',
            intro='Diez o quince minutos al día. Es una pieza de Navidad: se estudia cantando, y '
                  'se toca sonriendo.',
            bloques=[
                plan((4, 'Las letras del cifrado con la izquierda, diciéndolas en voz alta'),
                     (4, 'La derecha sola, cc. 1-7, cantando'),
                     (4, 'Los cc. 1-4 con las dos manos'),
                     (4, 'Los cc. 1-8 de una vez, sin parar')),
                escalera((50, 'la derecha sola, cc. 1-4'),
                         (60, 'las dos manos, cc. 1-4'),
                         (72, 'los cc. 1-8'),
                         (84, 'los 31 compases'),
                         meta='Tu partitura no trae número de metrónomo: la meta la eliges tú y la '
                              'apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                cifrado(['C', 'Dm', 'G', 'F', 'Fm', 'C7', 'G7', 'F7'],
                        ['Escribe las tres notas de cada uno de los cuatro primeros, de grave a '
                         'agudo.',
                         'Rodea los que llevan un 7 y di qué notas tienen de más.',
                         'Recuerda que en tu partitura Dm y Fm se escriben con un guion: D- y F-.'],
                        titulo='Las letras de tu partitura',
                        pista='están impresas encima del pentagrama y se repiten en toda la '
                              'canción'),
                unir([('Redonda', 'cuatro golpes seguidos, una sola vez'),
                      ('Negra', 'un golpe del pie'),
                      ('Becuadro', 'anula el bemol: la nota vuelve a ser blanca'),
                      ('Guion en el cifrado', 'D- quiere decir Re menor')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                nombres(['F4', 'E4', 'Eb4', 'A4', 'G4', 'B4', 'C5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='las cuatro primeras son las del giro del c. 2 de tu partitura · la '
                              'tercera lleva un bemol'),
                para_clase('Los cc. 1-8 cantando y con las dos manos. Y dime qué letra del cifrado '
                           'se te olvida más: la repasamos juntos. Si el Mi♭ del c. 2 se te '
                           'escapa, tráelo marcado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
