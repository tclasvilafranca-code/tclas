# -*- coding: utf-8 -*-
"""Pieza 13 · Can't Stop the Feeling! (Justin Timberlake). MEDIDO sobre el PDF de Drive de Sharifa:
   1 pagina apaisada y girada 90 grados (imagen de 79 ppp) con 17 compases en 3 sistemas (6+6+5),
   sin armadura ni alteraciones, 4/4, sin tempo ni matices, corchea como figura mas corta.
   Derecha: solo Do4, Re4, Mi4 y un Sol4 (c. 6). Izquierda: La3, Sol3 y un Mi3 (c. 9); silencio de
   compas entero en los cc. 1, 4, 8 y 17. El PDF se gira con PyMuPDF y se recoloca en filas mas
   cortas (cc. 1-4, 5-6, 7-9, 10-12, 13-15, 16-17): ver _cs_prep.py (se genera solo)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
import _cs_prep

_cs_prep.preparar(os.path.join(SRCDIR, 'copia_de_can_t_stop_the_feeling.pdf'),
                  os.path.join(SRCDIR, 'cant_stop_recto.pdf'))


def _n(p, d='e', b=None):
    ev = {'pitch': p, 'dur': d}
    if b is not None:
        ev['beam'] = b
    return ev


def _r(d='e'):
    return {'rest': True, 'dur': d}


# cc. 10 medidos: derecha Do, silencio x3 + silencio de negra; izquierda silencio, La, ... La Sol La
_DER = [_n('C4'), _r(), _n('C4'), _r(), _n('C4'), _r(), _r('q')]
_IZQ = [_r(), _n('A3'), _r(), _n('A3'), _r(), _n('A3', 'e', 0), _n('G3', 'e', 0), _n('A3', 'e', 0)]

SPEC = dict(
    num=13, slug='cant_stop', pdf='cant_stop_recto.pdf', time_sig=(4, 4),
    titulo="Can't Stop the Feeling!", autor='Justin Timberlake · de la película "Trolls" (2016)',
    kicker="Sharifa · pieza 13 · Can't Stop the Feeling!", mes='Junio · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=cant+stop+the+feeling+piano+tutorial',
    credito="Partitura: Can't Stop the Feeling! (Drive), girada y recolocada. Anotaciones: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Tempo', 'Sin indicar'),
               ('Figura corta', 'Corchea'), ('Compases', '17')],
        total=17,
        secciones=[('A', 1, 4, 'La frase', AZUL), ('A', 5, 8, 'Vuelve y sube a Sol', AZUL),
                   ('B', 9, 17, 'Golpes sueltos y final', OCRE)],
        ideas=[('LA DERECHA', 'Do, Re, Mi y Sol',
                'Cuatro notas vecinas, casi todas corcheas. Solo teclas blancas.'),
               ('LA IZQUIERDA', 'La y Sol',
                'Entra poco a poco: un La suelto, y desde el c. 9 La, Sol y (una vez) Mi.'),
               ('LOS SILENCIOS', 'Marcan el ritmo',
                'Hay muchos silencios. Cuéntalos en voz alta: son parte de la música.'),
               ('EL VAIVÉN', 'Do · silencio · Do',
                'En los cc. 10, 12, 14 y 16 la derecha cae en el pulso y la izquierda, en el '
                '"y".')],
        especial=[
            'No lleva armadura ni alteraciones: solo teclas blancas.',
            'El compás es 4/4. No trae tempo ni matices.',
            'Las manos están cerca: la derecha en torno al Do central y la izquierda en el La '
            'de debajo.',
            'La izquierda descansa un compás entero en los cc. 1, 4, 8 y 17; la derecha, en el '
            'c. 9.',
            'Acaba en Do (negra con puntillo) y silencios.'],
        reto='Que las manos se turnen sin pisarse: la derecha en el pulso, la izquierda en el "y".',
        truco='Cuenta "1-y-2-y-3-y-4-y" y da palmas del c. 10: palma fuerte en el pulso, floja en '
              'el "y". Luego, solo la derecha.',
        sabias='Justin Timberlake la escribió con Max Martin y Shellback para la película "Trolls" '
               '(2016) y fue nominada al Óscar a la mejor canción original.',
        qr_texto='Escucha el estribillo y marca el pulso con el pie: la derecha cae sobre él.',
        ts=(4, 4), cuenta_titulo='El vaivén del c. 10, medido',
        cuenta_pie='Un compás de cada mano: la derecha toca en el pulso y la izquierda, en el '
                   '"y" que hay entre pulso y pulso.',
        ritmos=[('LA DERECHA', 'c. 10', _DER, AZUL, 'treble', None),
                ('LA IZQUIERDA', 'c. 10', _IZQ, OCRE, 'bass', None)]),
    manos=dict(
        titulo='Cada mano, por separado',
        sub='Pocas notas y muchos silencios: cuenta bien y todo sale.',
        tit_izq='MANO IZQUIERDA', tit_der='MANO DERECHA',
        izq=[('Cuenta los silencios', 'Los cc. 1 y 4 no se toca nada. Cuenta 1-2-3-4 en voz '
                                      'alta con el compás vacío.'),
             ('Un solo La', 'Cc. 2-6: un La por compás. Cae en el 1 (cc. 3 y 5) o en el "y" '
                            'del 3 (cc. 2 y 6).'),
             ('La, Mi, Sol, La', 'El c. 9 es el más movido. Aprende solo ese compás, despacio.'),
             ('El vaivén', 'Cc. 10, 12, 14, 16: La, La, y La-Sol-La. Siempre en el "y".')],
        der=[('Cuatro notas', 'Do, Re, Mi y Sol, con la mano abierta y cómoda en una posición.'),
             ('Entrar tarde', 'Los cc. 1, 3 y 5 empiezan con silencio: cuenta y entra en el "y" '
                              'del 3.'),
             ('La escalerita', 'Cc. 4 y 8: Mi, Re, Do, Re, Mi, Re, Do, Do. Ocho corcheas '
                               'parejas.'),
             ('Do, silencio', 'Cc. 10, 12, 14, 16: Do, silencio, tres veces. El silencio vale '
                              'lo mismo que la nota.')],
        tecnica=['Muñeca suelta: las corcheas, ligeras, sin golpear.',
                 'Cuenta "1-y-2-y-3-y-4-y" en voz alta, también en los silencios.',
                 'Las manos casi no se mueven: quédate cerca del Do central.']),
    bloques=[
        B(1, 'cc. 1-4', 'La frase de entrada', (0, 0),
          D('grupos', 'Cuenta: 1-y-2-y-3-y-4-y', (4, 2, ['1 y', '2 y', '3 y', '4 y'])),
          [('IZQUIERDA', 'c. 1 y c. 4: silencio. En los cc. 2 y 3, un solo La.'),
           ('DERECHA', 'Dos tiempos y medio de silencio, y entran Mi, Re, Do. En el c. 4: '
                       'Mi, Re, Do, Re, Mi, Re, Do, Do.'),
           ('JUNTAS', 'Un compás cada vez; el c. 4, solo con la derecha.'),
           ('OJO', 'En el c. 3 la derecha entra con Do, Do, Re.')]),
        B(2, 'cc. 5-6', 'Vuelve la frase y sube a Sol', (1, 1),
          D('cadena', 'En el c. 6', [('Mi', False), ('Sol', True)]),
          [('IZQUIERDA', 'Un La en el 1 (c. 5) y otro en el "y" del 3 (c. 6).'),
           ('DERECHA', 'c. 5 como el c. 1. En el c. 6: Mi y Sol (suben), dos silencios y Do, Do.'),
           ('JUNTAS', 'Los dos compases en bucle.'),
           ('OJO', 'El salto de Mi a Sol se salta el Fa: mira la mano.')]),
        B(3, 'cc. 7-9', 'La escalerita y el c. 9', (2, 2),
          D('cadena', 'En el c. 9', [('La', False), ('Mi', False), ('Sol', False),
                                     ('La', True)]),
          [('IZQUIERDA', 'c. 7: La y La. c. 8: silencio. c. 9: La, silencio, Mi, Sol, La.'),
           ('DERECHA', 'c. 7: Do, Re. c. 8: Mi, Re, Do, Re, Mi, Re, Do, Do. c. 9: silencio.'),
           ('JUNTAS', 'Primero el c. 7, luego el c. 9, y al final los tres.'),
           ('OJO', 'El c. 9: la izquierda se mueve y la derecha calla.')]),
        B(4, 'cc. 10-12', 'Do, silencio, Do', (3, 3),
          D('fichas', 'Un compás de 4 tiempos: Do = derecha · La y Sol = izquierda',
            ['1 Do', 'y La', '2 Do', 'y La', '3 Do', 'y La', '4 Sol', 'y La']),
          [('IZQUIERDA', 'c. 10: silencio, La, silencio, La, silencio, La, Sol, La.'),
           ('DERECHA', 'c. 10: Do, silencio, tres veces. c. 11: Do, Do, Do, Do, Mi.'),
           ('JUNTAS', 'Cuenta "1-y-2-y": la derecha en el número, la izquierda en el "y".'),
           ('OJO', 'En el c. 11 la izquierda entra al final con Sol y La.')]),
        B(5, 'cc. 13-15', 'Sol y La, y otra vez el vaivén', (4, 4),
          D('cadena', 'El camino', [('c. 13 Do suelto', False), ('c. 14 vaivén', False),
                                    ('c. 15 con Mi', True)]),
          [('IZQUIERDA', 'c. 13: silencio y, al final, Sol y La. c. 14 como el c. 10.'),
           ('DERECHA', 'c. 13: Do y dos tiempos de silencio. c. 15: Do, Do, Do, Mi.'),
           ('JUNTAS', 'Del c. 13 al c. 14: el Sol-La de la izquierda lanza el vaivén.'),
           ('OJO', 'c. 15: la izquierda toca La en el "y" del 1 y acaba con Sol y La.')]),
        B(6, 'cc. 16-17', 'El final', (5, 5),
          D('cadena', 'El final', [('c. 16 vaivén', False), ('Do largo', True),
                                   ('silencio', False)]),
          [('IZQUIERDA', 'c. 16: el vaivén de siempre. c. 17: silencio.'),
           ('DERECHA', 'c. 16: Do, silencio, tres veces. c. 17: Do (negra con puntillo).'),
           ('JUNTAS', 'Para en el c. 17: suelta el Do y deja que se apague.'),
           ('A TEMPO', 'Toda la pieza, contando los silencios.')]),
    ],
    cortes={1: [248.2, 392.2], 2: [168.2, 312.2]}, corte_titulo=98.2,
    burb={
        0: [('arriba', 290, 'DER', 'Dos tiempos y medio de silencio, y entran Mi, Re, Do. Cuenta '
                                   'antes de entrar.', 0.2),
            ('abajo', 270, 'IZQ', 'Los cc. 1 y 4 son silencio. En los cc. 2 y 3, un solo La.',
             0.44)],
        1: [('arriba', 250, 'DER', 'En el c. 6 la melodía sube de Mi a Sol.', 0.33),
            ('abajo', 270, 'IZQ', 'Un La en el 1 (c. 5) y otro en el "y" del 3 (c. 6).', 0.42)],
        2: [('arriba', 270, 'OJO', 'c. 8: ocho corcheas seguidas, Mi Re Do Re, Mi Re Do Do. La '
                                   'izquierda calla.', 0.39),
            ('abajo', 340, 'IZQ', 'c. 9: La, silencio, Mi, Sol, La. La derecha calla.', 0.57)],
        3: [('arriba', 280, 'AMB', 'La derecha cae en el pulso y la izquierda en el "y": se '
                                   'turnan.', 0.17),
            ('abajo', 270, 'OJO', 'c. 11: cuatro Do y un Mi. La izquierda entra al final: Sol, '
                                  'La.', 0.44)],
        4: [('arriba', 250, 'DER', 'c. 13: un Do y dos tiempos de silencio.', 0.09),
            ('abajo', 270, 'IZQ', 'c. 13: solo Sol y La, al final del compás.', 0.22)],
        5: [('arriba', 290, 'OJO', 'c. 17: el último Do dura una negra con puntillo; luego, '
                                   'silencio. Fin.', 0.42)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_cant_stop.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
