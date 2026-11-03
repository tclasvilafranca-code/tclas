# -*- coding: utf-8 -*-
"""It's Beginning to Look a Lot Like Christmas — pieza 10 de Aida. Formato
   ADULTO exigente. A CUATRO MANOS.

   Abre la cuarta etapa, la de los compases que se cuentan de otra manera, y lo
   hace con un 6/8. Es la primera vez del cuaderno que un compas no se cuenta
   en negras: aqui hay seis corcheas y DOS golpes, tres corcheas dentro de cada
   uno. Va justo detras de Perfect a proposito — alli el mismo agrupamiento de
   tres, pero con cuatro golpes por compas en vez de dos.

   Lo comprobado sobre el PDF de SU carpeta (Musescore, "Piano Duet", arr.
   Rachel Chytelman, 2 paginas; el mismo archivo, byte a byte, que el de Josep,
   Dilan y Eva):

     - Detras de la clave no hay nada.
     - **6/8**.
     - Es un DUETO. Aida toca el Piano 1, y sus DOS pentagramas van en clave de
       sol (no uno de sol y otro de fa). El Piano 2 lo toca la profesora.
     - Hay un sostenido escrito como alteracion accidental dentro de la musica
       (el Fa# del c. 2), no en la armadura.

   LAS ALTURAS del primer sistema, medidas a 150 ppp sobre las cinco lineas de
   cada pentagrama (apertura morfologica para las cabezas llenas; las
   posiciones salen en espacios de pentagrama, no en pixeles):

       pentagrama de ARRIBA     c. 1  silencio de negra con puntillo · Mi5 (negra) · Fa5 (corchea)
                                c. 2  Sol5 · La5 · Sol5 (corcheas) · Fa#5 (negra) · Sol5 (corchea)
                                c. 3  La5 (negra con puntillo) · Do6 (negra con puntillo)
                                c. 4  Mi6 (negra con puntillo) · Sol5 (negra con puntillo)
                                c. 5  compas entero de silencio

       pentagrama de ABAJO      lo mismo UNA OCTAVA JUSTA POR DEBAJO, nota a
                                nota: Mi4 · Fa4 / Sol4 · La4 · Sol4 · Fa#4 ·
                                Sol4 / La4 · Do5 / Mi5 · Sol4 / silencio.

   Cada compas cierra en 3 (1,5 + 1 + 0,5, y 0,5x3 + 1 + 0,5), que es lo que
   vale un compas de 6/8.

   DOS COSAS QUE SALIERON DE MEDIR, y que a ojo se habian leido mal:

     1. la segunda corchea del c. 2 es un **La5**, no un Si5. La cabeza va
        montada SOBRE la linea adicional, y ampliada parece estar encima de
        ella. Se distingue midiendo el centro de la cabeza contra las lineas
        del pentagrama: 252,5 px, y el La5 cae en 253,7 y el Si5 en 248,6.
     2. el pentagrama de abajo NO es un andamio nuestro: es la misma melodia a
        la octava, y por eso aqui se cita, no se inventa. Escribirlo como
        andamio habria sido inventar lo que ya estaba impreso.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, reto, plan, a_cuatro_manos, nombres,
                      diferencias, acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los cuatro primeros compases del pentagrama de ARRIBA del Piano 1, medidos.
# Cita literal.
C1 = [sil('q.'), n('E5'), n('F5', 'e')]
C2 = corch(['G5', 'A5', 'G5'], 3) + [n('F#5'), n('G5', 'e')]
C34 = [n('A5', 'q.'), n('C6', 'q.'), n('E6', 'q.'), n('G5', 'q.')]

# Y los mismos cuatro compases del pentagrama de ABAJO, una octava por debajo.
# Tambien medidos: en esta edicion los dos pentagramas del Piano 1 llevan la
# melodia a la octava.
B1 = [sil('q.'), n('E4'), n('F4', 'e')]
B2 = corch(['G4', 'A4', 'G4'], 3) + [n('F#4'), n('G4', 'e')]
B34 = [n('A4', 'q.'), n('C5', 'q.'), n('E5', 'q.'), n('G4', 'q.')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=10, nivel='intermedio',
    slug='ItsBeginningToLook', formato='adulto',
    titulo_corto="It's Beginning to Look a Lot Like Christmas", time_sig=(6, 8), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Its Beginning to Look 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=its+beginning+to+look+a+lot+like+christmas+piano+duet',

    ficha=dict(
        titulo="It's Beginning to Look a Lot Like Christmas",
        autor='Meredith Willson · dueto de piano · parte del Piano 1',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '6/8'),
               ('Golpes', 'Dos por compás'), ('Empieza', 'En el segundo'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='El compás 1 del Piano 1',
        pie_ritmos='Arriba, los compases 1 y 2 del pentagrama de arriba, MEDIDOS en tu partitura. '
                   'Abajo, el compás 1 del pentagrama de abajo, también medido: en tu edición los '
                   'dos pentagramas del Piano 1 llevan la misma melodía, a la octava.',
        armonia=dict(
            titulo='Seis corcheas que son dos golpes',
            tarjetas=[
                ('EL 6/8', 'Dos y tres',
                 'Seis corcheas por compás, agrupadas de tres en tres. Se cuentan DOS golpes, no '
                 'seis: es el mismo reparto de Perfect, pero con dos en vez de cuatro.'),
                ('LA ENTRADA', 'En el segundo',
                 'El compás 1 empieza con un silencio de negra con puntillo, o sea un golpe entero. '
                 'Tú entras en el segundo golpe.'),
                ('DOS CLAVES DE SOL', 'Y la misma melodía',
                 'Los dos pentagramas del Piano 1 llevan clave de sol, y llevan lo mismo: la misma '
                 'melodía a distancia de octava. No busques la clave de fa, no está.'),
                ('EL PIANO 2', 'La profesora',
                 'La otra parte la toca ella. Tú llevas la melodía y las dos partes tienen que '
                 'contar los mismos dos golpes por compás.'),
            ],
            pie='Un 6/8 lento es lo mismo que un 3/4 rápido si solo miras las corcheas, y sin '
                'embargo suenan distintos. Lo que los separa es dónde caen los golpes fuertes: aquí '
                'son dos por compás, y todo lo demás va colgado de esos dos.',
        ),
        ritmos=[
            ('ARRIBA', 'los cc. 1 y 2, MEDIDOS · entras en el 2º golpe',
             C1 + C2, OCRE, 'treble', None),
            ('ABAJO', 'el c. 1, medido · la misma melodía una octava más grave',
             B1, AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 6/8: seis corcheas agrupadas de tres en tres.',
            'El compás 1 empieza con un silencio de negra con puntillo.',
            'Los dos pentagramas del Piano 1 llevan clave de sol.',
            'En el compás 2 hay un Fa sostenido escrito dentro de la música.',
            'El compás 5 es un compás entero de silencio.',
            'Es un dueto: la otra parte la toca la profesora.',
        ],
        reto='Contar el 6/8 en dos y no en seis. Contando seis la pieza se vuelve un trote de '
             'corcheas iguales y se pierde el balanceo, que es lo que la hace sonar a villancico.',
        truco='Cuenta "UN-dos-tres DOS-dos-tres" y marca con el pie solo las mayúsculas: dos '
              'pisadas por compás. Si te salen seis pisadas, estás contando corcheas.',
        sabias='Meredith Willson la escribió en 1951, el mismo año que empezó "The Music Man". La '
               'grabó Bing Crosby y desde entonces no ha dejado de sonar: es de los pocos '
               'villancicos modernos que se canta igual en inglés y en versión instrumental.',
        qr=dict(titulo='Escúchala',
                texto='Marca el pie con la grabación. Si te salen dos pisadas por compás vas bien; '
                      'si te salen seis, estás contando las corcheas una a una.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El 6/8 ya lo trabajaste en Perfect, pero allí eran cuatro golpes y aquí son dos. '
              'Empieza por eso: contar dos, no seis, y sin tocar.',
        reglas=['DOS GOLPES POR COMPÁS, NO SEIS', 'TRES CORCHEAS DENTRO DE CADA GOLPE',
                'TÚ ENTRAS EN EL SEGUNDO'],
        bloques=[
            dict(num=1, titulo='Los dos golpes del 6/8',
                 pista='andamio en Do mayor · lo que se practica es el agrupamiento, no las notas',
                 sistemas=[
                     dict(cap='a) un compás entero en una nota larga · eso es lo que dura un 6/8',
                          events=[n('C5', 'h.')],
                          matiz='mf',
                          bars=1),
                     dict(cap='b) y el mismo compás partido en sus dos golpes',
                          events=[n('C5', 'q.'), n('E5', 'q.'), n('D5', 'q.'), n('C5', 'q.')],
                          bars=2, show_time=False),
                     dict(cap='c) y ahora con las tres corcheas dentro de cada golpe · di '
                              '"UN-dos-tres DOS-dos-tres"',
                          events=corch(['C5', 'D5', 'E5'], 3) + corch(['F5', 'E5', 'D5'], 3) +
                                 corch(['E5', 'D5', 'C5'], 3) + corch(['D5', 'C5', 'B4'], 3),
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ NO ES LO MISMO QUE UN 3/4',
                 texto='Un 3/4 tiene tres golpes y cada uno se parte en dos; un 6/8 tiene dos '
                       'golpes y cada uno se parte en tres. Escritos con corcheas se parecen mucho, '
                       'pero suenan distinto porque el golpe fuerte cae en otro sitio: en 3/4 hay tres '
                       'sitios fuertes por compás y en 6/8 solo dos. Si cuentas un 6/8 de tres, la '
                       'música empieza a sonar a vals y deja de sonar a villancico.'),
            dict(num=2, titulo='Los compases 1 y 2, tal y como están escritos',
                 pista='cc. 1-2 · MEDIDO en tu partitura · el silencio ocupa el primer golpe entero',
                 sistemas=[
                     dict(cap='a) el compás 1 con el silencio partido en tres corcheas, para '
                              'contarlo · en tu partitura es UN silencio de negra con puntillo',
                          events=[sil('e'), sil('e'), sil('e'), n('E5'), n('F5', 'e')],
                          bars=1),
                     dict(cap='b) y el compás 2 solo, que es el único que corre · el Fa sostenido '
                              'está escrito dentro de la música, no en la armadura',
                          events=list(C2), bars=1, show_time=False),
                     dict(cap='c) del 2 al 3: las tres corcheas se acaban y el compás siguiente son '
                              'dos notas largas · ahí es donde se suele acelerar',
                          events=list(C2) + C34[:2], bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Los compases 3, 4 y 5: la cuesta y el hueco',
                 pista='cc. 3-5 · MEDIDO · seis notas largas y un compás entero de silencio',
                 sistemas=[
                     dict(cap='a) los cc. 3 y 4 · cuatro negras con puntillo subiendo hasta el Mi '
                              'agudo, una por golpe',
                          events=list(C34), bars=2),
                     dict(cap='b) y con el c. 5 detrás, que es un compás entero callado · cuéntalo '
                              'con el pie, no lo saltes',
                          events=list(C34) + [sil('h.')], bars=3, show_time=False),
                 ]),
            dict(num=4, titulo='El pentagrama de abajo: lo mismo, una octava más grave',
                 pista='cc. 1-4 del pentagrama de abajo · MEDIDO · en tu edición también va en '
                       'clave de sol',
                 sistemas=[
                     dict(cap='a) los cc. 1 y 2 de abajo · nota por nota, tu mano izquierda hace lo '
                              'que hace la derecha',
                          events=B1 + B2, bars=2),
                     dict(cap='b) y los cc. 3 y 4 de abajo, con la misma subida',
                          events=list(B34), bars=2, show_time=False),
                     dict(cap='c) y las dos a la vez, cc. 1 y 2 · cada pareja de notas es una '
                              'octava justa: si suena a otra cosa, una de las dos se ha ido',
                          events=[sil('q.'), ac(('E4', 'E5')), ac(('F4', 'F5'), 'e'),
                                  ac(('G4', 'G5'), 'e'), ac(('A4', 'A5'), 'e'),
                                  ac(('G4', 'G5'), 'e'), ac(('F#4', 'F#5')),
                                  ac(('G4', 'G5'), 'e')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cinco primeros compases, contando dos golpes por compás y con el pie '
                       'marcando solo esos dos. Y una cosa que no se puede ensayar sola: en un '
                       'dueto los dos tenéis que contar EL MISMO golpe. Llévalo aprendido a tu '
                       'velocidad y decidid en clase cuál es la de las dos partes juntas.'),
        ] + bloques_extra('Do mayor', 99, 'E5', 'C3',
                          'el 6/8: dos golpes por compás con tres corcheas dentro de cada uno',
                          desde=5, time_sig=(6, 8), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="It's Beginning · para casa",
            intro='Quince minutos al día, y los cinco primeros sin piano: contando y marcando con '
                  'el pie. El compás es lo único nuevo.',
            bloques=[
                reto('Contar el 6/8 en DOS golpes por compás, no en seis.',
                     'Marca el pie solo en las mayúsculas de "UN-dos-tres DOS-dos-tres". Si el pie '
                     'te va a seis, estás contando corcheas y el villancico se convierte en un '
                     'trote.'),
                plan((5, 'Contar "UN-dos-tres DOS-dos-tres" con el pie, sin tocar'),
                     (4, 'Los cc. 1 y 2, con el golpe de silencio delante'),
                     (3, 'Los cc. 3 a 5, con el compás callado del final'),
                     (3, 'Los dos pentagramas a la vez, en octavas')),
                a_cuatro_manos('En un dueto los dos tenéis que contar el mismo golpe, y en 6/8 es '
                               'fácil que uno cuente dos y el otro seis. Acordad en clase quién '
                               'marca la entrada y a qué velocidad: el Piano 2 lleva el bajo, así '
                               'que lo natural es que la marque la profesora.'),
                nombres(['E5', 'F5', 'A5', 'F#5', 'C6', 'E6', 'G5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='todas salen de tus cuatro primeros compases · ojo con la cuarta, que '
                              'lleva sostenido escrito, y con las dos que van sobre líneas '
                              'adicionales'),
                diferencias(list(C1),
                            [sil('q'), n('E5'), n('F5', 'e'), sil('e')],
                            cuantas=2,
                            titulo='Busca las diferencias',
                            pista='arriba, tu compás 1 medido · abajo, con el silencio cambiado de '
                                  'sitio'),
                acuerdate('En un compás compuesto el número de abajo dice qué figura se cuenta y el '
                          'de arriba cuántas caben. En 6/8 caben seis corcheas, pero NO se cuentan '
                          'seis: se agrupan de tres en tres y salen dos golpes. Esa es toda la '
                          'diferencia entre un 6/8 y un 3/4.',
                          etiqueta='EL COMPÁS COMPUESTO'),
                para_clase('Los cinco primeros compases contando dos golpes por compás. Y dime a '
                           'qué velocidad te salen: la del dueto la decidimos entre las dos, porque '
                           'el Piano 2 se mueve más que el 1.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
