# -*- coding: utf-8 -*-
"""La Pantera Rosa — pieza 7 de Eduard. Formato ADULTO.

   La PRIMERA pieza del cuaderno con las dos manos escritas, y esta elegida
   justo por como empieza.

   Medido sobre el PDF de su carpeta (vectorial, pentagrama de 21 px de
   espacio, dos pentagramas por sistema):

     - 4/4 y detras de la clave no hay nada.
     - La DERECHA no toca en los tres primeros compases: tres silencios de
       redonda seguidos. Entra en el compas 4, y todavia despues de tres
       silencios de negra: su primera nota es el CUARTO tiempo del cuarto
       compas.
     - La IZQUIERDA empieza sola:

         c. 1   Do3 · Sol3            dos blancas
         c. 2   Do3                   redonda
         c. 3   Do3 · Sol3            dos blancas
         c. 4   Do3 (blanca con puntillo) y un silencio de negra

     - La primera nota de la derecha es un Do4 —el do central— en el cuarto
       tiempo del c. 4. Se miro ampliada del todo porque el lector la daba
       media linea mas abajo: la cabeza esta ATRAVESADA por su linea
       adicional, y esa linea es el Do central.
     - La digitacion viene impresa: se ven el 5 y el 1 debajo del pentagrama
       de la izquierda, y numeros sueltos encima del de la derecha.

   POR QUE ES LA PIEZA DEL SALTO A LAS DOS MANOS. Las seis anteriores o son de
   una sola mano o llevan las dos haciendo lo mismo. Aqui, por primera vez,
   cada mano hace lo suyo — y el arreglo lo pone facil de la unica manera
   sensata: dejando que la izquierda entre sola y dando tres compases enteros
   para colocar la derecha sin prisa.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, sil, plan, metronomo, contar, teclado, ordenar,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los compases 3 y 4 de la DERECHA, medidos. Cita literal: un compas entero
# callado, tres tiempos mas de silencio, y la primera nota en el cuarto.
ENTRADA = [sil('w'), sil('q'), sil('q'), sil('q'), n('C4')]

# Los compases 1 y 2 de la IZQUIERDA, medidos.
BAJO = [n('C3', 'h'), n('G3', 'h'), n('C3', 'w')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=7, nivel='iniciación',
    slug='PanteraRosa', formato='adulto',
    titulo_corto='La Pantera Rosa', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'La Panthere Rose.pdf'),
    yt='https://www.youtube.com/results?search_query=pantera+rosa+piano+facil',

    ficha=dict(
        titulo='La Pantera Rosa',
        autor='Henry Mancini · arreglo fácil para piano',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Manos', 'Las dos, por fin'), ('Empieza', 'La izquierda sola'),
               ('Dedos', 'Escritos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, lo que hace la derecha en los compases 3 y 4: '
                   'nada, hasta el último tiempo. Abajo, la izquierda de los compases 1 y 2.',
        armonia=dict(
            titulo='Cada mano por su lado, y con red',
            tarjetas=[
                ('DOS PENTAGRAMAS', 'Uno por mano',
                 'El de arriba, en clave de sol, es la derecha. El de abajo, en clave de fa, la '
                 'izquierda. A partir de aquí casi todas las piezas vienen así.'),
                ('EMPIEZA ABAJO', 'Tres compases',
                 'La derecha no toca hasta el compás 4. Tienes tres compases enteros para colocar '
                 'la mano con calma mientras la izquierda ya suena.'),
                ('LA IZQUIERDA', 'Do y Sol',
                 'Dos teclas, y notas largas: blancas y una redonda. Es un acompañamiento de los '
                 'que se aprenden en un rato.'),
                ('LA ENTRADA', 'En el cuarto tiempo',
                 'La primera nota de la derecha es el do central, y cae en el último tiempo del '
                 'compás 4. Contar hasta ahí es todo el trabajo de la semana.'),
            ],
            pie='Fíjate en que las dos manos nunca están igual de ocupadas: mientras una lleva la '
                'melodía, la otra sostiene. Ese reparto es el pan de cada día del piano.',
        ),
        ritmos=[
            ('LA DERECHA', 'cc. 3 y 4, medidos · no toca hasta el último tiempo',
             ENTRADA, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · empieza sola',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Dos pentagramas: arriba la derecha, abajo la izquierda.',
            'La derecha calla los tres primeros compases enteros.',
            'La izquierda empieza sola, con dos teclas: Do y Sol.',
            'Compás de 4/4, y no hay ni un sostenido ni un bemol.',
            'La primera nota de la derecha es el do central.',
            'La digitación viene impresa en tu edición.',
        ],
        reto='Contar tres compases sin tocar y entrar en el sitio. Un compás callado se hace corto '
             'cuando estás nervioso y larguísimo cuando estás contando bien.',
        truco='Cuenta en voz alta "uno-dos-tres-cuatro" los cuatro compases enteros, tocando solo '
              'la izquierda. Cuando llegues al cuatro del cuarto compás, la mano derecha ya tiene '
              'que estar colocada encima de la tecla, sin apretar.',
        sabias='Henry Mancini escribió este tema en 1963 para los títulos de crédito de la '
               'película, y la pantera del dibujo se hizo tan famosa que acabó teniendo su propia '
               'serie. La melodía se apoya toda en notas que caen a destiempo: por eso suena a '
               'alguien andando de puntillas.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta con el pie desde el primer golpe y verás que el saxo entra tarde, '
                      'justo antes del compás siguiente.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí lo nuevo es que hay dos pentagramas. Se estudia una mano cada vez, y solo se '
              'juntan cuando las dos salen solas.',
        reglas=['PRIMERO LA IZQUIERDA, QUE EMPIEZA ELLA', 'CUENTA LOS COMPASES CALLADOS',
                'LAS DOS JUNTAS, AL FINAL Y DESPACIO'],
        bloques=[
            dict(num=1, titulo='La izquierda sola, con notas largas', clef='bass',
                 pista='andamio en Do mayor · dos teclas y nada más',
                 sistemas=[
                     dict(cap='a) las dos teclas de la pieza, una en cada mitad del compás',
                          events=[n('C3', 'h'), n('G3', 'h'), n('G3', 'h'), n('C3', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y con una redonda en medio, que dura el compás entero',
                          events=[n('C3', 'w'), n('G3', 'h'), n('C3', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE LEEN DOS PENTAGRAMAS A LA VEZ',
                 texto='No se leen a la vez: se leen por columnas. Lo que está uno encima de otro '
                       'suena a la vez, y lo que está más a la derecha suena después. Al principio '
                       'conviene ir marcando con el dedo la columna que toca, como quien sigue un '
                       'renglón. En dos semanas deja de hacer falta.'),
            dict(num=2, titulo='Contar sin tocar, que es la mitad de esta pieza',
                 pista='andamio en Do mayor · la mano derecha, esperando su turno',
                 sistemas=[
                     dict(cap='a) un compás entero callado y luego cuatro notas · cuenta en voz alta',
                          events=[sil('w'), n('C4'), n('D4'), n('E4'), n('D4')],
                          bars=2),
                     dict(cap='b) y ahora callando tres tiempos y entrando en el cuarto',
                          events=[sil('q'), sil('q'), sil('q'), n('E4'),
                                  n('D4'), sil('q'), sil('q'), n('C4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, en el sitio donde se juntan',
                 pista='cc. 3–4 · el dibujo de tu partitura, con la entrada de la derecha',
                 sistemas=[
                     dict(cap='a) la izquierda sostiene y la derecha entra al final del compás',
                          events=[ac(('C3',), 'h'), ac(('G3',), 'h'),
                                  ac(('C3',), 'h.'), ac(('C4',))],
                          bars=2, manos='sostiene'),
                     dict(cap='b) y una vez más, con la derecha aguantando su nota',
                          events=[ac(('C3',), 'h'), ac(('G3',), 'h'),
                                  ac(('C3',), 'h.'), ac(('C4',))],
                          bars=2, manos='sostiene', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='La Pantera Rosa · para casa',
            intro='Quince minutos al día. La izquierda de esta pieza se aprende en dos días; lo que '
                  'lleva la semana entera es contar los compases en los que no tocas.',
            bloques=[
                plan((4, 'La izquierda sola, los cuatro primeros compases'),
                     (4, 'Contar los cuatro compases en voz alta, tocando solo la izquierda'),
                     (4, 'La entrada de la derecha, en el cuarto tiempo del compás 4'),
                     (3, 'Las dos manos, muy despacio')),
                metronomo('Empieza a ♩ = 60 y no subas hasta que la entrada salga tres veces seguidas.',
                          'Tu partitura no trae número de metrónomo: estos son de trabajo, no de la '
                          'edición.'),
                contar([n('C3', 'h'), n('G3', 'h'), n('C3', 'w'), n('C3', 'h'), n('G3', 'h')],
                       ['¿Cuántas notas hay en total?', '¿Cuántas veces aparece el Do?',
                        '¿Cuál dura más, y cuántos tiempos?'],
                       titulo='Mira la izquierda y cuenta',
                       pista='son los tres primeros compases de tu mano izquierda'),
                teclado([('Do', 'la tecla de la izquierda'), ('Sol', 'la otra tecla de la izquierda')],
                        ['Marca dónde está el do central, que es donde entra la derecha.'],
                        titulo='Señala las teclas de esta pieza',
                        pista='son tres en total, y no se mueven en toda la página'),
                ordenar(['Coloco la mano izquierda en Do y Sol.',
                         'Toco los tres primeros compases contando en voz alta.',
                         'Pongo la derecha encima del do central, sin apretar.',
                         'Entro con la derecha en el cuarto tiempo del compás 4.'],
                        titulo='Pon en orden lo que hay que hacer',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                para_clase('Los cuatro primeros compases con las dos manos. Si la entrada de la '
                           'derecha te sale unas veces sí y otras no, dilo: se arregla contando '
                           'distinto, no repitiendo más.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 67, 'C4', 'C3',
    'la izquierda entre Do y Sol, que es lo único que toca al principio',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
