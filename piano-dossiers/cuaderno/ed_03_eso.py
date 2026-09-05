# -*- coding: utf-8 -*-
"""Eso que tú me das — pieza 3 de Eduard. Formato ADULTO.

   Medido sobre el PDF de su carpeta (Jarabe de Palo, "Parte 1", 1 pagina):

     - 4/4 y detras de la clave no hay nada.
     - UN SOLO PENTAGRAMA, el tercero y el ultimo. A partir de la 4 ya entran
       las dos manos.
     - Trae **cifrado** encima del pentagrama —C, G, Am, C— y la **letra**
       debajo, en mayusculas. Es la primera pieza del cuaderno con letras de
       acorde, y por eso toca explicar que no son notas.
     - La melodia del principio, medida a 300 ppp:

         c. 1   Do5 · Sol4 · Do5 · Sol4 · Do5
                negra, negra, dos corcheas unidas y negra
         c. 2   Si4 · (silencio de negra) · Si4 · Do5 · Si4

   UNA NOTA SOBRE LA MEDICION. `medir_arranque` se deja la PRIMERA nota de este
   compas: esta edicion pega la cifra de compas a la musica y el salto de
   cabecera se la come. Se miro ampliada del todo y el compas 1 son CINCO notas,
   no cuatro — ademas la aritmetica lo confirma, porque con cuatro el compas
   sale de tres tiempos en un 4/4. La lectura buena esta anotada en
   `auditar_alturas.MIRADAS`, que es donde va lo que se mira a ojo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, sil, corch, plan, metronomo, objetivo, cifrado,
                      nombres, diferencias, escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1, medido. Cita literal.
ARRANQUE = [n('C5'), n('G4')] + corch(['C5', 'G4']) + [n('C5')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=3, nivel='iniciación',
    slug='EsoQueTuMeDas', formato='adulto',
    titulo_corto='Eso que tú me das', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Eso que tu me das.pdf'),
    yt='https://www.youtube.com/results?search_query=eso+que+tu+me+das+jarabe+de+palo+piano',

    ficha=dict(
        titulo='Eso que tú me das',
        autor='Jarabe de Palo · Pau Donés · parte 1',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Manos', 'Solo la derecha'), ('Extras', 'Letra y cifrado'),
               ('Acordes', 'C · G · Am')],
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás, medido en tu partitura. La mano va y viene entre las dos '
                   'mismas teclas.',
        armonia=dict(
            titulo='Dos teclas, y unas letras encima',
            tarjetas=[
                ('EL CIFRADO', 'C · G · Am',
                 'Esas letras de encima del pentagrama NO son notas: son acordes, y le dicen a '
                 'un guitarrista qué tocar. A ti te avisan de cuándo cambia la armonía.'),
                ('LA MELODÍA', 'Do y Sol',
                 'El compás entero va y viene entre esas dos teclas. Es un salto de quinta, y se '
                 'coge con el uno y el cinco sin mover la mano.'),
                ('LA LETRA', 'Va debajo',
                 'Cada sílaba va debajo de su nota. Decirla en voz alta mientras tocas es la '
                 'manera más rápida de que el ritmo salga solo.'),
                ('EL SILENCIO', 'En el compás 2',
                 'Un silencio de negra en medio de la frase. Un tiempo callado, y se cuenta.'),
            ],
            pie='Esta es la última pieza de un solo pentagrama. A partir de la siguiente entran '
                'las dos manos, así que aprovecha para dejar la lectura muy asentada.',
        ),
        ritmos=[
            ('LA DERECHA', 'el compás 1, medido · va y viene entre Do y Sol',
             ARRANQUE, OCRE, 'treble', None),
            ('Y EL SIGUIENTE', 'el compás 2, medido · con un silencio en medio',
             [n('B4'), sil('q')] + corch(['B4', 'C5']) + [n('B4')], AZUL, 'treble', None),
        ],
        especial=[
            'Un solo pentagrama: la izquierda todavía no toca.',
            'Encima del pentagrama hay letras de acorde: C, G, Am.',
            'Debajo va la letra de la canción, sílaba a sílaba.',
            'Compás de 4/4, y no hay ni un sostenido ni un bemol.',
            'El compás 1 va y viene entre dos teclas: Do y Sol.',
            'En el compás 2 hay un silencio de negra en mitad de la frase.',
        ],
        reto='El salto de Do a Sol, una y otra vez, sin mirarse la mano. Es corto pero se repite '
             'tantas veces que cualquier tensión en la muñeca se nota enseguida.',
        truco='Coloca el uno en el Sol y el cinco en el Do y no muevas la mano de ahí en todo el '
              'compás. Si tienes que buscar la tecla cada vez, es que la mano se está moviendo.',
        sabias='Pau Donés escribió esta canción cuando ya estaba enfermo, y va justo de eso: de '
               'agradecer. La grabó en 2020, unos meses antes de morir.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la voz repite las dos mismas notas casi todo el rato: eso es '
                      'lo que vas a tocar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí lo nuevo no son las notas —solo hay dos— sino el salto entre ellas y las '
              'letras de acorde de arriba. Se trabaja el salto hasta que salga sin mirar.',
        reglas=['LA MANO NO SE MUEVE DE SITIO', 'EL UNO EN SOL Y EL CINCO EN DO',
                'DI LA LETRA EN VOZ ALTA'],
        bloques=[
            dict(num=1, titulo='El salto, sin mirarse la mano',
                 pista='andamio en Do mayor · coloca los cinco dedos y no los muevas',
                 sistemas=[
                     dict(cap='a) primero despacio, mirando la tecla de destino ANTES de saltar',
                          events=[n('G4'), n('C5'), n('G4'), n('C5')],
                          bars=1),
                     dict(cap='b) y ahora sin mirar: la mano ya sabe dónde está',
                          events=[n('G4'), n('C5'), n('C5'), n('G4'),
                                  n('G4'), n('C5'), n('G4'), n('G4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ SON LAS LETRAS DE ENCIMA',
                 texto='C, G, Am… son cifrado americano: la letra dice el acorde y no la nota. C '
                       'es el acorde de Do mayor, G el de Sol mayor y Am el de La menor —la "m" '
                       'pequeña quiere decir menor—. Tú de momento no las tocas: te sirven para '
                       'saber cuándo cambia el color de la canción, que es justo donde suele '
                       'cambiar también la melodía.'),
            dict(num=2, titulo='El compás 1, tal y como está escrito',
                 pista='c. 1 · medido en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) primero todo en negras, para verlo sin prisa',
                          events=[n('C5'), n('G4'), n('C5'), n('G4')],
                          bars=1),
                     dict(cap='b) y con su ritmo, dos veces seguidas: las del medio valen media',
                          events=ARRANQUE + [n('G4'), n('C5')] + corch(['G4', 'C5']) + [n('G4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='El silencio del compás 2',
                 pista='c. 2 · medido · un tiempo callado en mitad de la frase',
                 sistemas=[
                     dict(cap='a) el mismo dibujo, pero empezando en el silencio',
                          events=[sil('q'), n('B4')] + corch(['B4', 'C5']) + [n('B4')],
                          bars=1),
                     dict(cap='b) y ahora con el silencio en su sitio, que es donde cuesta',
                          events=[n('B4'), sil('q')] + corch(['B4', 'C5']) +
                                 [n('B4'), n('A4'), sil('q'), n('A4', 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Eso que tú me das · para casa',
            intro='Quince minutos al día. Es la última de un pentagrama: si acabas la semana '
                  'leyendo esta hoja sin pararte, la siguiente con las dos manos entra sola.',
            bloques=[
                plan((4, 'El salto Sol-Do, ida y vuelta, sin mirarte la mano'),
                     (4, 'El compás 1 con su ritmo, diciendo la letra'),
                     (4, 'El compás 2, contando el silencio en voz alta'),
                     (3, 'Los dos seguidos, y luego la página entera')),
                metronomo('Empieza a ♩ = 66 y sube de cuatro en cuatro.',
                          'La canción original va bastante más lenta de lo que parece: no corras.'),
                objetivo('Saltar de Sol a Do sin mirar. Si al final de la semana lo haces con los '
                         'ojos cerrados cinco veces seguidas, está conseguido.'),
                cifrado(['C', 'G', 'Am'],
                        ['¿Cuál de los tres es menor, y en qué se nota al mirarlo?',
                         '¿Cuál de los tres empieza por la misma nota que la melodía?'],
                        titulo='Las letras que trae tu partitura',
                        pista='escribe las tres notas de cada uno, de grave a agudo'),
                nombres(['C5', 'G4', 'C5', 'B4', 'A4', 'B4', 'C5'],
                        titulo='Los nombres, sin mirar la partitura',
                        pista='son las notas que usa esta primera frase'),
                diferencias([n('C5'), n('G4'), n('C5'), n('G4'), n('C5')],
                            [n('C5'), n('G4'), n('C5'), n('A4'), n('C5')],
                            cuantas=1,
                            titulo='Busca la diferencia',
                            pista='arriba, tu compás 1 · abajo, con un cambio'),
                escribir(titulo='Copia aquí el compás 2, con su silencio',
                         pista='y luego tócalo cinco veces contando en voz alta'),
                para_clase('La página entera y el salto Sol-Do. Trae marcado el sitio donde se te '
                           'descoloca el silencio, si es que se te descoloca.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 63, 'C5', 'C3',
    'la mano abierta entre Sol y Do, que es el salto de la pieza',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
