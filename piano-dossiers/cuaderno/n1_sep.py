# -*- coding: utf-8 -*-
"""SEPTIEMBRE · Notacion musical y figuras."""
from n1_base import *
from n1_base import _abs_idx
from reportlab.lib.colors import HexColor
from notation import draw_staff, draw_clef, note_y, draw_notehead, draw_note

MES = 'Septiembre'


# ------------------------------------------------------------------ diagramas
def diag_pentagrama():
    """Pentagrama con lineas y espacios numerados (izquierda) y las siete notas de Do a Do (derecha)."""
    h = 128

    def f(c, x, y, w):
        g = 10.0
        xs, ws = x + 4, 150
        top = y - 34
        ys = draw_staff(c, xs, top, ws, g)
        draw_clef(c, xs + 4, ys[-1], g, 'treble')
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY)
        c.drawString(xs, y - 8, 'LÍNEAS Y ESPACIOS')
        for k in range(5):
            c.setFont('DejaVuSans-Bold', 7.2)
            c.setFillColor(OCRE)
            c.drawString(xs + ws + 8, ys[-1 - k] - 2.5, '%d.ª línea' % (k + 1))
        for k in range(4):
            c.setFont('DejaVuSans', 7.0)
            c.setFillColor(AZUL)
            c.drawString(xs + ws + 62, ys[-1 - k] + g / 2 - 2.5, ['1.er', '2.º', '3.er', '4.º'][k] + ' espacio')
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(OCRE)
        c.drawString(xs, ys[-1] - 20, 'siempre de abajo arriba  ↑')
        # --- derecha: las siete notas
        xr = x + 300
        wr = w - 300
        top2 = y - 34
        ys2 = draw_staff(c, xr, top2, wr, g)
        bot2 = ys2[-1]
        draw_clef(c, xr + 4, bot2, g, 'treble')
        notas = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
        nm = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do']
        lt = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
        x0 = xr + 46
        paso = (wr - 52) / 8.0
        for k, p in enumerate(notas):
            cx = x0 + paso * (k + 0.5)
            draw_note(c, cx, bot2, ys2[0], g, p, dur='w', clef='treble')
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY)
            c.drawCentredString(cx, bot2 - 26, nm[k])
            c.setFont('DejaVuSans', 7.0)
            c.setFillColor(MUTED)
            c.drawCentredString(cx, bot2 - 36, lt[k])
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY)
        c.drawString(xr, y - 8, 'LAS SIETE NOTAS (DE DO A DO)')
        c.setFillColor(OCRE)
        c.setFont('DejaVuSans', 7.0)
        c.drawString(xr + 4, bot2 - 50, 'El primer Do, con su rayita, es el «Do central».')
    return Blk(h, f)


def diag_sol_clave():
    """La clave de sol: se enrolla en la 2.ª linea, que es Sol. La de fa: la 4.ª linea, Fa."""
    h = 100

    def f(c, x, y, w):
        g = 10.0
        xs = x + 4
        ys = draw_staff(c, xs, y - 34, 200, g)
        draw_clef(c, xs + 4, ys[-1], g, 'treble')
        c.setStrokeColor(OCRE)
        c.setLineWidth(2.2)
        c.line(xs + 52, ys[-2], xs + 200, ys[-2])
        draw_note(c, xs + 150, ys[-1], ys[0], g, 'G4', dur='w', clef='treble')
        c.setFont('DejaVuSans-Bold', 8.2)
        c.setFillColor(OCRE)
        c.drawString(xs + 60, ys[-2] + 3.6 - 14, '')
        c.drawCentredString(xs + 100, ys[-1] - 26, '2.ª línea = SOL')
        xb = x + 262
        yb = draw_staff(c, xb, y - 34, 200, g)
        draw_clef(c, xb + 4, yb[-1], g, 'bass')
        c.setStrokeColor(OCRE)
        c.setLineWidth(2.2)
        c.line(xb + 50, yb[1], xb + 200, yb[1])
        draw_note(c, xb + 150, yb[-1], yb[0], g, 'F3', dur='w', clef='bass')
        c.setFillColor(OCRE)
        c.setFont('DejaVuSans-Bold', 8.2)
        c.drawCentredString(xb + 100, yb[-1] - 26, '4.ª línea = FA')
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY)
        c.drawString(xs, y - 8, 'CLAVE DE SOL: LA ESPIRAL RODEA LA 2.ª LÍNEA')
        c.drawString(xb, y - 8, 'CLAVE DE FA: LA 4.ª LÍNEA, ENTRE SUS DOS PUNTOS')
    return Blk(h, f)


