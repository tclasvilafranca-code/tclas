# -*- coding: utf-8 -*-
"""Pieza 14 · Mariage d'amour (Paul de Senneville). MEDIDO sobre el PDF (6 paginas A4, imagen
   escaneada, 35 sistemas, 83 compases con numeracion impresa al inicio de cada sistema):
   negra = 78, armadura de DOS bemoles (si y mi bemol; Sol menor), 4/4 con compases de 5/4
   (cc. 3, 7, 25, 45, 50, 73, 77), 3/4 en el c. 10 y 3/8 en el c. 58; 8va sobre la derecha desde
   el c. 12; calderones en el c. 20 y en el ultimo compas; mp en el c. 12 y p / mp en el c. 81;
   semicorchea como figura corta en las carreras de la derecha."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=14, slug='mariage', pdf='mariage_damour.pdf', time_sig=(4, 4),
    titulo="Mariage d'amour", autor='Paul de Senneville · edición para piano',
    kicker="Eva · pieza 14 · Mariage d'amour", mes='Mayo · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=mariage+d%27amour+piano+tutorial',
    credito="Partitura: Mariage d'amour (copia escaneada). Anotaciones: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '4/4 con 5/4'), ('Tempo', '♩ = 78'),
               ('Figura corta', 'Semicorchea'), ('Compases', '83')],
        total=83,
        secciones=[('A', 1, 3, '', AZUL), ('B', 4, 11, 'Tema', OCRE),
                   ('C', 12, 26, 'Con 8va', AZUL), ('D', 27, 54, 'Sigue y crece', OCRE),
                   ('E', 55, 68, 'Notas altas', AZUL), ('F', 69, 83, 'Final', OCRE)],
        ideas=[('IZQUIERDA', 'Corcheas en vaivén',
                'Empieza sola, con ocho corcheas por compás. Es el acompañamiento de casi '
                'toda la pieza.'),
               ('DERECHA', 'Carreras rápidas',
                'En los compases de 5/4 la derecha sube y baja en semicorcheas rápidas. Entre '
                'medias, notas más tranquilas.'),
               ('EL 8va', 'Una octava más aguda',
                'Desde el c. 12 hay líneas de puntos con "8": toca esas notas una octava más '
                'aguda de lo escrito.'),
               ('LOS COMPASES', '4/4, 5/4, 3/4 y 3/8',
                'El compás base es 4/4. Cambia a 5/4 en varias frases, a 3/4 en el c. 10 y a '
                '3/8 en el c. 58.')],
        especial=[
            'Pone negra = 78: la negra es el pulso.',
            'La armadura tiene dos bemoles (si♭ y mi♭): Sol menor.',
            'Los dos primeros compases son de silencio en la derecha: la izquierda empieza sola.',
            'El compás alterna 4/4 y 5/4 (por ejemplo, cc. 3, 7 y 25); en el c. 10 hay un 3/4.',
            'Desde el c. 12 aparecen líneas de 8va: notas una octava más agudas.',
            'Hay un calderón en el c. 20 y otro en la nota final (c. 83).'],
        reto='Que las corcheas de la izquierda suenen siempre iguales y suaves mientras la '
             'derecha cambia de dibujo y de compás.',
        truco='Mira primero solo los compases con compás distinto de 4/4 (5/4, 3/4, 3/8) y '
              'cuéntalos en voz alta antes de tocar.',
        sabias='Esta melodía es muy conocida como "Mariage d\'amour" y la popularizó el '
               'pianista Richard Clayderman en los años 70. (Dato de memoria, sin verificar.)',
        qr_texto='Escúchala con la partitura delante y cuenta los compases de 5/4.',
        ts=(4, 4), cuenta_titulo='Cómo se cuenta el 4/4 (el compás base)'),
    manos=dict(
        izq=[('Un compás, ocho corcheas', 'Aprende solo el primer compás, despacio, diez veces '
                                         'seguidas sin fallar.'),
             ('Parejo y suave', 'Metrónomo lento y las corcheas iguales: ninguna debe '
                                'sobresalir.'),
             ('Cuando cambia', 'Del c. 14 en adelante el dibujo de la izquierda se hace más '
                               'rápido en algunos compases. Míralo antes.'),
             ('De memoria', 'Si sabes el dibujo de memoria, la derecha puede cantar.')],
        der=[('Cantar antes de tocar', 'Escucha la melodía y cántala: así sabes adónde va cada '
                                       'frase.'),
             ('Las carreras', 'Estudia una carrera de semicorcheas sola, despacio. Luego sube '
                              'el metrónomo poco a poco.'),
             ('El 8va', 'Lee la nota escrita y toca una octava más aguda mientras dure la línea '
                        'de puntos.'),
             ('Con la izquierda', 'Une un sistema con la izquierda ya segura. Si se rompe, '
                                  'vuelve a una mano.')],
        tecnica=['Muñeca suelta: las carreras salen solas si no aprietas.',
                 'Cuenta negras, también en los compases de 5/4.',
                 'Sonido suave y parejo en la izquierda: la melodía manda.']),
    bloques=[
        B(1, 'cc. 1-3', 'La entrada', (0, 0),
          D('cuenta', 'Un compás de 4/4: 4 golpes de 2 corcheas', [('un compás', 4, 2)]),
          [('IZQUIERDA', 'Empieza sola: ocho corcheas por compás, despacio y parejo.'),
           ('DERECHA', 'Dos compases de silencio. Entra en el c. 3 con una carrera.'),
           ('JUNTAS', 'Dos compases de izquierda y, en el tercero, entra la derecha.'),
           ('A TEMPO', 'Negra = 78.')]),
        B(2, 'cc. 4-11', 'El primer tema', (1, 3),
          D('cadena', 'Los compases cambian',
            [('4/4', False), ('5/4 (c. 7)', False), ('3/4 (c. 10)', True)]),
          [('IZQUIERDA', 'Mismo vaivén de corcheas, con cambios de nota.'),
           ('DERECHA', 'Carreras de semicorcheas y notas más tranquilas en medio.'),
           ('JUNTAS', 'Un sistema cada día: cc. 4-6, 7-8 y 9-11.'),
           ('OJO', 'Cuenta negras: 5/4 son cinco y 3/4 son tres.')]),
        B(3, 'cc. 12-26', 'Con 8va', (4, 10),
          D('cadena', 'El 8va',
            [('nota escrita', False), ('suena una octava más aguda', True)]),
          [('IZQUIERDA', 'Pasa de corcheas a semicorcheas en algunos compases.'),
           ('DERECHA', 'Desde el c. 12 hay 8va: toca una octava más aguda mientras dure.'),
           ('JUNTAS', 'Siete sistemas: uno cada día.'),
           ('OJO', 'En el c. 12 pone mp y en el c. 20 hay un calderón.')]),
        B(4, 'cc. 27-54', 'Sigue y crece', (11, 22),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: corcheas', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Corcheas parejas; cambia de clave en algunos compases.'),
           ('DERECHA', 'La melodía vuelve con más variaciones. Reconoce lo que ya sabes.'),
           ('JUNTAS', 'Doce sistemas: dos por sesión, sin prisa.'),
           ('OJO', 'Mira el compás: aparecen 5/4 en los cc. 45 y 50.')]),
        B(5, 'cc. 55-68', 'Notas altas', (23, 28),
          D('cadena', 'El 3/8 del c. 58',
            [('4/4', False), ('3/8 (c. 58)', True), ('4/4', False)]),
          [('IZQUIERDA', 'Semicorcheas en la izquierda: despacio y parejas.'),
           ('DERECHA', 'Notas altas con 8va y adornos. Lee nota a nota.'),
           ('JUNTAS', 'Un sistema cada día.'),
           ('OJO', 'El c. 58 es de 3/8: seis semicorcheas. Cuéntalo despacio.')]),
        B(6, 'cc. 69-83', 'El final', (29, 34),
          D('cadena', 'Hacia el final', [('carreras', False), ('silencios', False),
                                       ('calderón', True)]),
          [('IZQUIERDA', 'Vuelven las corcheas de la entrada; al final hay silencios.'),
           ('DERECHA', 'Carreras y notas altas con 8va. En el último sistema, ritmos '
                       'de silencios.'),
           ('JUNTAS', 'Un sistema cada día, y luego todo seguido.'),
           ('A TEMPO', 'En el c. 81 pone p y mp. Acaba con calderón.')]),
    ],
    cortes={1: [227.8, 366.2, 504.5, 644.2], 2: [162.2, 289.5, 410, 530.5, 655.2],
            3: [162.2, 285, 409, 532, 652], 4: [159, 292, 409, 536, 654],
            5: [165, 292, 411, 530, 653], 6: [165, 286, 409, 532, 644]},
    corte_titulo=97.2,
    burb={
        0: [('abajo', 250, 'IZQ', 'Empiezas tú, sola: ocho corcheas por compás. Despacio y '
                                  'parejo.', 0.2),
            ('abajo', 290, 'DER', 'La derecha entra en el c. 3 (5/4) con una carrera de '
                                  'semicorcheas.', 0.6)],
        2: [('arriba', 330, 'OJO', 'c. 7: otra vez 5/4. Cuenta cinco negras, luego 4/4.', 0.1)],
        3: [('arriba', 330, 'OJO', 'c. 10: 3/4, solo tres negras. En el c. 11 vuelve el 4/4.', 0.45)],
        4: [('arriba', 330, 'AMB', 'Desde aquí hay 8va (línea de puntos): derecha una octava '
                                   'más aguda. mp.', 0.05)],
        8: [('arriba', 330, 'OJO', 'Calderón en el c. 20: alarga la nota, sin contar.', 0.1)],
        24: [('arriba', 330, 'OJO', 'c. 58: compás de 3/8, seis semicorcheas. Cuenta despacio.', 0.7)],
        34: [('arriba', 330, 'AMB', 'p y mp en el c. 81; calderón en la nota final: déjala '
                                   'sonar.', 0.5)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Sol menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_mariage.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
