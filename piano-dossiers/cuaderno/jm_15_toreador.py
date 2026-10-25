# -*- coding: utf-8 -*-
"""Toreador, de Carmen — pieza 15 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Georges Bizet, arreglo
   de Gilbert DeBenedetti, "Level Four", 1 página):

     - FA MAYOR: un bemol detrás de la clave, como Deck the Halls. Todos los
       Si van a la tecla negra.
     - El compás se escribe con una C, que es 4/4. Pone "March time".
     - Es "LEVEL FOUR": el escalón más alto de este arreglista en todo el
       cuaderno. America era Level Two y Grandfather's Clock, Level Three.
     - La digitación viene impresa, y la melodía arranca con CORCHEA CON
       PUNTILLO Y SEMICORCHEA, la figura de marcha. Durante meses este dosier
       decía "negra con puntillo y corchea", que es el mismo gesto al doble
       de lento y no es lo que hay impreso: el c. 1 son negra, corchea con
       puntillo, semicorchea, negra y negra, y la cuenta cierra en cuatro
       tiempos solo así (1 + 0,75 + 0,25 + 1 + 1). Medido a 300 ppp sobre el
       PDF, alturas incluidas: Do5 · Re5 · Do5 · La4 · La4.

   Lo que NO se cita nota a nota: el material va como ANDAMIO en Fa mayor y
   remite a la partitura.

   Es la última pieza antes de los cuatro retos del final del curso, y está
   aquí a propósito: sirve de prueba de que el nivel ha subido de verdad.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloque_puntillo, bloques_extra
from jm_comun import (n, ac, sil, objetivo, plan, ordenar, contar, teclado,
                      para_clase, escalera)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=15, nivel='iniciación',
    slug='Toreador', formato='adulto',
    titulo_corto='Toreador · Carmen', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'Toreador. Bizet'),
    yt='https://www.youtube.com/results?search_query=toreador+song+carmen+piano+easy',

    ficha=dict(
        titulo='Toreador',
        autor='Georges Bizet · de la ópera Carmen · arr. Gilbert DeBenedetti · Level Four',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', 'C (4/4)'),
               ('Carácter', 'March time'), ('Nivel', 'Level Four'),
               ('Páginas', 'Una')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='La derecha es el c. 1 medido sobre tu partitura, nota a nota. La izquierda va '
                   'como andamio en Fa mayor. Los Si, todos a la tecla negra.',
        armonia=dict(
            titulo='La prueba de que el nivel ha subido',
            tarjetas=[
                ('LEVEL FOUR', 'Dos escalones',
                 'Del mismo arreglista tienes America (Level Two) y Grandfather\'s Clock (Level '
                 'Three). Esta es dos escalones por encima de la segunda pieza del cuaderno.'),
                ('LA ARMADURA', 'Ya conocida',
                 'Fa mayor, la misma que Deck the Halls. Un bemol, y todos los Si a la negra. Eso ya '
                 'no es trabajo nuevo.'),
                ('EL RITMO', 'De marcha',
                 'Corchea con puntillo y SEMICORCHEA, una y otra vez. Larga y corta, muy juntas: eso '
                 'es lo que suena a desfile.'),
                ('MARCH TIME', 'Ni rápido ni lento',
                 'A paso de marcha: firme y regular. No es una indicación de velocidad, es de '
                 'carácter.'),
            ],
            pie='Compárala con America, la segunda del cuaderno: misma editorial, mismo arreglista, y '
                'dos escalones de diferencia. Si esta te sale, el curso ha hecho lo que tenía que '
                'hacer.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el ritmo de marcha, con SEMICORCHEA',
             [n('F4'), n('F4', 'e.'), n('F4', 's'), n('F4'), n('F4')],
             OCRE, 'treble', FA),
            ('MANO IZQUIERDA', 'firme, marcando el paso · andamio',
             [ac(('F2', 'C3'), 'h'), ac(('C3', 'F3'), 'h')], AZUL, 'bass', FA),
        ],
        especial=[
            'Hay UN bemol detrás de la clave: todos los Si van a la tecla negra.',
            'El compás se escribe con una C, que quiere decir 4/4.',
            'Pone "March time": a paso de marcha, firme y regular.',
            'La melodía va en corchea con puntillo y semicorchea casi todo el rato: la corta es la '
            'nota más rápida de toda la pieza.',
            'La digitación viene impresa.',
            'El arreglista la marca como Level Four, el nivel más alto suyo de todo tu cuaderno.',
        ],
        reto='Que el ritmo de marcha no se ablande. La corchea con puntillo tiende a acortarse y la '
             'semicorchea a adelantarse, y en cuanto eso pasa deja de ser una marcha.',
        truco='Marca el paso con el pie mientras tocas: pie abajo en el uno y en el tres, y la '
              'semicorchea cae justo antes de que el pie vuelva a bajar. Suena a truco de banda de pueblo y es '
              'exactamente lo que hace que una marcha suene a marcha.',
        sabias='Bizet la escribió a disgusto: le pidieron un número pegadizo para el torero y él lo '
               'llamó "porquería", pero lo entregó porque hacía falta. Es, con diferencia, lo más '
               'conocido que compuso. Murió tres meses después del estreno, convencido de que Carmen '
               'había sido un fracaso.',
        qr=dict(titulo='Escúchala',
                texto='Escucha una versión de orquesta y fíjate en el pulso: no acelera ni un poco en '
                      'toda la pieza. Eso es "March time".'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La tonalidad la conoces y el gesto largo-corto también: salió en America, en la '
              'semana 2. Pero allí era negra con puntillo y corchea, y aquí es la mitad de largo: '
              'corchea con puntillo y SEMICORCHEA. Mismo dibujo, el doble de rápido. Trabaja las '
              'manos por separado y júntalas al final.',
        reglas=['LOS SI, EN LA TECLA NEGRA', 'LA LARGA DURA LO QUE DURA',
                'EL PULSO NO SE MUEVE'],
        bloques=[
            dict(num=1, titulo='El ritmo de marcha, sin notas difíciles',
                 pista='medido sobre tu c. 1 · corchea con puntillo y semicorchea',
                 sistemas=[
                     dict(cap='a) las cinco notas del c. 1, todas iguales, para colocarlas · '
                              'Do · Re · Do · La · La',
                          events=[n('C5'), n('D5'), n('C5'), n('A4'), n('A4', 'w')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y ahora con su ritmo de verdad · la larga lleva puntillo y la '
                              'corta es una SEMICORCHEA, pegada a la siguiente',
                          events=[n('C5'), n('D5', 'e.'), n('C5', 's'), n('A4'), n('A4')],
                          bars=1, key_sig=FA, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: el paso', clef='bass',
                 pista='andamio en Fa mayor · firme, y sin acelerar nunca',
                 sistemas=[
                     dict(cap='a) dos apoyos por compás, iguales de firmes',
                          events=[ac(('F2', 'C3'), 'h'), ac(('C3', 'F3'), 'h'),
                                  ac(('Bb2', 'F3'), 'h'), ac(('C3', 'G3'), 'h')],
                          bars=2, clef='bass', key_sig=FA),
                     dict(cap='b) y cambiando de acorde sin que el paso se note · el pulso manda',
                          events=[ac(('F2', 'C3'), 'h'), ac(('C3', 'F3'), 'h'),
                                  ac(('F2', 'C3'), 'h'), ac(('Bb2', 'F3'), 'h'),
                                  ac(('C3', 'G3'), 'h'), ac(('F2', 'C3'), 'h')],
                          bars=3, clef='bass', key_sig=FA, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='COMPÁRALA CON LA PIEZA 2',
                 texto='Coge la partitura de America y ponla al lado de esta. Mismo arreglista, misma '
                       'editorial, y dos niveles de diferencia. Mira qué ha cambiado: más notas por '
                       'compás, las dos manos ocupadas, un ritmo que no se para. Ver eso escrito, en '
                       'papel, vale más que cualquier cosa que te pueda decir nadie sobre tu progreso.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio · despacio, con el pie marcando el paso',
                 sistemas=[
                     dict(cap='a) la derecha con su marcha encima del paso de la izquierda',
                          events=[n('C5'), n('D5', 'e.'), n('C5', 's'), n('A4'), n('A4'),
                                  n('C5', 'h'), n('F4', 'h')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · el paso no cambia porque '
                              'la derecha se complique',
                          events=[ac(('F2', 'C3'), 'h'), ac(('C3', 'F3'), 'h'),
                                  ac(('F2', 'C3'), 'h'), ac(('C3', 'F3'), 'h')],
                          bars=2, clef='bass', key_sig=FA, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Toreador · para casa',
            intro='Veinte minutos al día. Y un día de esta semana, saca la partitura de America.',
            bloques=[
                objetivo('Dos compases con las dos manos, a paso de marcha, sin que la corchea con '
                         'puntillo se acorte ni una vez.'),
                plan((5, 'La melodía en negras, colocando las notas'),
                     (5, 'La misma con el puntillo, marcando el paso con el pie'),
                     (5, 'La izquierda sola: dos apoyos por compás, firmes'),
                     (5, 'Dos compases con las dos manos')),
                ordenar(['Las dos manos, dos compases a paso de marcha.',
                         'La melodía en negras, sin el puntillo.',
                         'La izquierda sola, marcando el paso.',
                         'La melodía con el puntillo puesto.'],
                        titulo='Pon los pasos en el orden bueno',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                escalera((60, 'la melodía en negras, colocando las notas'),
                         (80, 'las dos manos, dos compases seguidos'),
                         (100, 'a paso de marcha, que es lo que pide'),
                         meta='que suene a marcha y no a ejercicio · tu partitura pone "March time" '
                              'pero no trae número de metrónomo',
                         notas=['Si la corchea con puntillo se te aplana al subir, baja un escalón.']),
                teclado({3: 1, 5: 2, 0: 3, 6: 4},
                        ['Escribe el nombre de las cuatro teclas blancas marcadas.',
                         'Y pinta la negra que hay a la izquierda de la número 4: ese es el Si bemol.'],
                        titulo='En el teclado',
                        pista='la misma tonalidad que Deck the Halls'),
                para_clase('Dos compases a paso de marcha, y la partitura de America al lado para '
                           'mirar juntos qué ha cambiado en quince semanas.'),
            ],
        ),
    ],
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Fa mayor', 38, 'F4', 'F2',
    'el Si bemol, antes de pelearse con el ritmo',
    desde=5, time_sig=(4, 4)) + [
    # `lento=True` escribia el gesto como negra con puntillo + corchea "porque
    # el escalon 2 no tiene la semicorchea". Manda la partitura: la suya la
    # trae, y ver el apoyo en una figura distinta de la impresa era peor que
    # no verlo.
    bloque_puntillo('Fa mayor', 4, 'F4', 'el ritmo con puntillo de la marcha',
                    time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
