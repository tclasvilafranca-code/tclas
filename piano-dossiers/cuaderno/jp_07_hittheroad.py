# -*- coding: utf-8 -*-
"""Hit the Road Jack — pieza 7 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, 1 página,
   24 compases, sin arreglista impreso):

     - Fa mayor: UN BEMOL detrás de la clave, desde el compás 1. (A baja
       resolución parecía que el bemol aparecía en el c. 7; ampliando a 250 dpi
       se ve que está desde el principio. Ver TRANSCRIPCION_JOSEP_FUENTES.)
     - 4/4. No imprime tempo.
     - Los seis primeros compases la DERECHA HACE ACORDES EN BLOQUE con
       silencios entre medias, y la izquierda negras sueltas: es una
       introducción, no la melodía.
     - Del c. 7 al 19 la derecha lleva la melodía y la izquierda hace redondas.
     - Del c. 20 al final vuelven los acordes en bloque de la introducción.
     - Hay barras de repetición en los cc. 12 y 20.

   Primera pieza del cuaderno con armadura. Todo el material inventado va como
   ANDAMIO en Fa mayor y remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jp_comun import (n, ac, sil, reto, plan, escalera, inventa, teclado,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=7, nivel='intermedio', slug='HitTheRoadJack',
    formato='adulto',
    titulo_corto='Hit the Road Jack', time_sig=(4, 4), key_sig='Fa mayor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source', 'hit-the-road-jack-ray-.pdf'),
    yt='https://www.youtube.com/results?search_query=hit+the+road+jack+piano+easy',

    ficha=dict(
        titulo='Hit the Road Jack',
        autor='Popularizada por Ray Charles · arreglo de Musescore',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Teclas negras', 'El Si bemol'),
               ('Páginas', 'Una')],
        titulo_ritmos='Las dos caras de la pieza',
        pie_ritmos='Andamio en Fa mayor. Lo literal es la estructura: acordes en bloque con '
                   'silencios en la introducción y melodía con redondas en el centro.',
        armonia=dict(
            titulo='La primera armadura del cuaderno',
            tarjetas=[
                ('UN BEMOL', 'Fa mayor',
                 'Detrás de la clave hay un bemol, y está desde el compás 1. Eso quiere decir que '
                 'TODOS los Si de la pieza son Si bemol, la tecla negra, hasta el final.'),
                ('LA INTRODUCCIÓN', 'cc. 1-6',
                 'Acordes en bloque en la derecha, con silencios entre medias, y negras sueltas en '
                 'la izquierda. No es la melodía todavía: es el arranque.'),
                ('EL CENTRO', 'cc. 7-19',
                 'Ahí entra la melodía en la derecha y la izquierda se queda en redondas. Es la '
                 'parte que la gente canta.'),
                ('Y VUELTA', 'cc. 20-24',
                 'Regresan los acordes en bloque del principio. La pieza cierra como abrió, así que '
                 'lo que aprendas al principio te vale otra vez al final.'),
            ],
            pie='Es la primera vez que hay que mirar el principio del pentagrama antes de tocar. Lo '
                'que falla con una armadura nueva no son los dedos: es que a mitad de frase se te '
                'olvida que está, y tocas un Si natural en medio de una pieza en Fa.',
        ),
        ritmos=[
            ('MANO DERECHA · INTRO', 'acordes y silencios · andamio',
             [sil('q'), ac(('A3', 'C4', 'F4')), sil('q'), ac(('A3', 'C4', 'F4'))],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA · CENTRO', 'una redonda por compás · literal',
             [n('F2', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Un bemol detrás de la clave desde el compás 1: todos los Si son Si bemol.',
            'Los seis primeros compases son acordes en bloque con silencios en medio.',
            'Del compás 7 al 19 la izquierda hace una redonda por compás.',
            'Del compás 20 al final vuelven los acordes del principio.',
            'Hay barras de repetición en los compases 12 y 20.',
            'La edición no imprime tempo.',
        ],
        reto='No olvidarte del Si bemol a mitad de frase. Con una armadura nueva, los primeros '
             'compases salen bien porque estás pendiente, y el fallo llega en el compás nueve, '
             'cuando ya estás pensando en otra cosa.',
        truco='Antes de tocar, busca en tu partitura TODOS los Si y márcalos a lápiz con un '
              'circulito. Son pocos. Marcarlos una vez ahorra veinte correcciones, porque el '
              'problema nunca es la mano: es que el ojo deja de ver la armadura.',
        sabias='Ray Charles la grabó en 1961 y llegó al número uno, pero la escribió otro: Percy '
               'Mayfield, que se la mandó grabada a capela en una cinta como maqueta. La versión de '
               'Charles con las voces respondiendo es idea del estudio, no del autor.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en la diferencia entre la introducción y la parte cantada. Son dos '
                      'texturas distintas, y en tu partitura están escritas distinto.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza tiene dos texturas distintas y una armadura nueva. Trabaja primero el Si '
              'bemol solo, después la introducción, y deja la melodía para el final: es la parte '
              'que ya te sabes de oído y la que menos trabajo necesita.',
        reglas=['TODOS LOS SI SON SI BEMOL', 'LA INTRO NO ES LA MELODÍA',
                'LOS SILENCIOS SE CUENTAN'],
        bloques=[
            dict(num=1, titulo='El Si bemol, hasta que suene raro tocar el otro',
                 pista='andamio en Fa mayor · la posición empieza en Fa y el 4 cae en la tecla negra',
                 sistemas=[
                     dict(cap='a) la posición de Fa, subiendo y bajando · el dedo 4 va a la tecla '
                              'negra y ahí se queda toda la pieza',
                          events=[n('F4'), n('A4'), n('G4'), n('Bb4'),
                                  n('A4'), n('C5'), n('Bb4'), n('G4')],
                          bars=2, key_sig='Fa mayor'),
                     dict(cap='b) y ahora con el Si bemol repetido, que es donde se olvida · si en '
                              'algún momento suena a blanca, para y empieza otra vez',
                          events=[n('Bb4'), n('A4'), n('Bb4'), n('C5'),
                                  n('Bb4'), n('G4'), n('F4', 'h')],
                          bars=2, key_sig='Fa mayor', show_time=False),
                 ]),
            dict(num=2, titulo='La introducción: acordes y silencios',
                 pista='la FORMA es literal (acorde, silencio, acorde); las notas, andamio en Fa',
                 sistemas=[
                     dict(cap='a) el acorde cae y se levanta · el silencio hay que contarlo, no '
                              'esperarlo a ojo',
                          events=[sil('q'), ac(('A3', 'C4', 'F4')), sil('q'), ac(('A3', 'C4', 'F4')),
                                  sil('q'), ac(('Bb3', 'D4', 'F4')), sil('h')],
                          bars=2, key_sig='Fa mayor'),
                     dict(cap='b) con la izquierda de la introducción debajo, en negras sueltas',
                          events=[n('F2'), sil('q'), n('F2'), sil('q'),
                                  n('C3'), sil('q'), n('C3'), sil('q')],
                          bars=2, clef='bass', key_sig='Fa mayor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE MARCAN LOS SI',
                 texto='Una armadura no se olvida por falta de técnica: se olvida porque el ojo deja '
                       'de mirar el principio del pentagrama en cuanto lleva dos líneas leyendo. '
                       'Marcar los Si a lápiz no es hacer trampa, es lo que hace todo el mundo la '
                       'primera semana con una tonalidad nueva. En la tercera ya se borra.'),
            dict(num=3, titulo='La melodía sobre las redondas',
                 pista='andamio en Fa mayor · cc. 7-19 de tu partitura',
                 sistemas=[
                     dict(cap='a) la izquierda aguanta la redonda entera y la derecha se mueve · '
                              'comprueba en el cuarto golpe que el bajo sigue sonando',
                          events=[ac(('F2', 'C5')), n('Bb4'), n('A4'), n('G4'),
                                  ac(('C3', 'F4'), 'h'), n('A4'), n('F4')],
                          bars=2, key_sig='Fa mayor'),
                     dict(cap='b) y bajando hasta la tónica, que es como acaba cada frase',
                          events=[n('C5'), n('Bb4'), n('A4'), n('G4'),
                                  n('F4'), n('A4'), n('F4', 'h')],
                          bars=2, key_sig='Fa mayor', show_time=False),
                 ]),
        ] + bloques_extra('Fa mayor', 21, 'F4', 'F2',
                          'el Si bemol se olvida justo a mitad de frase',
                          desde=4, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Hit the Road Jack · para casa',
            intro='Veinte minutos. Lo primero de todo, coger el lápiz y marcar los Si.',
            bloques=[
                reto('Tocar la pieza entera sin un solo Si natural.',
                     'Marca a lápiz todos los Si de tu partitura antes de tocar nada. Si al final '
                     'de la semana puedes borrarlos y sigue saliendo bien, la armadura ya es tuya.'),
                plan((4, 'La posición de Fa, con el 4 en la tecla negra'),
                     (6, 'La introducción, cc. 1-6, contando los silencios'),
                     (6, 'La melodía, cc. 7-19, con la izquierda en redondas'),
                     (4, 'El final, cc. 20-24: son los acordes del principio')),
                escalera((60, 'la introducción, contando los silencios'),
                         (75, 'la melodía con las redondas'),
                         (90, 'la pieza entera, sin parar'),
                         meta='la velocidad a la que la puedas tocar entera sin parar — esta '
                              'partitura no trae tempo impreso',
                         notas=['Elige tu meta el primer día y apúntala en la partitura.']),
                inventa(['Solo Fa, Sol, La, Si bemol y Do.',
                         'Dos compases de cuatro golpes.',
                         'Que el Si bemol aparezca por lo menos dos veces.',
                         'Y que haya un silencio de negra en cada compás.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases en Fa mayor',
                        pista='con silencios, como la introducción de la pieza'),
                teclado({3: 1, 0: 2, 4: 3},
                        ['Escribe el nombre de las tres teclas blancas marcadas.',
                         'Y pinta la tecla negra que hay justo antes de la número 1: ese es tu Si '
                         'bemol, y vale para toda la pieza.'],
                        titulo='En el teclado',
                        pista='la número 1 es el Si'),
                para_clase('La introducción y la melodía por separado, y a qué velocidad has '
                           'llegado. Si has tenido que dejar los Si marcados toda la semana no '
                           'pasa nada: dilo y seguimos con ellos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
