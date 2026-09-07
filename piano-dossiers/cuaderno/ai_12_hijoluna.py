# -*- coding: utf-8 -*-
"""Hijo de la Luna, de Mecano — pieza 12 de Aida. Formato ADULTO exigente.

   Cierra la cuarta etapa. El 6/8 ya se conto en el villancico; aqui vuelve,
   pero en MODO MENOR y muy despacio, y con la mano derecha entrando siempre
   despues de un silencio de corchea. Es la primera pieza del cuaderno en la
   que Aida tiene un numero de metronomo impreso y muy lento: 58 la negra con
   puntillo, o sea menos de un golpe por segundo.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de Unai Karam,
   3 paginas, vectorial). Es solo suya: no la comparte ningun otro alumno.

     - Detras de la clave hay **UN BEMOL** (Si bemol): Re menor.
     - **6/8**.
     - Trae tempo impreso: **negra con puntillo = 58**.
     - Trae **digitacion impresa** (un 5 sobre la primera nota, un 1 en el
       c. 5). Es un dato de SU edicion, no nuestro: en estas hojas los dedos
       los escribe ella.
     - Lleva semicorcheas, medidas: 36 pares de barras dobles en el PDF. La
       primera tanda esta en el c. 5.

   LAS ALTURAS de los cuatro primeros compases, medidas a 150 ppp sobre las
   cinco lineas de cada pentagrama:

       DERECHA    c. 1  silencio de corchea · La4 · Sol4 · silencio de corchea ·
                        Mi4 · Re4   (todo corcheas)
                  c. 2  silencio de corchea · Fa4 · Sol4 · silencio de corchea ·
                        Mi4 · Re4
                  c. 3  igual que el 1
                  c. 4  igual que el 2

       IZQUIERDA  c. 1  Re3 · Do3      c. 2  Si bemol2 · Do3
                  c. 3  Re3 · Do3      c. 4  Si bemol2 · Do3
                  todas negras con puntillo: una por golpe.

   Cada compas cierra en 3: seis corcheas arriba y dos negras con puntillo
   abajo. Y el dibujo de la izquierda —Rem, Sib, Do— es la armonia de la
   cancion entera, repetida sin cambiar.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, semi, reto, plan, metronomo, unir,
                      colorear, acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los cuatro primeros compases de la DERECHA, medidos. Cita literal.
D1 = [sil('e')] + corch(['A4', 'G4']) + [sil('e')] + corch(['E4', 'D4'])
D2 = [sil('e')] + corch(['F4', 'G4']) + [sil('e')] + corch(['E4', 'D4'])

# El c. 5, medido: es donde entran las SEMICORCHEAS. El primer golpe se reparte
# en un silencio de corchea y cuatro semicorcheas; el segundo, en una negra y
# una corchea. Cita literal.
D5 = [sil('e')] + semi(['D4', 'E4', 'F4', 'A4']) + [n('E4'), n('D4', 'e')]

# Y la IZQUIERDA: dos negras con puntillo por compas, una por golpe. Medido.
I1 = [n('D3', 'q.'), n('C3', 'q.')]
I2 = [n('Bb2', 'q.'), n('C3', 'q.')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=12, nivel='intermedio',
    slug='HijoDeLaLuna', formato='adulto',
    titulo_corto='Hijo de la Luna', time_sig=(6, 8), key_sig='Re menor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Hijo de la luna.pdf'),
    yt='https://www.youtube.com/results?search_query=hijo+de+la+luna+piano',

    ficha=dict(
        titulo='Hijo de la Luna',
        autor='Mecano · José María Cano · arr. Unai Karam',
        datos=[('Tonalidad', 'Re menor'), ('Compás', '6/8'),
               ('Tempo', '♩. = 58'), ('Armadura', 'Un bemol'),
               ('Izquierda', 'Dos por compás')],
        titulo_ritmos='Los compases 1 y 2, medidos',
        pie_ritmos='Arriba, los dos primeros compases de la derecha MEDIDOS en tu partitura: cada '
                   'grupo de tres empieza con un silencio de corchea. Abajo, la izquierda de esos '
                   'mismos compases, una negra con puntillo por golpe.',
        armonia=dict(
            titulo='Tres acordes y ni uno más',
            tarjetas=[
                ('Re menor', 'El de casa',
                 'Re · Fa · La. Es el primero de cada vuelta y el que le da el color triste. La '
                 'izquierda lo toca en el compás 1 y en el 3.'),
                ('Si bemol', 'El de la negra',
                 'Si♭ · Re · Fa. Aquí es donde se nota el bemol de detrás de la clave: ese Si va '
                 'siempre en la tecla negra, en las dos manos y en cualquier octava.'),
                ('Do mayor', 'El que devuelve',
                 'Do · Mi · Sol. Cierra la vuelta y empuja de nuevo hacia el Re menor. Toca los '
                 'tres seguidos y oirás la canción entera en cuatro segundos.'),
                ('EL 6/8 MENOR', 'Dos golpes lentos',
                 'Dos golpes por compás, tres corcheas en cada uno, y a 58 por minuto: cada golpe '
                 'dura más de un segundo. Hay tiempo de sobra para pensar cada nota.'),
            ],
            pie='La izquierda hace Rem · Si♭ · Rem · Do y vuelta a empezar, sin cambiar, durante '
                'casi toda la pieza. Aprendida esa vuelta, la mano izquierda ya no tiene nada nuevo '
                'que aprender en toda la canción: lo que queda es llegar a tiempo.',
        ),
        ritmos=[
            ('DERECHA', 'los cc. 1 y 2, MEDIDOS · cada grupo entra tras un silencio',
             D1 + D2, OCRE, 'treble', 'Re menor'),
            ('IZQUIERDA', 'los mismos dos compases, medidos · una por golpe',
             I1 + I2, AZUL, 'bass', 'Re menor'),
        ],
        especial=[
            'Detrás de la clave hay un bemol: todos los Si se tocan en la tecla negra.',
            'El compás es 6/8: dos golpes, con tres corcheas en cada uno.',
            'El tempo está impreso: negra con puntillo = 58. Es muy lento.',
            'Cada grupo de tres empieza con un silencio de corchea.',
            'La izquierda hace dos negras con puntillo por compás.',
            'Tu edición trae algunos números de dedo impresos.',
            'En el compás 5 hay cuatro semicorcheas seguidas.',
        ],
        reto='Entrar después del silencio, seis veces por compás y a una velocidad en la que el '
             'silencio dura casi medio segundo. Cuanto más lento, más largo se hace el hueco y más '
             'fácil es adelantarse.',
        truco='Cuenta las tres corcheas de cada golpe en voz alta: "uno-DOS-TRES". El silencio es '
              'el "uno", y tú entras en el "DOS". Marca el pie solo en los golpes, que son dos.',
        sabias='José María Cano la escribió en un rato, y en Mecano nadie la quería de single '
               'porque duraba mucho y no tenía estribillo repetido. Acabó siendo la canción '
               'española más versionada fuera de España: hay grabaciones en más de veinte idiomas.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta solo los golpes grandes: dos por compás, muy lentos. Y fíjate en que '
                      'la voz siempre entra un poco después del golpe, nunca encima.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El 6/8 ya lo trabajaste en el villancico. Lo nuevo aquí son dos cosas: el bemol de '
              'la armadura y que cada grupo de tres empieza callado.',
        reglas=['TODOS LOS SI, EN LA TECLA NEGRA', 'DOS GOLPES POR COMPÁS, MUY LENTOS',
                'CADA GRUPO EMPIEZA CON UN SILENCIO'],
        bloques=[
            dict(num=1, titulo='El compás 1, tal y como está escrito',
                 pista='c. 1 · MEDIDO en tu partitura · el silencio abre cada uno de los dos golpes',
                 sistemas=[
                     dict(cap='a) el compás 1 entero · silencio, dos corcheas, silencio, dos '
                              'corcheas',
                          events=list(D1), matiz='mp', bars=1, key_sig='Re menor'),
                     dict(cap='b) y con el hueco relleno, solo para oír lo que ocupa · esto NO es '
                              'lo que pone tu partitura',
                          events=corch(['A4', 'A4', 'G4'], 3) + corch(['E4', 'E4', 'D4'], 3),
                          bars=1, show_time=False, key_sig='Re menor'),
                     dict(cap='c) y los cc. 2 y 3 seguidos · lo único que cambia entre un compás '
                              'y el siguiente es la primera nota',
                          events=D2 + D1, bars=2, show_time=False, key_sig='Re menor'),
                     dict(cap='d) y con el silencio cambiado al segundo golpe · andamio, para que '
                              'la mano no aprenda el hueco de memoria y tenga que contarlo',
                          events=corch(['A4', 'G4', 'F4']) + [sil('e')] + corch(['E4', 'D4']),
                          bars=1, show_time=False, key_sig='Re menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTE SILENCIO CUESTA MÁS QUE OTROS',
                 texto='No es por la figura: un silencio de corchea es de los más cortos que hay. '
                       'Es por la velocidad. A 58 la negra con puntillo, cada golpe dura más de un '
                       'segundo y cada corchea, un tercio de segundo largo. Ese hueco se hace '
                       'eterno, y la mano quiere llenarlo. Cuéntalo con la voz —"uno-DOS-TRES"— y '
                       'entra en el DOS: si lo cuentas, deja de ser un hueco y pasa a ser un sitio.'),
            dict(num=2, titulo='La izquierda: tres acordes que dan la vuelta',
                 pista='cc. 1-4 de la mano izquierda · MEDIDO · una negra con puntillo por golpe',
                 sistemas=[
                     dict(cap='a) los cuatro compases tal y como están · Re, Do, Si bemol, Do, y '
                              'vuelta a empezar',
                          events=I1 + I2 + I1 + I2, bars=4, clef='bass', key_sig='Re menor'),
                     dict(cap='b) y las mismas notas con el acorde entero debajo, para oír de qué '
                              'acorde sale cada una · en tu partitura solo está la nota de abajo',
                          events=[ac(('D3', 'F3', 'A3'), 'q.'), ac(('C3', 'E3', 'G3'), 'q.'),
                                  ac(('Bb2', 'D3', 'F3'), 'q.'), ac(('C3', 'E3', 'G3'), 'q.')],
                          bars=2, clef='bass', show_time=False, key_sig='Re menor'),
                     dict(cap='c) y los tres desplegados nota a nota, para oír de qué está hecho '
                              'cada uno · andamio sobre esos mismos tres acordes',
                          events=corch(['D3', 'F3', 'A3'], 3) + corch(['Bb2', 'D3', 'F3'], 3) +
                                 corch(['C3', 'E3', 'G3'], 3) + corch(['D3', 'F3', 'A3'], 3),
                          bars=2, clef='bass', show_time=False, key_sig='Re menor'),
                 ]),
            dict(num=3, titulo='Las semicorcheas del compás 5',
                 pista='c. 5 · MEDIDO · cuatro semicorcheas dentro del primer golpe',
                 sistemas=[
                     dict(cap='a) el c. 5 tal y como está · el silencio, cuatro notas rápidas y '
                              'después el golpe largo',
                          events=list(D5), bars=1, key_sig='Re menor'),
                     dict(cap='b) y las cuatro semicorcheas sueltas, subiendo y bajando, para '
                              'colocar la mano · andamio sobre las mismas notas',
                          events=semi(['D4', 'E4', 'F4', 'A4']) + [n('A4', 'e')] +
                                 semi(['A4', 'F4', 'E4', 'D4']) + [n('D4', 'e')],
                          bars=1, show_time=False, key_sig='Re menor'),
                     dict(cap='c) y las mismas cuatro empezando un grado más arriba · andamio: si '
                              'salen igual de iguales que las de abajo, ya están',
                          events=semi(['E4', 'F4', 'G4', 'Bb4']) + [n('Bb4', 'e')] +
                                 semi(['Bb4', 'G4', 'F4', 'E4']) + [n('E4', 'e')],
                          bars=1, show_time=False, key_sig='Re menor'),
                 ]),
            dict(num=4, titulo='Las dos manos, con el hueco en su sitio',
                 pista='cc. 1-2 con las dos manos · MEDIDO · la izquierda cae en el silencio de la '
                       'derecha',
                 sistemas=[
                     dict(cap='a) el c. 1 · fíjate en dónde entra cada mano: la izquierda toca '
                              'justo donde la derecha calla',
                          events=[ac(('D3',), 'e'), n('A4', 'e'), n('G4', 'e'),
                                  ac(('C3',), 'e'), n('E4', 'e'), n('D4', 'e')],
                          bars=1, manos='sostiene', key_sig='Re menor'),
                     dict(cap='b) y los cc. 1 y 2 seguidos, que es la vuelta entera de la izquierda',
                          events=[ac(('D3',), 'e'), n('A4', 'e'), n('G4', 'e'),
                                  ac(('C3',), 'e'), n('E4', 'e'), n('D4', 'e'),
                                  ac(('Bb2',), 'e'), n('F4', 'e'), n('G4', 'e'),
                                  ac(('C3',), 'e'), n('E4', 'e'), n('D4', 'e')],
                          bars=2, manos='sostiene', show_time=False, key_sig='Re menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cuatro primeros compases con las dos manos, con el metrónomo a 58 y un '
                       'clic por golpe grande: dos clics por compás. Y no le pongas los dedos que '
                       'trae impresos tu edición sin probarlos: escríbete los tuyos encima a lápiz '
                       'si los otros no te caen bien, que la mano es la tuya.'),
        ] + bloques_extra('Re menor', 103, 'D4', 'D3',
                          'el 6/8 en menor: dos golpes lentos con tres corcheas dentro',
                          desde=5, time_sig=(6, 8), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Hijo de la Luna · para casa',
            intro='Quince minutos al día. La pieza es lenta y corta de material: casi todo el '
                  'trabajo es entrar a tiempo después del silencio.',
            bloques=[
                reto('Entrar después del silencio de corchea sin adelantarse, seis veces por '
                     'compás.',
                     'Cuenta "uno-DOS-TRES" en voz alta mientras tocas, y marca con el pie solo el '
                     '"uno". Si te adelantas, es que has dejado de contar: no es la mano, es la '
                     'cuenta.'),
                plan((4, 'Contar "uno-DOS-TRES" con el pie, sin tocar'),
                     (4, 'La derecha sola, los cc. 1 y 2, con el silencio contado'),
                     (3, 'La izquierda sola: Re, Do, Si bemol, Do'),
                     (4, 'Las dos manos, los cc. 1 a 4, con el metrónomo a 58')),
                metronomo('A 58 desde el primer día: viene impreso en tu partitura, así que no hay '
                          'nada que decidir. Un clic por golpe grande, dos por compás.',
                          'Si el silencio se te va, no bajes el metrónomo: cuenta más alto. A '
                          'menos velocidad el hueco se hace todavía más largo y cuesta más.'),
                unir([('Un bemol en la armadura', 'todos los Si van en la tecla negra'),
                      ('Re menor', 'Re · Fa · La'),
                      ('Negra con puntillo', 'un golpe entero en 6/8'),
                      ('♩. = 58', 'la velocidad impresa en tu partitura')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                colorear(I1 + I2 + I1 + I2,
                         [('las de Re menor', 'las que empiezan cada vuelta'),
                          ('las de Do mayor', 'las que la cierran')],
                         titulo='Colorea la vuelta de la izquierda',
                         pista='queda una sin color: es la del acorde de Si bemol'),
                acuerdate('La armadura no es una nota suelta: es una instrucción que vale para toda '
                          'la pieza. Ese bemol de detrás de la clave dice que TODOS los Si se tocan '
                          'en la tecla negra, en las dos manos y en cualquier octava, hasta que '
                          'aparezca un becuadro que lo contradiga.',
                          etiqueta='LA ARMADURA MANDA EN TODA LA PIEZA'),
                para_clase('Los cuatro primeros compases con las dos manos, a 58. Y dime si los '
                           'dedos que trae impresos tu edición te van bien o has cambiado alguno: '
                           'eso lo miramos juntas.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
