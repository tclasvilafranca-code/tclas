# -*- coding: utf-8 -*-
"""Popeye el marinerito (canción 17 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (Sammy Lerner, arr. A. C.
   Escobes, 1 pagina):

     - SOL MAYOR: comprobado a zoom, un sostenido detras de la clave. Eso
       quiere decir que todos los FA de la cancion se tocan en la tecla negra.
       Es la primera pieza del cuaderno con sostenido en la armadura (antes
       solo habia habido bemol).
     - Compas de 3/4 y pone "Allegretto".
     - Empieza con un SILENCIO: la primera nota no cae en el uno.
     - La izquierda hace un vaiven de acordes que se repite todo el rato:
       medido Sol · Si · Si, una y otra vez.
     - Es larga: pasa de los 29 compases.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         diferencias, contar, teclado, acuerdate,
                         verdadero_falso, palmas, rodear, dibujar)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

CANCION = dict(
    alumno='Arnau', num=17, nivel='iniciación', slug='Popeye',
    formato='corto', titulo_corto='Popeye el marinerito',
    time_sig=(3, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Popeye el marinerito.pdf'),
    yt='https://www.youtube.com/results?search_query=popeye+the+sailor+man+piano',

    ficha=dict(
        titulo='Popeye el marinerito',
        autor='Sammy Lerner (1933) · arreglo de A. C. Escobés',
        datos=[('Novedad', 'Un sostenido'), ('Golpes', '3 por compás'),
               ('Empieza', 'Con silencio'), ('Mano izq.', 'Vaivén'),
               ('Carácter', 'Allegretto')],
        armonia=dict(
            titulo='Un sostenido en la armadura',
            tarjetas=[
                ('EL SOSTENIDO', 'Todos los Fa',
                 'Detrás de la clave hay un signo: cada Fa de la canción va en la tecla negra.'),
                ('EMPIEZA TARDE', 'Con un silencio',
                 'La primera nota no cae en el uno: hay un hueco antes. Se cuenta igual.'),
                ('LA IZQUIERDA', 'Siempre lo mismo',
                 'Un vaivén de acordes que se repite sin cambiar casi nunca.'),
                ('ES LARGA', 'Más de 29 compases',
                 'Pero repite mucho: si te aprendes la primera parte, tienes casi todo.'),
            ],
            pie='Ya has visto un bemol en la armadura (canción 5) y sostenidos escritos a mano '
                '(canción 13). Aquí es un sostenido puesto al principio, que vale para toda la pieza: '
                'la misma idea del bemol, pero con la tecla negra del otro lado.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Un compás de cada mano, medido en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'entra después del silencio',
             [sil('q'), n('D4'), n('D4')], AZUL, 'treble', SOL),
            ('LA IZQUIERDA', 'el vaivén: abajo y dos veces arriba',
             [n('G3'), n('B3'), n('B3')], OCRE, 'bass', SOL),
        ],
        especial=[
            'Hay UN SOSTENIDO detrás de la clave: todos los Fa van en la tecla negra.',
            'Cada compás lleva tres golpes: un-dos-tres.',
            'La canción empieza con un silencio: la primera nota no cae en el uno.',
            'La izquierda hace siempre el mismo vaivén: una abajo y dos arriba.',
            'Pone «Allegretto»: alegre, con marcha, pero sin correr.',
            'Es larga, pero repite mucho: hay pocas cosas distintas.',
            'El vaivén de la izquierda solo cambia de sitio cuatro o cinco veces.',
            'El primer golpe de cada compás pesa más que los otros dos.',
        ],
        reto='Acordarse del sostenido. Está escrito una vez, al principio, y vale para toda la canción: '
             'si tocas un Fa en la tecla blanca, la canción suena rara y no sabrás por qué.',
        truco='Antes de empezar, toca todos los Fa de la canción en la tecla negra, uno detrás de otro. '
              'Con eso la mano se acuerda. Y si algo suena raro mientras tocas, lo primero que hay que '
              'mirar no es el ritmo: es si te has dejado el sostenido.',
        sabias='La canción es de 1933 y la escribieron para los dibujos animados. En los cines, cuando '
               'sonaba esta música, los niños ya sabían que Popeye iba a comerse las espinacas: es una '
               'de las primeras melodías que se usaron como aviso de que algo iba a pasar.',
        qr=dict(titulo='Escúchala',
                texto='Marca tres golpes con el pie: un-dos-tres, y verás que encaja.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Aquí hay dos cosas que ya sabes hacer por separado: un sostenido en la armadura y entrar '
              'después de un silencio. Lo que es nuevo es hacerlas a la vez, y que la pieza es larga.',
        reglas=['TODOS LOS FA, EN LA TECLA NEGRA', 'CUENTA EL SILENCIO DEL PRINCIPIO',
                'ALLEGRETTO, PERO SIN CORRER'],
        bloques=[
            dict(num=1, titulo='Primero, los Fa de la tecla negra',
                 pista='el sostenido del principio vale para toda la canción',
                 sistemas=[
                     dict(cap='a) sube y baja pasando por el Fa · ese Fa es la tecla negra',
                          events=[n('D4'), n('E4'), n('F#4'), n('G4'), n('F#4'), n('E4'),
                                  n('D4', 'h.')],
                          bars=3),
                 ]),
            dict(tipo='nota', etiqueta='EL SOSTENIDO DEL PRINCIPIO',
                 texto='En la canción 5 había un bemol al principio y todos los Si iban a la tecla '
                       'negra de la izquierda. Aquí hay un sostenido y todos los Fa van a la tecla '
                       'negra de la derecha. Es la misma idea: se escribe una vez y manda en toda la '
                       'pieza. No lo van a repetir delante de cada nota.'),
            dict(num=2, titulo='Entrar después del silencio',
                 pista='medido · la primera nota no cae en el uno, cae en el dos',
                 sistemas=[
                     dict(cap='a) un golpe de silencio y entras · cuenta “un” en voz alta y toca en el “dos”',
                          events=[sil('q'), n('D4'), n('D4'), sil('q'), n('E4'), n('E4'),
                                  n('D4', 'h.')],
                          bars=3),
                     dict(cap='b) y ahora la frase entera detrás · si entras en el uno, todo va corrido',
                          events=[sil('q'), n('D4'), n('D4'), n('G4'), n('F#4'), n('E4'),
                                  n('D4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='El vaivén de la izquierda', clef='bass',
                 pista='medido · una abajo y dos arriba, siempre igual',
                 sistemas=[
                     dict(cap='a) Sol · Si · Si, una y otra vez · el primero pesa más que los otros dos',
                          events=[n('G3'), n('B3'), n('B3'), n('G3'), n('B3'), n('B3'),
                                  n('G3', 'h.')],
                          bars=3, clef='bass'),
                     dict(cap='b) y cuando cambia de sitio · el dibujo es el mismo, solo se muda',
                          events=[n('A3'), n('C4'), n('C4'), n('D3'), n('A3'), n('A3'),
                                  n('G3', 'h.')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ ESTA CANCIÓN ES MÁS FÁCIL DE LO QUE PARECE',
                 texto='Tiene muchos compases, pero la izquierda hace casi siempre el mismo vaivén y '
                       'solo cambia de sitio. Así que no hay veintinueve compases que aprender: hay un '
                       'vaivén y unos pocos sitios donde se muda. Busca en tu partitura dónde cambia y '
                       'márcalo a lápiz: verás que son cuatro o cinco veces.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R3 (diferencias · cuenta ·
    # teclado) y semana 2 la R4 (verdadero o falso · palmas · rodea · dibuja).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Popeye el marinerito · para hacer en casa',
            intro='Lo nuevo: un sostenido al principio. Todos los Fa van en la tecla negra.',
            bloques=[
                diferencias(
                    [n('D4'), n('E4'), n('F#4'), n('G4'), n('B4'), n('A4')],
                    [n('D4'), n('E4'), n('F4'), n('G4'), n('B4'), n('A4', 'h')],
                    cuantas=2,
                    titulo='Busca las dos diferencias',
                    pista='el de arriba es tu canción · en el de abajo hay dos cosas cambiadas'),
                contar([n('D4'), n('E4'), n('F#4'), n('G4'), n('B4'), n('A4'), n('D5'), n('C5')],
                       ['¿Cuántas notas hay en total?', '¿Cuántos Fa hay?',
                        '¿Cuántas notas van en tecla negra?'],
                       titulo='Cuenta lo que ves',
                       pista='son las notas de tu melodía, medidas en tu partitura'),
                teclado({3: 1, 4: 2, 6: 3, 0: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'La número 1 es un Fa: en esta canción se toca en la negra de al lado.'],
                        titulo='En el teclado',
                        pista='ojo con la número 1'),
                acuerdate('Un sostenido detrás de la clave manda en toda la canción y en todos los '
                          'Fa, estén arriba o abajo. No lo repiten en cada nota: se da por sabido. '
                          'Antes de tocar, busca todos los Fa de tu partitura y márcalos con lápiz.',
                          etiqueta='EL SOSTENIDO DEL PRINCIPIO'),
                rutina('Todos los Fa de la canción, en la tecla negra',
                       'El vaivén de la izquierda, solo, veinte veces',
                       'Entrar después del silencio del principio'),
                juego('Quien esté contigo dice nombres de nota y tú las buscas en el piano. Cuando '
                      'diga Fa, tienes que ir a la tecla negra.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Popeye el marinerito · para hacer en casa',
            intro='Segunda semana: preguntas, ritmo de palabras y notas que dibujar.',
            bloques=[
                verdadero_falso([
                    'Esta canción tiene un sostenido detrás de la clave.',
                    'Eso quiere decir que todos los Fa van en la tecla negra.',
                    'La canción empieza en el primer golpe del compás.',
                    'La mano izquierda repite el mismo vaivén casi todo el rato.',
                    'Esta canción tiene tres golpes en cada compás.',
                ], titulo='Verdadero o falso', pista='de tu canción · marca la casilla'),
                palmas([('PO-PE-YE', 3), ('MA-RI-NE-RO', 4), ('ES-PI-NA-CAS', 4)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                rodear([[n('G3'), n('B3'), n('B3')], [n('G3'), n('B3'), n('D4')],
                        [n('G3'), n('B3'), n('B3')], [n('A3'), n('C4'), n('C4')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='es el vaivén de tu mano izquierda · míralo nota a nota'),
                dibujar(['Sol', 'Fa♯', 'Re', 'Si', 'Mi', 'La', 'Do', 'Re'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · el Fa♯ se dibuja igual que el Fa'),
                rutina('La canción entera, sin fallar ni un Fa',
                       'Los 29 compases seguidos, aunque sea muy despacio',
                       'Contar un-dos-tres en voz alta mientras tocas'),
                acuerdate('Esta canción empieza con un silencio: la primera nota NO cae en el uno. '
                          'Cuenta “un” en silencio y entra en el golpe siguiente. Si entras en el '
                          'uno, la izquierda y la derecha no se juntan nunca.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
