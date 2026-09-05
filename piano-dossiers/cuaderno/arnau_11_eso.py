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
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         sopa, unir, verdadero_falso, contar, inventa, ordenar,
                         colorear, acuerdate)

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

    # Reparto de `arnau_recetas`: semana 1 la R11 (sopa · une · verdadero o
    # falso) y semana 2 la R12 (cuenta · inventa · ordena · colorea).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Eso que tú me das · para hacer en casa',
            intro='Esta hoja es distinta a todas: solo tiene una línea de música, con la letra '
                  'debajo y los acordes encima. Los deberes van de aprender a leerla.',
            bloques=[
                sopa(['ACORDES', 'LETRA', 'MELODIA', 'CANTAR', 'JARABE', 'RESPIRAR',
                      'UNA', 'MI', 'RE', 'DO'], semilla=1111, filas=8,
                     titulo='Sopa de letras de tu canción',
                     pista='diez palabras · tumbadas, de pie o en diagonal'),
                unir([('Las letras C, G, Am de arriba', 'la que tocas tú, con la mano derecha'),
                      ('La letra de debajo', 'el nombre de los acordes que acompañan'),
                      ('La línea de música', 'sirve para saber dónde respirar'),
                      ('Los cuatro golpes del compás', 'se cuentan igual aunque no haya dos manos')],
                     titulo='Une cada cosa con lo que es',
                     pista='están desordenadas · una raya de un punto al otro'),
                verdadero_falso([
                    'Esta hoja tiene dos pentagramas, como las demás.',
                    'Las letras de arriba son acordes, no notas para tocar.',
                    'La melodía repite mucho la misma nota.',
                    'La letra de debajo ayuda a saber cuándo respirar.',
                ], titulo='Verdadero o falso', pista='de tu hoja · marca la casilla'),
                rutina('La melodía entera, leyendo la letra a la vez',
                       'Cantarla mientras la tocas, aunque desafines',
                       'Marcar con lápiz en la hoja dónde respiras'),
                juego('Tú tocas la melodía y quien esté contigo canta la letra. Después al revés. '
                      'Lo importante es acabar los dos a la vez.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Eso que tú me das · para hacer en casa',
            intro='Esta semana toca contar, inventar y ordenar los pasos.',
            bloques=[
                contar([n('E4'), n('E4'), n('E4'), n('D4'), n('E4'), n('G4'), n('E4'), n('D4')],
                       ['¿Cuántos Mi hay?', '¿Cuántas veces sale el Re?',
                        '¿Cuántas notas hay en total?'],
                       titulo='Cuenta lo que ves',
                       pista='es el principio de tu melodía, medido en tu hoja'),
                inventa(['Solo Do, Re y Mi, que son las que más repite tu canción.',
                         'Dos compases de cuatro golpes.',
                         'Que repita una nota tres veces seguidas, como la canción.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases para cantar',
                        pista='tiene que cumplir las tres cosas'),
                ordenar(['Tocar y cantar a la vez.',
                         'Leer la letra en voz alta, sin tocar.',
                         'Tocar la melodía sola, muy despacio.',
                         'Marcar dónde vas a respirar.'],
                        titulo='Pon los pasos en el orden bueno',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                colorear([n('E4'), n('E4'), n('E4'), n('D4'),
                          n('E4', 'h'), n('G4'), n('E4'), n('D4', 'h')],
                         ['Un color para las de un golpe y otro para las de dos.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                acuerdate('En una hoja de melodía y acordes tú solo tocas la línea de notas. Los '
                          'acordes son para quien te acompañe con una guitarra o con el piano. No '
                          'te líes intentando tocar las letras: no son notas.',
                          etiqueta='TÚ TOCAS LA LÍNEA'),
                rutina('La melodía entera sin pararse',
                       'Cantarla de memoria, sin mirar la hoja',
                       'Contar cuatro golpes en voz alta mientras tocas'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