def trazar_claves():
    """Una pauta con claves de sol en gris para repasar con el lapiz."""
    g = 9.0
    h = 62

    def f(c, x, y, w):
        ys = draw_staff(c, x, y - 18, w, g)
        c.saveState()
        c.setFillAlpha(0.22)
        for k in range(8):
            draw_clef(c, x + 8 + k * 40, ys[-1], g, 'treble')
        c.restoreState()
        c.setStrokeColor(RULE)
        c.setDash(2, 3)
        c.line(x + 8 * 40 + 14, ys[0] + 8, x + 8 * 40 + 14, ys[-1] - 8)
        c.setDash()
    return Blk(h, f)


def diag_muro():
    """El 'muro de fracciones': cada fila es la figura de arriba partida en dos."""
    filas = ['w', 'h', 'q', 'e', 's', 'f', 'g']
    RH = 28
    h = len(filas) * RH + 24

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x + 14, y - 8, 'FIGURA')
        c.drawString(x + 74, y - 8, 'NOMBRE')
        c.drawString(x + 170, y - 8, 'EL MISMO ESPACIO, REPARTIDO EN PARTES IGUALES')
        bx0 = x + 170
        bw = w - 170
        yy = y - 16
        cols = [NAVY, AZUL, OCRE, VERDE, ROJO, MORADO_, NAVY_SOFT]
        for i, d in enumerate(filas):
            cy = yy - RH / 2.0
            fig_celda(d, gap=3.6)(c, x + 30, cy, 60, RH)
            c.setFont('DejaVuSans-Bold', 8.6)
            c.setFillColor(INK)
            c.drawString(x + 74, cy - 3, NOM_FIG[d])
            n = 2 ** i
            sw = bw / float(n)
            for k in range(n):
                c.setFillColor(cols[i])
                c.setStrokeColor(CREAM)
                c.setLineWidth(0.4 if n > 16 else 1.0)
                c.roundRect(bx0 + k * sw, cy - 9, sw, 18, 2 if n < 16 else 0.4, fill=1, stroke=1)
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSans-Bold', 8.0)
            txt = {'w': '4', 'h': '2', 'q': '1', 'e': '½', 's': '¼', 'f': '⅛', 'g': '1/16'}[d]
            if n <= 8:
                c.drawCentredString(bx0 + sw / 2, cy - 2.8, txt)
            else:
                c.drawString(bx0 + 2, cy - 2.8, txt)
            yy -= RH
        c.setFont('DejaVuSans', 7.0)
        c.setFillColor(MUTED)
        c.drawString(x + 170, y - h + 8, 'Los números son los tiempos que dura cada trozo (la negra = 1).')
    return Blk(h, f)


MORADO_ = HexColor('#6B5B95')


