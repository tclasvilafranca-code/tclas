# -*- coding: utf-8 -*-
"""Can't Stop the Feeling! (Justin Timberlake) — pieza 12 de Alan.
   ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (1 página, imagen a 79 ppp,
   mirada a 200 ppp). OJO: la página viene con la música GIRADA 90 grados, de
   modo que hay que mirarla de lado; para el álbum se genera una copia con la
   música derecha sobre un A4 vertical (`_vertical`).

     - Detrás de la clave no hay nada. 4/4. No trae tempo ni intensidad.
     - 17 compases en tres sistemas, con barra final.
     - Casi todo son silencios entre notas sueltas: silencios de blanca, de
       negra y de corchea. Ninguna figura más corta que la corchea.
     - MEDIDO, mano derecha:
       c. 1: silencio de blanca · silencio de corchea · Mi4 · Re4 · Do4 (corcheas)
       c. 2: Mi4 · Mi4 (corcheas) · silencio de negra · silencio de negra ·
             Do4 · Do4 (corcheas)
       c. 3: silencio de blanca · silencio de corchea · Do4 · Do4 · Re4 (corcheas)
       c. 4: Mi4 · Re4 · Do4 · Re4 · Mi4 · Re4 · Do4 · Do4 (ocho corcheas)
       c. 6: Mi4 · Sol4 (corcheas) · silencio de negra · silencio de negra · Do4 · Do4
       c. 10: Do4 · silencio · Do4 · silencio · Do4 · silencio (corcheas) y silencio de negra
       c. 11: cuatro Do4 (corcheas) · Mi4 (negra) · silencio de negra
       c. 17: Do4 (negra con puntillo) · silencio de corchea · silencio de blanca
     - MEDIDO, mano izquierda:
       c. 1: silencio de compás entero.
       c. 2: silencio de blanca · silencio de corchea · La3 (corchea) · silencio de negra
       c. 3: La3 (negra) · silencio de negra · silencio de blanca
       c. 10: silencio de corchea y La3 (corchea) tres veces, y después La3 · Sol3 · La3 (corcheas)
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, reto, plan, rodear, unir, colorear, acuerdate,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

ORIGEN = os.path.join(HERE, '..', 'students', 'alan', 'source', "CAN'T STOP THE FEELLING.")
VERTICAL = os.path.join(HERE, '..', 'students', 'alan', 'source', 'CANT_STOP_vertical.pdf')


def _vertical(src, dst):
    """La partitura de Drive trae la música girada: copia con la música derecha."""
    from pypdf import PdfReader, PdfWriter, Transformation, PageObject
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return dst
    pag = PdfReader(src).pages[0]
    w, h = float(pag.mediabox.width), float(pag.mediabox.height)
    s = w / h
    nueva = PageObject.create_blank_page(width=w, height=h)
    nueva.merge_transformed_page(
        pag, Transformation().rotate(-90).translate(0, w).scale(s, s)
        .translate(0, h - w * s - 90))
    sal = PdfWriter()
    sal.add_page(nueva)
    with open(dst, 'wb') as f:
        sal.write(f)
    return dst


if os.path.exists(ORIGEN):
    _vertical(ORIGEN, VERTICAL)

# MEDIDO: cc. 1-4 (derecha)
C1 = [sil('h'), sil('e'), n('E4', 'e'), n('D4', 'e'), n('C4', 'e')]
C2 = [n('E4', 'e'), n('E4', 'e'), sil('q'), sil('q'), n('C4', 'e'), n('C4', 'e')]
C3 = [sil('h'), sil('e'), n('C4', 'e'), n('C4', 'e'), n('D4', 'e')]
C4 = [n('E4', 'e'), n('D4', 'e'), n('C4', 'e'), n('D4', 'e'),
      n('E4', 'e'), n('D4', 'e'), n('C4', 'e'), n('C4', 'e')]
# MEDIDO: izquierda, cc. 1-2
L1 = [sil('w')]
L2 = [sil('h'), sil('e'), n('A3', 'e'), sil('q')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=12, nivel='intermedio', slug='CantStop',
    formato='adulto',
    titulo_corto="Can't Stop the Feeling!", time_sig=(4, 4), key_sig=None,
    partitura=VERTICAL,
    yt='https://www.youtube.com/results?search_query=cant+stop+the+feeling+piano+easy',

    ficha=dict(
        titulo="Can't Stop the Feeling!",
        autor='Justin Timberlake · versión fácil',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Derecha', 'Do, Re, Mi'),
               ('Páginas', 'Una')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: la derecha entra tras un silencio de tiempo y '
                   'medio. Abajo, medido: la izquierda no toca el c. 1 y en el c. 2 solo una corchea.',
        armonia=dict(
            titulo='Una pieza en la que mandan los silencios',
            tarjetas=[
                ('LOS SILENCIOS', 'Más que notas',
                 'Casi cada compás tiene un silencio de blanca, de negra o de corchea. La pieza '
                 'se toca contando los huecos: lo que no suena es lo que da el ritmo.'),
                ('LA DERECHA', 'Do, Re, Mi',
                 'En los cuatro primeros compases solo hay Do4, Re4 y Mi4, todas corcheas. En el c. 6 '
                 'sube hasta un Sol4. Las notas no son el problema: lo es el cuándo.'),
                ('LA IZQUIERDA', 'Una nota suelta',
                 'En los cc. 2 y 3 toca un La3 entre silencios: una corchea y una negra. Entra '
                 'justo en el hueco donde la derecha calla.'),
                ('LA PÁGINA', 'Viene de lado',
                 'La partitura original viene con la música girada 90 grados: en el álbum la tienes '
                 'ya derecha, y si abres la de Drive, gira la pantalla antes de empezar.'),
            ],
            pie='Son 17 compases, una página, sin armadura y sin tempo. La dificultad es entrar a '
                'tiempo tras los silencios sin que se te vaya el pulso.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 1-2 · medido', L1 + L2, AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 4/4 y no trae número de metrónomo.',
            'La derecha entra tras un silencio de blanca y uno de corchea.',
            'La izquierda no toca en el c. 1, y en el c. 2 solo toca una corchea.',
            'El c. 4 son ocho corcheas seguidas, la única frase sin silencios.',
            'La partitura de Drive viene girada: hay que darle la vuelta al papel.',
        ],
        reto='Entrar a tiempo después de un silencio de blanca y uno de corchea. La entrada cae '
             'en la segunda mitad del tercer tiempo, y ahí no suena ningún clic.',
        truco='Cuenta "uno-dos-tres-y" con la boca y entra con la última "y". Si te adelantas, '
              'es que has contado "tres" en vez de "y".',
        sabias='Can\'t Stop the Feeling! salió en 2016 para la película Trolls y fue número uno '
               'en muchos países. Justin Timberlake la cantó con la idea de que no se pudiera '
               'estar quieto al oírla.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el ritmo del principio y dilo con las palmas: la entrada cae '
                      'después de un hueco, y ese hueco es lo que hace que quieras bailar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí se estudia el hueco, no la nota. Primero se cuenta el silencio en voz alta '
              'y después se toca lo que viene detrás.',
        reglas=['EL SILENCIO SE CUENTA EN VOZ ALTA', 'LA ENTRADA CAE EN UNA "Y"',
                'LAS MANOS SE ALTERNAN'],
        bloques=[
            dict(num=1, titulo='La entrada tras el silencio, c. 1',
                 pista='c. 1 · medido sobre tu partitura · un silencio de blanca, uno de corchea y '
                       'tres corcheas',
                 sistemas=[
                     dict(cap='a) los dos silencios ocupan dos tiempos y medio · cuenta "uno, '
                              'dos, tres-y" y entra con la "y" del tres',
                          events=C1, bars=1),
                     dict(cap='b) el mismo ritmo sobre otras tres notas · andamio · para '
                              'comprobar que no es de memoria',
                          events=[sil('h'), sil('e'), n('G4', 'e'), n('F4', 'e'), n('E4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='Dos corcheas, dos silencios, dos corcheas, c. 2',
                 pista='c. 2 · medido sobre tu partitura · el pulso no se detiene en los silencios',
                 sistemas=[
                     dict(cap='a) dos corcheas, dos silencios de negra y dos corcheas · los '
                              'silencios duran lo mismo que las notas',
                          events=C2, bars=1),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UN SILENCIO ES MÁS DIFÍCIL QUE UNA NOTA',
                 texto='Una nota se oye y el oído se orienta solo. Un silencio no se oye, y hay '
                       'que contarlo por dentro sin que ningún sonido te avise. Por eso estudia '
                       'siempre con el metrónomo y con la boca: di "uno, dos, tres-y" en voz '
                       'alta y toca justo donde cae la "y".'),
            dict(num=3, titulo='Ocho corcheas seguidas, c. 4',
                 pista='c. 4 · medido sobre tu partitura · la única frase sin silencios',
                 sistemas=[
                     dict(cap='a) Mi, Re, Do, Re, Mi, Re, Do, Do · ocho corcheas pareadas, sin '
                              'una nota más fuerte que otra',
                          events=C4, bars=1),
                 ]),
            dict(num=4, titulo='La nota suelta de la izquierda, cc. 2-3',
                 pista='cc. 2-3 · medidos sobre tu partitura · la izquierda toca poco y tiene que '
                       'estar a tiempo',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) un La3 entre silencios · una corchea en el c. 2 y una negra '
                              'en el c. 3 · y todo lo demás es silencio',
                          events=L2 + [n('A3'), sil('q'), sil('h')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=5, titulo='Las dos manos del c. 2, alternándose',
                 pista='c. 2 · medido sobre tu partitura · la izquierda cae en el hueco de la '
                       'derecha',
                 sistemas=[
                     dict(cap='a) mientras la derecha calla, la izquierda toca un La3 corto · no '
                              'se tocan nunca a la vez',
                          events=[n('E4', 'e'), n('E4', 'e'), sil('q'), sil('e'),
                                  ac(('A3',), 'e'), n('C4', 'e'), n('C4', 'e')],
                          bars=1, manos='dobla'),
                 ]),
            dict(num=6, titulo='La última nota, c. 17',
                 pista='c. 17 · medido sobre tu partitura · una negra con puntillo y dos silencios',
                 sistemas=[
                     dict(cap='a) la negra con puntillo dura uno y medio · después, un silencio de '
                              'corchea y otro de blanca · acaba en silencio, no en nota',
                          events=[n('C4', 'q.'), sil('e'), sil('h')], bars=1),
                 ]),
        ] + bloques_extra('Do mayor', 12, 'E4', 'C3',
                          'entrar a tiempo tras los silencios de blanca y de corchea',
                          desde=7, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="Can't Stop the Feeling! · para casa",
            intro='Veinte minutos al día, y los primeros cinco sin piano: contando huecos en voz '
                  'alta.',
            bloques=[
                reto('Tocar los cc. 1-4 con las entradas a tiempo tres veces seguidas, sin que la '
                     'entrada del c. 1 se te adelante.',
                     'Pon el metrónomo a 66 y cuenta "uno, dos, tres-y" en voz alta. Anota cuántas '
                     'veces seguidas entras bien: el objetivo son tres limpias, no tres en total.'),
                plan((4, 'Contar los silencios del c. 1 en voz alta, sin tocar'),
                     (4, 'La derecha sola, cc. 1-4, a ♩ = 66'),
                     (4, 'La izquierda sola: solo el La3 de los cc. 2 y 3'),
                     (8, 'Las dos manos, cc. 1-4, sin pararte')),
                rodear([list(C1),
                        [sil('h'), sil('e'), n('E4', 'e'), n('E4', 'e'), n('C4', 'e')],
                        [sil('h'), sil('e'), n('E4', 'e'), n('D4', 'e'), n('C4', 'e')],
                        [sil('h'), sil('e'), n('E4', 'e'), n('D4', 'e'), n('D4', 'e')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='dos son el c. 1 y el c. 5 de tu partitura · los otros llevan una nota '
                             'cambiada'),
                unir([('Silencio de blanca', 'dos golpes sin tocar'),
                      ('Silencio de corchea', 'medio golpe sin tocar'),
                      ('Corchea', 'medio golpe, dos por cada negra'),
                      ('Negra con puntillo', 'un golpe y medio')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                colorear([n('E4', 'e'), n('D4', 'e'), n('C4', 'e'), n('E4'), n('C4', 'q.'),
                          n('D4', 'e'), n('C4', 'e')],
                         ['Las corcheas, de azul.',
                          'La negra, de rojo.',
                          'La negra con puntillo, de verde.'],
                         titulo='Colorea según la figura',
                         pista='son figuras de los cc. 1, 11 y 17 de tu partitura, con notas '
                               'nuestras'),
                acuerdate('Un silencio no es una pausa para distraerte: es tiempo que se cuenta. '
                          'Si lo cuentas entero, la nota siguiente cae sola en su sitio.',
                          etiqueta='EL SILENCIO SE CUENTA'),
                para_clase('Los cc. 1-4 con las dos manos y cuántas entradas seguidas has '
                           'conseguido a tiempo. Y dime en qué compás te cuesta más entrar: '
                           'empezamos por ahí.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
