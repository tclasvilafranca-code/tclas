# -*- coding: utf-8 -*-
"""Baa Baa Black Sheep (canción 8 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (mfiles.co.uk, arr. Jim
   Paterson, 1 pagina):

     - Do mayor (nada detras de la clave) y compas de 4/4.
     - LO NUEVO: la mano derecha toca DOS COSAS A LA VEZ. Se ve a simple
       vista en la partitura: hay notas con el palito hacia arriba (la
       melodia, que se mueve) y notas con el palito hacia abajo (largas, que
       se quedan sonando). Las dos en el mismo pentagrama y con la misma mano.
     - Encima del pentagrama vienen las LETRAS de los acordes: C, F, G, C/G.
     - La mano izquierda toca notas largas: una o dos por compas.

   Lo que NO se cita nota a nota: la melodia y las notas largas van mezcladas
   en el mismo pentagrama y el lector las confunde, asi que los ejercicios de
   este dosier trabajan el GESTO (mover unos dedos y dejar otros quietos) y
   estan rotulados como andamio donde hace falta.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def d(a, b, dur='q'):
    return {'pitches': [a, b], 'dur': dur}


CANCION = dict(
    alumno='Arnau', num=8, nivel='iniciación', slug='BaaBaaBlackSheep',
    formato='corto', titulo_corto='Baa Baa Black Sheep',
    time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Baa Baa Black Sheep.pdf'),
    yt='https://www.youtube.com/results?search_query=baa+baa+black+sheep+piano',

    ficha=dict(
        titulo='Baa Baa Black Sheep',
        autor='Canción popular · arr. Jim Paterson (mfiles)',
        datos=[('Teclas', 'Solo blancas'), ('Golpes', '4 por compás'),
               ('Novedad', 'Dos a la vez'), ('Mano izq.', 'Notas largas'),
               ('Extras', 'Letras encima')],
        armonia=dict(
            titulo='Una mano tocando dos cosas',
            tarjetas=[
                ('PALITO ARRIBA', 'La melodía',
                 'Las notas que se mueven y que cantas. Las tocan los dedos de arriba.'),
                ('PALITO ABAJO', 'Las largas',
                 'Se tocan una vez y se quedan sonando debajo. Las aguanta el pulgar.'),
                ('LAS DOS', 'La misma mano',
                 'Los dos dibujos están en el mismo pentagrama: los toca la derecha.'),
                ('LAS LETRAS', 'C · F · G',
                 'Encima del pentagrama. No son notas: son el nombre del acorde.'),
            ],
            pie='Mira tu partitura y fíjate en los palitos de las notas de arriba: unos van para '
                'arriba y otros para abajo. No es un adorno del que dibujó la partitura — es la manera '
                'de decirte que ahí hay dos cosas sonando a la vez con una sola mano.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Un compás de ejemplo. Arriba, la melodía; abajo, la nota que se queda sonando.',
        ritmos=[
            ('LA MELODÍA', 'se mueve, con el palito para arriba',
             [n('C5'), n('C5'), n('G4'), n('G4')], AZUL, 'treble', None),
            ('Y DEBAJO', 'una nota larga que se queda (andamio)',
             [n('E4', 'w')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'La mano derecha toca DOS cosas: una que se mueve y otra que se queda.',
            'Las notas con el palito para abajo son las que hay que aguantar.',
            'Encima hay letras (C, F, G): son los acordes, no notas.',
            'La mano izquierda toca notas muy largas y las deja sonar.',
            'La melodía baja de una en una hasta el Do, sin saltarse ninguna.',
            'Las dos primeras notas son iguales: se repite antes de moverse.',
        ],
        reto='Aguantar una nota con un dedo mientras los otros se mueven. Lo que pasa siempre es que, '
             'al mover los dedos de arriba, el pulgar se levanta sin querer y la nota larga se corta.',
        truco='Toca la nota larga con el pulgar y CANTA esa nota en voz alta mientras mueves los otros '
              'dedos. Si dejas de oírla, es que el pulgar se te ha levantado. No hace falta que te lo '
              'diga nadie: lo oyes tú.',
        sabias='Esta canción tiene la misma melodía que el abecedario en inglés y que «Estrellita '
               'dónde estás». Son tres letras distintas encima de la misma música, y la escribió Mozart '
               'cuando ya era mayor, con doce variaciones.',
        qr=dict(titulo='Escúchala',
                texto='Escucha si por debajo de la melodía hay una nota que se queda sonando.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo de esta canción es que una sola mano hace dos cosas: unos dedos se mueven y '
              'otro se queda apretando. Se aprende por partes: primero lo que se mueve, luego lo que '
              'se queda, y al final las dos cosas juntas.',
        reglas=['EL PULGAR NO SE LEVANTA', 'PRIMERO POR SEPARADO', 'CUENTA HASTA CUATRO'],
        bloques=[
            dict(num=1, titulo='Primero, solo lo que se mueve',
                 pista='la melodía sola, sin la nota larga de debajo',
                 sistemas=[
                     dict(cap='a) la melodía del principio · dos notas iguales y baja',
                          events=[n('C5'), n('C5'), n('G4'), n('G4'),
                                  n('A4'), n('A4'), n('G4', 'h')],
                          bars=2),
                     dict(cap='b) y lo que sigue · va bajando de una en una hasta el Do',
                          events=[n('F4'), n('F4'), n('E4'), n('E4'),
                                  n('D4'), n('D4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Ahora, solo lo que se queda',
                 pista='andamio · esta es la nota que aguanta el pulgar mientras los otros se mueven',
                 sistemas=[
                     dict(cap='a) una nota larga por compás · tócala y cuenta cuatro sin levantar el dedo',
                          events=[n('E4', 'w'), n('F4', 'w'), n('E4', 'w'), n('C4', 'w')],
                          bars=4),
                     dict(cap='b) y ahora cambiando de nota larga cada dos golpes · el dedo se mueve, '
                              'pero solo cuando toca',
                          events=[n('E4', 'h'), n('F4', 'h'), n('E4', 'h'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ HAY PALITOS PARA ARRIBA Y PARA ABAJO',
                 texto='Cuando en un mismo pentagrama hay dos cosas sonando a la vez, se escriben con '
                       'los palitos en direcciones distintas para poder distinguirlas: los de arriba '
                       'son una voz y los de abajo son la otra. Así, aunque las notas estén mezcladas '
                       'en la misma línea, se ve a simple vista cuál se mueve y cuál se queda.'),
            dict(num=3, titulo='Y ahora las dos cosas juntas',
                 pista='andamio · la de abajo se toca una vez y no se suelta',
                 sistemas=[
                     dict(cap='a) muy despacio · si dejas de oír la nota de abajo, vuelve al paso 2',
                          events=[d('E4', 'C5'), d('E4', 'C5'), d('E4', 'G4'), d('E4', 'G4'),
                                  d('E4', 'A4'), d('E4', 'A4'), d('E4', 'G4', 'h')],
                          bars=2),
                 ]),
            dict(tipo='nota', etiqueta='LA PRUEBA QUE NO ENGAÑA',
                 texto='Toca el paso 3 y canta en voz alta la nota de ABAJO, no la de arriba. Si en '
                       'algún momento dejas de oírla, es que el pulgar se ha levantado. Bájalo otra vez '
                       'y repite el compás. Cuando puedas cantarla entera sin que se corte, esta '
                       'canción ya es tuya.'),
        ],
    ),

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='Baa Baa Black Sheep · para hacer en casa',
             intro='Esta semana toca aprender a mirar los palitos de las notas, que son los que te '
                   'dicen qué se mueve y qué se queda.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='escríbelas en la cajita de debajo',
                      notas=['C5', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4', 'G4']),
                 dict(tipo='colorea', num=2, titulo='Colorea las notas largas',
                      pista='las que duran cuatro golpes son las que aguanta el pulgar',
                      eventos=[n('C5'), n('E4', 'w'), n('G4'), n('A4'),
                               n('F4', 'w'), n('E4'), n('D4'), n('C4', 'w')],
                      leyenda=['La redonda dura cuatro golpes: se toca y se deja.',
                               'La negra dura uno: se toca y se levanta.']),
                 dict(tipo='figuras', num=3, titulo='¿Cuántos golpes dura cada una?',
                      pista='escribe el número en la caja',
                      figuras=[('w', 'redonda'), ('h', 'blanca'), ('q', 'negra'),
                               ('h.', 'blanca con puntito')]),
                 dict(tipo='dibuja', num=4, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Do', 'La', 'Sol', 'Fa', 'Mi', 'Re', 'Do', 'Sol']),
                 rutina('La melodía sola, los cuatro primeros compases',
                        'La nota larga sola: tocar y contar cuatro sin levantar el dedo',
                        'Las dos cosas juntas, un compás, diez veces'),
                 juego('Aprieta una tecla con el pulgar y no la sueltes. Con los otros dedos toca lo '
                       'que quieras encima. Quien esté contigo tiene que avisarte en cuanto deje de '
                       'oírse la nota del pulgar. Aguanta lo máximo que puedas.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='Baa Baa Black Sheep · para hacer en casa',
             intro='Esta semana toca mirar la partitura con lápiz y descubrir cuánto se repite.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('C5'), n('C5'), n('G4'), n('G4')],
                                [n('A4'), n('A4'), n('G4', 'h')],
                                [n('C5'), n('C5'), n('G4'), n('G4')],
                                [n('F4'), n('E4'), n('D4'), n('C4')]]),
                 dict(tipo='une', num=2, titulo='Une cada cosa con lo que quiere decir',
                      pista='una raya de un punto al otro',
                      pares=[('Palito para arriba', 'el nombre del acorde'),
                             ('Palito para abajo', 'la melodía, la que se mueve'),
                             ('Las letras de encima', 'la nota larga, la que se queda')]),
                 dict(tipo='nombres', num=3, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['G4', 'C5', 'F4', 'A4', 'E4', 'B4', 'D4', 'C5']),
                 dict(tipo='colorea', num=4, titulo='Colorea las notas que se repiten',
                      pista='en esta canción casi todas las notas salen dos veces seguidas',
                      eventos=[n('C5'), n('C5'), n('G4'), n('G4'),
                               n('A4'), n('A4'), n('G4', 'h')],
                      leyenda=['Repetir una nota es más fácil que cambiar de tecla.',
                               'Por eso esta canción se aprende tan deprisa.']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='La nota que aguanta el pulgar no se vuelve a tocar en todo el compás. Si '
                            'la repites cada vez que suena una de arriba, ya no son dos cosas: son '
                            'dieciséis golpes seguidos, y la canción deja de sonar como debe.'),
                 rutina('Los cuatro primeros compases con las dos manos',
                        'Cantar la nota de abajo mientras tocas la de arriba',
                        'La canción entera, aunque sea muy despacio'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
