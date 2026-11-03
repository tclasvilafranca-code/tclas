# -*- coding: utf-8 -*-
"""Petite Chanson, de Riccardo Collu (pieza 2 de Josep). Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, 2 páginas,
   24 compases, ©2025 Riccardo Collu):

     - Do mayor: detrás de la clave no hay nada.
     - 4/4, y pone "♩ = 80 andante".
     - Es a cuatro manos. El Primo (el de arriba) lleva LOS DOS PENTAGRAMAS EN
       CLAVE DE SOL; el Secondo sí lleva sol y fa.
     - Empieza con anacrusa: dos corcheas antes del primer compás.

   MEDIDO nota a nota (300 dpi, `cabezas.py`; ver TRANSCRIPCION_JOSEP_FUENTES):

       anacrusa   Mi · Fa            (dos corcheas)
       c. 1       Sol · Sol · Sol    (tres negras)

   y el segundo Sol está UNA OCTAVA por encima del primero (índices medidos
   7,87 y 0,90: siete grados justos). Ese salto de octava en el primer compás
   es el reto de la semana, y es literal, no andamio.

   Lo que NO se cita: el resto de la pieza. Las corcheas que cierran el c. 1
   quedan por encima del pentagrama con líneas adicionales y no se dan por
   medidas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, plan, a_cuatro_manos, escalera, diferencias,
                      nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=2, nivel='intermedio', slug='PetiteChanson',
    formato='adulto',
    titulo_corto='Petite Chanson', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'Petite chanson.(4 MANOS)'),
    yt='https://www.youtube.com/results?search_query=petite+chanson+riccardo+collu+piano+4+hands',

    ficha=dict(
        titulo='Petite Chanson',
        autor='Riccardo Collu · a cuatro manos · parte del Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 80 andante'), ('Empieza', 'Con anacrusa'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='El primer compás, medido',
        pie_ritmos='Esto NO es andamio: está medido nota a nota sobre tu partitura. Las dos corcheas '
                   'de la anacrusa y las tres negras del compás 1, con el salto de octava incluido.',
        armonia=dict(
            titulo='Lo que trae esta pieza que no traía la primera',
            tarjetas=[
                ('LA ANACRUSA', 'Se entra antes',
                 'Dos corcheas ANTES del primer compás. El compás 1 no empieza en tu primera nota: '
                 'empieza en la tercera.'),
                ('EL SALTO', 'Una octava',
                 'Mi · Fa | Sol · Sol · Sol, y el segundo Sol está una octava arriba. Medido: siete '
                 'grados justos. La mano tiene que ir y volver sin mirarse.'),
                ('LAS DOS EN SOL', 'Sin clave de fa',
                 'Los dos pentagramas del Primo van en clave de sol. La izquierda lee arriba, no '
                 'abajo: si lees por costumbre, te vas a equivocar de octava.'),
                ('ANDANTE', '♩ = 80',
                 'Viene con número. No es rápido, pero es un número: se puede comprobar con el '
                 'metrónomo y saber si estás o no estás.'),
            ],
            pie='Es la única pieza del cuaderno con las dos manos escritas en clave de sol y con el '
                'tempo impreso desde el primer día. Las dos cosas juntas la hacen buena para la '
                'segunda semana: hay algo concreto que medir y algo concreto que desaprender.',
        ),
        ritmos=[
            ('ANACRUSA + C. 1', 'medido: Mi Fa | Sol Sol Sol',
             [n('E4', 'e'), n('F4', 'e'), n('G4'), n('G5'), n('G5')], OCRE, 'treble', None),
            ('LA IZQUIERDA', 'también en clave de sol · andamio',
             [n('C4'), n('E4'), n('G4'), n('E4')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol.',
            'Pone "♩ = 80 andante": el tempo viene con número, no solo con palabra.',
            'Empieza con dos corcheas antes del primer compás.',
            'Los dos pentagramas del Primo van en clave de SOL: la izquierda no lee en clave de fa.',
            'El segundo Sol del compás 1 está una octava por encima del primero (medido).',
            'El Secondo lo toca la profesora, y lleva clave de sol y de fa.',
        ],
        reto='El salto de octava del compás 1, y que no se note. La mano tiene que subir una octava '
             'entera y caer en la tecla correcta a la primera, en un tempo que no te deja tiempo '
             'de buscarla.',
        truco='Toca Sol grave y Sol agudo alternando veinte veces, sin tocar nada más y sin mirar '
              'la mano. Lo que aprendes ahí no es la nota, es la distancia: el brazo se acuerda de '
              'cuánto tiene que moverse. Después mete el salto en el compás y ya está resuelto.',
        sabias='Las piezas a cuatro manos se inventaron para tocar en casa, no en concierto. Antes '
               'de que hubiera grabaciones, la manera de escuchar una sinfonía era que dos personas '
               'la tocaran a cuatro manos en el salón, y se publicaban arreglos de casi todo.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cómo entra: la melodía empieza antes que el compás. Cuenta "y" '
                      'antes del primer golpe y verás dónde cae de verdad.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas y las dos son de sitio, no de notas: entrar antes del compás y '
              'saltar una octava. Trabájalas por separado antes de tocar la pieza, porque juntas '
              'no se arreglan.',
        reglas=['LA ENTRADA VA ANTES DEL UNO', 'EL SALTO, SIN MIRAR LA MANO',
                'LAS DOS MANOS LEEN EN CLAVE DE SOL'],
        bloques=[
            dict(num=1, titulo='La anacrusa: entrar antes de que empiece el compás',
                 pista='c. 1 · MEDIDO sobre tu partitura, no es andamio',
                 sistemas=[
                     dict(cap='a) cuenta el compás entero en silencio y entra en la "y" del cuatro · '
                              'las dos corcheas son Mi y Fa, y el compás 1 empieza en el Sol',
                          events=[{'rest': True, 'dur': 'h'}, {'rest': True, 'dur': 'q'},
                                  n('E4', 'e'), n('F4', 'e'),
                                  n('G4'), n('G5'), n('G5'), {'rest': True, 'dur': 'q'}],
                          bars=2),
                 ]),
            dict(num=2, titulo='El salto de octava, solo',
                 pista='andamio construido sobre el salto medido · sin mirarte la mano',
                 sistemas=[
                     dict(cap='a) Sol y Sol, ida y vuelta · el brazo aprende la distancia, no el dedo',
                          events=[n('G4'), n('G5'), n('G4'), n('G5'),
                                  n('G4'), n('G5'), n('G4', 'h')],
                          bars=2),
                     dict(cap='b) y ahora la octava desde otras notas · si te sale solo desde Sol, '
                              'es que has memorizado la tecla y no la distancia',
                          events=[n('E4'), n('E5'), n('F4'), n('F5'),
                                  n('D4'), n('D5'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LAS DOS MANOS EN CLAVE DE SOL',
                 texto='Tu parte lleva los dos pentagramas en clave de sol, y eso descoloca a '
                       'cualquiera que ya sepa leer: la mano izquierda está acostumbrada a que su '
                       'renglón sea el de la clave de fa. Aquí no. Antes de tocar, mira la clave de '
                       'CADA renglón, no la posición del renglón en la página.'),
            dict(num=3, titulo='La izquierda sola, leyendo en clave de sol',
                 pista='andamio · lee la clave de cada renglón antes de empezar',
                 sistemas=[
                     dict(cap='a) el acompañamiento, en el registro en el que de verdad está escrito · '
                              'si te suena una octava por debajo, estás leyendo en clave de fa',
                          events=[n('C4'), n('G4'), n('E4'), n('G4'),
                                  n('D4'), n('A4'), n('F4'), n('A4')],
                          bars=2),
                     dict(cap='b) y con las dos notas juntas, que es como suena · sin apoyar el peso '
                              'del brazo: la izquierda aquí acompaña',
                          events=[ac(('C4', 'E4'), 'h'), ac(('D4', 'F4'), 'h'),
                                  ac(('E4', 'G4'), 'h'), ac(('C4', 'E4'), 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, con la anacrusa puesta',
                 pista='andamio · muy despacio, y contando en voz alta desde antes de empezar',
                 sistemas=[
                     dict(cap='a) la derecha entra antes y la izquierda entra en el uno · lo difícil '
                              'es que la izquierda NO se adelante',
                          events=[{'rest': True, 'dur': 'h'}, {'rest': True, 'dur': 'q'},
                                  n('E4', 'e'), n('F4', 'e'),
                                  ac(('C4', 'G4')), ac(('C4', 'G5')),
                                  ac(('C4', 'G5')), {'rest': True, 'dur': 'q'}],
                          bars=2),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Petite Chanson · para casa',
            intro='Veinte minutos, y quince de ellos en dos cosas: la entrada y el salto.',
            bloques=[
                plan((5, 'El salto de octava solo, veinte veces, sin mirar'),
                     (5, 'La anacrusa: contar "un dos tres Y" y entrar'),
                     (5, 'Los cuatro primeros compases, derecha sola'),
                     (5, 'Los mismos cuatro con las dos manos, a ♩ = 60')),
                a_cuatro_manos('El Secondo entra en el uno y tú entras antes. Decidid en clase quién '
                               'cuenta en voz alta el compás de entrada: si contáis los dos, no '
                               'entra nadie a tiempo.'),
                escalera((60, 'las notas y el salto, sin prisa'),
                         (70, 'con la anacrusa en su sitio'),
                         (80, 'su velocidad: andante'),
                         meta='♩ = 80, que es lo que pone tu partitura',
                         notas=['Dos veces limpio antes de subir de escalón.']),
                diferencias([n('E4', 'e'), n('F4', 'e'), n('G4'), n('G5'), n('G5'), n('E4', 'h')],
                            [n('E4', 'e'), n('G4', 'e'), n('G4'), n('G5'), n('G4'), n('E4', 'h')],
                            2,
                            titulo='Busca las diferencias',
                            pista='el de arriba es tu compás 1 medido · en el de abajo hay 2 cosas '
                                  'cambiadas'),
                nombres(['E4', 'F4', 'G4', 'G5', 'C5', 'A4', 'D5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='ojo con las dos últimas: no todas están en el mismo sitio'),
                para_clase('El salto de octava y a qué escalón del metrónomo has llegado. Y si la '
                           'izquierda se te adelanta en la entrada, dilo: se arregla en dos minutos '
                           'con alguien contando al lado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
