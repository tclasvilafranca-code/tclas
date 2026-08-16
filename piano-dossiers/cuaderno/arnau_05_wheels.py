# -*- coding: utf-8 -*-
"""The Wheels on the Bus (canción 5 de Arnau, iniciación). Formato CORTO.

   Lo medido sobre el PDF de su carpeta de Drive (Sheet Music from
   www.mfiles.co.uk, arr. Jim Paterson, 1 página):

     - FA MAYOR: hay un bemol detrás de la clave, y eso quiere decir que
       todos los SI de la canción se tocan en la tecla negra de al lado. Es la
       primera pieza del cuaderno con una tecla negra.
     - Compás de 3/4: tres golpes por compás.
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
    titulo_corto='The Wheels on the Bus', time_sig=(3, 4), key_sig=FA,
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
            ('LA DERECHA', 'cuatro Fa seguidos y después sube',
             [n('F4'), n('F4'), n('F4')], AZUL, 'treble', FA),
            ('LA IZQUIERDA', 'una nota larga que ocupa el compás entero (andamio)',
             [ac(('F2', 'C3'))], OCRE, 'bass', FA),
        ],
        especial=[
            'Hay UN BEMOL detrás de la clave: todos los Si se tocan en la tecla negra.',
            'Cada compás lleva tres golpes: un-dos-tres.',
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
                texto='Marca tres golpes con el pie mientras suena: un-dos-tres, un-dos-tres.'),
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
                                  n('A4'), n('G4'), n('F4'), n('F4', 'h')],
                          bars=3),
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
                     dict(cap='a) Fa · Fa · Fa · Fa · La · las cuatro primeras son la misma tecla',
                          events=[n('F4'), n('F4'), n('F4'),
                                  n('F4'), n('A4'), n('C5')],
                          bars=2),
                     dict(cap='b) y lo que sigue · Do · La | Sol · Sol | Mi · Re · Do, bajando otra vez',
                          events=[n('C5'), n('A4'), n('G4'),
                                  n('G4'), n('E4'), n('D4'),
                                  n('C4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: tocar y dejar sonar', clef='bass',
                 pista='andamio en Fa mayor: el dibujo es el de tu partitura, las notas exactas míralas allí',
                 sistemas=[
                     dict(cap='a) una nota larga por compás · tócala en el uno y cuenta hasta tres sin '
                              'volver a apretar',
                          events=[ac(('F2', 'C3')), ac(('C3', 'G3')),
                                  ac(('F2', 'C3')), ac(('C3', 'G3'))],
                          bars=4, clef='bass'),
                     dict(cap='b) y solo la nota de abajo · Fa · Do · Fa · Do: ese es el suelo de toda '
                              'la canción, y son dos notas',
                          events=[n('F2', 'h.'), n('C3', 'h.'), n('F2', 'h.'), n('C3', 'h.')],
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

    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='The Wheels on the Bus · para hacer en casa',
            intro='Esta semana toca hacerse amigo del bemol. Todo lo de aquí está en tu partitura.',
            bloques=[
                dict(tipo='nombres', num=1,
                     titulo='¿Cómo se llama cada nota?',
                     pista='ojo: en esta canción los Si son tecla negra · escríbelos igual',
                     notas=['F4', 'A4', 'C5', 'Bb4', 'A4', 'G4', 'F4', 'C5']),
                dict(tipo='dibuja', num=2,
                     titulo='Dibuja tú las notas',
                     pista='solo el óvalo, sin el palito',
                     nombres=['Fa', 'La', 'Do', 'Si', 'La', 'Sol', 'Fa', 'La']),
                dict(tipo='figuras', num=3,
                     titulo='¿Cuántos golpes dura cada una?',
                     pista='acuérdate: aquí cada compás tiene tres golpes',
                     figuras=[('q', 'negra'), ('h', 'blanca'), ('h.', 'blanca con puntito'),
                              ('w', 'redonda')]),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas · cinco minutos bastan',
                     tareas=['Subir y bajar pasando por el Si de la tecla negra',
                             'Los cuatro Fa seguidos y la subida al La',
                             'La izquierda sola: tocar y contar hasta tres']),
                dict(tipo='colorea', num=4,
                     titulo='Rodea todos los Si',
                     pista='en esta canción todos van en la tecla negra · búscalos en tu partitura',
                     eventos=[n('F4'), n('A4'), n('Bb4'), n('A4'),
                              n('G4'), n('Bb4'), n('A4'), n('F4', 'h')],
                     leyenda=['El Si está en la tercera línea del pentagrama, en medio.',
                              'Aquí siempre se toca en la tecla negra de al lado.']),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='no hace falta que sepa música',
                     texto='Toca el Si blanco y luego el Si negro, uno detrás de otro, y pregunta cuál '
                           'suena más alegre. No hay respuesta correcta: lo que se entrena es notar que '
                           'cambia. Después toca la canción con el blanco a propósito y verás que suena '
                           'mal: eso es lo que pasa si te olvidas del bemol.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='The Wheels on the Bus · para hacer en casa',
            intro='Esta semana toca mirar la partitura con lápiz y descubrir cuánto se repite esta '
                  'canción, que es casi todo.',
            bloques=[
                dict(tipo='rodea', num=1,
                     titulo='Rodea los dos compases que son iguales',
                     pista='fíjate en las notas de una en una',
                     compases=[[n('F4'), n('F4'), n('F4')],
                               [n('A4'), n('C5'), n('A4')],
                               [n('F4'), n('F4'), n('F4')],
                               [n('G4'), n('E4'), n('C4')]]),
                dict(tipo='une', num=2,
                     titulo='Une cada cosa con lo que significa',
                     pista='una raya de un punto al otro',
                     pares=[('El bemol del principio', 'tres golpes en cada compás'),
                            ('El 3 y el 4 de la clave', 'el nombre del acorde'),
                            ('Las letras de encima', 'todos los Si, tecla negra')]),
                dict(tipo='nota',
                     etiqueta='ACUÉRDATE',
                     texto='El bemol se escribe UNA vez, al principio, y manda en toda la canción. No '
                           'es un adorno del primer compás: es una instrucción para las dos páginas. '
                           'Si algo te suena raro, mira primero si te has dejado un Si sin bemol.'),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas',
                     tareas=['Los cuatro primeros compases con las dos manos',
                             'La canción entera con la derecha sola',
                             'Contar un-dos-tres en voz alta mientras tocas']),
                dict(tipo='nombres', num=3,
                     titulo='Otra vez los nombres, a ver si ya te los sabes',
                     pista='sin mirar los deberes de la semana pasada',
                     notas=['A4', 'F4', 'C5', 'Bb4', 'G4', 'E4', 'A4', 'D4']),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='esta vez de contar hasta tres',
                     texto='Quien esté contigo cuenta un-dos-tres sin parar y tú tocas solo en el UNO. '
                           'Después probad al revés: tú cuentas y toca esa persona. Es el pulso de '
                           'esta canción, y hay que tenerlo antes de tocar las notas.'),
                dict(tipo='escribe', num=4,
                     titulo='Copia aquí el compás que más te cueste',
                     pista='cópialo tal cual y luego tócalo cinco veces',
                     lineas=1),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
