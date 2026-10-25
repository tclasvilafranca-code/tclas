# -*- coding: utf-8 -*-
"""Santa Claus Is Coming to Town — pieza 8 de Alan (NAVIDAD, una semana).
   ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (J. Fred Coots, 2 páginas,
   imagen a 53 ppp), mirado a 220 ppp:

     - Detrás de la clave no hay nada. 4/4. Trae ♩ = 130.
     - 36 compases: 19 en la primera página y 17 en la segunda. Termina con barra final.
     - Trae dedos impresos y algún sostenido o bemol escrito delante de una nota.
     - Ninguna figura más corta que la corchea: negras, blancas, corcheas sueltas
       y en parejas, negras con puntillo, silencios.
     - MEDIDO, mano derecha:
       c. 1 y c. 2 (iguales): Do5 · Sol4 · La4 · Mi4 (negras)
       c. 3: cinco acordes de Do-Mi-Sol (corchea · negra · corchea · negra · negra)
       c. 4: acorde de Do-Mi-Sol en blanca · silencio de negra · silencio de corchea ·
             Sol4 (corchea)
       c. 5: Mi4 · Fa4 (corcheas) · Sol4 (negra) · Sol4 (negra con puntillo) · Sol4 (corchea)
     - MEDIDO, mano izquierda: c. 1 y c. 2, Do3 en redonda; c. 3, Sol2 en redonda.
   El resto de la izquierda se da como andamio.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, plan, escalera, rodear, escribir,
                      verdadero_falso, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: cc. 1-5 (derecha)
C1 = [n('C5'), n('G4'), n('A4'), n('E4')]
C3 = [ac(('C4', 'E4', 'G4'), 'e'), ac(('C4', 'E4', 'G4')), ac(('C4', 'E4', 'G4'), 'e'),
      ac(('C4', 'E4', 'G4')), ac(('C4', 'E4', 'G4'))]
C4 = [ac(('C4', 'E4', 'G4'), 'h'), sil('q'), sil('e'), n('G4', 'e')]
C5 = [n('E4', 'e'), n('F4', 'e'), n('G4'), n('G4', 'q.'), n('G4', 'e')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=8, nivel='intermedio', slug='SantaClaus',
    formato='adulto',
    titulo_corto='Santa Claus Is Coming', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source',
                           'SANTA CLAUS IS COMING TO TOWN.pdf'),
    yt='https://www.youtube.com/results?search_query=santa+claus+is+coming+to+town+piano+easy',

    ficha=dict(
        titulo='Santa Claus Is Coming to Town',
        autor='J. Fred Coots · NAVIDAD',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 130'), ('Dedos', 'Impresos'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Los cc. 1-4, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: la entrada, los acordes del c. 3 y el final del '
                   'c. 4. Abajo, andamio: acorde, silencio, acorde, silencio.',
        armonia=dict(
            titulo='Una melodía que todo el mundo se sabe, y un 130 que no perdona',
            tarjetas=[
                ('LA ENTRADA', 'Do, Sol, La, Mi',
                 'Cuatro negras que bajan y suben: Do5, Sol4, La4, Mi4. Se repiten en el c. 2. '
                 'Son las primeras que la gente reconoce, así que tienen que salir limpias.'),
                ('LOS ACORDES', 'Do-Mi-Sol',
                 'En el c. 3 la derecha toca cinco acordes de tres notas seguidos: corchea, '
                 'negra, corchea, negra y negra. Cuenta "uno-y, dos, tres-y, cuatro".'),
                ('EL TEMPO', '♩ = 130',
                 'Tu partitura trae el número escrito: 130 negras por minuto, bastante '
                 'deprisa. Es una pieza que se gana subiendo el metrónomo.'),
                ('LA IZQUIERDA', 'Larga y luego corta',
                 'Al principio la izquierda aguanta redondas, y después cambia a acordes con '
                 'silencios entre ellos. El silencio también se toca.'),
            ],
            pie='Son 36 compases en dos páginas, con un final de redonda y una nota aguda de '
                'remate. Lo que más cuesta no es la melodía, sino llegar a 130 sin atropellarse.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-4 · medido', C1 + C1 + C3 + C4, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · acorde, silencio, acorde, silencio',
             [ac(('C3', 'E3', 'G3'), 'q'), sil('q'), ac(('C3', 'E3', 'G3'), 'q'), sil('q')],
             AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 4/4 y la partitura trae ♩ = 130.',
            'El c. 3 de la derecha son cinco acordes de tres notas.',
            'El c. 4 acaba con un silencio de negra, uno de corchea y una corchea.',
            'Trae dedos impresos y alguna alteración escrita delante de una nota.',
            'Son 36 compases en dos páginas.',
        ],
        reto='Llegar a ♩ = 130, el número que pone tu partitura, sin que se atropelle ni una '
             'corchea de los cc. 3 y 4.',
        truco='Sube de diez en diez. Si a una velocidad fallas dos veces seguidas, no subas: '
              'baja diez y sácala limpia antes de intentarlo otra vez.',
        sabias='La música es de J. Fred Coots y la letra de Haven Gillespie. Se estrenó en la radio '
               'en 1934, y se vendieron cientos de miles de copias de la partitura en muy pocos '
               'días: es de las canciones navideñas que más se han cantado.',
        qr=dict(titulo='Escúchala',
                texto='Escucha con la partitura delante y señala dónde caen los acordes del c. 3. '
                      'Si los encuentras de oído, ya sabes dónde ponerlos.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Es una pieza corta y rápida: se estudia por trozos pequeños y se junta cuando cada '
              'trozo sale solo. Esta semana es la única de Navidad que tiene el metrónomo pegado.',
        reglas=['EL 130 SE GANA POR ESCALONES', 'LOS ACORDES DEL C. 3, DE UN GOLPE',
                'EL SILENCIO TAMBIÉN SE CUENTA'],
        bloques=[
            dict(num=1, titulo='La entrada: cuatro negras',
                 pista='cc. 1-2 · medido sobre tu partitura · Do, Sol, La, Mi',
                 sistemas=[
                     dict(cap='a) las cuatro negras de la entrada · cada una dura un golpe de '
                              'metrónomo',
                          events=C1, bars=1),
                     dict(cap='b) el mismo dibujo en otras notas · andamio · para comprobar que '
                              'no lo tocas de memoria',
                          events=[n('D5'), n('A4'), n('B4'), n('F4')], bars=1,
                          show_time=False),
                 ]),
            dict(num=2, titulo='Los acordes del c. 3',
                 pista='cc. 3-4 · medidos sobre tu partitura · tres notas, cinco golpes',
                 sistemas=[
                     dict(cap='a) los cinco acordes de Do-Mi-Sol · las tres notas bajan a la vez, '
                              'no una detrás de otra',
                          events=C3, bars=1),
                     dict(cap='b) el c. 4: acorde largo, dos silencios y la corchea que entra '
                              'sola · el silencio de corchea se cuenta',
                          events=C4, bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE SUBE POR ESCALONES',
                 texto='El metrónomo no es un examen, es una escalera. Si a 90 te sale limpio y a '
                       '110 se te cae un compás, el trozo se queda a 110 hasta que salga limpio '
                       'tres veces seguidas. Saltar a 130 con el trozo flojo solo enseña a '
                       'equivocarse más rápido.'),
            dict(num=3, titulo='Un golpe largo y una nota de remate',
                 pista='c. 5 · medido sobre tu partitura · la negra con puntillo y la corchea que '
                       'sigue',
                 sistemas=[
                     dict(cap='a) dos corcheas, una negra, una negra con puntillo y una corchea · '
                              'la corchea de después completa el compás',
                          events=C5, bars=1),
                 ]),
            dict(num=4, titulo='Las dos manos, el principio',
                 pista='cc. 1-2 · la derecha es MEDIDA · la redonda de la izquierda también',
                 sistemas=[
                     dict(cap='a) la izquierda aguanta el Do mientras la derecha canta · la '
                              'redonda no se suelta hasta el final del compás',
                          events=[ac(('C3', 'C5'), 'q'), ac(('G4',)), ac(('A4',)),
                                  ac(('E4',))],
                          bars=1, manos='sostiene'),
                 ]),
        ] + bloques_extra('Do mayor', 8, 'E4', 'C3',
                          'llegar a 130 sin atropellar las corcheas',
                          desde=5, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Santa Claus Is Coming to Town · para casa',
            intro='Es la semana corta de Navidad: diez o quince minutos al día, pero bien '
                  'aprovechados. El objetivo está escrito en tu partitura.',
            bloques=[
                plan((3, 'La entrada de los cc. 1-2, hasta que salga sola'),
                     (4, 'Los cinco acordes del c. 3, de un golpe'),
                     (4, 'El c. 4 con sus dos silencios, contados en voz alta'),
                     (4, 'Los cc. 1-5 con las dos manos')),
                escalera((70, 'la derecha sola, cc. 1-5'),
                         (90, 'las dos manos, cc. 1-5'),
                         (110, 'los cc. 1-8 seguidos'),
                         (130, 'la meta: lo que pone tu partitura'),
                         meta='♩ = 130 es el número impreso en tu partitura. Si llegas, '
                              'apúntalo con la fecha.',
                         titulo='La escalera hasta el 130'),
                rodear([list(C1),
                        [n('C5'), n('G4'), n('A4'), n('F4')],
                        [n('C5'), n('A4'), n('G4'), n('E4')],
                        list(C1)],
                       titulo='Rodea los dos grupos que son iguales',
                       pista='uno es el c. 1 de tu partitura y otro el c. 2 · los otros dos '
                             'llevan una nota cambiada'),
                escribir(titulo='Copia el c. 4 de la derecha',
                         pista='un acorde largo, dos silencios y una corchea · y escribe debajo '
                               'cuántos golpes ocupa cada cosa'),
                verdadero_falso([
                    'Detrás de la clave hay un sostenido.',
                    'La partitura pone ♩ = 130.',
                    'El c. 3 de la derecha son cinco acordes de tres notas.',
                    'El c. 4 de la derecha termina con un silencio.',
                    'Son 36 compases en dos páginas.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                para_clase('Los cc. 1-8 a la velocidad más alta en la que te salga limpio. Y '
                           'dime cuál es: si es 110, la semana que viene empieza por ahí.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
