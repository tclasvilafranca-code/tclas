# -*- coding: utf-8 -*-
"""Gladiator, de Hans Zimmer — pieza 15 de Aida. Formato ADULTO exigente.

   Cierra la etapa del modo menor y es la pieza con MAS COSAS NUEVAS de todo su
   cuaderno: doble puntillo, semicorchea, tresillo, calderon y barras de
   repeticion. No hay ninguna nota dificil; lo dificil es la escritura.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de Ana Cristina Escobes,
   1 pagina). Es solo suya.

     - Detras de la clave hay **UN SOSTENIDO** (Fa#): Mi menor.
     - **4/4**.
     - Arriba pone **Allegro** y **ff**. NO trae numero de metronomo, asi que la
       velocidad se decide en clase y asi esta dicho en la hoja.
     - Empieza con una **ANACRUSA de un tiempo**: silencio de corchea con
       puntillo y una semicorchea.
     - **Los dos pentagramas hacen lo mismo, a la octava**, compas por compas.
     - Trae **tresillos** marcados con su 3, un **calderon** sobre el Si4 en
       redonda del c. 6, y barras de repeticion (la de abrir esta justo detras
       de ese c. 6).

   LAS ALTURAS del primer sistema, medidas a 150 ppp sobre las cinco lineas de
   cada pentagrama:

       DERECHA   anacrusa  silencio de corchea con puntillo · Mi4 (semicorchea)
                 c. 2  Si4 (negra con DOBLE puntillo) · Mi4 (semicorchea) ·
                       Si4 (negra con DOBLE puntillo) · Sol4 (semicorchea)
                 c. 3  Si4 (blanca con puntillo) · tresillo de corcheas
                       Si4 · Sol4 · Do5
                 c. 4  igual que el 2
                 c. 5  Si4 (blanca con puntillo) · tresillo de corcheas
                       Si4 · La#4 · Re5

       IZQUIERDA  lo mismo, una octava justa por debajo: Mi3 / Si3 · Mi3 · Si3 ·
                  Sol3 / Si3 + Si3 · Sol3 · Do4 / ... / Si3 + Si3 · La#3 · Re4

   Cada compas cierra en 4: 1,75 + 0,25 + 1,75 + 0,25 en el segundo, y 3 + 1
   (el tresillo vale un tiempo) en el tercero.

   EL DOBLE PUNTILLO ENTRO EN EL MOTOR CON ESTA PIEZA. Una negra con dos
   puntillos vale 1 + 1/2 + 1/4 = 1,75 tiempos, y la semicorchea que la sigue
   entra todavia mas tarde que en un largo-corto normal. Escribirla con un solo
   puntillo habria dejado el compas en 3,5 tiempos —el auditor lo habria
   cazado— pero escribirla "parecida" habria sido contarle otro ritmo. Ver
   `notation.DUR_BEATS` y el escalon 4 de `niveles.py`.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, plan, metronomo, diferencias, rodear,
                      dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def tres(pitches, gid):
    """Un tresillo de corcheas: tres notas en el hueco de dos."""
    return [dict(pitch=p, dur='e', tresillo=gid, beam=gid) for p in pitches]


# El primer sistema de la DERECHA, medido. Cita literal. La ANACRUSA (silencio
# de corchea con puntillo y una semicorchea, Mi4) vale un tiempo y no se dibuja
# en ningun sistema: una fila de la ficha y un sistema de la hoja tienen que
# sumar compases enteros, asi que va contada en la prosa. Es la misma decision
# que en el We Wish You de la pieza 3.
LARGO = [n('B4', 'q..'), n('E4', 's'), n('B4', 'q..'), n('G4', 's')]      # cc. 2 y 4
TRES1 = [n('B4', 'h.')] + tres(['B4', 'G4', 'C5'], 151)                   # c. 3
TRES2 = [n('B4', 'h.')] + tres(['B4', 'A#4', 'D5'], 152)                  # c. 5

# Y la IZQUIERDA, que hace lo mismo una octava por debajo. Tambien medido.
LARGO_I = [n('B3', 'q..'), n('E3', 's'), n('B3', 'q..'), n('G3', 's')]
TRES1_I = [n('B3', 'h.')] + tres(['B3', 'G3', 'C4'], 153)

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=15, nivel='intermedio',
    slug='Gladiator', formato='adulto',
    titulo_corto='Gladiator', time_sig=(4, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source', 'Gladiator.pdf'),
    yt='https://www.youtube.com/results?search_query=gladiator+now+we+are+free+piano',

    ficha=dict(
        titulo='Gladiator',
        autor='Hans Zimmer · arr. Ana Cristina Escobés',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'),
               ('Carácter', 'Allegro · ff'), ('Armadura', 'Un sostenido'),
               ('Empieza', 'Antes del compás')],
        titulo_ritmos='Los compases 2 y 3, medidos',
        pie_ritmos='Arriba, los cc. 2 y 3 de la derecha MEDIDOS en tu partitura: negra con DOBLE '
                   'puntillo y semicorchea, y después el tresillo. Abajo, los mismos dos compases '
                   'en la izquierda, que hace exactamente lo mismo una octava por debajo. La '
                   'anacrusa va antes del c. 2 y no se dibuja aquí porque no llena un compás.',
        armonia=dict(
            titulo='Cinco cosas nuevas en una página',
            tarjetas=[
                ('EL DOBLE PUNTILLO', 'Vale 1 ¾',
                 'Dos puntillos: el primero añade la mitad y el segundo, la mitad del primero. Una '
                 'negra pasa de 1 a 1,75 tiempos, y la nota corta que va detrás entra casi encima '
                 'del tiempo siguiente.'),
                ('EL TRESILLO', 'Tres donde caben dos',
                 'Las tres corcheas del 3 ocupan lo que ocuparían dos: un tiempo entero entre las '
                 'tres. Van más juntas de lo que parecen.'),
                ('LA ANACRUSA', 'Un tiempo',
                 'La pieza empieza antes del primer compás: un silencio de corchea con puntillo y '
                 'una semicorchea. Ese primer compás no está completo, y es a propósito.'),
                ('LAS DOS MANOS', 'Lo mismo, a la octava',
                 'Los dos pentagramas llevan la misma línea separada por una octava. Solo hay una '
                 'melodía que aprender, pero cualquier desajuste entre las manos se oye como un '
                 'eco.'),
            ],
            pie='Ninguna de las cinco cosas nuevas es una nota difícil: son cinco maneras de '
                'escribir el tiempo. Por eso esta semana se cuenta más de lo que se toca, y por eso '
                'va aquí y no antes: llega con el 6/8, el 2/4 y la semicorchea ya trabajados.',
        ),
        ritmos=[
            ('DERECHA', 'los cc. 2 y 3, MEDIDOS · doble puntillo y tresillo',
             LARGO + TRES1, OCRE, 'treble', 'Mi menor'),
            ('IZQUIERDA', 'los mismos dos, medidos · una octava por debajo',
             LARGO_I + TRES1_I, AZUL, 'bass', 'Mi menor'),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa van en tecla negra.',
            'Arriba pone Allegro y ff, pero no hay número de metrónomo.',
            'Empieza con una anacrusa de un tiempo, antes del primer compás.',
            'Hay negras con DOS puntillos: valen 1 tiempo y tres cuartos.',
            'Hay tresillos, marcados con un 3 encima del grupo.',
            'Los dos pentagramas llevan la misma música, separada una octava.',
            'En el compás 6 hay un calderón, y después una barra de repetición.',
        ],
        reto='Que la semicorchea del doble puntillo entre de verdad al final del tiempo. Con un '
             'puntillo ya cuesta; con dos, la nota larga se lleva casi todo y la corta queda '
             'pegadísima a la siguiente.',
        truco='Cuenta cada tiempo en cuatro y la nota larga en siete: "1-2-3-4-5-6-7" y la corta en '
              'el ocho. Suena raro dicho así, pero es exactamente lo que vale.',
        sabias='Hans Zimmer escribió la música de Gladiator en seis semanas y con la película sin '
               'montar del todo. La voz que se oye en el tema es de Lisa Gerrard, que canta en un '
               'idioma inventado por ella: no hay letra que traducir, y esa es la idea.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate solo en el principio: una nota corta de entrada y luego el balanceo '
                      'largo-corto. Ese desnivel tan marcado es el doble puntillo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Cinco cosas nuevas y ninguna es una nota. Esta semana se cuenta antes de tocar, y se '
              'cuenta en voz alta: si la cuenta no sale, la mano tampoco.',
        reglas=['TODOS LOS FA, EN TECLA NEGRA', 'LA LARGA VALE 1 Y ¾',
                'LAS DOS MANOS HACEN LO MISMO'],
        bloques=[
            dict(num=1, titulo='La entrada y el doble puntillo',
                 pista='anacrusa y c. 2 · MEDIDO en tu partitura · la larga se lleva casi el tiempo '
                       'entero',
                 sistemas=[
                     dict(cap='a) la anacrusa, con tres tiempos de silencio delante para poder '
                              'contarla · en tu partitura ese primer compás solo tiene el último '
                              'tiempo',
                          events=[sil('h.'), sil('e.'), n('E4', 's')],
                          matiz='ff', bars=1, key_sig='Mi menor'),
                     dict(cap='b) y el c. 2, que es el que entra detrás',
                          events=list(LARGO), bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='c) y el mismo compás con la larga de un solo puntillo · NO es lo que '
                              'pone tu partitura: es para oír la diferencia entre uno y dos',
                          events=[n('B4', 'q.'), n('E4', 'e'), n('B4', 'q.'), n('G4', 'e')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='d) y con las ocho notas iguales, que es como suena cuando la cuenta '
                              'se pierde · andamio, para reconocer el error de oído',
                          events=corch(['B4', 'E4']) + corch(['B4', 'G4']) +
                                 corch(['B4', 'E4']) + corch(['B4', 'G4']),
                          bars=1, show_time=False, key_sig='Mi menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE CUENTA UN DOBLE PUNTILLO',
                 texto='Un puntillo añade la mitad de la figura; el segundo puntillo añade la mitad '
                       'del primero. Negra = 1, con un puntillo 1,5, con dos 1,75. Lo que queda '
                       'para la nota corta es un cuarto de tiempo, o sea una semicorchea. Para '
                       'contarlo, parte cada tiempo en cuatro y di "1-2-3-4": la larga ocupa hasta '
                       'el 3 del segundo tiempo y la corta cae en el 4. Si la corta te sale antes, '
                       'estás tocando un puntillo solo, que es medio tiempo de diferencia.'),
            dict(num=2, titulo='El tresillo del compás 3',
                 pista='c. 3 · MEDIDO · tres corcheas en el hueco de dos, dentro del último tiempo',
                 sistemas=[
                     dict(cap='a) el c. 3 tal y como está · una nota larga de tres tiempos y el '
                              'tresillo en el cuarto',
                          events=list(TRES1), bars=1, key_sig='Mi menor'),
                     dict(cap='b) y el mismo tiempo con DOS corcheas normales en vez de tres · así '
                              'se oye lo que aprieta el tresillo; tu partitura lleva tres',
                          events=[n('B4', 'h.')] + corch(['B4', 'G4']),
                          bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='c) y el c. 5, que es el mismo compás con otras dos notas dentro del '
                              'tresillo · ojo al La sostenido, escrito dentro de la música',
                          events=list(TRES2), bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='d) y los cc. 3 y 5 seguidos, que es lo que oyes dos veces con el 4 '
                              'en medio · lo único que cambia son las dos últimas del tresillo',
                          events=TRES1 + TRES2, bars=2, show_time=False, key_sig='Mi menor'),
                 ]),
            dict(num=3, titulo='La izquierda hace lo mismo, una octava abajo',
                 pista='anacrusa y cc. 2-3 de la mano izquierda · MEDIDO · nota por nota, lo mismo '
                       'que la derecha',
                 sistemas=[
                     dict(cap='a) el c. 2 de la izquierda · si lo comparas con el primer sistema '
                              'de esta hoja, son las mismas notas una octava más abajo',
                          events=list(LARGO_I), bars=1, clef='bass', key_sig='Mi menor'),
                     dict(cap='b) y el c. 3 de la izquierda, con su tresillo',
                          events=list(TRES1_I), bars=1, clef='bass', show_time=False,
                          key_sig='Mi menor'),
                     dict(cap='c) y las dos manos a la vez en el c. 2 · cada pareja de notas es una '
                              'octava justa: si suena a otra cosa, una de las dos se ha ido',
                          events=[ac(('B3', 'B4'), 'q..'), ac(('E3', 'E4'), 's'),
                                  ac(('B3', 'B4'), 'q..'), ac(('G3', 'G4'), 's')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='d) y el c. 6, donde todo se para: una redonda con CALDERÓN · el '
                              'calderón dice que la nota dura más de lo que vale, y cuánto lo '
                              'decides tú',
                          events=[dict(pitch='B4', dur='w', art='calderon')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='La anacrusa y los cc. 2 a 5 con las dos manos, contando cada tiempo en '
                       'cuatro partes en voz alta. Tu edición no dice a qué velocidad hay que '
                       'tocarla —solo pone Allegro—, así que empieza despacio y apunta a lápiz el '
                       'número al que te salen los dobles puntillos: ese es el que vamos a mirar. Y '
                       'antes de tocar, sigue con el dedo el camino de la pieza: hay un calderón en '
                       'el compás 6 y después una barra de repetición.'),
        ] + bloques_extra('Mi menor', 109, 'E4', 'E2',
                          'el doble puntillo: la larga se lleva 1 tiempo y ¾, y la corta el resto',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Gladiator · para casa',
            intro='Quince minutos al día, y los cinco primeros sin piano: contando cada tiempo en '
                  'cuatro partes con el pie. Esta pieza es de contar.',
            bloques=[
                plan((5, 'Contar "1-2-3-4" por tiempo y decir dónde cae la nota corta'),
                     (4, 'La anacrusa y el c. 2, con la derecha sola'),
                     (3, 'El tresillo del c. 3, contando "tres en el hueco de dos"'),
                     (3, 'Las dos manos, de la anacrusa al c. 5')),
                metronomo('Empieza a ♩ = 60 con la derecha sola: a esa velocidad da tiempo a partir '
                          'el tiempo en cuatro y colocar la semicorchea donde va.',
                          'Tu partitura pone Allegro pero no trae número, así que estos son de '
                          'trabajo. Sube a 84 solo cuando el doble puntillo salga tres veces '
                          'seguidas sin adelantarse.'),
                diferencias(list(LARGO),
                            [n('B4', 'q.'), n('E4', 'e'), n('B4', 'q.'), n('G4', 'e')],
                            cuantas=4,
                            titulo='Busca las diferencias',
                            pista='arriba, tu compás 2 medido · abajo, el mismo compás con un solo '
                                  'puntillo en las largas'),
                rodear([list(LARGO),
                        [n('B4', 'q..'), n('E4', 's'), n('B4', 'q..'), n('E4', 's')],
                        list(LARGO),
                        [n('B4', 'q..'), n('G4', 's'), n('B4', 'q..'), n('G4', 's')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='los dos que buscas son el c. 2 de tu partitura · fíjate en la última '
                             'nota de cada uno'),
                dibujar(['Mi', 'Sol', 'Si', 'Do', 'Re', 'Fa sostenido', 'Si'],
                        titulo='Dibuja tú las notas',
                        pista='en clave de sol · las tres primeras son las de tu compás 2, y el Fa '
                              'lleva el sostenido de la armadura'),
                para_clase('La anacrusa y los cc. 2 a 5 con las dos manos, a la velocidad que te '
                           'salga el doble puntillo sin adelantar la corta. Y tráeme apuntado ese '
                           'número: el Allegro lo ponemos a partir de ahí, no al revés.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
