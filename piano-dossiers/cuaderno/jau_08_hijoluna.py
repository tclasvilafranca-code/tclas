# -*- coding: utf-8 -*-
"""Hijo de la Luna (Mecano) — pieza 8 de Jaume. Formato ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Unai Karam,
   versión "easy", 3 páginas APAISADAS, 35 compases), mirado a 100 dpi:

     - **UN BEMOL** detrás de la clave (Si♭): Re menor. 6/8.
     - Tempo impreso: **negra con puntillo = 58**.
     - Las tres páginas son apaisadas: en el álbum se giran 90° (hay que girar
       el cuaderno para leerlas, como cualquier partitura ancha).
     - MEDIDO (`medir_arranque`): el c. 1 de la derecha es silencio de corchea ·
       La4 · Sol4 · silencio de corchea · Mi4 · Re4, todo corcheas. El c. 2 es
       lo mismo con Fa4 y Sol4 donde estaban La4 y Sol4.
     - La izquierda, en negras con puntillo, una por golpe: Re3 · Do3 en los
       cc. 1 y 3, Si♭2 · Do3 en los cc. 2 y 4. Es Re menor, Si♭ y Do: la
       armonía de toda la canción.
     - **Semicorcheas** desde el c. 5 (la primera tanda: Re4 · Mi4 · Fa4 · La4
       tras un silencio de corchea), medidas: 36 pares de barras dobles.
     - Del c. 17 al c. 24 hay un puente con becuadros (Si♮) y un La♭, y en
       los cc. 27-28 sostenidos delante de las notas.
     - El último compás es un acorde arpegiado (la línea ondulada).
     - Digitación impresa en algunos compases.

   Comparte archivo con la carpeta de Aída (arreglo de Unai Karam): lo literal
   coincide y lo inventado no puede. Aquí el trabajo va por **contar el 6/8 en
   dos** y por las semicorcheas, que entran antes de que el oído se haya
   acostumbrado al balanceo.
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

# los dos primeros compases de la derecha, tal como los trae la partitura
D_1 = [sil('e'), n('A4', 'e'), n('G4', 'e'), sil('e'), n('E4', 'e'), n('D4', 'e')]
D_2 = [sil('e'), n('F4', 'e'), n('G4', 'e'), sil('e'), n('E4', 'e'), n('D4', 'e')]
# la primera tanda de semicorcheas (c. 5) y la del c. 9
D_5 = [sil('e'), n('D4', 's'), n('E4', 's'), n('F4', 's'), n('A4', 's'),
       n('E4'), n('D4', 'e')]
D_9 = [sil('e'), n('F4', 's'), n('G4', 's'), n('A4', 's'), n('C5', 's'),
       n('Bb4', 'e'), n('G4', 'e'), sil('e')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=8, nivel='intermedio', slug='HijoDeLaLuna',
    formato='adulto',
    titulo_corto='Hijo de la Luna', time_sig=(6, 8), key_sig='Re menor',
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           'Hijo-de-la-luna-Mecano.'),
    yt='https://www.youtube.com/results?search_query=hijo+de+la+luna+mecano+piano+easy',

    ficha=dict(
        titulo='Hijo de la Luna',
        autor='Mecano · arreglo de Unai Karam · versión fácil',
        datos=[('Tonalidad', 'Re menor'), ('Compás', '6/8'),
               ('Tempo', '♩. = 58'), ('Figura corta', 'Semicorchea'),
               ('Páginas', 'Tres')],
        titulo_ritmos='La entrada y las primeras semicorcheas',
        pie_ritmos='Arriba, medido sobre tu partitura: silencio, La y Sol, silencio, Mi y Re, todo '
                   'corcheas. Abajo, leído del c. 9: una tanda de semicorcheas.',
        armonia=dict(
            titulo='Un 6/8 muy despacio, y con semicorcheas',
            tarjetas=[
                ('♩. = 58', 'Muy lento',
                 'La negra con puntillo a 58 es el tempo más lento del cuaderno. A esa '
                 'velocidad cada compás dura poco más de tres segundos y el silencio de corchea '
                 'del principio se hace largo.'),
                ('6/8', 'Se cuenta en dos',
                 'Seis corcheas por compás, agrupadas de tres en tres: dos golpes grandes, uno en '
                 'el Re y otro en el Do. La izquierda lo dice solo, una negra con puntillo por '
                 'golpe.'),
                ('LAS SEMICORCHEAS', 'Desde el c. 5',
                 'Cuatro notas en el sitio de una negra. Entran antes de que el oído se haya '
                 'acostumbrado al balanceo, y por eso hay que estudiarlas aparte.'),
                ('EL PUENTE', 'cc. 17-24',
                 'Becuadros y un La♭ delante de las notas, y dobles notas en la izquierda. Es la '
                 'única parte de la pieza que no se aprende por la frase de arriba.'),
            ],
            pie='Con tu base, el 6/8 no es el problema: lo es el tempo. A ♩. = 58 no hay dónde '
                'esconderse: cada nota suena el tiempo que dura, y si dudas, se oye.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', D_1, OCRE, 'treble', None),
            ('MANO DERECHA', 'c. 9 · leído: otra tanda de semicorcheas', D_9, AZUL, 'treble',
             None),
        ],
        especial=[
            'Un bemol detrás de la clave (Si♭): es Re menor.',
            'Pone "♩. = 58", que es la negra con puntillo: menos de un golpe por segundo.',
            'Las tres páginas van apaisadas: gira el cuaderno para leerlas.',
            'La izquierda toca una negra con puntillo por golpe: Re, Do, Si♭, Do.',
            'Desde el c. 5 aparecen las semicorcheas, en grupos de cuatro.',
            'El último compás es un acorde arpegiado, con la línea ondulada a la izquierda.',
        ],
        reto='Que las semicorcheas del c. 5 no se atropellen. Vienen después de un silencio de '
             'corchea y justo cuando el oído ya se había acostumbrado al balanceo de las '
             'corcheas: la mano acelera sin que te enteres.',
        truco='Estudia el c. 5 con las cuatro semicorcheas a ritmo de corchea (una nota cada '
              'golpe del metrónomo), y después juntas de dos en dos. A ♩. = 58 las cuatro caben '
              'en un solo golpe: no se tocan más rápido, se tocan más seguidas.',
        sabias='La canción es de Mecano, de 1986, y la letra la escribió José María Cano: cuenta una '
               'leyenda gitana en la que la luna es la protagonista. En directo se tocaba siempre '
               'con muy poco acompañamiento, como esta versión.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la entrada de la voz: respira antes de cada frase, justo en el sitio '
                      'donde tu mano derecha tiene un silencio de corchea.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia a ♩. = 58 o más despacio, que es el tempo de la pieza, y en tres '
              'tiempos de trabajo: los cuatro primeros compases, las semicorcheas y el puente.',
        reglas=['CONTAR EN DOS', 'LAS SEMICORCHEAS, JUNTAS DE DOS EN DOS',
                'EL PUENTE, APARTE'],
        bloques=[
            dict(num=1, titulo='Los dos primeros compases de la derecha',
                 pista='cc. 1-2 · MEDIDO sobre tu partitura · seis corcheas por compás, con dos '
                       'silencios',
                 sistemas=[
                     dict(cap='a) cuenta "uno-y-a, dos-y-a" y deja que los silencios respiren · el '
                              'segundo compás cambia solo una nota respecto del primero',
                          events=D_1 + D_2,
                          bars=2),
                 ]),
            dict(num=2, titulo='La izquierda: una negra con puntillo por golpe',
                 pista='cc. 1-4 · leído de tu partitura · Re, Do, Si♭, Do',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) dos golpes por compás · deja sonar cada nota los tres tiempos '
                              'enteros y cámbiala a la vez que la mano derecha',
                          events=[n('D3', 'q.'), n('C3', 'q.'), n('Bb2', 'q.'), n('C3', 'q.')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=3, titulo='Las dos manos, los dos primeros compases',
                 pista='cc. 1-2 · leído de tu partitura · el bajo suena mientras la derecha respira',
                 sistemas=[
                     dict(cap='a) el bajo entra en el uno y en el cuatro y la derecha en medio · '
                              'si se te corta el bajo en el silencio, estás contando corcheas',
                          events=[n('D3', 'e'), n('A4', 'e'), n('G4', 'e'),
                                  n('C3', 'e'), n('E4', 'e'), n('D4', 'e'),
                                  n('Bb2', 'e'), n('F4', 'e'), n('G4', 'e'),
                                  n('C3', 'e'), n('E4', 'e'), n('D4', 'e')],
                          bars=2, manos='sostiene'),
                 ]),
            dict(tipo='nota',
                 etiqueta='CUENTA EN DOS, NO EN SEIS',
                 texto='Seis corcheas por compás se leen como dos golpes de tres. Si cuentas seis, '
                       'cada nota parece una pregunta; si cuentas dos, la frase tiene dos '
                       'respiraciones y se mueve sola. El tempo impreso, ♩. = 58, está dado al '
                       'golpe grande: un uno y un dos por compás.'),
            dict(num=4, titulo='Las primeras semicorcheas, c. 5',
                 pista='cc. 5 y 6 · leído de tu partitura · el c. 6 es la versión lenta del mismo '
                       'dibujo',
                 sistemas=[
                     dict(cap='a) el c. 5 tal como está escrito · cuatro semicorcheas seguidas, una '
                              'negra y una corchea',
                          events=D_5, bars=1),
                     dict(cap='b) el c. 6: las mismas notas a la mitad de velocidad · aprende primero '
                              'este y después el de arriba',
                          events=[sil('e'), n('D4', 'e'), n('E4', 'e'),
                                  sil('e'), n('F4', 'e'), n('G4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=5, titulo='La misma figura en otras notas',
                 pista='andamio sobre el c. 5 · el mismo dibujo, medio tono más abajo y más arriba',
                 sistemas=[
                     dict(cap='a) tres tandas de semicorcheas empezando en notas distintas · el '
                              'dibujo es el mismo, pero la mano ya no puede confiar en el sitio',
                          events=[sil('e'), n('E4', 's'), n('F4', 's'), n('G4', 's'),
                                  n('Bb4', 's'), n('F4'), n('E4', 'e'),
                                  sil('e'), n('F4', 's'), n('G4', 's'), n('A4', 's'),
                                  n('C5', 's'), n('G4'), n('F4', 'e')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL PUENTE DE LOS CC. 17 A 24',
                 texto='Es la única parte de la pieza con becuadros, un La bemol y dobles notas '
                       'en la izquierda. No se estudia con el resto: marca a lápiz cada alteración '
                       'antes de tocar y toca solo esos ocho compases hasta que el oído '
                       'reconozca la sensación de que la tonalidad se tuerce y vuelve.'),
        ] + bloques_extra('Re menor', 8, 'A4', 'D3',
                          '6/8 muy lento: la corchea es el pulso, la negra con puntillo es el '
                          'compás',
                          desde=6, time_sig=(6, 8)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Hijo de la Luna · para casa',
            intro='Veinte minutos, y ni uno a la velocidad de la pieza hasta que las semicorcheas '
                  'salgan solas.',
            bloques=[
                reto('Las semicorcheas del c. 5, sin atropellarse a ♩. = 58.',
                     'Tócalas de una en una al principio y de dos en dos después; nunca juntas a '
                     'la vez hasta que las dos mitades salgan solas.'),
                plan((4, 'Los cuatro primeros compases, contando en dos'),
                     (6, 'El c. 5 y el c. 6, despacio, de dos en dos'),
                     (5, 'La izquierda sola, una negra con puntillo por golpe'),
                     (5, 'Las dos manos, hasta el c. 8')),
                metronomo('Empieza a ♩. = 40 y sube de dos en dos; la meta es ♩. = 58.',
                          'Eso es lo que pone tu partitura: ♩. = 58.',
                          titulo='A qué velocidad te sale'),
                escribir(titulo='Copia las semicorcheas del c. 5',
                         pista='cópialas tal cual de tu partitura y tócalas diez veces solas'),
                diferencias(D_5,
                            [sil('e'), n('D4', 's'), n('E4', 's'), n('G4', 's'), n('A4', 's'),
                             n('E4'), n('D4', 'e')],
                            1,
                            titulo='Busca la diferencia en las semicorcheas',
                            pista='el de arriba es tu c. 5 · el de abajo ha cambiado una nota'),
                acuerdate('Las tres páginas van apaisadas: gira el cuaderno antes de ponerte a '
                          'estudiar, no mientras. Si lo giras a mitad de pieza, pierdes el sitio.',
                          etiqueta='GIRA EL CUADERNO'),
                para_clase('Las semicorcheas del c. 5 a la velocidad que te salgan, y el puente '
                           'de los cc. 17-24 con las alteraciones marcadas. Si el 6/8 se te va a '
                           'seis, tráelo: se arregla contando en dos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