def diag_puntillo():
    h = 118

    def f(c, x, y, w):
        # blanca + negra = blanca con puntillo
        def barra(xx, yy, ancho, cols, textos):
            tot = sum(cols_w for cols_w, _ in cols)
            xo = xx
            for wv, (txt, colr) in zip([a for a, _ in cols], textos):
                ww = ancho * wv / float(tot)
                c.setFillColor(colr)
                c.setStrokeColor(CREAM)
                c.setLineWidth(1.0)
                c.roundRect(xo, yy, ww, 16, 2, fill=1, stroke=1)
                c.setFillColor(BLANCO)
                c.setFont('DejaVuSans-Bold', 8.2)
                c.drawCentredString(xo + ww / 2, yy + 5, txt)
                xo += ww
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 9, 'EL PUNTILLO SUMA LA MITAD')
        figura(c, x + 30, y - 46, 6.4, 'h', linea=False)
        c.setFont('DejaVuSans-Bold', 12)
        c.setFillColor(OCRE)
        c.drawString(x + 52, y - 50, '+')
        figura(c, x + 90, y - 46, 6.4, 'q', linea=False)
        c.drawString(x + 112, y - 50, '=')
        figura(c, x + 150, y - 46, 6.4, 'h', linea=False, dot=True)
        barra(x + 190, y - 50, w - 200, [(2, 0), (1, 0)], [('2', AZUL), ('+1', OCRE)])
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(INK)
        c.drawString(x + 190, y - 66, 'blanca con puntillo = 2 + 1 = 3 tiempos')
        figura(c, x + 30, y - 98, 6.4, 'q', linea=False)
        c.setFont('DejaVuSans-Bold', 12)
        c.setFillColor(OCRE)
        c.drawString(x + 52, y - 102, '+')
        figura(c, x + 90, y - 98, 6.4, 'e', linea=False)
        c.drawString(x + 112, y - 102, '=')
        figura(c, x + 150, y - 98, 6.4, 'q', linea=False, dot=True)
        barra(x + 190, y - 102, w - 200, [(2, 0), (1, 0)], [('1', AZUL), ('+½', OCRE)])
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(INK)
        c.drawString(x + 190, y - 118 + 0, 'negra con puntillo = 1 + ½ = 1 ½ tiempos')
    return Blk(h + 14, f)


def fig_celda(d, silencio_=False, dot=False, gap=3.7):
    """Celda de tabla con una figura (o su silencio), centrada vertical y horizontalmente."""
    def f(c, cx, cy, w, hh):
        if silencio_:
            silencio(c, cx, cy, gap * 1.15, d, linea=False)
        else:
            nf = FIG[d][0]
            alto = gap * (3.4 + 0.95 * max(0, nf - 2)) + gap * 0.5 if FIG[d][2] else gap
            figura(c, cx - gap * 0.6, cy - alto / 2.0 + gap * 0.5, gap, d, linea=False, dot=dot)
    return f


# ------------------------------------------------------------------ sopa de letras
def sopa(palabras, n=14, sem=7):
    r = rnd(sem)
    grid = [[None] * n for _ in range(n)]
    dirs = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1)]
    pos = {}
    for pal in sorted(palabras, key=len, reverse=True):
        for _ in range(400):
            dy, dx = r.choice(dirs)
            L = len(pal)
            y0 = r.randrange(n)
            x0 = r.randrange(n)
            y1, x1 = y0 + dy * (L - 1), x0 + dx * (L - 1)
            if not (0 <= y1 < n and 0 <= x1 < n):
                continue
            ok = all(grid[y0 + dy * k][x0 + dx * k] in (None, pal[k]) for k in range(L))
            if not ok:
                continue
            for k in range(L):
                grid[y0 + dy * k][x0 + dx * k] = pal[k]
            pos[pal] = (y0, x0, dy, dx)
            break
        else:
            raise RuntimeError('no cabe ' + pal)
    pool = ''.join(palabras)
    for yy in range(n):
        for xx in range(n):
            if grid[yy][xx] is None:
                grid[yy][xx] = r.choice(pool)
    return grid, pos


