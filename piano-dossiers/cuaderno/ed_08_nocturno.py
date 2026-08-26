# -*- coding: utf-8 -*-
"""Nocturno op. 9 nº 2, de Chopin — pieza 8 de Eduard. Formato ADULTO.

   Version muy simplificada, la de su carpeta: el Nocturno original va en Mib
   mayor y en 12/8, y este arreglo lo pasa a 3/4 y a teclas blancas para que
   se pueda tocar el primer ano. Eso hay que decirlo en la hoja, porque si el
   alumno pone la grabacion no va a reconocer ni el compas.

   Medido sobre ESE PDF (vectorial, dos pentagramas por sistema):

     - 3/4 y detras de la clave NO hay nada. Todo teclas blancas.
     - Empieza con ANACRUSA de un tiempo, y la anacrusa la toca solo la
       IZQUIERDA: la derecha tiene ahi un silencio de negra.
     - Pone **mp** debajo de cada pentagrama.
     - La melodia del principio, medida a 300 ppp:

         c. 1   Mi4                    blanca con puntillo, con ligadura
         c. 2   Mi4 · Re4 · Mi4        tres negras
         c. 3   Re4                    blanca con puntillo

     - La izquierda: Sol3 en la anacrusa, y despues DOS COMPASES ENTEROS de
       silencio. Vuelve a entrar mas adelante.
     - La digitacion viene impresa (un 3 encima de la derecha, un 4 debajo de
       la izquierda).

   POR QUE VA AQUI. Es la pieza mas lenta del cuaderno y la que menos notas
   tiene por compas: sirve para lo que ninguna rapida sirve, que es escuchar
   el sonido de una nota entera mientras dura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, sil, plan, objetivo, unir, colorear, escribir,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los compases 1 y 2 de la DERECHA, medidos. Cita literal. La ligadura es la
# que trae la partitura: arquea desde la nota larga hasta la frase siguiente.
MELODIA = [n('E4', 'h.'), n('E4'), n('D4'), n('E4')]
MELODIA[0] = dict(MELODIA[0], lig=1)

# La anacrusa y el c. 1 de la IZQUIERDA. Delante van dos tiempos de silencio
# que la partitura no dibuja: son la parte del compas de anacrusa que no
# suena, y puestos ahi la fila suma dos compases justos.
BAJO = [sil('h'), n('G3'), sil('h.')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=8, nivel='iniciación',
    slug='NocturnoChopin', formato='adulto',
    titulo_corto='Nocturno op. 9 nº 2', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Nocturne op9 Chopin.pdf'),
    yt='https://www.youtube.com/results?search_query=chopin+nocturne+op+9+no+2',

    ficha=dict(
        titulo='Nocturno op. 9 nº 2',
        autor='Frédéric Chopin · versión muy simplificada',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Manos', 'Las dos, por turnos'), ('Volumen', 'mp'),
               ('Dedos', 'Escritos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, los compases 1 y 2 de la derecha. Abajo, la '
                   'izquierda: una nota de anacrusa y después un compás entero callada.',
        armonia=dict(
            titulo='Lo que aquí se aprende es a escuchar',
            tarjetas=[
                ('NOTAS LARGAS', 'Tres tiempos',
                 'La primera nota dura el compás entero. Eso no es fácil: hay que quedarse quieto '
                 'escuchando cómo se apaga, sin correr a la siguiente.'),
                ('LA ANACRUSA', 'La toca la izquierda',
                 'La pieza empieza antes del primer compás, y esa nota de impulso es de la mano '
                 'izquierda. La derecha entra en el compás 1.'),
                ('LA LIGADURA', 'El arco de arriba',
                 'Ese arco que une notas quiere decir que la frase no se corta: se toca de un tirón, '
                 'como una frase hablada sin puntos.'),
                ('MP', 'Medio suave',
                 'Mezzo piano. Un poco por debajo del volumen normal de hablar. En una pieza lenta, '
                 'el volumen se nota mucho más que en una rápida.'),
            ],
            pie='Ojo con la grabación: el Nocturno de verdad está en otra tonalidad y en otro '
                'compás, y va lleno de adornos. Esta es una versión reducida al hueso, hecha para '
                'poder tocarla el primer año.',
        ),
        ritmos=[
            ('LA DERECHA', 'cc. 1 y 2, medidos · la primera nota dura todo el compás',
             MELODIA, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'la anacrusa y el c. 1, medidos · una nota y a callar',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Compás de 3/4: tres golpes, y el primero es el fuerte.',
            'No hay ni un sostenido ni un bemol.',
            'La anacrusa la toca la izquierda, no la derecha.',
            'La primera nota de la derecha dura el compás entero.',
            'Debajo de los dos pentagramas pone "mp": medio suave.',
            'Hay ligaduras dibujadas encima de la melodía.',
        ],
        reto='Aguantar. Una blanca con puntillo son tres tiempos enteros, y la tentación es soltarla '
             'al segundo y quedarse mirando la siguiente nota.',
        truco='Cuenta los tres tiempos EN VOZ ALTA mientras la nota suena, y no levantes el dedo '
              'hasta decir el uno del compás siguiente. Si el sonido se apaga antes, no pasa nada: '
              'el dedo se queda igual.',
        sabias='Chopin escribió los Nocturnos pensando en el sonido de un piano tocado de noche, '
               'bajito, en un salón pequeño. Casi nunca daba conciertos grandes: decía que el '
               'público numeroso le intimidaba.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en lo despacio que va y en cuánto dura cada nota. Es lo contrario de '
                      'lo que pide el cuerpo cuando uno está aprendiendo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza tiene pocas notas y mucho tiempo entre ellas. Se estudia despacio a '
              'propósito: lo que se trabaja aquí es el sonido, no los dedos.',
        reglas=['CUENTA LOS TRES TIEMPOS EN VOZ ALTA', 'NO SUELTES LA TECLA ANTES DE TIEMPO',
                'MP: NI FUERTE NI TÍMIDO'],
        bloques=[
            dict(num=1, titulo='Notas largas, y escucharlas hasta el final',
                 pista='andamio en Do mayor · tres tiempos cada una',
                 sistemas=[
                     dict(cap='a) una nota por compás · cuenta "un-dos-tres" mientras suena',
                          events=[n('C4', 'h.'), n('D4', 'h.'), n('E4', 'h.'), n('D4', 'h.')],
                          matiz='mp',
                          bars=4),
                     dict(cap='b) y ahora larga, corta, corta · la larga sigue durando tres',
                          events=[n('E4', 'h.'), n('F4'), n('E4'), n('D4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ CUESTA TANTO UNA NOTA LARGA',
                 texto='Porque no hay nada que hacer mientras dura, y el cuerpo quiere hacer algo. '
                       'Lo que hay que hacer es escuchar: una nota de piano no se queda igual, va '
                       'bajando de volumen desde el primer instante. Si te acostumbras a oír cómo '
                       'se apaga, dejarás de tener prisa por la siguiente.'),
            dict(num=2, titulo='La melodía del principio, tal y como está escrita',
                 pista='cc. 1–2 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) primero solo las tres notas cortas del compás 2',
                          events=[n('E4'), n('D4'), n('E4'), n('D4'), n('E4'), n('D4')],
                          bars=2),
                     dict(cap='b) y con la nota larga delante, que es como va de verdad',
                          events=[n('E4', 'h.'), n('E4'), n('D4'), n('E4'), n('D4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: una nota y a esperar', clef='bass',
                 pista='andamio en Do mayor · lo raro aquí es el silencio, no la nota',
                 sistemas=[
                     dict(cap='a) una nota y un compás entero callado · cuenta los tres tiempos',
                          events=[n('G3'), sil('h'), sil('h.'), n('C3'), sil('h')],
                          bars=3, clef='bass'),
                     dict(cap='b) y dos compases callados seguidos, que es lo que hace tu partitura',
                          events=[n('G3'), sil('h'), sil('h.'), sil('h.'), n('C3', 'h.')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y por último, las dos manos: la izquierda da el impulso y la '
                              'derecha se queda con la nota larga',
                          events=[sil('h'), ac(('G3',)), ac(('E4',), 'h.'),
                                  ac(('C3', 'E4'), 'h.')],
                          bars=3, manos='dobla', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Nocturno · para casa',
            intro='Quince minutos al día, y esta semana con el metrónomo apagado casi todo el rato: '
                  'lo que hay que oír es el sonido de la nota, no el tic.',
            bloques=[
                plan((4, 'Notas largas sueltas, contando tres en voz alta'),
                     (4, 'Los compases 1 y 2 de la derecha, muy despacio'),
                     (4, 'La izquierda: la anacrusa y los compases callados'),
                     (3, 'La primera línea entera, sin parar aunque salga lenta')),
                objetivo('Que una blanca con puntillo dure tres tiempos de verdad. Si la sueltas '
                         'en el dos, la pieza entera va a sonar apurada.'),
                unir([('Blanca con puntillo', '3 tiempos'),
                      ('Negra', '1 tiempo'),
                      ('mp', 'medio suave'),
                      ('Ligadura', 'no se corta la frase'),
                      ('Anacrusa', 'empieza antes del compás')],
                     titulo='Une cada cosa con lo que significa',
                     pista='todas están en tu partitura de esta semana'),
                colorear([n('E4', 'h.'), n('E4'), n('D4'), n('E4'), n('D4', 'h.')],
                         [('h.', 'las largas'), ('q', 'las cortas')],
                         titulo='Colorea de un color las largas y de otro las cortas',
                         pista='son los compases 1, 2 y 3 de tu mano derecha'),
                escribir(titulo='Copia aquí el compás 2, con sus tres negras',
                         pista='y luego tócalo cinco veces contando en voz alta'),
                para_clase('La primera línea con las dos manos, y sobre todo cuánto te duran las '
                           'notas largas. Trae marcado el sitio donde se te escapa el tiempo.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 68, 'E4', 'C3',
    'aquí lo que se trabaja es el sonido, no la velocidad',
    desde=4, time_sig=(3, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
