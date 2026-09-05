# -*- coding: utf-8 -*-
"""Jingle Bell Rock — pieza 16 de Eduard. Formato ADULTO.

   Medido sobre el PDF de su carpeta (vectorial, dos pentagramas por sistema):

     - 4/4 y detras de la clave no hay nada.
     - Encima del pentagrama pone **Swing**. Debajo va la **letra**, silaba a
       silaba, y hay **digitacion impresa** (5, 2, 1...).
     - Medido a 300 ppp:

         DERECHA    c. 1   Do5 · Do5 · Do5 · Si4 · Si4 · Si4
                           corchea, corchea, negra · corchea, corchea, negra
                    c. 2   La4 · Si4 · La4 · Mi4      cuatro corcheas, una sola
                                                      barra
                           y el Mi4 sigue sonando en una BLANCA ligada
         IZQUIERDA  c. 1   Do3 · Sol2                 dos blancas
                    c. 2   Do3 · Sol2                 igual

     - El c. 2 se sumo para comprobar la ligadura: cuatro corcheas son dos
       tiempos, y la blanca ligada son los otros dos. Cuatro justos. Si la
       ultima corchea no estuviera ligada faltaria medio tiempo.

   POR QUE VA AQUI Y NO ANTES. Es la primera pieza del cuaderno donde la
   derecha lleva cuatro corcheas seguidas debajo de una sola barra, y ademas
   trae una ligadura de union en la melodia. La izquierda, en cambio, es la
   misma de *Heart and Soul* pero mas simple: dos notas por compas que no
   cambian. Justo lo que hace falta para poder mirar solo hacia arriba.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, corch, plan, escalera, nombres, unir, inventa,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 de la DERECHA, medido. Cita literal.
ARRANQUE = (corch(['C5', 'C5']) + [n('C5')] + corch(['B4', 'B4']) + [n('B4')])

# Los compases 1 y 2 de la IZQUIERDA, medidos.
BAJO = [n('C3', 'h'), n('G2', 'h'), n('C3', 'h'), n('G2', 'h')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=16, nivel='iniciación',
    slug='JingleBellRock', formato='adulto',
    titulo_corto='Jingle Bell Rock', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Jingle Bell Rock.pdf'),
    yt='https://www.youtube.com/results?search_query=jingle+bell+rock+piano+easy',

    ficha=dict(
        titulo='Jingle Bell Rock',
        autor='Joe Beal y Jim Boothe · arreglo fácil',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Swing'), ('Manos', 'Las dos, distintas'),
               ('Extras', 'Letra y dedos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, el compás 1 de la derecha. Abajo, la izquierda '
                   'de los compases 1 y 2, que son iguales.',
        armonia=dict(
            titulo='Corcheas arriba, dos notas abajo',
            tarjetas=[
                ('CORTA, CORTA, LARGA', 'El motivo',
                 'Dos corcheas y una negra, y otra vez lo mismo un escalón más abajo. Todo el '
                 'compás 1 son esas seis notas, y la palabra las dice: "jin-gle bell".'),
                ('LA LIGADURA', 'En el compás 2',
                 'La última corchea del compás 2 está unida a una blanca: se toca una vez y suena '
                 'dos tiempos y medio. Si la vuelves a tocar, el compás se descoloca.'),
                ('LA IZQUIERDA', 'Do y Sol',
                 'Dos notas largas por compás, y las mismas en los dos primeros compases. No hay '
                 'nada más fácil de aprender de memoria.'),
                ('SWING', 'Cómo se toca',
                 'Los pares de corcheas se hacen desiguales: la primera un poco más larga. No está '
                 'escrito en el papel, se aprende de oído.'),
            ],
            pie='Fíjate en que el dibujo del compás 1 se repite entero un escalón más abajo. Media '
                'canción funciona así: aprender el gesto una vez y luego moverlo de sitio.',
        ),
        ritmos=[
            ('LA DERECHA', 'el compás 1, medido · corta, corta, larga · dos veces',
             ARRANQUE, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · dos notas largas por compás',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Compás de 4/4, y no hay ni un sostenido ni un bemol.',
            'Encima del pentagrama pone "Swing".',
            'El compás 1 son seis notas: dos cortas y una larga, dos veces.',
            'En el compás 2 hay cuatro corcheas bajo una sola barra.',
            'Hay una ligadura: la última corchea sigue sonando en una blanca.',
            'Debajo va la letra y encima hay números de dedo.',
        ],
        reto='Las cuatro corcheas seguidas del compás 2. Cuatro notas en dos tiempos parece poco, '
             'pero en cuanto se juntan cuatro iguales la mano tiende a acelerar en la última.',
        truco='Toca las cuatro corcheas con el metrónomo puesto en dos golpes por compás, no en '
              'cuatro. Con menos referencias te obligas a repartir tú el tiempo, y las cuatro '
              'salen parejas mucho antes.',
        sabias='Se grabó en 1957, cuando el rock and roll llevaba dos años existiendo, y fue de las '
               'primeras canciones navideñas que sonaron a música moderna en vez de a villancico. '
               'Bobby Helms la cantó con veinte años y vivió de ella el resto de su vida.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cómo las parejas de corcheas suenan desiguales, largas-cortas. Eso '
                      'es el swing, y no está escrito en ninguna parte.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda se aprende en un minuto. Todo el trabajo está arriba: en repartir bien '
              'las corcheas y en no volver a tocar la nota ligada.',
        reglas=['LA IZQUIERDA, DOS NOTAS Y YA', 'CUATRO CORCHEAS = DOS TIEMPOS',
                'LA NOTA LIGADA NO SE REPITE'],
        bloques=[
            dict(num=1, titulo='El motivo: corta, corta, larga',
                 pista='c. 1 · medido en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) primero solo la primera mitad, cuatro veces seguidas',
                          events=corch(['C5', 'C5']) + [n('C5')] + corch(['C5', 'C5']) + [n('C5')] +
                                 corch(['C5', 'C5']) + [n('C5')] + corch(['C5', 'C5']) + [n('C5')],
                          bars=2),
                     dict(cap='b) el mismo dibujo un escalón más abajo, que es la otra mitad del '
                              'compás 1 · cuatro veces',
                          events=corch(['B4', 'B4']) + [n('B4')] + corch(['B4', 'B4']) + [n('B4')] +
                                 corch(['B4', 'B4']) + [n('B4')] + corch(['B4', 'B4']) + [n('B4')],
                          bars=2, show_time=False),
                     dict(cap='c) y las dos mitades enlazadas, que es el compás 1 entero, dos veces',
                          events=corch(['C5', 'C5']) + [n('C5')] + corch(['B4', 'B4']) + [n('B4')] +
                                 corch(['C5', 'C5']) + [n('C5')] + corch(['B4', 'B4']) + [n('B4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UNA LIGADURA DE UNIÓN',
                 texto='Es un arco que une DOS NOTAS DE LA MISMA ALTURA. No quiere decir "tócalas '
                       'suave" ni "no cortes": quiere decir que son una sola nota, y que la segunda '
                       'NO se toca. Se aprieta la tecla una vez y se aguanta el dedo lo que suman '
                       'las dos. Aquí sirve para escribir una nota que dura dos tiempos y medio, '
                       'algo que con una sola figura no se puede escribir.'),
            dict(num=2, titulo='Las cuatro corcheas y la nota ligada',
                 pista='c. 2 · medido en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) las cuatro corcheas solas · cuenta "un-y-dos-y" en voz alta',
                          events=corch(['A4', 'B4', 'A4', 'E4'], 4) + [n('E4', 'h')],
                          bars=1),
                     dict(cap='b) y con la ligadura: la última corchea se aguanta, no se repite',
                          events=corch(['A4', 'B4', 'A4'], 3) +
                                 [dict(n('E4', 'e'), lig=1), n('E4', 'h')],
                          bars=1, show_time=False),
                     dict(cap='c) y enlazado con el compás 1, que es como se toca de verdad',
                          events=corch(['C5', 'C5']) + [n('C5')] + corch(['B4', 'B4']) + [n('B4')] +
                                 corch(['A4', 'B4', 'A4'], 3) +
                                 [dict(n('E4', 'e'), lig=1), n('E4', 'h')],
                          bars=2, show_time=False),
                     dict(cap='d) y con la nota larga escrita entera, para oír cuánto tiene que durar',
                          events=corch(['A4', 'B4', 'A4', 'E4'], 4) + [n('E4', 'h'),
                                  n('E4', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda, y las dos manos',
                 pista='cc. 1–2 · medidos · abajo no cambia nada en dos compases',
                 sistemas=[
                     dict(cap='a) la izquierda sola, cuatro compases seguidos, sin mirarla',
                          events=[n('C3', 'h'), n('G2', 'h'), n('C3', 'h'), n('G2', 'h'),
                                  n('C3', 'h'), n('G2', 'h'), n('C3', 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y las dos manos: el compás 1 dos veces y después el 2',
                          events=[ac(('C3', 'C5'), 'e'), ac(('C5',), 'e'), ac(('C5',)),
                                  ac(('G2', 'B4'), 'e'), ac(('B4',), 'e'), ac(('B4',)),
                                  ac(('C3', 'C5'), 'e'), ac(('C5',), 'e'), ac(('C5',)),
                                  ac(('G2', 'B4'), 'e'), ac(('B4',), 'e'), ac(('B4',)),
                                  ac(('C3', 'A4'), 'e'), ac(('B4',), 'e'), ac(('A4',), 'e'),
                                  ac(('E4',), 'e'), ac(('G2', 'E4'), 'h')],
                          bars=3, manos='sostiene', show_time=False),
                     dict(cap='d) y solo los cambios: la primera nota de cada mitad, para que las '
                              'dos manos caigan juntas',
                          events=[ac(('C3', 'C5'), 'h'), ac(('G2', 'B4'), 'h'),
                                  ac(('C3', 'A4'), 'h'), ac(('G2', 'E4'), 'h'),
                                  ac(('C3', 'C5'), 'w')],
                          bars=3, manos='sostiene', show_time=False),
                     dict(cap='c) y una vez más, empezando por la mitad grave del compás 1',
                          events=[ac(('G2', 'B4'), 'e'), ac(('B4',), 'e'), ac(('B4',)),
                                  ac(('C3', 'C5'), 'e'), ac(('C5',), 'e'), ac(('C5',)),
                                  ac(('C3', 'A4'), 'e'), ac(('B4',), 'e'), ac(('A4',), 'e'),
                                  ac(('E4',), 'e'), ac(('G2', 'E4'), 'h')],
                          bars=2, manos='sostiene', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Jingle Bell Rock · para casa',
            intro='Quince minutos al día. La izquierda te la sabes el primer día: dedícale el resto '
                  'de la semana a que las corcheas de arriba salgan parejas.',
            bloques=[
                plan((3, 'La izquierda sola, Do y Sol, sin mirar'),
                     (4, 'El motivo corta-corta-larga, en las dos alturas'),
                     (4, 'Las cuatro corcheas del compás 2, contando en corcheas'),
                     (4, 'Los dos primeros compases con las dos manos')),
                escalera((66, 'la derecha sola, los dos primeros compases'),
                         (84, 'las dos manos, los dos primeros compases'),
                         (100, 'la primera línea entera, sin parar'),
                         meta='la primera línea con las dos manos · tu partitura no trae número de '
                              'metrónomo, estos son de trabajo',
                         notas=['Con el swing, el metrónomo marca los golpes, no las corcheas.']),
                nombres(['C5', 'B4', 'A4', 'E4', 'C3', 'G2'],
                        titulo='Los nombres, con las dos claves mezcladas',
                        pista='las cuatro primeras en clave de sol y las dos últimas en clave de fa'),
                unir([('Ligadura de unión', 'la segunda nota no se toca'),
                      ('Corchea', 'medio tiempo'),
                      ('Blanca', 'dos tiempos'),
                      ('Swing', 'las parejas de corcheas, desiguales'),
                      ('4/4', 'cuatro golpes por compás')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cinco están en tu partitura de esta semana'),
                inventa(['cuatro tiempos en total', 'que lleve cuatro corcheas seguidas',
                         'que acabe en una nota larga'],
                        (4, 4),
                        titulo='Inventa tú un compás para la derecha',
                        pista='usa solo las notas de la canción: Do, Si, La y Mi'),
                para_clase('Los dos primeros compases con las dos manos. Y dime si la nota ligada '
                           'te sale sonando dos veces: es lo más normal del mundo y se arregla en '
                           'un minuto.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 77, 'C5', 'C3',
    'cuatro corcheas seguidas que tienen que salir parejas',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
