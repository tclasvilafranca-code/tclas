# -*- coding: utf-8 -*-
"""Polly Put the Kettle On (canción 9 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (mfiles.co.uk, arr. Jim
   Paterson, 1 pagina):

     - FA MAYOR: un bemol detras de la clave, o sea que todos los Si van en la
       tecla negra. Ya salio en la cancion 5.
     - Compas de **4/4**, cuatro golpes por compas. (Esta ficha dijo durante
       meses que era 2/4, y era falso: se ha vuelto a mirar el PDF a zoom y
       detras de la armadura hay un 4 sobre un 4. Un nino contando de dos una
       cancion que va de cuatro no puede tocarla bien.)
     - LO NUEVO de verdad: la melodia va en notas cortas casi todo el rato,
       corcheas seguidas, y hay que decir muchas notas seguidas sin acelerar.
     - Los dos primeros compases, medidos nota a nota sobre el PDF a 300 ppp
       (21 ago 2026). Los dos llevan el MISMO dibujo: cuatro corcheas unidas,
       dos corcheas unidas y una negra.
         c.1  Do · Re · Do · Si(b) · La · Fa · Fa     (Do5 Re5 Do5 Sib4 La4 Fa4 Fa4)
         c.2  Sol · La · Sol · Fa · Mi · Do · Do      (Sol4 La4 Sol4 Fa4 Mi4 Do4 Do4)
       El c.2 es el c.1 bajado una cuarta: misma forma, mas abajo. (La ficha
       decia antes que la cancion EMPEZABA por Sol-La-Sol-Fa-Mi-Do-Do: eso es
       el compas 2, no el 1. Se ha corregido midiendo.)
     - Encima vienen las letras de los acordes: F, B b, C, C7.
     - La izquierda va en blancas y negras, DOS O TRES notas por compas
       (c.1 dos blancas; c.4 negra, negra, blanca).
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         crucigrama, contar, unir, acuerdate, camino, adivinar,
                         rodear, teclado)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='Arnau', num=9, nivel='iniciación', slug='PollyKettle',
    formato='corto', titulo_corto='Polly Put the Kettle On',
    time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Polly Put the Kettle On.pdf'),
    yt='https://www.youtube.com/results?search_query=polly+put+the+kettle+on+piano',

    ficha=dict(
        titulo='Polly Put the Kettle On',
        autor='Canción popular · arr. Jim Paterson (mfiles)',
        datos=[('Novedad', 'Corre sin parar'), ('Teclas negras', 'Los Si'),
               ('Mano dcha.', 'Notas cortas'), ('Mano izq.', 'Notas largas'),
               ('Extras', 'Letras encima')],
        armonia=dict(
            titulo='La melodía corriendo, sin acelerar',
            tarjetas=[
                ('EL COMPÁS', 'Cuatro golpes',
                 'Un-dos-tres-cua. Lo que cambia no es el compás: son las notas, que van seguidas.'),
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
        pie_ritmos='Los dos primeros compases de la melodía, medidos en tu partitura. '
                   'Fíjate: el dibujo es el mismo dos veces.',
        ritmos=[
            ('COMPÁS 1', 'seis notas cortas y una larga',
             corch(['C5', 'D5', 'C5', 'Bb4'], 4) + corch(['A4', 'F4']) + [n('F4')],
             AZUL, 'treble', FA),
            ('COMPÁS 2', 'el mismo dibujo, más abajo',
             corch(['G4', 'A4', 'G4', 'F4'], 4) + corch(['E4', 'C4']) + [n('C4')],
             AZUL, 'treble', FA),
        ],
        especial=[
            'Hay UN BEMOL detrás de la clave: todos los Si van en la tecla negra.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cua.',
            'La melodía va casi toda en notas cortas, de dos en dos.',
            'Encima del pentagrama hay letras: son los acordes, no notas.',
            'La izquierda va en notas largas: dos o tres por compás.',
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
                texto='Marca cuatro golpes con el pie: un-dos-tres-cua, sin correr.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo aquí es que la melodía va en notas cortas seguidas. Ninguna '
              'tecla es nueva. Así que se empieza contando, y las notas vienen detrás.',
        reglas=['CUENTA UN-Y-DOS-Y-TRES-Y-CUA-Y', 'LOS SI, EN LA TECLA NEGRA',
                'DESPACIO ANTES QUE RÁPIDO'],
        bloques=[
            dict(num=1, titulo='Primero, contar los cuatro golpes',
                 pista='cuatro golpes por compás · di “un-y-dos-y-tres-y-cua-y” mientras tocas',
                 sistemas=[
                     dict(cap='a) una nota en cada golpe · esto es fácil, es solo para coger el paso',
                          events=[n('F4'), n('G4'), n('A4'), n('G4'),
                                  n('F4'), n('E4'), n('F4'), n('F4')],
                          bars=2),
                     dict(cap='b) y ahora dos notas en cada golpe · la segunda cae en la Y',
                          events=corch(['F4', 'G4']) + corch(['A4', 'G4']) +
                                 corch(['F4', 'E4']) + corch(['F4', 'G4']) + [n('F4', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='QUÉ ES ESO DE LA Y',
                 texto='Cuando en un golpe caben dos notas, la primera va en el número y la segunda '
                       'justo en medio, entre un número y el siguiente. Por eso se cuenta «un-y-dos-y»: '
                       'la Y es el sitio de la segunda nota. Si la dices siempre en el mismo momento, '
                       'las notas salen iguales solas.'),
            dict(num=2, titulo='La melodía del principio',
                 pista='medida en tu partitura · Do · Re · Do · Si · La · Fa · Fa',
                 # Las siete notas de cada compás, pero estiradas en figuras
                 # largas: aquí se trata de VERLAS, no de correr. Tal como
                 # están escritas de verdad salen en la ficha, y repetirlas
                 # aquí seria imprimir dos veces el mismo compás.
                 sistemas=[
                     dict(cap='a) las notas del compás 1, estiradas · el Si va en la tecla negra',
                          events=[n('C5'), n('D5'), n('C5'), n('Bb4'),
                                  n('A4'), n('F4'), n('F4', 'h')],
                          bars=2),
                     dict(cap='b) y las del compás 2, que son el mismo dibujo más abajo',
                          events=[n('G4'), n('A4'), n('G4'), n('F4'),
                                  n('E4'), n('C4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda, con el bemol', clef='bass',
                 pista='andamio en Fa mayor · notas largas, siguiendo las letras',
                 sistemas=[
                     # Antes eran Fa · Do · Fa · Do, que es exactamente lo que hace
                     # la izquierda de The Wheels on the Bus: el mismo andamio en
                     # dos piezas del mismo alumno. Ahora sigue las LETRAS que la
                     # edición imprime encima (F · B♭ · C · F), que además es lo
                     # que la frase dice que hay que mirar.
                     dict(cap='a) una nota por compás, siguiendo las letras impresas · F · B♭ · C · F',
                          events=[n('F2', 'w'), n('Bb2', 'w'), n('C3', 'w'), n('F2', 'w')],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE SUBE DE VELOCIDAD',
                 texto='Toca la canción tan despacio que te salga entera sin parar ni una vez. Cuando '
                       'salga tres veces seguidas así, súbela un poquito. Un poquito de verdad, no el '
                       'doble. Si en algún momento tienes que parar, es que has subido demasiado: baja '
                       'otra vez y sigue desde ahí.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R17 (crucigrama · cuenta · une) y
    # semana 2 la R18 (camino · adivina · rodea · teclado · escribe).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Polly Put the Kettle On · para hacer en casa',
            intro='Lo nuevo: muchas notas cortas seguidas. Hay que decir más '
                  'notas en menos sitio.',
            bloques=[
                crucigrama('CORTAS', [
                    ('COMPAS', 0, 'El trozo que hay entre dos rayas de arriba abajo.'),
                    ('SOL', 1, 'La primera nota de la melodía de esta canción.'),
                    ('NEGRA', 3, 'La figura que dura un golpe entero.'),
                    ('PUNTILLO', 3, 'El puntito que le añade la mitad a una figura.'),
                    ('BLANCA', 5, 'La figura hueca que dura dos golpes.'),
                    ('MANOS', 4, 'Tienes dos, y las dos tocan.'),
                ], cierre='Las casillas grises dicen cómo son las notas de esta canción.'),
                contar([n('G4'), n('A4'), n('G4'), n('F4'), n('E4'), n('C4'), n('C4')],
                       ['¿Cuántos Do hay?', '¿Cuántas veces sale el Sol?',
                        '¿Cuántas notas hay en total?'],
                       titulo='Cuenta lo que ves',
                       pista='es el compás 2 de tu canción, medido en la partitura'),
                unir([('El bemol del principio', 'cuatro golpes en cada compás'),
                      ('El 4/4 de después de la clave', 'la mitad de una negra'),
                      ('Una corchea', 'todos los Si van en la tecla negra'),
                      ('Las letras F, B♭, C de arriba', 'el nombre del acorde que suena')],
                     titulo='Une cada cosa con lo que significa',
                     pista='están desordenadas · una raya de un punto al otro'),
                rutina('Sol · La · Sol · Fa, contando un-y-dos-y',
                       'La melodía entera muy despacio, buscando los Si',
                       'Las dos manos, cuatro compases'),
                acuerdate('Pasan muy seguidas y engañan. Cuenta “un-y-dos-y-tres-y-cua-y”.',
                          etiqueta='NOTAS CORTAS NO ES IR DEPRISA'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Polly Put the Kettle On · para hacer en casa',
            intro='Segunda semana: un camino de notas cortas, adivinanzas y el teclado.',
            bloques=[
                camino([['negra', 'corchea', 'negra', 'blanca', 'negra', 'negra'],
                        ['negra', 'corchea', 'corchea', 'negra', 'blanca', 'negra'],
                        ['blanca', 'negra', 'corchea', 'negra', 'negra', 'corchea'],
                        ['negra', 'negra', 'corchea', 'corchea', 'negra', 'blanca'],
                        ['negra', 'blanca', 'negra', 'corchea', 'negra', 'negra']],
                       titulo='El camino de las notas cortas',
                       pista='colorea solo las que valen medio golpe y sale un camino'),
                adivinar([('Valgo medio golpe y voy casi siempre acompañada.', 'CORCHEA'),
                          ('Somos cuatro en cada compás de esta canción.', 'GOLPES'),
                          ('Estoy al principio y mando en todos los Si.', 'BEMOL')],
                         titulo='Adivina quién soy',
                         pista='una letra en cada casilla'),
                rodear([[n('G4'), n('A4')], [n('G4'), n('F4')],
                        [n('G4'), n('A4')], [n('E4'), n('C4')]],
                       titulo='Rodea los dos grupos que son iguales',
                       pista='son parejas de notas cortas de tu canción · míralas de una en una'),
                teclado({0: 1, 2: 2, 4: 3, 6: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'La número 4 es un Si: en esta canción se toca en la tecla negra de al lado.'],
                        titulo='En el teclado',
                        pista='ojo con la número 4'),
                escribir(titulo='Copia aquí un compás de tu canción',
                         pista='el que más te cueste · cópialo tal cual y tócalo cinco veces'),
                rutina('La melodía entera, contando un-y-dos-y',
                       'Los compases con notas cortas, un poco más rápido cada día',
                       'Las dos manos, sin parar aunque haya fallos'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
