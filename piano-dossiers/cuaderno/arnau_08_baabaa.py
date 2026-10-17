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
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         sopa, diferencias, acuerdate, verdadero_falso, ordenar,
                         figuras, dibujar)

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

    # Reparto de `arnau_recetas`: semana 1 la R15 (sopa · diferencias) y semana
    # 2 la R16 (verdadero o falso · ordena · figuras · dibuja).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Baa Baa Black Sheep · para hacer en casa',
            intro='Lo nuevo de esta canción: una sola mano toca dos cosas a la vez. Se ve en la '
                  'partitura porque hay palitos hacia arriba y palitos hacia abajo.',
            bloques=[
                sopa(['OVEJA', 'PALITOS', 'ARRIBA', 'ABAJO', 'LARGAS', 'ACORDE',
                      'MELODIA', 'SOL', 'FA', 'DO'], semilla=808, filas=8,
                     titulo='Sopa de letras de tu canción',
                     pista='diez palabras · tumbadas, de pie o en diagonal'),
                diferencias(
                    [n('C5'), n('C5'), n('G4'), n('G4'), n('F4'), n('F4'), n('E4', 'h')],
                    [n('C5'), n('C5'), n('A4'), n('G4'), n('F4'), n('G4'), n('E4')],
                    cuantas=3,
                    titulo='Busca las tres diferencias',
                    pista='el de arriba es el principio de tu melodía · el de abajo tiene trampas'),
                acuerdate('Cuando en el mismo pentagrama hay notas con el palito hacia arriba y '
                          'notas con el palito hacia abajo, quiere decir que suenan a la vez y las '
                          'toca la misma mano. Las de arriba se mueven (son la melodía) y las de '
                          'abajo se quedan quietas sonando. El truco es mover unos dedos y dejar '
                          'los otros apoyados sin levantarlos.',
                          etiqueta='PALITOS ARRIBA Y PALITOS ABAJO'),
                rutina('Solo la melodía, con los dedos de arriba',
                       'Solo las notas largas, dejándolas sonar cuatro golpes',
                       'Las dos cosas a la vez, dos compases'),
                juego('Apoya la mano derecha en el piano y aprieta solo el pulgar diez veces sin '
                      'mover los demás. Luego solo el meñique. Quien esté contigo mira si se te '
                      'levanta algún otro dedo.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Baa Baa Black Sheep · para hacer en casa',
            intro='Esta semana hay preguntas, pasos que ordenar y notas que dibujar.',
            bloques=[
                verdadero_falso([
                    'En esta canción una mano toca dos cosas a la vez.',
                    'Las notas con el palito hacia abajo son las que se mueven.',
                    'Las letras C, F y G de arriba son el nombre del acorde.',
                    'Esta canción tiene cuatro golpes en cada compás.',
                    'La mano izquierda toca notas largas.',
                ], titulo='Verdadero o falso', pista='de tu canción · marca la casilla'),
                ordenar(['Las dos cosas a la vez, muy despacio.',
                         'Solo las notas largas, contando cuatro.',
                         'Solo la melodía, con los dedos de arriba.',
                         'Añadir la mano izquierda.'],
                        titulo='Pon los pasos en el orden bueno',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                figuras([('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                         ('e', 'corchea')],
                        titulo='¿Cuántos golpes dura cada una?',
                        pista='la corchea es la mitad de una negra'),
                dibujar(['Do', 'Sol', 'Fa', 'Mi', 'Re', 'Do', 'La', 'Sol'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · debajo pone cuál va en cada sitio'),
                rutina('La melodía entera con la derecha sola',
                       'Las dos cosas a la vez, cuatro compases',
                       'Las dos manos, sin parar aunque haya fallos'),
                acuerdate('Las letras que hay encima del pentagrama (C, F, G, C/G) no son notas '
                          'para tocar: son el nombre del acorde que suena debajo. Sirven para que '
                          'alguien pueda acompañarte con una guitarra.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
