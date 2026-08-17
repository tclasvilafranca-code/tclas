# -*- coding: utf-8 -*-
"""Hoja de DEBERES ESCRITOS, para hacer en casa. Una por semana.

   Pedido por el cliente para Arnau (10 anos, media hora de clase): que cada
   semana se lleve una hoja de deberes YA ESCRITOS, con ejercicios de verdad
   adaptados a su nivel, en vez de un recuadro en blanco para que la profesora
   apunte tareas. Con media hora de clase no hay tiempo de inventar deberes al
   final; y con diez anos, unos deberes escritos se hacen y unos deberes
   dictados se olvidan.

   Como se compone
   ---------------
   Igual que `hoja_piano`: la hoja recibe una lista de `bloques` y cada bloque
   es un ejercicio de un tipo. Los tipos son estos, y todos salen de la
   cancion que toca esa semana (las notas son las suyas, no notas al azar):

     nombres   escribe debajo como se llama cada nota
     dibuja    al reves: le doy el nombre y dibuja la nota en su sitio
     figuras   cuantos tiempos vale cada figura
     rodea     rodea los compases que son iguales (los busca en su partitura)
     colorea   colorea cada figura de un color
     une       une con una raya cada dibujo con su nombre
     rutina    la tabla de que tocar cada dia de la semana
     escucha   un juego para hacer con un adulto, sin partitura
     escribe   dos pentagramas vacios para copiar o inventar
     nota      un recuadro con una explicacion corta

   Y los de JUGAR, que son los que hacen que la hoja se haga (norma de
   variedad del cliente: dos semanas seguidas no pueden llevar la misma
   estructura, y ningun tipo puede salir en mas del 60% de las hojas):

     sopa        sopa de letras con palabras de la cancion de esa semana
     adivina     adivinanzas, con las letras de la respuesta en cajitas
     crucigrama  acrostico: una palabra vertical y las demas cruzandola
     camino      colorea solo las casillas que cumplen la regla y sale un camino
     vf          verdadero o falso
     ordena      los pasos desordenados, y hay que numerarlos
     diferencias dos pentagramas casi iguales: encuentra las diferencias
     cuenta      cuantas veces aparece cada cosa en un pentagrama
     teclado     un teclado dibujado para marcar o nombrar teclas
     palmas      escribe el ritmo de una palabra con figuras
     inventa     dos compases propios, pero con condiciones

   Todo el texto va SIN TECNICISMOS: "la nota que esta en la primera linea",
   no "el Mi del primer espacio del pentagrama en clave de sol". Cuando hace
   falta una palabra tecnica se explica ahi mismo, en la misma frase.
"""
import random
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import (draw_staff, draw_clef, draw_barline, draw_note, draw_chord,
                      draw_notehead, draw_ledger, ledger_lines_needed, note_y,
                      draw_time_sig)
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)
from ficha_info import BLACK_AFTER

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')

GAP = 8.2           # pentagrama grande: esto se escribe a mano
SUELO = 46


# --------------------------------------------------------------------------
# piezas sueltas
# --------------------------------------------------------------------------
def _cabecera(c, cfg):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, cfg['kicker'].upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, cfg.get('esquina', 'Deberes · para hacer en casa'))
    y -= 27

    c.setFont('DejaVuSerif-Bold', 23)
    c.setFillColor(NAVY)
    titulo = cfg.get('titulo', 'Deberes de esta semana')
    c.drawString(MARGIN, y, titulo)
    y -= 14
    y = _wrap(c, cfg.get('intro', ''), MARGIN, y, 'DejaVuSans', 8.8,
              CONTENT_W, 11.0, MUTED)
    y -= 6

    # la linea de nombre y fecha: es una hoja que sale de casa y vuelve
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.setFont('DejaVuSans-Bold', 8.0)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y - 12, 'NOMBRE')
    c.line(MARGIN + 48, y - 14, MARGIN + CONTENT_W * 0.58, y - 14)
    c.drawString(MARGIN + CONTENT_W * 0.63, y - 12, 'FECHA')
    c.line(MARGIN + CONTENT_W * 0.63 + 40, y - 14, W - MARGIN, y - 14)
    return y - 30


