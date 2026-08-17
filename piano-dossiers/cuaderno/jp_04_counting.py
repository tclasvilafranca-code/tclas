# -*- coding: utf-8 -*-
"""Counting Stars (OneRepublic) — pieza 4 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Becky Messer,
   marcado "Easy Version", descarga de Musescore, 2 páginas):

     - Do mayor: detrás de la clave no hay nada.
     - 4/4. No imprime tempo.
     - La DIGITACIÓN VIENE IMPRESA nota a nota encima de la melodía: 2 3 5 2 1
       3, 4, 5 1, 3… Es de las pocas partituras del cuaderno que la traen, y
       está para usarla.
     - La izquierda hace redondas de dos notas, una por compás, en casi toda la
       primera página.
     - Hay barras de repetición en los cc. 5, 10 y 22, y una casilla "1."

   El archivo es EL MISMO que el de José María (md5 idéntico). Lo inventado va
   por otro camino: aquí el andamio trabaja el cambio de dedo sobre la misma
   tecla y allí trabaja las corcheas seguidas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, plan, metronomo, verdadero_falso, inventa,
                      dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=4, nivel='intermedio', slug='CountingStars',
    formato='adulto',
    titulo_corto='Counting Stars', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source', 'Counting-stars.pdf'),
    yt='https://www.youtube.com/results?search_query=counting+stars+piano+easy+version',

    ficha=dict(
        titulo='Counting Stars',
        autor='OneRepublic · arreglo de Becky Messer · Easy Version',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Digitación', 'Impresa'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Cómo se reparten las dos manos',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: redondas de dos notas abajo y '
                   'melodía con digitación escrita arriba. Las notas exactas, en tu partitura.',
        armonia=dict(
            titulo='La partitura te está diciendo más de lo que parece',
            tarjetas=[
                ('LOS NÚMEROS', 'Digitación impresa',
                 'Encima de las notas hay números pequeños: 2 3 5 2 1 3… Son los dedos, y no son '
                 'una sugerencia. Con otros dedos, la frase siguiente no te cabe en la mano.'),
                ('LAS REDONDAS', 'La izquierda espera',
                 'Dos notas a la vez, una vez por compás. Es el reparto más común del piano y aquí '
                 'está en su forma más pura.'),
                ('LAS REPETICIONES', 'cc. 5, 10 y 22',
                 'Tres barras de repetición y una casilla "1.". La pieza es más corta de lo que '
                 'parece: mucho de lo escrito ya lo sabes tocar cuando llegas.'),
                ('SIN TEMPO', 'Lo eliges tú',
                 'La edición no imprime velocidad. Elige una que puedas mantener en la parte más '
                 'apretada, no en la primera línea.'),
            ],
            pie='Que la digitación venga impresa cambia cómo se estudia esto: no hay que decidir '
                'nada, hay que obedecer y repetir. Ese es el trabajo de esta semana, y es más '
                'aburrido y más rápido que inventarse los dedos.',
        ),
        ritmos=[
            ('MANO DERECHA', 'melodía con los dedos escritos · andamio',
             [n('C4'), n('D4'), n('E4'), n('D4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas, una redonda por compás · literal',
             [ac(('C3', 'G3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay armadura: ni sostenidos ni bemoles.',
            'La digitación viene impresa nota a nota: 2 3 5 2 1 3, 4, 5 1, 3…',
            'La izquierda hace redondas de dos notas, una por compás.',
            'Hay barras de repetición en los compases 5, 10 y 22.',
            'Hay una casilla de primera vez ("1.") cerca del final.',
            'La edición no imprime tempo.',
        ],
        reto='Usar la digitación escrita, toda, también donde te parece que sobra. Al que lleva '
             'tiempo tocando le sale sola una digitación propia, y aquí la propia se acaba '
             'estrellando dos compases más adelante.',
        truco='La primera vez que leas cada frase, tócala SOLO mirando los números, sin mirar las '
              'notas: pon los dedos donde dice y deja que suene lo que suene. Suena mal una vez y '
              'después ya no hay que decidir nada.',
        sabias='OneRepublic la grabó en 2013 y el estribillo está en un compás distinto del resto '
               'de la canción en la versión original. Los arreglos fáciles suelen enderezarlo todo '
               'a 4/4, que es lo que hace este.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cuántas veces se repite lo mismo. Lo que estás aprendiendo esta '
                      'semana te sirve para más de la mitad de la canción.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana no hay que decidir nada: la partitura trae los dedos escritos. El trabajo '
              'es obedecerlos hasta que salgan solos, y eso se hace despacio y repitiendo, no '
              'tocando la pieza entera.',
        reglas=['LOS DEDOS ESCRITOS, TODOS', 'LA REDONDA DURA CUATRO GOLPES',
                'DESPACIO Y REPITIENDO'],
        bloques=[
            dict(num=1, titulo='Cambiar de dedo sin cambiar de tecla',
                 pista='andamio en Do mayor · es lo que te va a pedir la digitación impresa',
                 sistemas=[
                     dict(cap='a) la misma nota con dedos distintos, seguidos · sin mover la mano y '
                              'sin que se oiga el cambio',
                          events=[dict(pitch='C4', dur='q', number=1),
                                  dict(pitch='C4', dur='q', number=2),
                                  dict(pitch='C4', dur='q', number=3),
                                  dict(pitch='C4', dur='q', number=2),
                                  dict(pitch='D4', dur='q', number=1),
                                  dict(pitch='D4', dur='q', number=2),
                                  dict(pitch='D4', dur='h', number=3)],
                          bars=2),
                     dict(cap='b) y ahora subiendo, que es donde sirve de verdad · el pulgar pasa '
                              'por debajo sin que la muñeca dé un salto',
                          events=[dict(pitch='C4', dur='q', number=1),
                                  dict(pitch='D4', dur='q', number=2),
                                  dict(pitch='E4', dur='q', number=3),
                                  dict(pitch='F4', dur='q', number=1),
                                  dict(pitch='G4', dur='q', number=2),
                                  dict(pitch='A4', dur='q', number=3),
                                  dict(pitch='G4', dur='h', number=2)],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: dos notas y aguantar', clef='bass',
                 pista='la FORMA es literal (una redonda de dos notas por compás); las notas, andamio',
                 sistemas=[
                     dict(cap='a) cuatro compases seguidos · comprueba en el cuarto golpe que sigue '
                              'sonando, y si no, es que la sueltas antes',
                          events=[ac(('C3', 'G3'), 'w'), ac(('A2', 'E3'), 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde · prepara el siguiente mientras suena el '
                              'anterior, no cuando llega su turno',
                          events=[ac(('F2', 'C3'), 'w'), ac(('G2', 'D3'), 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ NO TE INVENTES LOS DEDOS',
                 texto='La digitación impresa no está pensada para la nota que estás tocando: está '
                       'pensada para la que viene tres después. Cuando te la saltas, la frase '
                       'empieza bien y se atasca al final, y entonces parece que el problema está '
                       'al final. No lo está: está en el dedo con el que empezaste.'),
            dict(num=3, titulo='Las dos manos, cuatro compases',
                 pista='andamio · con los dedos escritos puestos y contando en voz alta',
                 sistemas=[
                     dict(cap='a) la melodía por encima de la redonda · muy despacio',
                          events=[ac(('C3', 'C4')), n('D4'), n('E4'), n('D4'),
                                  ac(('A2', 'E4')), n('F4'), n('E4'), n('C4')],
                          bars=2),
                     dict(cap='b) y ahora con el cambio de dedo metido dentro · el Sol se repite '
                              'con dos dedos distintos y la izquierda no se entera',
                          events=[ac(('F2', 'G4')), dict(pitch='G4', dur='q', number=2),
                                  dict(pitch='A4', dur='q', number=3), n('F4'),
                                  ac(('G2', 'E4')), n('D4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Counting Stars · para casa',
            intro='Veinte minutos al día. Esta semana el objetivo son los dedos, no los compases.',
            bloques=[
                plan((6, 'Cambiar de dedo sobre la misma tecla, sin mirar'),
                     (6, 'La derecha, cc. 1-8, SOLO mirando los números'),
                     (4, 'La izquierda, cc. 1-8, comprobando las redondas'),
                     (4, 'Las dos juntas, de dos en dos compases')),
                metronomo('Elige una velocidad a la que te salga la parte más apretada, no la primera.',
                          'Apúntala aquí cada día y no la subas hasta que los dedos salgan solos.'),
                verdadero_falso([
                    'Los números pequeños encima de las notas son los dedos.',
                    'Una redonda dura cuatro golpes.',
                    'Si una digitación me resulta rara, es mejor cambiarla por la mía.',
                    'La barra de repetición manda volver atrás y tocar otra vez.',
                    'Esta partitura trae escrita la velocidad a la que hay que tocarla.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas'),
                inventa(['Solo Do, Re, Mi, Fa y Sol.',
                         'Dos compases de cuatro golpes.',
                         'Escribe TÚ el número de dedo encima de cada nota.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases y ponles la digitación',
                        pista='y tócalo con los dedos que hayas escrito, sin cambiarlos'),
                dibujar(['Do', 'Mi', 'Sol', 'La', 'Fa', 'Re', 'Do'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo, en clave de sol'),
                para_clase('Los ocho primeros compases con la digitación escrita. Si hay un sitio '
                           'donde la digitación impresa te parece imposible, tráelo marcado: casi '
                           'siempre es que la mano entra al compás anterior de otra manera.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
