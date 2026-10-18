# -*- coding: utf-8 -*-
"""Pieza 5 · Counting Stars (OneRepublic), Easy Version, arr. Becky Messer. MEDIDO sobre el PDF
   de Musescore (2 paginas, 55 compases en 12 sistemas): sin armadura (La menor: la izquierda
   gira La menor - Do - Sol - Fa y el final cae en La), 4/4, sin tempo ni matices impresos;
   repeticiones en los cc. 1-4, 6-9, 10-29 (con casillas 1.a cc. 22-29 y 2.a cc. 30-33) y 43-46;
   semicorchea como figura mas corta (cc. 10, 14 y 34-39). Izquierda en dos notas largas
   (quintas vacias). La partitura trae digitacion impresa: no se menciona."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=5, slug='counting_stars', pdf='counting_stars.pdf', time_sig=(4, 4),
    titulo='Counting Stars', autor='OneRepublic · Easy Version, arreglo de Becky Messer',
    kicker='Sharifa · pieza 5 · Counting Stars', mes='Febrero · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=onerepublic+counting+stars+piano+easy',
    credito='Partitura: OneRepublic, arr. Becky Messer, Easy Version (Musescore.com). '
            'Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'La menor'), ('Compás', '4/4'), ('Tempo', 'Sin indicar'),
               ('Figura corta', 'Semicorchea'), ('Compases', '55')],
        total=55,
        secciones=[('A', 1, 9, 'La entrada', AZUL), ('B', 10, 21, 'La estrofa', OCRE),
                   ('C', 22, 33, 'Casillas 1.ª y 2.ª', AZUL), ('D', 34, 42, 'La parte nueva', OCRE),
                   ('E', 43, 55, 'Vuelve y final', AZUL)],
        ideas=[('IZQUIERDA', 'Cuatro acordes que giran',
                'Dos notas largas a la vez, una vuelta por cuatro compases: La-Mi, Do-Sol, Sol-Re, '
                'Fa-Do (quintas vacías).'),
               ('DERECHA', 'Una frase que vuelve',
                'Cuatro compases cortos (Re-Mi-Sol-Mi...) que se repiten casi iguales a lo '
                'largo de la pieza.'),
               ('EL RITMO', 'Negras, corcheas y silencios',
                'Hay silencios de corchea al empezar el compás y, pocas veces, notas muy '
                'rápidas (semicorcheas).'),
               ('EL RECORRIDO', 'Repeticiones y casillas',
                'Hay cuatro barras de repetición y una casilla 1.ª y 2.ª. Hay que saber '
                'por dónde vas.')],
        especial=[
            'No lleva armadura ni tempo: no hay sostenidos ni bemoles escritos.',
            'Compás de 4/4: cuatro negras por compás.',
            'Repeticiones: cc. 1-4, cc. 6-9, cc. 43-46 y la grande, del c. 10 al c. 29.',
            'Casillas: la 1.ª vez toca los cc. 22-29; la 2.ª vez salta a los cc. 30-33.',
            'Semicorcheas en los cc. 10, 14 y 34-39: son lo único rápido de la pieza.',
            'En los cc. 30-33 la derecha calla y toca solo la izquierda.'],
        reto='Los cuatro acordes de la izquierda siempre a tiempo, mientras la derecha cambia de '
             'ritmo y de lugar.',
        truco='Aprende la izquierda de memoria: son solo cuatro acordes y siempre el mismo '
              'orden. Así miras solo la derecha.',
        sabias='«Counting Stars» es de 2013, del álbum Native de OneRepublic. La escribió Ryan '
               'Tedder, cantante del grupo, y llegó al número 2 de la lista Billboard Hot 100 '
               'de Estados Unidos.',
        qr_texto='Escúchala y cuenta 1-2-3-4: ¿cuándo cambia el acorde?', ts=(4, 4)),
    manos=dict(
        izq=[('Los cuatro acordes', 'Un acorde por compás, dos notas a la vez: La-Mi, Do-Sol, '
                                    'Sol-Re, Fa-Do. Cuenta 1-2-3-4 en cada uno.'),
             ('La vuelta entera', 'Toca los cuatro acordes seguidos, cuatro veces, sin parar. '
                                  'Siempre el mismo orden.'),
             ('De memoria', 'Repite la vuelta mirando la partitura de la derecha. La izquierda '
                            'tiene que salir sola.'),
             ('Cuando cambia', 'Cc. 34-37: una sola nota larga, La aguda y La grave. En el c. 21 '
                               'entran dos corcheas al final.')],
        der=[('Una frase', 'Aprende los cc. 1-4: Re-Mi-Sol-Mi y corcheas que bajan. Es la frase '
                           'que más vuelve.'),
             ('Las corcheas', 'Cuenta «1-y-2-y». En el c. 3 empieza un silencio de corchea: '
                              'cuéntalo, no lo saltes.'),
             ('Lo nuevo', 'Cc. 10-13: ritmo con puntillo. Cc. 18-21: notas repetidas. Cc. 34-39: '
                          'notas rápidas.'),
             ('Con la izquierda', 'Junta cada frase con su acorde. Si te pierdes, vuelve a una '
                                  'sola mano.')],
        tecnica=['Muñeca suelta y dedos curvos: acordes sin apretar.',
                 'La izquierda suena suave y la derecha canta por encima.',
                 'Cuenta en voz alta y no pares si te equivocas: sigue.']),
    bloques=[
        B(1, 'cc. 1-5', 'El motivo', (0, 0),
          D('cadena', 'Los acordes de la izquierda',
            [('La menor', False), ('Do', False), ('Sol', False), ('Fa', True)]),
          [('IZQUIERDA', 'La-Mi, Do-Sol, Sol-Re, Fa-Do: un acorde por compás, notas largas.'),
           ('DERECHA', 'Re-Mi-Sol-Mi y luego corcheas que bajan. Es la frase más repetida.'),
           ('JUNTAS', 'Los cuatro compases juntos. Se tocan dos veces (barra del c. 4).'),
           ('OJO', 'El c. 5 es solo la nota larga que cierra: déjala sonar.')]),
        B(2, 'cc. 6-9', 'Silencio y corcheas', (1, 1),
          D('cadena', 'Un compás del c. 6',
            [('negra', False), ('silencio de corchea', False), ('corcheas', False),
             ('negra', True)]),
          [('IZQUIERDA', 'Los mismos cuatro acordes: La menor, Do, Sol, Fa.'),
           ('DERECHA', 'Mi repetido con un silencio de corchea. En los cc. 8-9: Mi-Re-Do-La.'),
           ('JUNTAS', 'Cuatro compases juntos. Se tocan dos veces (barra del c. 9).'),
           ('OJO', 'El silencio de corchea dura: cuéntalo en voz alta.')]),
        B(3, 'cc. 10-17', 'La estrofa', (2, 3),
          D('cadena', 'Un ritmo nuevo',
            [('negra', False), ('corchea con puntillo', False), ('semicorchea', True)]),
          [('IZQUIERDA', 'Los cuatro acordes de siempre, un compás cada uno.'),
           ('DERECHA', 'En el c. 10: corchea con puntillo y semicorchea. Despacio.'),
           ('JUNTAS', 'Los cc. 10-13 y los cc. 14-17 son iguales: aprendes cuatro y valen ocho.'),
           ('OJO', 'Ligadura de los cc. 12-13: la corchea se toca una vez y se alarga.')]),
        B(4, 'cc. 18-21', 'Notas repetidas', (4, 4),
          D('cadena', 'La derecha en los cc. 18-19',
            [('silencio', False), ('La-Sol', False), ('La', False), ('La-Sol', True)]),
          [('IZQUIERDA', 'Fa-Do largo en los cc. 18-20 (los dos primeros ligados). No lo repitas.'),
           ('DERECHA', 'La-Sol y La repetidos. En el c. 20 baja: La, Sol, Mi-Re, Do.'),
           ('JUNTAS', 'La izquierda aguanta y la derecha lleva el ritmo.'),
           ('OJO', 'En el c. 21 la izquierda entra con dos corcheas, La-Sol, al final.')]),
        B(5, 'cc. 22-33', 'Primera y segunda vez', (5, 6),
          D('cadena', 'El recorrido',
            [('22-29 (1.ª)', False), ('↩ al c. 10', True), ('10-21', False),
             ('30-33 (2.ª)', True)]),
          [('IZQUIERDA', 'Cc. 22-29: los cuatro acordes. Cc. 30-33: una sola nota, La grave y '
                         'La aguda.'),
           ('DERECHA', 'Cc. 22-29: la frase del principio, dos veces. Cc. 30-33: en silencio.'),
           ('JUNTAS', 'Toca los cc. 22-29 y vuelve al c. 10 (barra del c. 29).'),
           ('OJO', 'La 2.ª vez te saltas la casilla 1.ª: del c. 21 pasas al c. 30.')]),
        B(6, 'cc. 34-42', 'La parte nueva', (7, 8),
          D('capas', 'Dos capas a la vez',
            [('Derecha: corcheas', 'puntos', AZUL, 6), ('Izquierda: una nota', 'barras', OCRE)]),
          [('IZQUIERDA', 'Cc. 34-37: una nota larga por compás, La aguda y La grave. Cc. 38-39: '
                         'vuelven los acordes.'),
           ('DERECHA', 'Do-Si-La y notas rápidas. Los cc. 34-35 se repiten en 36-37 y 38-39.'),
           ('JUNTAS', 'De dos en dos compases: 34-35, 36-37, 38-39.'),
           ('OJO', 'Cc. 40-42: la bajada final y una nota larga ligada.')]),
        B(7, 'cc. 43-55', 'Vuelve el tema y el final', (9, 11),
          D('cadena', 'El recorrido',
            [('43-46 (x2)', False), ('47-50', False), ('51-54', False), ('55 FIN', True)]),
          [('IZQUIERDA', 'Otra vez La-Mi, Do-Sol, Sol-Re, Fa-Do. En el c. 55 la izquierda calla.'),
           ('DERECHA', 'Es la frase del principio. El c. 54 acaba con Mi-Re-Re-Do.'),
           ('JUNTAS', 'Los cc. 51-55 sin parar hasta la última nota.'),
           ('A TEMPO', 'La pieza entera, una vez al día, con repeticiones y casillas.')]),
    ],
    cortes={1: [184.0, 296.2, 413.0, 529.2, 648.2], 2: [145.2, 264.0, 395.5, 521.0, 646.0]},
    corte_titulo=76.0, inicio={1: 18.5, 2: 30.0}, fin={1: 762.0, 2: 762.0},
    burb={
        0: [('arriba', 250, 'DER', 'Empiezas aquí: Re-Mi-Sol-Mi. Cuenta 1-2-3-4.', 0.1),
            ('abajo', 250, 'IZQ', 'Cuatro acordes, uno por compás: La-Mi, Do-Sol, Sol-Re, Fa-Do.',
             0.2),
            ('abajo', 250, 'OJO', 'La barra de repetición del c. 4 te devuelve al c. 1.', 0.75)],
        1: [('arriba', 300, 'OJO', 'Cc. 6-9: se tocan dos veces. Cuenta el silencio de corchea '
                                   'antes de las corcheas.', 0.1)],
        2: [('arriba', 300, 'DER', 'Corchea con puntillo y semicorchea: la segunda nota es muy '
                                   'corta. Despacio.', 0.12)],
        4: [('arriba', 300, 'AMB', 'La izquierda aguanta Fa-Do (ligados): no la toques otra vez. '
                                   'La derecha repite La-Sol.', 0.15)],
        5: [('arriba', 300, 'OJO', 'Casilla 1.ª: toca los cc. 22-29 y vuelve al c. 10.', 0.1)],
        6: [('abajo', 300, 'OJO', 'Casilla 2.ª (cc. 30-33): derecha en silencio, izquierda sola. '
                                  'La 2.ª vez llegas aquí desde el c. 21.', 0.8)],
        7: [('arriba', 250, 'DER', 'Parte nueva. Las notas muy rápidas son semicorcheas: cuatro '
                                   'por golpe.', 0.1),
            ('abajo', 250, 'IZQ', 'Una sola nota larga por compás: La aguda y La grave.', 0.2)],
        8: [('arriba', 300, 'AMB', 'Cc. 38-39 repiten 34-35, ahora con acordes. Cc. 40-42: La, Sol, '
                                   'Mi-Re, Do y nota larga.', 0.2)],
        9: [('arriba', 300, 'OJO', 'Vuelve el tema. Cc. 43-46 se tocan dos veces (barra del c. 46).',
             0.1)],
        11: [('arriba', 300, 'AMB', 'Último compás: La larga en la derecha y silencio en la '
                                    'izquierda. Déjala sonar.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia los cuatro acordes de la izquierda')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_counting_stars.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