def _titulo_ej(c, y, num, titulo, pista):
    """El encabezado de cada ejercicio. Con numero si lo lleva; la tabla de
       la semana no es un ejercicio, asi que va sin casilla."""
    x = MARGIN
    if num:
        c.setFillColor(ACCENT)
        c.roundRect(MARGIN, y - 14, 15, 15, 3, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 9.0)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 7.5, y - 10.6, str(num))
        x = MARGIN + 22
    else:
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 4, y - 6.5, 3.4, fill=1, stroke=0)
        x = MARGIN + 14

    c.setFont('DejaVuSans-Bold', 10.2)
    c.setFillColor(NAVY)
    c.drawString(x, y - 11, titulo)
    tw = stringWidth(titulo, 'DejaVuSans-Bold', 10.2) + (x - MARGIN)
    if pista:
        size = _fit(pista, 'DejaVuSans', 8.0, CONTENT_W - tw - 16, floor=6.2)
        c.setFont('DejaVuSans', size)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + tw + 12, y - 10.6, pista)
    return y - 22


def _pauta(c, y, gap, clef=None, key_sig=None, ancho=None):
    """Un pentagrama solo, con o sin clave. Devuelve (top, bot)."""
    ancho = ancho if ancho is not None else CONTENT_W
    ys = draw_staff(c, MARGIN, y, ancho, gap=gap)
    top, bot = ys[0], ys[-1]
    if clef:
        draw_clef(c, MARGIN + 4, bot, gap, clef=clef)
    return top, bot


def _huecos(c, x, bot, gap, n, paso, ancho=None):
    """Las cajitas donde el alumno escribe el nombre de la nota."""
    ancho = ancho or paso * 0.72
    for i in range(n):
        cx = x + i * paso
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.setFillColor(white)
        c.roundRect(cx - ancho / 2, bot - gap * 3.5, ancho, gap * 1.7, 2, fill=1, stroke=1)


# --------------------------------------------------------------------------
# los ejercicios
# --------------------------------------------------------------------------
def ej_nombres(c, y, b):
    """Notas dibujadas; el alumno escribe el nombre debajo de cada una."""
    y = _titulo_ej(c, y, b['num'], b['titulo'],
                   b.get('pista', 'escribe debajo de cada nota cómo se llama'))
    gap = b.get('gap', GAP)
    clef = b.get('clef', 'treble')
    pitches = b['notas']
    y -= gap * 1.2
    top, bot = _pauta(c, y, gap, clef=clef)
    x0 = MARGIN + gap * 7.2
    paso = (CONTENT_W - gap * 9.0) / max(1, len(pitches) - 1)
    for i, p in enumerate(pitches):
        draw_note(c, x0 + i * paso, bot, top, gap, p, dur='q', clef=clef)
    _huecos(c, x0, bot, gap, len(pitches), paso)
    return bot - gap * 5.6


def ej_dibuja(c, y, b):
    """Al reves: el nombre esta escrito y el alumno dibuja la nota."""
    y = _titulo_ej(c, y, b['num'], b['titulo'],
                   b.get('pista', 'dibuja tú la nota: solo el óvalo, sin el palito'))
    gap = b.get('gap', GAP)
    clef = b.get('clef', 'treble')
    nombres = b['nombres']
    y -= gap * 1.2
    top, bot = _pauta(c, y, gap, clef=clef)
    x0 = MARGIN + gap * 7.2
    paso = (CONTENT_W - gap * 9.0) / max(1, len(nombres) - 1)
    for i, nm in enumerate(nombres):
        c.setFont('DejaVuSans-Bold', gap * 0.95)
        c.setFillColor(ACCENT)
        c.drawCentredString(x0 + i * paso, bot - gap * 2.9, nm)
    return bot - gap * 4.8


def ej_figuras(c, y, b):
    """Cuantos tiempos vale cada figura. Se dibujan de verdad, no con letras."""
    y = _titulo_ej(c, y, b['num'], b['titulo'],
                   b.get('pista', 'escribe en la caja cuántos tiempos dura cada una'))
    gap = b.get('gap', 9.0)
    items = b['figuras']          # [(dur, etiqueta), ...]
    n = len(items)
    ancho = CONTENT_W / n
    # la plica de una negra sube 3,5 espacios desde la cabeza: sin este aire
    # el palito se mete dentro del titulo del ejercicio
    base = y - gap * 4.6
    for i, (dur, etiqueta) in enumerate(items):
        cx = MARGIN + ancho * (i + 0.5)
        # la figura, dibujada sobre un pentagrama invisible
        draw_note(c, cx, base, base + gap * 4, gap, 'B4', dur=dur, clef='treble')
        c.setFont('DejaVuSans', 7.8)
        c.setFillColor(MUTED)
        c.drawCentredString(cx, base - gap * 2.3, etiqueta)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.setFillColor(white)
        c.roundRect(cx - 15, base - gap * 4.6, 30, 17, 2, fill=1, stroke=1)
    return base - gap * 5.6


