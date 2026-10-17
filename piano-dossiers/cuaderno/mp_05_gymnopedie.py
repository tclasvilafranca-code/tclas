# -*- coding: utf-8 -*-
"""Pieza 5 · Gymnopedie n.º 1 (Satie). MEDIDO sobre el PDF (imagen escaneada de 3 paginas, 15
   sistemas, numeros de compas impresos al inicio de cada sistema: 1,6,11,16,21,26,31,36,41,46,52,
   57,63,68,74; el ultimo sistema tiene 5 compases -> 78 compases): 3/4, dos sostenidos (Re mayor),
   "Lent et douloureux", todo en negras y notas largas (negra = figura mas corta); derecha en
   silencio en cc. 1-4 y 40-43; matices pp (cc. 1, 5, 13, 40, 44, 52), f (cc. 9 y 48), p (cc. 22 y 61).
   No verificado: nombres exactos de las notas (imagen de 64 ppi)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=5, slug='gymnopedie', pdf='gymnopedie_e_satie.pdf', time_sig=(3, 4),
    titulo='Gymnopédie n.º 1', autor='Erik Satie · de las Trois Gymnopédies',
    kicker='Eva · pieza 5 · Gymnopédie n.º 1', mes='Enero · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=satie+gymnopedie+no+1+piano',
    credito='Partitura: Erik Satie, Gymnopédie n.º 1 (copia escaneada). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '3/4'), ('Tempo', 'Lent et douloureux'),
               ('Figura corta', 'Negra'), ('Compases', '78')],
        total=78,
        secciones=[('A', 1, 4, 'La izquierda sola', AZUL), ('B', 5, 39, 'La melodía', OCRE),
                   ('C', 40, 43, 'Silencio otra vez', AZUL), ('D', 44, 73, 'Vuelve la melodía', OCRE),
                   ('E', 74, 78, 'Final', AZUL)],
        ideas=[('IZQUIERDA', 'Nota grave y acorde',
                'Casi cada compás: una nota grave en el primer tiempo y un acorde en el segundo. '
                'Es el balanceo de toda la pieza.'),
               ('DERECHA', 'Negras y notas largas',
                'La melodía es lenta: negras y notas largas, en frases con ligaduras largas. '
                'No hay notas rápidas.'),
               ('EL SILENCIO', 'La derecha se calla',
                'En los cc. 1-4 y 40-43 solo toca la izquierda. Hay que contar esos compases.'),
               ('LOS MATICES', 'pp, p y f',
                'Casi todo es muy suave (pp). Hay una f en los cc. 9 y 48 y una p en los cc. 22 '
                'y 61.')],
        especial=[
            'Pone "Lent et douloureux" (en francés: lento y doloroso).',
            'Dos sostenidos al principio: Re mayor (fa♯ y do♯). Compás de 3/4.',
            'La derecha empieza en silencio: entra en el c. 5, en el segundo tiempo.',
            'Hay becuadros sueltos en la melodía (por ejemplo en los cc. 27 y 28).',
            'Muchas notas largas ligadas, por ejemplo en los cc. 48-51.',
            'Acaba en el c. 78 con dos acordes largos y la barra final.'],
        reto='Tocar muy lento y muy suave sin apresurarse: que el acorde caiga siempre en el '
             'segundo tiempo y que la melodía cante por encima.',
        truco='Cuenta 1-2-3 en voz baja. Primero la izquierda sola, mirando la partitura; luego '
              'añade solo la primera nota larga de cada frase de la derecha.',
        sabias='Satie compuso las tres Gymnopédies hacia 1888 y esta es la primera, la más '
               'conocida. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchala siguiendo la partitura con el dedo: cuenta los tres tiempos.',
        ts=(3, 4),
        cuenta_pie='Un compás de 3/4 en negras: tres golpes iguales, lentos. Aquí solo el ritmo; '
                   'las notas, en tu partitura.',
        ritmos=[('LA CUENTA', '3/4 · tres negras',
                 [{'pitch': 'B4', 'dur': 'q'} for _ in range(3)], OCRE, 'treble', None)]),
    manos=dict(
        izq=[('Bajo y acorde', 'Cada compás: nota grave en el 1 y acorde en el 2. Toca solo un '
                               'compás, despacio, hasta que salga sin mirar las manos.'),
             ('Cuenta 1-2-3', 'Cuenta en voz baja y sin prisa: el bajo cae en el 1 y el acorde '
                              'en el 2. Todo muy suave (pp).'),
             ('Cambia la nota grave', 'El bajo alterna entre dos notas graves. Antes de cada '
                                      'compás, mira cuál toca.'),
             ('Cuando cambia el dibujo', 'En los cc. 37-39 y 76-78 la izquierda es distinta. '
                                         'Míralos antes de tocar.')],
        der=[('Cantar antes de tocar', 'La melodía va en negras y notas largas con ligaduras '
                                       'largas. Cántala por dentro y respira donde acaba cada '
                                       'ligadura.'),
             ('Entrar a tiempo', 'En el c. 5 hay un silencio de negra y entras en el segundo '
                                 'tiempo. Cuenta los cuatro compases de antes.'),
             ('Notas largas ligadas', 'En los cc. 48-51 la misma nota va ligada de compás en '
                                      'compás: pulsa una vez y cuenta hasta el final.'),
             ('Los becuadros', 'En los cc. 27 y 28 hay becuadros. Di el nombre de cada nota '
                               'antes de tocarla.')],
        tecnica=['Brazo y muñeca sueltos: el sonido se deja caer, no se golpea.',
                 'Acorde de la izquierda más suave que la melodía.',
                 'Tempo muy lento: cuenta 1-2-3 sin acelerar.']),
    bloques=[
        B(1, 'cc. 1-5', 'La entrada', (0, 0),
          D('cadena', 'Cómo empieza', [('izquierda sola cc. 1-4', False),
                                       ('entra la derecha c. 5', True)]),
          [('IZQUIERDA', 'Nota grave en el 1 y acorde en el 2, en pp. Los cuatro primeros '
                         'compases son solo para ti.'),
           ('DERECHA', 'Cuenta cuatro compases y entra en el c. 5, en el segundo tiempo.'),
           ('JUNTAS', 'Despacio, cuenta 1-2-3 hasta que la entrada salga sin dudar.'),
           ('A TEMPO', 'Lent et douloureux: muy lento y muy suave.')]),
        B(2, 'cc. 6-15', 'La primera frase', (1, 2),
          D('cadena', 'Los matices', [('c. 9: f', False), ('c. 13: pp', True)]),
          [('IZQUIERDA', 'El mismo balanceo: bajo y acorde.'),
           ('DERECHA', 'Una frase con ligadura larga. En el c. 9 hay f y notas largas ligadas.'),
           ('JUNTAS', 'Un sistema cada día: cc. 6-10 y cc. 11-15.'),
           ('OJO', 'En el c. 13 vuelves a pp: baja el sonido de golpe pero con suavidad.')]),
        B(3, 'cc. 16-30', 'La melodía sigue', (3, 5),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: bajo y acorde', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Sigue igual. Aprende de memoria este balanceo.'),
           ('DERECHA', 'Frases largas ligadas. En el c. 22 hay una p.'),
           ('JUNTAS', 'Un sistema cada día: cc. 16-20, 21-25 y 26-30.'),
           ('OJO', 'Los becuadros de los cc. 27 y 28: léelos nota a nota.')]),
        B(4, 'cc. 31-40', 'Hacia el silencio', (6, 7),
          D('cadena', 'Lo que cambia', [('notas largas', False), ('izquierda distinta cc. 37-39',
                                                                  False), ('c. 40: derecha en '
                                                                           'silencio', True)]),
          [('IZQUIERDA', 'En los cc. 37-39 el dibujo cambia: míralo antes de tocar.'),
           ('DERECHA', 'Notas largas en los cc. 32-33; en los cc. 38-39 hay acordes. '
                       'Cuéntalas enteras.'),
           ('JUNTAS', 'Un sistema cada día: cc. 31-35 y cc. 36-40.'),
           ('OJO', 'En el c. 40 la derecha se calla con pp.')]),
        B(5, 'cc. 41-51', 'Vuelve a entrar', (8, 9),
          D('cadena', 'La vuelta', [('cc. 41-43: silencio', False), ('c. 44: entra en pp', False),
                                    ('c. 48: f', True)]),
          [('IZQUIERDA', 'Sola en los cc. 41-43, igual que al principio.'),
           ('DERECHA', 'Entra en el c. 44, en el segundo tiempo y en pp.'),
           ('JUNTAS', 'Cuenta los tres compases de silencio y entra.'),
           ('OJO', 'En el c. 48 hay f y notas largas ligadas hasta el c. 51.')]),
        B(6, 'cc. 52-78', 'Los últimos sistemas', (10, 14),
          D('cadena', 'Hacia el final', [('c. 52: pp', False), ('c. 61: p', False),
                                         ('cc. 77-78: acordes', True)]),
          [('IZQUIERDA', 'El mismo balanceo hasta el c. 75; al final cambia (cc. 76-78).'),
           ('DERECHA', 'Frases largas con reguladores < y >. Al final, acordes largos.'),
           ('JUNTAS', 'Un sistema cada día. Es el tramo más largo: ve despacio.'),
           ('A TEMPO', 'Deja sonar el último acorde y cuenta los tres tiempos enteros.')]),
    ],
    cortes={1: [256.0, 387.5, 511.2, 638.0], 2: [233.0, 359.8, 489.0, 606.0],
            3: [230.0, 362.0, 489.5, 625.8]},
    corte_titulo=149.2, inicio={1: 85.0}, fin={2: 731.2, 3: 762.8},
    burb={
        0: [('arriba', 250, 'OJO', 'Lent et douloureux: lento y doloroso. Muy suave: pp.', 0.1),
            ('arriba', 250, 'DER', 'La derecha entra en el c. 5, en el segundo tiempo.', 0.85),
            ('abajo', 330, 'IZQ', 'Nota grave en el 1 y acorde en el 2. Los cc. 1-4 son para la '
                                  'izquierda sola.', 0.25)],
        1: [('arriba', 300, 'AMB', 'f en el c. 9: suena más fuerte; las notas largas van ligadas.',
             0.76)],
        5: [('arriba', 330, 'OJO', 'Becuadros en los cc. 27 y 28: léelos nota a nota.', 0.3)],
        7: [('arriba', 270, 'IZQ', 'Desde el c. 37 la izquierda cambia de dibujo.', 0.3),
            ('arriba', 230, 'AMB', 'c. 40: la derecha se calla (cc. 40-43), pp.', 0.83)],
        9: [('arriba', 300, 'AMB', 'f en el c. 48. Las notas largas ligadas llegan hasta el c. '
                                   '51.', 0.36)],
        14: [('arriba', 300, 'AMB', 'Final: dos acordes largos. Deja que suenen y cuenta los '
                                    'tres tiempos.', 0.75)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Re mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_gymnopedie.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
