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
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

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

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='Rain Rain Go Away · para hacer en casa',
             intro='Esta semana toca aprenderse tu parte en casa. La semana que viene se junta con la '
                   'otra.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='escríbelas en la cajita de debajo',
                      notas=['G5', 'E5', 'A5', 'C5', 'D5', 'B4', 'F5', 'G5']),
                 dict(tipo='dibuja', num=2, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Sol', 'Mi', 'La', 'Do', 'Re', 'Si', 'Fa', 'Sol']),
                 dict(tipo='figuras', num=3, titulo='¿Cuántos golpes dura cada una?',
                      pista='escribe el número en la caja',
                      figuras=[('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                               ('h.', 'blanca con puntito')]),
                 dict(tipo='colorea', num=4, titulo='Colorea las notas que se repiten',
                      pista='en esta pieza hay muchas notas iguales seguidas',
                      eventos=[n('G5'), n('G5'), n('E5'), n('A5'), n('G5'), n('G5'), n('E5', 'h')],
                      leyenda=['Repetir una tecla es fácil: no hay que buscar nada.',
                               'Lo difícil de esta pieza es tocarla al mismo tiempo que otra persona.']),
                 rutina('Tu parte, muy despacio, contando en voz alta',
                        'Contar un compás y entrar en el golpe siguiente, diez veces',
                        'Tu parte entera sin parar, aunque haya fallos'),
                 juego('Quien esté contigo cuenta un compás en voz alta y luego lleva el pulso con '
                       'palmadas mientras tú tocas tu parte. Si te pierdes, NO pares: sigue contando y '
                       'vuelve a entrar. Eso es lo que hay que practicar, no las notas.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='Rain Rain Go Away · para hacer en casa',
             intro='Esta semana ya se toca con otra persona. En casa, prepara lo que se puede preparar '
                   'solo.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('G5'), n('G5'), n('E5'), n('A5')], [n('G5'), n('E5'), n('G5'), n('A5')], [n('G5'), n('G5'), n('E5'), n('A5')], [n('C5'), n('D5'), n('E5'), n('E5')]]),
                 dict(tipo='nombres', num=2, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['E5', 'G5', 'C5', 'A5', 'B4', 'D5', 'G5', 'F5']),
                 dict(tipo='une', num=3, titulo='Une cada cosa con lo que hay que hacer',
                      pista='una raya de un punto al otro',
                      pares=[('Antes de empezar', 'seguir contando y volver a entrar'),
                             ('Si te pierdes', 'mirar a la otra persona de vez en cuando'),
                             ('Mientras tocáis', 'contar un compás en voz alta')]),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='En una pieza a cuatro manos, acabar juntos es tan importante como empezar '
                            'juntos. La última nota se levanta a la vez, y eso se decide antes: una de '
                            'las dos hace un gesto pequeño con la cabeza y las dos sueltan.'),
                 juego('Tocad los dos a la vez la última nota y levantad la mano en el mismo '
                       'momento, sin decir nada: solo con un gesto pequeño de la cabeza. Cinco veces. '
                       'Acabar juntos se nota tanto como empezar juntos.', 'esta vez para acabar'),
                 rutina('Tu parte entera sin parar, tres veces',
                        'Contar un compás y entrar, con alguien de casa llevando el pulso',
                        'La última nota: levantar la mano a la vez que otra persona'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