def ej_une(c, y, b):
    """Dos columnas para unir con una raya."""
    y = _titulo_ej(c, y, b['num'], b['titulo'],
                   b.get('pista', 'une con una raya cada cosa de la izquierda con la de la derecha'))
    pares = b['pares']            # [(izquierda, derecha_desordenada), ...]
    izq = [p[0] for p in pares]
    der = b.get('derecha') or [p[1] for p in pares]
    paso = 19.0
    yy = y - 6
    # las dos columnas son de ancho fijo y su texto no envuelve, asi que hay
    # que encogerlo: una frase de mas se salia del margen derecho sin avisar
    x_der = MARGIN + CONTENT_W * 0.62
    ancho_izq = CONTENT_W * 0.42 - 20
    ancho_der = W - MARGIN - x_der
    for i in range(len(izq)):
        c.setFont('DejaVuSans-Bold', _fit(izq[i], 'DejaVuSans-Bold', 8.6, ancho_izq, floor=6.4))
        c.setFillColor(NAVY)
        c.drawString(MARGIN + 14, yy - 9, izq[i])
        c.setFillColor(ACCENT)
        c.circle(MARGIN + CONTENT_W * 0.42, yy - 6, 2.4, fill=1, stroke=0)
        c.circle(MARGIN + CONTENT_W * 0.58, yy - 6, 2.4, fill=1, stroke=0)
        c.setFont('DejaVuSans', _fit(der[i], 'DejaVuSans', 8.6, ancho_der, floor=6.4))
        c.setFillColor(INK)
        c.drawString(x_der, yy - 9, der[i])
        yy -= paso
    return yy - 4


def ej_rodea(c, y, b):
    """Un pentagrama con varios compases; hay que rodear los que se repiten."""
    y = _titulo_ej(c, y, b['num'], b['titulo'],
                   b.get('pista', 'rodea con lápiz los dos compases que son iguales'))
    gap = b.get('gap', b.get('gap_rodea', 7.6))
    clef = b.get('clef', 'treble')
    compases = b['compases']      # [[eventos], [eventos], ...]
    y -= gap * 2.6                # sitio para el numero de compas, que va ARRIBA
    top, bot = _pauta(c, y, gap, clef=clef)
    x0 = MARGIN + gap * 6.6
    ancho = (CONTENT_W - gap * 7.4) / len(compases)
    for i, comp in enumerate(compases):
        bx = x0 + i * ancho
        if i:
            draw_barline(c, bx - 4, top, bot)
        paso = (ancho - 12) / max(1, len(comp))
        for j, ev in enumerate(comp):
            cx = bx + 8 + j * paso
            if ev.get('pitches'):
                draw_chord(c, cx, bot, top, gap, ev['pitches'],
                           dur=ev.get('dur', 'q'), clef=clef)
            else:
                draw_note(c, cx, bot, top, gap, ev['pitch'],
                          dur=ev.get('dur', 'q'), clef=clef)
        # el numero del compas, encima del pentagrama: debajo se choca con las
        # notas que bajan de la primera linea y con sus lineas adicionales
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(MUTED)
        c.drawString(bx, top + gap * 1.1, str(i + 1))
    draw_barline(c, MARGIN + CONTENT_W, top, bot, final=True)
    return bot - gap * 3.4


def ej_colorea(c, y, b):
    """Notas de distintas figuras para colorear cada una de un color."""
    y = _titulo_ej(c, y, b['num'], b['titulo'], b.get('pista'))
    gap = b.get('gap', GAP)
    clef = b.get('clef', 'treble')
    eventos = b['eventos']
    y -= gap * 1.2
    top, bot = _pauta(c, y, gap, clef=clef)
    x0 = MARGIN + gap * 7.2
    paso = (CONTENT_W - gap * 9.0) / max(1, len(eventos) - 1)
    for i, ev in enumerate(eventos):
        draw_note(c, x0 + i * paso, bot, top, gap, ev['pitch'],
                  dur=ev.get('dur', 'q'), clef=clef)
    yy = bot - gap * 3.0
    for etiqueta in b.get('leyenda', []):
        c.setFont('DejaVuSans', 8.2)
        c.setFillColor(INK)
        c.drawString(MARGIN + 12, yy, '·  ' + etiqueta)
        yy -= 12
    return yy - 4


