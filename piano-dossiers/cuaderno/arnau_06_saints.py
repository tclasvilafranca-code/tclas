# -*- coding: utf-8 -*-
"""Oh, When the Saints (canción 6 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "Primer Level", 1 página):

     - Do mayor (nada detrás de la clave), 4/4, y pone "Lively".
     - La melodia empieza ANTES del primer compas, con tres notas de
       carrerilla: Do · Mi · Fa, y despues sube al Sol y se para.
     - La mano izquierda repite la MISMA nota (Do) varias veces seguidas, y
       tiene compases enteros de silencio.
     - Es la primera del cuaderno donde una mano descansa compases enteros
       mientras la otra sigue.
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
    alumno='Arnau', num=6, nivel='iniciación', slug='WhenTheSaints',
    formato='corto', titulo_corto='Oh, When the Saints',
    time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Oh when the Saint.pdf'),
    yt='https://www.youtube.com/results?search_query=when+the+saints+go+marching+in+piano',

    ficha=dict(
        titulo='Oh, When the Saints',
        autor='Canción popular · arreglo de Gilbert DeBenedetti',
        datos=[('Teclas', 'Solo blancas'), ('Golpes', '4 por compás'),
               ('Empieza', 'Antes de tiempo'), ('Mano izq.', 'Una nota'),
               ('Carácter', 'Lively')],
        armonia=dict(
            titulo='Tres notas de carrerilla y a subir',
            tarjetas=[
                ('LA ENTRADA', 'Do · Mi · Fa',
                 'Tres notas antes del primer compás, como cuando coges carrerilla para saltar.'),
                ('Y DESPUÉS', 'Sube al Sol',
                 'Llega arriba y se queda quieta. Ese es el sitio donde la canción respira.'),
                ('LA IZQUIERDA', 'La misma nota',
                 'Repite el Do varias veces y luego se calla compases enteros.'),
                ('LOS DESCANSOS', 'Compases vacíos',
                 'Hay trozos en los que una mano no toca nada. Se cuentan igual.'),
            ],
            pie='Casi toda la canción son las mismas cuatro notas subiendo. Lo que hay que aprender '
                'no son las teclas: es entrar a tiempo, porque la melodía empieza antes de que empiece '
                'el compás.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Las tres notas de carrerilla y lo que viene detrás, medido en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'tres notas de carrerilla y una larga arriba',
             [n('C4'), n('E4'), n('F4'), n('G4')], AZUL, 'treble', None),
            ('LA IZQUIERDA', 'la misma nota, repetida',
             [n('C3'), n('C3'), n('C3'), n('C3')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'La canción empieza antes del primer compás, con tres notas.',
            'La mano izquierda repite la misma nota muchas veces.',
            'Hay compases en los que una mano no toca nada.',
            'Pone «Lively», que quiere decir con marcha: es una canción alegre.',
        ],
        reto='Entrar a tiempo. Como la melodía empieza antes del primer compás, hay que contar los '
             'cuatro golpes ENTEROS antes de tocar la primera nota. Si entras cuando te apetece, la '
             'canción se descoloca desde el principio.',
        truco='Cuenta un compás entero en voz alta antes de empezar: «un, dos, tres» y en el CUATRO '
              'tocas la primera nota. Los cantantes lo hacen así siempre. Si te cuesta, que alguien te '
              'cuente los cuatro golpes mientras tú solo escuchas, y entra cuando toque.',
        sabias='Esta canción se toca en Nueva Orleans en los desfiles, y allí la tocan dos veces: '
               'muy lenta y triste a la ida, y rápida y alegre a la vuelta. Es la misma melodía, solo '
               'cambia la velocidad.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuatro golpes con el pie antes de que empiece a cantar.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo difícil de esta canción no son las notas, que son cuatro y suben seguidas: es entrar '
              'a tiempo. Así que primero se aprende a contar y a entrar, y después ya se toca.',
        reglas=['CUENTA UN COMPÁS ANTES DE EMPEZAR', 'LAS CUATRO NOTAS SUBEN SEGUIDAS',
                'LOS DESCANSOS SE CUENTAN'],
        bloques=[
            dict(num=1, titulo='Las cuatro notas que suben',
                 pista='medido en tu partitura · Do · Mi · Fa · Sol, y arriba se queda quieta',
                 sistemas=[
                     dict(cap='a) sube y quédate arriba · la última dura el doble que las otras',
                          events=[n('C4'), n('E4'), n('F4'), n('G4'),
                                  n('G4', 'h'), n('F4'), n('E4')],
                          bars=2),
                     dict(cap='b) y ahora subiendo y bajando, para que la mano se acostumbre',
                          events=[n('C4'), n('E4'), n('F4'), n('G4'),
                                  n('F4'), n('E4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Entrar a tiempo',
                 pista='la melodía empieza antes del compás · cuenta cuatro y entra en el último',
                 sistemas=[
                     dict(cap='a) tres golpes de silencio y entras en el cuarto · cuenta en voz alta',
                          events=[sil('q'), sil('q'), sil('q'), n('C4'),
                                  n('E4'), n('F4'), n('G4', 'h')],
                          bars=2),
                     dict(cap='b) y otra vez, ahora con la frase entera detrás · si entras tarde, para '
                              'y vuelve a contar desde el principio',
                          events=[sil('q'), sil('q'), sil('q'), n('C4'),
                                  n('E4'), n('F4'), n('G4', 'h'),
                                  n('G4'), n('F4'), n('E4'), n('C4'),
                                  n('E4', 'h'), sil('h')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA ANTES DEL COMPÁS',
                 texto='Muchas canciones empiezan con una o varias notas de carrerilla, antes de que '
                       'empiece el primer compás de verdad. No es un error de la partitura: es que la '
                       'letra empieza así. Cuenta los cuatro golpes enteros y entra en el último, y '
                       'verás que todo lo demás encaja solo.'),
            dict(tipo='nota', etiqueta='CÓMO SE CUENTA UN COMPÁS ENTERO',
                 texto='Da cuatro golpes con el pie, siempre a la misma velocidad, y di los números en '
                       'voz alta: un, dos, tres, CUATRO. En ese cuatro tocas. No vale contar deprisa '
                       'los tres primeros: los cuatro golpes tienen que durar exactamente lo mismo, '
                       'porque esa es la velocidad a la que va a ir la canción entera.'),
            dict(num=3, titulo='La izquierda: una nota y a descansar', clef='bass',
                 pista='medido · repite el Do y después se calla compases enteros',
                 sistemas=[
                     dict(cap='a) tres veces la misma nota y un compás sin tocar nada · cuéntalo igual',
                          events=[n('C3'), n('C3'), n('C3'), sil('q'),
                                  sil('q'), sil('q'), sil('q'), sil('q')],
                          bars=2, clef='bass'),
                 ]),
        ],
    ),

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='Oh, When the Saints · para hacer en casa',
             intro='Esta semana toca contar antes de empezar, que es de lo que va esta canción.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='son las notas de la melodía · escríbelas en la cajita',
                      notas=['C4', 'E4', 'F4', 'G4', 'E4', 'F4', 'G4', 'A4']),
                 dict(tipo='dibuja', num=2, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Do', 'Mi', 'Fa', 'Sol', 'Fa', 'Mi', 'Sol', 'Do']),
                 dict(tipo='figuras', num=3, titulo='¿Cuántos golpes dura cada una?',
                      pista='escribe el número en la caja',
                      figuras=[('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                               ('h.', 'blanca con puntito')]),
                 dict(tipo='colorea', num=4, titulo='Colorea las notas que suben',
                      pista='la melodía sube cuatro escalones seguidos · píntalos de un color',
                      eventos=[n('C4'), n('E4'), n('F4'), n('G4'),
                               n('F4'), n('E4'), n('C4'), n('C4', 'h')],
                      leyenda=['Subir es ir de una nota a otra más arriba en el papel.',
                               'En el piano, más arriba en el papel es más a la derecha.']),
                 rutina('Contar cuatro golpes y entrar en el último, diez veces',
                        'Las cuatro notas que suben, muy despacio',
                        'La izquierda sola, contando los compases de silencio'),
                 juego('Quien esté contigo cuenta cuatro golpes en voz alta, siempre a la misma '
                       'velocidad, y tú entras tocando una nota justo en el cuatro. Diez veces. Luego '
                       'cambiad. Es lo mismo que hacen los músicos antes de empezar a tocar juntos.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='Oh, When the Saints · para hacer en casa',
             intro='Ahora que ya entras a tiempo, esta semana toca mirar la partitura con lápiz.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('C4'), n('E4'), n('F4'), n('G4')],
                                [n('G4'), n('F4'), n('E4'), n('C4')],
                                [n('C4'), n('E4'), n('F4'), n('G4')],
                                [n('E4'), n('C4'), n('E4'), n('G4')]]),
                 dict(tipo='colorea', num=2, titulo='Colorea las notas largas',
                      pista='las que tienen el óvalo hueco duran más',
                      eventos=[n('C4'), n('E4'), n('F4'), n('G4', 'h'),
                               n('F4'), n('E4'), n('C4', 'h')],
                      leyenda=['El óvalo pintado dura un golpe.',
                               'El óvalo hueco dura dos golpes.']),
                 dict(tipo='nombres', num=3, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['G4', 'F4', 'E4', 'C4', 'A4', 'G4', 'E4', 'F4']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='Cuando una mano no toca nada durante un compás entero, el tiempo sigue '
                            'corriendo igual. No es un descanso para ti: es un descanso para esa mano, '
                            'mientras tú sigues contando por dentro.'),
                 rutina('La canción entera con la derecha sola',
                        'Los cuatro primeros compases con las dos manos',
                        'Contar en voz alta mientras tocas, sin parar en los fallos'),
                 juego('Toca la primera nota de la canción justo después de que quien esté contigo '
                       'cuente cuatro golpes. Que cambie la velocidad cada vez: unas veces muy lento y '
                       'otras más rápido. Tú tienes que entrar siempre a tiempo, vaya como vaya.',
                       'esta vez cambiando la velocidad'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
