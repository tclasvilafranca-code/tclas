# -*- coding: utf-8 -*-
"""Pieza 13 · Elegy for the Arctic (Ludovico Einaudi). MEDIDO sobre el PDF (2 paginas carta,
   12 sistemas, 26 compases numerados): cuatro bemoles (si, mi, la, re bemol), "Con rubato" sin
   metronomo, semicorchea como figura mas corta; compases cambiantes impresos: 11/4 (c. 1), 10/4
   (c. 2), 7/4 (c. 3), 4/4 (c. 4), 6/4 (c. 7), 4/4 (c. 8), 5/4 (c. 9), 4/4 (c. 10), 6/4 (c. 25),
   13/4 (c. 26); matices mp, pp, mf, f, ff, mp, mp."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=13, slug='elegy', pdf='elegy_for_the_arctic_ludovico_einaudi_pd.pdf', time_sig=(4, 4),
    titulo='Elegy for the Arctic', autor='Ludovico Einaudi · edición de musicaparadisfrutar.com',
    kicker='Eva · pieza 13 · Elegy for the Arctic', mes='Mayo · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=einaudi+elegy+for+the+arctic+piano+tutorial',
    credito='Partitura: L. Einaudi, Elegy for the Arctic (musicaparadisfrutar.com). '
            'Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Armadura', '4 bemoles'), ('Compás', 'Cambia mucho'), ('Tempo', 'Con rubato'),
               ('Figura corta', 'Semicorchea'), ('Compases', '26')],
        total=26,
        secciones=[('A', 1, 11, 'Primera parte · hasta la doble barra', AZUL),
                   ('B', 12, 15, 'mf → f → ff', OCRE),
                   ('C', 16, 26, 'Vaivén en mp y final', AZUL)],
        ideas=[('LOS COMPASES', 'Cambian mucho',
                '11/4, 10/4, 7/4, 4/4, 6/4, 5/4 y 13/4. El normal es el 4/4.'),
               ('DERECHA', 'Grupos de cuatro',
                'Desde el c. 3, grupos de cuatro semicorcheas. En los cc. 1-2 y 26, notas dobles.'),
               ('IZQUIERDA', 'Bajos largos',
                'Notas y acordes largos, casi siempre ligados. En los cc. 14-15, semicorcheas.'),
               ('LOS MATICES', 'mp · pp · mf · f · ff',
                'pp en el c. 3, mf en el 12, f en el 14, ff en el 15 y mp en los cc. 17 y 26.')],
        especial=[
            'Pone "Con rubato" y no tiene metrónomo: el tempo es libre.',
            'La armadura tiene cuatro bemoles: si♭, mi♭, la♭ y re♭.',
            'Compás de 11/4 en el c. 1, 10/4 en el c. 2 y 13/4 en el c. 26.',
            'Hay doble barra entre los cc. 3 y 4 y entre los cc. 11 y 12.',
            'Aparece un becuadro en los cc. 19, 21, 23 y 25 (tercer grupo).',
            'El ff cae en el tercer tiempo del c. 15: el punto más fuerte.'],
        reto='Mantener los grupos de semicorcheas iguales y suaves mientras cambia el número '
             'de tiempos por compás. Cuenta siempre en negras.',
        truco='Antes de tocar, repasa solo los compases con compás distinto de 4/4 (cc. 1-3, 7, '
              '9, 25 y 26) y cuenta sus negras en voz alta.',
        sabias='Einaudi la tocó en 2016 sobre una plataforma flotante junto a un glaciar de Svalbard, en el Ártico, en una campaña de Greenpeace.',
        qr_texto='Escúchala con la partitura delante: fíjate en cuándo cambia el compás.',
        ts=(4, 4), cuenta_titulo='Cómo se cuenta el 4/4 (el compás más habitual)',
        cuenta_pie='Un compás de 4/4 contado en corcheas. En esta pieza cada golpe se reparte '
                   'en cuatro semicorcheas. Aquí solo el ritmo, sobre una nota cualquiera.'),
    manos=dict(
        izq=[('Notas largas', 'En los cc. 1-11 son notas y acordes largos. Cuenta sus negras y '
                              'mantén cada uno entero.'),
             ('Dos ritmos de acorde', 'En los cc. 4 y 6 la izquierda toca una blanca y dos '
                                      'negras. En los cc. 3 y 5, un solo acorde.'),
             ('La bajada', 'En los cc. 14-15 la izquierda toca semicorcheas que bajan, como la '
                           'derecha. Tócalas despacio.'),
             ('Negras y blancas', 'Del c. 18 al c. 24: cuatro negras en los compases pares y '
                                  'dos blancas en los impares.')],
        der=[('Un grupo, cuatro notas', 'Aprende un solo grupo de cuatro semicorcheas, despacio, '
                                        'diez veces seguidas sin fallar.'),
             ('Igual y suave', 'Metrónomo muy lento, las cuatro notas iguales. Ninguna debe '
                               'sobresalir.'),
             ('Cuando cambia', 'El dibujo cambia en los cc. 9 y 12. En los cc. 5 y 7 hay una '
                               'ligadura y un silencio de semicorchea.'),
             ('Con la izquierda', 'Une un sistema con la izquierda ya segura. Si se rompe, '
                                  'vuelve a una mano.')],
        tecnica=['Muñeca suelta: las semicorcheas salen solas si no aprietas.',
                 'Cuenta siempre en negras, aunque cambie el número de tiempos del compás.',
                 'El sonido va de pp a ff: guarda la fuerza para el c. 15.']),
    bloques=[
        B(1, 'cc. 1-2', 'La entrada', (0, 0),
          D('cuenta', 'Dos compases largos · cuenta negras',
            [('c. 1 · 11/4', 11, 1), ('c. 2 · 10/4', 10, 1)]),
          [('IZQUIERDA', 'Una sola nota muy grave en cada compás. Cuéntala entera.'),
           ('DERECHA', 'Notas dobles ligadas: una frase que acaba en nota larga y se repite.'),
           ('JUNTAS', 'La izquierda suena mientras la derecha dice su frase.'),
           ('A TEMPO', 'Con rubato: libre. El mp está impreso en el c. 2.')]),
        B(2, 'cc. 3-8', 'Semicorcheas y acordes', (1, 3),
          D('cuenta', '4/4 en semicorcheas · 4 golpes de 4 notas', [('un compás', 4, 4)]),
          [('IZQUIERDA', 'Acorde largo en el c. 3 y acorde de blanca y dos negras en el c. 4.'),
           ('DERECHA', 'Grupos de cuatro semicorcheas, en pp. Mismo dibujo en los cc. 3 y 4.'),
           ('JUNTAS', 'Un sistema cada día: cc. 3-4, 5-6 y 7-8.'),
           ('OJO', 'Compás: 7/4, 4/4, 6/4 y 4/4. Cuenta negras sin prisa.')]),
        B(3, 'cc. 9-11', 'Cambia el dibujo', (4, 4),
          D('cuenta', 'Los compases de este bloque',
            [('c. 9 · 5/4', 5, 4), ('c. 10 · 4/4', 4, 4)]),
          [('IZQUIERDA', 'Acordes largos con una ligadura grande de varios compases.'),
           ('DERECHA', 'Otro dibujo de cuatro semicorcheas, repetido en los tres compases.'),
           ('JUNTAS', 'Los tres compases en bucle, sin parar.'),
           ('OJO', 'Doble barra al final del c. 11: aquí acaba la primera parte.')]),
        B(4, 'cc. 12-13', 'mf: baja la derecha', (5, 5),
          D('cadena', 'Un compás de la derecha',
            [('3 grupos iguales', False), ('el cuarto baja', True)]),
          [('IZQUIERDA', 'Un acorde de cuatro notas, ligado de un compás al otro.'),
           ('DERECHA', 'Cada grupo baja de cuatro en cuatro. Tres iguales y un cuarto más bajo.'),
           ('JUNTAS', 'Los dos compases en bucle, en mf.'),
           ('OJO', 'La ligadura une todo el compás: toca con un gesto del brazo.')]),
        B(5, 'cc. 14-15', 'f y ff', (6, 6),
          D('cadena', 'El sonido sube',
            [('mf (c. 12)', False), ('f (c. 14)', False), ('ff (c. 15)', True)]),
          [('IZQUIERDA', 'Semicorcheas que bajan, igual que la derecha. Tócalas despacio.'),
           ('DERECHA', 'Bajan en grupos de cuatro; en el c. 15 hay una nota larga con ff.'),
           ('JUNTAS', 'Cuenta cuatro negras y llega al ff en el tercer tiempo del c. 15.'),
           ('OJO', 'El ff es el momento más fuerte de toda la pieza.')]),
        B(6, 'cc. 16-24', 'Vuelve el vaivén', (7, 10),
          D('capas', 'Dos capas a la vez',
            [('Derecha: semicorcheas', 'puntos', AZUL), ('Izquierda: negras', 'barras', OCRE)]),
          [('IZQUIERDA', 'Del c. 18 al 24: cuatro negras o dos blancas por compás.'),
           ('DERECHA', 'Mismo dibujo en grupos de cuatro, con una ligadura de dos compases.'),
           ('JUNTAS', 'Un sistema cada día: cc. 16-18, 19-20, 21-22 y 23-24.'),
           ('OJO', 'Becuadro en el tercer grupo de los cc. 19, 21 y 23.')]),
        B(7, 'cc. 25-26', 'El final', (11, 11),
          D('cuenta', 'Dos compases · cuenta negras',
            [('c. 25 · 6/4', 6, 1), ('c. 26 · 13/4', 13, 1)]),
          [('IZQUIERDA', 'Notas largas: cuéntalas enteras.'),
           ('DERECHA', 'En el c. 26 vuelve la frase de la entrada, en mp, hasta una nota larga.'),
           ('JUNTAS', 'Los dos compases, despacio, hasta la barra final.'),
           ('OJO', 'Compás de 13/4: cuenta trece negras sin prisa.')]),
    ],
    cortes={1: [238.8, 332.8, 428.8, 545.0, 654.5], 2: [196.0, 309.8, 420.0, 531.0, 632.5]},
    corte_titulo=131.8,
    burb={
        0: [('abajo', 330, 'AMB', 'Con rubato: libre. La izquierda tiene una nota larguísima por '
                                   'compás (11/4 y 10/4).', 0.2)],
        1: [('arriba', 330, 'DER', 'Aquí empiezan los grupos de cuatro semicorcheas, en pp. '
                                   'Despacio y parejo.', 0.3)],
        2: [('arriba', 330, 'DER', 'c. 5: una ligadura y un silencio de semicorchea antes de '
                                   'los tres últimos sonidos. Cuéntalo.', 0.45)],
        3: [('arriba', 330, 'OJO', 'c. 7: 6/4 (seis negras). Al final del c. 7 hay otra ligadura '
                                   'y otro silencio de semicorchea.', 0.1)],
        4: [('arriba', 330, 'OJO', 'c. 9: 5/4; cc. 10 y 11: 4/4. Doble barra al final del c. 11.',
             0.1)],
        5: [('arriba', 300, 'AMB', 'mf: la derecha baja de cuatro en cuatro y la izquierda '
                                   'sostiene un acorde ligado.', 0.15)],
        6: [('arriba', 330, 'OJO', 'f en el c. 14 y ff en el c. 15 (tercer tiempo). La izquierda '
                                   'copia la bajada de la derecha.', 0.4)],
        7: [('arriba', 330, 'AMB', 'mp en el c. 17. Desde el c. 18 la izquierda toca negras '
                                   'parejas y suaves.', 0.5)],
        8: [('arriba', 330, 'OJO', 'Becuadro en el tercer grupo del c. 19 (también en la '
                                   'izquierda). Se repite en los cc. 21, 23 y 25.', 0.25)],
        11: [('arriba', 330, 'OJO', 'c. 26: 13/4 y mp. Vuelve la frase de la entrada. La última '
                                    'nota lleva becuadro.', 0.65)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe una escala con 4 bemoles')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_elegy.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
