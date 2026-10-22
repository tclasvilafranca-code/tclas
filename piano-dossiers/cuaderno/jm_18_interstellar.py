# -*- coding: utf-8 -*-
"""Interstellar — pieza 18 de José María. Formato ADULTO. RETO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Hans Zimmer,
   Campamento Musical Bye Bye Beethoven, 6 páginas):

     - Detrás de la clave NO HAY armadura.
     - Compás de 3/4 y ♩ = 96 impreso. Pone "p" al principio.
     - La digitación viene impresa desde el primer compás (3 y 1).
     - SON SEIS PÁGINAS: es, con diferencia, la pieza más larga del cuaderno.

   Por qué está aquí: por la longitud. La música de Zimmer funciona por
   repetición y acumulación, así que el material se repite muchísimo — pero
   seis páginas siguen siendo seis páginas, y eso es un problema de cabeza,
   no de dedos.

   El dosier ACOTA el trabajo a las DOS primeras páginas y lo dice en el
   objetivo. Y manda hacer antes el mapa de la pieza con lápiz: en una pieza
   por repetición, saber qué se repite es literalmente la mitad del trabajo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import encajar
from jm_comun import (n, ac, sil, corch, plan, teclado, inventa, rodear,
                      metronomo, para_clase, escalera)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=18, nivel='iniciación',
    slug='Interstellar', formato='adulto',
    titulo_corto='Interstellar', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'Interstellar _ .pdf'),
    yt='https://www.youtube.com/results?search_query=interstellar+piano+easy',

    ficha=dict(
        titulo='Interstellar',
        autor='Hans Zimmer · arreglo del Campamento Musical Bye Bye Beethoven',
        datos=[('Compás', '3/4'), ('Tempo', '♩ = 96'),
               ('Páginas', 'Seis'), ('Esta semana', 'Las dos primeras'),
               ('Dedos', 'Escritos')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio: el dibujo es el de tu partitura y las notas exactas están allí. Lo '
                   'literal es que la pieza funciona por repetición.',
        armonia=dict(
            titulo='Seis páginas que se repiten muchísimo',
            tarjetas=[
                ('LA LONGITUD', 'Seis páginas',
                 'La pieza más larga de todo tu cuaderno. Esta semana son las dos primeras, y no es '
                 'una rebaja: es como se estudia algo así.'),
                ('CÓMO ESTÁ HECHA', 'Por capas',
                 'Zimmer construye repitiendo un dibujo corto y añadiendo cosas encima. Por eso hay '
                 'seis páginas y no seis páginas de material.'),
                ('LO PRIMERO', 'El mapa',
                 'Antes de tocar: numerar los compases y marcar con colores qué se repite. En esta '
                 'pieza eso ahorra la mitad del trabajo.'),
                ('EL CARÁCTER', 'p, y 3/4',
                 'Empieza flojito y en tres tiempos. No es una pieza de fuerza: es de paciencia y de '
                 'sonido sostenido.'),
            ],
            pie='Cuando una pieza se construye repitiendo, la partitura larga engaña. Lo que hay que '
                'aprender casi siempre cabe en una página; el resto es reconocer lo que ya sabes y no '
                'perder el sitio.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el dibujo corto que se repite · andamio',
             [n('C4'), n('E4'), n('G4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'sostiene el compás entero · andamio',
             [n('C3', 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay armadura.',
            'Compás de 3/4, y pone ♩ = 96.',
            'Pone "p" al principio: se empieza flojito.',
            'La digitación viene impresa desde el primer compás.',
            'Son SEIS páginas: la pieza más larga del cuaderno.',
            'El trabajo de esta semana son las DOS primeras páginas.',
        ],
        reto='No perder el sitio. Con seis páginas de material parecido, lo que falla no es tocar: es '
             'saber en qué compás estás cuando llevas dos minutos.',
        truco='Numera todos los compases a lápiz, del 1 al final, y marca con colores los grupos que se '
              'repiten. Después aprende de memoria SOLO los sitios donde cambia algo. Cuando toques, '
              'no vas leyendo nota a nota: vas reconociendo bloques, que es lo que hace un músico con '
              'una pieza larga.',
        sabias='Zimmer compuso la música antes de que hubiera guion: Nolan le dio un sobre con una '
               'página sobre un padre y su hija, sin decirle que era una película del espacio. Lo que '
               'escribió con eso es el tema que estás tocando.',
        qr=dict(titulo='Escúchala',
                texto='Escucha los tres primeros minutos y cuenta cuántas veces vuelve el mismo dibujo '
                      'de notas. Esa es la pieza entera.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Con seis páginas, lo primero no es el piano: es el lápiz. Haz el mapa de la pieza antes '
              'de tocar una nota y verás que lo que hay que aprender de verdad es muchísimo menos de '
              'lo que parece.',
        reglas=['PRIMERO EL MAPA, DESPUÉS EL PIANO', 'ESTA SEMANA, DOS PÁGINAS',
                'FLOJITO: NO ES UNA PIEZA DE FUERZA'],
        bloques=[
            dict(num=1, titulo='El dibujo que se repite',
                 pista='andamio · tres notas por compás, y vuelven una y otra vez',
                 sistemas=[
                     dict(cap='a) el dibujo, cuatro veces · igual de flojito las cuatro',
                          events=[n('C4'), n('E4'), n('G4'),
                                  n('C4'), n('E4'), n('G4'),
                                  n('C4'), n('E4'), n('G4'),
                                  n('C4'), n('E4'), n('G4')],
                          bars=4),
                     dict(cap='b) y el mismo dibujo empezando en otra nota · es lo único que cambia '
                              'durante páginas enteras',
                          events=encajar([n('A3'), n('C4'), n('E4'),
                                          n('F3'), n('A3'), n('C4'),
                                          n('G3'), n('B3'), n('D4')], 'treble'),
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL MAPA, ANTES DE TOCAR',
                 texto='Coge la partitura y numera los compases del 1 al último. Después, con dos o '
                       'tres colores, marca los grupos de compases que son iguales entre sí. Cuando '
                       'acabes vas a tener seis páginas convertidas en cuatro o cinco bloques, y esos '
                       'bloques son lo que hay que aprender. Es una hora de trabajo sin piano y te '
                       'ahorra semanas.'),
            dict(num=2, titulo='La izquierda: sostener tres golpes', clef='bass',
                 pista='andamio · una nota por compás, y aguanta',
                 sistemas=[
                     dict(cap='a) toca en el uno y deja sonar hasta el final del compás',
                          events=[n('C3', 'h.'), n('A2', 'h.'), n('F2', 'h.'), n('G2', 'h.')],
                          bars=4, clef='bass'),
                     dict(cap='b) y con dos notas a la vez, que es como está en varios sitios',
                          events=[ac(('C3', 'G3'), 'h.'), ac(('A2', 'E3'), 'h.'),
                                  ac(('F2', 'C3'), 'h.')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, cuatro compases',
                 pista='andamio · flojito, y con metrónomo desde el primer día',
                 sistemas=[
                     dict(cap='a) la derecha repitiendo su dibujo encima de la izquierda',
                          events=encajar([n('C4'), n('E4'), n('G4'),
                                          n('C4'), n('E4'), n('G4'),
                                          n('A3'), n('C4'), n('E4'),
                                          n('G3'), n('B3'), n('D4')], 'treble'),
                          bars=4),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · una nota por compás, y '
                              'aguanta los tres golpes',
                          events=[n('C3', 'h.'), n('C3', 'h.'), n('A2', 'h.'), n('G2', 'h.')],
                          bars=4, clef='bass', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Interstellar · para casa',
            intro='Veinte minutos al día, y el primer día entero con el lápiz y sin piano.',
            bloques=[
                plan((0, 'DÍA 1: numerar los compases y marcar lo que se repite'),
                     (7, 'El dibujo repetido, flojito y sin acelerar'),
                     (7, 'La izquierda: sostener los tres golpes'),
                     (6, 'Cuatro compases con las dos manos')),
                teclado({0: 1, 2: 2, 4: 3, 5: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'Las tres primeras son el dibujo que se repite toda la pieza.'],
                        titulo='En el teclado',
                        pista='tres notas, y con eso se hacen seis páginas'),
                inventa(['Solo Do, Mi y Sol.',
                         'Cuatro compases de tres golpes.',
                         'Que los cuatro compases sean iguales menos el último.'],
                        time_sig=(3, 4),
                        titulo='Escribe tú una pieza por repetición',
                        pista='así se construye la de Zimmer, y así se entiende'),
                rodear([[n('C4'), n('E4'), n('G4')], [n('A3'), n('C4'), n('E4')],
                        [n('C4'), n('E4'), n('G4')], [n('G3'), n('B3'), n('D4')]],
                       titulo='Rodea los dos compases iguales',
                       pista='andamio · en esta pieza esto es el ejercicio principal'),
                escalera((60, 'la primera página, leyendo el mapa'),
                         (75, 'dos páginas seguidas'),
                         (96, 'su velocidad'),
                         meta='♩ = 96, que es lo que pone tu partitura',
                         notas=['Con seis páginas, sube por trozos y no la pieza entera de golpe.']),
                para_clase('El mapa de la pieza hecho con lápiz, y cuatro compases tocados. El mapa '
                           'es lo importante: lo miramos juntos antes de seguir.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