def rutina(c, y, b):
    """La tabla de la semana: que tocar cada dia, con casillas."""
    y = _titulo_ej(c, y, b.get('num', 0), b.get('titulo', 'Lo que hay que tocar cada día'),
                   b.get('pista', 'pon una cruz cuando lo hagas · con cinco días basta'))
    dias = b.get('dias', ['L', 'M', 'X', 'J', 'V'])
    tareas = b['tareas']
    col = 21.0
    x_tab = MARGIN + CONTENT_W - col * len(dias) - 4
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY_SOFT)
    for i, d in enumerate(dias):
        c.drawCentredString(x_tab + col * (i + 0.5), y - 8, d)
    yy = y - 20
    for t in tareas:
        size = _fit(t, 'DejaVuSans', 8.6, x_tab - MARGIN - 22, floor=6.6)
        c.setFont('DejaVuSans', size)
        c.setFillColor(INK)
        c.drawString(MARGIN + 12, yy - 9, t)
        for i in range(len(dias)):
            c.setStrokeColor(RULE)
            c.setLineWidth(0.8)
            c.setFillColor(white)
            c.rect(x_tab + col * i + 4, yy - 12, 13, 13, fill=1, stroke=1)
        yy -= 19
    return yy - 2


def _lineas_que_ocupa(texto, size, ancho):
    """Cuantas lineas va a escribir _wrap con ese ancho. Sirve para que un
       recuadro mida lo que mide su texto y no una altura fija: con una altura
       fija, un texto corto deja un hueco vacio que parece un fallo (y uno
       largo se sale)."""
    linea, n = '', 1
    for palabra in texto.split():
        prueba = (linea + ' ' + palabra).strip()
        if stringWidth(prueba, 'DejaVuSans', size) > ancho:
            n += 1
            linea = palabra
        else:
            linea = prueba
    return n


def ej_escucha(c, y, b):
    """El juego con un adulto. No hace falta que sepa musica."""
    h = b.get('alto') or 27 + 11.0 * _lineas_que_ocupa(b['texto'], 8.4, CONTENT_W - 28)
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9.0)
    c.setFillColor(ACCENT)
    tit = b.get('titulo', 'UN JUEGO, CON ALGUIEN DE CASA')
    c.drawString(MARGIN + 14, y - 16, tit)
    tw = stringWidth(tit, 'DejaVuSans-Bold', 9.0)
    sub = b.get('pista', 'no hace falta que sepa música')
    c.setFont('DejaVuSans', 7.8)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 14 + tw + 10, y - 16, sub)
    _wrap(c, b['texto'], MARGIN + 14, y - 29, 'DejaVuSans', 8.4,
          CONTENT_W - 28, 11.0, INK)
    return y - h - 10


def nota(c, y, b):
    """Un recuadro con una explicacion corta."""
    texto = b['texto']
    size = 8.4
    inner = CONTENT_W - 26
    h = 20 + 11.0 * _lineas_que_ocupa(texto, size, inner)
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(BLUE)
    c.drawString(MARGIN + 14, y - 14, b.get('etiqueta', 'ACUÉRDATE'))
    _wrap(c, texto, MARGIN + 14, y - 26, 'DejaVuSans', size, inner, 11.0, INK)
    return y - h - 10


