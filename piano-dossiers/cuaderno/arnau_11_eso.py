# -*- coding: utf-8 -*-
"""Eso que tú me das (canción 11 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (Jarabe de Palo, descarga de
   Musescore, 1 pagina, "PARTe 1"):

     - Do mayor (nada detras de la clave) y compas de 4/4.
     - LO NUEVO: esta hoja NO tiene dos pentagramas. Solo hay UNA linea de
       musica, con la letra debajo y las letras de los acordes encima
       (C · G · Am · C · F · Dm · F · G). Es lo que se llama una hoja de
       melodia y acordes: tu tocas la linea y quien te acompana pone lo demas.
     - La melodia se mueve muy poquito y repite mucho la misma nota, porque
       esta pensada para cantarla.
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
    alumno='Arnau', num=11, nivel='iniciación', slug='EsoQueTuMeDas',
    formato='corto', titulo_corto='Eso que tú me das',
    time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Eso-que-tu-me-das. Jarabe de Palo.pdf'),
    yt='https://www.youtube.com/results?search_query=jarabe+de+palo+eso+que+tu+me+das',

    ficha=dict(
        titulo='Eso que tú me das',
        autor='Jarabe de Palo · Pau Donés (2020)',
        datos=[('Novedad', 'Una sola línea'), ('Golpes', '4 por compás'),
               ('Teclas', 'Solo blancas'), ('Encima', 'Los acordes'),
               ('Debajo', 'La letra')],
        armonia=dict(
            titulo='Una hoja distinta a todas las demás',
            tarjetas=[
                ('UNA SOLA LÍNEA', 'Sin mano izquierda',
                 'Aquí no hay dos pentagramas: solo la melodía, que la tocas con la derecha.'),
                ('LAS LETRAS', 'C · G · Am · F',
                 'Encima. Son los acordes que pone quien te acompaña, no notas para ti.'),
                ('LA LETRA', 'Debajo',
                 'Cada sílaba está debajo de su nota. Si cantas, el ritmo se coloca solo.'),
                ('LA MELODÍA', 'Se mueve poco',
                 'Repite mucho la misma nota, porque está hecha para cantarla, no para lucirse.'),
            ],
            pie='Esta es la clase de hoja que usan los músicos cuando tocan juntos: uno lleva la '
                'melodía y los demás miran las letras de encima para saber qué poner debajo. Saber '
                'leerla te sirve para tocar con otra gente el resto de tu vida.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Los primeros compases de la melodía. Aquí no hay ejemplo de mano izquierda porque '
                   'la partitura no lleva.',
        ritmos=[
            ('LA MELODÍA', 'repite la misma nota y luego baja',
             [n('E4'), n('E4'), n('E4'), n('D4')], AZUL, 'treble', None),
            ('Y SIGUE', 'sube otra vez y se queda quieta',
             [n('E4'), n('G4'), n('E4'), n('E4')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'Solo hay UNA línea de música: la melodía.',
            'Encima del pentagrama hay letras: son los acordes, no notas.',
            'Debajo está la letra de la canción, sílaba a sílaba.',
            'La melodía repite mucho la misma nota antes de moverse.',
            'Las notas largas marcan los sitios donde la voz coge aire.',
            'No hay pentagrama de mano izquierda: esa mano descansa.',
        ],
        reto='Que suene a canción y no a lista de notas. Como la melodía repite mucho, es facilísimo '
             'tocarla toda igual y plana. Lo que la hace sonar bien no son las notas: es respirar '
             'donde respira la letra.',
        truco='Canta la letra antes de tocar, mirando la hoja. Donde tú respiras al cantar, ahí es '
              'donde tiene que respirar la melodía. Márcalo con una rayita a lápiz y tócalo así.',
        sabias='Pau Donés escribió esta canción cuando ya estaba muy enfermo, y va de dar las gracias '
               'por lo que la vida le había dado. La grabó pocos meses antes de morir, en 2020, y es '
               'la última que publicó.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en dónde respira la voz. Ahí es donde respira la melodía.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Esta hoja es distinta: solo hay una línea de música y unas letras encima. Tú tocas la '
              'línea con la derecha; las letras son para quien te acompañe. Así que aquí se trabaja '
              'una cosa nueva: hacer que una melodía sola suene bien.',
        reglas=['SOLO LA MANO DERECHA', 'CANTA ANTES DE TOCAR', 'RESPIRA DONDE RESPIRA LA LETRA'],
        bloques=[
            dict(num=1, titulo='La melodía del principio',
                 pista='medida en tu partitura · repite la misma nota y luego se mueve',
                 sistemas=[
                     dict(cap='a) tres notas iguales y baja · cuenta los cuatro golpes',
                          events=[n('E4'), n('E4'), n('E4'), n('D4'),
                                  n('E4'), n('G4'), n('E4'), n('E4')],
                          bars=2),
                     dict(cap='b) y lo que sigue · sube al La y vuelve, sin salirse de sitio',
                          events=[n('A4'), n('G4'), n('E4'), n('D4'),
                                  n('C4'), n('D4'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='QUÉ SON LAS LETRAS DE ENCIMA',
                 texto='C, G, Am, F… no son notas ni hay que tocarlas: son el nombre del acorde que '
                       'suena debajo de la melodía en ese compás. Si alguien te acompaña con una '
                       'guitarra o con el piano, mira esas letras y sabe qué poner sin leer ni una '
                       'nota. A ti te sirven para saber cuándo cambia el ambiente de la canción.'),
            dict(num=2, titulo='Respirar donde respira la letra',
                 pista='las notas largas son los sitios donde la voz se para: ahí respiras tú también',
                 sistemas=[
                     dict(cap='a) toca hasta la nota larga y para de verdad, como cuando coges aire',
                          events=[n('E4'), n('E4'), n('E4'), n('D4'), n('E4', 'h'), sil('h')],
                          bars=2),
                     dict(cap='b) y ahora dos frases seguidas, respirando en medio',
                          events=[n('E4'), n('G4'), n('E4'), n('D4'), n('C4', 'h'), sil('h'),
                                  n('D4'), n('E4'), n('G4'), n('E4'), n('E4', 'h'), sil('h')],
                          bars=4, show_time=False),
                 ]),
            dict(num=3, titulo='Y la melodía entera, del tirón',
                 pista='medida en tu partitura · las dos frases seguidas, sin parar entre medias',
                 sistemas=[
                     dict(cap='a) si te equivocas, no repitas ese compás: vuelve al principio de la frase',
                          events=[n('E4'), n('E4'), n('E4'), n('D4'),
                                  n('E4'), n('G4'), n('E4'), n('E4'),
                                  n('A4'), n('G4'), n('E4'), n('D4'),
                                  n('C4', 'h'), sil('h')],
                          bars=4),
                 ]),
            dict(tipo='nota', etiqueta='Y ANTES DE TOCAR, CANTA',
                 texto='Pon la hoja delante, sigue la letra con el dedo y canta la canción entera sin '
                       'tocar nada. No hace falta que cantes bien: hace falta que notes dónde coges '
                       'aire. Marca esos sitios con una rayita a lápiz. Después toca, y para en cada '
                       'rayita. Eso es lo que convierte una fila de notas en una canción.'),
        ],
    ),

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='Eso que tú me das · para hacer en casa',
             intro='Esta semana toca aprender a leer una hoja de melodía y acordes, que es distinta '
                   'de las de antes.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='escríbelas en la cajita de debajo',
                      notas=['E4', 'D4', 'C4', 'G4', 'A4', 'E4', 'F4', 'D4']),
                 dict(tipo='une', num=2, titulo='Une cada cosa con dónde está en la hoja',
                      pista='una raya de un punto al otro',
                      pares=[('Las letras C, G, Am', 'debajo del pentagrama'),
                             ('La letra de la canción', 'en el pentagrama'),
                             ('Las notas', 'encima del pentagrama')]),
                 dict(tipo='figuras', num=3, titulo='¿Cuántos golpes dura cada una?',
                      pista='escribe el número en la caja',
                      figuras=[('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                               ('h.', 'blanca con puntito')]),
                 dict(tipo='dibuja', num=4, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Mi', 'Re', 'Do', 'Sol', 'La', 'Mi', 'Fa', 'Re']),
                 rutina('Cantar la canción entera mirando la hoja, sin tocar',
                        'La melodía del principio, muy despacio',
                        'Marcar a lápiz dónde respiras'),
                 juego('Canta la canción mientras quien esté contigo lleva el pulso dando palmadas '
                       'flojitas. Tú tienes que parar de cantar exactamente donde respira la letra, y '
                       'las palmadas siguen igual. Así se ve que el tiempo no se para cuando tú '
                       'respiras.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='Eso que tú me das · para hacer en casa',
             intro='Esta semana toca fijarse en cuánto se repite la melodía y tocarla ya entera.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('E4'), n('E4'), n('E4'), n('D4')],
                                [n('E4'), n('G4'), n('E4'), n('E4')],
                                [n('E4'), n('E4'), n('E4'), n('D4')],
                                [n('C4'), n('D4'), n('E4'), n('E4')]]),
                 dict(tipo='nombres', num=2, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['G4', 'E4', 'A4', 'C5', 'D4', 'F4', 'B4', 'E4']),
                 dict(tipo='colorea', num=3, titulo='Colorea las notas que se repiten',
                      pista='esta melodía dice muchas veces la misma nota antes de moverse',
                      eventos=[n('E4'), n('E4'), n('E4'), n('D4'),
                               n('E4'), n('E4'), n('G4'), n('E4', 'h')],
                      leyenda=['Repetir una nota es fácil para los dedos.',
                               'Lo que hace bonita la canción es dónde para, no cuántas notas tiene.']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='En una hoja como esta tú solo tocas la línea de música. Las letras de '
                            'encima son para quien te acompaña. Si algún día tocas con alguien, esa '
                            'persona mirará las letras y tú la melodía, y sonará entero.'),
                 rutina('La canción entera con la derecha, parando donde respiras',
                        'Cantarla una vez sin tocar, siguiendo la letra con el dedo',
                        'Tocarla mientras alguien canta la letra'),
                 juego('Tú tocas la melodía y quien esté contigo canta la letra. Después cambiad. Lo '
                       'que hay que conseguir es que los dos respiréis en el mismo sitio, sin poneros '
                       'de acuerdo antes.', 'esta vez para hacerlo juntos'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
