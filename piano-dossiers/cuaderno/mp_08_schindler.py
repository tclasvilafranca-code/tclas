# -*- coding: utf-8 -*-
"""Pieza 8 · Theme from Schindler's List (John Williams), descarga de Musescore. MEDIDO sobre el
   PDF (2 paginas carta, 9 sistemas, 27 compases numerados; el c. 1 es una sola negra con
   calderon): dos bemoles (Sol menor, con fa sostenido), 4/4, "Expressively" sin metronomo, mp,
   rit., a tempo, dim., cresc., rall., "a tempo, moving along", mf, "passionately", p; acordes
   arpegiados (linea ondulada), doble barra oblicua en el c. 11, clave de sol en la izquierda
   en el c. 26 y calderon final; semicorchea la figura mas corta (cc. 12, 13, 15, 23).
   La marca de agua de Musescore (primera linea de cada pagina) se excluye con `inicio`."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=8, slug='schindler', pdf='schindlers_list.pdf', time_sig=(4, 4),
    titulo="Theme from Schindler's List", autor='John Williams · arreglo para piano',
    kicker="Eva · pieza 8 · Schindler's List", mes='Febrero · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=schindler%27s+list+theme+piano+tutorial',
    credito="Partitura: J. Williams, Theme from Schindler's List (Musescore). Anotaciones: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '4/4'), ('Carácter', 'Expressively'),
               ('Figura corta', 'Semicorchea'), ('Compases', '27')],
        total=27,
        secciones=[('A', 1, 3, 'Entrada · mp', AZUL), ('B', 4, 9, 'El tema · cresc.', OCRE),
                   ('C', 10, 15, 'dim. · rall. · a tempo', AZUL),
                   ('D', 16, 24, 'mf · passionately', OCRE), ('E', 25, 27, 'Final · p', AZUL)],
        ideas=[('IZQUIERDA', 'Acordes y bajo',
                'Acordes de dos o tres notas y notas sueltas del bajo, en negras y blancas. '
                'Muchos acordes llevan una línea ondulada.'),
               ('DERECHA', 'Melodía a dos notas',
                'Corcheas y negras que cantan, a menudo con una segunda nota debajo, tocadas a '
                'la vez.'),
               ('EL TEMPO', 'Respira todo el rato',
                'Hay rit., rall. y a tempo una y otra vez: la pieza no va a una velocidad fija.'),
               ('LOS MATICES', 'mp → mf → p',
                'Empieza en mp, llega a mf y "passionately" en el c. 18, y acaba en p con dim.')],
        especial=[
            'Pone "Expressively" y no trae metrónomo: el tempo lo marca la expresión.',
            'Dos bemoles (si♭, mi♭) y fa♯ en varios compases (cc. 3, 7, 10...): Sol menor.',
            'El c. 1 es una sola nota con calderón; el tema empieza en el c. 2.',
            'La línea ondulada junto a un acorde: tócalo de abajo arriba, rápido (arpegiado).',
            'rit./rall. (cc. 3, 11, 15, 24) y a tempo (cc. 4, 12, 16): cuida cada cambio.',
            'En el c. 26 la izquierda pasa a clave de sol. El acorde final (c. 27) lleva '
            'calderón en las dos manos.'],
        reto='Cantar la melodía con expresión mientras la izquierda cambia entre acordes y notas '
             'sueltas, y seguir todos los cambios de tempo y de matiz.',
        truco='Marca con lápiz en tu partitura cada rit., rall. y a tempo, y ensaya cada cambio '
              'suelto, con dos compases antes y dos después.',
        sabias='La música es de John Williams para la película "La lista de Schindler" (1993) de '
               'Steven Spielberg. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchala con la partitura delante y sigue los rit. y los a tempo.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Acordes y notas sueltas', 'Aprende la sucesión de posiciones: acorde, nota suelta, '
                                         'acorde. Toca solo el primer sistema, despacio.'),
             ('Acordes arpegiados', 'Con la línea ondulada toca la nota más grave primero y '
                                    'sube rápido; deja sonar la última.'),
             ('Pasajes que suben', 'En el c. 11 hay corcheas que suben y en el c. 23, '
                                   'semicorcheas. Tócalos lentos y parejos.'),
             ('Clave de sol en la izquierda', 'En el c. 26 las tres últimas notas de la izquierda '
                                              'se leen en clave de sol: míralo antes.')],
        der=[('Cantar la melodía', 'Cántala por dentro y respira en los silencios. Marca con '
                                   'lápiz los rit. y los a tempo.'),
             ('Dos notas a la vez', 'A menudo la melodía lleva otra nota debajo: lee las dos '
                                    'juntas y toca con la mano relajada.'),
             ('Fa♯ y silencios', 'El fa♯ aparece en varios compases (cc. 3, 7, 10...). En los '
                                 'cc. 12 y 14 empiezas tras un silencio de corchea: cuéntalo.'),
             ('Con la izquierda', 'Une despacio un sistema con la izquierda ya segura. Si se '
                                  'rompe, vuelve a una mano.')],
        tecnica=['Brazo y muñeca sueltos: la melodía se canta, no se golpea.',
                 'Cuenta 1-2-3-4 y marca tú el rit. y el rall., no la prisa.',
                 'Estudia cada cambio de tempo por separado antes de unirlo.']),
    bloques=[
        B(1, 'cc. 1-6', 'La entrada', (0, 1),
          D('cadena', 'Calderón → tema → rit. → a tempo', [('c. 1: calderón', False),
                                                          ('c. 2: el tema', False), ('c. 3: rit.', False),
                                                          ('c. 4: a tempo', True)]),
          [('IZQUIERDA', 'c. 2: acorde largo arpegiado y, encima, negras iguales; luego acordes.'),
           ('DERECHA', 'Nota con calderón y corcheas que cantan en mp; fa♯ en el c. 3.'),
           ('JUNTAS', 'Dos tramos: cc. 1-3 y cc. 4-6; en cada uno, lento.'),
           ('OJO', 'rit. en el c. 3, a tempo con regulador creciente en el c. 4, dim. en el c. 6.')]),
        B(2, 'cc. 7-9', 'El tema crece', (2, 2),
          D('cadena', 'Los matices', [('c. 7', False), ('cresc. (c. 8)', False),
                                      ('ligaduras largas (c. 9)', True)]),
          [('IZQUIERDA', 'Acordes arpegiados y blancas; en el c. 9 una ligadura larga.'),
           ('DERECHA', 'Dos voces a la vez en el c. 7; fa♯ en los cc. 7 y 9.'),
           ('JUNTAS', 'Un compás cada vez, y después los tres.'),
           ('OJO', 'cresc. en el c. 8; en el c. 9 mantén las notas ligadas, no las repitas.')]),
        B(3, 'cc. 10-12', 'Calma y vuelta', (3, 3),
          D('cadena', 'Cambios de tempo', [('dim. (c. 10)', False), ('rall. (c. 11)', False),
                                           ('a tempo, moving along (c. 12)', True)]),
          [('IZQUIERDA', 'Corcheas que suben en el c. 11; en el c. 12, silencios de corchea y '
                         'acordes.'),
           ('DERECHA', 'c. 12: semicorcheas tras un silencio de corchea. Entra justo.'),
           ('JUNTAS', 'Toca el c. 11 y el c. 12 seguidos, con el cambio de tempo.'),
           ('OJO', 'La doble barra oblicua (//) del c. 11 es una pausa corta.')]),
        B(4, 'cc. 13-15', 'Acordes entre silencios', (4, 4),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: acordes', 'puntos', OCRE, 4)]),
          [('IZQUIERDA', 'Silencio de corchea y acorde de tres notas, una y otra vez.'),
           ('DERECHA', 'Semicorcheas en los cc. 13-15 y una ligadura larga en el c. 15.'),
           ('JUNTAS', 'Cuenta los silencios de la izquierda en voz alta.'),
           ('OJO', 'rit. en el c. 15, justo antes del a tempo del c. 16.')]),
        B(5, 'cc. 16-21', 'Más fuerza', (5, 6),
          D('cadena', 'Los matices', [('mf (c. 16)', False), ('passionately (c. 18)', False),
                                      ('dim. (c. 19)', False), ('cresc. (c. 20)', True)]),
          [('IZQUIERDA', 'Muchos acordes arpegiados: sube rápido y mantén el pulso.'),
           ('DERECHA', 'Acento (>) en el c. 16; corcheas con acordes de dos notas.'),
           ('JUNTAS', 'Dos tramos: cc. 16-18 y cc. 19-21.'),
           ('OJO', 'mf con regulador y "a tempo" en el c. 16; "passionately" en el c. 18.')]),
        B(6, 'cc. 22-24', 'La ola se calma', (7, 7),
          D('cadena', 'Hacia el final', [('c. 23: semicorcheas (izq.)', False), ('dim.', False),
                                         ('rall. (c. 24)', True)]),
          [('IZQUIERDA', 'c. 23: semicorcheas que suben hasta una nota larga.'),
           ('DERECHA', 'Acordes de dos y tres notas con ligaduras; fa♯ en cc. 22-24.'),
           ('JUNTAS', 'Toca cc. 22-24 en bucle, sin acelerar.'),
           ('OJO', 'dim. y rall. en el c. 24: más suave y más lento.')]),
        B(7, 'cc. 25-27', 'El final', (8, 8),
          D('cadena', 'Hacia el final', [('p (c. 25)', False), ('dim. (c. 26)', False),
                                         ('calderón (c. 27)', True)]),
          [('IZQUIERDA', 'c. 26: las tres últimas notas, en clave de sol. c. 27: acorde de tres '
                         'notas.'),
           ('DERECHA', 'c. 26: corcheas que suben, con rayita encima (tenuto); c. 27: acorde de tres notas.'),
           ('JUNTAS', 'Los tres compases en bucle.'),
           ('A TEMPO', 'p y dim.: casi sin sonido. Calderón en las dos manos: alarga.')]),
    ],
    cortes={1: [249.5, 410.8, 571.2], 2: [174.5, 319.5, 457.0, 583.5]},
    corte_titulo=89.2, inicio={1: 25.2, 2: 33.2},
    burb={
        0: [('arriba', 270, 'OJO', 'Calderón en el c. 1: dura lo que quieras. Dos bemoles: Sol '
                                   'menor. Empieza en mp.', 0.05),
            ('arriba', 270, 'IZQ', 'c. 2: abajo, acorde largo arpegiado (línea ondulada: de abajo '
                                   'arriba); arriba, negras iguales.', 0.55)],
        1: [('arriba', 330, 'AMB', 'a tempo y regulador creciente en el c. 4; dim. en el c. 6.',
             0.3)],
        3: [('arriba', 270, 'OJO', 'rall. en el c. 11. La doble barra oblicua (//) es una pausa '
                                   'corta.', 0.35),
            ('arriba', 270, 'DER', 'c. 12: "a tempo, moving along" y semicorcheas tras un silencio '
                                   'de corchea.', 0.8)],
        4: [('arriba', 330, 'IZQ', 'Silencio de corchea y acorde, una y otra vez (cc. 12-14): '
                                   'cuenta el silencio.', 0.1)],
        5: [('arriba', 270, 'AMB', 'c. 16: mf, a tempo y un acento (>). En el c. 18: regulador '
                                   'creciente y "passionately".', 0.1),
            ('arriba', 270, 'DER', 'Las corcheas llevan acordes de dos notas: toca las dos '
                                   'juntas, con la melodía arriba.', 0.7)],
        7: [('arriba', 270, 'IZQ', 'c. 23: semicorcheas que suben en la izquierda.', 0.3),
            ('arriba', 270, 'OJO', 'c. 24: dim. y rall.: más suave y más lento.', 0.8)],
        8: [('arriba', 270, 'OJO', 'c. 26: las tres últimas notas de la izquierda van en clave de '
                                   'sol.', 0.5),
            ('arriba', 270, 'AMB', 'Acorde final arpegiado, con calderón en las dos manos.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_schindler.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
