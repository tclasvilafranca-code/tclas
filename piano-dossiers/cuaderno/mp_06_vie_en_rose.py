# -*- coding: utf-8 -*-
"""Pieza 6 · La vie en rose (Louiguy / Edith Piaf), arreglo de nephele.kulichki.com. MEDIDO a zoom
   (170-250 dpi) sobre el PDF (2 paginas A4, 8 sistemas): compas C (4/4), sin armadura, "Slowly".
   Empieza con un compas incompleto de un tiempo (anacrusa, no numerado: el sistema 2 empieza en el
   "4" tras anacrusa + cc. 1-3); numeros impresos 4,7,11,15,19,23,26 -> 27 compases numerados.
   Doble barra al final del c. 6; fermatas en los cc. 2, 22 y 27; "rit." c. 6; barra de repeticion
   |: al empezar el c. 7 ("a tempo", mp - mf) y :| al final del c. 26; casilla "1." (c. 26) y "2."
   (c. 27: "rall.", p, acordes arpegiados, sextillo de semicorcheas en la izquierda, barra final).
   Tonalidad: armadura vacia; bajo y acorde de Do en los cc. 7-8 y 26-27 (Do mayor, deducida por los
   acordes). Figura mas corta: semicorchea (sextillo del c. 27); en el resto, corchea."""
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
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Tempo', 'Slowly (lento)'),
               ('Figura corta', 'Semicorchea'), ('Compases', '27 + anacrusa')],
        total=27,
        secciones=[('A', 1, 6, 'Introducción', AZUL), ('B', 7, 18, 'El tema · se repite', OCRE),
                   ('C', 19, 27, 'Cambio, casillas y final', AZUL)],
        ideas=[('IZQUIERDA', 'Notas largas y acordes',
                'En el tema, casi siempre dos notas largas por compás: bajo grave y acorde.'),
               ('DERECHA', 'Corcheas y acordes',
                'La melodía va en corcheas ligadas, con acordes de dos y tres notas debajo.'),
               ('LA REPETICIÓN', 'Dos finales',
                'Del c. 7 al c. 26 se repite: casilla 1 (c. 26) la 1.ª vez; casilla 2 (c. 27) la 2.ª.'),
               ('LAS PAUSAS', 'Fermatas, rit. y rall.',
                'Fermatas en los cc. 2, 22 y 27. "rit." en el c. 6 y "rall." en el c. 27.')],
        especial=[
            'Pone "Slowly" (lento). El compás es C, es decir, 4/4.',
            'No hay armadura: ni sostenidos ni bemoles fijos. Es Do mayor: los bajos de los cc. '
            '7-8 y 26-27 son de Do.',
            'Empieza con un compás incompleto de un tiempo (anacrusa), que no se numera.',
            'Las dos rayitas // de los cc. 2-5 marcan una pausa breve.',
            'En el c. 7 hay barra de repetición, "a tempo" y mp - mf. Termina en el c. 26.',
            'El c. 27 lleva acordes arpegiados (línea ondulada), "rall.", p y seis notas rápidas '
            '(sextillo) en la izquierda.'],
        reto='Contar bien las pausas y las fermatas, y recordar por dónde se vuelve en la '
             'repetición y qué casilla toca cada vez.',
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
             ('Cuando cambia el dibujo', 'En los cc. 19-22 la izquierda va en negras con notas '
                                         'largas debajo, y en el c. 27 hay seis notas rápidas.'),
             ('Con fermata', 'En los cc. 2 y 22 hay fermata: aguanta la nota y cuenta.')],
        der=[('Cantar la melodía', 'Las corcheas van ligadas en frases cortas. Cántalas por '
                                   'dentro y respira al acabar cada ligadura.'),
             ('Los acordes', 'Debajo de la melodía hay notas de dos y tres sonidos. Tócalos '
                             'juntos, sin que sobresalga ninguno.'),
             ('Alteraciones', 'En los cc. 19-22 cada compás empieza con una alteración: ♭, ♮, ♯ '
                              'y ♮. Di cada nota despacio.'),
             ('Con la izquierda', 'Une despacio cuatro compases con la izquierda ya segura.')],
        tecnica=['Muñeca suelta: las corcheas ligadas salen cantadas.',
                 'Cuenta 1-2-3-4 despacio, también en las pausas.',
                 'Mira dónde empieza y acaba la repetición antes de tocar.']),
    bloques=[
        B(1, 'cc. 0-3', 'La anacrusa', (0, 0),
          D('cuenta', 'Una anacrusa de 1 tiempo y un compás de 4',
            [('anac.', 1, 2), ('c. 1', 4, 2)]),
          [('IZQUIERDA', 'Un solo acorde en la anacrusa y cuatro acordes de negra en el c. 1.'),
           ('DERECHA', 'Dos corcheas ligadas en la anacrusa. En el c. 2, nota con fermata.'),
           ('JUNTAS', 'Cuenta 1-2-3 en silencio y entra en el 4. Aguanta la fermata del c. 2.'),
           ('A TEMPO', 'Slowly: lento. Las rayitas // piden una pausa breve.')]),
        B(2, 'cc. 4-6', 'Se frena', (1, 1),
          D('cadena', 'Hacia la doble barra',
            [('cc. 4-5: frases con //', False), ('c. 6: rit.', False), ('doble barra', True)]),
          [('IZQUIERDA', 'Blancas ligadas, silencio de corchea y acordes: mira dónde cae cada '
                         'uno.'),
           ('DERECHA', 'Frases cortas de corcheas ligadas. Respira en las rayitas //.'),
           ('JUNTAS', 'Primero la derecha cantando; luego añade la izquierda.'),
           ('OJO', 'rit. en el c. 6: frena poco a poco hasta la doble barra.')]),
        B(3, 'cc. 7-10', 'Empieza el tema', (2, 2),
          D('cadena', 'Desde aquí se repite',
            [('barra |: en el c. 7', False), ('a tempo · mp - mf', True)]),
          [('IZQUIERDA', 'Dos blancas por compás en los cc. 7-8 (bajo y acorde). En el c. 9, '
                         'blanca y dos negras.'),
           ('DERECHA', 'Corcheas ligadas con acordes. En el c. 9 hay un regulador <, en el c. 10 '
                       'un >.'),
           ('JUNTAS', 'Un compás cada vez (7, 8, 9, 10) y luego los cuatro en bucle.'),
           ('A TEMPO', 'a tempo y mp - mf: sonido medio, sin correr.')]),
        B(4, 'cc. 11-18', 'El tema sigue', (3, 4),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: notas largas', 'puntos', OCRE)]),
          [('IZQUIERDA', 'En el c. 14 hay cuatro negras con un sostenido y un becuadro: míralas '
                         'antes.'),
           ('DERECHA', 'Cc. 15-16 muy parecidos a 7-8. En el c. 17 hay un bemol y el c. 18 acaba '
                       'en un acorde largo.'),
           ('JUNTAS', 'Un sistema cada día: cc. 11-14 y cc. 15-18.'),
           ('OJO', 'Reguladores en los cc. 13-14 y 17-18: sube y baja el sonido sin acentuar.')]),
        B(5, 'cc. 19-22', 'Cambia el dibujo', (5, 5),
          D('cadena', 'Lo que cambia',
            [('derecha: corcheas repetidas', False), ('izquierda en negras', False),
             ('fermata c. 22', True)]),
          [('IZQUIERDA', 'Cuatro negras arriba y notas largas graves debajo. Alteraciones: ♭ en '
                         'el 19, ♯ en el 21.'),
           ('DERECHA', 'Notas repetidas, corcheas y negras, parejas y suaves. Un regulador en '
                       'cada compás.'),
           ('JUNTAS', 'Compás a compás, despacio, hasta unirlos sin parar.'),
           ('OJO', 'Fermata en el c. 22 (en las dos manos): aguanta y cuenta antes de seguir.')]),
        B(6, 'cc. 23-25', 'Vuelve el tema', (6, 6),
          D('cadena', 'Hacia las casillas',
            [('c. 23: tema', False), ('c. 25: ligadura', False), ('casilla 1 o 2', True)]),
          [('IZQUIERDA', 'Dos blancas por compás en los cc. 23-24. En el c. 25: blanca, dos '
                         'corcheas y negra.'),
           ('DERECHA', 'Frase parecida a la de los cc. 7-9. El c. 25 acaba con una ligadura hacia '
                       'el siguiente compás.'),
           ('JUNTAS', 'Los tres compases en bucle.'),
           ('OJO', 'La nota ligada del c. 25 sigue en la casilla 1 y en la casilla 2: no la '
                   'pulses otra vez.')]),
        B(7, 'cc. 26-27', 'Casillas y final', (7, 7),
          D('cadena', 'Las dos vueltas',
            [('1.ª vez: casilla 1', False), ('↩ al c. 7', False), ('2.ª vez: casilla 2', True)]),
          [('IZQUIERDA', 'Casilla 1: negras y acordes. Casilla 2: seis notas rápidas que suben '
                         '(sextillo).'),
           ('DERECHA', 'Casilla 1: corcheas con ♭ y ♮. Casilla 2: acordes arpegiados y fermata.'),
           ('JUNTAS', 'Recorre con el dedo: 7→26, vuelta al 7, hasta el 25 y salto al 27.'),
           ('A TEMPO', 'rall.: frena poco a poco y acaba en p. Aguanta la fermata.')]),
    ],
    cortes={1: [273.2, 420.2, 588.8], 2: [223.2, 396.8, 547.5]},
    corte_titulo=125.5, inicio={2: 56.0},
    burb={
        0: [('arriba', 250, 'OJO', 'Slowly: lento. Compás C (4/4), sin sostenidos ni bemoles '
                                   'fijos.', 130),
            ('arriba', 250, 'AMB', 'Fermata del c. 2: aguanta la nota. Las rayitas // son una '
                                   'pausa breve.', 330),
            ('abajo', 330, 'IZQ', 'Anacrusa: el compás empieza incompleto, con un solo acorde de '
                                  'un tiempo. No se numera.', 135)],
        1: [('arriba', 480, 'OJO', 'rit. en el c. 6: frena poco a poco hasta la doble barra.',
             481)],
        2: [('arriba', 300, 'AMB', 'Barra |: del c. 7, "a tempo" y mp - mf. Desde aquí se '
                                   'repite.', 88)],
        3: [('arriba', 500, 'OJO', 'c. 14: sostenido y becuadro en las cuatro negras, en las dos '
                                   'manos.', 500)],
        5: [('arriba', 540, 'OJO', 'Fermata del c. 22, en las dos manos: aguanta y cuenta.', 546),
            ('abajo', 330, 'AMB', 'Cada compás empieza con una alteración: ♭ (c. 19), ♮ (c. 20), '
                                  '♯ (c. 21) y ♮ (c. 22).', 300)],
        6: [('arriba', 520, 'AMB', 'c. 25: la ligadura del final une con la primera nota de la '
                                   'casilla. No la pulses otra vez.', 530)],
        7: [('arriba', 250, 'OJO', 'Casilla 1 (c. 26): la primera vez. Acaba en :| y vuelves al '
                                   'c. 7.', 110),
            ('arriba', 250, 'AMB', 'Casilla 2 (c. 27): la segunda vez. "rall." y p, con acordes '
                                   'arpegiados.', 350),
            ('abajo', 400, 'IZQ', 'Seis notas rápidas que suben (sextillo): estúdialas aparte, '
                                  'despacio.', 470)],
    },
    marcas=[(1, 323.5, 151, 21, 16, 1, 1, 'caja'), (1, 483, 357, 26, 16, 2, 1, 'caja'),
            (1, 113, 506, 74, 34, 3, 1, 'caja'), (2, 547, 244, 26, 16, 5, 1, 'caja'),
            (2, 179, 561, 210, 16, 7, 1, 'caja'), (2, 417, 561, 258, 16, 7, 2, 'caja')],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_vie_en_rose.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
