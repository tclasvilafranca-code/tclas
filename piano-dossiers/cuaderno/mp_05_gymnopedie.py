# -*- coding: utf-8 -*-
"""Pieza 5 · Gymnopedie n.º 1 (Satie). MEDIDO a zoom (150 dpi) sobre el PDF (imagen escaneada de 3
   paginas, 64 ppi, 15 sistemas con el numero de compas impreso al inicio: 1,6,11,16,21,26,31,36,
   41,46,52,57,63,68,74): 12 sistemas de 5 compases y 3 de 6 (46, 57 y 68) = 78 compases.
   3/4, dos sostenidos (Re mayor), "Lent et douloureux". Todo son negras, blancas con puntillo y
   compases enteros de silencio: no hay figuras mas rapidas que la negra. Derecha en silencio en los
   cc. 1-4 y 40-43 (entra en el 2.º tiempo de los cc. 5, 13, 44 y 52). Matices: pp cc. 1, 5, 13, 40,
   44 y 52; f cc. 9 y 48; p cc. 22 y 61. Nota larga ligada: cc. 9-12, 19-21, 29-31, 48-51, 58-60.
   Becuadros en la melodia: cc. 27, 28, 38, 61, 63, 66, 67, 72, 73.
   La copia escaneada trae una franja gris a un lado: se blanquea en una copia limpia
   (students/eva_sc/source_limpia/, que no se versiona)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403


def _limpiar():
    """Copia de la partitura escaneada sin la franja gris lateral (no se toca el original)."""
    import io
    import numpy as np
    import pymupdf
    from PIL import Image
    src = os.path.join(SRCDIR, 'gymnopedie_e_satie.pdf')
    dst_dir = os.path.join(SRCDIR, '..', 'source_limpia')
    dst = os.path.abspath(os.path.join(dst_dir, 'gymnopedie_limpia.pdf'))
    if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src):
        return dst
    os.makedirs(dst_dir, exist_ok=True)
    d = pymupdf.open(src)
    out = pymupdf.open()
    for pg in d:
        xref = pg.get_images(full=True)[0][0]
        rect = pg.get_image_rects(xref)[0]
        pix = pymupdf.Pixmap(d, xref)
        if pix.n > 3:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        arr = np.frombuffer(pix.samples, np.uint8).reshape(pix.h, pix.w, pix.n)[:, :, :3].copy()
        g = arr.mean(2)
        panel = (g > 222) & (g < 250)
        cols = panel.mean(0) > 0.30
        arr[panel & cols[None, :]] = 255
        buf = io.BytesIO()
        Image.fromarray(arr).save(buf, 'PNG')
        npg = out.new_page(width=pg.rect.width, height=pg.rect.height)
        npg.insert_image(rect, stream=buf.getvalue())
    out.save(dst)
    return dst


SPEC = dict(
    num=5, slug='gymnopedie', pdf=_limpiar(), time_sig=(3, 4),
    titulo='Gymnopédie n.º 1', autor='Erik Satie · de las Trois Gymnopédies',
    kicker='Eva · pieza 5 · Gymnopédie n.º 1', mes='Enero · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=satie+gymnopedie+no+1+piano',
    credito='Partitura: Erik Satie, Gymnopédie n.º 1 (copia escaneada). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '3/4'), ('Tempo', 'Lent et douloureux'),
               ('Figura corta', 'Negra'), ('Compases', '78')],
        total=78,
        secciones=[('A', 1, 12, 'Entrada y 1.ª frase', AZUL), ('B', 13, 39, 'La melodía sigue', OCRE),
                   ('C', 40, 51, 'Silencio y vuelta', AZUL), ('D', 52, 78, 'Última melodía · final', OCRE)],
        ideas=[('IZQUIERDA', 'Bajo y acorde',
                'Casi cada compás: nota grave en el 1 y acorde en el 2. Es el balanceo de toda la '
                'pieza.'),
               ('DERECHA', 'Notas lentas',
                'Solo negras y notas largas, con ligaduras largas. No hay ninguna nota más '
                'rápida.'),
               ('EL SILENCIO', 'La derecha se calla',
                'En los cc. 1-4 y 40-43 solo toca la izquierda. Hay que contar esos compases.'),
               ('LOS MATICES', 'pp, p y f',
                'Casi todo es pp. Hay f en los cc. 9 y 48, y p en los cc. 22 y 61.')],
        especial=[
            'Pone "Lent et douloureux" (en francés: lento y doloroso).',
            'Dos sostenidos al principio: Re mayor (fa♯ y do♯). Compás de 3/4.',
            'La derecha empieza en silencio y entra en el c. 5, en el segundo tiempo.',
            'Hay becuadros en la melodía (cc. 27, 28, 61, 63, 66 y 67, entre otros).',
            'Una misma nota larga va ligada de compás en compás (cc. 9-12 y 48-51).',
            'Acaba en el c. 78 con dos acordes largos y la barra final.'],
        reto='Tocar muy lento y muy suave sin apresurarte: que el acorde caiga siempre en el '
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
             ('Cambia la nota grave', 'El bajo alterna entre notas graves distintas. Antes de '
                                      'cada compás, mira cuál toca.'),
             ('Cuando cambia el dibujo', 'En los cc. 37-39 y 76-78 la izquierda es distinta '
                                         '(negras o acordes largos). Míralos antes de tocar.')],
        der=[('Cantar antes de tocar', 'La melodía va en negras y notas largas con ligaduras '
                                       'largas. Cántala por dentro y respira donde acaba cada '
                                       'ligadura.'),
             ('Entrar a tiempo', 'En el c. 5 hay un silencio de negra y entras en el segundo '
                                 'tiempo. Antes, cuenta los cuatro compases de silencio.'),
             ('Notas largas ligadas', 'En los cc. 48-51 la misma nota va ligada de compás en '
                                      'compás: pulsa una vez y cuenta hasta el final.'),
             ('Los becuadros', 'En los cc. 27 y 28 hay becuadros. Di el nombre de cada nota '
                               'antes de tocarla.')],
        tecnica=['Brazo y muñeca sueltos: el sonido se deja caer, no se golpea.',
                 'Acorde de la izquierda más suave que la melodía.',
                 'Tempo muy lento: cuenta 1-2-3 sin acelerar.']),
    bloques=[
        B(1, 'cc. 1-5', 'La entrada', (0, 0),
          D('cuenta', 'Un compás de 3/4: tres golpes', [('un compás', 1, 3)]),
          [('IZQUIERDA', 'Bajo en el 1 y acorde en el 2, en pp. Cuatro compases iguales: tócalos '
                         'hasta que salgan solos.'),
           ('DERECHA', 'Silencio de negra y entras en el 2.º tiempo del c. 5 con dos negras, en '
                       'pp.'),
           ('JUNTAS', 'La izquierda toca sola cuatro compases y la derecha entra en el c. 5, sin '
                      'dudar.'),
           ('A TEMPO', 'Lent et douloureux (lento y doloroso): tres negras iguales y muy lentas.')]),
        B(2, 'cc. 6-15', 'La primera frase', (1, 2),
          D('grupos', 'La nota ligada de los cc. 9-12: 4 compases, 12 tiempos',
            (4, 3, ['c. 9', 'c. 10', 'c. 11', 'c. 12'])),
          [('IZQUIERDA', 'Igual que antes. En el c. 9 hay f: bajo y acorde algo más fuertes, sin '
                         'golpear.'),
           ('DERECHA', 'Cc. 6-8: tres negras por compás bajo una ligadura larga. Cc. 9-12: una '
                       'sola nota larga ligada.'),
           ('JUNTAS', 'Un sistema cada día: cc. 6-10 y cc. 11-15.'),
           ('OJO', 'En el c. 13 vuelve el pp y entras otra vez en el segundo tiempo.')]),
        B(3, 'cc. 16-25', 'La melodía sigue', (3, 4),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: bajo y acorde', 'puntos', OCRE)]),
          [('IZQUIERDA', 'El mismo dibujo en todos los compases: apréndelo de memoria.'),
           ('DERECHA', 'Notas largas en los cc. 16-21 (ligadas del 19 al 21) y tres negras por '
                       'compás en los cc. 22-24.'),
           ('JUNTAS', 'Un sistema cada día: cc. 16-20 y cc. 21-25.'),
           ('OJO', 'En el c. 22 hay p: un poco más fuerte que el pp de antes.')]),
        B(4, 'cc. 26-35', 'Los becuadros', (5, 6),
          D('fichas', 'Lo que hay que vigilar',
            ['becuadros en los cc. 27-28', 'notas largas en los cc. 32-33']),
          [('IZQUIERDA', 'En los cc. 27 y 28 el acorde lleva un becuadro: míralo antes de '
                         'tocar.'),
           ('DERECHA', 'Becuadros en la melodía de los cc. 27 y 28. Cc. 32-33: una nota larga '
                       'por compás.'),
           ('JUNTAS', 'Un sistema cada día: cc. 26-30 y cc. 31-35.'),
           ('OJO', 'Un becuadro vale solo hasta el final de su compás.')]),
        B(5, 'cc. 36-45', 'El silencio de la derecha', (7, 8),
          D('cadena', 'Lo que pasa en este bloque',
            [('cc. 38-39: acordes', False), ('c. 40: pp, derecha calla', False),
             ('c. 44: entra', True)]),
          [('IZQUIERDA', 'En el c. 37 hay dos negras y en los cc. 38-39 un acorde largo: míralo '
                         'antes de tocar.'),
           ('DERECHA', 'En los cc. 38-39 toca acordes largos y en el c. 40 se calla. Entra en el '
                       'c. 44.'),
           ('JUNTAS', 'Cuenta los cuatro compases de silencio (cc. 40-43) mientras la izquierda '
                      'sigue.'),
           ('OJO', 'En el c. 44 entras en el segundo tiempo y en pp, como en el c. 5.')]),
        B(6, 'cc. 46-56', 'De la f al pp', (9, 10),
          D('cadena', 'Hacia el final de la frase',
            [('c. 48: f', False), ('ligadas cc. 48-51', False), ('c. 52: pp', True)]),
          [('IZQUIERDA', 'Bajo y acorde como siempre, también durante las notas ligadas.'),
           ('DERECHA', 'Del c. 48 al c. 51 la misma nota larga va ligada: pulsa solo la primera '
                       'vez.'),
           ('JUNTAS', 'Un sistema cada día: cc. 46-51 y cc. 52-56.'),
           ('OJO', 'En el c. 52 vuelve el pp y la entrada de los cc. 5 y 44.')]),
        B(7, 'cc. 57-67', 'Ligaduras y becuadros', (11, 12),
          D('grupos', 'La nota ligada de los cc. 58-60: 3 compases, 9 tiempos',
            (3, 3, ['c. 58', 'c. 59', 'c. 60'])),
          [('IZQUIERDA', 'Mismo balanceo. Algunos acordes llevan becuadros, como el del c. 61.'),
           ('DERECHA', 'Cc. 58-60: nota ligada. En el c. 61 hay p; becuadros en los cc. 61, 63, '
                       '66 y 67.'),
           ('JUNTAS', 'Dos días: cc. 57-62 y cc. 63-67.'),
           ('OJO', 'Los reguladores < > piden subir y bajar el sonido muy poco a poco.')]),
        B(8, 'cc. 68-78', 'El final', (13, 14),
          D('cadena', 'Hacia el final',
            [('cc. 68-73: melodía', False), ('cc. 74-76: negras', False),
             ('cc. 77-78: acordes', True)]),
          [('IZQUIERDA', 'En el c. 76 hay dos negras y en los cc. 77-78 acordes largos.'),
           ('DERECHA', 'Becuadros en los cc. 72 y 73. En los cc. 77 y 78 toca acordes largos.'),
           ('JUNTAS', 'Los dos últimos sistemas, en bucle.'),
           ('A TEMPO', 'Deja sonar el último acorde y cuenta los tres tiempos enteros.')]),
    ],
    cortes={1: [256.0, 387.5, 511.2, 638.0], 2: [233.0, 359.8, 489.0, 606.0],
            3: [230.0, 362.0, 489.5, 625.8]},
    corte_titulo=149.2, inicio={1: 85.0}, fin={2: 731.2, 3: 762.8},
    burb={
        0: [('arriba', 250, 'OJO', 'Lent et douloureux: lento y doloroso. Tres negras por compás, '
                                   'muy suaves (pp).', 150),
            ('arriba', 250, 'DER', 'Silencio de negra y entras en el segundo tiempo del c. 5.', 485),
            ('abajo', 330, 'IZQ', 'Bajo en el 1 y acorde en el 2. Los cuatro primeros compases '
                                  'son para la izquierda sola.', 142)],
        1: [('arriba', 270, 'DER', 'Una sola ligadura larga cubre los cc. 6-8: tócalos como una '
                                   'frase y respira al final.', 200),
            ('arriba', 270, 'AMB', 'f en el c. 9. Desde aquí la misma nota va ligada hasta el c. '
                                   '12.', 398)],
        2: [('arriba', 330, 'AMB', 'c. 11-12: sigue la nota ligada (no la pulses otra vez). En el '
                                   'c. 13, pp y entra en el 2.º tiempo.', 120)],
        4: [('arriba', 300, 'AMB', 'p en el c. 22: un poco más fuerte que el pp. Tres negras por '
                                   'compás, parejas.', 185)],
        5: [('arriba', 330, 'OJO', 'Becuadros en los cc. 27 y 28, en la melodía y en el acorde '
                                   'de la izquierda.', 226)],
        7: [('arriba', 270, 'IZQ', 'Desde el c. 37 la izquierda cambia: dos negras y luego '
                                   'acordes largos.', 240),
            ('arriba', 270, 'AMB', 'c. 40: pp y la derecha se calla. Cuenta hasta el c. 44.', 487)],
        9: [('arriba', 300, 'AMB', 'f en el c. 48. La misma nota larga va ligada hasta el c. 51.',
             282)],
        11: [('arriba', 300, 'DER', 'Ligadas en los cc. 58-60 y p en el c. 61, con un becuadro en '
                                    'la melodía.', 372)],
        14: [('arriba', 300, 'AMB', 'Final: dos acordes largos. Deja que suenen y cuenta los '
                                    'tres tiempos.', 380)],
    },
    marcas=[(1, 485, 180, 70, 30, 1, 1, 'caja'), (1, 399.5, 327.5, 17, 17, 2, 1, 'caja'),
            (1, 284, 443, 22, 16, 2, 2, 'caja'), (2, 282.5, 671, 19, 18, 6, 1, 'caja'),
            (3, 374, 291, 16, 18, 7, 1, 'caja')],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Re mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_gymnopedie.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
