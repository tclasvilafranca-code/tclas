# -*- coding: utf-8 -*-
"""Heart and Soul — pieza 10 de Eduard. Formato ADULTO.

   Medido sobre el PDF de su carpeta (vectorial, dos pentagramas por sistema):

     - 4/4 y detras de la clave no hay nada.
     - Encima del pentagrama pone **Swing**.
     - La IZQUIERDA lleva la progresion de cuatro acordes mas famosa que hay,
       y la lleva en blancas, dos por compas:

         c. 1   Do3 · La2
         c. 2   Fa2 · Sol2

       Do, La menor, Fa y Sol: es el "Heart and Soul" de toda la vida, y es la
       primera vez en el cuaderno que la izquierda cambia de nota cada dos
       tiempos.

     - La DERECHA, medida a 300 ppp:

         c. 1   Do4 · Do4 · Do4          negra, negra y BLANCA
         c. 2   (silencio de corchea) Do4 · Si3 · La3 · Si3 · Do4   seis
                corcheas ... no: cinco corcheas y una NEGRA (Re4) al final
         c. 3   Mi4 · Mi4 · Mi4          igual que el 1, un tercio mas arriba

       El c. 2 se sumo para comprobarlo: 0,5 (silencio) + 5 x 0,5 + 1 = 4. Con
       seis corcheas salian 4,5 y el compas no cerraba. La ultima es negra.

   UNA NOTA SOBRE LA MEDICION. El lector de alturas ve tres cabezas en el c. 1
   y a la tercera le pone Si5: no es una nota, es la palabra **Swing** impresa
   encima del pentagrama, que tiene agujeros cerrados igual que una blanca. Se
   miro ampliado del todo y las tres cabezas del c. 1 estan en la MISMA linea
   adicional, la del do central. La lectura buena esta anotada en
   `auditar_alturas.MIRADAS`.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, sil, corch, plan, metronomo, nombres, teclado,
                      inventa, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 de la DERECHA, medido. Cita literal.
ARRANQUE = [n('C4'), n('C4'), n('C4', 'h')]

# Los compases 1 y 2 de la IZQUIERDA, medidos: los cuatro acordes.
BAJO = [n('C3', 'h'), n('A2', 'h'), n('F2', 'h'), n('G2', 'h')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=10, nivel='iniciación',
    slug='HeartAndSoul', formato='adulto',
    titulo_corto='Heart and Soul', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Heart and Soul.pdf'),
    yt='https://www.youtube.com/results?search_query=heart+and+soul+piano+easy',

    ficha=dict(
        titulo='Heart and Soul',
        autor='Hoagy Carmichael y Frank Loesser · arreglo fácil',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Manos', 'Las dos, distintas'), ('Carácter', 'Swing'),
               ('Izquierda', 'Cuatro acordes')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, el compás 1 de la derecha. Abajo, los compases '
                   '1 y 2 de la izquierda: cuatro notas largas, dos por compás.',
        armonia=dict(
            titulo='Los cuatro acordes que has oído mil veces',
            tarjetas=[
                ('LA IZQUIERDA', 'Do · La · Fa · Sol',
                 'Cuatro notas largas, una cada dos tiempos. Es la vuelta de acordes más famosa de '
                 'la música popular: está en cientos de canciones.'),
                ('LA DERECHA', 'Tres notas iguales',
                 'El compás 1 son tres veces el do central: dos cortas y una larga. Más fácil, '
                 'imposible.'),
                ('SWING', 'No es un tempo',
                 'Es una manera de tocar: los pares de corcheas se hacen desiguales, la primera un '
                 'poco más larga que la segunda. Se aprende oyéndolo, no leyéndolo.'),
                ('LAS DOS MANOS', 'Cada una a lo suyo',
                 'Por primera vez cada mano lleva su ritmo: la izquierda camina despacio y la '
                 'derecha se mueve por encima.'),
            ],
            pie='Esta canción es famosa por tocarse a cuatro manos, dos personas en el mismo piano. '
                'La parte de abajo, la de los cuatro acordes, es la que se toca sola en cuanto la '
                'tienes: por eso vale la pena aprenderla de memoria.',
        ),
        ritmos=[
            ('LA DERECHA', 'el compás 1, medido · tres veces el do central',
             ARRANQUE, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · los cuatro acordes, en blancas',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Compás de 4/4, y no hay ni un sostenido ni un bemol.',
            'Encima del pentagrama pone "Swing".',
            'La izquierda cambia de nota cada dos tiempos.',
            'Las cuatro notas de la izquierda son Do, La, Fa y Sol.',
            'La derecha empieza con tres notas iguales, en el do central.',
            'En el compás 2 hay un silencio de corchea antes de empezar.',
        ],
        reto='Que la izquierda no se pare cuando la derecha se mueve. Es lo primero que pasa: la '
             'derecha hace algo complicado y la izquierda espera educadamente.',
        truco='Aprende la izquierda de memoria, sin mirar el papel, hasta que la puedas tocar '
              'mientras hablas de otra cosa. Solo entonces añade la derecha. Si tienes que pensar '
              'en las dos manos a la vez, no va a salir.',
        sabias='Se escribió en 1938 para una película, pero se hizo famosa treinta años después '
               'gracias a que cualquiera podía tocar la parte de abajo con dos dedos. Es, '
               'probablemente, la canción que más gente ha tocado por primera vez en un piano.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo la mano de abajo: cuatro notas que se repiten toda la canción. '
                      'Esa es la que vas a aprender primero.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí el orden importa más que nunca: primero la izquierda hasta tenerla de memoria, '
              'y solo después la derecha. Al revés no funciona.',
        reglas=['LA IZQUIERDA, DE MEMORIA', 'DOS TIEMPOS POR NOTA, SIN PRISA',
                'LA DERECHA, DESPUÉS'],
        bloques=[
            dict(num=1, titulo='Los cuatro acordes de la izquierda', clef='bass',
                 pista='cc. 1–2 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) las cuatro notas en redondas, una por compás · para verlas bien',
                          events=[n('C3', 'w'), n('A2', 'w'), n('F2', 'w'), n('G2', 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y dando la vuelta entera dos veces, que es como suena de verdad',
                          events=[n('C3', 'h'), n('A2', 'h'), n('F2', 'h'), n('G2', 'h'),
                                  n('C3', 'h'), n('A2', 'h'), n('F2', 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA VUELTA DE ACORDES SUENA A CANCIÓN',
                 texto='Do, La menor, Fa y Sol. El primero es la casa; el segundo es la misma casa '
                       'con la luz apagada; el tercero se aleja y el cuarto empuja para volver. Ese '
                       'empujón del cuarto es lo que hace que la vuelta pueda repetirse sin parar. '
                       'Cuando la reconozcas de oído la vas a encontrar por todas partes.'),
            dict(num=2, titulo='La derecha, sin prisa',
                 pista='c. 1 y lo que viene detrás · medidos en tu partitura',
                 sistemas=[
                     dict(cap='a) el compás 1 y el 3: la misma figura, dos alturas distintas',
                          events=[n('C4'), n('C4'), n('C4', 'h'),
                                  n('E4'), n('E4'), n('E4', 'h')],
                          bars=2),
                     dict(cap='b) y el compás 2, con su silencio delante y su negra al final',
                          events=[sil('e')] + corch(['C4', 'B3', 'A3']) +
                                 corch(['B3', 'C4']) + [n('D4')],
                          bars=1, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, una vez cada una',
                 pista='cc. 1 y 3 · medidos · la izquierda camina y la derecha se mueve encima',
                 sistemas=[
                     dict(cap='a) los compases 1 y 3, que son los que se repiten toda la canción',
                          events=[ac(('C3', 'C4')), ac(('C4',)), ac(('A2', 'C4'), 'h'),
                                  ac(('C3', 'E4')), ac(('E4',)), ac(('A2', 'E4'), 'h')],
                          bars=2, manos='sostiene'),
                     dict(cap='b) y la vuelta entera de la izquierda, con la derecha aguantando el '
                              'do central por encima',
                          events=[ac(('C3', 'C4'), 'h'), ac(('A2',), 'h'),
                                  ac(('F2', 'C4'), 'h'), ac(('G2',), 'h'),
                                  ac(('C3', 'E4'), 'h'), ac(('A2',), 'h'),
                                  ac(('F2', 'E4'), 'h'), ac(('G2',), 'h')],
                          bars=4, manos='dobla', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Heart and Soul · para casa',
            intro='Quince minutos al día, y los ocho primeros para la izquierda sola. Es la pieza '
                  'del curso en la que más se gana teniendo paciencia con una sola mano.',
            bloques=[
                plan((6, 'La izquierda sola, hasta tocarla sin mirar el papel'),
                     (3, 'La derecha del compás 1 y del compás 3'),
                     (3, 'La derecha del compás 2, con su silencio'),
                     (3, 'Las dos manos, los dos primeros compases')),
                metronomo('Empieza a ♩ = 72 con la izquierda sola, que aguanta bien esa velocidad.',
                          'Con las dos manos, baja a 60 el primer día. No es retroceder: es empezar '
                          'otra cosa.'),
                nombres(['C3', 'A2', 'F2', 'G2'],
                        titulo='Los nombres de las cuatro notas de la izquierda',
                        pista='están en clave de fa · escríbelos debajo de cada una'),
                teclado([('Do', 'primer acorde'), ('La', 'segundo'), ('Fa', 'tercero'),
                         ('Sol', 'cuarto')],
                        ['¿Cuál de las cuatro es la más grave?',
                         '¿Entre cuáles dos hay más distancia?'],
                        titulo='Marca en el teclado las cuatro notas de la izquierda',
                        pista='y fíjate en que las cuatro son teclas blancas'),
                inventa(['cuatro tiempos en total', 'solo notas blancas y negras',
                         'que empiece y acabe en Do'],
                        (4, 4), clef='bass',
                        titulo='Inventa tú un compás para la izquierda',
                        pista='con las mismas notas de tu pieza: Do, La, Fa y Sol'),
                para_clase('La izquierda sola, de memoria y sin mirar. Si te la sabes, la clase '
                           'entera se puede dedicar a juntar las dos manos.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 70, 'C4', 'C3',
    'la izquierda cambiando de nota cada dos tiempos, sin parar',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
