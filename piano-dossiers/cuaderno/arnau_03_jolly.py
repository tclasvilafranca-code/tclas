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
from arnau_comun import (rutina, juego, acuerdate, camino, nombres, inventa,
                         unir, sopa, ordenar, colorear)

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

    # Reparto de `arnau_recetas`: semana 1 la R5 (camino · nombres · inventa ·
    # une) y semana 2 la R6 (sopa · ordena · colorea).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Jolly Old Saint Nicholas · para hacer en casa',
            intro='Esta canción trae las notas más largas que has tocado hasta ahora: las que duran '
                  'cuatro golpes. Los deberes de esta semana van casi todos de eso.',
            bloques=[
                camino([['negra', 'redonda', 'negra', 'negra', 'blanca', 'negra'],
                        ['blanca', 'redonda', 'redonda', 'negra', 'negra', 'negra'],
                        ['negra', 'negra', 'redonda', 'blanca', 'negra', 'blanca'],
                        ['negra', 'blanca', 'redonda', 'redonda', 'negra', 'negra'],
                        ['negra', 'negra', 'negra', 'redonda', 'blanca', 'negra']],
                       titulo='El camino de las notas largas',
                       pista='colorea solo las que duran cuatro golpes y sale un camino'),
                nombres(['E4', 'D4', 'C4', 'E4', 'G4', 'F4', 'E4', 'D4'],
                        pista='son las notas de tu melodía · escríbelas debajo'),
                inventa(['Solo Mi, Re y Do, que son las de tu melodía.',
                         'Dos compases de cuatro golpes cada uno.',
                         'Que una de las notas sea una redonda.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases',
                        pista='tiene que cumplir las tres cosas'),
                unir([('Negra', 'cuatro golpes'),
                      ('Blanca', 'un golpe'),
                      ('Redonda', 'tres golpes'),
                      ('Blanca con puntito', 'dos golpes')],
                     titulo='Une cada figura con lo que dura',
                     pista='ojo, están desordenadas'),
                rutina('Las cuatro notas iguales del principio, contando cuatro',
                       'La izquierda sola: tocar y aguantar cuatro golpes',
                       'Las dos manos, los dos primeros compases'),
                juego('Tú tocas una nota y la aguantas, y quien esté contigo cuenta en voz alta '
                      'hasta que deje de sonar. Tiene que llegar a cuatro. Cinco veces.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Jolly Old Saint Nicholas · para hacer en casa',
            intro='Villancico y sopa de letras. Después, a ordenar los pasos de estudiar, que es lo '
                  'que hay que hacer con todas las canciones.',
            bloques=[
                sopa(['REDONDA', 'NAVIDAD', 'CUATRO', 'LARGAS', 'PULGAR', 'MENIQUE',
                      'IGUALES', 'MI', 'RE', 'DO'], semilla=303, filas=8,
                     titulo='Sopa de letras de Navidad',
                     pista='diez palabras · algunas están en diagonal'),
                ordenar(['Tocarla entera despacio, sin pararse.',
                         'Mirar la partitura y decir los nombres en voz alta.',
                         'Tocar solo la mano derecha.',
                         'Juntar las dos manos, dos compases.'],
                        titulo='Pon los pasos en el orden bueno',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                colorear([n('E4'), n('E4'), n('E4'), n('E4'),
                          n('D4', 'h'), n('C4', 'w'), n('E4'), n('E4')],
                         ['Un color para las de un golpe, otro para las de dos y otro para la de '
                          'cuatro.'],
                         titulo='Colorea según lo que duran',
                         pista='tres colores, uno por figura'),
                rutina('El villancico entero, muy despacio',
                       'La izquierda, sin mirarse la mano',
                       'Contar cuatro en voz alta mientras tocas'),
                acuerdate('Los dedos 1 y 5 son el pulgar y el meñique, los de los extremos. En tu '
                          'partitura vienen escritos debajo de las notas de la izquierda. Colócalos '
                          'y deja los tres de en medio apoyados sin apretar: así la mano no se '
                          'cansa y no tienes que buscar nada.',
                          etiqueta='EL 1 Y EL 5'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
