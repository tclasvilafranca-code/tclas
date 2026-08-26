# -*- coding: utf-8 -*-
"""Honor Him (Gladiator) — pieza 15 de Eduard. Formato ADULTO.

   Medido sobre el PDF de su carpeta (vectorial, dos pentagramas por sistema):

     - 3/4 y detras de la clave hay **TRES SOSTENIDOS**. Es la primera
       armadura de verdad del cuaderno, y la mas grande que va a ver este
       curso. Tres sostenidos son Fa#, Do# y Sol#.
     - Pone **mp**.
     - Medido a 300 ppp:

         DERECHA    c. 1   callada (silencio de compas)
                    c. 2   callada
                    c. 3   Do#4 · Fa#4 · La4      tres negras
         IZQUIERDA  c. 1   Fa#2                    blanca con puntillo
                    c. 2   Fa#2                    blanca con puntillo, ligada
                    c. 3   Fa#2                    blanca con puntillo, ligada

     - Las tres notas de la izquierda van unidas por LIGADURAS DE UNION: es una
       sola nota que suena tres compases seguidos. Se toca una vez y se aguanta.

   POR QUE SE DICE QUE ES FA# MENOR Y NO LA MAYOR. Las dos tonalidades llevan
   tres sostenidos y la armadura no las distingue. Lo que las distingue es
   donde descansa la musica, y aqui esta clarisimo: la izquierda aguanta un
   Fa#2 tres compases enteros, y las tres notas de la derecha del c. 3 son
   Do#, Fa# y La, que son justamente las tres notas del acorde de Fa# menor.

   POR QUE VA TAN AL FINAL. No por las notas —son tres— sino por la armadura.
   Tres sostenidos obligan a mirar el principio del pentagrama antes de tocar
   una sola tecla, y esa costumbre se coge mejor cuando ya no hay que pensar en
   nada mas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, sil, plan, metronomo, teclado, verdadero_falso,
                      dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FASM = 'Fa# menor'

# Los compases 1 a 3 de la DERECHA, medidos. Cita literal: dos compases
# callados y la entrada.
ENTRADA = [sil('h.'), sil('h.'), n('C#4'), n('F#4'), n('A4')]

# Los compases 1 y 2 de la IZQUIERDA, medidos: una sola nota, ligada.
BAJO = [dict(n('F#2', 'h.'), lig=1), n('F#2', 'h.')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=15, nivel='iniciación',
    slug='HonorHim', formato='adulto',
    titulo_corto='Honor Him · Gladiator', time_sig=(3, 4), key_sig=FASM,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Honor Him Gladiator.pdf'),
    yt='https://www.youtube.com/results?search_query=honor+him+gladiator+piano+easy',

    ficha=dict(
        titulo='Honor Him',
        autor='Hans Zimmer · banda sonora de Gladiator · arreglo fácil',
        datos=[('Tonalidad', 'Fa# menor'), ('Compás', '3/4'),
               ('Armadura', '3 sostenidos'), ('Manos', 'Las dos, por turnos'),
               ('Volumen', 'mp')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, los compases 1 a 3 de la derecha: dos callada y '
                   'la entrada. Abajo, la izquierda: una sola nota que dura y dura.',
        armonia=dict(
            titulo='Tres sostenidos, y casi ninguna nota',
            tarjetas=[
                ('LA ARMADURA', 'Fa# · Do# · Sol#',
                 'Detrás de la clave hay tres sostenidos. Eso quiere decir que TODOS los Fa, los Do '
                 'y los Sol de la pieza son teclas negras, aunque no lleven ningún símbolo al lado.'),
                ('FA# MENOR', 'Dónde descansa',
                 'La menor con tres sostenidos. La izquierda aguanta un Fa# tres compases: esa nota '
                 'es la casa a la que vuelve todo.'),
                ('LA LIGADURA', 'Suena una vez',
                 'Las tres notas largas de abajo están unidas por ligaduras. No se vuelven a tocar: '
                 'se toca la primera y se aguanta el dedo tres compases enteros.'),
                ('DOS COMPASES', 'Sin tocar',
                 'La derecha no entra hasta el compás 3. Otra vez toca contar sin tocar, como en La '
                 'Pantera Rosa, pero ahora en compás de tres.'),
            ],
            pie='Esta pieza tiene menos notas que ninguna otra del cuaderno y aun así es de las '
                'últimas. La dificultad no está en los dedos: está en mirar la armadura antes de '
                'tocar y en aguantar un sonido sin ponerse nervioso.',
        ),
        ritmos=[
            ('LA DERECHA', 'cc. 1–3, medidos · no entra hasta el tercero',
             ENTRADA, OCRE, 'treble', FASM),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · una nota ligada, que no se repite',
             BAJO, AZUL, 'bass', FASM),
        ],
        especial=[
            'Detrás de la clave hay TRES sostenidos: Fa#, Do# y Sol#.',
            'Compás de 3/4: tres golpes por compás.',
            'La derecha no toca en los dos primeros compases.',
            'La izquierda aguanta una sola nota tres compases seguidos.',
            'Las notas largas van unidas por ligaduras: no se repiten.',
            'Pone "mp": medio suave.',
        ],
        reto='Acordarte de la armadura. Tres sostenidos son tres teclas negras que valen para toda '
             'la pieza, y no vuelven a avisarte: el símbolo solo está al principio de cada línea.',
        truco='Antes de tocar, toca las tres teclas negras de la armadura —Fa#, Do# y Sol#— y dilas '
              'en voz alta. Diez segundos. Hazlo cada vez que te sientes al piano con esta pieza '
              'hasta que la mano vaya sola.',
        sabias='Hans Zimmer escribió la música de Gladiator en 1999 y esta pieza suena en el final '
               'de la película. La grabó con una orquesta pequeña y muchas voces, y casi todo el '
               'tema se sostiene sobre una nota grave que no se mueve: justo lo que hace tu '
               'izquierda.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el fondo, no la melodía: hay una nota grave que se queda quieta '
                      'debajo de todo. Esa es tu mano izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí lo que hay que estudiar no son las notas, que son cuatro: es la armadura y la '
              'paciencia. Se empieza tocando las tres teclas negras y contando.',
        reglas=['FA#, DO# Y SOL#: SIEMPRE NEGRAS', 'LA LIGADURA NO SE VUELVE A TOCAR',
                'CUENTA LOS DOS COMPASES CALLADOS'],
        bloques=[
            dict(num=1, titulo='Las tres teclas negras de la armadura',
                 pista='andamio en Fa# menor · las teclas que manda el principio del pentagrama',
                 sistemas=[
                     dict(cap='a) las tres, una detrás de otra · dilas en voz alta mientras tocas',
                          events=[n('F#4', 'h.'), n('C#4', 'h.'), n('G#4', 'h.')],
                          key_sig=FASM, matiz='mp',
                          bars=3),
                     dict(cap='b) y mezcladas con teclas blancas, para no confiarte',
                          events=[n('F#4'), n('A4'), n('C#5'), n('B4'), n('G#4'), n('F#4')],
                          key_sig=FASM, bars=2, show_time=False),
                     dict(cap='c) la escala entera de Fa# menor, subiendo · tres negras y una larga',
                          events=[n('F#4'), n('G#4'), n('A4'), n('B4'), n('C#5'), n('D5'),
                                  n('E5'), n('F#5'), n('E5'), n('D5', 'h.')],
                          key_sig=FASM, bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE LEE UNA ARMADURA DE TRES SOSTENIDOS',
                 texto='Los tres sostenidos siempre aparecen en el mismo orden: Fa, Do, Sol. Si ves '
                       'tres, ya sabes cuáles son sin mirarlos uno a uno. Y valen para TODOS los Fa, '
                       'Do y Sol de la pieza, en cualquier octava, hasta el final. Es la manera que '
                       'tiene la música de no repetir el mismo símbolo cuatrocientas veces.'),
            dict(num=2, titulo='La izquierda: tocar una vez y aguantar', clef='bass',
                 pista='cc. 1–3 · medidos en tu partitura · una sola nota',
                 sistemas=[
                     dict(cap='a) tres compases de una nota, sin volver a tocarla · cuenta nueve',
                          events=[dict(n('F#2', 'h.'), lig=2), n('F#2', 'h.'), n('F#2', 'h.')],
                          key_sig=FASM, bars=3, clef='bass'),
                     dict(cap='b) y ahora cambiando de nota cada tres compases, que es lo que hará',
                          events=[dict(n('F#2', 'h.'), lig=1), n('F#2', 'h.'),
                                  dict(n('C#3', 'h.'), lig=1), n('C#3', 'h.')],
                          key_sig=FASM, bars=4, clef='bass', show_time=False),
                     dict(cap='c) y con el acorde de Fa# menor desplegado debajo, para colocar la mano',
                          events=[n('F#2'), n('C#3'), n('F#3'), n('C#3'), n('F#2'), n('C#3'),
                                  n('F#3'), n('A3'), n('F#3'), n('F#2', 'h.')],
                          key_sig=FASM, bars=4, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='La entrada de la derecha, en el compás 3',
                 pista='cc. 1–3 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) las tres notas solas: son el acorde de Fa# menor, una a una',
                          events=[n('C#4'), n('F#4'), n('A4'), n('C#4'), n('F#4'), n('A4')],
                          key_sig=FASM, bars=2),
                     dict(cap='b) y con los dos compases callados delante · no toques hasta el tres',
                          events=[sil('h.'), sil('h.'), n('C#4'), n('F#4'), n('A4'),
                                  n('F#4', 'h.')],
                          key_sig=FASM, bars=4, show_time=False),
                     dict(cap='c) y las dos manos: abajo la misma nota compás a compás —en tu partitura va '
                              'ligada, se toca una vez— y arriba la entrada',
                          events=[ac(('F#2',), 'h.'), ac(('F#2',), 'h.'),
                                  ac(('F#2', 'C#4')), ac(('F#4',)), ac(('A4',)),
                                  ac(('F#2', 'F#4'), 'h.')],
                          key_sig=FASM, bars=4, manos='sostiene', show_time=False),
                 ]),
            dict(num=4, titulo='Y el sonido, que es de lo que va esta pieza',
                 pista='andamio en Fa# menor · lo mismo tocado de dos maneras distintas',
                 sistemas=[
                     dict(cap='a) las tres notas del acorde muy suave, aguantando cada una',
                          events=[n('C#4', 'h.'), n('F#4', 'h.'), n('A4', 'h.'), n('F#4', 'h.')],
                          key_sig=FASM, matiz='mp', bars=4),
                     dict(cap='b) y las tres a la vez, que es el acorde entero · escúchalo hasta que '
                              'se apague',
                          events=[ac(('C#4', 'F#4', 'A4'), 'h.'), ac(('C#4', 'F#4', 'A4'), 'h.')],
                          key_sig=FASM, bars=2, show_time=False),
                     dict(cap='c) y con la izquierda debajo, que es como suena en tu partitura',
                          events=[ac(('F#2', 'F#4', 'A4'), 'h.'),
                                  ac(('F#2', 'F#4', 'A4'), 'h.'),
                                  ac(('F#2', 'F#4', 'A4'), 'h.')],
                          key_sig=FASM, bars=3, manos='dobla', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Honor Him · para casa',
            intro='Quince minutos al día, y no hacen falta más: la pieza tiene cuatro notas. Lo que '
                  'se trabaja es leer la armadura y aguantar el sonido.',
            bloques=[
                plan((3, 'Tocar y decir en voz alta las tres teclas de la armadura'),
                     (4, 'La izquierda: una nota, tres compases, contando nueve'),
                     (4, 'Las tres notas de la derecha del compás 3'),
                     (4, 'Los tres primeros compases con las dos manos')),
                metronomo('Empieza a ♩ = 50: es una pieza lenta y suena mejor cuanto más quieta.',
                          'Tu partitura no trae número de metrónomo, así que este es de trabajo.'),
                teclado([('Fa#', 'la primera de la armadura'), ('Do#', 'la segunda'),
                         ('Sol#', 'la tercera')],
                        ['¿Las tres son teclas negras?',
                         '¿Cuál de las tres NO aparece en el compás 3?'],
                        titulo='Marca en el teclado las tres teclas de la armadura',
                        pista='y fíjate en dónde está cada una dentro de su grupo de negras'),
                verdadero_falso([
                    ('La armadura de esta pieza tiene tres sostenidos.', True),
                    ('El sostenido solo vale para la nota que lo lleva al lado.', False),
                    ('La mano derecha empieza a tocar en el compás 1.', False),
                    ('La nota larga de la izquierda se vuelve a tocar cada compás.', False),
                    ('La pieza va en compás de tres tiempos.', True),
                ],
                    titulo='Verdadero o falso, mirando tu partitura',
                    pista='marca la casilla · todas se contestan con la primera línea'),
                dibujar(['Fa#', 'Do#', 'Sol#'],
                        titulo='Dibuja tú estas tres notas con su sostenido',
                        pista='en clave de sol · el símbolo va SIEMPRE delante de la nota'),
                para_clase('Los tres primeros compases con las dos manos, y las tres teclas de la '
                           'armadura dichas de memoria. Si te has equivocado de tecla alguna vez, '
                           'trae marcado dónde.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Fa# menor', 75, 'F#4', 'F#2',
    'tres sostenidos: hay que mirarlos antes de tocar la primera tecla',
    desde=4, time_sig=(3, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
