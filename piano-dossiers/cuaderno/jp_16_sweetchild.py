# -*- coding: utf-8 -*-
"""Sweet Child O' Mine (Guns N' Roses) — pieza 16 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Sadie King,
   marcado "easy piano", Musescore, 1 página, 33 compases):

     - DOS BEMOLES detrás de la clave: Si bemol mayor.
     - 4/4. No imprime tempo. Pone "mf" al empezar y "p (repeat mf)" en el c. 23.
     - La derecha hace el RIFF EN CORCHEAS SEGUIDAS desde el primer compás y no
       para hasta el c. 22.
     - La izquierda empieza en redondas y a partir del c. 13 pasa a acordes de
       redonda de tres notas; en el c. 23 pasa a corcheas con silencios.
     - Lleva el PEDAL MARCADO debajo del pentagrama, compás a compás: es la
       única pieza del cuaderno que lo trae escrito.
     - Hay barras de repetición en los cc. 9, 15 y 23, y casillas de 1ª y 2ª vez.

   Todo el material inventado va como ANDAMIO en Si bemol mayor.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jp_comun import (n, ac, plan, metronomo, ordenar, contar, teclado, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=16, nivel='intermedio', slug='SweetChildOMine',
    formato='adulto',
    titulo_corto="Sweet Child O' Mine", time_sig=(4, 4), key_sig='Sib mayor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'sweet-child-o-mine-guns-n-roses-easy-piano.pdf'),
    yt='https://www.youtube.com/results?search_query=sweet+child+o+mine+piano+easy',

    ficha=dict(
        titulo="Sweet Child O' Mine",
        autor="Guns N' Roses · arreglo de Sadie King",
        datos=[('Tonalidad', 'Si bemol mayor'), ('Compás', '4/4'),
               ('Carácter', 'mf · sin tempo'), ('Pedal', 'Marcado'),
               ('Páginas', 'Una')],
        titulo_ritmos='El riff, y lo que aguanta debajo',
        pie_ritmos='Andamio en Si bemol mayor. Lo literal es el reparto: corcheas seguidas arriba '
                   'sin parar y redondas abajo, con el pedal escrito.',
        armonia=dict(
            titulo='La primera pieza con el pedal escrito',
            tarjetas=[
                ('EL PEDAL', 'Viene marcado',
                 'Debajo del pentagrama hay una línea que dice cuándo se pisa y cuándo se suelta, '
                 'compás a compás. Es la única pieza del cuaderno que lo trae escrito.'),
                ('EL RIFF', 'Corcheas sin parar',
                 'La derecha no descansa desde el compás 1 hasta el 22. Es el riff que todo el '
                 'mundo reconoce, y es lo mismo repetido con la mano quieta.'),
                ('DOS BEMOLES', 'Si bemol mayor',
                 'Si bemol y Mi bemol. La misma armadura que Bella Ciao, y aquí es mayor: la '
                 'música descansa en Si bemol, no en Sol.'),
                ('TRES PARTES', 'Y se repiten',
                 'Repeticiones en los cc. 9, 15 y 23, con casillas de primera y segunda vez. La '
                 'pieza es más corta de lo que parecen 33 compases.'),
            ],
            pie='El riff es lo que la gente reconoce y es lo que menos trabajo tiene: la mano casi '
                'no se mueve. Lo que de verdad se estudia aquí es el pedal, y es la primera vez '
                'que el cuaderno lo pide.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el riff, corcheas seguidas · andamio',
             [n('Bb4', 'e'), n('F5', 'e'), n('D5', 'e'), n('Bb4', 'e'),
              n('F5', 'e'), n('D5', 'e'), n('Bb4', 'e'), n('F5', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda debajo, con el pedal · andamio',
             [n('Bb2', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Dos bemoles detrás de la clave: Si bemol y Mi bemol.',
            'Pone "mf" al empezar y "p (repeat mf)" en el compás 23.',
            'El pedal viene marcado debajo del pentagrama, compás a compás.',
            'La derecha hace corcheas seguidas desde el compás 1 hasta el 22.',
            'La izquierda empieza en redondas y pasa a acordes de tres notas en el c. 13.',
            'Hay repeticiones en los compases 9, 15 y 23.',
        ],
        reto='El pedal. Está escrito compás a compás y se cambia justo cuando cambia el acorde de '
             'abajo, no cuando cambia la nota de arriba. Si lo cambias con la derecha, el riff se '
             'convierte en un charco.',
        truco='Toca SOLO la izquierda con el pedal, sin la derecha, mirando la línea del pedal en '
              'la partitura. El pie tiene que subir y bajar justo después del acorde, nunca a la '
              'vez. Cuando salga solo, pon el riff encima y no vuelvas a pensar en el pie.',
        sabias='El riff nació de un ejercicio de calentamiento: Slash lo estaba tocando en broma '
               'para reírse de las escalas de circo cuando el resto del grupo le dijo que lo '
               'repitiera. La canción entera se escribió esa misma tarde.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el riff no cambia casi nunca. Lo que cambia debajo es la '
                      'armonía, y es lo que hace que suene distinto cada ocho compases.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El riff se aprende en diez minutos y el pedal no: primero el pie, después las manos.',
        reglas=['EL PEDAL CAMBIA DESPUÉS DEL ACORDE', 'EL RIFF, CON LA MANO QUIETA',
                'DOS BEMOLES: SI Y MI'],
        bloques=[
            dict(num=1, titulo='El pedal, con la izquierda sola', clef='bass',
                 pista='la línea del pedal viene escrita en tu partitura · míralA mientras tocas',
                 sistemas=[
                     dict(cap='a) una redonda por compás, y el pie sube y baja JUSTO DESPUÉS del '
                              'acorde · si suben a la vez, el sonido anterior se queda dentro',
                          events=[n('Bb2', 'w'), n('F2', 'w')],
                          matiz='mf',
                          pedal=4,
                          bars=2, clef='bass', key_sig='Sib mayor'),
                     dict(cap='b) y con acordes de tres notas, que es lo que hace del c. 13 en '
                              'adelante · el cambio de pedal es el mismo',
                          events=[ac(('Bb2', 'F3', 'Bb3'), 'w'), ac(('Eb2', 'Bb2', 'Eb3'), 'w')],
                          bars=2, clef='bass', key_sig='Sib mayor', show_time=False),
                 ]),
            dict(num=2, titulo='El riff, con la mano quieta',
                 pista='andamio en Si bemol mayor · la mano no se mueve de sitio: solo caen dedos',
                 sistemas=[
                     dict(cap='a) el dibujo sube y vuelve, ocho corcheas por compás · todas iguales '
                              'de fuerza, sin acentuar la primera',
                          events=[n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e'),
                                  n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e'),
                                  n('Eb5', 'e'), n('Bb4', 'e'), n('Eb5', 'e'), n('G5', 'e'),
                                  n('Eb5', 'e'), n('Bb4', 'e'), n('Eb5', 'e'), n('G5', 'e')],
                          bars=2, key_sig='Sib mayor'),
                     dict(cap='b) y con el dibujo movido de sitio, que es lo que pasa cada ocho '
                              'compases · la forma de la mano no cambia, solo dónde se apoya',
                          events=[n('C5', 'e'), n('A4', 'e'), n('C5', 'e'), n('F5', 'e'),
                                  n('C5', 'e'), n('A4', 'e'), n('C5', 'e'), n('F5', 'e'),
                                  n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e'),
                                  n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e')],
                          bars=2, key_sig='Sib mayor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL PEDAL VA DESPUÉS',
                 texto='Si pisas a la vez que el acorde, atrapas el final del anterior y los dos '
                       'suenan juntos. Se vuelve a pisar justo DESPUÉS de que el dedo haya bajado: '
                       'un instante, y es el que limpia el sonido.'),
            dict(num=3, titulo='Las dos manos y el pie',
                 pista='andamio · muy lento, y mirando la línea del pedal',
                 sistemas=[
                     dict(cap='a) riff arriba, redonda abajo, pedal por compás · si el riff se '
                              'emborrona al cambiar de acorde, el problema es el pie, no la mano',
                          events=[ac(('Bb2', 'D5'), 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e'),
                                  n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e'),
                                  ac(('Eb2', 'Eb5'), 'e'), n('Bb4', 'e'), n('Eb5', 'e'), n('G5', 'e'),
                                  n('Eb5', 'e'), n('Bb4', 'e'), n('Eb5', 'e'), n('G5', 'e')],
                          bars=2, key_sig='Sib mayor'),
                     dict(cap='b) y con el acorde de tres notas debajo, que es lo del c. 13 · el '
                              'pedal cambia una vez por compás y no una vez por acorde de arriba',
                          events=[ac(('Bb2', 'F3', 'Bb3'), 'e'), n('Bb4', 'e'), n('D5', 'e'),
                                  n('F5', 'e'), n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'),
                                  n('F5', 'e'),
                                  ac(('F2', 'C3', 'F3'), 'e'), n('C5', 'e'), n('A4', 'e'),
                                  n('F5', 'e'), n('C5', 'e'), n('A4', 'e'), n('C5', 'e'),
                                  n('F5', 'e')],
                          bars=2, key_sig='Sib mayor', show_time=False),
                 ]),
        ] + bloques_extra('Sib mayor', 21, 'Bb3', 'Bb2',
                          'dos bemoles y el pedal escrito: las dos cosas a la vez',
                          desde=4, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="Sweet Child O' Mine · para casa",
            intro='Veinte minutos, y los diez primeros sin tocar la mano derecha.',
            bloques=[
                plan((6, 'La izquierda sola con el pedal, mirando la línea escrita'),
                     (5, 'El riff solo, con la mano quieta'),
                     (5, 'Las dos manos sin pedal, para oír si el riff está limpio'),
                     (4, 'Las dos manos con pedal, muy lento')),
                metronomo('La partitura no trae tempo: elige uno donde el pedal te salga limpio.',
                          'Apunta cada día el número, y sube solo si el sonido no se emborrona.'),
                ordenar(['Las dos manos con pedal, muy lento.',
                         'La izquierda sola con el pedal.',
                         'El riff solo, sin pedal y con la mano quieta.',
                         'Las dos manos SIN pedal, para comprobar que el riff está limpio.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='el pedal es lo primero y lo último, y en medio no está'),
                contar([n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e'),
                        n('D5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e')],
                       ['¿Cuántas corcheas hay en total?',
                        '¿Cuántas veces aparece el Re?',
                        '¿Cuántos compases de 4/4 llenan estas notas?'],
                       titulo='Cuenta sobre el riff',
                       pista='andamio en Si bemol mayor · es el dibujo del compás 1'),
                teclado({6: 1, 3: 2, 0: 3},
                        ['Escribe el nombre de las tres teclas blancas marcadas.',
                         'Y pinta las dos negras de tu armadura: el Si bemol y el Mi bemol.'],
                        titulo='En el teclado',
                        pista='la número 1 es el Si'),
                para_clase('La izquierda con el pedal, sola, y el riff limpio sin pedal. Si al '
                           'juntarlo todo se emborrona, tráelo así: es exactamente lo que hay que '
                           'mirar juntos, y con el pie se ve en un minuto.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
