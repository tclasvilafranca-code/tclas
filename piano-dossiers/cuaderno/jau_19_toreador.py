# -*- coding: utf-8 -*-
"""Toreador (Bizet, de Carmen) — pieza 19 de Jaume. ADULTO exigente, sin cifrado.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Gilbert
   DeBenedetti, "Level Four", edición Gradimi, 1 página, 13 compases), a
   200-400 ppp:

     - FA MAYOR: un bemol detrás de la clave. El compás se escribe con una C
       (4/4). Arriba pone "March time" y la dinámica f. No trae metrónomo.
     - Lleva digitación impresa, staccato en los acordes de la izquierda, una
       NOTA DE ADORNO en el c. 2, semicorcheas, reguladores, matices (f, p, mf),
       una barra de repetición con casilla 1 y casilla 2, y un signo > sobre el
       acorde final.
     - MEDIDO, mano derecha (cabeza a cabeza a 200-400 ppp):
       c. 1: Do5 (negra), Re5 (corchea con puntillo), Do5 (semicorchea), La4 y
             La4 (negras)
       c. 2: nota de adorno Si♭4, La4 (corchea con puntillo), Sol4 (semicorchea),
             La4 (corchea con puntillo), Si♭4 (semicorchea) y La4 (blanca)
       c. 3: Si♭4 (negra), Sol4 (corchea con puntillo), Do5 (semicorchea) y
             La4 (blanca)
       c. 11 (casilla 1): La4 y Sol4 (negras) y ocho semicorcheas seguidas:
             Fa4 (staccato) · Do4 · Re4 · Mi4 | Fa4 · Sol4 · La4 · Si♭4
       c. 12 (casilla 2): La4 · Sol4 · Fa4 (staccato) y silencio de negra
     - La nota de adorno la dibuja el motor desde esta pieza (`gracia=`).
   Mismo archivo que el de José María, Isaac, Mercè, Nel y Eduard.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, metronomo, escribir, diferencias,
                       acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'


def st(p, d='q'):
    return dict(pitch=p, dur=d, art='staccato')


# MEDIDO: cc. 1-3
C1 = [n('C5'), n('D5', 'e.'), n('C5', 's'), n('A4'), n('A4')]
C2 = [dict(pitch='A4', dur='e.', gracia='Bb4'), n('G4', 's'), n('A4', 'e.'), n('Bb4', 's'),
      n('A4', 'h')]
C3 = [n('Bb4'), n('G4', 'e.'), n('C5', 's'), n('A4', 'h')]
# MEDIDO: c. 11 (casilla 1) y c. 12 (casilla 2)
C11 = [n('A4'), n('G4'), st('F4', 's'), n('C4', 's'), n('D4', 's'), n('E4', 's'),
       dict(pitch='F4', dur='s', cresc=3), n('G4', 's'), n('A4', 's'), n('Bb4', 's')]
C12 = [n('A4'), n('G4'), st('F4'), sil('q')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=19, nivel='intermedio', slug='Toreador',
    formato='adulto',
    titulo_corto='Toreador · Carmen', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'Toreador.Bizet'),
    yt='https://www.youtube.com/results?search_query=toreador+song+carmen+piano+easy',

    ficha=dict(
        titulo='Toreador',
        autor='Georges Bizet · de la ópera Carmen · arr. Gilbert DeBenedetti · Level Four',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4'),
               ('Carácter', 'March time · f'), ('Armadura', 'Un bemol'),
               ('Estructura', 'Con casillas')],
        titulo_ritmos='Los tres primeros compases, medidos',
        pie_ritmos='Arriba, la derecha de los cc. 1-3 medida sobre tu partitura, con el largo-corto de '
                   'la marcha. Abajo, andamio: los acordes de dos notas que la izquierda toca en '
                   'staccato.',
        armonia=dict(
            titulo='Una marcha: el largo-corto, la nota de adorno y las casillas',
            tarjetas=[
                ('EL LARGO-CORTO', 'Largo y corto',
                 'Es el gesto de marcha: la larga se lleva tres cuartos del tiempo y la corta, el '
                 'cuarto que queda. Aparece en los cc. 1, 2 y 3 y es la firma de la pieza.'),
                ('LA NOTA DE ADORNO', 'Nota pequeña',
                 'En el c. 2 hay una nota pequeña con una raya en la plica antes de la primera '
                 'nota. Se toca muy corta, justo antes del tiempo, y no cuenta en el compás.'),
                ('LAS CASILLAS', '1 y 2',
                 'La pieza acaba en una barra de repetición con dos finales: la primera vez se '
                 'toca el c. 11, con ocho semicorcheas seguidas, y la segunda, el c. 12.'),
                ('EL STACCATO', 'En la izquierda',
                 'Los acordes de dos notas de la izquierda llevan punto: se tocan secos, sin '
                 'pegar un acorde con el siguiente. Es lo que marca el paso.'),
            ],
            pie='Son 13 compases en una página. La edición trae la digitación impresa, y los '
                'reguladores y matices (f, p y mf) están dibujados: se estudian con ellos desde '
                'el primer día.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-3 · medido', C1 + C2 + C3, OCRE, 'treble', FA),
            ('MANO IZQUIERDA', 'andamio · acordes de dos notas en staccato',
             [dict(pitches=['F3', 'A3'], dur='q', art='staccato')] * 8 +
             [dict(pitches=['G3', 'Bb3'], dur='q', art='staccato')] * 2 +
             [dict(pitches=['F3', 'A3'], dur='q', art='staccato')] * 2,
             AZUL, 'bass', FA),
        ],
        especial=[
            'Detrás de la clave hay un bemol: todos los Si van a la tecla negra.',
            'El compás se escribe con una C: es 4/4. Pone "March time" y f, pero no trae metrónomo.',
            'El largo-corto del c. 1 vuelve en los cc. 2 y 3.',
            'El c. 2 empieza con una nota de adorno: una nota pequeña, con raya, antes de la nota.',
            'Lleva semicorcheas, staccato, reguladores y matices dibujados, y la edición imprime la digitación.',
            'Acaba en una barra de repetición con casilla 1 y casilla 2.',
        ],
        reto='Que el largo-corto salga igual las tres veces: la semicorchea del final de cada grupo '
             'tiende a adelantarse, y entonces la marcha se vuelve un galope.',
        truco='Cuenta el compás en semicorcheas, 1-2-3-4, y pon la corta en el 4 del tiempo, nunca '
              'en el 3. Si la corta se te adelanta, estás tocando un puntillo de menos.',
        sabias='La música es de Bizet, de la ópera Carmen, estrenada en París en 1875. La '
               'melodía es la de la canción del torero Escamillo, y por eso va como una marcha.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo la izquierda marca el paso con acordes cortos y la derecha '
                      'canta encima con el largo-corto. Las dos manos van en el mismo golpe.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Es una marcha y se estudia como tal: primero el paso de la izquierda, después el '
              'largo-corto de la derecha, y solo entonces juntas. La nota de adorno y las '
              'semicorcheas del c. 11 son lo que se deja para el final.',
        reglas=['EL LARGO-CORTO', 'EL ADORNO NO CUENTA', 'STACCATO EN LA IZQUIERDA'],
        bloques=[
            dict(num=1, titulo='El largo-corto del c. 1',
                 pista='c. 1 · medido sobre tu partitura · negra, corchea con puntillo, semicorchea '
                       'y dos negras',
                 sistemas=[
                     dict(cap='a) el compás tal y como está · la corta cae justo antes de la nota '
                              'siguiente',
                          events=C1, bars=1, key_sig=FA, matiz='f'),
                     dict(cap='b) el mismo compás con la corta y la larga al revés · NO es lo que '
                              'pone tu partitura: es para oír lo que la marcha NO hace',
                          events=[n('C5'), n('D5', 's'), n('C5', 'e.'), n('A4'), n('A4')],
                          bars=1, show_time=False, key_sig=FA),
                     dict(cap='c) el mismo ritmo sobre una sola nota · andamio, para que la mano '
                              'aprenda el golpe sin pensar en las notas',
                          events=[n('A4'), n('A4', 'e.'), n('A4', 's'), n('A4'), n('A4')],
                          bars=1, show_time=False, key_sig=FA),
                 ]),
            dict(num=2, titulo='La nota de adorno del c. 2',
                 pista='c. 2 · medido sobre tu partitura · la nota pequeña no suma tiempo: el '
                       'compás sigue valiendo cuatro',
                 sistemas=[
                     dict(cap='a) el compás con su nota de adorno, un Si♭ pequeño antes del La · '
                              'se toca muy corta y pegada al La',
                          events=C2, bars=1, key_sig=FA),
                     dict(cap='b) el mismo compás SIN el adorno · NO es lo que pone tu partitura: '
                              'sirve para ver que el resto es idéntico',
                          events=[n('A4', 'e.'), n('G4', 's'), n('A4', 'e.'), n('Bb4', 's'),
                                  n('A4', 'h')],
                          bars=1, show_time=False, key_sig=FA),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA NOTA DE ADORNO NO CUENTA',
                 texto='La nota pequeña con raya no tiene valor en el compás: si sumas los tiempos '
                       'de las notas grandes, siguen dando cuatro. Se toca justo antes de la nota '
                       'principal y MUY corta, y el peso de la frase sigue estando en la grande. '
                       'Si la pones larga, la marcha pierde el golpe.'),
            dict(num=3, titulo='El c. 3',
                 pista='c. 3 · medido sobre tu partitura · el largo-corto vuelve en el segundo '
                       'tiempo, ahora con una negra antes',
                 sistemas=[
                     dict(cap='a) negra, largo-corto y blanca · el Si♭ de la primera nota es la '
                              'tecla negra de la armadura',
                          events=C3, bars=1, key_sig=FA),
                 ]),
            dict(num=4, titulo='La izquierda: acordes de dos notas en staccato',
                 pista='andamio sobre Fa mayor · el staccato quiere decir seco, no rápido',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) un acorde de Fa en cada golpe, con punto · después de cada uno, la '
                              'mano suelta la tecla',
                          events=[dict(pitches=['F3', 'A3'], dur='q', art='staccato')] * 4,
                          bars=1, clef='bass', key_sig=FA),
                     dict(cap='b) Fa y Sol menor, dos golpes cada uno · cambia de acorde sin '
                              'dejar de soltar',
                          events=[dict(pitches=['F3', 'A3'], dur='q', art='staccato')] * 2 +
                                 [dict(pitches=['G3', 'Bb3'], dur='q', art='staccato')] * 2,
                          bars=1, clef='bass', show_time=False, key_sig=FA),
                 ]),
            dict(num=5, titulo='Las casillas y las ocho semicorcheas',
                 pista='cc. 11-12 · medido sobre tu partitura · la primera vez se toca el c. 11 y '
                       'la segunda el c. 12',
                 sistemas=[
                     dict(cap='a) casilla 1: dos negras y ocho semicorcheas, dos grupos de cuatro · '
                              'el primero baja al Do con un punto, el segundo sube con un '
                              'regulador',
                          events=C11, bars=1, repetir='cierra', casilla='1', key_sig=FA),
                     dict(cap='b) casilla 2: la segunda vez se salta el c. 11 y se toca este · es '
                              'el final: la última nota es corta',
                          events=C12, bars=1, casilla='2', show_time=False, key_sig=FA),
                 ]),
            dict(num=6, titulo='Los matices y los reguladores',
                 pista='andamio sobre Fa mayor · tu partitura lleva f al principio, p y mf después, y '
                       'reguladores bajo los compases',
                 sistemas=[
                     dict(cap='a) cuatro notas que suben, con un regulador que abre · el sonido '
                              'crece sin que cambie la velocidad',
                          events=[n('F4'), n('A4'), n('C5'), n('F5')], bars=1, key_sig=FA,
                          matiz='p', cresc=3),
                     dict(cap='b) las mismas cuatro bajando, con un regulador que cierra · acaba en '
                              'piano',
                          events=[n('F5'), n('C5'), n('A4'), n('F4')], bars=1, show_time=False,
                          key_sig=FA, matiz='f', dim=3),
                 ]),
        ] + bloques_extra(FA, 19, 'F4', 'F3',
                          'la semicorchea del largo-corto y las casillas de repetición',
                          desde=7, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Toreador · para casa',
            intro='Veinte minutos al día. La pieza es corta: el trabajo es de limpieza, no de '
                  'cantidad.',
            bloques=[
                reto('Tocar el largo-corto de los cc. 1-3 sin que la semicorchea se adelante, tres '
                     'veces seguidas, con el metrónomo.',
                     'Pon el metrónomo, cuenta en semicorcheas y marca el golpe de la corta con '
                     'el pie. Si se te adelanta una sola vez, empieza otra vez desde el principio.'),
                plan((5, 'El paso de la izquierda: acordes de dos notas en staccato'),
                     (6, 'La derecha de los cc. 1-3 contando en semicorcheas'),
                     (5, 'La nota de adorno del c. 2, diez veces'),
                     (4, 'Las casillas 1 y 2, cada una por su lado')),
                metronomo('Empieza muy despacio, con el metrónomo marcando la negra, y sube de seis '
                          'en seis cuando el largo-corto salga tres veces seguidas.',
                          'Tu partitura pone "March time" pero no trae número de metrónomo: la '
                          'meta la eliges tú y la apuntas a lápiz.',
                          titulo='A qué velocidad te sale'),
                escribir(titulo='Escribe el nombre de las notas del c. 1 de tu partitura',
                         pista='son cinco notas · y escribe debajo cuántos tiempos suma cada una'),
                diferencias(C1,
                            [n('D5'), n('D5', 'e'), n('C5', 'e'), n('A4'), n('G4')],
                            cuantas=4,
                            titulo='Busca las diferencias',
                            pista='arriba, tu compás 1 medido · abajo, un compás parecido con cuatro '
                                  'cosas cambiadas'),
                acuerdate('La nota de adorno no cuenta en el compás: se toca muy corta, justo antes '
                          'de la nota principal, y el compás sigue sumando cuatro tiempos.',
                          etiqueta='RECUERDA EL ADORNO'),
                para_clase('Los cc. 1-3 con las dos manos y el largo-corto sin adelantarse. Y dime '
                           'cuántas veces seguidas te sale limpio: si es menos de tres, lo '
                           'miramos juntos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
