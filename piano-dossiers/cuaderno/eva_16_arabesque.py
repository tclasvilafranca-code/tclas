# -*- coding: utf-8 -*-
"""Arabesque (canción 16 de Eva, nivel avanzado). A CUATRO MANOS.

   Burgmüller op. 100 nº 2, arr. a cuatro manos de MB. Misma edición que la de
   Dilan (sha256 idéntico); el material medido se importa de
   `dilan_17_arabesque`. Ver TRANSCRIPCION_D15_17.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por las NOTAS: la célula, la subida, la bajada.
     - A Eva se le entra por el ATAQUE, porque esta pieza no es una canción:
       es un ESTUDIO. El op. 100 de Burgmüller son veinticinco estudios y cada
       uno entrena una cosa concreta; el nº 2 entrena dedo ligero y picado a
       velocidad. Las notas son cinco y se aprenden en dos minutos — si se
       estudian como si fueran el contenido, se acaba tocando el estudio sin
       estudiar nada. Por eso el paso 1 es la misma célula tocada de tres
       maneras distintas, y lo que se compara es el sonido, no los dedos.

   La menor, sin armadura: todas las alteraciones van escritas. El dosier está
   escrito para el PRIMO, que es la parte de la alumna.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_17_arabesque import (n, ac, sil, corch, CELULA, SUBIDA, BAJADA)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eva', num=16, nivel='avanzado', slug='Arabesque',
    titulo_corto='Arabesque', time_sig=(2, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'arabesque-burgmuller-( 4 manos).pdf'),
    yt='https://www.youtube.com/results?search_query=burgmuller+arabesque+op+100',

    ficha=dict(
        titulo='Arabesque',
        autor='Johann Friedrich Burgmüller · op. 100 nº 2 (1851) · arreglo a cuatro manos de MB',
        datos=[('Tonalidad', 'La menor'), ('Compás', '2/4'), ('Tempo', 'Allegro scherzando'),
               ('Formato', '4 manos'), ('Tu parte', 'Primo')],
        armonia=dict(
            titulo='Esto no es una canción: es un estudio',
            tarjetas=[
                ('QUÉ ENTRENA', 'Dedo ligero y rápido',
                 'El op. 100 son veinticinco estudios y cada uno trabaja una cosa. Este, el ataque.'),
                ('LA CÉLULA', 'La · Si · Do · Si · La',
                 'Cinco notas, en los cc. 3, 9 y 31. Eso es casi toda tu parte.'),
                ('TUS DOS MANOS', 'Lo mismo, a la octava',
                 'No hay independencia que resolver: las dos hacen exactamente lo mismo.'),
                ('EL 8VA', 'Desde el c. 5',
                 'Una línea de puntos: todo lo que hay debajo suena una octava más arriba.'),
            ],
            pie='Las notas de tu parte se aprenden en dos minutos. Lo que cuesta —y lo único que se '
                'está entrenando— es que suenen cortas, ligeras y todas iguales a Allegro. Por eso este '
                'cuaderno compara la misma célula tocada de tres maneras: lo que se juzga es el sonido.',
        ),
        ritmos=[
            ('MD', 'la célula: cuatro semicorcheas y una nota larga (ritmo simplificado)',
             CELULA, AZUL, 'treble', None),
            ('MD · andamio', 'la misma célula en negras, para colocar',
             [n('A4'), n('B4'), n('C5'), n('B4')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay armadura: la pieza está en La menor y las alteraciones van escritas.',
            'Compás de 2/4 y tempo Allegro scherzando: rápido y con guasa.',
            'Es a cuatro manos: tú tocas el Primo y la profesora el Secondo.',
            'Tus dos manos tocan lo mismo, separadas por una octava.',
            'Desde el c. 5 hay un 8va: se toca una octava más arriba de lo escrito.',
            'Tú NO empiezas la pieza: entras en el c. 3, después de dos compases.',
        ],
        reto='Que las notas suenen cortas, ligeras y todas iguales — a velocidad. Es un estudio de '
             'ataque: cuando se acelera, la mano tiende a apretar, y en cuanto aprieta las notas se '
             'alargan y el picado desaparece sin que te des cuenta.',
        truco='Toca la célula tres veces seguidas: en negras sin picar, en negras picadas, y como está '
              'escrita. Escucha las tres y quédate con la sensación de la segunda, que es la que hay '
              'que llevarse a la tercera. El picado se decide despacio; a velocidad ya solo se '
              'mantiene.',
        sabias='Burgmüller escribió los veinticinco estudios del op. 100 con un título para cada uno '
               'para que los alumnos no sintieran que estaban haciendo ejercicios. Funcionó tan bien '
               'que “Arabesque” lleva 170 años tocándose, y casi nadie recuerda que es un estudio.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en lo cortas que son las notas. Eso es todo lo que hay que copiar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Tu parte son cinco notas y se aprenden en dos minutos. Lo que se estudia aquí es otra '
              'cosa: cómo suenan. Es un estudio de ataque, así que el paso 1 es la misma célula tocada '
              'de tres maneras, comparando el sonido. El ritmo real va en semicorcheas; aquí está '
              'simplificado para poder leerlo.',
        reglas=['ESTO ES UN ESTUDIO DE ATAQUE', 'CORTO NO ES FUERTE', 'EL PICADO SE DECIDE DESPACIO'],
        bloques=[
            dict(num=1, titulo='La misma célula, de tres maneras', clef='treble',
                 pista='cc. 3–4 medidos · las dos manos a la vez, la izquierda una octava más abajo',
                 sistemas=[
                     dict(cap='a) primero en negras y SIN picar, con el dedo pegado a la tecla · esto '
                              'es solo para colocar la mano y oír la afinación del gesto',
                          events=[n('A4'), n('B4'), n('C5'), n('B4'), n('A4', 'h')],
                          bars=3),
                     dict(cap='b) las mismas notas en negras pero PICADAS · la mano rebota y se va; si '
                              'suenan más fuertes que en la a), estás apretando en vez de soltar',
                          events=[n('A4'), n('B4'), n('C5'), n('B4'), n('A4', 'h')],
                          bars=3, show_time=False),
                     dict(cap='c) y ya como está escrita, con la subida detrás · cc. 3–4: mismo picado '
                              'de la b), solo que ahora deprisa',
                          events=CELULA + SUBIDA + CELULA + SUBIDA, bars=4, show_time=False),
                     dict(cap='d) y la subida sola, que es la otra mitad de tu parte · cc. 4, 25 y 30: '
                              'cinco notas seguidas subiendo, sin ningún salto',
                          events=SUBIDA + SUBIDA, bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LAS TRES MANERAS, Y EN ESE ORDEN',
                 texto='La a) te dice dónde están las notas. La b) te dice a qué suena el picado cuando '
                       'hay tiempo de sobra para hacerlo bien: ese sonido es el objetivo, y hay que '
                       'memorizarlo con el oído, no con los dedos. La c) es la pieza. Si al llegar a la '
                       'c) el sonido no se parece al de la b), no es que vayas rápido: es que has '
                       'cambiado de gesto sin querer. Vuelve a la b), escúchala otra vez y sube desde '
                       'ahí. Esto es exactamente lo que Burgmüller quería que aprendieras.'),
            dict(num=2, titulo='El 8va del c. 5, ya en su sitio',
                 pista='cc. 5–6 · andamio sobre las notas medidas, escrito donde de verdad se toca',
                 sistemas=[
                     dict(cap='a) practícala ya en la octava buena · si la lees donde está escrita y '
                              'luego la subes, se te caerá siempre en el mismo punto',
                          events=corch(['A5', 'B5', 'C6', 'B5']) + [n('A5', 'h')] +
                                 corch(['D6', 'E6', 'F6', 'G6']) + [n('A6', 'h')],
                          bars=4),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Tu parte puede estar perfecta y la pieza no funcionar. Lo que viene aquí no se estudia '
              'sola: se trabaja en clase, las dos sentadas al piano. Ven con los pasos 1 y 2 sabidos y '
              'aprovecha la clase para esto.',
        reglas=['ENTRÁIS EN EL C. 3, NO EN EL 1', 'CONTAD JUNTAS EN VOZ ALTA', 'NADIE ACELERA POR SU CUENTA'],
        bloques=[
            dict(num=3, titulo='Los dos compases de espera',
                 pista='cc. 1–3 · lo que tú haces mientras suena la introducción: contar',
                 sistemas=[
                     dict(cap='a) dos compases de silencio y entras · cuéntalos en voz alta, no de '
                              'memoria, y respira justo antes de tocar',
                          events=[sil('h'), sil('h')] + CELULA, bars=4),
                     dict(cap='b) y la escala que baja del c. 33, que cierra la pieza · el último La se '
                              'suelta, no se remata, y las dos tenéis que soltarlo a la vez',
                          events=BAJADA + BAJADA, bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='TÚ NO EMPIEZAS LA PIEZA',
                 texto='Los cc. 1 y 2 los toca la otra parte sola: acordes picados y el bajo. Tú entras '
                       'en el c. 3, y ese es el momento más delicado de toda la pieza. No cuentes por '
                       'dentro: contad las dos en voz alta “un-dos, un-dos” durante los dos compases de '
                       'introducción, y respira justo antes de entrar. Si respiras, entras a tiempo casi '
                       'sin querer.'),
            dict(num=4, titulo='Lo que toca la otra parte', clef='bass',
                 pista='Secondo medido · La m · Re m · Do · Sol7 · esto NO lo tocas tú',
                 sistemas=[
                     dict(cap='a) escúchalo y aprende dónde cambia: es lo que te va a decir si vas bien',
                          events=[ac(('A2', 'C3', 'E3')), ac(('A2', 'C3', 'E3')),
                                  ac(('A2', 'D3', 'F3')), ac(('A2', 'D3', 'F3')),
                                  ac(('G2', 'C3', 'E3')), ac(('G2', 'C3', 'E3')),
                                  ac(('G2', 'B2', 'F3')), ac(('G2', 'B2', 'F3'))],
                          bars=4, clef='bass'),
                     dict(cap='b) y solo su bajo · La · La · Sol · Sol: apréndetelo de oído, porque '
                              'cuando cambia tú tienes que estar ya en el sitio',
                          events=[n('A2', 'h'), n('A2', 'h'), n('G2', 'h'), n('G2', 'h')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA PIEZA SE ESTUDIA DISTINTO',
                 texto='En casi todas las demás del cuaderno el problema es coordinar tus dos manos. '
                       'Aquí tus dos manos hacen lo mismo, así que ese problema no existe: la parte que '
                       'se estudia en casa es la fácil, y la difícil solo se puede trabajar en pareja. '
                       'Entrad juntas en el c. 3 una y otra vez, hasta que no haga falta ninguna señal '
                       'ni ninguna mirada.'),
            dict(tipo='escalera', valores=[60, 76, 88, 100, 112, 126],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
