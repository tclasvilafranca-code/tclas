# -*- coding: utf-8 -*-
"""The Wheels on the Bus (canción 5 de Arnau, iniciación). Formato CORTO.

   Lo medido sobre el PDF de su carpeta de Drive (Sheet Music from
   www.mfiles.co.uk, arr. Jim Paterson, 1 página):

     - FA MAYOR: hay un bemol detrás de la clave, y eso quiere decir que
       todos los SI de la canción se tocan en la tecla negra de al lado. Es la
       primera pieza del cuaderno con una tecla negra.
     - Compás de **4/4**: cuatro golpes por compás. (Esta ficha dijo durante
       meses que era 3/4, y era falso: se ha vuelto a mirar el PDF a zoom y
       detras de la armadura hay un 4 sobre un 4. Un nino de diez anos
       contando de tres una cancion que va de cuatro no puede tocarla bien.)
     - La cancion **empieza antes del compas**: una negra sola de anacrusa.
     - En el c. 1 y en el c. 5 hay una **corchea con puntillo y una
       semicorchea** (el "round and round"): es la unica figura corta de la
       pieza y es la que le da el balanceo.
     - La melodía empieza con CUATRO FA seguidos y después sube al La y al Do.
       Medido: Fa · Fa · Fa · Fa · La | Do · La | Sol · Sol | Mi · Re · Do.
     - Encima del pentagrama vienen escritas unas LETRAS (F, C, C7, B♭). No
       son notas: son el nombre del acorde que suena debajo.
     - La izquierda toca notas largas, una o dos por compás.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (rutina, juego, acuerdate, diferencias, verdadero_falso,
                         dibujar, escribir, nombres, camino, palmas, unir)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h.'):
    return {'pitches': list(ps), 'dur': d}


CANCION = dict(
    alumno='Arnau', num=5, nivel='iniciación', slug='WheelsOnTheBus',
    formato='corto',
    titulo_corto='The Wheels on the Bus', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'The Wheels on the Bus.pdf'),
    yt='https://www.youtube.com/results?search_query=wheels+on+the+bus+piano',

    ficha=dict(
        titulo='The Wheels on the Bus',
        autor='Canción popular · arr. Jim Paterson (mfiles)',
        datos=[('Novedad', 'Una tecla negra'), ('Golpes', '3 por compás'),
               ('Mano dcha.', 'La melodía'), ('Mano izq.', 'Notas largas'),
               ('Extras', 'Letras encima')],
        armonia=dict(
            titulo='Aquí aparece la primera tecla negra',
            tarjetas=[
                ('EL BEMOL', 'Todos los Si',
                 'Ese signo raro detrás de la clave manda: cada vez que veas un Si, tecla negra.'),
                ('LA MELODÍA', 'Cuatro Fa y a subir',
                 'Empieza repitiendo el Fa cuatro veces y después sube al La y al Do.'),
                ('LAS LETRAS', 'F · C · C7 · B♭',
                 'No son notas: son el nombre del acorde. Te dicen qué suena debajo.'),
                ('LA IZQUIERDA', 'Notas largas',
                 'Una o dos por compás, y se dejan sonar. No hay que correr con esa mano.'),
            ],
            pie='El bemol del principio es lo único nuevo de esta canción, y no hay que acordarse de '
                'él nota a nota: se pone una vez al principio y vale para toda la pieza. Búscalo, '
                'míralo bien, y ya no lo vuelvas a pensar.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Los primeros compases de cada mano. La de arriba repite y sube; la de abajo se '
                   'queda quieta.',
        ritmos=[
            ('LA DERECHA', 'cuatro Fa: la segunda es larga-corta',
             [n('F4'), n('F4', 'e.'), n('F4', 's'), n('F4', 'h')], AZUL, 'treble', FA),
            ('LA IZQUIERDA', 'una nota larga que ocupa el compás entero (andamio)',
             [ac(('F2', 'C3'), 'w')], OCRE, 'bass', FA),
        ],
        especial=[
            'Hay UN BEMOL detrás de la clave: todos los Si se tocan en la tecla negra.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'La canción empieza con una nota suelta, antes del primer compás entero.',
            'La melodía empieza repitiendo la misma nota cuatro veces.',
            'Encima del pentagrama hay letras (F, C, C7): son los acordes, no notas.',
            'La izquierda toca notas largas y las deja sonar.',
            'La canción se repite entera: aprendida la primera mitad, ya sabes el resto.',
        ],
        reto='Acordarse del bemol. Está escrito UNA vez, al principio, y vale para toda la canción; '
             'como no aparece delante de cada Si, es facilísimo tocar la tecla blanca sin darse cuenta. '
             'Y entonces la canción suena rara aunque el ritmo esté perfecto.',
        truco='Antes de tocar, busca el bemol del principio y toca los Si de la canción una vez, '
              'seguidos, en la tecla negra. Con eso la mano se acuerda sola. Y si en algún momento algo '
              'suena raro, lo primero que hay que mirar no es el ritmo: es si te has dejado el bemol.',
        sabias='Esta canción se inventó para cantarla en el autobús del colegio, y cada estrofa cambia '
               'una cosa: las ruedas giran, el claxon pita, los limpiaparabrisas se mueven. Por eso se '
               'repite tanto: está hecha para no acabarse nunca.',
        qr=dict(titulo='Escúchala',
                texto='Marca cuatro golpes con el pie mientras suena: un-dos-tres-cua.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende',
        esquina='Al piano · tres pasos',
        intro='Lo único nuevo de esta canción es el bemol del principio: una tecla negra que hay que '
              'recordar toda la pieza. Empieza por eso, y el resto ya lo sabes hacer.',
        reglas=['TODOS LOS SI, EN LA TECLA NEGRA', 'CUENTA UN-DOS-TRES',
                'LA IZQUIERDA SE DEJA SONAR'],
        bloques=[
            dict(num=1, titulo='Primero, la tecla negra',
                 pista='el bemol del principio vale para toda la canción, aunque no vuelva a aparecer',
                 sistemas=[
                     dict(cap='a) sube y baja pasando por el Si · tócalo despacio y mira la mano: ese '
                              'Si es la tecla negra',
                          events=[n('F4'), n('G4'), n('A4'), n('Bb4'),
                                  n('A4'), n('G4'), n('F4', 'h')],
                          bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES ESE SIGNO DEL PRINCIPIO',
                 texto='El bemol que hay justo detrás de la clave está puesto en el sitio del Si, y '
                       'quiere decir: “en esta canción, todos los Si son la tecla negra de al lado”. No '
                       'lo van a repetir delante de cada nota, así que hay que acordarse. Es una sola '
                       'cosa que recordar para la canción entera.'),
            dict(num=2, titulo='La melodía del principio',
                 pista='medida en tu partitura · cuatro notas iguales y después sube',
                 sistemas=[
                     dict(cap='a) Fa · Fa · Fa · Fa · La · las cuatro primeras son la misma tecla, y '
                              'la segunda es larga-corta: “round and RO-und”',
                          events=[n('F4'), n('F4', 'e.'), n('F4', 's'),
                                  n('F4'), n('A4')],
                          bars=1),
                     dict(cap='b) y lo que sigue · Do · La | Sol · Sol | Mi · Re · Do, bajando otra vez',
                          events=[n('C5'), n('A4'), n('F4', 'h'),
                                  n('G4'), n('G4'), n('F4', 'h'),
                                  n('E4'), n('D4'), n('C4', 'h')],
                          bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: tocar y dejar sonar', clef='bass',
                 pista='andamio en Fa mayor: el dibujo es el de tu partitura, las notas exactas míralas allí',
                 sistemas=[
                     dict(cap='a) una nota larga por compás · tócala en el uno y cuenta hasta cuatro '
                              'sin volver a apretar',
                          events=[ac(('F2', 'C3'), 'w'), ac(('C3', 'G3'), 'w'),
                                  ac(('F2', 'C3'), 'w'), ac(('C3', 'G3'), 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y solo la nota de abajo · Fa · Do · Fa · Do: ese es el suelo de toda '
                              'la canción, y son dos notas',
                          events=[n('F2', 'w'), n('C3', 'w'), n('F2', 'w'), n('C3', 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LAS LETRAS DE ENCIMA',
                 texto='Encima del pentagrama verás letras sueltas: F, C, C7, B♭. No hay que tocarlas '
                       'ni son notas: son el nombre del acorde que suena en ese compás. Sirven para que '
                       'un guitarrista pueda acompañarte sin leer el pentagrama. Tú puedes usarlas para '
                       'otra cosa: cuando la letra cambia, es que la izquierda también cambia.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R9 (diferencias · verdadero o
    # falso · dibuja · escribe) y semana 2 la R10 (nombres · camino · palmas ·
    # une).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='The Wheels on the Bus · para hacer en casa',
            intro='Primera canción con una tecla negra. Casi todos los deberes de esta semana van '
                  'de eso: de acordarse de que todos los Si se tocan en la negra de al lado.',
            bloques=[
                diferencias(
                    [n('F4'), n('F4'), n('F4'), n('F4'), n('A4'), n('C5')],
                    [n('F4'), n('F4'), n('G4'), n('F4'), n('Bb4'), n('C5', 'h')],
                    cuantas=3,
                    titulo='Busca las tres diferencias',
                    pista='el de arriba es el principio de tu canción · el de abajo tiene trampas'),
                verdadero_falso([
                    'Esta canción tiene un bemol detrás de la clave.',
                    'Eso quiere decir que todos los Si se tocan en la tecla negra.',
                    'Esta canción tiene cuatro golpes en cada compás.',
                    'Las cuatro primeras notas de la melodía son la misma tecla.',
                    'Las letras que hay encima del pentagrama son notas para tocar.',
                ], titulo='Verdadero o falso', pista='de tu canción · marca la casilla'),
                dibujar(['Fa', 'La', 'Do', 'Si♭', 'La', 'Sol', 'Fa', 'Do'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · el Si♭ se dibuja igual que el Si'),
                escribir(titulo='Copia aquí el primer compás de tu canción',
                         pista='cópialo tal cual y luego tócalo cinco veces'),
                rutina('Los cuatro Fa seguidos y el salto al La',
                       'Toda la melodía muy despacio, buscando los Si',
                       'La izquierda sola: tocar y dejar sonar'),
                acuerdate('El bemol se escribe UNA vez, al principio, y vale para toda la canción y '
                          'para todos los Si, estén arriba o abajo. No hace falta que lo pongan otra '
                          'vez en cada nota: se da por sabido.',
                          etiqueta='EL BEMOL DEL PRINCIPIO'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='The Wheels on the Bus · para hacer en casa',
            intro='Segunda semana: los nombres, un camino de teclas negras y el ritmo de unas '
                  'palabras. La partitura, al lado.',
            bloques=[
                nombres(['F4', 'A4', 'C5', 'Bb4', 'A4', 'G4', 'F4', 'C5'],
                        pista='son las notas de tu melodía · cuidado con el Si'),
                camino([['Fa', 'Si', 'Do', 'Sol', 'La', 'Re'],
                        ['La', 'Si', 'Si', 'Do', 'Fa', 'Sol'],
                        ['Do', 'Sol', 'Si', 'La', 'Re', 'Do'],
                        ['Re', 'Fa', 'Si', 'Si', 'Sol', 'La'],
                        ['Sol', 'La', 'Do', 'Si', 'Fa', 'Re']],
                       titulo='El camino de la tecla negra',
                       pista='colorea solo los Si, que son los que van en la negra'),
                palmas([('AU-TO-BUS', 3), ('RUE-DAS', 2), ('CIU-DAD', 2)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                unir([('El bemol del principio', 'no son notas: es el nombre del acorde'),
                      ('Las letras F, C, B♭ de arriba', 'cuatro golpes en cada compás'),
                      ('El 4/4 de después de la clave', 'todos los Si van en la tecla negra'),
                      ('La mano izquierda', 'toca notas largas, una o dos por compás')],
                     titulo='Une cada cosa con lo que significa',
                     pista='están desordenadas · una raya de un punto al otro'),
                rutina('La melodía entera, sin fallar ni un Si',
                       'Las dos manos, los cuatro primeros compases',
                       'Contar un-dos-tres-cua en voz alta mientras tocas'),
                juego('Quien esté contigo dice un nombre de nota y tú la buscas en el piano lo más '
                      'rápido que puedas. Si dice Si, tienes que ir a la tecla negra.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
