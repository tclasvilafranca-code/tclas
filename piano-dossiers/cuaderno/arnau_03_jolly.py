# -*- coding: utf-8 -*-
"""Jolly Old Saint Nicholas (canción 3 de Arnau, iniciación). Formato CORTO.

   Lo medido sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "Level One", 1 página):

     - Do mayor (nada detrás de la clave) y compás de 4/4. Pone "Happily".
     - La melodía empieza con CUATRO NOTAS IGUALES seguidas —"Jol-ly old
       Saint"—, comprobado a zoom: las cuatro cabezas están a la misma altura.
       Después baja dos escalones y se para en una nota larga.
     - La mano izquierda toca DOS NOTAS A LA VEZ y muy largas: una por compás.
       La digitación viene impresa, 1 y 5, así que son los dedos de los
       extremos y la mano no se mueve de sitio dentro del compás.
     - Es la primera pieza del cuaderno con notas de cuatro golpes (redondas).

   Lo que NO se cita: las alturas exactas de la izquierda. Se leen como dos
   cabezas juntas y no las he podido medir con seguridad, así que sus
   ejercicios van rotulados como ANDAMIO y remiten a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='w'):
    return {'pitches': list(ps), 'dur': d}


CANCION = dict(
    alumno='Arnau', num=3, nivel='iniciación', slug='JollySaintNicholas',
    formato='corto',
    titulo_corto='Jolly Old Saint Nicholas', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'JOLLY OLD SAINT NICHOLAS.pdf'),
    yt='https://www.youtube.com/results?search_query=jolly+old+saint+nicholas+piano',

    ficha=dict(
        titulo='Jolly Old Saint Nicholas',
        autor='Villancico popular · arreglo de Gilbert DeBenedetti',
        datos=[('Teclas', 'Solo blancas'), ('Golpes', '4 por compás'),
               ('Mano dcha.', 'La melodía'), ('Mano izq.', 'Dos notas largas'),
               ('Dedos izq.', '1 y 5')],
        armonia=dict(
            titulo='Una mano corre y la otra aguanta',
            tarjetas=[
                ('LA DERECHA', 'Cuatro iguales',
                 'Empieza con cuatro notas seguidas en el mismo sitio: “Jol-ly old Saint”.'),
                ('LA IZQUIERDA', 'Dos a la vez',
                 'Toca dos notas juntas y muy largas: una sola vez en cada compás.'),
                ('LOS DEDOS', '1 y 5',
                 'Vienen escritos: el pulgar y el meñique. Los de en medio no tocan nada.'),
                ('LA REDONDA', 'Cuatro golpes',
                 'La nota más larga del cuaderno hasta ahora. Se toca una vez y se deja sonar.'),
            ],
            pie='Aquí cada mano hace un trabajo distinto por primera vez: una se mueve y la otra se '
                'queda quieta aguantando. Suena difícil, pero es más fácil que las dos moviéndose, '
                'porque la izquierda solo tiene que acordarse de NO volver a tocar.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás de cada mano. Fíjate en que la de arriba toca cuatro veces y la '
                   'de abajo, una sola.',
        ritmos=[
            ('LA DERECHA', 'cuatro notas iguales, una por golpe',
             [n('E4'), n('E4'), n('E4'), n('E4')], AZUL, 'treble', None),
            ('LA IZQUIERDA', 'dos notas juntas, todo el compás (andamio)',
             [ac(('C3', 'G3'))], OCRE, 'bass', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'La melodía empieza con cuatro notas iguales seguidas.',
            'La izquierda toca dos notas a la vez, con el pulgar y el meñique.',
            'Las notas de la izquierda duran el compás entero: se tocan una vez y ya.',
            'Pone «Happily», que quiere decir alegre: no la toques triste.',
        ],
        reto='Que la izquierda no vuelva a tocar. Cuando una mano se está moviendo, la otra quiere '
             'moverse también, y sin darte cuenta acabas repitiendo la nota larga cada vez que la '
             'derecha toca. Aguantar sin hacer nada cuesta más de lo que parece.',
        truco='Toca la nota larga de la izquierda y quédate mirando la mano: no la levantes, no la '
              'aprietes, solo déjala puesta. Cuenta cuatro golpes en voz alta antes de cambiarla. Si '
              'te sale eso, ya tienes la mitad de la canción.',
        sabias='Este villancico es de 1865 y la letra es un niño contándole a Papá Noel, en secreto, '
               'qué quiere que le traiga. Por eso dice «acércame la oreja» al principio: se supone que '
               'lo está diciendo bajito para que nadie más lo oiga.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántas veces toca la mano de abajo en cada compás. Solo una.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende',
        esquina='Al piano · tres pasos',
        intro='Lo nuevo de esta canción no son las notas: es que cada mano hace una cosa distinta. '
              'Así que primero cada una por su lado, y solo cuando las dos salgan solas, juntas.',
        reglas=['LA IZQUIERDA SE QUEDA QUIETA', 'CUENTA HASTA CUATRO EN VOZ ALTA',
                'PRIMERO CADA MANO POR SU LADO'],
        bloques=[
            dict(num=1, titulo='La derecha: cuatro notas iguales',
                 pista='“Jol-ly old Saint” · las cuatro en el mismo sitio, medidas en tu partitura',
                 sistemas=[
                     dict(cap='a) cuatro golpes iguales, sin acelerar · cuenta un-dos-tres-cuatro',
                          events=[n('E4'), n('E4'), n('E4'), n('E4'),
                                  n('E4'), n('E4'), n('E4'), n('E4')],
                          bars=2),
                     dict(cap='b) y ahora bajando, que es lo que hace después · dos escalones y se para',
                          events=[n('E4'), n('E4'), n('E4'), n('E4'),
                                  n('D4'), n('D4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: tocar una vez y no hacer nada más', clef='bass',
                 pista='andamio en Do mayor: mira en tu partitura cuáles son exactamente las dos notas',
                 sistemas=[
                     dict(cap='a) dos notas juntas que duran los cuatro golpes · tócalas y cuenta hasta '
                              'cuatro sin levantar los dedos',
                          events=[ac(('C3', 'G3')), ac(('C3', 'G3')),
                                  ac(('B2', 'G3')), ac(('C3', 'G3'))],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL DEDO 1 Y EL DEDO 5',
                 texto='En tu partitura hay un 1 y un 5 escritos debajo de las notas de la izquierda: '
                       'son el pulgar y el meñique, los dedos de los extremos. Colócalos y deja los '
                       'tres de en medio apoyados encima de las teclas sin apretar. Así la mano no se '
                       'cansa y no tienes que buscar nada cuando cambia el acorde.'),
            dict(num=3, titulo='Y ahora las dos manos',
                 pista='muy despacio · la derecha toca cuatro veces y la izquierda solo una',
                 sistemas=[
                     dict(cap='a) esto es lo que hace la derecha mientras la izquierda aguanta · toca '
                              'primero solo esto y cuenta en voz alta',
                          events=[n('E4'), n('E4'), n('E4'), n('E4'),
                                  n('D4'), n('D4'), n('C4', 'h'),
                                  n('E4', 'w')],
                          bars=3),
                     dict(cap='b) y esto es lo que hace la izquierda a la vez (andamio) · una sola vez '
                              'por compás, en el primer golpe',
                          events=[ac(('C3', 'G3')), ac(('B2', 'G3')), ac(('C3', 'G3'))],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE JUNTAN LAS DOS MANOS',
                 texto='Las dos manos tocan a la vez SOLO en el primer golpe de cada compás. En el dos, '
                       'el tres y el cuatro, la izquierda ya no hace nada. Así que no tienes que '
                       'coordinar cuatro cosas: solo tienes que acertar la primera, y después dejar la '
                       'izquierda tranquila.'),
        ],
    ),

    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Jolly Old Saint Nicholas · para hacer en casa',
            intro='Esta semana toca aprender la nota más larga de todas y contar hasta cuatro sin '
                  'perderse. Todo lo de aquí está en tu partitura.',
            bloques=[
                dict(tipo='figuras', num=1,
                     titulo='¿Cuántos golpes dura cada una?',
                     pista='escribe el número en la caja · la redonda es la más larga de todas',
                     figuras=[('w', 'redonda'), ('h', 'blanca'), ('q', 'negra'),
                              ('h.', 'blanca con puntito')]),
                dict(tipo='nombres', num=2,
                     titulo='¿Cómo se llama cada nota?',
                     pista='escríbelas en la cajita de debajo',
                     notas=['E4', 'D4', 'C4', 'E4', 'G4', 'F4', 'E4', 'D4']),
                dict(tipo='dibuja', num=3,
                     titulo='Dibuja tú las notas',
                     pista='solo el óvalo, sin el palito',
                     nombres=['Do', 'Mi', 'Sol', 'Mi', 'Fa', 'Re', 'Sol', 'Do']),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas · cinco minutos bastan',
                     tareas=['Las cuatro notas iguales, contando un-dos-tres-cuatro',
                             'La izquierda sola: tocar una vez y aguantar cuatro golpes',
                             'Los dos primeros compases con las dos manos, muy despacio']),
                dict(tipo='colorea', num=4,
                     titulo='Colorea las redondas de un color y las negras de otro',
                     pista='la redonda es hueca y no lleva palito',
                     eventos=[n('E4'), n('E4'), n('C4', 'w'), n('D4'),
                              n('G4', 'w'), n('E4'), n('F4'), n('C4', 'w')],
                     leyenda=['La redonda dura cuatro golpes y no tiene palito.',
                              'La negra dura un golpe y tiene el óvalo pintado.']),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='no hace falta que sepa música',
                     texto='Toca una nota y déjala sonar mientras contáis los dos en voz alta hasta '
                           'que deje de oírse. Probad en varias partes del piano: las notas graves '
                           'duran mucho más que las agudas. Es un juego, pero también es la razón por '
                           'la que la izquierda de esta canción puede aguantar cuatro golpes.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Jolly Old Saint Nicholas · para hacer en casa',
            intro='Esta semana toca mirar la partitura con un lápiz en la mano y darse cuenta de que '
                  'la izquierda repite mucho.',
            bloques=[
                dict(tipo='rodea', num=1,
                     titulo='Rodea los dos compases que son iguales',
                     pista='fíjate en las notas de una en una',
                     compases=[[n('E4'), n('E4'), n('E4'), n('E4')],
                               [n('D4'), n('D4'), n('C4', 'h')],
                               [n('E4'), n('E4'), n('E4'), n('E4')],
                               [n('G4'), n('E4'), n('C4', 'h')]]),
                dict(tipo='une', num=2,
                     titulo='Une cada figura con lo que dura',
                     pista='una raya de un punto al otro',
                     pares=[('Redonda', 'dos golpes'),
                            ('Blanca', 'un golpe'),
                            ('Negra', 'cuatro golpes')]),
                dict(tipo='nota',
                     etiqueta='ACUÉRDATE',
                     texto='Cuando una nota dura cuatro golpes no hay que volver a apretarla: se toca '
                           'una vez y el piano sigue sonando solo. Apretar más fuerte no hace que dure '
                           'más; lo único que hace es cansarte la mano.'),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas',
                     tareas=['Los cuatro primeros compases con las dos manos',
                             'La canción entera con la derecha sola',
                             'Contar hasta cuatro en voz alta mientras tocas']),
                dict(tipo='nombres', num=3,
                     titulo='Otra vez los nombres, a ver si ya te los sabes',
                     pista='sin mirar los deberes de la semana pasada',
                     notas=['G4', 'F4', 'E4', 'A4', 'C5', 'B4', 'D5', 'G4']),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='esta vez de contar',
                     texto='Toca un acorde de dos notas y cuenta en voz alta hasta cuatro sin volver '
                           'a tocarlo. Quien esté contigo comprueba que no has vuelto a apretar. Cinco '
                           'veces. Es exactamente lo que tiene que hacer tu mano izquierda en toda '
                           'esta canción.'),
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
