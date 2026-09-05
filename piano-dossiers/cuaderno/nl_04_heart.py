# -*- coding: utf-8 -*-
"""Heart and Soul (Hoagy Carmichael) — pieza 4 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (guestinpiano.fr, "Easy
   Piano Version", 1 página, 24 compases; el mismo archivo que la pieza 6 de
   Josep y la de Luisa, byte a byte), medido nota a nota (300 dpi):

     - Do mayor: detrás de la clave no hay nada.
     - 4/4, "♩ = 110" y debajo "Swing".
     - c. 1: Do · Do · Do (negra, negra, blanca).
     - c. 2: silencio de corchea y Do · Si · La · Si · Do · Re.
     - Desde el c. 8 la izquierda pasa a bajo + acorde alternando.
     - Barras de repetición en los cc. 9 y 16.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import arpegio, giro, cadencia, escala, encajar
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=4, nivel='avanzado', slug='HeartAndSoul',
    formato='adulto',
    titulo_corto='Heart and Soul', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source', 'heart-and-soul-.pdf'),
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
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('EL SWING', 'No se cuenta',
                 'Pone "Swing" debajo del tempo: las parejas de corcheas no valen igual, la primera '
                 'dura más. Se copia de oído, no se hace ninguna cuenta.'),
                ('BAJO Y ACORDE', 'Desde el c. 8',
                 'La izquierda deja las blancas del principio y pasa a alternar una nota grave sola '
                 'con un acorde: el acompañamiento más usado del piano popular.'),
                ('TRES DO SEGUIDOS', 'El compás 1',
                 'Negra, negra y blanca, las tres en el mismo Do central. Está medido, no hace falta '
                 'comprobarlo otra vez.'),
                ('EL SILENCIO', 'Antes del c. 2',
                 'La segunda frase entra tras un silencio de corchea. Entrar en el "uno" sin ese '
                 'hueco deshace por completo el balanceo de la melodía.'),
            ],
            pie='Es una de las piezas más tocadas del mundo a cuatro manos improvisadas: el '
                'acompañamiento de bajo y acorde que trae se repite en cientos de canciones distintas.',
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
        reto='El bajo con acorde de la izquierda, sin mirarla: son dos zonas del teclado que se '
             'alternan cada compás, y en cuanto la vista se va a la izquierda se pierde la derecha.',
        truco='Toca solo la izquierda dos minutos con los ojos cerrados, bajo-acorde-bajo-acorde. Lo '
              'que hace falta memorizar no son las notas: es la distancia entre las dos posiciones.',
        sabias='Su acompañamiento de cuatro acordes es tan reconocible que casi cualquiera que se '
               'sienta al piano por primera vez acaba tocando estas cuatro notas sin saber su nombre.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en las parejas de corcheas: la primera dura más que la segunda. Eso es '
                      'el swing, y no se puede escribir con exactitud, solo copiar de oído.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El swing se copia de oído; el bajo con acorde de la izquierda sí se estudia, y es el '
              'trabajo central de esta semana.',
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
                          events=[n('D3'), ac(('F3', 'A3')), n('D3'), ac(('F3', 'A3')),
                                  n('B2'), ac(('D3', 'F3')), n('B2'), ac(('D3', 'F3'))],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de bajo, que es donde se falla · el acorde de arriba '
                              'casi no se mueve, el que salta es el pulgar de abajo',
                          events=[n('E2'), ac(('G2', 'B2')), n('E2'), ac(('G2', 'B2')),
                                  n('C2'), ac(('E2', 'G2')), n('C2'), ac(('E2', 'G2'))],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL SWING',
                 texto='Cuando pone "Swing", las parejas de corcheas no se tocan iguales: la primera '
                       'dura como dos tercios del golpe y la segunda como uno. Es lo que hace '
                       'cualquiera al decir "PAA-pa, PAA-pa" en voz alta. Se escucha, no se cuenta.'),
            dict(num=3, titulo='Las parejas de corcheas, balanceadas',
                 pista='andamio construido sobre la bajada medida del c. 2 · larga-corta, no iguales',
                 sistemas=[
                     dict(cap='a) desde una nota más alta, diciendo PAA-pa en voz alta',
                          events=[n('E4', 'e'), n('D4', 'e'), n('C4', 'e'), n('D4', 'e'),
                                  n('E4', 'e'), n('F4', 'e'), n('G4', 'e'), n('F4', 'e'),
                                  n('E4', 'h'), n('D4', 'h')],
                          bars=2),
                     dict(cap='b) y bajando, que es lo que hace la segunda mitad de la frase',
                          events=[n('G4', 'e'), n('A4', 'e'), n('B4', 'e'), n('A4', 'e'),
                                  n('G4', 'e'), n('F4', 'e'), n('E4', 'e'), n('F4', 'e'),
                                  n('G4', 'h'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=4, titulo='El acorde de Do, desplegado',
                 pista='andamio en Do mayor · las mismas notas del bajo, pero una detrás de otra',
                 sistemas=[
                     dict(cap='a) sube y baja sin parar en la cima · la mano se abre una vez y se '
                              'queda abierta',
                          events=encajar(arpegio('Do mayor', 'G3'), 'treble'), bars=2),
                 ]),
            dict(num=5, titulo='Las dos manos, cuatro compases',
                 pista='andamio a partir del material medido · despacio, y sin mirarse la izquierda',
                 sistemas=[
                     dict(cap='a) la melodía sobre el bajo con acorde · si la derecha se para cada '
                              'vez que la izquierda cambia de bajo, trabaja el paso 2 otra vez',
                          events=[ac(('D3', 'D4')), ac(('F3', 'A3')), n('D4', 'h'),
                                  ac(('B2', 'D4'), 'e'), n('C4', 'e'), ac(('F3', 'A3')), n('B3', 'h')],
                          bars=2),
                 ]),
            dict(num=6, titulo='Soltar el dedo que se agarrota',
                 pista='andamio · el giro de siempre, sin mover la mano de sitio',
                 sistemas=[
                     dict(cap='a) alrededor del Mi · si la muñeca se levanta, es que estás '
                              'empujando en vez de dejar caer',
                          events=giro('Do mayor', 'E4'), bars=2),
                     dict(cap='b) y alrededor del Sol, que es el que más trabaja en esta pieza',
                          events=giro('Do mayor', 'G4'), bars=2, show_time=False),
                 ]),
            dict(num=7, titulo='Los cuatro acordes, y la escala que los une',
                 pista='andamio en Do mayor · la armonía de Heart and Soul es esta y nada más',
                 sistemas=[
                     dict(cap='a) I - IV - V - I con la izquierda · apréndetelos de memoria y la '
                              'pieza se queda en la mitad de trabajo',
                          events=cadencia('Do mayor', 'C3'), bars=4, clef='bass'),
                     dict(cap='b) y la escala por encima, para colocar la derecha',
                          events=encajar(escala('Do mayor', 'G4', sentido='baja'), 'treble'),
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