def ej_escribe(c, y, b):
    """Pentagramas vacios al final: para copiar un compas o inventar."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Para escribir'),
                   b.get('pista', 'la clave la pones tú'))
    gap = b.get('gap', 8.6)
    n = b.get('lineas', 2)
    paso = gap * 7.2
    for _ in range(n):
        y -= gap * 1.4
        draw_staff(c, MARGIN, y, CONTENT_W, gap=gap)
        y -= paso - gap * 1.4
    return y


# --------------------------------------------------------------------------
# los ejercicios de JUGAR
#
# Son los que pidio el cliente al ver que las 40 hojas de Arnau tenian todas
# la misma forma. Cada uno se dibuja con las primitivas que ya hay, y todos
# sacan su contenido de la cancion de esa semana: las palabras de la sopa son
# las palabras de la pieza, las diferencias son compases suyos, y las
# adivinanzas preguntan por lo que esa cancion trae de nuevo.
# --------------------------------------------------------------------------
_ALFABETO = 'ABCDEFGHILMNOPRSTUV'      # sin K, sin W, sin X: no salen en las palabras


def _caja_letra(c, x, y, lado, letra=None, relleno=None):
    """Una casilla cuadrada, con o sin letra dentro."""
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.setFillColor(relleno or white)
    c.rect(x, y, lado, lado, fill=1, stroke=1)
    if letra:
        c.setFont('DejaVuSans-Bold', lado * 0.58)
        c.setFillColor(INK)
        c.drawCentredString(x + lado / 2, y + lado * 0.29, letra)


def ej_sopa(c, y, b):
    """Sopa de letras. Las palabras son de la cancion de esa semana."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Sopa de letras'),
                   b.get('pista', 'las palabras están en línea, tumbadas, de pie o en diagonal'))
    palabras = [p.upper() for p in b['palabras']]
    filas = b.get('filas', 9)
    cols = b.get('columnas', 22)
    rnd = random.Random(b.get('semilla', 7) * 1000 + len(''.join(palabras)))
    rejilla = [[None] * cols for _ in range(filas)]
    DIRS = [(0, 1), (1, 0), (1, 1), (1, -1)]
    colocadas = []
    for pal in palabras:
        for _ in range(600):
            df, dc = DIRS[rnd.randrange(len(DIRS))]
            f0 = rnd.randrange(filas)
            c0 = rnd.randrange(cols)
            ff, cf = f0 + df * (len(pal) - 1), c0 + dc * (len(pal) - 1)
            if not (0 <= ff < filas and 0 <= cf < cols):
                continue
            if any(rejilla[f0 + df * i][c0 + dc * i] not in (None, pal[i])
                   for i in range(len(pal))):
                continue
            for i, ch in enumerate(pal):
                rejilla[f0 + df * i][c0 + dc * i] = ch
            colocadas.append(pal)
            break
    for f in range(filas):
        for co in range(cols):
            if rejilla[f][co] is None:
                rejilla[f][co] = _ALFABETO[rnd.randrange(len(_ALFABETO))]

    # la rejilla ocupa el ancho entero: centrada y pequena parecia un recorte
    lado = CONTENT_W / cols
    x0 = MARGIN
    top = y - 4
    for f in range(filas):
        for co in range(cols):
            _caja_letra(c, x0 + co * lado, top - (f + 1) * lado, lado, rejilla[f][co])
    yy = top - filas * lado - 14

    # la lista de palabras, en columnas, con una casilla para tachar
    por_fila = b.get('por_fila', 5)
    ancho = CONTENT_W / por_fila
    for i, pal in enumerate(colocadas):
        fila, col = divmod(i, por_fila)
        px = MARGIN + col * ancho
        py = yy - fila * 15
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.setFillColor(white)
        c.rect(px, py - 8, 9, 9, fill=1, stroke=1)
        c.setFont('DejaVuSans-Bold', 8.0)
        c.setFillColor(NAVY)
        c.drawString(px + 14, py - 7, pal)
    n_filas_lista = (len(colocadas) + por_fila - 1) // por_fila
    return yy - n_filas_lista * 15 - 4


