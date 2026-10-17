# -*- coding: utf-8 -*-
"""Pieza 1 · El cisne (Saint-Saens), edicion "Piano Collection for Beginners - Grade 3".
   MEDIDO sobre el PDF (5 paginas, tamano carta): una armadura de un sostenido (Sol mayor), 3/4,
   Andante negra = 96, termina en el c. 54 (numeracion impresa, que cuenta el primer compas vacio
   como 0); todo en corcheas (una barra), izquierda en seis corcheas por compas; matices pp, p,
   poco cresc., dim. e poco rit., a tempo, mf, dim., rit., lento, pp, rit.; sostenidos y becuadros
   en los cc. 14-15 y 32-33."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403



SPEC = dict(
    num=1, slug='cisne', pdf='the_swan.pdf', time_sig=(3, 4),
    titulo='El cisne', autor='Camille Saint-Saëns · edición para principiantes de Ricardo Boppré',
    kicker='Eva · pieza 1 · El cisne', mes='Noviembre · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=saint-saens+the+swan+le+cygne+piano',
    credito='Partitura: C. Saint-Saëns, revisión de Ricardo Boppré (theperfectscores.com). '
            'Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '3/4'), ('Tempo', 'Andante ♩=96'),
               ('Figura corta', 'Corchea'), ('Compases', '54')],
        total=54,
        secciones=[('A', 1, 9, 'Entrada y primera frase', AZUL),
                   ('B', 10, 20, 'La melodía crece', OCRE),
                   ('C', 21, 31, 'Poco cresc.', AZUL),
                   ('D', 32, 43, 'Vuelve · clímax en mf', OCRE),
                   ('E', 44, 54, 'Final: dim., lento, rit.', AZUL)],
        ideas=[('IZQUIERDA', 'Seis corcheas por compás',
                'Un arpegio que sube y baja, compás tras compás, bajo una ligadura larga. Es el '
                'mar sobre el que nada el cisne.'),
               ('DERECHA', 'Notas largas que cantan',
                'La melodía va en negras y blancas, en frases ligadas de tres o cuatro compases. '
                'Se estudia cantando.'),
               ('LOS CAMBIOS', 'Sostenidos y becuadros',
                'Casi toda la pieza usa las notas de Sol mayor. Las alteraciones llegan en los '
                'cc. 14-15 y 32-33.'),
               ('LOS MATICES', 'pp → p → mf → pp',
                'Empieza muy suave, crece hasta el mf del c. 42 y se apaga con rit. al final.')],
        especial=[
            'Pone "Andante" y negra = 96.',
            'Los dos primeros compases son de silencio en la derecha: empieza la izquierda sola.',
            'La izquierda hace casi siempre lo mismo: seis corcheas por compás.',
            'Las frases de la derecha van ligadas: cada ligadura es una respiración.',
            'Hay "poco cresc." (cc. 28-31), "dim. e poco rit." (c. 32-33) y "lento" (c. 49).',
            'El final lleva "pp" y "rit.": termina casi sin sonido.'],
        reto='Que la izquierda suene siempre igual y muy suave mientras la derecha canta. Si un '
             'compás se te escapa, lo normal es que la izquierda no esté de memoria.',
        truco='Estudia la izquierda sola hasta tocarla mirando la derecha de la partitura. Luego '
              'añade solo la primera nota larga de cada frase, y no la segunda hasta que salga.',
        sabias='El cisne es una pieza de "El carnaval de los animales" (1886), escrita para '
               'violonchelo y piano. Saint-Saëns no quiso publicar casi nada de esa obra en vida, '
               'pero sí esta pieza.',
        qr_texto='Escúchala con la partitura delante: sigue las ligaduras con el dedo.',
        ts=(3, 4)),
    manos=dict(
        izq=[('Un compás, un arco', 'En cada compás la izquierda sube y baja por seis corcheas. '
                                    'Toca solo el primer compás, despacio, diez veces seguidas '
                                    'sin fallar.'),
             ('Parejo y suave', 'Metrónomo lento, seis corcheas iguales y muy suaves (pp). Si una '
                                'nota sobresale, repite.'),
             ('Cuando el dibujo cambia', 'En los cc. 13-15 el dibujo se aplana y cambian algunas '
                                         'notas (con sostenidos). En el c. 16 vuelve el de '
                                         'siempre.'),
             ('De memoria', 'Aprende la izquierda de memoria: la derecha necesita que ella ande '
                            'sola.')],
        der=[('Cantar antes de tocar', 'La derecha casi siempre toca notas largas en una frase '
                                       'ligada. Cántala por dentro y respira donde acaba la '
                                       'ligadura.'),
             ('Una frase, un gesto', 'Toca cada frase ligada como un solo movimiento del brazo: '
                                     'baja el brazo en la primera nota y deja subir la muñeca al '
                                     'final.'),
             ('Las alteraciones', 'En los cc. 14-15 la derecha sube por semitonos, con sostenidos '
                                  'y becuadros. Tócala despacio y di el nombre de cada nota.'),
             ('Con la izquierda', 'Une despacio una frase con la izquierda ya segura. Si se '
                                  'rompe, vuelve a una sola mano.')],
        tecnica=['Brazo y muñeca sueltos: la melodía se canta, no se golpea.',
                 'Sonido pequeño y parejo en la izquierda: la melodía manda.',
                 'Cuenta 1-2-3 en cada compás, sin prisa (Andante).']),
    bloques=[
        B(1, 'cc. 1-5', 'La entrada', (0, 1), D('cuenta', 'La izquierda: seis corcheas por compás',
                                                [('un compás', 1, 6)]),
          [('IZQUIERDA', 'Empieza sola: seis corcheas por compás, sube y baja. Despacio y '
                         'parejo.'),
           ('DERECHA', 'Entra en el c. 2 con tres notas largas ligadas. Cántalas antes de '
                       'tocarlas.'),
           ('JUNTAS', 'Dos compases de izquierda y, en el tercero, entra la derecha.'),
           ('A TEMPO', 'Andante, negra = 96. Empieza más despacio.')]),
        B(2, 'cc. 6-12', 'La melodía crece', (2, 3),
          D('capas', 'Dos capas que suenan a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: corcheas', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Mismo arco de seis corcheas; en el c. 12 la forma cambia: míralo antes '
                         'de tocar.'),
           ('DERECHA', 'La frase sube hasta la nota más alta de la página: pasa de una nota larga '
                       'a otra sin cortar.'),
           ('JUNTAS', 'Una frase de la derecha con su izquierda, y respiras.'),
           ('OJO', 'En el c. 12 acaba la ligadura larga: ahí se respira.')]),
        B(3, 'cc. 13-20', 'Sostenidos y becuadros', (4, 5),
          D('cadena', 'La subida de los cc. 14-15',
            [('lee nota a nota', False), ('sube por semitonos', False), ('termina en nota larga',
                                                                         True)]),
          [('IZQUIERDA', 'En los cc. 13-15 el dibujo se aplana y lleva sostenidos. En el c. 16 '
                         'vuelve el de siempre.'),
           ('DERECHA', 'La subida de los cc. 14-15 va por semitonos. Di cada nota en voz alta y '
                       'toca despacio.'),
           ('JUNTAS', 'Primero solo los cc. 13-16, en bucle.'),
           ('OJO', 'Los sostenidos y becuadros valen solo hasta el final de su compás.')]),
        B(4, 'cc. 21-31', 'Poco a poco, más sonido', (6, 8),
          D('cadena', 'El arco de matices',
            [('p', False), ('poco cresc.', False), ('más sonido', True)]),
          [('IZQUIERDA', 'Sigue con seis corcheas por compás. Más sonido, pero sin correr.'),
           ('DERECHA', 'Las frases son parecidas a las de antes: reconoce las que ya sabes.'),
           ('JUNTAS', 'Un sistema cada día: cc. 21-23, 24-27, 28-31.'),
           ('OJO', 'Poco cresc.: sube el sonido despacio, no de golpe.')]),
        B(5, 'cc. 32-39', 'Vuelve el tema', (9, 10),
          D('cadena', 'Las indicaciones de este bloque',
            [('dim. e poco rit.', False), ('a tempo', False), ('pp', True)]),
          [('IZQUIERDA', 'En los cc. 32-33 el dibujo lleva alteraciones; después vuelven los '
                         'arcos de siempre.'),
           ('DERECHA', 'En el c. 34 vuelve la melodía del principio, otra vez en pp.'),
           ('JUNTAS', 'Cuida el cambio: dim. e poco rit., y a tempo en el c. 34.'),
           ('OJO', 'En el c. 34 vuelve el tempo: no te quedes lenta.')]),
        B(6, 'cc. 40-43', 'El punto más fuerte', (11, 11),
          D('cadena', 'El clímax', [('p', False), ('mf', True), ('baja otra vez', False)]),
          [('IZQUIERDA', 'Más sonido, pero siempre pareja: no aceleres con la fuerza.'),
           ('DERECHA', 'Aquí está la nota más aguda de la melodía: tócala cantando.'),
           ('JUNTAS', 'Los cuatro compases en bucle, sin parar.'),
           ('A TEMPO', 'mf es el punto más fuerte de toda la pieza.')]),
        B(7, 'cc. 44-54', 'El final', (12, 14),
          D('cadena', 'Hacia el silencio',
            [('dim.', False), ('p', False), ('rit.', False), ('lento', False), ('a tempo', False),
             ('pp', False), ('rit.', True)]),
          [('IZQUIERDA', 'Del c. 51 al 54 la izquierda pasa a clave de sol: lee la clave antes de '
                         'tocar.'),
           ('DERECHA', 'Notas largas al final: cuéntalas enteras.'),
           ('JUNTAS', 'Tres sistemas: cc. 44-47, 48-50 y 51-54.'),
           ('OJO', 'Poco a poco más suave y más lento: acaba casi sin sonido.')]),
    ],
    cortes={1: [333.5, 521.2], 2: [293.8, 502.5], 3: [303.0, 507.2], 4: [305.5, 503.5],
            5: [299.8, 509.2]},
    corte_titulo=151.8, inicio={2: 80, 3: 80, 4: 80, 5: 80},
    fin={1: 712.0, 2: 711.8, 3: 717.2, 4: 710.2, 5: 712.0},
    burb={
        0: [('abajo', 300, 'IZQ', 'Empiezas tú, sola: seis corcheas por compás, sube y baja como un '
                                  'arco. Despacio y parejo.', 0.25)],
        1: [('arriba', 300, 'DER', 'Entra la melodía: tres notas largas ligadas. Cántala por dentro '
                                   'antes de tocarla.', 0.15)],
        2: [('arriba', 330, 'AMB', 'Una frase larga = un solo arco: toca las notas como una sola '
                                   'idea y respira donde acaba la ligadura.', 0.2)],
        3: [('arriba', 300, 'IZQ', 'En el c. 12 la izquierda cambia de dibujo: seis corcheas '
                                   'seguidas, sin arco.', 0.85)],
        4: [('arriba', 330, 'OJO', 'Sostenidos y becuadros: la subida de los cc. 14-15 va por '
                                   'semitonos. Léela nota a nota.', 0.55)],
        5: [('arriba', 300, 'DER', 'Más suave (p): las notas largas se oyen sobre la izquierda. '
                                   'Pesa con el brazo, no con el dedo.', 0.1)],
        8: [('arriba', 300, 'AMB', 'Poco cresc.: sube el sonido poco a poco, sin acelerar.', 0.5)],
        9: [('arriba', 330, 'OJO', 'dim. e poco rit.: baja el sonido y afloja el tempo; en el c. 34 '
                                   'vuelve "a tempo" en pp.', 0.6)],
        11: [('arriba', 300, 'AMB', 'mf: el punto más fuerte de la pieza. Que suene, pero cantando.',
              0.6)],
        12: [('arriba', 300, 'OJO', 'dim., p y rit.: el sonido se va apagando hasta el c. 47.', 0.3)],
        13: [('arriba', 330, 'OJO', 'lento en el c. 49 y "a tempo" en el c. 50.', 0.45)],
        14: [('arriba', 330, 'AMB', 'pp y rit.: acaba casi sin sonido y deja que el último compás '
                                    'se apague.', 0.6)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_cisne.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
