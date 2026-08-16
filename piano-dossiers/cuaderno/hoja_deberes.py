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

   Todo el texto va SIN TECNICISMOS: "la nota que esta en la primera linea",
   no "el Mi del primer espacio del pentagrama en clave de sol". Cuando hace
   falta una palabra tecnica se explica ahi mismo, en la misma frase.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import (draw_staff, draw_clef, draw_barline, draw_note, draw_chord,
                      draw_notehead, draw_ledger, ledger_lines_needed, note_y,
                      draw_time_sig)
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

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
    for i in range(len(izq)):
        c.setFont('DejaVuSans-Bold', 8.6)
        c.setFillColor(NAVY)
        c.drawString(MARGIN + 14, yy - 9, izq[i])
        c.setFillColor(ACCENT)
        c.circle(MARGIN + CONTENT_W * 0.42, yy - 6, 2.4, fill=1, stroke=0)
        c.circle(MARGIN + CONTENT_W * 0.58, yy - 6, 2.4, fill=1, stroke=0)
        c.setFont('DejaVuSans', 8.6)
        c.setFillColor(INK)
        c.drawString(MARGIN + CONTENT_W * 0.62, yy - 9, der[i])
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


def ej_escucha(c, y, b):
    """El juego con un adulto. No hace falta que sepa musica."""
    h = b.get('alto', 78)
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
    words, ln, count = texto.split(), '', 1
    for wd in words:
        t = (ln + ' ' + wd).strip()
        if stringWidth(t, 'DejaVuSans', size) > inner:
            count += 1; ln = wd
        else:
            ln = t
    h = 20 + count * 11.0
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


TIPOS = {
    'nombres': ej_nombres, 'dibuja': ej_dibuja, 'figuras': ej_figuras,
    'une': ej_une, 'rodea': ej_rodea, 'colorea': ej_colorea,
    'rutina': rutina, 'escucha': ej_escucha, 'nota': nota,
    'escribe': ej_escribe,
}


def build_deberes(c, cfg):
    y = _cabecera(c, cfg)
    for b in cfg['bloques']:
        fn = TIPOS[b['tipo']]
        y = fn(c, y, b)
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y
