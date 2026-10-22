# -*- coding: utf-8 -*-
"""Soldadito de Hierro (canción 11 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico); el material medido se
   importa de `dilan_11_soldadito`. Ver TRANSCRIPCION_D09_11.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por la IZQUIERDA, que es lo cómodo: una quinta en
       redonda por compás que no cambia de gesto en toda la pieza.
     - A Eva se le entra por el TRESILLO, que es la dificultad de verdad y la
       razón por la que esta pieza está donde está en su álbum. Empezar por lo
       fácil tiene sentido cuando hace falta confianza; cuando lo que hace
       falta es resolver un problema concreto, se empieza por el problema. La
       izquierda llega en el paso 3, y llega en cinco minutos.

   El ritmo real de la derecha va en tresillos y el motor no los escribe: se
   dice en cada bloque que lo cita.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloque_tresillos, bloques_extra
from dilan_11_soldadito import (n, ac, corch, QUINTAS, MEL_1, MEL_2, MEL_3)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eva', num=11, nivel='avanzado', slug='Soldadito',
    titulo_corto='Soldadito de Hierro', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'SOLDADITO DE HIERRO _ Nil Moliner.pdf'),
    yt='https://www.youtube.com/results?search_query=nil+moliner+soldadito+de+hierro',

    ficha=dict(
        titulo='Soldadito de Hierro',
        autor='Nil Moliner (2019) · arr. musicaparadisfrutar.com',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Ritmo', 'Tresillos'),
               ('Mano izq.', 'Quintas vacías'), ('Mano dcha.', 'Melodía cantada')],
        armonia=dict(
            titulo='Lo difícil no está en las notas',
            tarjetas=[
                ('EL TRESILLO', 'Tres en un tiempo',
                 'Va de principio a fin. Es el motor de la canción y lo único que hay que estudiar.'),
                ('LA IZQUIERDA', 'Una por compás',
                 'Do · Rem · Sol · Do · Fa · Sol · Fa, en redondas. No cambia de gesto ni una vez.'),
                ('LAS QUINTAS VACÍAS', 'Sin tercera',
                 'Falta la nota que decide mayor o menor. Por eso suena hueco, y es a propósito.'),
                ('LOS CC. 15–24', 'Ya te los sabes',
                 'Son nota por nota los cc. 4 al 13. Comprobado compás a compás.'),
            ],
            pie='Es una canción con muy pocas notas distintas y un problema rítmico enorme. Por eso '
                'aquí se estudia al revés de lo habitual: primero el ritmo, sin notas; después las '
                'notas; y la izquierda, que es lo cómodo, la última.',
        ),
        ritmos=[
            ('MD', 'la melodía real va en tresillos · aquí en corcheas, para leerla',
             corch(['G4', 'G4', 'G4', 'F4', 'E4', 'D4', 'E4', 'C4']), AZUL, 'treble', None),
            ('MI', 'una quinta vacía en redonda: se ataca y ya',
             [ac(('C3', 'G3'))], OCRE, 'bass', None),
        ],
        especial=[
            'No hay armadura: la pieza está en Do mayor.',
            'La izquierda toca DOS notas a la vez, siempre a distancia de quinta.',
            'La derecha va casi entera en tresillos, marcados con un 3.',
            'La edición trae la letra debajo del pentagrama.',
            'Los cc. 15 al 24 repiten exactamente los cc. 4 al 13.',
            'La melodía no acaba la primera frase en la tónica: por eso la canción sigue.',
        ],
        reto='El tresillo. No es difícil de entender —tres notas donde normalmente van dos— pero sí de '
             'mantener: en cuanto te despistas se convierte en dos corcheas y un silencio, y la canción '
             'pierde el balanceo que la hace ser lo que es.',
        truco='Deja el piano un momento y canta la letra en voz alta con el pie marcando los cuatro '
              'tiempos. Los tresillos están escritos donde la frase cantada los pide, no por capricho: '
              'si cantas bien, ya los estás haciendo. Después toca exactamente lo que has cantado.',
        sabias='Nil Moliner era maestro de escuela antes de dedicarse a la música, y la escribió '
               'pensando en la gente que aguanta callada. El título viene del soldadito de plomo de '
               'Andersen, que se mantiene de pie con una sola pierna hasta el final.',
        qr=dict(titulo='Escucha la original',
                texto='Marca los cuatro tiempos con el pie y cuenta tres notas en cada uno.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Aquí se empieza por el problema, no por lo cómodo. El problema de esta canción es el '
              'tresillo: aparece en el primer compás y no se va hasta el último. Las notas son pocas y '
              'la izquierda es un regalo, así que si el ritmo está resuelto, la pieza está resuelta.',
        reglas=['PRIMERO EL RITMO, DESPUÉS LAS NOTAS', 'TRES POR CADA GOLPE DEL PIE', 'SIN ACELERAR EN LA BARRA'],
        bloques=[
            dict(num=1, titulo='El tresillo, antes que ninguna nota de la pieza',
                 pista='andamio rítmico en Do mayor · tres notas por tiempo, y el pie marcando cuatro',
                 sistemas=[
                     # Este sistema ENSENABA el tresillo y lo escribia en corcheas.
                     # El Soldadito lleva los tresillos marcados con un 3 de
                     # principio a fin —se ven en la primera linea del PDF— y Eva,
                     # cuyo dosier entra por el tresillo porque es LA dificultad de
                     # la pieza, no veia ninguno dibujado en todo su cuaderno.
                     dict(cap='a) así se escribe: TRES notas dentro de un solo golpe, con su 3 encima · '
                              'di “un-dos-tres” en cada grupo y que las tres duren igual',
                          events=[{'pitch': 'C4', 'dur': 'e', 'tresillo': 60, 'beam': 7260}, {'pitch': 'D4', 'dur': 'e', 'tresillo': 60, 'beam': 7260}, {'pitch': 'E4', 'dur': 'e', 'tresillo': 60, 'beam': 7260}, {'pitch': 'D4', 'dur': 'e', 'tresillo': 61, 'beam': 7261}, {'pitch': 'C4', 'dur': 'e', 'tresillo': 61, 'beam': 7261}, {'pitch': 'B3', 'dur': 'e', 'tresillo': 61, 'beam': 7261}, {'pitch': 'C4', 'dur': 'e', 'tresillo': 62, 'beam': 7262}, {'pitch': 'D4', 'dur': 'e', 'tresillo': 62, 'beam': 7262}, {'pitch': 'E4', 'dur': 'e', 'tresillo': 62, 'beam': 7262}, {'pitch': 'F4', 'dur': 'e', 'tresillo': 63, 'beam': 7263}, {'pitch': 'E4', 'dur': 'e', 'tresillo': 63, 'beam': 7263}, {'pitch': 'D4', 'dur': 'e', 'tresillo': 63, 'beam': 7263}],
                          bars=1),
                     dict(cap='b) y ahora la OTRA figura de la pieza, la semicorchea · cuatro por '
                              'golpe, que es donde la letra corre · el pie sigue marcando cuatro',
                          events=[{'pitch': 'G4', 'dur': 's', 'beam': 9820}, {'pitch': 'F4', 'dur': 's', 'beam': 9820}, {'pitch': 'E4', 'dur': 's', 'beam': 9820}, {'pitch': 'D4', 'dur': 's', 'beam': 9820}, {'pitch': 'C4', 'dur': 's', 'beam': 9821}, {'pitch': 'D4', 'dur': 's', 'beam': 9821}, {'pitch': 'E4', 'dur': 's', 'beam': 9821}, {'pitch': 'F4', 'dur': 's', 'beam': 9821}, {'pitch': 'G4', 'dur': 's', 'beam': 9822}, {'pitch': 'A4', 'dur': 's', 'beam': 9822}, {'pitch': 'G4', 'dur': 's', 'beam': 9822}, {'pitch': 'F4', 'dur': 's', 'beam': 9822}, {'pitch': 'E4', 'dur': 's', 'beam': 9823}, {'pitch': 'D4', 'dur': 's', 'beam': 9823}, {'pitch': 'C4', 'dur': 's', 'beam': 9823}, {'pitch': 'D4', 'dur': 's', 'beam': 9823}],
                          bars=1, show_time=False),
                     dict(cap='c) y con un silencio detrás · el tresillo cuesta el doble cuando hay que '
                              'parar y volver a entrar a tiempo, y en esta canción pasa todo el rato',
                          events=[{'pitch': 'C4', 'dur': 'e', 'tresillo': 70, 'beam': 7270}, {'pitch': 'D4', 'dur': 'e', 'tresillo': 70, 'beam': 7270}, {'pitch': 'E4', 'dur': 'e', 'tresillo': 70, 'beam': 7270}, {'rest': True, 'dur': 'q'}, {'pitch': 'G4', 'dur': 'e', 'tresillo': 80, 'beam': 7280}, {'pitch': 'F4', 'dur': 'e', 'tresillo': 80, 'beam': 7280}, {'pitch': 'E4', 'dur': 'e', 'tresillo': 80, 'beam': 7280}, {'rest': True, 'dur': 'q'}],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL TRESILLO SE APRENDE SIN LA PIEZA',
                 texto='Si intentas aprender el tresillo leyendo a la vez las notas de la canción, estás '
                       'haciendo dos cosas difíciles al mismo tiempo y no sabrás cuál de las dos te está '
                       'fallando. Aquí las notas son de andamio y son fáciles a propósito: lo único que '
                       'se entrena es que quepan tres en cada golpe del pie y que el golpe no cambie de '
                       'velocidad. Cuando eso salga solo, las notas de verdad entran sin pelea.'),
            dict(num=2, titulo='Y ahora sí, la melodía de la canción',
                 pista='cc. 1–3 · las alturas son las de la partitura; el ritmo va simplificado a corcheas',
                 sistemas=[
                     dict(cap='a) cc. 1–2 · en la partitura esto va en tresillos: léelo aquí y cuéntalo '
                              'como en el paso 1',
                          events=MEL_1 + MEL_2, bars=2),
                     dict(cap='b) el c. 3, que cierra la frase · fíjate en que no acaba en Do: por eso '
                              'la canción no puede parar ahí',
                          events=MEL_3 + [n('D4', 'w')], bars=2, show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Lo difícil ya está hecho. Lo que queda es la izquierda —que se aprende en cinco minutos y '
              'no vuelve a cambiar— y darse cuenta de que media canción está escrita dos veces.',
        reglas=['LAS DOS NOTAS, A LA VEZ', 'LOS CC. 15–24 SON LOS CC. 4–13', 'CANTA LA LETRA'],
        bloques=[
            dict(num=3, titulo='La izquierda, que es el regalo de esta pieza', clef='bass',
                 pista='cc. 1–7 medidos · ataca, suelta el brazo y no vuelvas a tocar hasta el compás siguiente',
                 sistemas=[
                     dict(cap='a) cc. 1–7 · Do · Rem · Sol · Do · Fa · Sol · Fa, una redonda doble por compás',
                          events=QUINTAS, bars=7, clef='bass'),
                     dict(cap='b) y los doce primeros compases sin parar · es lo que vas a tocar treinta '
                              'veces: tiene que salir sin mirarte la mano',
                          events=[ac(('C3', 'G3')), ac(('D3', 'A3')), ac(('G2', 'D3')),
                                  ac(('C3', 'G3')), ac(('F2', 'C3')), ac(('G2', 'D3')),
                                  ac(('F2', 'C3')), ac(('C3', 'G3')), ac(('G2', 'D3')),
                                  ac(('A2', 'E3')), ac(('F2', 'C3')), ac(('C3', 'G3'))],
                          bars=6, clef='bass', show_time=False),
                     dict(cap='c) y solo la nota de abajo de cada quinta · Do · Re · Sol · Do · Fa · '
                              'Sol · Fa: ese es el recorrido de la canción entera, en siete notas',
                          events=[n(p, 'w') for p in ('C3', 'D3', 'G2', 'C3', 'F2', 'G2', 'F2')],
                          bars=7, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SUENA HUECO',
                 texto='Las dos notas de la izquierda están siempre a distancia de quinta, y eso quiere '
                       'decir que falta la tercera: la nota que decide si un acorde es mayor o menor. Sin '
                       'ella el acorde no dice nada, solo sostiene. Es una decisión del arreglo, no una '
                       'simplificación: si le pones la tercera, la canción se vuelve dulce y deja de '
                       'sonar a lo que suena. Pruébalo una vez y luego déjalo como está.'),
            dict(num=4, titulo='La letra, que manda sobre el ritmo',
                 pista='sin pentagrama y sin piano a propósito: cantando, que es como se aprende un tresillo',
                 sistemas=[]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4, Y LOS DIEZ COMPASES REGALADOS',
                 texto='Canta “Me mue-ro al pen-sar que al-gún dí-a…” en voz alta, sin tocar, con el pie '
                       'marcando cuatro. Los tresillos están puestos donde la frase cantada los pide, así '
                       'que si cantas bien ya los estás haciendo; después toca exactamente lo que has '
                       'cantado. Y coge un lápiz: los cc. 15 al 24 son, nota por nota, los cc. 4 al 13. '
                       'Escribe al lado del c. 15 “= c. 4” y cuando llegues ahí no leas, toca de memoria.'),
            dict(tipo='escalera', valores=[52, 60, 66, 72, 78, 84],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 71, 'C4', 'C3',
    'la mano en Do antes de los grupos de tres',
    desde=6, time_sig=(4, 4)) + [
    bloque_tresillos('Do mayor', 5, 'C4', 'los tresillos de la melodía', time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
