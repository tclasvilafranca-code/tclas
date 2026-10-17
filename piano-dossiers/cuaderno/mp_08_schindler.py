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
                'Acordes (dos o más notas) y notas sueltas del bajo, casi siempre en negras y '
                'blancas. Muchos acordes llevan una línea ondulada.'),
               ('DERECHA', 'Melodía con segunda voz',
                'Corcheas y negras que cantan, a menudo con una segunda nota debajo, tocadas a '
                'la vez.'),
               ('EL TEMPO', 'Respira todo el rato',
                'Hay rit., rall. y a tempo una y otra vez: la pieza no va a una velocidad fija.'),
               ('LOS MATICES', 'mp → mf → p',
                'Empieza en mp, crece hasta mf y passionately, y acaba en p con dim.')],
        especial=[
            'Pone "Expressively" y no trae metrónomo: el tempo lo marca la expresión.',
            'Dos bemoles (si♭ y mi♭): Sol menor, con fa♯ en varios compases (cc. 3, 7...).',
            'El c. 1 es una sola nota con calderón; el tema empieza en el c. 2.',
            'Las líneas onduladas junto a un acorde: se toca de abajo arriba, rápido (arpegiado).',
            'rit./rall. (cc. 3, 11, 15, 24) y a tempo (cc. 4, 12, 16): cuidado con cada uno.',
            'En el c. 26 la izquierda pasa a clave de sol. Acaba con calderón (c. 27).'],
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
             ('Clave de sol en la izquierda', 'En el c. 26 la izquierda lee en clave de sol: '
                                              'mira la clave antes de tocar.')],
        der=[('Cantar la melodía', 'Cántala por dentro y respira en los silencios. Marca con '
                                   'lápiz los rit. y los a tempo.'),
             ('Dos notas a la vez', 'A menudo la melodía lleva otra nota debajo: lee las dos '
                                    'juntas y toca con la mano relajada.'),
             ('Fa♯ y silencios', 'El fa♯ aparece en varios compases (cc. 3, 7...). En los cc. '
                                 '12-14 hay silencios de corchea: cuéntalos.'),
             ('Con la izquierda', 'Une despacio un sistema con la izquierda ya segura. Si se '
                                  'rompe, vuelve a una mano.')],
        tecnica=['Brazo y muñeca sueltos: la melodía se canta, no se golpea.',
                 'Cuenta 1-2-3-4 y deja que el rit. y el rall. los marques tú, no la prisa.',
                 'Estudia cada cambio de tempo por separado antes de unirlo.']),
    bloques=[
        B(1, 'cc. 1-3', 'La entrada', (0, 0),
          D('cadena', 'Calderón → tema → rit.', [('c. 1: una nota con calderón', False),
                                                 ('c. 2: empieza el tema', False),
                                                 ('c. 3: rit.', True)]),
          [('IZQUIERDA', 'Silencio con calderón; en los cc. 2-3 acordes arpegiados y notas sueltas.'),
           ('DERECHA', 'Una nota larga y luego corcheas que cantan en mp.'),
           ('JUNTAS', 'Compás a compás, y después los tres.'),
           ('OJO', 'El calderón alarga la nota: no cuentes, escucha.')]),
        B(2, 'cc. 4-9', 'El tema crece', (1, 2),
          D('cadena', 'Los matices', [('a tempo', False), ('dim.', False), ('cresc.', True)]),
          [('IZQUIERDA', 'Acordes arpegiados y notas sueltas: coloca la mano antes de cada cambio.'),
           ('DERECHA', 'Corcheas con segunda nota; fa♯ en el c. 7.'),
           ('JUNTAS', 'Un sistema cada día: cc. 4-6 y cc. 7-9.'),
           ('OJO', 'a tempo en el c. 4, dim. en el c. 6 y cresc. en el c. 8.')]),
        B(3, 'cc. 10-15', 'Calma y vuelta', (3, 4),
          D('cadena', 'Cambios de tempo', [('dim.', False), ('rall.', False),
                                           ('a tempo, moving along', False), ('rit.', True)]),
          [('IZQUIERDA', 'Corcheas que suben en el c. 11; luego acordes entre silencios.'),
           ('DERECHA', 'Doble barra oblicua al final del c. 11: una pausa corta. Silencios en '
                       'los cc. 12-14.'),
           ('JUNTAS', 'Dos sistemas: cc. 10-12 y cc. 13-15.'),
           ('OJO', 'rall. en el c. 11, a tempo en el c. 12 y rit. en el c. 15.')]),
        B(4, 'cc. 16-24', 'Más fuerza', (5, 7),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: acordes', 'puntos', OCRE, 4)]),
          [('IZQUIERDA', 'Muchos acordes arpegiados: sube rápido y mantén el pulso.'),
           ('DERECHA', 'mf en el c. 16 y "passionately" en el c. 18; después cresc. y dim.'),
           ('JUNTAS', 'Un sistema cada día: cc. 16-18, 19-21 y 22-24.'),
           ('OJO', 'Semicorcheas en la izquierda del c. 23. rall. en el c. 24.')]),
        B(5, 'cc. 25-27', 'El final', (8, 8),
          D('cadena', 'Hacia el final', [('p', False), ('dim.', False), ('calderón', True)]),
          [('IZQUIERDA', 'En el c. 26 pasa a clave de sol; en el c. 27, acorde con calderón.'),
           ('DERECHA', 'Notas que bajan y luego suben en el c. 26; acorde final.'),
           ('JUNTAS', 'Los tres compases en bucle.'),
           ('A TEMPO', 'p y dim.: acaba casi sin sonido y alarga el último acorde.')]),
    ],
    cortes={1: [249.5, 410.8, 571.2], 2: [174.5, 319.5, 457.0, 583.5]},
    corte_titulo=89.2, inicio={1: 25.2, 2: 33.2},
    burb={
        0: [('arriba', 270, 'OJO', 'Calderón en el c. 1: alarga la nota. Dos bemoles: Sol menor. '
                                   'Empieza en mp.', 0.05),
            ('abajo', 270, 'IZQ', 'La línea ondulada: toca el acorde de abajo arriba, rápido.', 0.1)],
        1: [('arriba', 300, 'AMB', 'rit. en el c. 3, a tempo en el c. 4 y dim. en el c. 6.', 0.45)],
        3: [('arriba', 300, 'OJO', 'rall. (c. 11) y a tempo, moving along (c. 12). La doble barra '
                                   'oblicua es una pausa corta.', 0.5)],
        5: [('arriba', 300, 'DER', 'mf en el c. 16 y "passionately" en el c. 18: con ganas.', 0.1)],
        7: [('arriba', 300, 'IZQ', 'Semicorcheas que suben en la izquierda del c. 23.', 0.3)],
        8: [('arriba', 300, 'OJO', 'En el c. 26 la izquierda lee en clave de sol. Calderón final.',
             0.55)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_schindler.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
