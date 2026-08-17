# -*- coding: utf-8 -*-
"""My Grandfather's Clock — pieza 9 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Henry Clay Work, arreglo
   de Gilbert DeBenedetti, "Level Three", 2 páginas):

     - SOL MAYOR: un sostenido detrás de la clave. Es la primera pieza del
       cuaderno con sostenido en la armadura, y quiere decir que todos los Fa
       se tocan en la tecla negra.
     - El compás se escribe con una C (que es 4/4). Pone "With precision".
     - Lleva la letra debajo del pentagrama, sílaba a sílaba, y la digitación
       impresa en las dos manos.
     - Es "Level Three": el propio arreglista la marca por encima de America y
       del himno, que eran Level Two.

   Lo que NO se cita nota a nota: la edición mezcla melodía y acompañamiento y
   la medición no sale limpia. El material va como ANDAMIO en Sol mayor y
   remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, objetivo, plan, verdadero_falso, dibujar,
                      contar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=9, nivel='iniciación',
    slug='GrandfathersClock', formato='adulto',
    titulo_corto="My Grandfather's Clock", time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           "Grandfather's Clock.pdf"),
    yt='https://www.youtube.com/results?search_query=my+grandfathers+clock+piano',

    ficha=dict(
        titulo="My Grandfather's Clock",
        autor='Henry Clay Work · arreglo de Gilbert DeBenedetti · Level Three',
        datos=[('Tonalidad', 'Sol mayor'), ('Novedad', 'Un sostenido'),
               ('Compás', 'C (4/4)'), ('Carácter', 'With precision'),
               ('Nivel', 'Level Three')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Sol mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Ojo con los Fa: en esta pieza van todos a la tecla negra.',
        armonia=dict(
            titulo='El primer sostenido, y qué cambia respecto al bemol',
            tarjetas=[
                ('EL SOSTENIDO', 'Sube medio',
                 'Un sostenido sube la nota a la tecla de al lado, hacia la derecha. El bemol de Deck '
                 'the Halls la bajaba hacia la izquierda.'),
                ('CUÁL ES', 'Todos los Fa',
                 'La armadura marca el Fa, así que todos los Fa de la pieza van a la tecla negra que '
                 'tienen a su derecha.'),
                ('LA C DEL COMPÁS', 'Es 4/4',
                 'Esa C no es de "Do": es una forma antigua de escribir cuatro por cuatro. Se cuenta '
                 'igual que siempre.'),
                ('WITH PRECISION', 'Es un reloj',
                 'La canción va de un reloj de pie, y el arreglista lo dice: se toca a tiempo exacto, '
                 'sin licencias. Es un buen sitio para el metrónomo.'),
            ],
            pie='Sol mayor y Fa mayor se parecen en la cabeza y no en la mano: una tecla negra arriba y '
                'la otra abajo. Merece la pena tocar las dos escalas seguidas alguna vez esta semana, '
                'para no mezclarlas.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, con el Fa sostenido · andamio',
             [n('G4'), n('A4'), n('B4'), n('C5')], OCRE, 'treble', SOL),
            ('MANO IZQUIERDA', 'dos notas largas por compás · andamio',
             [ac(('G2', 'D3'), 'h'), ac(('G2', 'D3'), 'h')], AZUL, 'bass', SOL),
        ],
        especial=[
            'Hay UN sostenido detrás de la clave: todos los Fa se tocan en la tecla negra.',
            'El compás se escribe con una C, que quiere decir 4/4.',
            'Pone "With precision": con precisión, a tiempo exacto.',
            'La letra va debajo del pentagrama, sílaba a sílaba.',
            'La digitación viene impresa en las dos manos.',
            'El arreglista la marca como Level Three: es un escalón por encima de las anteriores suyas.',
        ],
        reto='No confundir el sostenido con el bemol de la pieza 7. Los dos son "una tecla negra", pero '
             'una está a la derecha de la blanca y la otra a la izquierda, y la mano se lía.',
        truco='Toca la escala de Fa mayor y a continuación la de Sol mayor, dos veces cada una, antes '
              'de empezar. En la de Fa la tecla negra está bajando desde el Si; en la de Sol está '
              'subiendo desde el Fa. Si haces esto un minuto al día, la mano deja de dudar en una '
              'semana.',
        sabias='La canción es de 1876 y es la razón por la que en inglés a esos relojes altos se les '
               'llama "grandfather clocks". Antes se llamaban de otra forma: el nombre se lo puso esta '
               'canción, no al revés.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el acompañamiento va como un péndulo, sin acelerar nunca. Eso es '
                      'el "with precision".'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo de esta semana es la armadura, y lo demás ya lo sabes hacer. Dedica los dos '
              'primeros días a que la mano se aprenda dónde está el Fa sostenido, y el resto de la '
              'semana la pieza saldrá casi sola.',
        reglas=['TODOS LOS FA, EN LA TECLA NEGRA', 'A TIEMPO EXACTO, COMO UN RELOJ',
                'LA ESCALA DE SOL, TODOS LOS DÍAS'],
        bloques=[
            dict(num=1, titulo='La escala de Sol: dónde está el sostenido',
                 pista='andamio en Sol mayor · el séptimo escalón es el Fa sostenido',
                 sistemas=[
                     dict(cap='a) subiendo y bajando · la única tecla negra es la penúltima al subir',
                          events=[n('G3'), n('A3'), n('B3'), n('C4'),
                                  n('D4'), n('E4'), n('F#4'), n('G4')],
                          bars=2, key_sig=SOL),
                     dict(cap='b) y saltando al Fa sostenido desde varios sitios · para el tacto, no '
                              'para la vista',
                          events=[n('G4'), n('F#4'), n('D4'), n('F#4'),
                                  n('E4'), n('F#4'), n('G4'), n('F#4')],
                          bars=2, key_sig=SOL, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='SOSTENIDO Y BEMOL NO SON LO MISMO',
                 texto='Los dos te mandan a una tecla negra, pero por lados distintos: el sostenido '
                       'sube (la negra de la derecha) y el bemol baja (la de la izquierda). Como en la '
                       'pieza 7 tenías un bemol y aquí tienes un sostenido, la mano va a dudar los '
                       'primeros días. No es torpeza: es que son dos gestos contrarios y hay que '
                       'separarlos a propósito.'),
            dict(num=2, titulo='La melodía, con la armadura puesta',
                 pista='andamio en Sol mayor · las notas exactas están en tu partitura, con sus dedos',
                 sistemas=[
                     dict(cap='a) primero despacio, comprobando cada Fa',
                          events=[n('G4'), n('A4'), n('B4'), n('C5'),
                                  n('B4'), n('A4'), n('G4'), n('F#4')],
                          bars=2, key_sig=SOL),
                     dict(cap='b) y con el ritmo que tiene la canción · larga, corta, corta',
                          events=[n('G4', 'h'), n('A4'), n('B4'),
                                  n('C5', 'h'), n('B4'), n('G4')],
                          bars=2, key_sig=SOL, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: el péndulo', clef='bass',
                 pista='andamio · dos notas largas por compás, sin acelerar jamás',
                 sistemas=[
                     dict(cap='a) el mismo golpe dos veces por compás, como un reloj',
                          events=[ac(('G2', 'D3'), 'h'), ac(('G2', 'D3'), 'h'),
                                  ac(('C3', 'G3'), 'h'), ac(('C3', 'G3'), 'h')],
                          bars=2, clef='bass', key_sig=SOL),
                     dict(cap='b) y cambiando de acorde sin perder el paso · el péndulo no se para '
                              'porque cambie la armonía',
                          events=[ac(('G2', 'D3'), 'h'), ac(('G2', 'D3'), 'h'),
                                  ac(('D3', 'A3'), 'h'), ac(('D3', 'A3'), 'h'),
                                  ac(('G2', 'D3'), 'h'), ac(('G2', 'D3'), 'h')],
                          bars=3, clef='bass', key_sig=SOL, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="My Grandfather's Clock · para casa",
            intro='Veinte minutos al día, y el primer minuto siempre las dos escalas: Fa y Sol.',
            bloques=[
                objetivo('Que la mano vaya al Fa sostenido sola, sin pensarlo y sin mirarse. Ese es '
                         'el trabajo de la semana; la pieza es la excusa.'),
                plan((3, 'La escala de Fa y la de Sol, dos veces cada una'),
                     (5, 'Saltos al Fa sostenido desde varias notas, sin mirar'),
                     (6, 'La melodía despacio, comprobando cada Fa'),
                     (6, 'Las dos manos, cuatro compases con metrónomo')),
                verdadero_falso([
                    'Un sostenido sube la nota a la tecla negra de la derecha.',
                    'Un bemol hace lo mismo que un sostenido.',
                    'La C del compás quiere decir "Do".',
                    'En esta pieza todos los Fa van a la tecla negra.',
                    '"With precision" quiere decir que se puede ir libre de tiempo.',
                ], titulo='Verdadero o falso', pista='marca la casilla'),
                dibujar(['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa♯', 'Sol'],
                        titulo='Dibuja la escala de Sol',
                        pista='solo el óvalo · el Fa♯ se dibuja en el mismo sitio que el Fa'),
                contar([n('G4'), n('A4'), n('B4'), n('C5'), n('B4'), n('A4'), n('G4'), n('F#4')],
                       ['¿Cuántas notas hay en total?', '¿Cuántas van en tecla negra?',
                        '¿Cuál es la nota más aguda?'],
                       titulo='Mira y cuenta',
                       pista='es la escala del ejercicio 1a de la hoja de al lado'),
                para_clase('Las dos escalas seguidas, Fa y Sol, y cuatro compases de la pieza con '
                           'todos los Fa en su sitio.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
