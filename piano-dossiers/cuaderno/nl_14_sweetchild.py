# -*- coding: utf-8 -*-
"""Sweet Child O' Mine (Guns N' Roses) — pieza 14 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Sadie King,
   marcado "easy piano", Musescore, 1 página, 33 compases; el mismo archivo
   que la pieza 16 de Josep, byte a byte):

     - Dos bemoles detrás de la clave: Si bemol mayor.
     - 4/4. No imprime tempo. Pone "mf" al empezar y "p (repeat mf)" en el
       c. 23.
     - La derecha hace el riff en corcheas seguidas desde el primer compás
       y no para hasta el c. 22.
     - La izquierda empieza en redondas y a partir del c. 13 pasa a acordes
       de redonda de tres notas; en el c. 23 pasa a corcheas con silencios.
     - Lleva el pedal marcado debajo del pentagrama, compás a compás.
     - Hay barras de repetición en los cc. 9, 15 y 23, y casillas de 1ª y 2ª
       vez.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SIB = 'Sib mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=14, nivel='avanzado', slug='SweetChildOMine',
    formato='adulto',
    titulo_corto="Sweet Child O' Mine", time_sig=(4, 4), key_sig=SIB,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
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
            titulo='La única pieza con el pedal escrito',
            tarjetas=[
                ('EL PEDAL', 'Viene marcado',
                 'Debajo del pentagrama hay una línea que dice cuándo se pisa y cuándo se suelta, '
                 'compás a compás.'),
                ('EL RIFF', 'Corcheas sin parar',
                 'La derecha no descansa desde el compás 1 hasta el 22: es el riff que todo el '
                 'mundo reconoce, repetido con la mano quieta.'),
                ('DOS BEMOLES', 'Si bemol mayor',
                 'Si bemol y Mi bemol, la misma armadura que Bella Ciao, pero aquí mayor: la música '
                 'descansa en Si bemol, no en Sol.'),
                ('TRES PARTES', 'Y se repiten',
                 'Repeticiones en los cc. 9, 15 y 23, con casillas de primera y segunda vez.'),
            ],
            pie='El riff nació de un ejercicio de calentamiento: el guitarrista lo tocaba en broma '
                'para reírse de las escalas de circo cuando el resto del grupo le dijo que siguiera.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el riff, corcheas seguidas · andamio',
             [n('G4', 'e'), n('D5', 'e'), n('Bb4', 'e'), n('G4', 'e'),
              n('D5', 'e'), n('Bb4', 'e'), n('G4', 'e'), n('D5', 'e')], OCRE, 'treble', None),
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
        reto='El pedal: está escrito compás a compás y cambia justo cuando cambia el acorde de '
             'abajo, no cuando cambia la nota de arriba. Si lo cambias con la derecha, el riff se '
             'emborrona.',
        truco='Toca solo la izquierda con el pedal, mirando la línea escrita en la partitura. El pie '
              'sube y baja justo después del acorde, nunca a la vez.',
        sabias='La canción entera se escribió en una sola tarde de ensayo, a partir de ese riff que '
               'había nacido como una broma minutos antes.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el riff casi no cambia nunca: lo que cambia debajo es la '
                      'armonía, y eso es lo que hace que suene distinto cada ocho compases.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El riff se aprende en diez minutos y el pedal no: primero el pie, después las manos. '
              'Trabaja las dos cosas por separado antes de juntarlas, porque son dos aprendizajes '
              'distintos y mezclarlos desde el principio solo hace que cueste más tiempo el doble.',
        reglas=['EL PEDAL CAMBIA DESPUÉS DEL ACORDE', 'EL RIFF, CON LA MANO QUIETA',
                'DOS BEMOLES: SI Y MI'],
        bloques=[
            dict(num=1, titulo='El pedal, con la izquierda sola', clef='bass',
                 pista='la línea del pedal viene escrita en tu partitura',
                 sistemas=[
                     dict(cap='a) una redonda por compás, con otra pareja de acordes',
                          events=[n('Eb2', 'w'), n('C2', 'w')],
                          bars=2, clef='bass', key_sig=SIB),
                     dict(cap='b) y con acordes de tres notas, que es lo que hace del c. 13 en '
                              'adelante',
                          events=[ac(('F2', 'C3', 'F3'), 'w'), ac(('Bb2', 'D3', 'F3'), 'w')],
                          bars=2, clef='bass', key_sig=SIB, show_time=False),
                 ]),
            dict(num=2, titulo='El riff, con la mano quieta',
                 pista='andamio en Si bemol mayor · la mano no se mueve de sitio',
                 sistemas=[
                     dict(cap='a) dos peldaños más arriba',
                          events=[n('F5', 'e'), n('D5', 'e'), n('F5', 'e'), n('Bb5', 'e'),
                                  n('F5', 'e'), n('D5', 'e'), n('F5', 'e'), n('Bb5', 'e'),
                                  n('G5', 'e'), n('Eb5', 'e'), n('G5', 'e'), n('Bb5', 'e'),
                                  n('G5', 'e'), n('Eb5', 'e'), n('G5', 'e'), n('Bb5', 'e')],
                          bars=2, key_sig=SIB),
                     dict(cap='b) movido a otro sitio',
                          events=[n('A4', 'e'), n('F4', 'e'), n('A4', 'e'), n('D5', 'e'),
                                  n('A4', 'e'), n('F4', 'e'), n('A4', 'e'), n('D5', 'e'),
                                  n('Bb4', 'e'), n('F4', 'e'), n('Bb4', 'e'), n('D5', 'e'),
                                  n('Bb4', 'e'), n('F4', 'e'), n('Bb4', 'e'), n('D5', 'e')],
                          bars=2, key_sig=SIB, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL PEDAL VA DESPUÉS',
                 texto='Si pisas a la vez que el acorde, atrapas el final del anterior y los dos '
                       'suenan juntos. Se vuelve a pisar justo después de que el dedo haya bajado: '
                       'un instante, y es el que limpia el sonido antes de que llegue el siguiente '
                       'cambio de acorde.'),
            dict(num=3, titulo='Las dos manos y el pie',
                 pista='andamio · muy lento, y mirando la línea del pedal',
                 sistemas=[
                     dict(cap='a) riff arriba, redonda abajo, pedal por compás, con otro punto de '
                              'partida',
                          events=[ac(('Eb2', 'F5'), 'e'), n('D5', 'e'), n('F5', 'e'), n('Bb5', 'e'),
                                  n('F5', 'e'), n('D5', 'e'), n('F5', 'e'), n('Bb5', 'e'),
                                  ac(('C2', 'G5'), 'e'), n('Eb5', 'e'), n('G5', 'e'), n('Bb5', 'e'),
                                  n('G5', 'e'), n('Eb5', 'e'), n('G5', 'e'), n('Bb5', 'e')],
                          bars=2, key_sig=SIB),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
