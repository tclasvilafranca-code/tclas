# -*- coding: utf-8 -*-
"""Pieza 9 · Scherzo (Diabelli, op. 149 n.º 6), a cuatro manos. MEDIDO sobre el PDF (2 paginas,
   48 compases en 6 sistemas de 8): 3/4, Allegro sin metronomo, Do mayor sin armadura; Trio desde
   el c. 33 con tres bemoles (bajo y acordes sobre Do: Do menor). Primo en dos pentagramas (el de
   arriba con 8va), Secondo en dos. Repeticiones: :| al final del c. 16 (vuelve al c. 1); |: en el
   c. 17 y :| en el c. 32 (con 'Fine'); Trio |: c. 33 y :| c. 48 con 'Scherzo D.C. al Fine'. Las
   barras finales de los cc. 24 y 40 salen cortadas en el PDF. Figura corta: corchea (las notitas
   de adorno de los cc. 14 y 30 llevan doble barra). Matices p, f, reguladores, acentos >."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=9, slug='scherzo', pdf='scherzo_4_manos.pdf', time_sig=(3, 4),
    titulo='Scherzo', autor='Anton Diabelli · op. 149 n.º 6 · a cuatro manos',
    kicker='Eva · pieza 9 · Scherzo (Diabelli)', mes='Marzo · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=diabelli+scherzo+op+149+no+6+piano+4+hands',
    credito='Partitura: A. Diabelli, op. 149 n.º 6 (free-scores.com). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'), ('Tempo', 'Allegro'),
               ('Figura corta', 'Corchea'), ('Compases', '48')],
        total=48,
        secciones=[('A', 1, 16, 'Scherzo, 1.ª parte (se repite)', AZUL),
                   ('B', 17, 32, 'Scherzo, 2.ª parte (se repite) y Fine', OCRE),
                   ('T', 33, 48, 'Trio, con tres bemoles (se repite)', VERDE)],
        ideas=[('PRIMO', 'La melodía, arriba',
                'Va con 8va (suena una octava más aguda) y muchas notas llevan una marca de '
                'picado.'),
               ('SECONDO', 'Bajo y acordes',
                'Abajo hay un bajo y, después, dos acordes por compás.'),
               ('EL RECORRIDO', 'Scherzo, Trio, D.C.',
                'Scherzo, Trio y otra vez el Scherzo hasta "Fine" (D.C. al Fine).'),
               ('LOS MATICES', 'p · f · < >',
                'Cambios de golpe entre p y f, reguladores y acentos (>).')],
        especial=[
            'Pone "Allegro" y el compás es 3/4: tres negras por compás.',
            'Es a cuatro manos: Primo arriba y Secondo abajo.',
            'Barras de repetición: al final del c. 16 (vuelve al c. 1) y entre los cc. 17 y 32.',
            'En el c. 32 pone "Fine" y en el c. 48 "Scherzo D.C. al Fine".',
            'El Trio (cc. 33-48) cambia la armadura a tres bemoles.',
            'Notitas de adorno (cc. 14 y 30) y mi bemol en el Scherzo (c. 19).'],
        reto='Tocar el recorrido sin perderos: Scherzo con sus repeticiones, Trio y vuelta al '
             'principio hasta "Fine".',
        truco='Antes de tocar, seguid el camino con el dedo sobre la partitura, diciendo en voz '
              'alta dónde se vuelve y dónde se acaba.',
        sabias='(No verificado) Scherzo significa "broma" en italiano; es una pieza viva y '
               'ligera. Diabelli escribió estas piezas melódicas para estudiar a cuatro manos.',
        qr_texto='Escúchalo y sigue el camino: Scherzo, Trio y vuelta al Scherzo.', ts=(3, 4),
        cuenta_pie='Un compás de 3/4: tres golpes, cada uno con dos corcheas. Aquí solo el '
                   'ritmo, sobre una nota cualquiera.'),
    manos=dict(
        titulo='Secondo y Primo',
        sub='Cada parte se aprende sola. Luego os cambiáis de parte y juntas, despacio.',
        tit_izq='SECONDO · la parte grave', tit_der='PRIMO · la parte aguda',
        izq=[('El bajo, primero', 'Cada compás empieza con una nota grave y dos silencios. '
                                  'Tócala contando "uno-dos-tres".'),
             ('Los acordes', 'Encima, dos acordes por compás tras un silencio. Estúdialos solos, '
                             'cortitos y a tempo.'),
             ('Las dos líneas', 'Júntalos: bajo en el 1 y acordes en el 2 y el 3.'),
             ('El Trio', 'Cambian los bemoles (tres). Lee la armadura antes de empezar.')],
        der=[('Cantar la melodía', 'Cántala por dentro: notas largas y grupos de corcheas '
                                   'ligadas.'),
             ('El picado', 'Muchas notas llevan una marca de picado: cortas y ligeras.'),
             ('El 8va', 'El pentagrama de arriba va con 8va: lees lo escrito y suena una '
                        'octava más aguda.'),
             ('Con el Secondo', 'Tocad juntas despacio: el Primo escucha al Secondo.')],
        tecnica=['Muñecas sueltas: acordes cortos y ligeros, sin apretar.',
                 'Contad en voz alta "uno-dos-tres" antes de empezar, juntas.',
                 'Cambiad de parte: así se aprenden las dos.']),
    bloques=[
        B(1, 'cc. 1-8', 'El tema, en p', (0, 0),
          D('capas', 'Tres capas a la vez (un compás)',
            [('Primo: melodía', 'barras', AZUL), ('Secondo: acordes', 'puntos', OCRE, 2),
             ('Secondo: bajo', 'barras', OCRE)]),
          [('SECONDO', 'Bajo en el 1 y dos acordes en p. Suaves y cortos.'),
           ('PRIMO', 'La melodía en p, con corcheas ligadas y marcas de picado.'),
           ('JUNTAS', 'Contad "uno-dos-tres" y empezad a la vez.'),
           ('OJO', 'Reguladores < > en los cc. 2-4.')]),
        B(2, 'cc. 9-16', 'En f, y se repite', (1, 1),
          D('cadena', 'El recorrido', [('cc. 1-16', False), ('repite', False),
                                       ('luego cc. 17-32', True)]),
          [('SECONDO', 'f en el c. 9. El bajo baja hasta un fa sostenido en el c. 13.'),
           ('PRIMO', 'Acentos (>) en los cc. 11-12; notitas de adorno en el c. 14.'),
           ('JUNTAS', 'Al final del c. 16 hay una barra de repetición: volved al c. 1.'),
           ('OJO', 'Fa sostenido del bajo (c. 13): un sostenido que no está en la armadura.')]),
        B(3, 'cc. 17-24', 'Parte central, en p', (2, 2),
          D('cadena', 'Los matices', [('p', False), ('acento >', False), ('regulador <', True)]),
          [('SECONDO', 'Vuelve el p. Acordes con mi bemol en los cc. 19-20 y 22-23.'),
           ('PRIMO', 'Notas largas con acento (>) y mi bemol en los cc. 19 y 22.'),
           ('JUNTAS', 'Una barra |: marca el principio de la repetición del c. 17.'),
           ('OJO', 'El regulador < de los cc. 23-24 lleva al f del c. 25.')]),
        B(4, 'cc. 25-32', 'Vuelve el tema y "Fine"', (3, 3),
          D('cadena', 'La repetición', [('c. 25 f', False), ('c. 32 :| ', False),
                                        ('vuelta al c. 17', True)]),
          [('SECONDO', 'f desde el c. 25. Mismo diseño que los cc. 9-16.'),
           ('PRIMO', 'Los reguladores > de los cc. 27-28 y la notita de adorno del c. 30.'),
           ('JUNTAS', 'Al final del c. 32 hay :| y "Fine": se repite y luego pasáis al Trio.'),
           ('OJO', '"Fine" marca dónde se acaba al volver del D.C.')]),
        B(5, 'cc. 33-40', 'Trio: tres bemoles', (4, 4),
          D('cadena', 'Lo nuevo', [('3 bemoles', False), ('p', False), ('f en el c. 37', True)]),
          [('SECONDO', 'Bajo largo en los cc. 37-39 y acordes con sostenidos y becuadros.'),
           ('PRIMO', 'Melodía ligada y suave; en el c. 37 llega el f con acentos.'),
           ('JUNTAS', 'Leed la armadura: tres bemoles. Despacio, cuatro compases cada vez.'),
           ('OJO', 'Barra |: en el c. 33: el Trio se repite.')]),
        B(6, 'cc. 41-48', 'Final del Trio y D.C.', (5, 5),
          D('cadena', 'Después del Trio', [('c. 48 :|', False), ('D.C.', False),
                                           ('c. 1 → Fine', True)]),
          [('SECONDO', 'Acordes con mi bemol y un regulador antes del f del c. 45.'),
           ('PRIMO', 'p y luego < f. Acaba en nota larga ligada y silencios.'),
           ('JUNTAS', '"Scherzo D.C. al Fine": volved al c. 1 y tocad hasta "Fine".'),
           ('A TEMPO', 'Toda la pieza con su recorrido, sin parar.')]),
    ],
    cortes={1: [315.0, 569.2], 2: [271.0, 522.5]}, corte_titulo=86.3,
    fin={1: 802, 2: 790},
    burb={
        0: [('arriba', 330, 'AMB', 'Allegro, 3/4, en p. Cuenta "uno-dos-tres". El pentagrama de '
                                   'arriba del Primo va con 8va.', 0.25)],
        1: [('arriba', 330, 'OJO', 'Barra de repetición al final del c. 16: volved al c. 1.',
             0.95)],
        2: [('arriba', 330, 'OJO', 'Barra |: en el c. 17: aquí empieza la repetición.', 0.03)],
        3: [('arriba', 330, 'OJO', 'c. 32: barra :| y "Fine". Tras repetir, pasáis al Trio.',
             0.9)],
        4: [('arriba', 330, 'AMB', 'Trio: tres bemoles y |: en el c. 33. En el c. 37, f.', 0.1)],
        5: [('arriba', 330, 'OJO', '"Scherzo D.C. al Fine": volved al c. 1 y tocad hasta '
                                   '"Fine" (c. 32).', 0.85)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_scherzo.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
