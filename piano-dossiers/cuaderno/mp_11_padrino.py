# -*- coding: utf-8 -*-
"""Pieza 11 · El Padrino (Nino Rota), arreglo de Andre Jaklab (escaneado). MEDIDO sobre el PDF (3 pags,
   A4, 14 sistemas, 51 compases numerados): 4/4, armadura de tres bemoles, negra = 83; letras A (c.1),
   A' (c.10), B (c.18), A (c.22) y A'' (c.34); tresillos en la izquierda (cc.5-6 y 25-26); lineas
   onduladas de arpegio en acordes; matices mp, mf, f, p, sf; "accelerando poco a poco" (c.29),
   negra = 140 y calderon (c.32); doble barra y armadura de seis bemoles en el c.34; semicorchea."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=11, slug='padrino', pdf='el_padrino.pdf', time_sig=(4, 4),
    titulo='El Padrino', autor='Nino Rota · arreglo para piano de André Jaklab',
    kicker='Eva · pieza 11 · El Padrino', mes='Abril · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=el+padrino+the+godfather+nino+rota+piano+tutorial',
    credito='Partitura: N. Rota, El Padrino (arreglo para piano). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do menor → 6 bemoles'), ('Compás', '4/4'),
               ('Tempo', '♩=83 → ♩=140'), ('Figura corta', 'Semicorchea'), ('Compases', '51')],
        total=51,
        secciones=[('A', 1, 9, 'El tema', AZUL), ('A\'', 10, 17, 'Acordes arpegiados', OCRE),
                   ('B', 18, 21, 'Nueva', AZUL), ('A', 22, 33, 'Vuelve y se acelera', OCRE),
                   ('A\'\'', 34, 51, 'Seis bemoles · ♩=140', AZUL)],
        ideas=[('IZQUIERDA', 'Bajo y tresillos',
                'Notas sueltas y acordes cortos; en los cc. 5-6 y 25-26 hay tresillos (3 notas en '
                'el tiempo de dos).'),
               ('DERECHA', 'El tema, entre silencios',
                'La melodía entra tras un silencio, en corcheas, y más adelante lleva acordes con '
                'línea ondulada (arpegio).'),
               ('EL CAMBIO', 'Más rápido',
                '"accelerando poco a poco" en el c. 29, ♩=140 en el c. 32 y seis bemoles desde el '
                'c. 34.'),
               ('LOS MATICES', 'mp · mf · f · p · sf',
                'Empieza en mp, crece a mf y f, baja a p en la letra B y vuelve a subir.')],
        especial=[
            'Pone negra = 83 al principio y negra = 140 en el c. 32.',
            'El compás es 4/4: cuatro negras por compás, sin cambios de compás.',
            'Armadura de tres bemoles; en el c. 34 cambia a seis bemoles (doble barra).',
            'Letras A, A\', B, A y A\'\' marcan las partes: mira dónde empieza cada una.',
            'Tresillos en la izquierda (cc. 5-6 y 25-26) y semicorcheas rápidas (c. 29-30).',
            'Calderón en el c. 32: se alarga la nota antes de seguir.'],
        reto='Controlar el cambio de ritmo: de ♩=83 a la aceleración del c. 29 y al ♩=140 sin que '
             'se te escape la mano.',
        truco='Estudia por partes: A (cc. 1-9), A\' (cc. 10-17), B (cc. 18-21)... Cada parte, un '
              'día. Los tresillos, solos y despacio, diciendo "tre-si-llo".',
        sabias='La música de El Padrino (1972) es de Nino Rota, que compuso muchas bandas sonoras '
               'de cine italiano. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchalo con la partitura delante: ¿notas dónde acelera?', ts=(4, 4)),
    manos=dict(
        izq=[('El bajo del tema', 'Al principio son notas sueltas y acordes cortos, con una subida '
                                  'de corcheas en el c. 3. Tócalo solo, contando 1-2-3-4.'),
             ('Los tresillos', 'En los cc. 5-6 y 25-26 tocas tres notas en el tiempo de dos. Di '
                               '"tre-si-llo" en voz alta y ve despacio.'),
             ('La subida del c. 14', 'En el c. 14 sube en notas rápidas y ligadas. Estúdiala sola '
                                     'y despacio, con el metrónomo lento.'),
             ('Acordes para acelerar', 'En los cc. 29-33 son acordes que acompañan la aceleración. '
                                       'Ojo al calderón del c. 32.')],
        der=[('Entrar tras el silencio', 'El tema entra después de un silencio. Cuéntalo entero '
                                         'antes de tocar la primera nota.'),
             ('El tema en corcheas', 'Aprende cada frase corta con su silencio. Cántala por '
                                     'dentro para que no se frene.'),
             ('Acordes arpegiados', 'En los cc. 10-17 hay acordes con línea ondulada: tócalos de '
                                    'abajo arriba, rápido, como un pequeño arpegio.'),
             ('La aceleración', 'Los cc. 29-30 son semicorcheas de mp a f. Empieza lenta y sube '
                                'la velocidad poco a poco.')],
        tecnica=['Cuenta 1-2-3-4 y no te saltes los silencios.',
                 'Acelera poco a poco, no de golpe: primero lento, luego rápido.',
                 'Los acordes arpegiados, sueltos de muñeca y sin apretar.']),
    bloques=[
        B(1, 'cc. 1-8', 'El tema (A)', (0, 1),
          D('cadena', 'Lo primero', [('♩=83', False), ('mp', False), ('crece a mf', True)]),
          [('IZQUIERDA', 'Bajo con notas sueltas y acordes cortos; en el c. 3 sube en corcheas.'),
           ('DERECHA', 'Entra tras un silencio. Frases cortas en corcheas, en mp.'),
           ('JUNTAS', 'Cuatro compases y después los otros cuatro.'),
           ('OJO', 'Tresillos en la izquierda en los cc. 5-6.')]),
        B(2, 'cc. 9-16', 'Acordes arpegiados (A\')', (2, 3),
          D('cadena', 'La letra A\'', [('f', False), ('acordes con línea ondulada', False),
                                       ('subida del c. 14', True)]),
          [('IZQUIERDA', 'Notas largas y acordes; en el c. 14 una subida rápida y ligada.'),
           ('DERECHA', 'Los acordes con línea ondulada se tocan de abajo arriba.'),
           ('JUNTAS', 'Un sistema cada día.'),
           ('OJO', 'f en el c. 9 y mp en el mismo compás: baja el sonido.')]),
        B(3, 'cc. 17-24', 'La parte B y vuelta de A', (4, 5),
          D('cadena', 'El cambio', [('B en p (c. 18)', False), ('vuelve A en mf (c. 22)', True)]),
          [('IZQUIERDA', 'En la B, corcheas que suben y bajan; en la A vuelve el bajo.'),
           ('DERECHA', 'La B es nueva: léela despacio. En el c. 22 vuelve el tema.'),
           ('JUNTAS', 'Compás a compás en la B.'),
           ('OJO', 'p en el c. 18 y mf en el c. 22.')]),
        B(4, 'cc. 25-33', 'Se acelera', (6, 8),
          D('cadena', 'Hacia el cambio', [('tresillos', False), ('accelerando', False),
                                          ('♩=140 y calderón', True)]),
          [('IZQUIERDA', 'Tresillos en los cc. 25-26 y después acordes.'),
           ('DERECHA', 'Semicorcheas en los cc. 29-30, de mp a f.'),
           ('JUNTAS', 'Empieza lento y aprieta poco a poco.'),
           ('A TEMPO', 'En el c. 32 hay calderón y ♩=140.')]),
        B(5, 'cc. 34-41', 'Seis bemoles (A\'\')', (9, 10),
          D('cadena', 'Lo que cambia', [('doble barra', False), ('seis bemoles', False),
                                         ('♩=140 en f', True)]),
          [('IZQUIERDA', 'Mismo bajo del tema, con la nueva armadura.'),
           ('DERECHA', 'El tema vuelve en f; mira las notas de la armadura.'),
           ('JUNTAS', 'Un sistema cada día.'),
           ('OJO', 'Seis bemoles al principio de cada pentagrama.')]),
        B(6, 'cc. 42-51', 'El final', (11, 13),
          D('cadena', 'Hacia el final', [('mp', False), ('mf', False), ('mp', False),
                                         ('acorde final', True)]),
          [('IZQUIERDA', 'Más acordes; al final notas largas.'),
           ('DERECHA', 'Ligaduras largas en los cc. 50-51: cántalas.'),
           ('JUNTAS', 'Tres sistemas: cc. 42-45, 46-49 y 50-51.'),
           ('A TEMPO', 'Termina con el acorde del c. 51.')]),
    ],
    cortes={1: [320.0, 452.0, 600.0], 2: [212.5, 333.0, 454.5, 588.2],
            3: [225.5, 351.5, 475.5, 605.0]},
    corte_titulo=184.5, fin={2: 730.0, 3: 736.0},
    burb={
        0: [('arriba', 330, 'AMB', 'Negra = 83, 4/4 y tres bemoles. El tema entra tras un silencio, '
                                   'en mp.', 0.15)],
        1: [('arriba', 300, 'IZQ', 'Tresillos en los cc. 5-6: tres notas en el tiempo de dos.',
             0.1)],
        2: [('arriba', 330, 'DER', 'Letra A\': acordes con línea ondulada, de abajo arriba.',
             0.35)],
        4: [('arriba', 300, 'AMB', 'Letra B en p (c. 18) y vuelve A en mf (c. 22).', 0.45)],
        7: [('arriba', 330, 'OJO', '"accelerando poco a poco": de mp a f, sube la velocidad '
                                   'despacio.', 0.2)],
        8: [('arriba', 330, 'AMB', 'c. 32: ♩=140 y calderón. Tras la doble barra, seis bemoles.',
             0.5)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_padrino.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
