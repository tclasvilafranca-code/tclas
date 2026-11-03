# -*- coding: utf-8 -*-
"""The Beginner (Gurlitt, op. 211 nº 3) — pieza 4 de Martina (dueto). ADULTO exigente,
   tono de niña que empieza de cero.

   Lo comprobado sobre el PDF de su carpeta de Drive ("The Beginner, Le Début, Der
   Anfänger — 22 Melodic Studies, Piano 4-Hands", 1 página, vectorial, 206 ppp),
   medido con cabezas.medir a 250 ppp:

     - Detrás de la clave no hay nada: Do mayor. 3/4. Pone "Allegretto". 16 compases.
     - A cuatro manos. El PRIMO (arriba) lleva sus dos pentagramas en clave de sol y
       la derecha lleva un 8va encima de toda la línea; la izquierda toca lo mismo
       sin 8va. El SECONDO (abajo) lleva clave de sol y clave de fa.
     - Intensidad: mf al principio del Primo, con un regulador de apertura en el c. 1
       y uno de cierre en el c. 2; el Secondo empieza en p. Arcos de frase.
     - MEDIDO, Primo (alturas tal como están escritas, con el 8va encima):
       c. 1: Mi5 · Mi5 · Mi5 (negras)
       c. 2: Sol5 (blanca) · Fa5 (negra)
       c. 3: Mi5 (negra con puntillo) · Re5 (corchea) · Do5 (negra)
       c. 4: Re5 (blanca con puntillo)
       c. 5: Do5 · Do5 · Do5 (negras)
       c. 6: Do5 (negra con puntillo) · Mi5 (corchea) · Re5 (negra)
     - El Secondo, en cada compás: silencio de negra, una nota y un acorde
       de dos notas (dos negras) y, abajo, una blanca con puntillo.
     - Solo negras, blancas, corcheas y blancas con puntillo. Nada más corto que la corchea.
   Mismo archivo que la pieza 4 de Isaac y la 2 de Luisa: lo literal coincide y el
   andamio va por otros caminos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, reto, plan, a_cuatro_manos, contar, unir,
                      verdadero_falso, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: Primo, cc. 1-6 (alturas escritas, con el 8va encima)
C1 = [n('E5'), n('E5'), n('E5')]
C2 = [n('G5', 'h'), n('F5')]
C3 = [n('E5', 'q.'), n('D5', 'e'), n('C5')]
C4 = [n('D5', 'h.')]
C5 = [n('C5'), n('C5'), n('C5')]
C6 = [n('C5', 'q.'), n('E5', 'e'), n('D5')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=4, nivel='iniciación', slug='Beginner',
    formato='adulto',
    titulo_corto='The Beginner · Gurlitt', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'The Beginer le debut'),
    yt='https://www.youtube.com/results?search_query=gurlitt+op+211+the+beginner+piano+4+hands',

    ficha=dict(
        titulo='The Beginner',
        autor='Cornelius Gurlitt · op. 211 nº 3 · a cuatro manos · tu parte es el Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'Allegretto'), ('8va', 'Solo la derecha'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Los cc. 1-3 del Primo, y lo que toca el otro',
        pie_ritmos='Arriba, medido sobre tu partitura (tal como está escrito, con el 8va encima): '
                   'tres negras, una blanca y una negra con puntillo. Abajo, andamio: lo que hace el '
                   'Secondo.',
        armonia=dict(
            titulo='Un vals lento entre dos, con reguladores y un 8va',
            tarjetas=[
                ('EL 3/4', 'Un, dos, tres',
                 'Tres negras por compás, y un compás entero cabe en una blanca con puntillo. '
                 'Si en vez de contar tres cuentas cuatro, el compañero te dejará solo.'),
                ('EL 8VA', 'Solo la derecha',
                 'Encima del Primo hay un 8va con línea de puntos: la derecha suena una octava más '
                 'alto de lo escrito, y la izquierda toca lo mismo sin 8va.'),
                ('LOS REGULADORES', 'Mf, abre y cierra',
                 'Empieza en mf. En el c. 1 un regulador abre el sonido y en el c. 2 otro lo '
                 'cierra: el volumen se mueve dentro de cada pareja de compases.'),
                ('EL SECONDO', 'Silencio y acorde',
                 'Tu compañero toca en cada compás un silencio de negra, una nota y un '
                 'acorde, y debajo una blanca con puntillo. Empieza en p: tú, un escalón por '
                 'encima.'),
            ],
            pie='Una página, 16 compases y la melodía casi igual en los dos tramos. Es la pieza '
                'más corta del cuaderno: la dificultad es tocarla entre dos sin que se note.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-3 · medido', C1 + C2 + C3, OCRE, 'treble', None),
            ('SECONDO', 'andamio · silencio, nota y acorde',
             [sil('q'), n('B3'), ac(('D4', 'F4'))] * 2, AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: todas son teclas blancas.',
            'El compás es 3/4 y pone "Allegretto".',
            'Hay un 8va encima de la derecha del Primo, y de la izquierda no.',
            'Empieza en mf, con un regulador que abre y otro que cierra.',
            'El Secondo empieza en p.',
            'Solo hay negras, blancas, corcheas y blancas con puntillo.',
        ],
        reto='Contar tres y no cuatro, entre dos. Si uno de los dos se va al cuatro, la pieza '
             'se descuadra, y el que lo hace no lo nota.',
        truco='Cuenta "UN, dos, tres" en voz alta, con el pie. Si el compañero entra en el '
              'segundo golpe y tú lo oyes, es que cuentas igual que él.',
        sabias='Gurlitt fue profesor de piano en Hamburgo y escribió cientos de piezas cortas para '
               'sus alumnos. La serie op. 211 son 22 estudios melódicos a cuatro manos, para '
               'tocar un alumno con su profesor.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el Secondo hace de metrónomo suave y la melodía va por encima. '
                      'Cuando la toques, tienes que oír eso mismo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia solo la parte de arriba hasta que sale sin pensar, y después se junta con el '
              'compañero. Las dos primeras semanas el tempo lo marca el metrónomo, no el otro.',
        reglas=['CUENTA "UN, DOS, TRES" EN VOZ ALTA', 'EL 8VA SUENA UNA OCTAVA MÁS ALTO',
                'EL REGULADOR ABRE Y CIERRA'],
        bloques=[
            dict(num=1, titulo='Los dos primeros compases, con su regulador',
                 pista='cc. 1-2 · medidos sobre tu partitura · tal como está escrito, con el 8va '
                       'encima',
                 sistemas=[
                     dict(cap='a) tres negras, una blanca y una negra · mf, abre en el c. 1 y '
                              'cierra en el c. 2',
                          events=[dict(n('E5'), matiz='mf', cresc=3), n('E5'), n('E5'),
                                  dict(n('G5', 'h'), dim=2), n('F5')],
                          bars=2, time_sig=(3, 4), ottava=True),
                 ]),
            dict(num=2, titulo='La negra con puntillo y la corchea, c. 3',
                 pista='cc. 3-4 · medidos sobre tu partitura · uno y medio, medio y uno, y una '
                       'blanca con puntillo',
                 sistemas=[
                     dict(cap='a) la negra con puntillo dura uno y medio, la corchea completa '
                              'el golpe · la blanca con puntillo llena el compás',
                          events=C3 + C4, bars=2, time_sig=(3, 4), ottava=True),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA EN TRES',
                 texto='En 3/4 caben tres negras y el primer golpe pesa más: es un vals. Entre dos, '
                       'el riesgo es que cada uno cuente a su manera. Pónganse de acuerdo antes de '
                       'empezar: quién da la entrada, a qué velocidad y cuántos golpes de pie '
                       'antes de entrar.'),
            dict(num=3, titulo='El segundo tramo, cc. 5-6',
                 pista='cc. 5-6 · medidos sobre tu partitura · las mismas figuras sobre otra nota',
                 sistemas=[
                     dict(cap='a) tres Do seguidos, y después la negra con puntillo, la corchea y '
                              'la negra del c. 6',
                          events=C5 + C6, bars=2, time_sig=(3, 4), ottava=True),
                 ]),
            dict(num=4, titulo='Lo que toca tu compañero',
                 pista='andamio · el Secondo repite en cada compás: silencio, nota y acorde',
                 sistemas=[
                     dict(cap='a) un silencio de negra, una negra, y un acorde de dos notas · es '
                              'la parte que oirás mientras tocas la tuya',
                          events=[sil('q'), n('C4'), ac(('E4', 'G4')),
                                  sil('q'), n('D4'), ac(('F4', 'A4'))],
                          bars=2, time_sig=(3, 4)),
                 ]),
            dict(num=5, titulo='Las dos manos juntas, a la octava',
                 pista='andamio · la derecha y la izquierda tocan lo mismo; aquí, una octava más '
                       'grave que lo escrito',
                 sistemas=[
                     dict(cap='a) tres acordes de octava y una blanca · un solo sonido, no dos '
                              'golpecitos',
                          events=[ac(('D4', 'D5')), ac(('D4', 'D5')), ac(('D4', 'D5')),
                                  ac(('F4', 'F5'), 'h'), ac(('E4', 'E5'))],
                          bars=2, time_sig=(3, 4)),
                 ]),
        ] + bloques_extra('Do mayor', 4, 'E4', 'C3',
                          'el compás de tres, y las dos manos a la misma velocidad',
                          desde=6, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='The Beginner · para casa',
            intro='Quince minutos al día, y dos días con tu compañero. Es una pieza corta: el '
                  'objetivo es que sea limpia y que contéis lo mismo.',
            bloques=[
                reto('Tocar los cc. 1-8 contando tres, tres veces seguidas, sin que la mano se '
                     'vaya al cuatro.',
                     'Cuenta en voz alta "UN, dos, tres" y apunta cuántas veces lo consigues '
                     'seguidas. Si una vez cuentas cuatro, vuelves a cero.'),
                plan((4, 'La derecha sola, cc. 1-8, contando en voz alta'),
                     (3, 'La izquierda sola, la misma melodía sin el 8va'),
                     (4, 'Las dos manos, cc. 1-8, con metrónomo'),
                     (4, 'Con el compañero, hasta la mitad de la pieza')),
                a_cuatro_manos('El Secondo marca el pulso en el segundo golpe, no en el primero. '
                               'Acordad quién da la entrada, a qué número de metrónomo y cuántos '
                               'golpes de pie hay antes de empezar.'),
                contar(C5 + C6,
                       ['¿Cuántas negras hay?', '¿Cuántas corcheas hay?',
                        '¿Cuántas negras con puntillo hay?'],
                       titulo='Cuenta sobre los cc. 5 y 6',
                       pista='son dos compases del Primo, medidos'),
                unir([('3/4', 'tres negras por compás'),
                      ('Allegretto', 'alegre, pero sin correr'),
                      ('8va', 'suena una octava más alto de lo escrito'),
                      ('Blanca con puntillo', 'tres golpes: un compás entero')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                verdadero_falso([
                    'Detrás de la clave no hay nada.',
                    'La partitura pone "Allegretto".',
                    'Es una pieza en 4/4.',
                    'Solo la derecha del Primo lleva un 8va encima.',
                    'La izquierda toca una melodía distinta de la derecha.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                para_clase('Los cc. 1-8 con las dos manos, contando tres, y si con el compañero '
                           'habéis acordado la entrada. Traed el metrónomo: ajustamos el número '
                           'entre los dos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