def ej_adivina(c, y, b):
    """Adivinanzas. La respuesta se escribe letra a letra, que asi se ve
       cuantas letras tiene y ayuda."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Adivina quién soy'),
                   b.get('pista', 'una letra en cada casilla'))
    lado = 13.0
    for texto, respuesta in b['items']:
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 4, y - 6, 2.4, fill=1, stroke=0)
        yy = _wrap(c, texto, MARGIN + 14, y - 9, 'DejaVuSans', 8.6,
                   CONTENT_W - 150, 11.0, INK)
        n = len(respuesta.replace(' ', ''))
        bx = W - MARGIN - n * (lado + 2)
        for i in range(n):
            _caja_letra(c, bx + i * (lado + 2), y - 13, lado,
                        respuesta[i].upper() if b.get('resuelto') else None)
        y = min(yy, y - 13) - 8
    return y - 2


def ej_crucigrama(c, y, b):
    """Acrostico: una palabra vertical, y las demas cruzandola. Es un
       crucigrama de verdad pero facil de resolver, porque cada fila ya sabe
       una letra."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Crucigrama'),
                   b.get('pista', 'la columna gris se lee de arriba abajo'))
    clave = b['clave'].upper()
    palabras = b['palabras']          # [(palabra, indice_de_la_letra_que_cruza, pista)]
    # el acrostico solo funciona si la columna sombreada deletrea la clave: se
    # comprueba aqui, que es un fallo facil de cometer escribiendo los datos y
    # dificil de ver en el PDF (la columna sale con letras, pero no dice nada)
    if len(palabras) != len(clave):
        raise ValueError('el acrostico tiene %d palabras y la clave %d letras'
                         % (len(palabras), len(clave)))
    for i, (pal, cruce, _) in enumerate(palabras):
        if pal.upper()[cruce] != clave[i]:
            raise ValueError('fila %d: %s[%d] es %s y la clave pide %s'
                             % (i + 1, pal.upper(), cruce, pal.upper()[cruce], clave[i]))
    # 15 pt es lo minimo para que quepa una letra escrita a mano por un nino
    lado = min(15.0, (CONTENT_W - 30) / (max(len(p[0]) for p in palabras) + 2))
    # la columna de la clave se pone donde quepan todas las palabras
    izq = max(p[1] for p in palabras)
    x_clave = MARGIN + 24 + izq * lado
    top = y - 4
    for i, (pal, cruce, _) in enumerate(palabras):
        fy = top - (i + 1) * lado
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(MUTED)
        c.drawRightString(x_clave - izq * lado - 6, fy + lado * 0.3, str(i + 1))
        for j, ch in enumerate(pal.upper()):
            cx = x_clave + (j - cruce) * lado
            es_clave = (j == cruce)
            # la columna sombreada va VACIA: descubrir la palabra escondida es
            # el ejercicio, y las pistas son faciles de sobra
            _caja_letra(c, cx, fy, lado, ch if b.get('resuelto') else None,
                        relleno=PANEL if es_clave else None)
    yy = top - len(palabras) * lado - 12

    for i, (_, _, pista) in enumerate(palabras):
        c.setFont('DejaVuSans-Bold', 8.0)
        c.setFillColor(ACCENT)
        c.drawString(MARGIN + 4, yy - 8, '%d.' % (i + 1))
        yy = _wrap(c, pista, MARGIN + 20, yy - 8, 'DejaVuSans', 8.4,
                   CONTENT_W - 30, 10.6, INK) - 1
    c.setFont('DejaVuSans', 8.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 4, yy - 9, b.get('cierre', 'La columna gris dice: %s' % ('_ ' * len(clave))))
    return yy - 20


def ej_camino(c, y, b):
    """Colorea solo las casillas que cumplen la regla y aparece un camino de
       arriba abajo. Se resuelve leyendo, no adivinando."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'El camino correcto'),
                   b.get('pista', 'colorea solo esas casillas y verás el camino'))
    filas = b['filas']                # [[etiqueta, etiqueta, ...], ...]
    ncol = max(len(f) for f in filas)
    ancho = CONTENT_W / ncol
    alto = b.get('alto_casilla', 19.0)
    top = y - 2
    for i, fila in enumerate(filas):
        for j, etq in enumerate(fila):
            x = MARGIN + j * ancho
            fy = top - (i + 1) * alto
            c.setStrokeColor(RULE)
            c.setLineWidth(0.7)
            c.setFillColor(white)
            c.rect(x, fy, ancho, alto, fill=1, stroke=1)
            size = _fit(etq, 'DejaVuSans', 8.4, ancho - 6, floor=6.0)
            c.setFont('DejaVuSans', size)
            c.setFillColor(INK)
            c.drawCentredString(x + ancho / 2, fy + alto * 0.32, etq)
    return top - len(filas) * alto - 10


def ej_vf(c, y, b):
    """Verdadero o falso. Rapido de hacer y bueno para repasar de memoria."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Verdadero o falso'),
                   b.get('pista', 'marca la casilla que toca'))
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY_SOFT)
    x_v, x_f = W - MARGIN - 44, W - MARGIN - 18
    c.drawCentredString(x_v + 6, y - 6, 'V')
    c.drawCentredString(x_f + 6, y - 6, 'F')
    yy = y - 18
    for frase in b['frases']:
        size = _fit(frase, 'DejaVuSans', 8.6, x_v - MARGIN - 26, floor=6.8)
        c.setFont('DejaVuSans', size)
        c.setFillColor(INK)
        c.drawString(MARGIN + 12, yy - 9, frase)
        for bx in (x_v, x_f):
            c.setStrokeColor(RULE)
            c.setLineWidth(0.8)
            c.setFillColor(white)
            c.rect(bx, yy - 12, 12, 12, fill=1, stroke=1)
        yy -= 18
    return yy - 2


