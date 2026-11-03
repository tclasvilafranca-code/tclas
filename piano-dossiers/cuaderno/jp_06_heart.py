# -*- coding: utf-8 -*-
"""Heart and Soul (Hoagy Carmichael) — pieza 6 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (guestinpiano.fr, marcada
   "Easy Piano Version", 1 página, 24 compases):

     - Do mayor: detrás de la clave no hay nada.
     - 4/4, y pone "♩ = 110" y debajo "Swing".
     - La izquierda empieza en blancas y a partir del c. 8 pasa a BAJO + ACORDE
       alternando: la nota grave en el uno y el acorde en el dos. Es el primer
       acompañamiento de verdad del cuaderno.
     - Hay barras de repetición en los cc. 9 y 16.

   MEDIDO nota a nota (300 dpi, `cabezas.py`; ver TRANSCRIPCION_JOSEP_FUENTES):

       c. 1   Do · Do · Do                              (negra · negra · blanca)
       c. 2   (silencio de corchea) Do · Si · La · Si · Do · Re

   Los índices medidos dan 9,90 tres veces seguidas en el c. 1, así que el do
   central es firme. La última nota del c. 2 va sin barra: dura más que las
   anteriores.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jp_comun import (n, ac, sil, plan, metronomo, ordenar, contar, teclado,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=6, nivel='intermedio', slug='HeartAndSoul',
    formato='adulto',
    titulo_corto='Heart and Soul', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source', 'heart-and-soul-.pdf'),
    yt='https://www.youtube.com/results?search_query=heart+and+soul+piano+easy',

    ficha=dict(
        titulo='Heart and Soul',
        autor='Hoagy Carmichael · Easy Piano Version',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 110 Swing'), ('Izquierda', 'Bajo y acorde'),
               ('Páginas', 'Una')],
        titulo_ritmos='Los dos primeros compases, medidos',
        pie_ritmos='Esto NO es andamio: está medido nota a nota sobre tu partitura. Tres do en el '
                   'compás 1 y la bajada del compás 2 después del silencio de corchea.',
        armonia=dict(
            titulo='Lo que estrena esta pieza',
            tarjetas=[
                ('EL SWING', 'Está escrito',
                 'Pone "Swing" debajo del tempo. Las parejas de corcheas no se tocan iguales: la '
                 'primera dura más. No se cuenta, se copia de oído.'),
                ('BAJO Y ACORDE', 'Desde el c. 8',
                 'La izquierda deja las blancas y pasa a alternar nota grave y acorde. Es el '
                 'acompañamiento más usado del piano popular y es la primera vez que aparece.'),
                ('EL C. 1, MEDIDO', 'Do Do Do',
                 'Dos negras y una blanca, las tres en el do central. Medido nota a nota: no hace '
                 'falta que lo busques, ya está comprobado.'),
                ('EL SILENCIO', 'Del c. 2',
                 'La segunda frase entra después de un silencio de corchea. Es lo que le da el '
                 'balanceo a la melodía, y si entras en el uno se pierde entero.'),
            ],
            pie='Es una pieza que todo el mundo ha oído y casi nadie ha tocado con el acompañamiento '
                'escrito. Aquí lo trae, y es la razón por la que está en el cuaderno: el bajo con '
                'acorde te va a servir en la mitad de las piezas que vengan después.',
        ),
        ritmos=[
            ('MANO DERECHA · C. 1', 'medido: tres do, negra negra blanca',
             [n('C4'), n('C4'), n('C4', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'bajo en el uno, acorde en el dos · desde el c. 8',
             [n('C3'), ac(('E3', 'G3')), n('C3'), ac(('E3', 'G3'))], AZUL, 'bass', None),
        ],
        especial=[
            'No hay armadura: ni sostenidos ni bemoles.',
            'Pone "♩ = 110" y debajo "Swing".',
            'El compás 1 son tres do: negra, negra y blanca (medido).',
            'El compás 2 entra tras un silencio de corchea y baja Do · Si · La · Si · Do · Re.',
            'Desde el compás 8 la izquierda hace bajo y acorde alternando.',
            'Hay barras de repetición en los compases 9 y 16.',
        ],
        reto='El bajo con acorde de la izquierda, sin mirarla. Son dos sitios distintos del teclado '
             'alternando en cada compás, y en cuanto miras la mano izquierda pierdes la derecha.',
        truco='Toca solo la izquierda con los ojos cerrados durante dos minutos, sin música: bajo, '
              'acorde, bajo, acorde. Lo que hay que aprender no son las notas, es la distancia '
              'entre las dos posiciones, y esa se aprende antes con los ojos cerrados que abiertos.',
        sabias='Es probablemente la pieza más tocada del mundo a cuatro manos improvisadas: su '
               'acompañamiento de cuatro acordes se repite en cientos de canciones, y por eso suena '
               'familiar aunque no la hayas oído nunca entera.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en las parejas de corcheas: la primera dura más que la segunda. Eso '
                      'es el swing, y no está escrito porque no se puede escribir.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas: el swing, que se copia de oído y no se estudia, y el bajo con '
              'acorde de la izquierda, que sí se estudia y es el trabajo de la semana.',
        reglas=['LA IZQUIERDA, SIN MIRARLA', 'EL SWING SE COPIA, NO SE CUENTA',
                'EL C. 2 ENTRA DESPUÉS DEL SILENCIO'],
        bloques=[
            dict(num=1, titulo='Los dos primeros compases, tal como están escritos',
                 pista='cc. 1-2 · MEDIDO sobre tu partitura, no es andamio',
                 sistemas=[
                     dict(cap='a) tres do y la bajada · el silencio de corchea del compás 2 es lo '
                              'que hace que suene a esta canción y no a otra',
                          events=[n('C4'), n('C4'), n('C4', 'h'),
                                  {'rest': True, 'dur': 'e'}, n('C4', 'e'), n('B3', 'e'),
                                  n('A3', 'e'), n('B3', 'e'), n('C4', 'e'), n('D4')],
                          bars=2),
                 ]),
            dict(num=2, titulo='El bajo con acorde, solo', clef='bass',
                 pista='la FORMA es literal (bajo en el uno, acorde en el dos); las notas, andamio',
                 sistemas=[
                     dict(cap='a) bajo, acorde, bajo, acorde · con los ojos cerrados, dos minutos',
                          events=[n('C3'), ac(('E3', 'G3')), n('C3'), ac(('E3', 'G3')),
                                  n('A2'), ac(('E3', 'G3')), n('A2'), ac(('E3', 'G3'))],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de bajo, que es donde se falla · el acorde de arriba '
                              'casi no se mueve, el que salta es el pulgar de abajo',
                          events=[n('F2'), ac(('A2', 'C3')), n('F2'), ac(('A2', 'C3')),
                                  n('G2'), ac(('B2', 'D3')), n('G2'), ac(('B2', 'D3'))],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL SWING',
                 texto='Cuando pone "Swing", las parejas de corcheas no se tocan iguales: la primera '
                       'dura como dos tercios del golpe y la segunda como uno. Escrito así parece '
                       'un problema de matemáticas, y en realidad es lo que hace cualquiera al decir '
                       '"PAA-pa, PAA-pa". Escucha la grabación dos veces y sale solo. No lo cuentes.'),
            dict(num=3, titulo='Las parejas de corcheas, balanceadas',
                 pista='andamio construido sobre la bajada medida del c. 2 · larga-corta, no iguales',
                 sistemas=[
                     dict(cap='a) de dos en dos, con la primera de cada pareja más larga · dilo en '
                              'voz alta mientras tocas: PAA-pa, PAA-pa',
                          events=[n('C4', 'e'), n('B3', 'e'), n('A3', 'e'), n('B3', 'e'),
                                  n('C4', 'e'), n('D4', 'e'), n('E4', 'e'), n('D4', 'e'),
                                  n('C4', 'h'), n('B3', 'h')],
                          bars=2),
                     dict(cap='b) y subiendo, que es lo que hace la segunda mitad · el balanceo no '
                              'cambia porque cambie la dirección',
                          events=[n('E4', 'e'), n('F4', 'e'), n('G4', 'e'), n('F4', 'e'),
                                  n('E4', 'e'), n('D4', 'e'), n('C4', 'e'), n('D4', 'e'),
                                  n('E4', 'h'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, cuatro compases',
                 pista='andamio a partir del material medido · despacio, y sin mirarse la izquierda',
                 sistemas=[
                     dict(cap='a) la melodía sobre el bajo con acorde · si la derecha se para cada '
                              'vez que la izquierda cambia de bajo, trabaja el paso 2 otra vez',
                          events=[ac(('C3', 'C4')), ac(('E3', 'G3')), n('C4', 'h'),
                                  ac(('A2', 'C4'), 'e'), n('B3', 'e'), ac(('E3', 'G3')), n('A3', 'h')],
                          bars=2),
                 ]),
        ] + bloques_extra('Do mayor', 36, 'C4', 'C3',
                          'el swing: escritas iguales, tocadas desiguales',
                          desde=5, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Heart and Soul · para casa',
            intro='Veinte minutos, y la mitad para la mano izquierda sola.',
            bloques=[
                plan((6, 'Bajo y acorde con los ojos cerrados, sin música'),
                     (5, 'La izquierda, cc. 8-16, cambiando de bajo'),
                     (5, 'La derecha sola, con el silencio del c. 2 en su sitio'),
                     (4, 'Las dos juntas, de cuatro en cuatro compases')),
                metronomo('Empieza donde te salga el bajo con acorde sin mirarte la mano.',
                          'La meta son 110, pero con swing: primero que suene balanceado, luego rápido.'),
                ordenar(['Las dos manos, cuatro compases seguidos.',
                         'El bajo con acorde, con los ojos cerrados.',
                         'La derecha sola, con el silencio del compás 2 puesto.',
                         'Escuchar la grabación dos veces, para copiar el swing.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='uno de ellos va antes de tocar nada'),
                contar([n('C4'), n('C4'), n('C4', 'h'), n('C4', 'e'), n('B3', 'e'),
                        n('A3', 'e'), n('B3', 'e'), n('C4', 'e'), n('D4')],
                       ['¿Cuántos Do hay?', '¿Cuántas corcheas hay?',
                        '¿Cuál es la nota más grave?'],
                       titulo='Cuenta sobre los compases medidos',
                       pista='son tus dos primeros compases, sin el silencio'),
                teclado({0: 1, 2: 2, 4: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         'La número 1 es el do central: donde empieza la melodía.'],
                        titulo='En el teclado',
                        pista='las tres salen del compás 1 y del acompañamiento'),
                para_clase('El bajo con acorde a la velocidad que te salga sin mirar, y los dos '
                           'primeros compases con el silencio en su sitio. El swing lo miramos '
                           'juntos: es más fácil copiarlo que explicarlo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