PALABRAS = [
    ('PENTAGRAMA', 'Las cinco líneas y cuatro espacios donde se escribe la música.'),
    ('CLAVE', 'Signo del principio que dice qué nota es cada línea.'),
    ('REDONDA', 'La figura que dura cuatro tiempos.'),
    ('BLANCA', 'Dura dos tiempos; tiene la cabeza vacía y plica.'),
    ('NEGRA', 'La figura que suele marcar el pulso: dura un tiempo.'),
    ('CORCHEA', 'Dura medio tiempo: dos caben en una negra.'),
    ('SEMICORCHEA', 'Dura un cuarto de tiempo y lleva dos corchetes.'),
    ('SILENCIO', 'Signo que indica que no suena nada, con su duración.'),
    ('PLICA', 'La rayita vertical que sale de la cabeza de la nota.'),
    ('PUNTILLO', 'El punto que alarga una figura la mitad de su valor.'),
]


def bloque_sopa(grid, n=14):
    cell = 21.0
    h = n * cell + 6

    def f(c, x, y, w):
        x0 = x + (w - n * cell) / 2.0
        c.setFillColor(BLANCO)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.0)
        c.roundRect(x0 - 4, y - n * cell - 4, n * cell + 8, n * cell + 8, 4, fill=1, stroke=1)
        c.setFont('DejaVuSans-Bold', 11.5)
        c.setFillColor(INK)
        for r_ in range(n):
            for k in range(n):
                c.drawCentredString(x0 + k * cell + cell / 2, y - r_ * cell - cell + 6.4, grid[r_][k])
    return Blk(h + 6, f)


