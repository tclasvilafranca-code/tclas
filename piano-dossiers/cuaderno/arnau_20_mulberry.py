# -*- coding: utf-8 -*-
"""The Mulberry Bush (canción 20 de Arnau, iniciación). A CUATRO MANOS.

   Medido sobre el PDF de su carpeta de Drive (arr. Regina Pratley, "easy
   piano duet", 3 paginas: la primera es la portada de free-scores y la musica
   empieza en la segunda).

     - Do mayor: no hay nada detras de la clave.
     - COMPAS DE 6/8, leido en la partitura (el 6 y el 8 detras de la clave).
       Durante meses este dosier decia 4/4 y hablaba de "cuatro golpes por
       compas": era falso, y lo caro de un compas mal puesto es que el alumno
       cuenta mal la pieza entera. Arnau ya vio el 6/8 en Little Miss Muffet
       (cancion 10), asi que aqui no es material nuevo.
     - LO NUEVO: es una pieza a CUATRO MANOS. Se toca entre dos personas en el
       mismo piano: una hace la parte de arriba y la otra la de abajo. Arnau
       toca la parte de arriba, la que lleva la melodía.
     - Los dos pentagramas de Arnau (Primo) van los DOS en clave de sol.
     - Medido nota a nota sobre el PDF a 300 ppp (alturas por posicion en el
       pentagrama, duraciones por corchete y puntillo):
         c. 1  Do5 Do5 Do5 (unidas de tres) · Do5 negra · Mi5 corchea
         c. 2  Sol5 negra · Mi5 corchea · Do5 negra · Do5 corchea
         c. 3  Re5 negra · Re5 corchea · Re5 negra · Re5 corchea
         c. 4  la derecha CALLA · contesta la izquierda: Si4 negra · La4
               corchea · Sol4 negra con puntillo
         cc. 5-6 repiten los cc. 1-2
         c. 7  Re5 negra · Re5 corchea · silencio de negra con puntillo
         c. 8  la derecha calla · la izquierda: Do5 y Do5, negras con puntillo

   Lo que NO se cita compas a compas: nada de la parte del Secondo (la de la
   profesora), que no toca Arnau.
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


def _c1():
    """El compas 1 de la derecha, medido: tres corcheas unidas, negra, corchea."""
    return corch(['C5', 'C5', 'C5'], 3) + [n('C5'), n('E5', 'e')]


def _c2():
    """El compas 2, medido: Sol negra, Mi corchea, Do negra, Do corchea."""
    return [n('G5'), n('E5', 'e'), n('C5'), n('C5', 'e')]


def _c3():
    """El compas 3, medido: cuatro Re, negra-corchea dos veces."""
    return [n('D5'), n('D5', 'e'), n('D5'), n('D5', 'e')]


CANCION = dict(
    alumno='Arnau', num=20, nivel='iniciación', slug='MulberryBush',
    formato='corto', titulo_corto='The Mulberry Bush', time_sig=(6, 8), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'the-mulberry-bush-185807.4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=here+we+go+round+the+mulberry+bush+piano+duet',

    ficha=dict(
        titulo='The Mulberry Bush',
        autor='Canción popular · arreglo a cuatro manos de Regina Pratley',
        datos=[('Novedad', 'A cuatro manos'), ('Compás', '6/8, en dos'),
               ('Tu parte', 'La de arriba'), ('Se toca', 'Entre dos'),
               ('Teclas', 'Solo blancas')],
        armonia=dict(
            titulo='Una canción para dos personas',
            tarjetas=[
                ('CUATRO MANOS', 'Dos personas',
                 'Dos pianistas en el mismo piano: cada uno toca la mitad de la música.'),
                ('TU PARTE', 'La de arriba',
                 'Llevas la melodía, en el registro agudo del piano.'),
                ('EL COMPÁS', '6/8, en dos',
                 'Seis cortas por compás, de tres en tres. El pie marca dos veces, como en Miss Muffet.'),
                ('SI TE PIERDES', 'No pares',
                 'Sigue contando y vuelve a entrar en el compás siguiente. Parar es peor que fallar.'),
            ],
            pie='Tocar con otra persona es una cosa distinta de tocar solo, y no se aprende tocando '
                'solo. Aquí lo que se entrena no son los dedos: es escuchar a la otra persona mientras '
                'tocas, que al principio parece imposible y luego sale.',
        ),
        titulo_ritmos='Así empieza tu parte',
        pie_ritmos='El compás 1 de tu derecha y el compás 4 de tu izquierda, medidos en tu partitura. '
                   'La parte de abajo la toca la profesora.',
        ritmos=[
            ('TU DERECHA', 'c. 1 · tres cortas, una larga y otra corta',
             _c1(), AZUL, 'treble', None),
            ('TU IZQUIERDA', 'c. 4 · calla tres compases y contesta ella sola',
             [n('B4'), n('A4', 'e'), n('G4', 'q.')], OCRE, 'treble', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Va en 6/8: seis notas cortas por compás, agrupadas de tres en tres y contadas en DOS. '
            'Ya lo viste en Little Miss Muffet.',
            'Es a cuatro manos: se toca entre dos personas en el mismo piano.',
            'Tú tocas la parte de arriba, la que lleva la melodía; la otra parte la toca la profesora.',
            'Tu mano izquierda calla los tres primeros compases y contesta ella sola en el compás 4.',
            'La música empieza en la segunda página: la primera es la portada. Y lo importante no es '
            'tocar rápido: es empezar y acabar los dos juntos.',
        ],
        reto='Entrar a la vez. Cuando dos personas tocan juntas, el que empieza antes arrastra al otro '
             'y la música se descoloca desde el primer compás. Y no se arregla tocando mejor: se '
             'arregla contando en voz alta antes de empezar.',
        truco='Antes de tocar, una de las dos cuenta un compás entero en voz alta —un-dos, dos golpes, '
              'no seis— y las dos empezáis en el golpe siguiente. Siempre la misma persona, y siempre a '
              'la misma velocidad. Y mientras tocáis, miraos de vez en cuando: eso es lo que hace que '
              'suene a una sola música.',
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
                 pista='medido · los cuatro primeros compases de tu partitura, tal y como están escritos',
                 sistemas=[
                     dict(cap='a) los cc. 1 y 2, muy despacio, contando UN-dos en cada compás',
                          events=_c1() + _c2(),
                          bars=2),
                     dict(cap='b) el c. 3 y el c. 4 · fíjate: en el cuarto tu derecha calla y contesta '
                                  'la izquierda',
                          events=_c3() + [sil('q.'), sil('q.')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Entrar a tiempo',
                 pista='una de las dos cuenta un compás en voz alta y las dos entran en el golpe siguiente',
                 sistemas=[
                     dict(cap='a) un compás de silencio y entras · cuéntalo todo en voz alta',
                          events=[sil('q.'), sil('q.')] + _c1(),
                          bars=2),
                     dict(cap='b) y otra vez, entrando después de dos compases · mientras esperas, '
                              'la otra parte ya está sonando',
                          events=[sil('q.'), sil('q.'), sil('q.'), sil('q.')] + _c1(),
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE EMPIEZA ENTRE DOS',
                 texto='Siempre cuenta la misma persona, en voz alta, un compás entero antes de '
                       'empezar. En 6/8 se cuenta DOS, no seis. Y a la velocidad a la que se va a '
                       'tocar, no más rápido: la cuenta es la que decide el tempo. Si la cuenta va '
                       'deprisa, la pieza va deprisa, y ya no hay manera de arreglarlo a mitad.'),
            dict(num=3, titulo='Y si te pierdes, no pares',
                 pista='se deja de tocar un momento, se sigue contando, y se entra en el compás siguiente',
                 sistemas=[
                     dict(cap='a) toca el c. 1, deja un compás sin tocar contando, y entra con el c. 2',
                          events=_c1() + [sil('q.'), sil('q.')] + _c2(),
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
                    _c1() + _c2()[:2],
                    corch(['C5', 'C5', 'D5'], 3) + [n('C5'), n('E5', 'e'),
                                                    n('G5'), n('G5', 'e')],
                    cuantas=2,
                    titulo='Busca las dos diferencias',
                    pista='el de arriba es tu parte · en el de abajo hay dos notas cambiadas'),
                verdadero_falso([
                    'Esta pieza se toca entre dos personas en el mismo piano.',
                    'Tú tocas la parte de abajo.',
                    'Si te pierdes, hay que parar y empezar otra vez.',
                    'Acabar juntos es tan importante como empezar juntos.',
                    'Esta pieza va en 6/8 y se cuenta en dos.',
                ], titulo='Verdadero o falso', pista='de tu pieza · marca la casilla'),
                dibujar(['Do', 'Mi', 'Sol', 'Re', 'Si', 'La', 'Sol', 'Do'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · son todas las notas que tocas en esta pieza'),
                escribir(titulo='Copia aquí el compás que más te cueste',
                         pista='cópialo tal cual y luego tócalo cinco veces'),
                rutina('Tu parte, muy despacio, contando UN-dos en voz alta',
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
                nombres(['C5', 'E5', 'G5', 'D5', 'B4', 'A4', 'G4', 'C5'],
                        pista='son las notas de tu parte, contando las dos manos · escríbelas debajo'),
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
