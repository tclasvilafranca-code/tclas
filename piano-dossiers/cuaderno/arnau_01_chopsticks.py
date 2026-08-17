# -*- coding: utf-8 -*-
"""Chopsticks (canción 1 de Arnau, iniciación). Formato CORTO.

   Arnau tiene 10 años y clases de media hora, así que su dosier son cinco
   hojas y no ocho: partitura · qué es esta canción · dedos y ojos · cómo se
   aprende · y dos hojas de deberes escritos, una por semana.

   Y una norma de escritura que vale para todo su cuaderno: NADA de
   tecnicismos. Aquí no se dice "segunda", "tercera" ni "intervalo": se dice
   "notas vecinas", "una nota en medio" y "las manos se separan". Cuando hace
   falta una palabra de mayores (compás, silencio, blanca) se explica en la
   misma frase donde aparece, la primera vez.

   Lo medido sobre el PDF de su carpeta de Drive (Chopsticks, arr. Gilbert
   DeBenedetti, "Level One", 1 página, 32 compases):

     - Do mayor, sin ninguna alteración, y compás de 3/4: tres golpes por
       compás de principio a fin.
     - La indicación impresa del arreglo: "Only use finger 2, both hands".
     - Al principio las dos notas son VECINAS: Fa (izquierda) y Sol (derecha).
       Medido a 200 dpi: la de abajo en el primer espacio y la de arriba en
       la segunda línea.
     - Después las manos se separan y queda un hueco de una nota en medio:
       Mi (izquierda) y Sol (derecha).
     - Más adelante el hueco se hace grande: Re y Si, y por último Do con Do,
       que son la misma nota pero una arriba y otra abajo.
     - Hay silencios a partir del c. 13 y notas largas (blancas) desde el 17.

   No se cita el resto compás a compás: el lector confunde las dos cabezas
   pegadas con una sola, así que lo que no se ha comprobado a zoom no se
   escribe.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (rutina, juego, sopa, adivinar, crucigrama, figuras,
                         nombres, colorear)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='q'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


# las cuatro parejas de notas que salen en la pieza, de menos a mas abiertas
VECINAS = ('F4', 'G4')      # cc. 1-8   · una al lado de la otra
HUECO = ('E4', 'G4')        # despues   · queda una nota en medio
ANCHA = ('D4', 'B4')        # mas tarde · el hueco ya es grande
OCTAVA = ('C4', 'C5')       # la misma nota, arriba y abajo

CANCION = dict(
    alumno='Arnau', num=1, nivel='iniciación', slug='Chopsticks',
    formato='corto',
    titulo_corto='Chopsticks', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Chopsticks.pdf'),
    yt='https://www.youtube.com/results?search_query=chopsticks+piano',

    ficha=dict(
        titulo='Chopsticks',
        autor='Canción popular · arreglo de Gilbert DeBenedetti',
        datos=[('Teclas', 'Solo blancas'), ('Golpes por compás', '3'),
               ('Dedos', 'Solo el 2'),
               ('Compases', '32'), ('Cómo suena', 'A palillos chinos')],
        titulo_ritmos='Así suena un compás',
        pie_ritmos='Un compás de ejemplo, para ver de un vistazo qué tienes que tocar. La nota de '
                   'abajo es la mano izquierda y la de arriba, la derecha.',
        armonia=dict(
            titulo='Toda la canción son DOS notas a la vez',
            tarjetas=[
                ('AL PRINCIPIO', 'Fa y Sol',
                 'Dos notas vecinas, una pegada a la otra. La de abajo con la mano izquierda.'),
                ('DESPUÉS', 'Mi y Sol',
                 'Las manos se separan un poquito: entre las dos queda una nota sin tocar.'),
                ('MÁS TARDE', 'Re y Si',
                 'El hueco se hace grande. Las manos ya están lejos una de otra.'),
                ('AL FINAL', 'Do y Do',
                 'La misma nota dos veces: una abajo y otra arriba. Suena igual pero más gorda.'),
            ],
            pie='Fíjate en lo que pasa de principio a fin: las dos manos empiezan juntitas y se van '
                'separando poco a poco. Esa es la canción entera. Si te aprendes por dónde va cada '
                'mano, las notas se aprenden solas.',
        ),
        ritmos=[
            ('LAS DOS MANOS', 'suenan a la vez, tres veces por compás',
             [ac(VECINAS), ac(VECINAS), ac(VECINAS)], OCRE, 'treble', None),
            ('Y MÁS TARDE', 'lo mismo, con las manos ya separadas',
             [ac(HUECO), ac(HUECO), ac(HUECO)], AZUL, 'treble', None),
        ],
        especial=[
            'No hay ninguna nota rara: ni sostenidos ni bemoles. Todo teclas blancas.',
            'Se toca SOLO con el dedo 2 de cada mano (el índice). Lo pone el arreglo.',
            'Cada compás lleva tres golpes: un-dos-tres, un-dos-tres.',
            'Las dos manos tocan siempre a la vez, nunca una detrás de otra.',
            'A partir del compás 13 aparecen silencios: momentos en los que no se toca nada.',
            'Desde el compás 17 hay notas largas, que duran el doble.',
        ],
        reto='Que las dos manos bajen A LA VEZ. Como cada mano toca una nota distinta, es muy fácil '
             'que una llegue un pelín antes que la otra, y entonces en vez de un golpe se oyen dos.',
        truco='Cuenta en voz alta “un, dos, tres” y baja las dos manos como si fueran una sola pieza, '
              'igual que cuando aplaudes. Si oyes dos ruiditos seguidos en vez de uno, para y hazlo '
              'más despacio hasta que suene un solo golpe.',
        sabias='En inglés “chopsticks” son los palillos de comer chino, y la canción se llama así '
               'porque se toca con los dedos tiesos, como si fueran dos palillos. En realidad la '
               'escribió una chica de 16 años en 1877 y le puso otro nombre: “El vals de la chuleta”.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cómo las dos manos se van separando poco a poco.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende',
        esquina='Al piano · tres pasos',
        intro='Esta canción tiene tres pasos y ya está. Lo único que cambia de principio a fin es lo '
              'lejos que están tus dos manos, así que aprende primero las parejas de notas y luego '
              'ponles el ritmo.',
        reglas=['SOLO EL DEDO 2 DE CADA MANO', 'LAS DOS MANOS, A LA VEZ', 'CUENTA UN-DOS-TRES'],
        bloques=[
            dict(num=1, titulo='Las dos notas del principio: Fa y Sol',
                 pista='compases 1 al 8 · la de abajo es la izquierda y la de arriba la derecha',
                 sistemas=[
                     dict(cap='a) primero una sola vez, muy despacio · las dos manos bajan juntas, '
                              'como cuando aplaudes',
                          events=[ac(VECINAS, 'h.'), ac(VECINAS, 'h.')], bars=2),
                     dict(cap='b) y ahora tres golpes en cada compás, que es como está escrito',
                          events=[ac(VECINAS)] * 12, bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SABER SI LO ESTÁS HACIENDO BIEN',
                 texto='Cierra los ojos y toca un golpe. Tienes que oír UN ruido, no dos. Si oyes dos '
                       'seguiditos es que una mano ha llegado antes que la otra; no pasa nada, pero '
                       'hazlo más despacio hasta que suene uno solo. Cuando te salga cinco veces '
                       'seguidas, ya puedes ir un poquito más rápido.'),
            dict(num=2, titulo='Y ahora las manos se separan',
                 pista='las tres parejas que salen después · la mano no cambia de dedo, solo de sitio',
                 sistemas=[
                     dict(cap='a) Mi y Sol · entre las dos notas queda una sin tocar',
                          events=[ac(HUECO)] * 6, bars=2),
                     dict(cap='b) Re y Si · el hueco ya es grande: mira el teclado antes de bajar',
                          events=[ac(ANCHA)] * 6, bars=2, show_time=False),
                     dict(cap='c) Do y Do · es la misma nota, una abajo y otra arriba',
                          events=[ac(OCTAVA)] * 6, bars=2, show_time=False),
                     dict(cap='d) y las cuatro seguidas · aquí se ve de un vistazo cómo se van '
                              'abriendo las manos de principio a fin',
                          events=[ac(VECINAS, 'h.'), ac(HUECO, 'h.'),
                                  ac(ANCHA, 'h.'), ac(OCTAVA, 'h.')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LO QUE VIENE DESPUÉS',
                 texto='A partir del compás 13 hay SILENCIOS: ratos en los que no tocas nada pero sigues '
                       'contando un-dos-tres por dentro. Y desde el compás 17 salen notas más largas, '
                       'que valen dos golpes en vez de uno. Búscalas en tu partitura con el lápiz y '
                       'rodéalas antes de tocar.'),
        ],
    ),

    # Los deberes siguen el reparto de `arnau_recetas`: semana 1 la receta R1
    # (sopa · figuras · adivina) y semana 2 la R2 (crucigrama · nombres ·
    # colorea). Los numeros de ejercicio los pone `hoja_deberes` solo.
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Chopsticks · para hacer en casa',
            intro='Esta semana toca jugar un poco. Todo lo que sale aquí está en tu partitura, así '
                  'que puedes mirarla siempre que quieras: no es un examen.',
            bloques=[
                sopa(['PALILLOS', 'SILENCIO', 'BLANCA', 'NEGRA', 'COMPAS', 'DEDO',
                      'VECINAS', 'SOL', 'FA', 'MI'], semilla=101, filas=8,
                     titulo='Sopa de letras de tu canción',
                     pista='diez palabras · tumbadas, de pie o en diagonal'),
                figuras([('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                         ('h.', 'blanca con puntito')],
                        pista='acuérdate: la negra dura un golpe'),
                adivinar([('Solo se usa uno de los diez, el segundo de cada mano.', 'DEDO'),
                          ('No suenas cuando me ves, pero hay que contarme igual.', 'SILENCIO'),
                          ('Somos dos y bajamos siempre a la vez, nunca una detrás.', 'MANOS')]),
                rutina('Fa y Sol juntas, veinte veces, contando un-dos-tres',
                       'Los compases 1 al 4 seguidos, muy despacio',
                       'Buscar en la partitura dónde se separan las manos'),
                juego('Tú tocas dos notas a la vez y quien esté contigo dice si han sonado A LA '
                      'VEZ o una detrás de otra. Cinco veces. Luego cambiad: toca esa persona con '
                      'un dedo de cada mano y adivinas tú.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Chopsticks · para hacer en casa',
            intro='Esta semana hay crucigrama, y después toca mirar la partitura de verdad. Coge un '
                  'lápiz blando, que se pueda borrar.',
            bloques=[
                crucigrama('COMPAS', [
                    ('SILENCIO', 5, 'Cuando no se toca nada, pero el tiempo sigue pasando.'),
                    ('SOL', 1, 'La nota que toca tu mano derecha al principio de la canción.'),
                    ('MANOS', 0, 'Tienes dos, y en esta canción bajan siempre a la vez.'),
                    ('PIANO', 0, 'El instrumento que estás aprendiendo.'),
                    ('NEGRA', 4, 'La figura que dura un golpe y tiene el óvalo pintado.'),
                    ('TRES', 3, 'Los golpes que hay en cada compás de esta canción.'),
                ], cierre='Las casillas grises dicen cómo se llama el trozo que hay entre dos rayas.'),
                nombres(['F4', 'G4', 'E4', 'G4', 'B4', 'C5', 'A4', 'G4'],
                        pista='son las notas de tu canción · escríbelas en la cajita de debajo'),
                colorear([n('G4'), n('F4', 'h'), n('G4'), n('E4'),
                          n('G4', 'h'), n('F4'), n('G4'), n('E4', 'h')],
                         ['Óvalo pintado, un golpe. Óvalo hueco, dos golpes.'],
                         pista='las cortas de un color y las largas de otro'),
                rutina('Las cuatro parejas de notas, una detrás de otra',
                       'Los compases 1 al 8 seguidos y sin parar',
                       'Contar un-dos-tres en voz alta mientras tocas'),
                juego('Toca tres golpes seguidos y luego dos, sin decir cuántos, y quien esté '
                      'contigo adivina el número. Cinco veces cada uno.',
                      pista='esta vez de contar'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
