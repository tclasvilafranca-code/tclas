# -*- coding: utf-8 -*-
"""Polly Put the Kettle On (canción 9 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (mfiles.co.uk, arr. Jim
   Paterson, 1 pagina):

     - FA MAYOR: un bemol detras de la clave, o sea que todos los Si van en la
       tecla negra. Ya salio en la cancion 5.
     - LO NUEVO: compas de 2/4, solo DOS golpes por compas, y la melodia va en
       notas cortas casi todo el rato: hay que decir mas notas en menos sitio.
     - La melodia del principio, medida: Sol · La · Sol · Fa · Mi · Do · Do.
     - Encima vienen las letras de los acordes: F, B b, C, C7.
     - La izquierda toca notas sueltas, una o dos por compas.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='Arnau', num=9, nivel='iniciación', slug='PollyKettle',
    formato='corto', titulo_corto='Polly Put the Kettle On',
    time_sig=(2, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Polly Put the Kettle On.pdf'),
    yt='https://www.youtube.com/results?search_query=polly+put+the+kettle+on+piano',

    ficha=dict(
        titulo='Polly Put the Kettle On',
        autor='Canción popular · arr. Jim Paterson (mfiles)',
        datos=[('Novedad', 'Solo 2 golpes'), ('Teclas negras', 'Los Si'),
               ('Mano dcha.', 'Notas cortas'), ('Mano izq.', 'Notas sueltas'),
               ('Extras', 'Letras encima')],
        armonia=dict(
            titulo='Compases de dos golpes, y la melodía corriendo',
            tarjetas=[
                ('EL COMPÁS', 'Dos golpes',
                 'Un-dos, un-dos. Los compases son mucho más cortos que los de antes.'),
                ('LA MELODÍA', 'Notas cortas',
                 'Van de dos en dos, unidas por una barra: caben dos en cada golpe.'),
                ('EL BEMOL', 'Todos los Si',
                 'Otra vez la tecla negra, como en la canción 5. Ya te la sabes.'),
                ('LAS LETRAS', 'F · B♭ · C7',
                 'Encima del pentagrama. Son los acordes, y te avisan de cuándo cambia la izquierda.'),
            ],
            pie='Aquí no hay ninguna nota nueva ni ninguna tecla nueva: lo único que cambia es que hay '
                'que decir más notas en menos tiempo. Por eso esta canción se estudia despacio y se '
                'sube de velocidad poco a poco, no al revés.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Los dos primeros compases de la melodía, medidos en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'notas cortas de dos en dos, bajando',
             corch(['G4', 'A4']) + corch(['G4', 'F4']), AZUL, 'treble', FA),
            ('Y SE PARA', 'y al final del trozo se queda quieta',
             [n('E4'), n('C4')], AZUL, 'treble', FA),
        ],
        especial=[
            'Hay UN BEMOL detrás de la clave: todos los Si van en la tecla negra.',
            'Cada compás lleva solo DOS golpes: un-dos, un-dos.',
            'La melodía va casi toda en notas cortas, de dos en dos.',
            'Encima del pentagrama hay letras: son los acordes, no notas.',
            'La izquierda toca notas sueltas, una o dos por compás.',
            'La canción se repite: la segunda mitad es casi igual que la primera.',
        ],
        reto='Que las notas cortas no se atropellen. Cuando hay dos notas en cada golpe, lo que pasa '
             'es que la primera se alarga y la segunda sale corriendo detrás. Y entonces la canción '
             'cojea aunque toques las teclas correctas.',
        truco='Cuenta «un-y-dos-y» en voz alta: la nota cae en el número y la otra en la Y. Si dices la '
              'Y siempre en el mismo sitio, las dos notas salen igual de largas sin que tengas que '
              'pensarlo.',
        sabias='Esta canción es de hace más de 200 años y va de poner el agua a hervir para el té. En '
               'Inglaterra la cantaban los niños cuando llegaba visita a casa, y hay una segunda parte '
               'que dice «quitadla otra vez, que ya se han ido todos».',
        qr=dict(titulo='Escúchala',
                texto='Marca solo dos golpes con el pie: un-dos, un-dos. Es más rápido que antes.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo aquí es el compás de dos golpes y que la melodía va en notas cortas. Ninguna '
              'tecla es nueva. Así que se empieza contando, y las notas vienen detrás.',
        reglas=['CUENTA UN-Y-DOS-Y', 'LOS SI, EN LA TECLA NEGRA', 'DESPACIO ANTES QUE RÁPIDO'],
        bloques=[
            dict(num=1, titulo='Primero, contar de dos en dos',
                 pista='dos golpes por compás · di “un-y-dos-y” en voz alta mientras tocas',
                 sistemas=[
                     dict(cap='a) una nota en cada golpe · esto es fácil, es solo para coger el paso',
                          events=[n('F4'), n('G4'), n('A4'), n('G4'),
                                  n('F4'), n('E4'), n('F4'), n('F4')],
                          bars=4),
                     dict(cap='b) y ahora dos notas en cada golpe · la segunda cae en la Y',
                          events=corch(['F4', 'G4']) + corch(['A4', 'G4']) +
                                 corch(['F4', 'E4']) + corch(['F4', 'G4']) + [n('F4', 'h')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='QUÉ ES ESO DE LA Y',
                 texto='Cuando en un golpe caben dos notas, la primera va en el número y la segunda '
                       'justo en medio, entre un número y el siguiente. Por eso se cuenta «un-y-dos-y»: '
                       'la Y es el sitio de la segunda nota. Si la dices siempre en el mismo momento, '
                       'las notas salen iguales solas.'),
            dict(num=2, titulo='La melodía del principio',
                 pista='medida en tu partitura · Sol · La · Sol · Fa · Mi · Do · Do',
                 sistemas=[
                     dict(cap='a) tal como está escrita, en notas cortas',
                          events=corch(['G4', 'A4']) + corch(['G4', 'F4']) +
                                 corch(['E4', 'C4']) + corch(['C4', 'E4']) + [n('C4', 'h')],
                          bars=4),
                     dict(cap='b) y las mismas notas en figuras largas, para verlas sin prisa',
                          events=[n('G4'), n('A4'), n('G4'), n('F4'),
                                  n('E4'), n('C4'), n('C4'), n('C4')],
                          bars=4, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda, con el bemol', clef='bass',
                 pista='andamio en Fa mayor · notas sueltas, una o dos por compás',
                 sistemas=[
                     dict(cap='a) una nota por compás · las letras de encima te avisan de cuándo cambia',
                          events=[n('F2', 'h'), n('C3', 'h'), n('F2', 'h'), n('C3', 'h')],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE SUBE DE VELOCIDAD',
                 texto='Toca la canción tan despacio que te salga entera sin parar ni una vez. Cuando '
                       'salga tres veces seguidas así, súbela un poquito. Un poquito de verdad, no el '
                       'doble. Si en algún momento tienes que parar, es que has subido demasiado: baja '
                       'otra vez y sigue desde ahí.'),
        ],
    ),

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='Polly Put the Kettle On · para hacer en casa',
             intro='Esta semana toca aprender a contar de dos en dos y a meter dos notas en cada '
                   'golpe.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='ojo con los Si: en esta canción son tecla negra',
                      notas=['G4', 'A4', 'F4', 'Bb4', 'E4', 'C5', 'D4', 'F4']),
                 dict(tipo='figuras', num=2, titulo='¿Cuántos golpes dura cada una?',
                      pista='acuérdate: aquí cada compás tiene solo dos golpes',
                      figuras=[('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                               ('h.', 'blanca con puntito')]),
                 dict(tipo='dibuja', num=3, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Fa', 'Sol', 'La', 'Si', 'La', 'Sol', 'Fa', 'Do']),
                 dict(tipo='colorea', num=4, titulo='Rodea todos los Si',
                      pista='en esta canción todos van en la tecla negra',
                      eventos=[n('F4'), n('A4'), n('Bb4'), n('A4'),
                               n('G4'), n('Bb4'), n('A4'), n('F4', 'h')],
                      leyenda=['El bemol del principio manda en toda la canción.',
                               'No lo van a repetir delante de cada Si: hay que acordarse.']),
                 rutina('Contar “un-y-dos-y” dando palmadas, sin piano',
                        'La melodía del principio, muy despacio',
                        'Subir un poquito la velocidad, solo si sale sin parar'),
                 juego('Da dos palmadas por compás mientras quien esté contigo cuenta «un-y-dos-y». '
                       'Después cambiad: tú cuentas y esa persona da palmadas en las Y, que es lo '
                       'difícil. Es el mismo trabajo que hacen tus dedos en esta canción.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='Polly Put the Kettle On · para hacer en casa',
             intro='Esta semana toca mirar la partitura con lápiz y subir la velocidad poco a poco.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('G4'), n('A4')], [n('G4'), n('F4')],
                                [n('G4'), n('A4')], [n('E4'), n('C4')]]),
                 dict(tipo='nombres', num=2, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['A4', 'C5', 'G4', 'Bb4', 'F4', 'D5', 'E4', 'A4']),
                 dict(tipo='une', num=3, titulo='Une cada cosa con lo que quiere decir',
                      pista='una raya de un punto al otro',
                      pares=[('El bemol del principio', 'dos golpes en cada compás'),
                             ('El 2 y el 4 de la clave', 'el nombre del acorde'),
                             ('Las letras de encima', 'todos los Si, tecla negra')]),
                 dict(tipo='colorea', num=4, titulo='Colorea las notas cortas',
                      pista='las que van unidas de dos en dos por una barra de arriba',
                      eventos=corch(['G4', 'A4']) + [n('G4'), n('F4')] +
                              corch(['E4', 'C4']) + [n('C4', 'h')],
                      leyenda=['Dos notas cortas juntas duran lo mismo que una negra.',
                               'Por eso hay que decirlas más deprisa, pero iguales entre sí.']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='Subir de velocidad no es tocar más deprisa a ver qué pasa: es tocar un '
                            'poquito más rápido SIN fallar. Si al subir empiezas a parar, no has '
                            'subido: has empeorado. Vuelve abajo y sube más despacio.'),
                 rutina('La canción entera muy despacio, sin parar',
                        'Un poquito más rápido, solo si la anterior salió tres veces',
                        'Contar “un-y-dos-y” en voz alta mientras tocas'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
