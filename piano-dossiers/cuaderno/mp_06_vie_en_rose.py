# -*- coding: utf-8 -*-
"""Pieza 6 · La vie en rose (Louiguy / Edith Piaf), arreglo de nephele.kulichki.com. MEDIDO sobre el
   PDF (2 paginas A4, 8 sistemas): compas C (4/4), sin armadura, "Slowly"; empieza con un compas
   incompleto (anacrusa, no numerado); numeros impresos 4,7,11,15,19,23,26 -> 27 compases numerados;
   fermatas en los cc. 2, 22 y 27; "rit." c. 6; barra de repeticion |: al empezar el c. 7 ("a
   tempo", mp - mf) y :| al final del c. 26; casilla "1." (c. 26) y "2." (c. 27, con "rall.", p,
   sextillo de semicorcheas en la izquierda y barra final). Figura mas corta: semicorchea
   (sextillo del c. 27); en el resto, corchea. NO verificado: tonica (la armadura esta vacia)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=6, slug='vie_en_rose', pdf='edith_piaf_la_vie_en_rose_pdf.pdf', time_sig=(4, 4),
    titulo='La vie en rose', autor='Louiguy · letra original de Édith Piaf',
    kicker='Eva · pieza 6 · La vie en rose', mes='Enero · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=la+vie+en+rose+piano+tutorial',
    credito='Partitura: Louiguy, La vie en rose (nephele.kulichki.com). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Armadura', 'Sin alteraciones'), ('Compás', '4/4'), ('Tempo', 'Slowly (lento)'),
               ('Figura corta', 'Semicorchea'), ('Compases', '27')],
        total=27,
        secciones=[('A', 1, 6, 'Introducción lenta', AZUL), ('B', 7, 25, 'El tema · se repite', OCRE),
                   ('C', 26, 27, 'Casillas y final', AZUL)],
        ideas=[('IZQUIERDA', 'Notas largas y acordes',
                'En el tema, casi siempre dos notas largas por compás: un bajo grave y un acorde '
                'encima.'),
               ('DERECHA', 'Corcheas y acordes',
                'La melodía va en corcheas ligadas, con acordes de dos y tres notas debajo.'),
               ('LA REPETICIÓN', 'Dos finales',
                'Del c. 7 al c. 26 se repite. La primera vez, casilla 1 (c. 26); la segunda, '
                'casilla 2 (c. 27).'),
               ('LAS PAUSAS', 'Fermatas y rit.',
                'Hay fermatas en los cc. 2, 22 y 27, un "rit." en el c. 6 y un "rall." al final.')],
        especial=[
            'Pone "Slowly" (lento). El compás es C, es decir, 4/4. No hay armadura.',
            'Empieza con un compás incompleto (anacrusa) que no cuenta en la numeración.',
            'Las dos rayitas // de los primeros compases marcan una pausa breve.',
            'En el c. 7 hay barra de repetición, "a tempo" y mp - mf.',
            'Hay bemoles, sostenidos y becuadros sueltos, sobre todo en los cc. 1-6 y 19-22.',
            'El final lleva "rall.", p y seis notas rápidas (sextillo) en la izquierda.'],
        reto='Contar las pausas y las fermatas sin perderte, y recordar por dónde se vuelve en la '
             'repetición.',
        truco='Antes de tocar, recorre la partitura con el dedo: 1-6, luego 7-26, vuelta al 7, '
              'hasta el 25 y salto a la casilla 2 (c. 27).',
        sabias='La partitura dice: música de Louiguy, letra en inglés de Mack David y letra '
               'original en francés de Édith Piaf. Piaf la hizo famosa hacia 1946-47. (Fecha de '
               'memoria, sin verificar.)',
        qr_texto='Escúchala con la partitura delante: marca las fermatas y el rit.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Notas largas', 'En el tema la izquierda toca dos notas largas por compás. Toca '
                              'solo los cc. 7-10, despacio, hasta que salgan sin mirar.'),
             ('Cambio de acorde', 'Antes de cada compás mira qué acorde viene y coloca la mano '
                                  'antes de tocar.'),
             ('Cuando cambia el dibujo', 'En los cc. 19-22 la izquierda va en negras y en el c. '
                                         '27 hay seis notas rápidas. Míralos aparte.'),
             ('Con fermata', 'En los cc. 2 y 22 hay fermata: aguanta la nota y cuenta.')],
        der=[('Cantar la melodía', 'Las corcheas van ligadas en frases cortas. Cántalas por '
                                   'dentro y respira al acabar cada ligadura.'),
             ('Los acordes', 'Los acordes de dos y tres notas se tocan juntos, sin arpegiar.'),
             ('Alteraciones', 'En los cc. 1-6 y 19-22 hay bemoles, sostenidos y becuadros. Di '
                              'cada nota despacio.'),
             ('Con la izquierda', 'Une despacio cuatro compases con la izquierda ya segura.')],
        tecnica=['Muñeca suelta: las corcheas ligadas salen cantadas.',
                 'Cuenta 1-2-3-4 despacio, también en las pausas.',
                 'Mira dónde empieza y acaba la repetición antes de tocar.']),
    bloques=[
        B(1, 'cc. 0-6', 'La introducción', (0, 1),
          D('cadena', 'Las indicaciones', [('Slowly', False), ('fermata c. 2', False),
                                           ('rit. c. 6', True)]),
          [('IZQUIERDA', 'Acordes y notas largas, despacio. Aguanta la fermata del c. 2.'),
           ('DERECHA', 'Empieza con un compás incompleto y sigue en frases cortas con //.'),
           ('JUNTAS', 'Un sistema cada día: cc. 0-3 y cc. 4-6.'),
           ('OJO', 'Muchas alteraciones: lee nota a nota. En el c. 6 hay rit.')]),
        B(2, 'cc. 7-10', 'Empieza el tema', (2, 2),
          D('cadena', 'Desde aquí se repite', [('barra |: en el c. 7', False),
                                              ('a tempo · mp - mf', True)]),
          [('IZQUIERDA', 'Dos notas largas por compás: bajo grave y acorde.'),
           ('DERECHA', 'Corcheas ligadas con acordes. Cantan, no se golpean.'),
           ('JUNTAS', 'Los cuatro compases en bucle.'),
           ('A TEMPO', 'mp - mf: sonido medio, sin correr.')]),
        B(3, 'cc. 11-18', 'El tema sigue', (3, 4),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: notas largas', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Sigue con notas largas; en el c. 14 hay sostenidos y becuadros.'),
           ('DERECHA', 'Frases parecidas a las del c. 7: reconoce las que ya sabes.'),
           ('JUNTAS', 'Un sistema cada día: cc. 11-14 y cc. 15-18.'),
           ('OJO', 'Los reguladores < > piden subir y bajar el sonido poco a poco.')]),
        B(4, 'cc. 19-22', 'Cambia el dibujo', (5, 5),
          D('cadena', 'Lo que cambia', [('izquierda en negras', False), ('alteraciones', False),
                                        ('fermata c. 22', True)]),
          [('IZQUIERDA', 'Ahora va en negras y blancas, con bemoles y sostenidos.'),
           ('DERECHA', 'Notas repetidas en corcheas: tócalas parejas y suaves.'),
           ('JUNTAS', 'Compás a compás, despacio.'),
           ('OJO', 'Fermata en el c. 22: aguanta y cuenta antes de seguir.')]),
        B(5, 'cc. 23-25', 'Vuelve el tema', (6, 6),
          D('cadena', 'Hacia las casillas', [('c. 23: tema', False), ('c. 25', False),
                                             ('c. 26: casilla 1', True)]),
          [('IZQUIERDA', 'Dos notas largas por compás, como en el c. 7.'),
           ('DERECHA', 'Una frase parecida a la del c. 7: reconócela.'),
           ('JUNTAS', 'Los tres compases en bucle.'),
           ('OJO', 'Al acabar el c. 25 mira qué casilla te toca.')]),
        B(6, 'cc. 26-27', 'Casillas y final', (7, 7),
          D('cadena', 'Las dos vueltas', [('1.ª vez: casilla 1', False), ('↩ al c. 7', False),
                                          ('2.ª vez: casilla 2', True)]),
          [('IZQUIERDA', 'En el c. 27 hay seis notas rápidas que suben: tócalas aparte.'),
           ('DERECHA', 'Casilla 2: acordes largos y fermata en la última nota.'),
           ('JUNTAS', 'Recorre el camino con el dedo antes de tocar.'),
           ('A TEMPO', 'rall.: frena poco a poco y acaba en p.')]),
    ],
    cortes={1: [273.2, 420.2, 588.8], 2: [223.2, 396.8, 547.5]},
    corte_titulo=125.5, inicio={2: 56.0},
    burb={
        0: [('arriba', 250, 'OJO', 'Slowly: lento. Compás de 4/4 (C) y sin armadura.', 0.08),
            ('arriba', 250, 'AMB', 'Fermata en el c. 2: aguanta la nota y cuenta antes de seguir.',
             0.6)],
        1: [('arriba', 300, 'OJO', 'rit. en el c. 6: frena poco a poco.', 0.85)],
        2: [('arriba', 300, 'AMB', 'Barra |: del c. 7, "a tempo" y mp - mf. Desde aquí se repite.',
             0.06)],
        5: [('arriba', 300, 'OJO', 'Fermata en el c. 22: aguanta la nota y cuenta.', 0.95)],
        7: [('arriba', 250, 'OJO', 'Casilla 1 (c. 26) la 1.ª vez; casilla 2 (c. 27) la 2.ª.', 0.1),
            ('arriba', 250, 'IZQ', 'Seis notas rápidas que suben, con rall. y p.', 0.85)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_vie_en_rose.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
