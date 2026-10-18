# -*- coding: utf-8 -*-
"""Pieza 6 · Up, tema principal (Giacchino), Easy version. MEDIDO sobre el PDF (1 pagina, imagen
   de baja resolucion, 35 compases en 4 sistemas de 8, 9, 10 y 8): un bemol (Fa mayor), 3/4, solo
   el matiz p en el c. 1, sin tempo, sin repeticiones, corchea como figura mas corta (sin
   semicorcheas), sin digitacion impresa. Izquierda: c. 1 en silencio y un acorde de tres o
   cuatro notas por compas (blanca con puntillo), con ligaduras entre compases (6-7, 8-9, 12-13,
   14-15, 16-17, 23-24, 25-26, 29-30, 31-32, 33-34) y becuadros en los cc. 6, 8, 11, 23, 25 y 28;
   desde el c. 18 la izquierda lee en clave de sol. Los cc. 18-27 repiten los cc. 1-10 una octava
   mas aguda y los cc. 28-35 los cc. 11-17 (+ Fa largo final)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=6, slug='up', pdf='copia_de_up.pdf', time_sig=(3, 4),
    titulo='Up · tema principal', autor='Michael Giacchino · música de la película «Up» · Easy version',
    kicker='Sharifa · pieza 6 · Up (tema principal)', mes='Febrero · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=up+pixar+main+theme+married+life+piano+easy',
    credito='Partitura: «Up - Main theme», Easy version (música de M. Giacchino). '
            'Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '3/4'), ('Tempo', 'Sin indicar'),
               ('Figura corta', 'Corchea'), ('Compases', '35')],
        total=35,
        secciones=[('A', 1, 8, 'El tema', AZUL), ('B', 9, 17, 'Segunda frase', OCRE),
                   ('C', 18, 27, 'El tema, más agudo', AZUL), ('D', 28, 35, 'Final', OCRE)],
        ideas=[('IZQUIERDA', 'Un acorde por compás',
                'Acordes de tres o cuatro notas, de compás entero. Algunos van ligados al '
                'compás siguiente.'),
               ('DERECHA', 'Frases con respiro',
                'Cada frase entra tras un silencio y acaba en una nota larga. Hay que cantarla.'),
               ('LOS CAMBIOS', 'Un bemol y becuadros',
                'El Si es bemol en toda la pieza. En la izquierda, algún becuadro (cc. 6, 8, '
                '11...).'),
               ('LA CLAVE', 'Clave de sol abajo',
                'Desde el c. 18 la mano izquierda lee en clave de sol: mira la clave.')],
        especial=[
            'Armadura de un bemol (Si♭): la pieza está en Fa mayor.',
            'Compás de 3/4: tres negras por compás. No indica tempo.',
            'Solo hay un matiz: p (suave) en el c. 1.',
            'La derecha entra en el «y» del 2.º tiempo: silencio de negra y de corchea, y tres '
            'corcheas.',
            'La izquierda calla en el c. 1 y desde el c. 18 lee en clave de sol.',
            'Los cc. 18-27 repiten los cc. 1-10, una octava más aguda.'],
        reto='Que la izquierda no tape la melodía: acordes suaves (p) y la derecha cantando '
             'encima.',
        truco='Tararea la melodía antes de tocarla. Las frases se repiten, así que aprendes '
              'pocas y valen para toda la pieza.',
        sabias='«Up» es una película de Pixar de 2009. Su música es de Michael Giacchino, que '
               'ganó con ella el Óscar a la mejor banda sonora original.',
        qr_texto='Escúchala: ¿oyes cómo cada frase acaba en una nota larga?', ts=(3, 4)),
    manos=dict(
        izq=[('Un acorde, un compás', 'Cada acorde dura el compás entero. Tócalo, aguántalo y '
                                      'cuenta 1-2-3 sin soltarlo.'),
             ('Los ligados', 'Si dos acordes están unidos por una ligadura (cc. 6-7), se toca '
                             'el primero y se aguanta.'),
             ('Los becuadros', 'En los cc. 6, 8 y 11 hay un becuadro: ese Si no es bemol, es '
                               'Si natural.'),
             ('Clave de sol', 'Desde el c. 18 la izquierda lee en clave de sol. Mira la clave '
                              'antes de tocar.')],
        der=[('Cantar primero', 'Tararea los cc. 1-8: Fa-La-Fa, y Mi largo. Luego tócalos '
                                'despacio.'),
             ('Entrar en el «y»', 'Cuenta «1, 2-y, 3-y»: la melodía entra en el «y» del 2. '
                                  'Los silencios cuentan.'),
             ('Las frases', 'Cada frase acaba en una nota larga (cc. 2, 10 y 17). Respira '
                            'ahí.'),
             ('Una octava arriba', 'En el c. 18 vuelve el tema, igual pero más agudo: lee las '
                                   'notas altas con calma.')],
        tecnica=['Brazo suelto y dedos curvos: acordes sin apretar.',
                 'La izquierda suena suave (p) y la melodía manda.',
                 'Cuenta 1-2-3 sin correr y sin parar.']),
    bloques=[
        B(1, 'cc. 1-8', 'El tema', (0, 0),
          D('cadena', 'El c. 1 de la derecha',
            [('silencio de negra', False), ('silencio de corchea', False), ('3 corcheas', True)]),
          [('IZQUIERDA', 'El c. 1 en silencio. Del 2 al 7, un acorde por compás.'),
           ('DERECHA', 'Fa-La-Fa y Mi largo. Frases de dos compases.'),
           ('JUNTAS', 'De dos en dos compases: 1-2, 3-4, 5-6, 7-8.'),
           ('OJO', 'Becuadro en la izquierda (cc. 6 y 8). Matiz p en el c. 1.')]),
        B(2, 'cc. 9-17', 'Segunda frase', (1, 1),
          D('cadena', 'Tres frases con nota larga',
            [('cc. 9-10', False), ('cc. 11-13', False), ('cc. 14-17', True)]),
          [('IZQUIERDA', 'Un acorde por compás. Ligados: 12-13, 14-15 y 16-17. Becuadro en el 11.'),
           ('DERECHA', 'Cada frase acaba en nota larga (cc. 10, 13 y 17).'),
           ('JUNTAS', 'Frase a frase: 9-10, 11-13 y 14-17.'),
           ('OJO', 'Desde el c. 14 la melodía sube por pasos hasta la nota larga del c. 17.')]),
        B(3, 'cc. 18-27', 'El tema, más agudo', (2, 2),
          D('cadena', 'La misma melodía',
            [('cc. 1-10', False), ('una octava arriba', True), ('cc. 18-27', False)]),
          [('IZQUIERDA', 'El c. 18 en silencio, con cambio a clave de sol. Luego, acorde por '
                         'compás.'),
           ('DERECHA', 'Es la melodía de los cc. 1-10, más aguda: líneas adicionales arriba.'),
           ('JUNTAS', 'Toca antes los cc. 1-10: es la misma música en otro sitio.'),
           ('OJO', 'Becuadros en los cc. 23 y 25, ligados con el compás siguiente.')]),
        B(4, 'cc. 28-35', 'El final', (3, 3),
          D('cadena', 'Hacia el final',
            [('cc. 28-33', False), ('Mi largo', False), ('Fa largo: FIN', True)]),
          [('IZQUIERDA', 'Becuadro en el 28. Ligados: 29-30, 31-32 y 33-34. El 35, un acorde.'),
           ('DERECHA', 'La frase vuelve y sube por pasos: termina en Mi largo y Fa largo.'),
           ('JUNTAS', 'Los cuatro últimos compases en bucle, cantando.'),
           ('A TEMPO', 'La pieza entera de seguido. Aguanta el Fa final el compás entero.')]),
    ],
    cortes={1: [264.0, 426.5, 592.0]},
    corte_titulo=122.2,
    burb={
        0: [('arriba', 250, 'DER', 'Entras en el «y» del 2.º tiempo: silencio de negra, silencio '
                                   'de corchea y tres corcheas. Matiz p.', 0.12),
            ('arriba', 250, 'IZQ', 'El c. 1 es silencio. En el c. 2 entra el primer acorde.', 0.3),
            ('abajo', 300, 'OJO', 'Becuadros en la izquierda (cc. 6 y 8): ese Si no es bemol.',
             0.8)],
        1: [('arriba', 300, 'AMB', 'Cada frase acaba en una nota larga (cc. 10, 13 y 17): '
                                   'respira ahí.', 0.2),
            ('abajo', 300, 'IZQ', 'Ligados: 12-13, 14-15 y 16-17. Toca el primero y aguanta. '
                                  'Becuadro en el c. 11.', 0.6)],
        2: [('arriba', 250, 'DER', 'Vuelve el tema una octava más aguda: es la música de los '
                                   'cc. 1-10.', 0.1),
            ('arriba', 250, 'IZQ', 'Desde aquí la izquierda lee en clave de sol: mira la clave.',
             0.2),
            ('abajo', 300, 'OJO', 'Becuadros en los cc. 23 y 25, ligados con el compás '
                                  'siguiente.', 0.6)],
        3: [('arriba', 300, 'IZQ', 'Becuadro en el c. 28. Ligados: 29-30, 31-32 y 33-34.', 0.1),
            ('abajo', 300, 'AMB', 'Fa largo final (c. 35): aguántalo el compás entero y suelta '
                                  'con las dos manos.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia el c. 1 o escribe la escala de Fa mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_up.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
