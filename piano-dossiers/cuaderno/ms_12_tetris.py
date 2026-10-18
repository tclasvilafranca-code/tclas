# -*- coding: utf-8 -*-
"""Pieza 12 · Tetris (Korobeiniki). MEDIDO sobre el PDF de Drive de Sharifa: 3 paginas (la 3.ª en
   blanco), 24 compases en 6 sistemas de 4, sin armadura (La menor, con Sol sostenido en los
   cc. 10, 12 y 16), 4/4, sin tempo ni matices, corchea como figura mas corta.
   Derecha cc. 1-4: Mi5 | Si4 Do5 Re5 Do5 Si4 | La4 La4 Do5 Mi5 Re5 Do5 | Si4. Do5 Re5 Mi5 | Do5 La4 La4.
   Izquierda: nota grave + octava en corcheas; bajos Mi, La, Si, La | Re, Do, Si, La | La, Sol#, La, Si
   | La, Si, Do, Si. Los cc. 17-24 repiten los cc. 1-8 salvo el c. 24 (silencio de corchea, Do, La
   corchea, La, silencio)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403


def _e(p, d='q', b=None):
    ev = {'pitch': p, 'dur': d}
    if b is not None:
        ev['beam'] = b
    return ev


_MEL = [_e('E5'), _e('B4', 'e', 0), _e('C5', 'e', 0), _e('D5'), _e('C5', 'e', 1), _e('B4', 'e', 1),
        _e('A4'), _e('A4', 'e', 2), _e('C5', 'e', 2), _e('E5'), _e('D5', 'e', 3), _e('C5', 'e', 3)]
_IZQ = [_e(('E2', 'E3')[j % 2], 'e', j // 4) for j in range(8)]
_IZQ += [_e(('A1', 'A2')[j % 2], 'e', 2 + j // 4) for j in range(8)]

SPEC = dict(
    num=12, slug='tetris', pdf='copia_de_tetrix.pdf', time_sig=(4, 4),
    titulo='Tetris', autor='Korobeiniki · canción popular rusa · tema del videojuego',
    kicker='Sharifa · pieza 12 · Tetris', mes='Junio · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=tetris+theme+korobeiniki+piano',
    credito='Partitura: Korobeiniki, tema de Tetris (Drive). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'La menor'), ('Compás', '4/4'), ('Tempo', 'Sin indicar'),
               ('Figura corta', 'Corchea'), ('Compases', '24')],
        total=24,
        secciones=[('A', 1, 8, 'La melodía', AZUL),
                   ('B', 9, 16, 'Notas largas y subida', OCRE),
                   ('A', 17, 24, 'Vuelve la melodía', AZUL)],
        ideas=[('LA MELODÍA', 'Mi, Si, Do, Re',
                'Baja y sube por notas vecinas. Es la melodía que todo el mundo reconoce.'),
               ('LA IZQUIERDA', 'Una nota y su octava',
                'Ocho corcheas por compás: la nota grave y la misma, una octava más aguda, '
                'sin parar.'),
               ('LA BAJADA', 'Re, Do, Si, La',
                'En los cc. 5-8 la nota grave baja de uno en uno hasta llegar a La.'),
               ('SOL SOSTENIDO', 'Una tecla negra',
                'Aparece en los cc. 10, 12 y 16. Es la nota que "pide" volver a La menor.')],
        especial=[
            'No lleva armadura: es La menor, y el Sol sostenido va escrito en el compás.',
            'El compás es 4/4. No trae tempo ni matices.',
            'La izquierda toca ocho corcheas por compás, de principio a fin.',
            'La derecha mezcla negras, corcheas, negras con puntillo (cc. 3, 6, 7), blancas '
            '(cc. 9-11, 13-14) y redondas (cc. 12 y 16).',
            'Los cc. 17-24 repiten los cc. 1-8; solo cambia el final (c. 24).'],
        reto='Mantener la izquierda pareja, ocho corcheas por compás, mientras la derecha cambia '
             'de ritmo.',
        truco='Toca la izquierda sola hasta poder hablar a la vez. Después añade la derecha, un '
              'compás cada vez.',
        sabias='Korobeiniki significa "los buhoneros" (vendedores ambulantes) y es una canción '
               'popular rusa sobre un poema de Nekrásov de 1861. El Tetris lo creó Alekséi '
               'Pajítnov en 1984 y la versión de Game Boy (1989) la hizo famosa en todo el mundo.',
        qr_texto='Escúchala con la partitura delante y sigue la izquierda: no se detiene.',
        ts=(4, 4), cuenta_titulo='La melodía y la izquierda, medidas',
        cuenta_pie='Arriba, los cc. 1-2 de la derecha. Abajo, los cc. 1-2 de la izquierda: '
                   'ocho corcheas por compás.',
        ritmos=[('LA DERECHA', 'cc. 1-2', _MEL, AZUL, 'treble', None),
                ('LA IZQUIERDA', 'cc. 1-2', _IZQ, OCRE, 'bass', None)]),
    manos=dict(
        titulo='Cada mano, por separado',
        sub='La izquierda manda y la derecha canta encima. Empieza por la izquierda.',
        tit_izq='MANO IZQUIERDA', tit_der='MANO DERECHA',
        izq=[('Solo la nota grave', 'Toca una nota por compás, la grave: Mi, La, Si, La. '
                                    'Cuenta ocho corcheas.'),
             ('Nota y octava', 'Alterna la grave y la misma una octava más aguda. La mano '
                               'casi no se mueve.'),
             ('Los ocho compases', 'cc. 1-4: Mi, La, Si, La. cc. 5-8: Re, Do, Si, La. '
                                   'La nota grave baja de uno en uno.'),
             ('Sin parar', 'Corcheas parejas, sin acelerar. Tócalo de memoria.')],
        der=[('Cántala', 'Mi, Si-Do, Re, Do-Si, La... Canta los nombres antes de tocar.'),
             ('Largo y corto', 'Dos corcheas valen una negra. En el c. 3, el Si dura un golpe '
                               'y medio y el Do cae en el "y" del 2. Igual en los cc. 6 y 7.'),
             ('El c. 5', 'Empieza con un silencio de corchea: entra en el "y" del 1.'),
             ('Notas largas', 'En los cc. 9-16 hay blancas y redondas. Cuéntalas enteras y '
                              'cuida el Sol sostenido.')],
        tecnica=['Muñeca suelta: las corcheas de la izquierda se tocan ligeras.',
                 'Cuenta "1-y-2-y-3-y-4-y" en voz alta.',
                 'La izquierda es el reloj: no se acelera cuando la derecha cambia.']),
    bloques=[
        B(1, 'cc. 1-4', 'La melodía', (0, 0),
          D('grupos', 'Un compás de 4/4 = 4 golpes de 2 corcheas', (4, 2, ['1', '2', '3', '4'])),
          [('IZQUIERDA', 'Mi, La, Si, La: nota grave y octava, ocho corcheas por compás.'),
           ('DERECHA', 'Mi, Si-Do, Re, Do-Si | La, La-Do, Mi, Re-Do | Si., Do, Re, Mi | Do, La, La.'),
           ('JUNTAS', 'Un compás cada vez; luego los cuatro.'),
           ('OJO', 'En el c. 3, el Si dura un golpe y medio.')]),
        B(2, 'cc. 5-8', 'La nota grave baja', (1, 1),
          D('cadena', 'El bajo, compás a compás', [('Re', False), ('Do', False), ('Si', False),
                                                   ('La', True)]),
          [('IZQUIERDA', 'Re, Do, Si, La: baja de uno en uno. La mano sigue con octavas.'),
           ('DERECHA', 'Silencio de corchea, Re, Fa, La, Sol-Fa | Mi., Do, Mi, Re-Do | Si., Do, Re, Mi | Do, La, La.'),
           ('JUNTAS', 'Los cc. 5-6, luego los cc. 7-8.'),
           ('OJO', 'El c. 5 empieza con un silencio de corchea.')]),
        B(3, 'cc. 9-12', 'Notas largas', (2, 2),
          D('cadena', 'Las blancas, por compás',
            [('Mi-Do', False), ('Re-Si', False), ('Do-La', False), ('Sol#', True)]),
          [('IZQUIERDA', 'La, Sol sostenido, La, Si. El c. 10 entero lleva Sol sostenido.'),
           ('DERECHA', 'Dos blancas por compás. El c. 12 es una redonda: Sol sostenido.'),
           ('JUNTAS', 'La derecha aguanta y la izquierda sigue en corcheas. Cuenta.'),
           ('OJO', 'Sol sostenido = tecla negra, a la derecha del Sol.')]),
        B(4, 'cc. 13-16', 'La subida', (3, 3),
          D('cadena', 'El camino', [('cc. 13-14 = cc. 9-10', False), ('Do Mi La La', False),
                                    ('Sol# agudo', True)]),
          [('IZQUIERDA', 'La, Si, Do, Si. Sube un poco y vuelve.'),
           ('DERECHA', 'Los cc. 13-14 son los cc. 9-10. En el c. 15: Do, Mi, La, La.'),
           ('JUNTAS', 'El c. 15 es el más difícil: las dos manos se mueven a la vez.'),
           ('OJO', 'El c. 16 es una redonda de Sol sostenido agudo.')]),
        B(5, 'cc. 17-20', 'Vuelve el principio', (4, 4),
          D('cadena', 'Es el bloque 1', [('cc. 17-20', True), ('= cc. 1-4', False)]),
          [('IZQUIERDA', 'Mi, La, Si, La, como al principio.'),
           ('DERECHA', 'La misma melodía de los cc. 1-4. Tócala de memoria.'),
           ('JUNTAS', 'Los cuatro compases seguidos, sin parar.'),
           ('A TEMPO', 'Del c. 1 al c. 20, sin detenerte en el c. 16.')]),
        B(6, 'cc. 21-24', 'Final', (5, 5),
          D('cadena', 'Casi igual a los cc. 5-8', [('cc. 21-23 = 5-7', False),
                                                   ('c. 24 distinto', True)]),
          [('IZQUIERDA', 'Re, Do, Si, La, como en los cc. 5-8.'),
           ('DERECHA', 'c. 24: silencio de corchea, Do, La corchea, La y silencio.'),
           ('JUNTAS', 'Para al final con calma, sobre La.'),
           ('A TEMPO', 'Toda la pieza, de principio a fin.')]),
    ],
    cortes={1: [244.8, 391.2, 541.8, 684.2]}, corte_titulo=96.5,
    fin={1: 822},
    burb={
        0: [('arriba', 280, 'DER', 'Empieza en Mi: una negra, dos corcheas pegadas, otra negra y '
                                   'dos corcheas. Cántala antes de tocar.', 0.1),
            ('abajo', 270, 'IZQ', 'Ocho corcheas por compás: la nota grave y su octava. Mi, La, '
                                  'Si, La.', 0.2)],
        1: [('arriba', 250, 'OJO', 'El c. 5 empieza con un silencio de corchea: entra en el '
                                   '"y" del 1.', 0.05),
            ('abajo', 280, 'IZQ', 'La nota grave baja de uno en uno: Re, Do, Si, La.', 0.5)],
        2: [('arriba', 270, 'DER', 'Blancas: dos golpes cada una. La derecha canta largo.', 0.1),
            ('abajo', 280, 'OJO', 'Sol sostenido (tecla negra): en la izquierda del c. 10 y '
                                  'en la derecha del c. 12.', 0.55)],
        3: [('arriba', 270, 'DER', 'Los cc. 13-14 repiten los cc. 9-10. En el c. 15 sube: Do, '
                                   'Mi, La, La.', 0.55),
            ('abajo', 270, 'OJO', 'c. 16: una redonda en Sol sostenido agudo. Cuenta cuatro '
                                  'golpes.', 0.9)],
        4: [('arriba', 300, 'AMB', 'Son los cc. 1-4 otra vez: ya la sabes. Tócala de memoria.',
             0.1)],
        5: [('arriba', 300, 'OJO', 'El c. 24 es distinto: silencio de corchea, Do, La corchea, '
                                   'La y silencio. Termina con calma.', 0.8)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de La menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tetris.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
