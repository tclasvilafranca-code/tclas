# -*- coding: utf-8 -*-
"""Pieza 10 · Perfect (Ed Sheeran), arreglo de Elaine Kelkel (Musescore, marzo de 2021). MEDIDO sobre
   el PDF de Drive: 2 paginas A4, 54 compases (el c. 1 es una anacrusa de tres corcheas), una
   armadura de un sostenido (Sol mayor), 6/8, negra con puntillo = 70, sin matices ni repeticiones,
   cifrados impresos G, Em, C, D y D/F#; izquierda en seis corcheas por compas (arpegio de tres
   notas dos veces) hasta el c. 45, acordes de blanca con puntillo en los cc. 46-49 y notas
   sueltas en los cc. 50-53; corchea como figura mas corta."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=10, slug='perfect', pdf='perfect.pdf', time_sig=(6, 8),
    titulo='Perfect', autor='Ed Sheeran · arreglo de Elaine Kelkel',
    kicker='Sharifa · pieza 10 · Perfect', mes='Mayo · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=ed+sheeran+perfect+piano+tutorial',
    credito='Partitura: arreglo de Elaine Kelkel (Musescore, 2021). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '6/8'), ('Tempo', '♩. = 70'),
               ('Figura corta', 'Corchea'), ('Compases', '54')],
        total=54,
        secciones=[('A', 1, 17, 'Primera parte', AZUL),
                   ('B', 18, 33, 'Segunda parte', OCRE),
                   ('C', 34, 45, 'Un acorde por compás', AZUL),
                   ('D', 46, 54, 'Final', OCRE)],
        ideas=[('LOS ACORDES', 'Cuatro, en bucle',
                'Sol mayor, Mi menor, Do mayor y Re mayor (la partitura los imprime como G, Em, '
                'C y D). Casi toda la pieza gira entre ellos.'),
               ('IZQUIERDA', 'Un arpegio por compás',
                'Tres notas del acorde, de abajo arriba, dos veces por compás: seis corcheas.'),
               ('DERECHA', 'Melodía con puntillos',
                'Notas largas con puntillo y algunas corcheas. Empieza antes del compás (anacrusa).'),
               ('EL FINAL', 'Cambia la izquierda',
                'En los cc. 46-49 la izquierda toca acordes largos y en los cc. 50-53 notas '
                'sueltas.')],
        especial=[
            'Pone negra con puntillo = 70: dos pulsos por compás.',
            'El c. 1 es una anacrusa: tres corcheas que empiezan antes del primer compás.',
            'Cifrados impresos: G = Sol mayor, Em = Mi menor, C = Do mayor, D = Re mayor.',
            'En el c. 50 aparece D/F♯: Re mayor con Fa♯ en el bajo (primera inversión).',
            'No hay repeticiones ni matices escritos: elige tú dónde suena más suave.',
            'Los cc. 46-49 tienen acordes de tres notas en la izquierda.'],
        reto='Mantener las seis corcheas de la izquierda parejas mientras la derecha canta '
             'notas largas por encima.',
        truco='Estudia la izquierda en bucle: cuatro compases (Sol, Mi menor, Do, Re). Cuando salga '
              'sola, añade la derecha de dos en dos compases.',
        sabias='«Perfect» (2017) es una balada de Ed Sheeran del álbum «÷» (Divide). Fue el número 1 '
               'de Navidad de 2017 en Reino Unido y habla de su pareja, Cherry Seaborn.',
        qr_texto='Escúchala y cuenta dos pulsos por compás con la partitura delante.',
        ts=(6, 8), cuenta_pie='Un compás de 6/8: dos golpes, cada uno con tres corcheas. Aquí '
                              'solo el ritmo, sobre una nota cualquiera.'),
    manos=dict(
        izq=[('Tres notas que suben', 'En cada compás la izquierda toca tres notas del acorde, de '
                                      'abajo arriba, y repite. Haz solo el primer compás, diez '
                                      'veces.'),
             ('Cuatro compases', 'Sol, Mi menor, Do, Re: cuatro dibujos casi iguales. Cámbialos '
                                 'sin parar el pulso.'),
             ('Parejo y suave', 'Las seis corcheas iguales y muy suaves. Cuenta 1-2-3, 4-5-6.'),
             ('Los acordes del final', 'Cc. 46-49: acordes de tres notas con blanca con puntillo. '
                                       'Las tres juntas, sin romper.')],
        der=[('Antes del compás', 'La pieza empieza con tres corcheas de anacrusa. Cántalas y '
                                  'entra en la última corchea del compás.'),
             ('Notas con puntillo', 'La melodía va en negras con puntillo y blancas con '
                                    'puntillo. Cuenta 1-2-3 por cada una.'),
             ('Las corcheas', 'Hay grupos de corcheas entre las notas largas. Tócalas '
                              'tranquilas, sin correr.'),
             ('Con la izquierda', 'Une los cc. 2-5 despacio, con metrónomo. Si se rompe, vuelve a '
                                  'una mano.')],
        tecnica=['Muñeca suelta: el arpegio de la izquierda sube y baja sin golpear.',
                 'Cuenta dos pulsos largos por compás (1-2-3, 4-5-6), no seis rápidos.',
                 'Empieza a la mitad de la velocidad y sube poco a poco.']),
    bloques=[
        B(1, 'cc. 1-5', 'Anacrusa y primera frase', (0, 0),
          D('grupos', 'Un compás de 6/8 = 2 golpes · 3 corcheas cada uno',
            (2, 3, ['golpe 1', 'golpe 2'])),
          [('DERECHA', 'Tres corcheas de anacrusa y notas largas. Cántalas antes de tocar.'),
           ('IZQUIERDA', 'Silencio en el c. 1. Desde el c. 2 el arpegio de Sol y, en el c. 4, de '
                         'Mi menor.'),
           ('JUNTAS', 'Cc. 2-5 en bucle, con la anacrusa de entrada.'),
           ('A TEMPO', 'Negra con puntillo = 70. Empieza a la mitad.')]),
        B(2, 'cc. 6-9', 'Do y Re', (1, 1),
          D('cadena', 'Los acordes del bloque', [('Do mayor', False), ('Re mayor', True)]),
          [('DERECHA', 'Corcheas y notas largas. Cuenta bien las notas largas de los cc. 8-9.'),
           ('IZQUIERDA', 'Dos compases de arpegio de Do y dos de Re.'),
           ('JUNTAS', 'De dos en dos compases, y luego los cuatro.'),
           ('OJO', 'Al final de los cc. 5, 9 y 13 hay corcheas que llevan al compás siguiente.')]),
        B(3, 'cc. 10-13', 'Vuelve la primera frase', (2, 2),
          D('cadena', 'El camino', [('Sol', False), ('Mi menor', True)]),
          [('DERECHA', 'Sol mayor y Mi menor otra vez. La melodía es nueva: léela antes.'),
           ('IZQUIERDA', 'Cuatro compases de arpegios, como en los cc. 2-5.'),
           ('JUNTAS', 'Los cuatro compases y la última corchea, que lleva al siguiente.'),
           ('OJO', 'Compara con los cc. 2-5: parecidos, pero no iguales.')]),
        B(4, 'cc. 14-17', 'Do, Re y arriba', (3, 3),
          D('cadena', 'El camino', [('Do mayor', False), ('Re mayor', False), ('seis corcheas', True)]),
          [('DERECHA', 'En el c. 17 hay seis corcheas seguidas. Cuéntalas de tres en '
                       'tres.'),
           ('IZQUIERDA', 'Arpegios de Do y de Re, igual que en el bloque 2.'),
           ('JUNTAS', 'Dos compases y luego cuatro, sin parar.'),
           ('A TEMPO', 'Prepárate para el cambio de Re a Sol en el c. 18.')]),
        B(5, 'cc. 18-25', 'Segunda vez', (4, 5),
          D('cadena', 'Mismo camino', [('Sol', False), ('Mi m.', False), ('Do', False),
                                       ('Re', True)]),
          [('DERECHA', 'La melodía hace notas largas en el mismo orden que antes.'),
           ('IZQUIERDA', 'Mismos cuatro arpegios: Sol, Mi menor, Do, Re.'),
           ('JUNTAS', 'Un sistema cada vez: cc. 18-21 y 22-25.'),
           ('OJO', 'La melodía es nueva: lee con cuidado antes de tocar.')]),
        B(6, 'cc. 26-33', 'Tercera vez', (6, 7),
          D('cadena', 'Mismo camino', [('Sol', False), ('Mi m.', False), ('Do', False),
                                       ('Re', True)]),
          [('DERECHA', 'Mismos acordes; la melodía se parece a la de los cc. 18-25.'),
           ('IZQUIERDA', 'Mismos arpegios: ya los sabes de memoria.'),
           ('JUNTAS', 'Los cc. 26-29 y 30-33, uno cada día.'),
           ('A TEMPO', 'Toca los cc. 18-33 seguidos.')]),
        B(7, 'cc. 34-45', 'Un acorde por compás', (8, 10),
          D('cadena', 'Los acordes cambian cada compás',
            [('Mi menor', False), ('Do', False), ('Sol', False), ('Re', True)]),
          [('DERECHA', 'Notas más agudas, con notas largas y corcheas. Cambian los '
                       'dibujos.'),
           ('IZQUIERDA', 'Un arpegio distinto por compás: Mi menor, Do, Sol, Re.'),
           ('JUNTAS', 'Un sistema cada día: cc. 34-37, 38-41 y 42-45.'),
           ('OJO', 'El orden de los acordes se repite cada cuatro compases.')]),
        B(8, 'cc. 46-54', 'Final', (11, 12),
          D('cadena', 'Hacia el final',
            [('acordes largos', False), ('notas sueltas', False), ('Sol', True)]),
          [('DERECHA', 'Notas largas, cada vez más tranquilas. El último compás es Sol.'),
           ('IZQUIERDA', 'Cc. 46-49: acordes de tres notas. Cc. 50-53: notas sueltas, '
                         'con Fa♯ en el c. 50.'),
           ('JUNTAS', 'Cc. 46-49 y 50-54 por separado, y luego juntos.'),
           ('OJO', 'El acorde del último compás es de Sol mayor: déjalo sonar.')]),
    ],
    cortes={1: [206.5, 319.5, 437.5, 555.5, 672.5],
            2: [154.2, 256.8, 357.0, 459.8, 574.0, 682.0]},
    corte_titulo=93.0, inicio={1: 30, 2: 52},
    burb={
        0: [('arriba', 330, 'DER', 'Tres corcheas de anacrusa: entras antes del compás, en la '
                                   'última corchea. Cántalas.', 0.1),
            ('abajo', 330, 'IZQ', 'Silencio en el c. 1. Desde el c. 2: tres notas de Sol, dos '
                                  'veces por compás.', 0.4)],
        1: [('arriba', 330, 'AMB', 'Do mayor (C) y Re mayor (D): la izquierda cambia de dibujo '
                                   'cada dos compases.', 0.3)],
        2: [('arriba', 330, 'OJO', 'Vuelve la primera frase: Sol mayor (G) y Mi menor (Em).',
             0.3)],
        3: [('arriba', 330, 'AMB', 'Cuenta 1-2-3, 4-5-6. En el c. 17 hay seis corcheas '
                                   'seguidas: cuéntalas de tres en tres.', 0.5)],
        4: [('arriba', 330, 'AMB', 'Segunda vez: la izquierda repite Sol, Mi menor, Do y Re.',
             0.2)],
        7: [('arriba', 330, 'OJO', 'Tercera vez. Compara con los cc. 18-25: lo que cambia es la '
                                   'derecha.', 0.3)],
        8: [('arriba', 330, 'AMB', 'Ahora el acorde cambia cada compás: Mi menor, Do, Sol, Re.',
             0.2)],
        11: [('arriba', 330, 'IZQ', 'Cc. 46-49: la izquierda toca acordes de tres notas, de blanca '
                                    'con puntillo.', 0.2)],
        12: [('arriba', 330, 'IZQ', 'Cc. 50-53: notas sueltas. En el c. 50, D/F♯ = Re mayor con '
                                    'Fa♯ en el bajo.', 0.1),
             ('abajo', 330, 'AMB', 'Último compás: acorde de Sol mayor. Déjalo sonar.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_perfect.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
