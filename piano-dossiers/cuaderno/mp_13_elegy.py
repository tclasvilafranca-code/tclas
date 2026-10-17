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
        secciones=[('A', 1, 2, 'Entrada', AZUL),
                   ('B', 3, 8, 'Semicorcheas y acordes', OCRE),
                   ('C', 9, 11, 'Cambio', AZUL),
                   ('D', 12, 15, 'Bajada: mf, f, ff', OCRE),
                   ('E', 16, 24, 'Vuelve el vaivén · mp', AZUL),
                   ('F', 25, 26, 'Final', OCRE)],
        ideas=[('LOS COMPASES', 'Cambian mucho',
                'La partitura imprime 11/4, 10/4, 7/4, 4/4, 6/4, 5/4 y 13/4. Lo normal es el 4/4; '
                'los otros solo alargan o acortan el compás.'),
               ('DERECHA', 'Grupos de cuatro',
                'Desde el c. 3 la derecha toca grupos de cuatro semicorcheas, casi siempre con '
                'el mismo dibujo.'),
               ('IZQUIERDA', 'Bajos largos',
                'Casi siempre es un bajo largo o un acorde ligado. Es la base sobre la que se '
                'mueve la derecha.'),
               ('LOS MATICES', 'mp · pp · mf · f · ff',
                'Empieza en mp, baja a pp en el c. 3, crece hasta ff en el c. 15 y vuelve a mp.')],
        especial=[
            'Pone "Con rubato": el tempo es libre, sin metrónomo.',
            'Hay cuatro bemoles en la armadura: si♭, mi♭, la♭ y re♭.',
            'Los compases impresos cambian: 11/4 y 10/4 al principio, y 13/4 en el último.',
            'En el c. 12 la mano derecha baja en grupos de cuatro semicorcheas con matiz mf.',
            'El c. 15 termina con ff en una nota larga: el punto más fuerte.',
            'Los cc. 25-26 recuerdan la entrada: la melodía en corcheas vuelve en mp.'],
        reto='Mantener las semicorcheas iguales y suaves mientras cambia el número de tiempos '
             'por compás. Cuenta siempre en negras.',
        truco='Antes de tocar, repasa solo los compases con compás distinto del 4/4 (cc. 1-3, 7, '
              '9 y 25-26) y cuenta sus negras en voz alta.',
        sabias='Ludovico Einaudi es un compositor y pianista italiano. Esta pieza es de 2016 y '
               'está dedicada al Ártico. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchala con la partitura delante: fíjate en cuándo cambia el compás.',
        ts=(4, 4), cuenta_titulo='Cómo se cuenta el 4/4 (el compás más habitual)'),
    manos=dict(
        izq=[('Notas largas', 'Casi todo son notas largas y acordes ligados. Cuenta sus negras '
                              'y mantenlas todo su valor.'),
             ('Cambios de nota', 'En los cc. 7-11 el bajo se mueve en blancas y negras. Mira qué '
                                 'nota viene antes de tocar.'),
             ('La bajada', 'En los cc. 14-15 la izquierda toca semicorcheas que bajan, como la '
                           'derecha. Tócalas despacio.'),
             ('Acordes en 17-24', 'Del c. 17 al c. 24 la izquierda toca una nota por negra: '
                                  'parejas y suaves.')],
        der=[('Un grupo, cuatro notas', 'Aprende un solo grupo de cuatro semicorcheas, despacio, '
                                        'diez veces seguidas sin fallar.'),
             ('Igual y suave', 'Metrónomo muy lento, las cuatro notas iguales. Ninguna debe '
                               'sobresalir.'),
             ('Cuando cambia', 'Mira cuándo cambia el dibujo: cc. 9, 12, 16 y 25. Allí cambia '
                               'algo en la mano.'),
             ('Con la izquierda', 'Une un sistema con la izquierda ya segura. Si se rompe, '
                                  'vuelve a una mano.')],
        tecnica=['Muñeca suelta: las semicorcheas salen solas si no aprietas.',
                 'Cuenta siempre en negras, aunque cambie el número de tiempos del compás.',
                 'El sonido va de mp a ff: guarda la fuerza para el c. 15.']),
    bloques=[
        B(1, 'cc. 1-2', 'La entrada', (0, 0),
          D('cuenta', 'Dos compases largos: 11/4 y 10/4', [('11 negras', 11, 1), ('10 negras', 10, 1)]),
          [('IZQUIERDA', 'Una nota larguísima en cada compás. Cuéntala entera.'),
           ('DERECHA', 'Cinco notas ligadas que suben y bajan. Cántalas.'),
           ('JUNTAS', 'La izquierda suena mientras la derecha dice su frase.'),
           ('A TEMPO', 'Con rubato: libre. Empieza muy despacio, en mp.')]),
        B(2, 'cc. 3-8', 'Semicorcheas y acordes', (1, 3),
          D('cuenta', 'Un compás de 4/4 en semicorcheas', [('un compás', 4, 4)]),
          [('IZQUIERDA', 'Acordes largos ligados: uno por compás o uno por negra.'),
           ('DERECHA', 'Grupos de cuatro semicorcheas. En el c. 3 pone pp.'),
           ('JUNTAS', 'Un sistema cada día: cc. 3-4, 5-6 y 7-8.'),
           ('OJO', 'Cambios de compás: 7/4, 4/4, 6/4 y otra vez 4/4. Cuenta negras.')]),
        B(3, 'cc. 9-11', 'Cambia el dibujo', (4, 4),
          D('cadena', 'Mano derecha: cuatro notas, siempre iguales',
            [('1 grupo', False), ('se repite', False), ('c. 11: acaba larga', True)]),
          [('IZQUIERDA', 'Notas largas ligadas con una ligadura grande.'),
           ('DERECHA', 'Otro dibujo de cuatro semicorcheas, repetido. Compás 5/4 en el c. 9.'),
           ('JUNTAS', 'Los tres compases en bucle.'),
           ('OJO', 'Doble barra al final del c. 11: aquí termina la primera parte.')]),
        B(4, 'cc. 12-15', 'La bajada: mf, f, ff', (5, 6),
          D('cadena', 'El sonido sube',
            [('mf (c. 12)', False), ('f (c. 14)', False), ('ff (c. 15)', True)]),
          [('IZQUIERDA', 'Acordes largos en el c. 12 y semicorcheas en los cc. 14-15.'),
           ('DERECHA', 'Cuatro semicorcheas que bajan, en grupos. En el c. 15 acaba en nota larga.'),
           ('JUNTAS', 'Sin correr: cc. 12-13 y luego cc. 14-15.'),
           ('OJO', 'El ff del c. 15 es el momento más fuerte de la pieza.')]),
        B(5, 'cc. 16-24', 'Vuelve el vaivén', (7, 10),
          D('capas', 'Dos capas a la vez',
            [('Derecha: semis', 'puntos', AZUL), ('Izquierda: negras', 'barras',
                                                           OCRE)]),
          [('IZQUIERDA', 'Una nota por negra (cc. 17-24): parejas y suaves.'),
           ('DERECHA', 'El mismo dibujo en grupos de cuatro, con ligaduras de dos compases.'),
           ('JUNTAS', 'Un sistema cada día: cc. 16-18, 19-20, 21-22 y 23-24.'),
           ('A TEMPO', 'Vuelve a mp en el c. 17. Tranquila.')]),
        B(6, 'cc. 25-26', 'El final', (11, 11),
          D('cuenta', 'Dos compases: 6/4 y 13/4', [('6/4', 6, 1), ('13/4', 13, 1)]),
          [('IZQUIERDA', 'Notas largas: cuéntalas enteras.'),
           ('DERECHA', 'En el c. 26 vuelve la melodía de corcheas de la entrada, en mp.'),
           ('JUNTAS', 'Los dos compases, despacio, hasta la doble barra.'),
           ('OJO', 'Compás de 13/4: cuenta trece negras sin prisa.')]),
    ],
    cortes={1: [238.8, 332.8, 428.8, 545.0, 654.5], 2: [196.0, 309.8, 420.0, 531.0, 632.5]},
    corte_titulo=131.8,
    burb={
        0: [('abajo', 300, 'AMB', 'Con rubato: libre, sin metrónomo. La izquierda tiene una '
                                   'nota larga por compás (11/4 y 10/4).', 0.25)],
        1: [('arriba', 300, 'DER', 'Aquí empiezan los grupos de cuatro semicorcheas. pp: muy '
                                   'suave y parejo.', 0.3)],
        4: [('arriba', 330, 'OJO', 'c. 9: 5/4, luego 4/4. El dibujo de la derecha es otro.', 0.1)],
        5: [('arriba', 300, 'AMB', 'mf: sube el sonido. La derecha baja en grupos de cuatro.', 0.15)],
        6: [('arriba', 330, 'OJO', 'f en el c. 14 y ff en el c. 15: el momento más fuerte.', 0.55)],
        11: [('arriba', 300, 'OJO', 'c. 26: 13/4. Vuelve la melodía de la entrada, en mp.', 0.65)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe una escala con 4 bemoles')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_elegy.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
