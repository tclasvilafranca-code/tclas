# -*- coding: utf-8 -*-
"""The Mulberry Bush (canción 20 de Arnau, iniciación). A CUATRO MANOS.

   Medido sobre el PDF de su carpeta de Drive (arr. Regina Pratley, "easy
   piano duet", 3 paginas: la primera es la portada de free-scores y la musica
   empieza en la segunda).

     - Do mayor: no hay nada detras de la clave.
     - LO NUEVO: es una pieza a CUATRO MANOS. Se toca entre dos personas en el
       mismo piano: una hace la parte de arriba y la otra la de abajo. Arnau
       toca la parte de arriba, la que lleva la melodía.
     - Las alturas comprobadas de tu parte: Do · Do · Do · Do · Mi | Sol · Mi · Do · Do | Re · Re · Re · Re.

   Lo que NO se cita compas a compas: en una partitura a cuatro manos hay
   cuatro pentagramas por sistema y el lector los empareja mal, asi que se
   citan solo las alturas comprobadas y el resto va como ANDAMIO.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         diferencias, verdadero_falso, dibujar, acuerdate,
                         nombres, camino, palmas, unir)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Arnau', num=20, nivel='iniciación', slug='MulberryBush',
    formato='corto', titulo_corto='The Mulberry Bush', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'the-mulberry-bush-185807.4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=here+we+go+round+the+mulberry+bush+piano+duet',

    ficha=dict(
        titulo='The Mulberry Bush',
        autor='Canción popular · arreglo a cuatro manos de Regina Pratley',
        datos=[('Novedad', 'A cuatro manos'), ('Golpes', '4 por compás'),
               ('Tu parte', 'La de arriba'), ('Se toca', 'Entre dos'),
               ('Teclas', 'Solo blancas')],
        armonia=dict(
            titulo='Una canción para dos personas',
            tarjetas=[
                ('CUATRO MANOS', 'Dos personas',
                 'Dos pianistas en el mismo piano: cada uno toca la mitad de la música.'),
                ('TU PARTE', 'La de arriba',
                 'Llevas la melodía, en el registro agudo del piano.'),
                ('LO DIFÍCIL', 'Empezar juntos',
                 'No son las notas: es entrar los dos a la vez y no acelerar por tu cuenta.'),
                ('SI TE PIERDES', 'No pares',
                 'Sigue contando y vuelve a entrar en el compás siguiente. Parar es peor que fallar.'),
            ],
            pie='Tocar con otra persona es una cosa distinta de tocar solo, y no se aprende tocando '
                'solo. Aquí lo que se entrena no son los dedos: es escuchar a la otra persona mientras '
                'tocas, que al principio parece imposible y luego sale.',
        ),
        titulo_ritmos='Así empieza tu parte',
        pie_ritmos='Un compás de ejemplo de lo que tocas tú. La otra parte la toca la profesora.',
        ritmos=[
            ('TU MANO DERECHA', 'cuatro notas iguales y sube',
             [n('C5'), n('C5'), n('C5'), n('E5')], AZUL, 'treble', None),
            ('TU MANO IZQUIERDA', 'acompaña con notas largas (andamio)',
             [n('C3', 'h'), n('C3', 'h')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'Es a cuatro manos: se toca entre dos personas en el mismo piano.',
            'Tú tocas la parte de arriba, la que lleva la melodía; la otra parte la toca la profesora.',
            'La música empieza en la segunda página: la primera es la portada.',
            'Lo importante no es tocar rápido: es empezar y acabar los dos juntos.',
        ],
        reto='Entrar a la vez. Cuando dos personas tocan juntas, el que empieza antes arrastra al otro '
             'y la música se descoloca desde el primer compás. Y no se arregla tocando mejor: se '
             'arregla contando en voz alta antes de empezar.',
        truco='Antes de tocar, una de las dos cuenta un compás entero en voz alta y las dos empezáis en '
              'el golpe siguiente. Siempre la misma persona, y siempre a la misma velocidad. Y mientras '
              'tocáis, miraos de vez en cuando: eso es lo que hace que suene a una sola música.',
        sabias='Es una canción de corro: los niños se cogen de la mano y dan vueltas alrededor de un arbusto mientras la cantan. Es de mediados del siglo XIX y en Inglaterra dicen que la inventaron unas presas que daban vueltas al patio con sus hijos.',
        qr=dict(titulo='Escúchala',
                texto='Escúchala pensando en que son dos personas tocando a la vez.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Tu parte es fácil y la puedes aprender sola en casa. Lo que no se puede aprender solo es '
              'lo otro: entrar a la vez que otra persona, no acelerar y volver a entrar si te pierdes. '
              'Eso se trabaja en clase, las dos al piano.',
        reglas=['CUENTA UN COMPÁS ANTES DE EMPEZAR', 'SI TE PIERDES, NO PARES',
                'MIRA A LA OTRA PERSONA'],
        bloques=[
            dict(num=1, titulo='Tu parte, sola en casa',
                 pista='medido · esto es lo que tocas tú, y se aprende como cualquier otra canción',
                 sistemas=[
                     dict(cap='a) muy despacio, contando en voz alta',
                          events=[n('C5'), n('C5'), n('C5'), n('C5'), n('E5'), n('G5'), n('E5', 'h')],
                          bars=2),
                     dict(cap='b) y lo que sigue · las mismas notas, moviéndose un poco',
                          events=[n('C5'), n('C5'), n('D5'), n('D5'), n('D5'), n('D5'), n('C5', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Entrar a tiempo',
                 pista='una de las dos cuenta un compás en voz alta y las dos entran en el golpe siguiente',
                 sistemas=[
                     dict(cap='a) un compás de silencio y entras · cuéntalo todo en voz alta',
                          events=[sil('q'), sil('q'), sil('q'), sil('q'), n('C5'), n('C5'), n('C5'), n('E5')],
                          bars=2),
                     dict(cap='b) y otra vez, entrando después de dos compases · mientras esperas, '
                              'la otra parte ya está sonando',
                          events=[sil('q'), sil('q'), sil('q'), sil('q'),
                                  sil('q'), sil('q'), sil('q'), sil('q'),
                                  n('C5'), n('C5'), n('C5'), n('E5')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE EMPIEZA ENTRE DOS',
                 texto='Siempre cuenta la misma persona, en voz alta, un compás entero antes de '
                       'empezar. Y a la velocidad a la que se va a tocar, no más rápido: la cuenta es '
                       'la que decide el tempo. Si la cuenta va deprisa, la pieza va deprisa, y ya no '
                       'hay manera de arreglarlo a mitad.'),
            dict(num=3, titulo='Y si te pierdes, no pares',
                 pista='se deja de tocar un momento, se sigue contando, y se entra en el compás siguiente',
                 sistemas=[
                     dict(cap='a) toca, deja un compás sin tocar contando, y vuelve a entrar',
                          events=[n('C5'), n('C5'), n('C5'), n('E5'), sil('q'), sil('q'), sil('q'), sil('q'), n('G5'), n('E5'), n('C5', 'h')],
                          bars=3),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ NO SE PARA',
                 texto='Si tocas solo y te equivocas, puedes parar y repetir. Si tocas con otra persona, '
                       'no: mientras tú paras, esa persona sigue, y cuando vuelves ya no sabes dónde '
                       'está. Lo que se hace es dejar de tocar, seguir contando por dentro, y volver a '
                       'entrar al principio del compás siguiente. Eso hay que practicarlo a propósito.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R9 (diferencias · verdadero o
    # falso · dibuja · escribe) y semana 2 la R10 (nombres · camino · palmas ·
    # une). Es la ultima cancion del curso.
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='The Mulberry Bush · para hacer en casa',
            intro='La última del curso, y también a cuatro manos. Esta semana, tu parte en casa.',
            bloques=[
                diferencias(
                    [n('C5'), n('C5'), n('C5'), n('C5'), n('E5'), n('G5'), n('E5')],
                    [n('C5'), n('C5'), n('D5'), n('C5'), n('E5'), n('G5'), n('C5')],
                    cuantas=2,
                    titulo='Busca las dos diferencias',
                    pista='el de arriba es tu parte · en el de abajo hay dos cosas cambiadas'),
                verdadero_falso([
                    'Esta pieza se toca entre dos personas en el mismo piano.',
                    'Tú tocas la parte de abajo.',
                    'Si te pierdes, hay que parar y empezar otra vez.',
                    'Acabar juntos es tan importante como empezar juntos.',
                    'Esta pieza tiene cuatro golpes en cada compás.',
                ], titulo='Verdadero o falso', pista='de tu pieza · marca la casilla'),
                dibujar(['Do', 'Mi', 'Sol', 'Re', 'Si', 'La', 'Fa', 'Do'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · son las de tu parte, en la zona de arriba'),
                escribir(titulo='Copia aquí el compás que más te cueste',
                         pista='cópialo tal cual y luego tócalo cinco veces'),
                rutina('Tu parte, muy despacio, contando en voz alta',
                       'Tu parte entera sin parar, aunque haya fallos',
                       'Volver a entrar después de un fallo, sin pararse'),
                acuerdate('Lo difícil de una pieza a cuatro manos no son las notas: es no pararse. Si '
                          'te equivocas, sigue contando y vuelve a entrar en el compás siguiente. La '
                          'otra persona no puede esperarte.',
                          etiqueta='SI TE PIERDES, NO PARES'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='The Mulberry Bush · para hacer en casa',
            intro='Última hoja del curso. Esta semana ya se toca con otra persona.',
            bloques=[
                nombres(['C5', 'E5', 'G5', 'D5', 'B4', 'A4', 'F5', 'C5'],
                        pista='son las notas de tu parte · escríbelas debajo'),
                camino([['sigo', 'paro', 'sigo', 'sigo', 'paro', 'sigo'],
                        ['paro', 'sigo', 'sigo', 'paro', 'sigo', 'paro'],
                        ['sigo', 'paro', 'sigo', 'sigo', 'sigo', 'paro'],
                        ['paro', 'sigo', 'paro', 'paro', 'sigo', 'sigo']],
                       titulo='El camino de “no pararse”',
                       pista='colorea solo donde dice “sigo” y verás el camino que hay que hacer'),
                palmas([('MO-RE-RA', 3), ('JUN-TOS', 2), ('CON-CIER-TO', 3)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                unir([('Antes de empezar', 'seguir contando y volver a entrar'),
                      ('Si te pierdes', 'mirar a la otra persona de vez en cuando'),
                      ('Mientras tocáis', 'levantar la mano a la vez'),
                      ('La última nota', 'contar un compás en voz alta')],
                     titulo='Une cada momento con lo que hay que hacer',
                     pista='están desordenadas · una raya de un punto al otro'),
                rutina('Tu parte entera sin parar, tres veces',
                       'Contar un compás y entrar, con alguien de casa',
                       'La última nota: levantar la mano a la vez que la otra persona'),
                juego('Tocad los dos a la vez la última nota y levantad la mano en el mismo momento, '
                      'sin decir nada: solo con un gesto pequeño de la cabeza. Cinco veces. Acabar '
                      'juntos se nota tanto como empezar juntos.',
                      pista='esta vez para acabar el curso'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
