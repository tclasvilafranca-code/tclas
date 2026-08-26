# -*- coding: utf-8 -*-
"""Piano Man — pieza 18 de Eduard. Formato ADULTO.

   Medido sobre el PDF de su carpeta (vectorial, dos pentagramas por sistema):

     - 3/4 y detras de la clave no hay nada.
     - Medido a 300 ppp:

         DERECHA    c. 1   (silencio de blanca) Fa4        dos tiempos callada
                                                           y una negra
                    c. 2   Fa4 · Sol4                      blanca y negra
                    c. 3   Fa4 · Fa4 · Mi4                 blanca y dos corcheas
         IZQUIERDA  c. 1   callada (silencio de compas)
                    c. 2   Do3 y Sol3 juntas               blanca con puntillo
                    c. 3   callada

     - O sea: la izquierda toca UN acorde cada dos compases y el resto del
       tiempo esta callada. Es un vals, y el acompanamiento se limita a marcar
       el primer tiempo de vez en cuando.

   UNA NOTA SOBRE LA MEDICION. `medir_arranque` lee tres cabezas en el c. 1 y
   la primera no es una nota: es el SILENCIO DE BLANCA, que es un rectangulo
   macizo y el detector de cabezas llenas lo confunde con una. La lectura buena
   —Fa4 en el c. 1, Fa4 y Sol4 en el c. 2— esta anotada en
   `auditar_alturas.MIRADAS`, que es donde va lo que se mira a ojo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, sil, corch, plan, metronomo, figuras, diferencias,
                      escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los compases 1 y 2 de la DERECHA, medidos. Cita literal.
ARRANQUE = [sil('h'), n('F4'), n('F4', 'h'), n('G4')]

# Los compases 1 y 2 de la IZQUIERDA, medidos: un compas callada y un acorde.
BAJO = [sil('h.'), ac(('C3', 'G3'), 'h.')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=18, nivel='iniciación',
    slug='PianoMan', formato='adulto',
    titulo_corto='Piano Man', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Piano Man.pdf'),
    yt='https://www.youtube.com/results?search_query=billy+joel+piano+man+piano+easy',

    ficha=dict(
        titulo='Piano Man',
        autor='Billy Joel · arreglo fácil',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Manos', 'Las dos, por turnos'), ('Estilo', 'Vals'),
               ('Izquierda', 'Un acorde cada dos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, los compases 1 y 2 de la derecha, que entra en '
                   'el tercer tiempo. Abajo, la izquierda: un compás callada y un acorde.',
        armonia=dict(
            titulo='Un vals con la izquierda muy tranquila',
            tarjetas=[
                ('COMPÁS DE VALS', 'Tres tiempos',
                 'Un-dos-tres, un-dos-tres. Piano Man es un vals, aunque no lo parezca al oírla: '
                 'por eso se balancea así.'),
                ('LA ENTRADA', 'En el tres',
                 'Los dos primeros tiempos son un silencio de blanca. La melodía entra en el '
                 'tercero, justo antes del compás siguiente.'),
                ('LA IZQUIERDA', 'Un acorde y a callar',
                 'Toca dos notas juntas —Do y Sol— que duran el compás entero, y luego se calla otro '
                 'compás. Es lo más tranquilo que va a hacer tu izquierda en todo el cuaderno.'),
                ('DOS NOTAS JUNTAS', 'Do y Sol',
                 'Es una quinta: el pulgar y el meñique, sin mover nada de en medio. Se coloca una '
                 'vez y ya está.'),
            ],
            pie='Fíjate en el reparto: la derecha lleva la voz y la izquierda solo aparece cuando '
                'hace falta. Es exactamente lo que hace un pianista de bar, que es de lo que habla '
                'la canción.',
        ),
        ritmos=[
            ('LA DERECHA', 'cc. 1 y 2, medidos · entra en el tercer tiempo',
             ARRANQUE, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · un compás callada y un acorde',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Compás de 3/4: es un vals.',
            'No hay ni un sostenido ni un bemol.',
            'Los dos primeros tiempos son un silencio de blanca.',
            'La izquierda está callada el compás 1 entero.',
            'La izquierda toca dos notas a la vez: Do y Sol.',
            'En el compás 3 aparecen las primeras corcheas.',
        ],
        reto='Que la izquierda entre en su sitio después de un compás entero callada. Cuando una '
             'mano no toca durante un compás, es facilísimo que entre medio tiempo tarde.',
        truco='Cuenta el compás callado marcándolo con la mano izquierda EN LA TAPA del piano, sin '
              'tocar. Así la mano sigue contando con el cuerpo y no tiene que reaccionar de golpe. '
              'Cuando salga, deja de dar el golpe pero sigue contándolo.',
        sabias='Billy Joel trabajó de verdad tocando el piano en un bar de Los Ángeles durante seis '
               'meses, bajo un nombre falso, y la canción cuenta lo que veía allí cada noche. Los '
               'personajes de la letra existían.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta un-dos-tres con el pie y verás que encaja perfectamente. Es un vals, '
                      'aunque suene a canción de radio.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo que hay que trabajar aquí son los silencios: los dos tiempos del principio y el '
              'compás entero que la izquierda pasa callada. Las notas son pocas.',
        reglas=['UN-DOS-TRES, SIEMPRE', 'LA DERECHA ENTRA EN EL TRES',
                'LA IZQUIERDA CUENTA AUNQUE NO TOQUE'],
        bloques=[
            dict(num=1, titulo='Contar tres, y entrar en el tercero',
                 pista='andamio en Do mayor · el silencio ocupa dos tercios del ejercicio',
                 sistemas=[
                     dict(cap='a) dos tiempos callado y uno tocando · cuenta en voz alta',
                          events=[sil('h'), n('C4'), sil('h'), n('D4'),
                                  sil('h'), n('E4')],
                          bars=3),
                     dict(cap='b) y ahora entrando en el tres y siguiendo en el uno siguiente',
                          events=[sil('h'), n('E4'), n('D4', 'h'), n('C4'),
                                  n('D4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UN COMPÁS CALLADO ES MÁS DIFÍCIL QUE UNO TOCADO',
                 texto='Cuando tocas, la propia música te dice por dónde vas. Cuando callas, no hay '
                       'nada que te lo diga, y el compás se hace corto o largo según los nervios. La '
                       'solución no es contar más rápido ni más despacio: es contar SIEMPRE, tocando '
                       'y callando, con el mismo tono de voz. Un pianista que cuenta solo cuando no '
                       'toca no está contando: está adivinando.'),
            dict(num=2, titulo='La melodía del principio',
                 pista='cc. 1–3 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) los compases 1 y 2, con el silencio de entrada',
                          events=[sil('h'), n('F4'), n('F4', 'h'), n('G4'), n('F4', 'h.')],
                          bars=3),
                     dict(cap='b) y el compás 3, donde aparecen las dos primeras corcheas',
                          events=[n('F4', 'h')] + corch(['F4', 'E4']) + [n('F4', 'h.')],
                          bars=2, show_time=False),
                     dict(cap='c) y los tres seguidos, que es la primera frase entera',
                          events=[sil('h'), n('F4'), n('F4', 'h'), n('G4'), n('F4', 'h')] +
                                 corch(['F4', 'E4']),
                          bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: dos notas, y mucho silencio',
                 pista='cc. 1–2 · medidos en tu partitura · la quinta Do-Sol',
                 sistemas=[
                     dict(cap='a) el acorde solo, una vez por compás, para colocar la mano',
                          events=[ac(('C3', 'G3'), 'h.'), ac(('C3', 'G3'), 'h.'),
                                  ac(('C3', 'G3'), 'h.')],
                          bars=3, clef='bass'),
                     dict(cap='b) y ahora con el compás callado en medio · cuenta los tres tiempos',
                          events=[sil('h.'), ac(('C3', 'G3'), 'h.'),
                                  sil('h.'), ac(('C3', 'G3'), 'h.')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y las dos manos: la derecha entra en el tres y la izquierda en el uno',
                          events=[sil('h'), ac(('F4',)), ac(('C3', 'G3', 'F4'), 'h'), ac(('G4',)),
                                  ac(('F4',), 'h'), ac(('F4',), 'e'), ac(('E4',), 'e')],
                          bars=3, manos='sostiene', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Piano Man · para casa',
            intro='Quince minutos al día. Es una pieza de contar: hay más tiempos callados que '
                  'tocados en los tres primeros compases, y ahí está todo el trabajo.',
            bloques=[
                plan((4, 'Contar un-dos-tres en voz alta, con el pie, sin tocar'),
                     (4, 'La derecha: entrar en el tres, cc. 1 y 2'),
                     (4, 'La izquierda: el acorde Do-Sol y el compás callado'),
                     (3, 'Los tres primeros compases con las dos manos')),
                metronomo('Empieza a ♩ = 60 y déjalo ahí toda la semana.',
                          'Tu partitura no trae número de metrónomo: este es de trabajo. En una '
                          'pieza de silencios, subir la velocidad no arregla nada.'),
                figuras([('h', 'blanca'), ('q', 'negra'), ('e', 'corchea'),
                         ('h.', 'blanca con puntillo'), ('Rh', 'silencio de blanca')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='las cinco están en tus tres primeros compases'),
                diferencias([sil('h'), n('F4'), n('F4', 'h'), n('G4')],
                            [sil('h'), n('F4'), n('F4', 'h'), n('E4')],
                            cuantas=1,
                            titulo='Busca la diferencia',
                            pista='arriba, tus compases 1 y 2 medidos · abajo, con un cambio'),
                escribir(titulo='Copia aquí el compás 1, con su silencio de blanca',
                         pista='y luego tócalo cinco veces contando un-dos-tres en voz alta'),
                para_clase('Los tres primeros compases con las dos manos. Trae dicho en voz alta el '
                           'compás en el que la izquierda no toca: quiero oír cómo lo cuentas.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 78, 'F4', 'C3',
    'los silencios: dos tiempos al principio y un compás entero abajo',
    desde=4, time_sig=(3, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
