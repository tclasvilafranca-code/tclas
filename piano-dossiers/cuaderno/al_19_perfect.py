# -*- coding: utf-8 -*-
"""Perfect (Ed Sheeran) — pieza 19 de Alan. ADULTO exigente, con cifrado impreso, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo del Campamento
   Bye Bye Beethoven, 1 página), a 250 ppp, cabeza a cabeza:

     - SOL MAYOR: un sostenido detrás de la clave. Y **12/8**.
     - Arriba viene impreso el metrónomo: **negra con puntillo = 94**.
     - Encima del pentagrama va el CIFRADO: G · Em · C · D, que se repite casi
       toda la pieza; del c. 17 al 24 hay dos letras por compás, y en el c. 26
       sale un D/F♯. La edición trae además digitación impresa.
     - MEDIDO, mano derecha. Anacrusa de tres corcheas: **Re4 · Mi4 · Sol4**
       (con un silencio de negra con puntillo en la izquierda).
       c. 1: Sol4 blanca con puntillo, silencio de corchea, y
             Si4 · La4 · Si4 · La4 · Sol4 (corcheas).
       c. 2: Si4 blanca con puntillo, silencio de negra con puntillo, y
             La4 · Si4 · Si4 (corcheas).
       c. 3: Si4 · La4 · Sol4 (corcheas), Sol4 negra con puntillo, silencio de
             negra con puntillo y Sol4 · La4 · Si4 (corcheas).
     - Son 27 compases y acaba en Sol4 con una redonda con puntillo.

   Es el mismo archivo que el de Aída, que ya lo trabajó con andamio. Aquí lo
   literal es lo medido (cc. 1-3) y el andamio va por el cifrado: las
   inversiones y el arpegio de la izquierda no son los de ella.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, corch, reto, plan, escalera, cifrado, unir,
                      nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: anacrusa y c. 1 (mano derecha)
ENTRADA = [sil('h.'), sil('q.'), n('D4', 'e'), n('E4', 'e'), n('G4', 'e')]
C1 = [n('G4', 'h.'), sil('e'), n('B4', 'e'), n('A4', 'e'), n('B4', 'e'),
      n('A4', 'e'), n('G4', 'e')]
# MEDIDO: cc. 2 y 3
C2 = [n('B4', 'h.'), sil('q.'), n('A4', 'e'), n('B4', 'e'), n('B4', 'e')]
C3 = [n('B4', 'e'), n('A4', 'e'), n('G4', 'e'), n('G4', 'q.'), sil('q.'),
      n('G4', 'e'), n('A4', 'e'), n('B4', 'e')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=19, nivel='intermedio', slug='Perfect',
    formato='adulto',
    titulo_corto='Perfect', time_sig=(12, 8), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'Perfect .Ed Sheeran.'),
    yt='https://www.youtube.com/results?search_query=perfect+ed+sheeran+piano+tutorial',

    ficha=dict(
        titulo='Perfect',
        autor='Ed Sheeran · arreglo del Campamento Bye Bye Beethoven',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '12/8'),
               ('Tempo', '♩. = 94'), ('Cifrado', 'G Em C D'),
               ('Empieza', 'Con anacrusa')],
        titulo_ritmos='La anacrusa y el compás 1, medidos',
        pie_ritmos='Arriba, medido sobre tu partitura: tres corcheas de anacrusa y el c. 1. '
                   'Abajo, andamio: la izquierda en Sol y en Mi menor, con el bajo y el acorde '
                   'de las dos primeras letras impresas.',
        armonia=dict(
            titulo='Doce corcheas, cuatro golpes, cuatro acordes',
            tarjetas=[
                ('EL 12/8', 'Cuatro de tres',
                 'Doce corcheas por compás, agrupadas de tres en tres: cuatro golpes grandes. '
                 'El 94 del metrónomo va a la negra con puntillo, o sea al golpe, no a la corchea.'),
                ('LA ANACRUSA', 'Re · Mi · Sol',
                 'Tres corcheas antes del primer compás, que valen justo un golpe. Entras en el '
                 'cuarto golpe de un compás que no se ve, así que hay que contarlo.'),
                ('EL CIFRADO', 'G · Em · C · D',
                 'Cuatro letras, un acorde por compás hasta el c. 16; del c. 17 al 24 hay dos '
                 'por compás, y en el c. 26 aparece un D/F♯: el mismo Re, con Fa sostenido en el '
                 'bajo.'),
                ('LA MELODÍA', 'Tres notas',
                 'La, Si y Sol se reparten los primeros compases. Lo difícil no son las alturas '
                 'sino el ritmo, con la blanca con puntillo y los silencios que la rodean.'),
            ],
            pie='La pieza entera son 27 compases y una sola página: cabe de un vistazo, y por eso se '
                'estudia por acordes y no por compases sueltos.',
        ),
        ritmos=[
            ('MANO DERECHA', 'anacrusa y c. 1 · medido', ENTRADA + C1, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio sobre G y Em · bajo y acorde',
             [ac(('G2', 'G3'), 'q.'), ac(('D3', 'B3'), 'q.'),
              ac(('G2', 'G3'), 'q.'), ac(('D3', 'B3'), 'q.'),
              ac(('E2', 'E3'), 'q.'), ac(('B2', 'G3'), 'q.'),
              ac(('E2', 'E3'), 'q.'), ac(('B2', 'G3'), 'q.')],
             AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa suenan a la tecla negra.',
            'El compás es 12/8: doce corcheas por compás, contadas de tres en tres.',
            'Arriba viene impreso el metrónomo: negra con puntillo = 94.',
            'Empieza con una anacrusa de tres corcheas: Re, Mi y Sol.',
            'Encima del pentagrama va el cifrado: G, Em, C y D, y en el c. 26 un D/F♯.',
            'La edición trae digitación impresa.',
        ],
        reto='Contar el 12/8 en cuatro y no en doce, y hacer que cuatro compases de acordes parezcan '
             'uno solo. Lo que se pierde, si se cuentan corcheas, es el balanceo.',
        truco='Cuenta "UN-dos-tres DOS-dos-tres TRES-dos-tres CUA-tro-tres" y marca solo las '
              'mayúsculas con el pie. El pie va a 94: si va más deprisa, estás contando corcheas.',
        sabias='Perfect salió en 2017, en el disco ÷, y fue la canción número uno del Reino Unido '
               'en la Navidad de ese año. Está escrita en 12/8, un compás que suele sonar a '
               'balada lenta y a bolero.',
        qr=dict(titulo='Escúchala',
                texto='Marca el pie con la canción. Si te salen cuatro pisadas por compás vas bien; '
                      'si te salen doce, estás contando corcheas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia primero con el pie y con la voz, y después con los dedos. La pieza se apoya '
              'en cuatro acordes y en un compás compuesto, y las dos cosas se resuelven antes que '
              'las notas.',
        reglas=['CUATRO GOLPES, NO DOCE', 'LAS LETRAS ANTES QUE LAS NOTAS', 'LA ANACRUSA SE CUENTA'],
        bloques=[
            dict(num=1, titulo='La anacrusa y el c. 1, tal como están escritos',
                 pista='anacrusa y c. 1 · medido sobre tu partitura · la izquierda no toca en la '
                       'anacrusa',
                 sistemas=[
                     dict(cap='a) la anacrusa son tres corcheas, Re, Mi y Sol · el silencio antes de '
                              'ellas son los tres golpes que no suenan',
                          events=ENTRADA, bars=1),
                     dict(cap='b) el c. 1: una blanca con puntillo, un silencio de corchea y cinco '
                              'corcheas · el silencio es lo que da el aire',
                          events=C1, bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='Los cc. 2 y 3',
                 pista='cc. 2-3 · medido sobre tu partitura · la melodía repite casi las mismas '
                       'tres notas',
                 sistemas=[
                     dict(cap='a) Em y C: la blanca con puntillo del c. 2 y las dos negras con '
                              'puntillo del c. 3, con un silencio entre ellas',
                          events=C2 + C3, bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL 94 NO ES LO QUE PARECE',
                 texto='El número del metrónomo va a la figura dibujada a su lado, y aquí es una '
                       'negra con puntillo. Son 94 golpes grandes por minuto, con tres corcheas '
                       'dentro de cada uno. Si pones el clic a 94 y tocas una corchea por clic, '
                       'la pieza te durará tres veces más: el error clásico de los compases '
                       'compuestos, y se comete una sola vez.'),
            dict(num=3, titulo='Los acordes del cifrado, en inversión',
                 pista='andamio sobre las letras IMPRESAS en tu partitura (G, Em, C, D)',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) uno por compás: Sol, Mi menor, Do y Re, cada uno en la inversión '
                              'más cercana al anterior · se cambia de acorde moviendo lo mínimo',
                          events=[ac(('G2', 'B2', 'D3'), 'w.'), ac(('G2', 'B2', 'E3'), 'w.'),
                                  ac(('G2', 'C3', 'E3'), 'w.'), ac(('A2', 'D3', 'F#3'), 'w.')],
                          bars=4, clef='bass'),
                     dict(cap='b) Sol y Mi menor, tres veces cada uno por compás · cada golpe, un '
                              'acorde entero, para sentir los cuatro',
                          events=[ac(('B2', 'D3', 'G3'), 'q.'), ac(('B2', 'D3', 'G3'), 'q.'),
                                  ac(('B2', 'D3', 'G3'), 'q.'), ac(('B2', 'D3', 'G3'), 'q.'),
                                  ac(('B2', 'E3', 'G3'), 'q.'), ac(('B2', 'E3', 'G3'), 'q.'),
                                  ac(('B2', 'E3', 'G3'), 'q.'), ac(('B2', 'E3', 'G3'), 'q.')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=4, titulo='La melodía sobre el acorde que la sostiene',
                 pista='cc. 1-2 de tu partitura · el acorde de la izquierda es andamio sobre el '
                       'cifrado impreso',
                 sistemas=[
                     dict(cap='a) la derecha medida y la izquierda sostenida: Sol en el c. 1, Mi '
                              'menor en el c. 2 · la izquierda no se mueve hasta cambiar de letra',
                          events=[ac(('G2', 'B2', 'G4'), 'h.'), sil('e'),
                                  ac(('B4',), 'e'), ac(('A4',), 'e'), ac(('B4',), 'e'),
                                  ac(('A4',), 'e'), ac(('G4',), 'e'),
                                  ac(('E2', 'G2', 'B4'), 'h.'), sil('q.'),
                                  ac(('A4',), 'e'), ac(('B4',), 'e'), ac(('B4',), 'e')],
                          bars=2, manos='sostiene'),
                 ]),
            dict(num=5, titulo='La vuelta de cuatro acordes con una sola mano',
                 pista='andamio sobre el cifrado impreso · la mano derecha toca solo las notas '
                       'graves de cada acorde',
                 sistemas=[
                     dict(cap='a) la raíz de cada letra, Sol, Mi, Do y Re, una por compás · '
                              'sirve para decidir si el bajo va en blancas o en corcheas',
                          events=[n('G2', 'w.'), n('E2', 'w.'), n('C3', 'w.'), n('D3', 'w.')],
                          bars=4, clef='bass'),
                 ]),
            dict(num=6, titulo='Dos letras en un mismo compás, cc. 17-24',
                 pista='andamio sobre las letras IMPRESAS · del c. 17 al 24 tu partitura trae dos '
                       'letras por compás, cada una en una blanca con puntillo',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Sol y Mi menor en el mismo compás · cada letra dura la mitad: '
                              'seis corcheas',
                          events=[ac(('G2', 'B2', 'D3'), 'h.'), ac(('E2', 'B2', 'G3'), 'h.'),
                                  ac(('C3', 'E3', 'G3'), 'h.'), ac(('D3', 'F#3', 'A3'), 'h.')],
                          bars=2, clef='bass', key_sig='Sol mayor'),
                 ]),
            dict(num=7, titulo='El D/F♯ del c. 26',
                 pista='andamio sobre la letra IMPRESA en el c. 26 · el acorde de Re con el Fa '
                       'sostenido en el bajo',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) un Re normal y el mismo Re con el Fa sostenido debajo · el '
                              'acorde es el mismo, cambia la nota más grave',
                          events=[ac(('D3', 'F#3', 'A3'), 'w.'), ac(('F#2', 'A3', 'D3'), 'w.')],
                          bars=2, clef='bass', key_sig='Sol mayor'),
                 ]),
        ] + bloques_extra('Sol mayor', 19, 'G4', 'G2',
                          'el 12/8: cuatro golpes con tres corcheas dentro de cada uno',
                          desde=8, time_sig=(12, 8), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Perfect · para casa',
            intro='Veinte minutos al día. Los primeros cinco, sin tocar: contando en cuatro con el '
                  'pie. El compás es lo nuevo, y si lo cuentas bien la pieza se toca sola.',
            bloques=[
                plan((5, 'Contar "UN-dos-tres DOS-dos-tres…" con el pie, sin tocar'),
                     (5, 'Los cuatro acordes del cifrado, uno por compás'),
                     (5, 'La anacrusa y el c. 1 con la derecha sola'),
                     (5, 'Los cc. 1-3 con las dos manos')),
                escalera((56, 'los cuatro acordes, con el pie marcando los cuatro golpes'),
                         (70, 'la anacrusa y los tres primeros compases'),
                         (82, 'los cc. 1-8 con las dos manos'),
                         (94, 'los cc. 1-16: el número impreso en tu partitura'),
                         meta='94, que es el número IMPRESO en tu partitura · y va a la negra con '
                              'puntillo, o sea un clic por golpe grande',
                         notas=['Un clic por golpe, nunca uno por corchea.']),
                cifrado(['G', 'Em', 'C', 'D', 'D/F♯'],
                        ['Escribe las tres notas de cada uno de los cuatro primeros, de grave a '
                         'agudo.',
                         'Rodea el que lleva una tecla negra: es el que usa el Fa sostenido.',
                         'Explica con tus palabras qué dice la barra de D/F♯.'],
                        titulo='Las letras de tu partitura',
                        pista='los cuatro primeros están impresos en el c. 1-4; el D/F♯ sale en el '
                              'c. 26'),
                unir([('12/8', 'cuatro golpes de tres corcheas'),
                      ('Negra con puntillo = 94', 'un clic por golpe grande, no por corchea'),
                      ('Anacrusa', 'las tres corcheas que entran antes del compás 1'),
                      ('D/F♯', 'el acorde de Re con el Fa sostenido en el bajo')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                nombres(['B4', 'G4', 'D5', 'A4', 'E4', 'C5', 'D4'],
                        titulo='¿Qué notas componen la melodía?',
                        pista='son las siete alturas distintas que aparecen en los cuatro primeros '
                              'sistemas de tu partitura'),
                para_clase('La anacrusa y los ocho primeros compases con el metrónomo a 94. Y dime '
                           'cuántas pisadas te salen por compás: si son cuatro, ya está ganado lo '
                           'difícil de la pieza.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