def ej_ordena(c, y, b):
    """Los pasos, desordenados. Hay que numerarlos."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Pon los pasos en orden'),
                   b.get('pista', 'escribe 1, 2, 3… en las casillas'))
    yy = y - 4
    for paso in b['pasos']:
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.setFillColor(white)
        c.rect(MARGIN + 2, yy - 15, 16, 15, fill=1, stroke=1)
        size = _fit(paso, 'DejaVuSans', 8.6, CONTENT_W - 34, floor=6.8)
        c.setFont('DejaVuSans', size)
        c.setFillColor(INK)
        c.drawString(MARGIN + 26, yy - 11, paso)
        yy -= 19
    return yy - 2


def ej_diferencias(c, y, b):
    """Dos pentagramas casi iguales. Uno es el de la partitura y el otro tiene
       trampas: hay que encontrarlas comparando nota a nota."""
    n = b.get('cuantas', 3)
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Busca las diferencias'),
                   b.get('pista', 'hay %d cosas cambiadas · rodea las del pentagrama de abajo' % n))
    gap = b.get('gap', 7.4)
    clef = b.get('clef', 'treble')
    # el pentagrama arranca 16 pt a la derecha del margen: ese hueco es para la
    # letra A o B, que encima de la clave no se lee
    sangria = 16
    for etiqueta, eventos in (('A', b['a']), ('B', b['b'])):
        y -= gap * 1.6
        ys = draw_staff(c, MARGIN + sangria, y, CONTENT_W - sangria, gap=gap)
        top, bot = ys[0], ys[-1]
        draw_clef(c, MARGIN + sangria + 4, bot, gap, clef=clef)
        c.setFont('DejaVuSans-Bold', 9.0)
        c.setFillColor(NAVY_SOFT)
        c.drawString(MARGIN, (top + bot) / 2 - 3, etiqueta)
        x0 = MARGIN + sangria + gap * 6.8
        paso = (CONTENT_W - sangria - gap * 8.2) / max(1, len(eventos) - 1)
        for i, ev in enumerate(eventos):
            draw_note(c, x0 + i * paso, bot, top, gap, ev['pitch'],
                      dur=ev.get('dur', 'q'), clef=clef)
        y = bot - gap * 2.2
    return y - 6


def ej_cuenta(c, y, b):
    """Un pentagrama, y preguntas de contar. Obliga a mirar el papel entero."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Cuenta y escribe'),
                   b.get('pista', 'mira el pentagrama y escribe el número en la caja'))
    gap = b.get('gap', 7.6)
    clef = b.get('clef', 'treble')
    eventos = b['eventos']
    y -= gap * 1.4
    top, bot = _pauta(c, y, gap, clef=clef)
    x0 = MARGIN + gap * 6.8
    paso = (CONTENT_W - gap * 8.4) / max(1, len(eventos) - 1)
    for i, ev in enumerate(eventos):
        draw_note(c, x0 + i * paso, bot, top, gap, ev['pitch'],
                  dur=ev.get('dur', 'q'), clef=clef)
    yy = bot - gap * 2.6
    for pregunta in b['preguntas']:
        size = _fit(pregunta, 'DejaVuSans', 8.6, CONTENT_W - 60, floor=6.8)
        c.setFont('DejaVuSans', size)
        c.setFillColor(INK)
        c.drawString(MARGIN + 12, yy - 10, pregunta)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.setFillColor(white)
        c.rect(W - MARGIN - 30, yy - 13, 28, 15, fill=1, stroke=1)
        yy -= 19
    return yy - 2


def _teclado_mudo(c, x, y_top, n_white, kw, kh, senales=None):
    """Teclado sin los nombres puestos: los pone el alumno. `senales` marca
       teclas con una flecha y un numero, para preguntar por una en concreto."""
    senales = senales or {}
    bw, bh = kw * 0.60, kh * 0.62
    for i in range(n_white):
        kx = x + i * kw
        c.setFillColor(white)
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.8)
        c.rect(kx, y_top - kh, kw, kh, fill=1, stroke=1)
        if i in senales:
            c.setFont('DejaVuSans-Bold', 8.0)
            c.setFillColor(ACCENT)
            c.drawCentredString(kx + kw / 2, y_top + 5, str(senales[i]))
            c.setStrokeColor(ACCENT)
            c.setLineWidth(1.2)
            c.line(kx + kw / 2, y_top + 1, kx + kw / 2, y_top + 3.6)
    for i in range(n_white):
        if (i % 7) in BLACK_AFTER and i < n_white - 1:
            bx = x + (i + 1) * kw - bw / 2
            c.setFillColor(NAVY)
            c.setStrokeColor(NAVY)
            c.setLineWidth(0.6)
            c.rect(bx, y_top - bh, bw, bh, fill=1, stroke=1)
    return y_top - kh