# ------------------------------------------------------------------ contenido
def construir(d):
    d.nuevo('Septiembre · Notación musical y figuras')
    d.add(banda_mes('Septiembre', '1.er trimestre', 'Notación musical y figuras',
                    'El pentagrama, la clave, las siete notas, las figuras y los silencios: el alfabeto de la música escrita.'))
    d.add(
        caja('dato', 'El pentagrama y la clave de sol', [
            'La música se escribe sobre un **pentagrama**: cinco líneas y cuatro espacios que se cuentan **de abajo arriba**. '
            'Cada línea y cada espacio es una altura distinta: cuanto más arriba está la nota, **más aguda** suena.',
            'Para saber qué nota es cada una hace falta un punto de partida: la **clave**. La **clave de sol** se enrolla en la '
            '**2.ª línea**, y esa línea es **Sol**. A partir de ahí, líneas y espacios van tomando las notas en orden: '
            '**Do – Re – Mi – Fa – Sol – La – Si**, y vuelve a empezar.',
            'Con la **clave de fa**, que se coloca en la 4.ª línea, se escriben las notas graves (normalmente la mano izquierda). '
            'Este mes y el siguiente trabajamos con la clave de sol.']),
        diag_pentagrama(),
        diag_sol_clave())
    d.add(caja('nota', 'Las notas tienen dos nombres', [
        'En los países de habla inglesa (y en muchas partituras de pop) las notas se escriben con letras: '
        '**C = Do · D = Re · E = Mi · F = Fa · G = Sol · A = La · B = Si**. Merece la pena aprenderlo ya: '
        'lo verás en cifrados y en partituras de internet.']))

    # ---- Ejercicio 1
    d.add(ejercicio(1, 'Practicando la clave de sol',
                    ['Repasa con lápiz las claves de sol en gris y haz después las tuyas. Empieza por abajo, en la 2.ª línea, '
                     'y sube enrollando la espiral.',
                     'Dibuja las notas que faltan. La primera ya está puesta: sube o baja por orden, una línea o un espacio cada vez.'],
                    'Que la mano aprenda a hacer la clave sin pensarlo y que la vista aprenda dónde vive cada nota.'),
          trazar_claves(),
          pauta_vacia('treble', 1, None, titulo='Tus claves', alto_extra=0))
    ej1 = [
        ('Sube desde Sol', ['G4', None, None, None, None, None, None, None], ['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], 'G4'),
        ('Sube desde Mi', ['E4', None, None, None, None, None, None, None], ['Mi', 'Fa', 'Sol', 'La', 'Si', 'Do', 'Re', 'Mi'], 'E4'),
        ('Baja desde Fa', ['F5', None, None, None, None, None, None, None], ['Fa', 'Mi', 'Re', 'Do', 'Si', 'La', 'Sol', 'Fa'], 'F5'),
    ]
    sec = ['a', 'b', 'c']
    seq_sol = []
    for k, (tit, notas, nms, ini) in enumerate(ej1):
        d.add(fila_notas('treble', notas, 'w', bajo=nms, titulo='%s) %s' % (sec[k], tit)))
        # colocar las notas segun la secuencia de alturas
        idx = _abs_idx(ini)
        up = tit.startswith('Sube')
        ps = []
        letras = 'CDEFGAB'
        for j in range(8):
            ii = idx + j if up else idx - j
            ps.append(letras[ii % 7] + str(ii // 7))
        seq_sol.append('%s) %s' % (sec[k], ' · '.join('%s (%s)' % (nombre(p), posicion(p)) for p in ps)))
    sol(MES, 1, 'Practicando la clave de sol', seq_sol)

    # ---- Ejercicio 2: nombres
    d.add(ejercicio(2, 'Practicando las notas musicales',
                    ['Escribe el nombre de cada nota sobre su raya: Do, Re, Mi, Fa, Sol, La o Si.',
                     'Repite cada fila hasta que puedas decir los nombres de seguido, sin parar a pensar.'],
                    'Reconocer las notas por su posición, sin recitar el alfabeto desde abajo cada vez.'),
          caja('tip', 'Dos listas que ahorran tiempo',
               ['**Líneas** (de abajo arriba, clave de sol): **Mi – Sol – Si – Re – Fa**.   '
                '**Espacios**: **Fa – La – Do – Mi**.',
                'Los espacios, leídos de abajo arriba, forman en inglés la palabra FACE (F-A-C-E). Una nota que no sepas: '
                'cuenta desde la más cercana de estas.']))
    r = rnd(11)
    pool_a = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
    filas2 = []

    def sorteo(pool, n, ant=None):
        out = []
        while len(out) < n:
            p = r.choice(pool)
            if out and p == out[-1]:
                continue
            if out and abs(_abs_idx(p) - _abs_idx(out[-1])) > 5:
                continue
            out.append(p)
        return out
    sol2 = []
    for k, (tit, pool) in enumerate([('Dentro del pentagrama', pool_a), ('Más notas', pool_a + ['C4', 'D4']),
                                     ('Para terminar', pool_a)]):
        ps = sorteo(pool, 8)
        d.add(fila_notas('treble', ps, 'q', bajo='linea', barras=4, titulo='%s) %s' % (sec[k], tit)))
        sol2.append('%s) %s' % (sec[k], ' · '.join(nombre(p) for p in ps)))
    sol(MES, 2, 'Practicando las notas musicales', sol2)

    # ---- Figuras
    d.add(caja('dato', 'Las figuras: cada una vale la mitad de la anterior', [
        'Las **figuras** dicen **cuánto dura** cada sonido. Su duración es siempre relativa: se mide en **tiempos** '
        '(los pulsos de la música), y por costumbre se toma la **negra** como un tiempo.',
        'La regla es muy simple: cada figura **dura la mitad que la anterior**. Una redonda cabe 2 veces en… ella misma, '
        'dos blancas, cuatro negras, ocho corcheas… Mira cómo se reparte el mismo espacio:']),
        diag_muro(),
        par('Fíjate en cómo cambia el dibujo: la **cabeza vacía** es de redonda y blanca; la **cabeza llena**, de negra para abajo. '
            'La **plica** (la rayita) aparece desde la blanca; a partir de la corchea se añaden **corchetes** (uno por cada mitad más): '
            '1 la corchea, 2 la semicorchea, 3 la fusa, 4 la semifusa. Cuando van seguidas, los corchetes se unen en **barras**.', 9.2))
    d.add(ejercicio(3, 'Relaciona las figuras con sus nombres y sus tiempos',
                    ['Completa la tabla: en cada fila falta un dato (la figura, el nombre o los tiempos). Solo uno.',
                     'Después contesta las sumas en la parte de abajo.'],
                    'Que ver una figura signifique, sin traducir, «dura tanto».'))
    cols = ['w', 'h', 'q', 'e', 's', 'f', 'g']
    filas = []
    sol3 = []
    for i, dd in enumerate(cols):
        falta = i % 3
        cel_fig = fig_celda(dd) if falta != 0 else ''
        cel_nom = NOM_FIG[dd] if falta != 1 else ''
        cel_t = FIG[dd][4] if falta != 2 else ''
        filas.append([cel_fig, cel_nom, cel_t])
        sol3.append('%s → %s, %s' % (NOM_FIG[dd], 'dibuja la figura' if falta == 0 else ('escribe el nombre' if falta == 1
                                                                                       else 'escribe «' + FIG[dd][4] + '»'), ''))
    sol3 = ['%s (%s)%s' % (NOM_FIG[dd], FIG[dd][4], ' — falta la FIGURA' if i % 3 == 0 else (' — falta el NOMBRE' if i % 3 == 1 else ' — faltan los TIEMPOS'))
            for i, dd in enumerate(cols)]
    d.add(tabla([100, 150, 150], filas, ['Figura', 'Nombre', 'Tiempos'], alto=32))
    sol(MES, 3, 'Relaciona las figuras', sol3)
    d.add(h2('Sumas de figuras'))
    sumas = [
        ('1 blanca = ___ negras', '2'),
        ('1 redonda = ___ blancas', '2'),
        ('1 negra = ___ corcheas', '2'),
        ('1 corchea = ___ semicorcheas', '2'),
        ('1 redonda = ___ corcheas', '8'),
        ('2 negras + 1 blanca = ___ tiempos', '4'),
        ('1 blanca + 1 negra + 2 corcheas = ___ tiempos', '4'),
        ('4 semicorcheas + 1 negra = ___ tiempos', '2'),
    ]
    d.add(lista([t for t, _ in sumas], marca='▸', size=9.8, sep=6))
    sol(MES, '3 (sumas)', 'Sumas de figuras', ['  ·  '.join('%d) %s' % (k + 1, r_) for k, (_, r_) in enumerate(sumas))])

    # ---- Puntillo
    d.add(caja('tip', 'El puntillo', [
        'Un **punto a la derecha** de una figura la **alarga la mitad de lo que vale**. Así se consiguen duraciones '
        'que no existen como figura suelta: una blanca con puntillo dura 3 tiempos (2 + 1), una negra con puntillo, '
        '1 tiempo y medio (1 + ½).',
        'Al leer una partitura, fíjate siempre en los puntillos: modifican la duración y por tanto el ritmo.']),
        diag_puntillo())
    d.add(tabla([120, 90, 120, 130], [
        [fig_celda('w'), 'redonda: 4', '+ 2', '= 6 tiempos'],
        [fig_celda('h'), 'blanca: 2', '+ 1', '= 3 tiempos'],
        [fig_celda('q'), 'negra: 1', '+ ½', '= 1 ½ tiempos'],
        [fig_celda('e'), 'corchea: ½', '+ ¼', '= ¾ de tiempo'],
        [fig_celda('s'), 'semicorchea: ¼', '+ ⅛', '= ⅜ de tiempo'],
    ], ['Figura', 'Vale', 'El punto suma', 'Con puntillo'], alto=30))
    d.add(ejercicio(4, 'Calcula con puntillo',
                    ['Completa. Recuerda: el punto suma la mitad de lo que vale la figura.'], None))
    d.add(lista(['Una blanca con puntillo dura ___ tiempos.', 'Una negra con puntillo dura ___ tiempos.',
                 'Una redonda con puntillo dura ___ tiempos.',
                 'Una negra con puntillo + una corchea = ___ tiempos.',
                 'Una blanca con puntillo + una negra = ___ tiempos.'], marca='▸', size=9.8, sep=6))
    sol(MES, 4, 'Calcula con puntillo', ['1) 3  ·  2) 1 ½  ·  3) 6  ·  4) 2  ·  5) 4'])

    # ---- Silencios
    d.add(caja('dato', 'Los silencios: también se cuentan', [
        'Cuando una nota no suena, la música **no se detiene**: el silencio dura exactamente lo que dura la figura de su mismo nombre. '
        'Hay un silencio para cada figura, y se cuentan igual.',
        'Dos trucos para no confundirlos: el de **redonda cuelga** de la 4.ª línea («un sombrero colgando») y el de **blanca se '
        'apoya** sobre la 3.ª («un sombrero sobre la mesa»). Los dos son una pequeña caja negra.',
        '**Todo silencio vale lo mismo que su figura**: si sabes cuánto dura la negra, sabes cuánto dura su silencio.']))
    sil = []
    for dd in cols:
        sil.append([fig_celda(dd, True), NOM_SIL[dd], FIG[dd][4], fig_celda(dd)])
    d.add(tabla([100, 190, 105, 85], sil, ['Silencio', 'Nombre', 'Dura', 'Como la figura'], alto=32))
    d.add(ejercicio(5, 'Relaciona los silencios con sus nombres y tiempos',
                    ['Une cada silencio con su nombre con una línea.',
                     'A su derecha, escribe cuántos tiempos dura.'],
                    'Reconocer los silencios a primera vista, como una nota más.'))
    orden = ['q', 'w', 'e', 'h', 's', 'f', 'g']
    r2 = rnd(5)
    nombres_r = [NOM_SIL[x] for x in orden]
    r2.shuffle(nombres_r)
    d.add(une([fig_celda(x, True) for x in orden], nombres_r, alto=32, izq_w=80, der_w=190, hueco=70, sufijo='tiempos'))
    sol(MES, 5, 'Relaciona los silencios', ['  ·  '.join('%s → %s (%s)' % (['1.º', '2.º', '3.º', '4.º', '5.º', '6.º', '7.º'][k], NOM_SIL[x], FIG[x][4]) for k, x in enumerate(orden))])

    # ---- Plicas
    d.add(caja('dato', 'Cómo se colocan las plicas', [
        'La **plica** es la rayita que sale de la cabeza. La regla depende de dónde esté la nota:',
        '▸ **Por debajo de la línea central (la 3.ª, Si)**: la plica sube y va a la **derecha** de la cabeza.',
        '▸ **Por encima de la línea central**: la plica baja y va a la **izquierda**.',
        '▸ **En la línea central (Si)**: puede ir en cualquier sentido; se elige el que deje la música más clara.',
        'La plica mide, más o menos, **una octava** (tres espacios y medio). Las notas de redonda no llevan plica.']))
    d.add(fila_notas('treble', ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'], 'q', bajo='nada',
                     titulo='Así queda escrita una escala sencilla: las plicas cambian de lado al pasar la 3.ª línea'))
    d.add(ejercicio(6, 'Coloca las plicas',
                    ['Cada nota es una **negra** sin plica. Dibújale la plica: hacia arriba (a la derecha) o hacia abajo (a la izquierda).',
                     'Si la nota está en la línea central, elige tú el lado.'],
                    'Escribir música a mano de forma que se lea limpia.'))
    r = rnd(23)
    sol5 = []
    for k in range(3):
        ps = sorteo(pool_a, 8)
        d.add(fila_notas('treble', ps, 'q', bajo='nada', cabeza_sola=True, barras=4, titulo='%s)' % sec[k]))
        sol5.append('%s) %s' % (sec[k], ' · '.join(('↑' if _abs_idx(p) < _abs_idx('B4') else ('↓' if _abs_idx(p) > _abs_idx('B4') else '↑↓')) + nombre(p) for p in ps)))
    sol(MES, 6, 'Coloca las plicas', sol5 + ['↑ = plica hacia arriba · ↓ = hacia abajo · ↑↓ = cualquiera de las dos (nota en la línea central).'])

    # ---- Sopa
    d.add(ejercicio(7, 'Sopa de letras musical',
                    ['Cada pista de abajo define una palabra escondida. Encuéntrala en la sopa (puede ir en cualquier dirección: '
                     '→ ← ↓ ↑ ↘ ↗) y rodéala.',
                     'Primero adivina la palabra y después búscala: si no la sabes aún, mira las figuras de este mes.'],
                    'Que los términos del mes se queden en la memoria y se asocien a una idea, no a una lista.'))
    pal = [p for p, _ in PALABRAS]
    grid, pos = sopa(pal, 14, 41)
    d.add(bloque_sopa(grid, 14))
    d.add(lista(['%s' % t for _, t in PALABRAS], marca='▸', size=9.2, sep=3))
    sol6 = []
    for p in pal:
        y0, x0, dy, dx = pos[p]
        di = {(0, 1): '→', (1, 0): '↓', (1, 1): '↘', (0, -1): '←', (-1, 0): '↑', (1, -1): '↙'}[(dy, dx)]
        sol6.append('%s (fila %d, columna %d, %s)' % (p, y0 + 1, x0 + 1, di))
    sol(MES, 7, 'Sopa de letras', ['  ·  '.join(sol6)])

    # ---- En palmas
    d.add(caja('piano', 'Ritmo en palmas', [
        'Antes de tocar, **el ritmo se aprende con el cuerpo**. Lee cada línea marcando el pulso con el pie (o dando '
        'golpes suaves con la mano en la pierna) y **di en voz alta**: negra = **ta**, dos corcheas = **ti-ti**, blanca = **ta-a**, '
        'redonda = **ta-a-a-a**. En los silencios, abre las manos y **no digas nada**, pero sigue contando.',
        'Empieza despacio (unos 60 pulsos por minuto, más o menos un golpe por segundo) y no pares aunque te equivoques: '
        'la música sigue.']))
    ritmos = [
        ('a) Negras, blancas y redonda', [[('n', 'q'), ('n', 'q'), ('n', 'q'), ('n', 'q')], [('n', 'h'), ('n', 'q'), ('n', 'q')],
                                          [('n', 'q'), ('n', 'q'), ('n', 'h')], [('n', 'w')]]),
        ('b) Con silencios de negra y de blanca', [[('n', 'q'), ('n', 'q'), ('n', 'q'), ('r', 'q')], [('n', 'h'), ('r', 'h')],
                                                    [('n', 'q'), ('r', 'q'), ('n', 'q'), ('r', 'q')], [('n', 'h'), ('n', 'q'), ('r', 'q')]]),
        ('c) Con corcheas: «ti-ti»', [[('n', 'e'), ('n', 'e'), ('n', 'q'), ('n', 'e'), ('n', 'e'), ('n', 'q')],
                                      [('n', 'q'), ('n', 'e'), ('n', 'e'), ('n', 'q'), ('n', 'q')],
                                      [('n', 'e'), ('n', 'e'), ('n', 'e'), ('n', 'e'), ('n', 'h')], [('n', 'q'), ('n', 'q'), ('n', 'h')]]),
        ('d) Con puntillo', [[('n', 'h.'), ('n', 'q')], [('n', 'q.'), ('n', 'e'), ('n', 'h')],
                              [('n', 'q'), ('n', 'q'), ('n', 'q.'), ('n', 'e')], [('n', 'h'), ('n', 'h')]]),
    ]
    for tit, comp in ritmos:
        d.add(fila_compases(comp, ts=(4, 4), titulo=tit))
    d.add(par('**Reto:** repite cada línea con los ojos cerrados al segundo intento. Si te la sabes de memoria, '
              'puedes pasar a la siguiente.', 9.2, NAVY_SOFT))
    sol(MES, 'En palmas', 'Ritmo en palmas',
        ['Todos los compases suman 4 tiempos (4/4). En la línea d), blanca con puntillo + negra = 3 + 1; '
         'negra con puntillo + corchea = 1 ½ + ½ (los dos primeros tiempos).'])
