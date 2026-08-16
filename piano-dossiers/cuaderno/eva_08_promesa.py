# -*- coding: utf-8 -*-
"""La Promesa (canción 8 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico), así que el material medido
   se importa de `dilan_08_promesa`. Ver TRANSCRIPCION_D06_08.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por la IZQUIERDA, que es la que sostiene la pieza,
       y la derecha llega después.
     - A Eva se le entra por la DERECHA, que es la que se mueve. En una pieza
       donde una mano aguanta y la otra habla, lo que hay que decidir primero
       es el ritmo del habla: si el discurso de la derecha no está claro, la
       izquierda no tiene a qué acompañar. Por eso aquí la izquierda llega en
       el paso 2, y llega ya sabiendo debajo de qué se pone.

   Andamio y cita: los acordes de la izquierda NO están medidos (van en
   cabezas huecas y el lector no los lee con seguridad), así que sus
   ejercicios son andamio en Sol mayor y se dice. Las alturas de la derecha sí
   están medidas y se citan por compás.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_08_promesa import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

CANCION = dict(
    alumno='Eva', num=8, nivel='avanzado', slug='LaPromesa',
    titulo_corto='La Promesa', time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'la-promesa-MELENDI.pdf'),
    yt='https://www.youtube.com/results?search_query=melendi+la+promesa',

    ficha=dict(
        titulo='La Promesa', autor='Ramón Melendi Espina (2004)',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'), ('Tempo', 'Lento'),
               ('Compases', '32'), ('Repeticiones', 'dos')],
        total_compases=32,
        secciones=[
            ('A', 1, 28, 'Entrada en el c. 1 · todo el cuerpo · con repetición', AZUL),
            ("A'", 29, 32, 'Vuelve el principio', OCRE),
        ],
        armonia=dict(
            titulo='Una mano habla y la otra aguanta',
            tarjetas=[
                ('LA DERECHA', 'Habla',
                 'Semicorcheas con silencios y la misma nota repetida cuatro o cinco veces.'),
                ('LA IZQUIERDA', 'Dos capas',
                 'Una nota grave abajo y un acorde de tres notas encima, a la vez y en blancas.'),
                ('LA DISTANCIA', 'Octava y media',
                 'Entre el bajo y el acorde. Ninguna mano aguanta eso: lo aguanta el pedal.'),
                ('LOS CC. 29–32', 'El principio otra vez',
                 'Las mismas notas del c. 2 al 5. Cuando llegas al final ya te lo sabías.'),
            ],
            pie='Los dos bloques llevan barra de repetición: el primero va del c. 2 al 28 y el segundo '
                'del 29 al 32. La canción entera son 32 compases, pero solo hay que aprender 28: los '
                'cuatro últimos son los cuatro primeros.',
        ),
        ritmos=[
            ('MD', 'la misma nota, repetida, con silencios: así habla (andamio)',
             [sil('e')] + corch(['C5', 'C5', 'C5', 'C5']) + [sil('e')] +
             corch(['C5', 'C5']), AZUL, 'treble', SOL),
            ('MI', 'dos blancas por compás: grave abajo y acorde encima (andamio)',
             [ac(['G2', 'B3', 'D4']), ac(['G2', 'B3', 'D4'])], OCRE, 'bass', SOL),
        ],
        especial=[
            'Armadura de un sostenido: todos los Fa son ♯.',
            'La derecha repite la misma nota cuatro y cinco veces seguidas.',
            'La izquierda toca DOS cosas a la vez: una nota grave y un acorde encima.',
            'El c. 16 es el único de toda la pieza en el que la izquierda anda: cuatro negras.',
            'Hay TRESILLOS marcados con un 3 entre los cc. 24 y 27.',
            'Pone Lento, y va en serio: esta canción se cuenta, no se corre.',
        ],
        reto='Sostener con una mano mientras la otra se mueve, y que ninguna de las dos moleste a la '
             'otra. La izquierda tiene que sonar larga y quieta debajo de una derecha que va picando '
             'notas cortas: son dos maneras de tocar distintas ocurriendo a la vez.',
        truco='Empieza por la derecha y decide cómo habla: dónde separa, dónde respira, cuántas veces '
              'repite. Con el discurso claro, la izquierda entra sola debajo, porque ya sabes a qué '
              'acompaña.',
        sabias='Melendi la escribió cuando todavía cantaba en bares de Oviedo, y durante años la tocó '
               'en directo solo con guitarra: la versión de piano vino después, y por eso el '
               'acompañamiento es tan sencillo de acordes.',
        qr=dict(titulo='Escucha la original',
                texto='Cuenta cuántas veces repite la misma nota en cada frase.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Aquí se empieza por la derecha, que es la que se mueve. En una canción donde una mano '
              'aguanta y la otra habla, lo primero que hay que decidir es el ritmo del habla: si el '
              'discurso no está claro, la izquierda no tiene a qué acompañar. Las alturas de la '
              'derecha están medidas; el ritmo va simplificado para poder leerlo.',
        reglas=['NOTAS MEDIDAS EN LA DERECHA', 'PRIMERO EL DISCURSO', 'LENTO DE VERDAD'],
        bloques=[
            dict(num=1, titulo='La derecha no canta: habla',
                 pista='cc. 5–8 medidos · las alturas son las de la partitura, el ritmo está simplificado',
                 sistemas=[
                     dict(cap='a) los cc. 6, 7 y 8 · cada compás se planta en una nota y la repite: '
                              'Si, luego Do, luego Mi — sepáralas, no las ligues',
                          events=[n('B4'), n('B4'), n('B4'), n('B4'),
                                  n('C5'), n('C5'), n('C5'), n('C5'),
                                  n('E5'), n('E5'), n('E5'), n('E5'),
                                  n('E5', 'w')],
                          bars=4),
                     dict(cap='b) lo mismo, pero entrando después del silencio · el silencio real es de '
                              'semicorchea; aquí se agranda para que lo oigas',
                          events=[sil('q'), n('B4'), n('B4'), n('B4'),
                                  sil('q'), n('C5'), n('C5'), n('C5'),
                                  sil('q'), n('E5'), n('E5'), n('E5'),
                                  n('E5', 'w')],
                          bars=4, show_time=False),
                     dict(cap='c) y el suspiro del c. 5 · en la partitura baja por debajo del '
                              'pentagrama, en semicorcheas; aquí en negras, solo para leerlo',
                          events=[n('D4'), n('D4'), n('C4'), n('B3'),
                                  n('A3'), n('A3', 'h'), sil('q'),
                                  n('A3', 'w')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SUENA HABLADA, Y POR QUÉ SE EMPIEZA AQUÍ',
                 texto='La misma nota repetida cuatro y cinco veces, con silencios de semicorchea entre '
                       'medias: eso es lo que hace que suene a alguien contando algo y no a una melodía. '
                       'No ligues esas notas, sepáralas. Y decide TÚ dónde respira la frase antes de '
                       'poner la izquierda debajo: el acompañamiento no dirige nada, solo acompaña.'),
            dict(num=2, titulo='Y debajo, lo único que suena largo', clef='bass',
                 pista='cc. 2–5 · andamio en Sol mayor: el dibujo es el de la partitura, el acorde exacto '
                       'míralo allí · el bajo y el acorde entran SIEMPRE a la vez',
                 sistemas=[
                     dict(cap='a) solo la nota grave, una por compás: Sol · Mi · Do · Re, y nada más',
                          events=[n(p, 'w') for p in ('G2', 'E2', 'C2', 'D2')],
                          bars=4, clef='bass'),
                     dict(cap='b) y ahora con el acorde encima, en el mismo golpe · mira la distancia '
                              'que hay entre las dos cosas',
                          events=[ac(['G2', 'D3', 'B3']), ac(['G2', 'D3', 'B3']),
                                  ac(['E2', 'B2', 'G3']), ac(['E2', 'B2', 'G3']),
                                  ac(['C2', 'G2', 'E3']), ac(['C2', 'G2', 'E3']),
                                  ac(['D2', 'A2', 'F3']), ac(['D2', 'A2', 'F3'])],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y separando las dos capas a propósito · primero el grave y luego el '
                              'acorde: es para comprobar que llegas, no para tocarlo así',
                          events=[n('G2', 'h'), ac(['B3', 'D4'], 'h'),
                                  n('E2', 'h'), ac(['G3', 'B3'], 'h'),
                                  n('C2', 'h'), ac(['E3', 'G3'], 'h'),
                                  n('D2', 'h'), ac(['F3', 'A3'], 'h')],
                          bars=4, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Ya sabes cómo habla la derecha y qué hay debajo. Queda ver la canción entera de un '
              'vistazo —que es más corta de lo que parece— y los dos sitios donde cambia algo: el c. 16 '
              'y la costura del 28 al 29.',
        reglas=['LOS CC. 29–32 SON LOS CC. 2–5', 'EL PEDAL SOSTIENE, NO LA MANO', 'SE CUENTA, NO SE CORRE'],
        bloques=[
            dict(num=3, titulo='La canción entera, a un golpe por compás', clef='bass',
                 pista='andamio · toca solo el acorde que cae en el uno y salta al compás siguiente',
                 sistemas=[
                     dict(cap='a) ocho compases seguidos, un acorde por compás: así se oye por dónde va '
                              'la canción sin tocar ni una nota de la melodía',
                          events=[ac(['G2', 'D3', 'G3'], 'w'), ac(['E2', 'B2', 'E3'], 'w'),
                                  ac(['C2', 'G2', 'C3'], 'w'), ac(['D2', 'A2', 'D3'], 'w'),
                                  ac(['G2', 'D3', 'G3'], 'w'), ac(['E2', 'B2', 'E3'], 'w'),
                                  ac(['A2', 'E3', 'A3'], 'w'), ac(['D2', 'A2', 'D3'], 'w')],
                          bars=8, clef='bass'),
                     dict(cap='b) y solo el recorrido, escrito una octava arriba para que se vea sin '
                              'líneas adicionales · dilo en voz alta: Sol, Mi, Do, Re, Sol, Mi, La, Re',
                          events=[n(p, 'w') for p in ('G3', 'E3', 'C3', 'D3',
                                                      'G3', 'E3', 'A3', 'D3')],
                          bars=8, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='ESTO NO SE SOSTIENE CON LA MANO',
                 texto='La nota grave y el acorde están escritos como blancas: suenan los dos tiempos. '
                       'Pero entre ellos hay más de una octava y media, y esa distancia no la aguanta '
                       'ninguna mano. Se aguanta con el PEDAL, y el pedal se cambia justo DESPUÉS de '
                       'tocar el acorde nuevo, nunca antes. Si lo cambias antes, el bajo desaparece y la '
                       'canción se queda sin suelo.'),
            dict(num=4, titulo='Los dos sitios donde cambia algo',
                 pista='el c. 16 y la costura del 28 al 29 · los únicos dos sitios que hay que estudiar aparte',
                 sistemas=[
                     dict(cap='a) el c. 16 · el único compás de toda la canción en el que la izquierda '
                              'anda: deja las blancas y toca cuatro negras',
                          events=[ac(['C2', 'E3', 'G3'], 'q'), ac(['C2', 'E3', 'G3'], 'q'),
                                  ac(['C2', 'E3', 'G3'], 'q'), ac(['C2', 'E3', 'G3'], 'q'),
                                  ac(['C2', 'E3', 'G3'], 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) la costura del c. 28 al 29 (andamio) · para y respira en la barra: '
                              'lo que viene detrás es la frase del principio',
                          events=[n('D5', 'h'), n('B4', 'h'), n('A4', 'h'), sil('h'),
                                  n('B4'), n('B4'), n('A4'), n('B4'),
                                  n('B4', 'w')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LOS TRESILLOS DE LOS CC. 24 AL 27',
                 texto='Ahí aparece un 3 encima de algunos grupos: en ese tiempo caben tres notas donde '
                       'normalmente caben dos. No se toca más rápido, se reparte el mismo tiempo entre '
                       'tres. Y es el sitio donde la canción se calienta: los tresillos empujan justo '
                       'antes de que vuelva la frase del principio.'),
            dict(tipo='escalera', valores=[44, 50, 56, 62, 68, 72],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
