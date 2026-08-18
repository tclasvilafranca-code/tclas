# -*- coding: utf-8 -*-
"""Spring, de Vivaldi (versión *easy*) — pieza 9 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Spring (easy) — From the
   Four Seasons", 1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4.
     - El primer compás está CALLADO casi entero: silencio de blanca, silencio
       de negra y una sola negra en el cuarto tiempo. Justo detrás hay una
       BARRA DE REPETICIÓN con dos puntos.
     - La izquierda va en REDONDAS y en compases sueltos hace negras con
       silencios de negra.
     - La derecha va en negras y en parejas de corcheas.

   Lo nuevo de la semana es entrar tarde y a tiempo: contar tres tiempos en
   silencio y tocar en el cuarto.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from lu_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=9, nivel='iniciación', slug='Spring',
    formato='adulto',
    titulo_corto='Spring · La primavera', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'LA PRIMAVERA.pdf easy'),
    yt='https://www.youtube.com/results?search_query=vivaldi+spring+easy+piano',

    ficha=dict(
        titulo='Spring · La primavera',
        autor='Antonio Vivaldi · de Las cuatro estaciones · versión fácil',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Alegre'), ('Empieza', 'En el cuarto tiempo'),
               ('Izquierda', 'Redondas')],
        titulo_ritmos='Tres tiempos callada y una nota',
        pie_ritmos='El primer compás es literal: dos silencios y una negra en el cuarto tiempo. Las '
                   'notas de la melodía están en tu partitura.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('EMPIEZA CALLADA', 'Tres tiempos',
                 'El primer compás lleva un silencio de blanca y uno de negra, y solo entonces una '
                 'nota. Hay que contar uno-dos-tres en silencio y tocar en el cuatro.'),
                ('LOS DOS PUNTOS', 'Se repite',
                 'Justo después hay una barra con dos puntos. Quiere decir que ese trozo se toca '
                 'dos veces. No es un adorno: está para tocarlo.'),
                ('LA IZQUIERDA EN REDONDAS', 'Cuatro tiempos',
                 'Una sola nota por compás, aguantada entera. Es la mano fácil, y es la que lleva '
                 'la cuenta: si ella no se mueve, tú tampoco pierdes el sitio.'),
                ('PAREJAS DE CORCHEAS', 'Dos por golpe',
                 'La derecha tiene notas unidas de dos en dos. Dos de esas caben en un solo golpe '
                 'de la izquierda.'),
            ],
            pie='Vivaldi escribió esta música para orquesta, no para piano. Lo que tú tocas es la '
                'melodía del violín, puesta a la altura de dos manos.',
        ),
        ritmos=[
            ('EL PRIMER COMPÁS', 'callada hasta el cuarto tiempo · literal',
             [sil('h'), sil('q'), n('C4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda por compás · literal',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4.',
            'El primer compás está callado hasta el cuarto tiempo.',
            'Detrás del primer compás hay una barra de repetición: ese trozo se toca dos veces.',
            'La izquierda hace redondas, una nota por compás.',
            'La derecha lleva parejas de corcheas: dos notas en un golpe.',
        ],
        reto='Entrar en el cuarto tiempo, ni antes ni después. Callado no quiere decir parado: hay '
             'que contar los tres tiempos igual de despacio que si sonaran.',
        truco='Cuenta los tres primeros tiempos en voz alta y dando un golpecito con la mano en la '
              'pierna. El golpe hace que el silencio dure lo que tiene que durar. Cuando entres a '
              'tiempo tres veces seguidas, deja de dar el golpe pero sigue contando.',
        sabias='Vivaldi publicó Las cuatro estaciones en 1725 con un poema para cada una, escrito '
               'seguramente por él. La primavera empieza con los pájaros, y esa melodía que tocas '
               'es exactamente eso.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la versión de orquesta y busca tu melodía dentro. Está en los '
                      'violines, y una vez la oyes ya no se despega.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana lo difícil no es tocar: es esperar. Los tres pasos van del silencio a la '
              'melodía, y el primero es el importante.',
        reglas=['CUENTA LOS TIEMPOS CALLADOS EN VOZ ALTA', 'LA IZQUIERDA AGUANTA LOS CUATRO',
                'LOS DOS PUNTOS SE OBEDECEN'],
        bloques=[
            dict(num=1, titulo='Contar tres tiempos y entrar en el cuarto',
                 pista='andamio en Do mayor · el primer compás es el de tu partitura',
                 sistemas=[
                     dict(cap='a) uno, dos, tres en silencio y tocas en el cuatro · cuenta en voz '
                              'alta desde el principio',
                          events=[sil('h'), sil('q'), n('C4'),
                                  n('E4'), n('E4'), n('F4'), n('D4')],
                          bars=2),
                     dict(cap='b) lo mismo empezando más arriba · lo que se practica es la espera, '
                              'no las notas',
                          events=[sil('h'), sil('q'), n('G4'),
                                  n('A4'), n('G4'), n('F4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: una redonda y a esperar',
                 pista='andamio · la mano que sostiene y no se mueve',
                 sistemas=[
                     dict(cap='a) toca en el uno y no la sueltes hasta el compás siguiente',
                          events=[n('C3', 'w'), n('G2', 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) y el compás con negras y silencios, que también aparece · el '
                              'silencio dura lo mismo que la nota',
                          events=[sil('q'), n('E3'), n('G3'), sil('q'), n('C3', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ SIGNIFICAN LOS DOS PUNTOS',
                 texto='La barra gruesa con dos puntos que hay al principio marca el sitio al que '
                       'hay que volver. Se toca hasta la barra del final, se vuelve allí y se toca '
                       'otra vez. Es media pieza menos que leer, y una manera de que el trozo salga '
                       'el doble de veces con el mismo papel.'),
            dict(num=3, titulo='Las dos juntas, con las parejas de corcheas',
                 pista='andamio · dos notas de arriba caben en una de abajo · muy despacio',
                 sistemas=[
                     dict(cap='a) la izquierda aguanta y la derecha se mueve por encima',
                          events=[ac(('C3', 'E4')), n('E4')] + corch(['F4', 'D4']) + [n('E4')]
                                 + [ac(('G2', 'D4')), n('D4')] + corch(['E4', 'C4']) + [n('D4')],
                          bars=2),
                     dict(cap='b) y con la melodía bajando · si las corcheas te corren, cuenta '
                              '"un-y, dos-y" en voz alta',
                          events=[ac(('C3', 'G4'))] + corch(['F4', 'E4']) + [n('D4'), n('E4')]
                                 + [ac(('F2', 'A4'))] + corch(['G4', 'F4']) + [n('E4'), n('F4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
