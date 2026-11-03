# -*- coding: utf-8 -*-
"""Have Yourself a Merry Little Christmas — pieza 10 de Martina (NAVIDAD, una semana).
   ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Sadie King,
   Musescore, 1 página VECTORIAL, medida con cabezas.medir y mirada a 200 ppp):

     - Detrás de la clave no hay nada. 4/4. Trae ♩ = 100, "mp" en el primer
       compás y la palabra "Pedal" debajo de la clave de fa.
     - 30 compases en una página. Trae un regulador de apertura (c. 21), uno de cierre
       (c. 28), "ritardando" hacia el final, un arpegiado en el penúltimo compás y
       barra final.
     - Ninguna figura más corta que la corchea. Notas ligadas en los cc. 7-8, 23-24 y 27-28.
     - MEDIDO, mano derecha:
       c. 1 y c. 3: Do4 · Mi4 · Sol4 · Do5 (negras)
       c. 2: Sol4 · Fa4 · Mi4 · Re4 (corcheas) · Do4 · Re4 (negras)
       c. 4: Sol4 (redonda)
       c. 5: Mi4 · Sol4 · Do5 · Mi5 (negras)
       c. 6: Re5 · Do5 · Si4 · La4 (corcheas) · Sol4 · Fa4 (negras)
       c. 7 y 8: Mi4 (redonda), ligada a la del c. 8
   La izquierda va en acordes de tres notas, en redondas y blancas: se da como andamio.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, reto, plan, metronomo, escribir, diferencias,
                      acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: cc. 1-8 (derecha)
C1 = [n('C4'), n('E4'), n('G4'), n('C5')]
C2 = [n('G4', 'e'), n('F4', 'e'), n('E4', 'e'), n('D4', 'e'), n('C4'), n('D4')]
C4 = [n('G4', 'w')]
C5 = [n('E4'), n('G4'), n('C5'), n('E5')]
C6 = [n('D5', 'e'), n('C5', 'e'), n('B4', 'e'), n('A4', 'e'), n('G4'), n('F4')]
C7 = [dict(pitch='E4', dur='w', lig=True)]
C8 = [n('E4', 'w')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=10, nivel='iniciación', slug='HaveYourself',
    formato='adulto',
    titulo_corto='Have Yourself a Merry...', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source',
                           'Have-yourself-a-merry-little-christmas'),
    yt='https://www.youtube.com/results?search_query=have+yourself+a+merry+little+christmas+piano',

    ficha=dict(
        titulo='Have Yourself a Merry Little Christmas',
        autor='Hugh Martin y Ralph Blane · arreglo de Sadie King · NAVIDAD',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 100'), ('Intensidad', 'mp'),
               ('Pedal', 'Marcado')],
        titulo_ritmos='Los cc. 1-4, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: la subida de Do a Do, el giro de corcheas del '
                   'c. 2 y la redonda del c. 4. Abajo, andamio: acordes de tres notas.',
        armonia=dict(
            titulo='Una canción tranquila donde manda el sonido, no la velocidad',
            tarjetas=[
                ('LA SUBIDA', 'Do, Mi, Sol, Do',
                 'Empieza con las cuatro negras de un acorde de Do subiendo, y el c. 2 las '
                 'devuelve por escalones: Sol, Fa, Mi, Re en corcheas, y Do, Re.'),
                ('EL PEDAL', 'Y el mp',
                 'Debajo de la clave de fa pone "Pedal" y el primer compás lleva mp, medio '
                 'suave. Es una pieza para tocar con el sonido pegado, no cortado.'),
                ('LOS REGULADORES', 'Abren y cierran',
                 'Hacia el c. 21 un regulador abre el volumen y hacia el c. 28 otro lo cierra. '
                 'Se hacen con el brazo, no con la mano: el sonido crece sin apretar.'),
                ('EL FINAL', 'Más y más lento',
                 'La partitura trae "ritardando" hacia el final, y el último acorde se toca '
                 'arpegiado, de abajo arriba, antes de quedarse sonando.'),
            ],
            pie='Es una página, 30 compases, y la mitad son notas largas. Lo difícil es '
                'sostenerlas con intención: tocar poco y que suene a mucho.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-4 · medido', C1 + C2 + C1 + C4, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · un acorde de tres notas',
             [ac(('C3', 'E3', 'G3'), 'w'), ac(('C3', 'F3', 'A3'), 'h'),
              ac(('C3', 'E3', 'G3'), 'h')],
             AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 4/4. Trae ♩ = 100 y mp en el primer compás.',
            'Debajo de la clave de fa pone "Pedal".',
            'Hay un regulador que abre y otro que cierra.',
            'Hacia el final aparece la palabra "ritardando".',
            'El último acorde se toca arpegiado, de abajo arriba.',
        ],
        reto='Tocarla entera de memoria y con el sonido unido, sin que se oiga ninguna nota '
             'cortada entre una y otra.',
        truco='Toca la melodía sola y cántala por dentro: si cantando respiras, tocando '
              'también. La izquierda, con mucho menos volumen que la derecha.',
        sabias='La canción es de 1944 y salió en una película con Judy Garland. La frase "until '
               'then we\'ll have to muddle through somehow" la cambió Frank Sinatra por una más '
               'alegre cuando la grabó, porque la original le parecía demasiado triste.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la versión de Judy Garland y después la de Sinatra: son la misma '
                      'melodía con dos humores. Tu partitura se toca con el primero.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí no se estudia la velocidad, se estudia el sonido: cada nota larga se '
              'escucha hasta que se apaga, y la siguiente entra donde termina la anterior.',
        reglas=['LA MELODÍA, SIEMPRE LA MÁS FUERTE', 'EL PEDAL SE CAMBIA CON CADA ACORDE',
                'LAS LARGAS, HASTA EL FINAL'],
        bloques=[
            dict(num=1, titulo='La entrada y el giro de corcheas',
                 pista='cc. 1-2 · medidos sobre tu partitura · mp en el primer compás',
                 sistemas=[
                     dict(cap='a) las cuatro negras que suben, con el mp del primer compás · '
                              'toca sin separar una nota de otra',
                          events=[dict(n('C4'), matiz='mp')] + C1[1:], bars=1),
                     dict(cap='b) y el c. 2: corcheas que bajan por escalones y dos negras de '
                              'remate · sin cortar el sonido entre una y otra',
                          events=C2, bars=1, show_time=False),
                     dict(cap='c) la misma forma, otra nota de partida · andamio · el giro baja '
                              'cuatro escalones y se queda en la tónica',
                          events=[n('F4'), n('A4'), n('C5'), n('F5'),
                                  n('C5', 'e'), n('Bb4', 'e'), n('A4', 'e'), n('G4', 'e'),
                                  n('F4'), n('G4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La nota larga ligada de los cc. 7 y 8',
                 pista='cc. 7-8 · medidos sobre tu partitura · dos redondas del mismo Mi unidas '
                       'por una ligadura',
                 sistemas=[
                     dict(cap='a) la ligadura une las dos redondas: se toca una vez y suena '
                              'ocho tiempos · no se vuelve a pulsar',
                          events=C7 + C8, bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA LIGADURA NO SE VUELVE A TOCAR',
                 texto='Dos notas iguales unidas por una línea curva son una sola nota larga: la '
                       'segunda no se pulsa. Si la tocas dos veces, cambias lo que pone tu '
                       'partitura. Cuenta los ocho tiempos con la tecla bajada y suéltala al '
                       'final del segundo compás.'),
            dict(num=3, titulo='El pedal, con la izquierda',
                 pista='andamio · la marca de pedal abarca el acorde entero · se cambia al '
                       'cambiar de acorde',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) tres acordes de tres notas con pedal · el pedal se levanta y se '
                              'vuelve a bajar justo cuando entra el siguiente',
                          events=[ac(('F2', 'A2', 'C3'), 'w'), ac(('G2', 'B2', 'D3'), 'w'),
                                  ac(('C3', 'E3', 'G3'), 'w')],
                          bars=3, clef='bass', pedal=3),
                 ]),
            dict(num=4, titulo='Un regulador que abre',
                 pista='andamio · el regulador de tu partitura del c. 21 va hacia el c. 22 · '
                       'aquí, para que el brazo lo conozca',
                 sistemas=[
                     dict(cap='a) cuatro negras con el volumen creciendo · empiezan suaves y '
                              'acaban fuertes sin apretar la mano',
                          events=[n('C4'), n('E4'), n('G4'), n('C5')],
                          bars=1, matiz='p', cresc=3),
                 ]),
        ] + bloques_extra('Do mayor', 10, 'E4', 'C3',
                          'sonido unido, pedal limpio y notas largas escuchadas',
                          desde=5, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Have Yourself a Merry Little Christmas · para casa',
            intro='Es la semana corta de Navidad: diez o quince minutos al día. No hay nada rápido, '
                  'y por eso se nota todo.',
            bloques=[
                reto('Tocar los cc. 1-8 sin que se oiga ningún corte entre una nota y la '
                     'siguiente, tres veces seguidas.',
                     'Grábate con el móvil y escúchate con los ojos cerrados: cada corte que '
                     'oigas es un punto en contra. Tres veces limpias y ganas.'),
                plan((3, 'La derecha sola, cc. 1-4, con el sonido unido'),
                     (3, 'Los acordes de la izquierda, uno por compás'),
                     (4, 'Los cc. 1-8 con las dos manos y el pedal'),
                     (4, 'La grabación y la escucha crítica')),
                metronomo('Empieza a ♩ = 60 con la derecha sola y sube de cinco en cinco hasta '
                          '100, que es el número que trae tu partitura.',
                          'Es una canción lenta: si a una velocidad se te corta el sonido, no '
                          'subas, baja cinco y repítelo.',
                          titulo='A qué velocidad te sale'),
                escribir(titulo='Copia el c. 1 de la derecha',
                         pista='cuatro negras que suben · y escribe debajo el nombre de cada '
                               'nota'),
                diferencias(list(C1),
                            [n('C4'), n('E4'), n('G4'), n('E5')],
                            cuantas=1,
                            titulo='Busca la diferencia',
                            pista='arriba, el c. 1 de tu partitura · abajo, el mismo compás con '
                                  'una nota cambiada'),
                acuerdate('Una canción lenta no es una canción fácil: no hay donde esconder el '
                          'error. Si una nota suena fea, se oye hasta el final.',
                          etiqueta='LO LENTO SE OYE TODO'),
                para_clase('Los cc. 1-8 con el pedal y el sonido unido, y la grabación en el móvil '
                           'para escucharla juntos. Dime cuál es el corte que más te cuesta.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
