# -*- coding: utf-8 -*-
"""Pieza 11 · El Padrino (Nino Rota), arreglo para piano (escaneado a ~60 ppi). MEDIDO sobre el PDF
   a zoom (3 pags, A4, 14 sistemas, 51 compases numerados en el margen): 4/4 sin cambios de compas,
   armadura de tres bemoles y, tras la doble barra del c.33, seis bemoles; negra = 83 (c.1) y
   negra = 140 (c.32); letras A (c.1), A' (c.10), B (c.18), A (c.22), A'' (c.34); izquierda en
   silencio en los cc.1 y 10; tresillos de corcheas en la izquierda (cc.5-6 y 25-26); subida de
   semicorcheas ligadas en la izquierda (c.14); acordes arpegiados (linea ondulada); matices mp,
   mf, f, p, sf; "accelerando poco a poco" (c.29); calderon (c.32); semicorchea la figura corta.
   El credito del arreglista se lee 'ANDRE JAHJAH' pero el escaneo es borroso: no se imprime."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=11, slug='padrino', pdf='el_padrino.pdf', time_sig=(4, 4),
    titulo='El Padrino', autor='Nino Rota · arreglo para piano',
    kicker='Eva · pieza 11 · El Padrino', mes='Abril · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=el+padrino+the+godfather+nino+rota+piano+tutorial',
    credito='Partitura: N. Rota, El Padrino (arreglo para piano). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do menor → 6 bemoles'), ('Compás', '4/4'),
               ('Tempo', '♩=83 → ♩=140'), ('Figura corta', 'Semicorchea'), ('Compases', '51')],
        total=51,
        secciones=[('A', 1, 9, 'El tema', AZUL), ('A\'', 10, 17, 'Acordes arpegiados', OCRE),
                   ('B', 18, 21, 'Nueva', AZUL), ('A', 22, 33, 'Vuelve y acelera', OCRE),
                   ('A\'\'', 34, 51, 'Seis bemoles · ♩=140', AZUL)],
        ideas=[('IZQUIERDA', 'Bajo, tresillos y silencios',
                'Calla en el c. 1; después, bajo y acordes cortos. Tresillos de corcheas en los '
                'cc. 5-6 y 25-26.'),
               ('DERECHA', 'El tema, entre silencios',
                'Entra tras un silencio, en corcheas, y más adelante lleva acordes con línea '
                'ondulada (arpegio).'),
               ('EL CAMBIO', 'Más rápido',
                '"accelerando poco a poco" en el c. 29, ♩=140 en el c. 32 y seis bemoles desde el '
                'c. 34.'),
               ('LOS MATICES', 'mp · mf · f · p · sf',
                'Empieza en mp, crece a mf y f, baja a p en la letra B y vuelve a subir.')],
        especial=[
            'Pone negra = 83 al principio y negra = 140 en el c. 32.',
            'Es 4/4 de principio a fin: no hay cambios de compás.',
            'Tres bemoles (si♭, mi♭, la♭); tras la doble barra del c. 33 pasa a seis.',
            'Letras: A (c. 1), A\' (c. 10), B (c. 18), A (c. 22) y A\'\' (c. 34).',
            'La izquierda calla en los cc. 1 y 10 y hace tresillos en los cc. 5-6 y 25-26.',
            'Hay acordes con línea ondulada (arpegio), "accelerando" en el c. 29 y calderón en el '
            'c. 32.'],
        reto='Controlar el cambio de ritmo: de ♩=83 a la aceleración del c. 29 y al ♩=140 sin que '
             'se te escape la mano.',
        truco='Estudia por letras, una por día: A (cc. 1-9), A\' (cc. 10-17), B (cc. 18-21)... '
              'Los tresillos, solos y despacio, diciendo "tre-si-llo".',
        sabias='La música de El Padrino (1972) es de Nino Rota, que compuso muchas bandas sonoras '
               'de cine italiano. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchalo con la partitura delante: ¿notas dónde acelera?', ts=(4, 4)),
    manos=dict(
        izq=[('Calla y entra', 'En los cc. 1 y 10 la izquierda no toca. Del c. 2: bajo y acordes '
                               'cortos; en el c. 3 sube en cuatro corcheas hasta una blanca.'),
             ('Los tresillos', 'En los cc. 5-6 hay dos tresillos de corcheas (tres notas por '
                               'tiempo) y una blanca. Di "tre-si-llo" y sube con el regulador.'),
             ('La subida del c. 14', 'Ocho semicorcheas ligadas que suben hasta una blanca. '
                                     'Estúdialas sola, muy despacio, y acelera poco a poco.'),
             ('Acordes y calderón', 'En los cc. 29-33 son acordes. En el c. 32 baja en ocho '
                                    'corcheas con calderón en la primera nota.')],
        der=[('Entrar a destiempo', 'En el c. 1 hay silencio de blanca y de corchea, y entran tres '
                                    'corcheas. Cuenta 1-2-3-y y entra en el "y".'),
             ('Tres corcheas al final', 'En los cc. 5-7 cada compás acaba con tres corcheas que '
                                        'suben: es el mismo gesto, aprendido una vez.'),
             ('Acordes arpegiados', 'En los cc. 10-17 hay acordes con línea ondulada: toca las '
                                    'notas de abajo arriba, rápido, y sigue con las corcheas.'),
             ('La aceleración', 'Los cc. 29-30 son semicorcheas de mp a f. Empieza lenta y sube '
                                'la velocidad poco a poco.')],
        tecnica=['Cuenta 1-2-3-4 y no te saltes los silencios.',
                 'Acelera poco a poco, no de golpe: primero lento, luego rápido.',
                 'Los acordes arpegiados, con la muñeca suelta y sin apretar.']),
    bloques=[
        B(1, 'cc. 1-4', 'El tema en mp', (0, 0),
          D('cadena', 'Lo primero', [('♩=83', False), ('mp', False), ('regulador < a mf (c. 3)', True)]),
          [('IZQUIERDA', 'Calla en el c. 1. Bajo y acordes cortos; en el c. 3 sube en 4 corcheas.'),
           ('DERECHA', 'Silencio de blanca y de corchea, y entran tres corcheas. Cuenta 1-2-3-y.'),
           ('JUNTAS', 'Cuenta 1-2-3-y y entra la derecha; la izquierda no toca hasta el c. 2.'),
           ('A TEMPO', 'Negra = 83: lento. Empieza en mp y crece hacia mf.')]),
        B(2, 'cc. 5-8', 'Los tresillos', (1, 1),
          D('grupos', 'Tresillo: 3 notas en un tiempo', (2, 3, ['tre-si-llo', 'tre-si-llo'])),
          [('IZQUIERDA', 'Cc. 5-6: dos tresillos de corcheas y una blanca. Cc. 7-8: seis corcheas '
                         'y cuatro negras.'),
           ('DERECHA', 'Cada compás cierra con tres corcheas que suben (cc. 5-7).'),
           ('JUNTAS', 'Una mano cuenta "tre-si-llo" mientras la otra toca las tres corcheas.'),
           ('OJO', 'mp en el c. 5 y mf en el c. 6: sube el sonido con el regulador.')]),
        B(3, 'cc. 9-12', 'Acordes arpegiados (A\')', (2, 2),
          D('cadena', 'La letra A\'', [('f y mp (c. 9)', False), ('A\' en el c. 10', False),
                                      ('acorde arpegiado', True)]),
          [('IZQUIERDA', 'Nota larga en el c. 9, silencio en el c. 10, y luego negra y blanca.'),
           ('DERECHA', 'Dos voces: arriba corcheas, abajo negras, con arpegios.'),
           ('JUNTAS', 'Solo el c. 9 y el c. 10; después el c. 11.'),
           ('OJO', 'La línea ondulada: toca las notas de abajo arriba, rápido.')]),
        B(4, 'cc. 13-16', 'La subida del c. 14', (3, 3),
          D('cadena', 'Los cc. 13-16', [('acordes (c. 13)', False), ('subida en semicorcheas', False),
                                        ('f y acordes (c. 15)', True)]),
          [('IZQUIERDA', 'C. 14: ocho semicorcheas ligadas que suben a una blanca. Despacio.'),
           ('DERECHA', 'Acordes arpegiados y tres corcheas al final de cada compás.'),
           ('JUNTAS', 'Un compás cada vez, y los cuatro seguidos.'),
           ('OJO', 'f en el c. 15 y acordes con sostenidos en la izquierda.')]),
        B(5, 'cc. 17-24', 'La parte B y vuelta de A', (4, 5),
          D('cadena', 'El cambio', [('doble barra: B en p (c. 18)', False),
                                    ('vuelve A en mf (c. 22)', True)]),
          [('IZQUIERDA', 'En la B sube y baja en ocho corcheas por compás. En el c. 22 vuelve el '
                         'bajo del tema.'),
           ('DERECHA', 'La B empieza con una blanca y corcheas en p; léela despacio.'),
           ('JUNTAS', 'La B compás a compás; la A ya la conoces.'),
           ('OJO', 'Sostenidos en el c. 20 (dos semicorcheas en la izquierda).')]),
        B(6, 'cc. 25-33', 'Se acelera', (6, 8),
          D('cadena', 'Hacia el cambio', [('tresillos (cc. 25-26)', False),
                                          ('accelerando (c. 29)', False),
                                          ('♩=140 y calderón (c. 32)', True)]),
          [('IZQUIERDA', 'Tresillos en los cc. 25-26, luego acordes y en el c. 32 ocho corcheas '
                         'que bajan.'),
           ('DERECHA', 'Semicorcheas en los cc. 29-30, de mp a f; sf en los cc. 31-33.'),
           ('JUNTAS', 'Empieza lento y aprieta poco a poco.'),
           ('A TEMPO', 'Calderón en el c. 32; después, negra = 140.')]),
        B(7, 'cc. 34-41', 'Seis bemoles (A\'\')', (9, 10),
          D('cadena', 'Lo que cambia', [('doble barra', False), ('seis bemoles', False),
                                         ('♩=140 en f', True)]),
          [('IZQUIERDA', 'El mismo bajo del tema, ahora con seis bemoles.'),
           ('DERECHA', 'El tema en f, en corcheas; acordes y blancas entre las frases.'),
           ('JUNTAS', 'Un sistema cada día: cc. 34-37 y cc. 38-41.'),
           ('OJO', 'Seis bemoles al principio de cada pentagrama; mp en el c. 41.')]),
        B(8, 'cc. 42-51', 'El final', (11, 13),
          D('cadena', 'Hacia el final', [('mp (c. 45)', False), ('mf (c. 48)', False),
                                         ('mp (c. 49)', False), ('acorde final', True)]),
          [('IZQUIERDA', 'Mismo bajo; en los cc. 50-51 solo blancas.'),
           ('DERECHA', 'Corcheas bajo una ligadura larga y acordes arpegiados al final.'),
           ('JUNTAS', 'Tres sistemas: cc. 42-45, 46-49 y 50-51.'),
           ('A TEMPO', 'Doble barra final: aguanta el último acorde.')]),
    ],
    cortes={1: [320.0, 452.0, 600.0], 2: [212.5, 333.0, 454.5, 588.2],
            3: [225.5, 351.5, 475.5, 605.0]},
    corte_titulo=184.5, fin={2: 730.0, 3: 736.0},
    burb={
        0: [('arriba', 330, 'AMB', 'Negra = 83, 4/4 y tres bemoles. Empieza en mp: la izquierda '
                                   'calla y la derecha entra con tres corcheas.', 0.12)],
        1: [('arriba', 330, 'IZQ', 'Tresillos en los cc. 5-6: tres notas en cada tiempo, y sube '
                                   'con el regulador hasta mf.', 0.12)],
        2: [('arriba', 330, 'DER', 'Letra A\': acordes con línea ondulada, toca de abajo arriba. '
                                   'La izquierda calla en el c. 10.', 0.32)],
        3: [('arriba', 330, 'IZQ', 'C. 14: subida de ocho semicorcheas ligadas, despacio y '
                                   'parejas. En el c. 15 llega f.', 0.35)],
        4: [('arriba', 300, 'AMB', 'Doble barra: empieza la B en p (c. 18). La izquierda sube y '
                                   'baja en corcheas.', 0.35)],
        6: [('arriba', 300, 'IZQ', 'Otra vez los tresillos (cc. 25-26), como en los cc. 5-6.',
             0.12)],
        7: [('arriba', 330, 'OJO', '"accelerando poco a poco": semicorcheas de mp a f; sube la '
                                   'velocidad despacio.', 0.2)],
        8: [('arriba', 330, 'AMB', 'C. 32: calderón y ♩=140. Tras la doble barra del c. 33, '
                                   'seis bemoles.', 0.5)],
        9: [('arriba', 330, 'AMB', 'Letra A\'\' en f: seis bemoles y ♩=140. Es el tema otra vez.',
             0.1)],
        12: [('arriba', 330, 'OJO', 'mf en el c. 48 y mp en el c. 49: el sonido baja de golpe.',
              0.5)],
        13: [('arriba', 330, 'AMB', 'Corcheas bajo una ligadura larga y acordes arpegiados. Fin.',
              0.4)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_padrino.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
