# -*- coding: utf-8 -*-
"""Rain Rain Go Away (canción 19 de Arnau, iniciación). A CUATRO MANOS.

   Medido sobre el PDF de su carpeta de Drive (arr. Regina Pratley, "easy
   piano duet", 3 paginas: la primera es la portada de free-scores y la musica
   empieza en la segunda).

     - Do mayor: no hay nada detras de la clave.
     - LO NUEVO: es una pieza a CUATRO MANOS. Se toca entre dos personas en el
       mismo piano: una hace la parte de arriba y la otra la de abajo. Arnau
       toca la parte de arriba, la que lleva la melodía.
     - Las alturas comprobadas de tu parte: Sol · Sol | Sol · Sol · Mi · La | Sol · Sol.

   Lo que NO se cita compas a compas: en una partitura a cuatro manos hay
   cuatro pentagramas por sistema y el lector los empareja mal, asi que se
   citan solo las alturas comprobadas y el resto va como ANDAMIO.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         crucigrama, palmas, figuras, acuerdate, teclado,
                         adivinar, rodear, contar)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Arnau', num=19, nivel='iniciación', slug='RainRainGoAway',
    formato='corto', titulo_corto='Rain Rain Go Away', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'rain-rain-away-easy-piano-4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=rain+rain+go+away+piano+duet',

    ficha=dict(
        titulo='Rain Rain Go Away',
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
            ('TU MANO DERECHA', 'dos notas iguales, arriba del todo',
             [n('G5'), n('G5'), n('E5'), n('A5')], AZUL, 'treble', None),
            ('TU MANO IZQUIERDA', 'acompaña con notas largas (andamio)',
             [n('G3', 'h'), n('G3', 'h')], OCRE, 'bass', None),
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
        sabias='La canción es de hace siglos y en Inglaterra la cantaban los niños para que parara de llover y poder salir a jugar. Hay versiones en un montón de idiomas, y en todas se le pide lo mismo a la lluvia: que vuelva otro día.',
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
                          events=[n('G5'), n('G5'), n('E5'), n('A5'), n('G5'), n('G5'), n('E5', 'h')],
                          bars=2),
                     dict(cap='b) y lo que sigue · las mismas notas, moviéndose un poco',
                          events=[n('G5'), n('E5'), n('G5'), n('A5'), n('G5'), n('E5'), n('E5', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Entrar a tiempo',
                 pista='una de las dos cuenta un compás en voz alta y las dos entran en el golpe siguiente',
                 sistemas=[
                     dict(cap='a) un compás de silencio y entras · cuéntalo todo en voz alta',
                          events=[sil('q'), sil('q'), sil('q'), sil('q'), n('G5'), n('G5'), n('E5'), n('A5')],
                          bars=2),
                     dict(cap='b) y otra vez, entrando después de dos compases · mientras esperas, '
                              'la otra parte ya está sonando',
                          events=[sil('q'), sil('q'), sil('q'), sil('q'),
                                  sil('q'), sil('q'), sil('q'), sil('q'),
                                  n('G5'), n('G5'), n('E5'), n('A5')],
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
                          events=[n('G5'), n('G5'), n('E5'), n('A5'), sil('q'), sil('q'), sil('q'), sil('q'), n('G5'), n('G5'), n('E5', 'h')],
                          bars=3),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ NO SE PARA',
                 texto='Si tocas solo y te equivocas, puedes parar y repetir. Si tocas con otra persona, '
                       'no: mientras tú paras, esa persona sigue, y cuando vuelves ya no sabes dónde '
                       'está. Lo que se hace es dejar de tocar, seguir contando por dentro, y volver a '
                       'entrar al principio del compás siguiente. Eso hay que practicarlo a propósito.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R7 (crucigrama · palmas ·
    # figuras) y semana 2 la R8 (teclado · adivina · rodea · cuenta).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Rain Rain Go Away · para hacer en casa',
            intro='Lo nuevo: se toca entre dos personas. Esta semana prepara tu parte en casa.',
            bloques=[
                crucigrama('DUETO', [
                    ('REDONDA', 2, 'La figura que dura cuatro golpes.'),
                    ('PULSO', 1, 'Los golpes que van pasando siempre igual, como un reloj.'),
                    ('NEGRA', 1, 'La figura que dura un golpe.'),
                    ('CUATRO', 3, 'Las manos que hacen falta para tocar esta pieza.'),
                    ('MANOS', 3, 'Tienes dos, y con las de otra persona son cuatro.'),
                ], cierre='Las casillas grises dicen cómo se llama una pieza para dos personas.'),
                palmas([('LLU-VIA', 2), ('PA-RA-GUAS', 3)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                figuras([('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                         ('h.', 'blanca con puntito')],
                        titulo='¿Cuántos golpes dura cada una?',
                        pista='escribe el número en la caja'),
                acuerdate('Empezar a la vez no se adivina: se decide. Uno cuenta un compás en voz '
                          'alta y los dos entran en el golpe siguiente.',
                          etiqueta='EMPEZAR LOS DOS A LA VEZ'),
                rutina('Tu parte, muy despacio, contando en voz alta',
                       'Contar un compás y entrar en el golpe siguiente, diez veces',
                       'Tu parte entera sin parar, aunque haya fallos'),
                juego('Quien esté contigo cuenta un compás y luego lleva el pulso con palmadas '
                      'mientras tocas. Si te pierdes, NO pares: vuelve a entrar.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Rain Rain Go Away · para hacer en casa',
            intro='Esta semana ya se toca con otra persona. En casa, prepara lo que se puede solo.',
            bloques=[
                teclado({7: 1, 9: 2, 11: 3, 12: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'Tu parte va en esta zona, la de arriba: la otra persona toca a tu izquierda.'],
                        titulo='En el teclado',
                        pista='tu parte es la de la derecha del piano'),
                adivinar([('Nos hacen falta cuatro para tocar esta pieza.', 'MANOS'),
                          ('Voy pasando siempre igual y nos mantiene juntos.', 'PULSO'),
                          ('Es lo que NO hay que hacer si te pierdes.', 'PARAR')],
                         titulo='Adivina quién soy',
                         pista='una letra en cada casilla'),
                rodear([[n('G5'), n('G5'), n('E5'), n('A5')],
                        [n('G5'), n('E5'), n('G5'), n('A5')],
                        [n('G5'), n('G5'), n('E5'), n('A5')],
                        [n('C5'), n('D5'), n('E5'), n('E5')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='son de tu parte · míralos nota a nota'),
                contar([n('G5'), n('G5'), n('E5'), n('A5'), n('G5'), n('G5'), n('E5')],
                       ['¿Cuántos Sol hay?', '¿Cuántas veces sale el Mi?',
                        '¿Cuántas notas hay en total?'],
                       titulo='Cuenta lo que ves',
                       pista='son las alturas comprobadas de tu parte'),
                rutina('Tu parte entera sin parar, tres veces',
                       'Contar un compás y entrar, con alguien de casa',
                       'Mirar a la otra persona de vez en cuando, sin dejar de tocar'),
                juego('Tocad los dos a la vez y, sin decir nada, que uno de los dos vaya un poco más '
                      'despacio a propósito. El otro tiene que seguirle. Eso es tocar en pareja.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