def ej_teclado(c, y, b):
    """Un teclado dibujado, con las teclas en blanco. Sirve para pasar del
       papel a las manos, que es donde se lia todo el mundo."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'En el teclado'), b.get('pista'))
    n_white = b.get('teclas', 15)
    kh = b.get('alto', 44)
    kw = CONTENT_W / n_white
    bot = _teclado_mudo(c, MARGIN, y - 12, n_white, kw, kh, senales=b.get('senales'))
    yy = bot - 12
    for linea in b.get('preguntas', []):
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(INK)
        c.drawString(MARGIN + 12, yy, '·  ' + linea)
        yy -= 12
    return yy - 4


def ej_palmas(c, y, b):
    """El ritmo de una palabra. Se dice en voz alta, se cuenta las silabas y se
       escribe con figuras. Es lo que mas rapido ensena a leer ritmo."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'El ritmo de las palabras'),
                   b.get('pista', 'dilo en voz alta, cuenta las sílabas y escríbelo con figuras'))
    yy = y - 4
    for palabra, silabas in b['palabras']:
        c.setFont('DejaVuSans-Bold', 9.4)
        c.setFillColor(NAVY)
        c.drawString(MARGIN + 4, yy - 15, palabra)
        c.setFont('DejaVuSans', 7.6)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + 4, yy - 25, '%d sílabas' % silabas)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.setFillColor(white)
        c.roundRect(MARGIN + 118, yy - 27, CONTENT_W - 118, 26, 3, fill=1, stroke=1)
        yy -= 32
    return yy - 2


def ej_inventa(c, y, b):
    """Inventar, pero con condiciones. Sin condiciones un nino de diez anos
       escribe ocho redondas y se queda tan ancho."""
    y = _titulo_ej(c, y, b['num'], b.get('titulo', 'Inventa tú'),
                   b.get('pista', 'tiene que cumplir todo esto'))
    for cond in b['condiciones']:
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 8, y - 5, 2.2, fill=1, stroke=0)
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(INK)
        c.drawString(MARGIN + 18, y - 8, cond)
        y -= 12
    gap = b.get('gap', 8.6)
    for i in range(b.get('lineas', 1)):
        y -= gap * 2.0
        ys = draw_staff(c, MARGIN, y, CONTENT_W, gap=gap)
        if b.get('clef'):
            draw_clef(c, MARGIN + 4, ys[-1], gap, clef=b['clef'])
        # el compas solo en la primera linea, como en una partitura de verdad
        if b.get('time_sig') and not i:
            draw_time_sig(c, MARGIN + gap * 4.4, ys[-1], gap,
                          top=str(b['time_sig'][0]), bottom=str(b['time_sig'][1]))
        y = ys[-1] - gap * 1.6
    return y - 4


TIPOS = {
    'nombres': ej_nombres, 'dibuja': ej_dibuja, 'figuras': ej_figuras,
    'une': ej_une, 'rodea': ej_rodea, 'colorea': ej_colorea,
    'rutina': rutina, 'escucha': ej_escucha, 'nota': nota,
    'escribe': ej_escribe,
    'sopa': ej_sopa, 'adivina': ej_adivina, 'crucigrama': ej_crucigrama,
    'camino': ej_camino, 'vf': ej_vf, 'ordena': ej_ordena,
    'diferencias': ej_diferencias, 'cuenta': ej_cuenta, 'teclado': ej_teclado,
    'palmas': ej_palmas, 'inventa': ej_inventa,
}


# Estos tres no son ejercicios y van sin casilla numerada: la tabla de la
# semana es un marcador, y el juego y el recuadro de acordarse son texto.
SIN_NUMERO = {'rutina', 'escucha', 'nota'}


def build_deberes(c, cfg):
    y = _cabecera(c, cfg)
    # Los ejercicios se numeran SOLOS, en el orden en que van. Escribir el
    # numero a mano en cada bloque obligaba a renumerar la hoja entera cada vez
    # que se cambiaba el orden, y con la norma de variedad el orden cambia
    # todas las semanas.
    num = 0
    for bruto in cfg['bloques']:
        b = bruto
        if b['tipo'] not in SIN_NUMERO:
            num += 1
            b = dict(b, num=b.get('num') or num)
        fn = TIPOS[b['tipo']]
        y = fn(c, y, b)
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y
