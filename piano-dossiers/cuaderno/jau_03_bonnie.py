# -*- coding: utf-8 -*-
"""My Bonnie Lies Over the Ocean — pieza 3 de Jaume. Formato ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (arr. Gilbert
   DeBenedetti, edición Gradimi "Level Two", 1 página), mirado a 110 dpi. El
   archivo es una imagen de 77 ppi: no se puede medir con el programa, así que
   todo lo que sigue es lectura a ojo, compás a compás:

     - 3/4, sin armadura, "Slowly, longingly". La LETRA de la canción va
       impresa debajo del pentagrama de arriba.
     - **Empieza en anacrusa**: la derecha con un silencio de negra y la
       izquierda con un Sol de negra; el primer compás entero empieza después.
     - La derecha casi no toca: en los cc. 1-2 hace Mi · Re · Do y Re · Do con
       un silencio de negra, y los cc. 3 y 4 son **dos compases enteros de
       silencio**. La melodía, en lo que se canta.
     - La izquierda lleva la armonía: blanca con puntillo de Do en el c. 1, blanca
       de Fa y negra de La en el c. 2, y en varios compases hace dos notas a la
       vez.
     - Pone **"shift"** varias veces: la mano cambia de sitio en el teclado.
     - **Un Fa sostenido** en la izquierda, en blanca con puntillo (c. 6): la
       única tecla negra de la página.
     - Al final, **"l. h. over"**: la izquierda cruza por encima de la derecha.
     - La digitación va impresa en las dos manos, con los cinco números.

   Tercera pieza del álbum y la primera donde **no se toca la melodía**: la
   derecha espera y la izquierda manda. Con la base musical que tiene Jaume,
   el trabajo no es leer sino contar los silencios y dejar sonar el bajo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, metronomo, inventa, dibujar,
                       verdadero_falso, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=3, nivel='intermedio', slug='MyBonnie',
    formato='adulto',
    titulo_corto='My Bonnie', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'MyBonnie.pdf'),
    yt='https://www.youtube.com/results?search_query=my+bonnie+lies+over+the+ocean+piano',

    ficha=dict(
        titulo='My Bonnie Lies Over the Ocean',
        autor='Canción popular · arreglo de Gilbert DeBenedetti · «Level Two»',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'Slowly'), ('Empieza', 'En anacrusa'),
               ('Páginas', 'Una')],
        titulo_ritmos='El primer compás, mano a mano',
        pie_ritmos='Leído sobre tu partitura: la derecha hace Mi · Re · Do y la izquierda una blanca con '
                   'puntillo de Do. Los dedos, en tu partitura.',
        armonia=dict(
            titulo='La derecha espera, la izquierda manda',
            tarjetas=[
                ('LA IZQUIERDA', 'Lleva la armonía',
                 'Blanca con puntillo de Do, luego Fa y La, y en varios compases dos notas a la '
                 'vez. Es la que sostiene la canción mientras se canta la melodía.'),
                ('LOS SILENCIOS', 'Dos compases mudos',
                 'Los cc. 3 y 4 de la derecha son silencio de compás entero. No se tocan, se '
                 'cuentan: tres golpes cada uno, sin acelerar.'),
                ('"SHIFT"', 'La mano se muda',
                 'Aparece varias veces escrito debajo del pentagrama: es el aviso de que la mano '
                 'cambia de posición. No hay que buscar la tecla: hay que irse ya.'),
                ('"L. H. OVER"', 'Cruce de manos',
                 'En el último sistema la izquierda pasa por encima de la derecha. Es lo único '
                 'de la pieza que no se resuelve con la posición de siempre.'),
            ],
            pie='Es la primera pieza del cuaderno que no se toca para cantar la melodía sino para '
                'acompañarla. La letra va impresa debajo: úsala para saber dónde respira cada '
                'frase.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · leído de tu partitura',
             [n('E4'), n('D4'), n('C4')],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'c. 1 · leído de tu partitura',
             [n('C3', 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Pone "Slowly, longingly": despacio y con nostalgia.',
            'Empieza en anacrusa: un silencio en la derecha y un Sol en la izquierda antes del '
            'primer compás.',
            'La derecha tiene dos compases enteros de silencio, los cc. 3 y 4.',
            'Aparece "shift" varias veces: la mano cambia de posición.',
            'Hay un Fa sostenido en la izquierda: la única tecla negra de la página.',
            'Al final pone "l. h. over": la izquierda cruza por encima de la derecha.',
        ],
        reto='Contar dos compases de silencio sin moverte y entrar a tiempo. Con la mano derecha '
             'parada no hay nada que te guíe: solo el pulso de tres.',
        truco='Cuenta los tres golpes en voz alta los dos compases mudos, y deja sonar la '
              'blanca de la izquierda hasta el final del compás. Si cuando entra la derecha el '
              'bajo se ha cortado, ya lo estás contando de dos.',
        sabias='Es una canción popular de finales del siglo XIX. En 1961 Tony Sheridan la grabó en '
               'Hamburgo con los Beatles de grupo de acompañamiento, en uno de sus primeros '
               'discos.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la letra y fíjate en cuándo calla el que canta: es justo el sitio '
                      'donde tu mano derecha se para, los dos compases mudos.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza se estudia de abajo arriba: primero la izquierda, que es la que manda, y '
              'después la derecha, que casi solo tiene que saber esperar.',
        reglas=['LA IZQUIERDA PRIMERO', 'LOS SILENCIOS SE CUENTAN', 'EL "SHIFT" NO SE BUSCA'],
        bloques=[
            dict(num=1, titulo='La izquierda sola, los dos primeros compases',
                 pista='cc. 1-2 · leído de tu partitura · blanca con puntillo, blanca y negra',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) cuenta tres y deja sonar la blanca con puntillo hasta el final '
                              'del compás · el Fa y el La son una frase, no dos notas',
                          events=[n('C3', 'h.'), n('F3', 'h'), n('A3')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=2, titulo='La derecha: tres notas y un silencio',
                 pista='cc. 1-2 · leído de tu partitura · Mi, Re, Do, y vuelta',
                 sistemas=[
                     dict(cap='a) cántala con los nombres antes de tocarla · el silencio de negra '
                              'del final del c. 2 es el que da paso a los dos compases mudos',
                          events=[n('E4'), n('D4'), n('C4'), n('D4'), n('C4'), sil('q')],
                          bars=2),
                 ]),
            dict(num=3, titulo='Dos compases de silencio',
                 pista='cc. 3-4 · la derecha no toca · andamio en la izquierda para llenar el hueco',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) cuenta en voz alta "uno, dos, tres" mientras la izquierda hace '
                              'esto · si te pierdes en el segundo compás, el tercero no se arregla',
                          events=[n('G3'), n('E3', 'h'), n('E3', 'h'), n('G3')],
                          bars=2, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='CUÉNTALOS CANTANDO',
                 texto='Los dos compases mudos son el sitio donde en la canción se sostiene la '
                       'palabra "ocean". Cántala mentalmente, sin mover los dedos, y entra '
                       'cuando la hayas acabado de decir. Contar el silencio con la letra sale más '
                       'solo que contarlo con números.'),
            dict(num=4, titulo='El Fa sostenido de la izquierda',
                 pista='c. 6 · una blanca con puntillo con sostenido · andamio en tres compases',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) la tecla negra de paso entre el Mi y el Sol · el sostenido va '
                              'delante de la nota y vale solo para ese compás',
                          events=[n('E3', 'h.'), n('F#3', 'h.'), n('G3', 'h.')],
                          bars=3, clef='bass'),
                 ]),
            dict(num=5, titulo='El "shift": la misma frase en otro sitio',
                 pista='andamio · la mano se muda una cuarta y la frase es la misma',
                 sistemas=[
                     dict(cap='a) tres notas bajando, empezando en el Mi · luego, sin parar, en el '
                              'La · lo difícil no son las notas: es no frenar al mudarse',
                          events=[n('E4'), n('D4'), n('C4'), n('A4'), n('G4'), n('F4')],
                          bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL "L. H. OVER" SE ESTUDIA SIN PIANO',
                 texto='Antes de cruzar las manos en el teclado, hazlo sobre la mesa: derecha '
                       'quieta, izquierda por encima, sin tocarla. El cruce no es de dedos, es '
                       'del codo: si lo subes, la izquierda llega sin esfuerzo.'),
            dict(num=6, titulo='Las dos manos, los dos primeros compases',
                 pista='cc. 1-2 · leído de tu partitura · la izquierda sostiene mientras la '
                       'derecha canta',
                 sistemas=[
                     dict(cap='a) la blanca con puntillo del bajo no se corta cuando entra el Re '
                              '· en el c. 2 el bajo se mueve en el tercer golpe y la derecha calla',
                          events=[ac(('C3', 'E4')), n('D4'), n('C4'),
                                  ac(('F3', 'D4')), n('C4'), n('A3')],
                          bars=2, manos='sostiene'),
                 ]),
        ] + bloques_extra('Do mayor', 3, 'C4', 'C3',
                          'la derecha espera: lo que se estudia es el pulso de tres',
                          desde=7, time_sig=(3, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='My Bonnie · para casa',
            intro='Veinte minutos al día. Se estudia la izquierda y se cuentan los silencios; la '
                  'velocidad la pone la letra.',
            bloques=[
                plan((5, 'La izquierda sola, de principio a fin, dejando sonar las blancas'),
                     (5, 'La derecha sola, cantando la letra y contando los silencios'),
                     (6, 'Las dos manos, hasta el primer "shift"'),
                     (4, 'El cruce final sobre la mesa, sin piano')),
                metronomo('Empieza a ♩ = 52 y no pases de ahí hasta que los dos compases mudos '
                          'salgan sin contarlos con los labios.',
                          'La partitura no trae tempo impreso: pone solo "Slowly, longingly".',
                          titulo='A qué velocidad te sale'),
                verdadero_falso([
                    'La pieza empieza en el tiempo uno del primer compás.',
                    'En los cc. 3 y 4 la derecha no toca.',
                    'Lo que dice "shift" se refiere al cambio de posición de la mano.',
                    'Hay un Fa sostenido en la izquierda.',
                    'El "l. h. over" es una instrucción para la mano derecha.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas'),
                inventa(['Tres compases de tres golpes.',
                         'Solo Do, Re, Mi, Fa y Sol.',
                         'Que el segundo compás sea de silencio entero.'],
                        time_sig=(3, 4),
                        titulo='Inventa tres compases con un silencio',
                        pista='como los de la pieza, pero tuyos · y tócalo con los dedos que escribas'),
                dibujar(['Do', 'Fa', 'La', 'Sol', 'Mi', 'Do'],
                        titulo='Dibuja tú las notas de la izquierda',
                        pista='solo el óvalo, en clave de fa'),
                para_clase('Los dos compases mudos y el primer "shift": a qué velocidad te salen y '
                           'si el bajo se te corta al entrar. Si el cruce final se te resiste, '
                           'tráelo, se arregla con el codo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
