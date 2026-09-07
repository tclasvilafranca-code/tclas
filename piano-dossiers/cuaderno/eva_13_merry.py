# -*- coding: utf-8 -*-
"""Have Yourself a Merry Little Christmas (canción 13 de Eva, avanzado).

   Misma edición que la de Dilan (sha256 idéntico); el material medido se
   importa de `dilan_18_merry`. Ver TRANSCRIPCION_D18_20.md.

   Camino distinto al de Dilan:

     - A Dilan se le construye la pieza DE ABAJO ARRIBA: el bajo, el oom-pah,
       la melodía, y al final las tres capas juntas.
     - A Eva se le da primero LA PIEZA ENTERA REDUCIDA A UN GOLPE POR COMPÁS,
       melodía incluida, para que decida los volúmenes ANTES de tener nada que
       tocar deprisa. En una pieza cuya única dificultad es el equilibrio entre
       tres capas, decidir el equilibrio al final —cuando las manos ya están
       ocupadas— es decidirlo mal. El detalle (el oom-pah, las corcheas de la
       melodía) llega después, y llega sabiendo a qué volumen va cada cosa.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_18_merry import n, ac, corch, oompah, DO, FA, SOL, LAm

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eva', num=13, nivel='avanzado', slug='MerryLittleChristmas',
    titulo_corto='Have Yourself a Merry Little Christmas', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'have-yourself-a-merry-little-christmas.pdf'),
    yt='https://www.youtube.com/results?search_query=have+yourself+a+merry+little+christmas',

    ficha=dict(
        titulo='Have Yourself a Merry Little Christmas',
        autor='Hugh Martin y Ralph Blane (1944) · arr. para piano',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Carácter', 'Lento y cantado'),
               ('Mano izq.', 'Bajo y acorde'), ('Capas', 'Tres')],
        armonia=dict(
            titulo='Tres capas, y hay que decidir el volumen de cada una',
            tarjetas=[
                ('CAPA 1 · EL BAJO', 'Con peso de brazo',
                 'La nota grave de cada compás. Si esa línea suena bien, la canción suena bien.'),
                ('CAPA 2 · EL ACORDE', 'Casi sin dedo',
                 'Cae entre bajo y bajo. Es relleno: en cuanto se oye igual que el bajo, estorba.'),
                ('CAPA 3 · LA MELODÍA', 'Por encima de todo',
                 'La única que el oyente sigue. Va en la derecha y tiene que ganar siempre.'),
                ('LAS ALTERACIONES', 'Escritas a mano',
                 'No hay armadura: cada sostenido está puesto uno a uno, y son el color de la pieza.'),
            ],
            pie='Aquí no hay ningún pasaje difícil de dedos. Toda la dificultad es de oído: tres cosas '
                'sonando a la vez y tú decidiendo cuánto suena cada una. Por eso este cuaderno empieza '
                'por la pieza entera reducida, y no por el acompañamiento.',
        ),
        ritmos=[
            ('MI', 'bajo y acorde, dos veces por compás',
             oompah('D3', SOL), OCRE, 'bass', None),
            ('MD', 'la melodía baja despacio y se queda quieta',
             [n('G4', 'h'), n('D4', 'h')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay armadura: la pieza está en Do mayor.',
            'Cada sostenido y cada bemol están escritos a mano, uno por uno.',
            'La izquierda toca nota grave y acorde, dos veces por compás.',
            'Los cc. 2 y 6 son idénticos: la misma frase vuelve.',
            'La melodía de los cc. 3–4 baja desde el Re5 y se queda en La.',
            'Está en la tonalidad más neutra que existe y aun así suena melancólica.',
        ],
        reto='El equilibrio. Melodía fuerte, bajo con cuerpo y acorde casi inaudible, todo a la vez y '
             'con las dos manos ocupadas. No es un problema de dedos: es un problema de oírse, y por eso '
             'cuesta más de lo que parece en una pieza tan lenta.',
        truco='Decide los volúmenes ANTES de poder tocarla entera. Toca la pieza reducida a un acorde '
              'por compás con la melodía encima, muy lento, y en cada pasada escucha una sola capa. '
              'Cuando el equilibrio esté decidido, el oom-pah se pone debajo sin discutir.',
        sabias='La letra original de 1944 era mucho más triste —decía “puede que esta sea la última '
               'Navidad juntos”— y Judy Garland pidió que la cambiaran porque le parecía demasiado dura '
               'para la escena. La versión que conocemos es la suavizada, y aun así sigue sonando así.',
        qr=dict(titulo='Escucha la original',
                texto='Escucha solo el acompañamiento. Verás que casi no está.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Esta pieza no tiene ni un pasaje difícil de dedos: lo difícil es que suenen tres capas a '
              'la vez con tres volúmenes distintos. Por eso se empieza por la canción entera reducida a '
              'un golpe por compás — así se decide el equilibrio cuando todavía tienes oreja libre, y no '
              'al final, con las manos llenas.',
        reglas=['PRIMERO EL EQUILIBRIO, DESPUÉS EL DETALLE', 'EL ACORDE, CASI SIN DEDO', 'MUY LENTO'],
        bloques=[
            dict(num=1, titulo='La canción a un golpe por compás', clef='bass',
                 pista='cc. 1–8 · un acorde por compás y la derecha encima: así se oye el conjunto',
                 sistemas=[
                     dict(cap='a) cc. 1–4 · un solo acorde por compás, y pon la melodía encima aunque '
                              'sea muy despacio: lo que se está probando es si se oye por arriba',
                          events=[ac(('D3', 'G3', 'B3'), 'w'), ac(('C3', 'E3', 'G3'), 'w'),
                                  ac(('D3', 'F3', 'A3'), 'w'), ac(('E3', 'A3', 'C4'), 'w')],
                          pedal=4,
                          bars=4, clef='bass'),
                     dict(cap='b) cc. 5–8 · lo mismo con la segunda frase',
                          events=[ac(('F2', 'A2', 'C3'), 'w'), ac(('E3', 'A3', 'C4'), 'w'),
                                  ac(('G2', 'B2', 'D3'), 'w'), ac(('C3', 'E3', 'G3'), 'w')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y ahora solo la nota grave de cada compás · si esta línea sola ya '
                              'suena a la canción, es que el bajo está bien elegido de volumen',
                          events=[n('D3', 'w'), n('C3', 'w'), n('D3', 'w'), n('E3', 'w'),
                                  n('D3', 'w'), n('C3', 'w'), n('D3', 'w'), n('C3', 'w')],
                          bars=8, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='TRES CAPAS, TRES VOLÚMENES, Y EN ESTE ORDEN',
                 texto='La melodía manda siempre. El bajo va debajo, con peso de brazo, porque es lo que '
                       'sostiene la armonía. Y el acorde de en medio es relleno: tiene que oírse lo justo '
                       'para que la armonía exista y ni un pelo más. La prueba: toca los cc. 1–4 tres '
                       'veces y en cada pasada escucha una sola capa. Si en alguna pasada no encuentras '
                       'la capa que buscabas, ya sabes cuál hay que subir o bajar.'),
            dict(num=2, titulo='Y ahora el detalle: el oom-pah', clef='bass',
                 pista='cc. 1–8 · el bajo con peso de brazo y el acorde casi sin dedo',
                 sistemas=[
                     dict(cap='a) cc. 1–4 · bajo y acorde, dos veces por compás · si los dos suenan '
                              'igual, la melodía se pierde',
                          events=oompah('D3', SOL) + oompah('C3', DO) +
                                 oompah('D3', ('F3', 'A3', 'D4')) + oompah('E3', LAm),
                          bars=4, clef='bass'),
                     dict(cap='b) y los cc. 5–8 · cuando esto salga sin mirarte la mano, pon la derecha '
                              'encima y no antes',
                          events=oompah('F2', FA) + oompah('E3', LAm) +
                                 oompah('G2', SOL) + oompah('C3', DO),
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y el c. 2 aparte, que es también el c. 6 · está medido: son idénticos, '
                              'así que apréndete uno y tienes los dos',
                          events=oompah('C3', DO) * 2, bars=2, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='El equilibrio está decidido y el acompañamiento montado. Queda la melodía, que se coloca '
              'sola cantando la letra, y el lápiz: las alteraciones de esta canción están escritas una a '
              'una y son las que hacen que suene a lo que suena.',
        reglas=['MARCA LAS ALTERACIONES CON LÁPIZ', 'CANTA LA LETRA', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='La melodía, frase por frase',
                 pista='cc. 1–4 medidos · “Have your-self a mer-ry lit-tle Christ-mas”',
                 sistemas=[
                     dict(cap='a) cc. 1–2 · canta la letra mientras la lees y verás dónde respira la frase',
                          events=corch(['G4', 'F4', 'E4', 'D4']) + [n('A3'), n('C4')] +
                                 corch(['C4', 'E4', 'G4', 'C5']) + [n('C5'), n('G4')],
                          bars=2),
                     dict(cap='b) cc. 3–4 · baja desde el Re5 y se queda en La · es la respuesta a los '
                              'dos primeros: tiene que sonar más floja, no más fuerte',
                          events=corch(['D5', 'C5', 'B4', 'A4']) + [n('G4'), n('F4')] +
                                 [n('E4'), n('C5'), n('B4'), n('A4')],
                          bars=2, show_time=False),
                     dict(cap='c) y solo las notas donde la melodía cambia de dirección · seis notas, '
                              'y ese es el dibujo entero de la frase',
                          events=[n('G4', 'h'), n('C4', 'h'), n('C5', 'h'),
                                  n('D5', 'h'), n('A4', 'h'), n('E4', 'h'),
                                  n('A4', 'w')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA CANCIÓN SE PONE TRISTE',
                 texto='Está en Do mayor, la tonalidad más neutra que existe, y sin embargo suena '
                       'melancólica. El truco está en los acordes con alteraciones: el arreglista mete '
                       'notas que no pertenecen a Do mayor y que tiran hacia abajo. Cuando llegues a uno '
                       'de ellos, no lo toques más fuerte: tócalo más lento. Esa clase de acorde pide '
                       'tiempo, no volumen.'),
            dict(num=4, titulo='Las tres capas, ahora de verdad',
                 pista='sin pentagrama a propósito: se hace sobre la partitura de la página 1, muy lento',
                 sistemas=[]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4, Y EL LÁPIZ',
                 texto='Toca los cc. 1 al 4 muy lento y en cada pasada escucha UNA sola cosa: ¿se oye la '
                       'melodía por encima de todo?, ¿se oye el bajo con cuerpo?, ¿se oye el acorde de en '
                       'medio más de lo que debería? Tres pasadas, tres respuestas, y ya sabes qué '
                       'corregir. Y antes de nada, el lápiz: esta canción no tiene armadura, así que cada '
                       'sostenido y cada bemol están puestos uno a uno por el arreglista y son justo los '
                       'que le dan el color. Rodéalos todos: es el ejercicio más rentable de la semana.'),
            dict(tipo='nota',
                 etiqueta='EL PEDAL, QUE AQUÍ DECIDE SI SUENA A JAZZ O A VILLANCICO',
                 texto='El pedal cambia cuando cambia el acorde, y en esta canción el acorde cambia casi '
                       'cada compás: uno por compás, pisando justo DESPUÉS de tocar el bajo nuevo. Si lo '
                       'dejas puesto de más, las alteraciones escritas a mano se mezclan con las del '
                       'compás anterior y el color se convierte en barro. Y si no lo usas, el bajo se '
                       'queda corto y la canción suena a ejercicio. Cámbialo tarde y limpio.'),
            dict(tipo='escalera', valores=[44, 50, 56, 62, 68, 74],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
