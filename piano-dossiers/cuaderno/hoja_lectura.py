# -*- coding: utf-8 -*-
"""Hoja de AGUDEZA VISUAL Y AUDITIVA. Dos mitades, ninguna toca el piano.

   PARTE 1 · LEER — el ojo.
   Principio de ANTI-SECUENCIA: el calentamiento usa secuencias (una célula
   transportada) porque busca memoria muscular, pero leer necesita justo lo
   contrario. Si las notas siguen un patrón, el alumno lo adivina y deja de
   leer. Aquí el orden es deliberadamente irregular y ninguna célula se
   repite.

   PARTE 2 · ESCUCHAR — el oído.
   La dirige quien acompaña (el profesor en clase, cualquiera en casa): toca,
   y el alumno responde sin mirar el teclado. Todo lo que se pregunta sale de
   la pieza, igual que en el resto del cuaderno: si la canción se abre y se
   cierra en intervalos, la pregunta es "cerca o lejos"; si tiene dos partes
   con carácter distinto, la pregunta es "A o B".

   Las casillas se rodean con lápiz, así que la hoja tiene que dejar sitio
   físico para el trazo: de ahí el tamaño de las celdas.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system, draw_staff, draw_clef, note_y, draw_notehead
from page_layout_common import before_staff, after_system
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')

GAP = 6.6
BARS_PER_LINE = 5


def seccion(c, y, num, titulo, sub):
    """Cabecera de media hoja: PARTE 1 · LEER / PARTE 2 · ESCUCHAR."""
    c.setFillColor(NAVY)
    c.roundRect(MARGIN, y - 14, 17, 17, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9.4)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 8.5, y - 10.4, num)
    c.setFont('DejaVuSerif-Bold', 13)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 25, y - 11, titulo)
    tw = stringWidth(titulo, 'DejaVuSerif-Bold', 13)
    ss = _fit(sub, 'DejaVuSans', 8.2, CONTENT_W - 25 - tw - 12, floor=6.4)
    c.setFont('DejaVuSans', ss)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 25 + tw + 12, y - 10, sub)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(MARGIN, y - 21, W - MARGIN, y - 21)
    return y - 27


def _ej_heading(c, y, num, titulo, pista):
    c.setFillColor(BLUE)
    c.roundRect(MARGIN, y - 13, 16, 16, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 8, y - 9.5, str(num))
    c.setFont('DejaVuSans-Bold', 9.6)
    c.setFillColor(INK)
    c.drawString(MARGIN + 23, y - 9, titulo)
    tw = stringWidth(titulo, 'DejaVuSans-Bold', 9.6)
    psize = _fit(pista, 'DejaVuSans', 8.2, CONTENT_W - 23 - tw - 12, floor=6.2)
    c.setFont('DejaVuSans', psize)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 23 + tw + 12, y - 9, pista)
    return y - 20


def chuleta(c, y, pitches, nombres, gap=6.6, clef='treble', titulo='LAS NOTAS DE ESTA PARTITURA'):
    """Referencia: cada nota del registro de la pieza, con su nombre debajo.
       Sirve de apoyo las primeras semanas; luego se tapa con la mano."""
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, titulo)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.3)
    c.line(MARGIN, y - 5, MARGIN + 22, y - 5)
    y -= 19

    # la caja se dimensiona a partir de la nota mas grave: si se fija a ojo,
    # los nombres se montan encima de las notas de linea adicional
    staff_top = y - 11
    sx, sw = MARGIN + 16, CONTENT_W - 32
    bot = staff_top - gap * 4
    low = min(note_y(bot, gap, p, clef=clef) for p in pitches)
    label_y = min(low, bot) - gap * 1.9
    box_h = (y - label_y) + 9

    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - box_h, CONTENT_W, box_h, 4, fill=1, stroke=0)
    draw_staff(c, sx, staff_top, sw, gap=gap)
    draw_clef(c, sx + 3, bot, gap, clef=clef)
    # la clave de Sol ocupa mas de lo que parece: si las notas empiezan antes
    # de ~9 espacios, los nombres de debajo se montan encima del dibujo
    x0 = sx + gap * 9.4
    step = (sw - gap * 10.6) / max(len(pitches) - 1, 1)
    for i, (p, nm) in enumerate(zip(pitches, nombres)):
        cx = x0 + i * step
        cy = note_y(bot, gap, p, clef=clef)
        draw_notehead(c, cx, cy, gap, filled=True)
        if cy < bot:   # nota bajo el pentagrama: linea adicional
            c.setStrokeColor(NAVY)
            c.setLineWidth(1.0)
            c.line(cx - gap * 0.95, cy, cx + gap * 0.95, cy)
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY)
        c.drawCentredString(cx, label_y, nm)
    return y - box_h - 12


def _lineas(c, y, events, time_sig, bars_per_line=BARS_PER_LINE, gap=GAP,
            clef='treble', key_sig=None):
    dur_beats = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'q.': 1.5, 'h.': 3.0}
    bpb = time_sig[0] * (4.0 / time_sig[1])
    line_beats = bpb * bars_per_line
    lines, cur, acc = [], [], 0.0
    for e in events:
        cur.append(e)
        acc += dur_beats[e['dur']]
        if acc >= line_beats - 1e-6:
            lines.append(cur); cur, acc = [], 0.0
    if cur:
        lines.append(cur)
    for i, ln in enumerate(lines):
        y -= before_staff(gap, ln, clef)
        top, bot = draw_system(c, MARGIN, y, CONTENT_W, gap, ln, clef=clef,
                               time_sig=time_sig, show_time=(i == 0),
                               key_sig=key_sig, spacing='engraved')
        # entre lineas hay que reservar tambien el sitio de las plicas y
        # barras que cuelgan: con un hueco fijo de 2*gap, un compas de
        # corcheas con la barra abajo se mete dentro del pentagrama siguiente
        last = i == len(lines) - 1
        y = bot - (after_system(gap, ln, clef) if last
                   else max(gap * 2.0, after_system(gap, ln, clef) * 0.85))
    return y


def crono(c, y, titulo, intentos=3, w=None):
    """Casillas de tiempo: leer la misma línea varias veces y ver que cada
       vez se tarda menos es lo que de verdad engancha y mide la soltura."""
    w = w or CONTENT_W
    h = 24
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, w, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    # el titulo tiene que caber en lo que sobra a la izquierda de las
    # casillas: si se pone a pelo, se monta encima de la primera raya
    bx = W - MARGIN - 13 - intentos * 84 + 8
    tsize = _fit(titulo.upper(), 'DejaVuSans-Bold', 7.6,
                 bx - (MARGIN + 13) - 10, floor=5.6)
    c.setFont('DejaVuSans-Bold', tsize)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 13, y - 15, titulo.upper())
    for i in range(1, intentos + 1):
        c.setFont('DejaVuSans', 7.4)
        c.setFillColor(MUTED)
        c.drawString(bx, y - 15, f'{i}ª')
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.8)
        c.line(bx + 13, y - 16, bx + 68, y - 16)
        bx += 84
    return y - h


def caja_profe(c, y, lineas):
    """Lo que toca quien acompaña. Va con borde y en otro color porque NO es
       para que lo lea el alumno: si lo lee, se acabó el ejercicio."""
    inner = CONTENT_W - 24
    alto = []
    for _, txt in lineas:
        n, ln = 1, ''
        for wd in txt.split():
            t = (ln + ' ' + wd).strip()
            if stringWidth(t, 'DejaVuSans', 7.3) > inner - 16:
                n += 1; ln = wd
            else:
                ln = t
        alto.append(n)
    h = 20 + sum(n * 9.6 for n in alto) + 2.0 * len(lineas)

    c.setFillColor(white)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.9)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=1)
    c.setFont('DejaVuSans-Bold', 6.8)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 12, y - 12, 'PARA QUIEN TOCA  ·  el alumno no mira esta caja ni el teclado')

    yy = y - 21
    for (letra, txt), n in zip(lineas, alto):
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(ACCENT)
        c.drawString(MARGIN + 12, yy - 7.4, letra)
        _wrap(c, txt, MARGIN + 28, yy, 'DejaVuSans', 7.3, inner - 16, 9.6, INK)
        yy -= n * 9.6 + 2.0
    return y - h - 8


def fila_respuestas(c, y, letra, titulo, pista, n, opciones):
    """Fila de casillas numeradas: el alumno rodea la respuesta con lápiz."""
    c.setFont('DejaVuSans-Bold', 8.8)
    c.setFillColor(BLUE)
    c.drawString(MARGIN, y - 8, letra + ')')
    lw = stringWidth(letra + ')', 'DejaVuSans-Bold', 8.8)
    c.setFont('DejaVuSans-Bold', 8.8)
    c.setFillColor(INK)
    c.drawString(MARGIN + lw + 6, y - 8, titulo)
    tw = stringWidth(titulo, 'DejaVuSans-Bold', 8.8)
    ps = _fit(pista, 'DejaVuSans', 7.8, CONTENT_W - lw - tw - 20, floor=6.2)
    c.setFont('DejaVuSans', ps)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + lw + tw + 12, y - 8, pista)
    y -= 16

    sep, ch = 5, 18
    cw = (CONTENT_W - sep * (n - 1)) / n
    k = len(opciones)
    largest = max(opciones, key=len)
    osize = _fit(largest, 'DejaVuSans-Bold', 8.6, cw / k - 3.5, floor=5.4)
    for i in range(n):
        bx = MARGIN + i * (cw + sep)
        c.setFont('DejaVuSans', 6.2)
        c.setFillColor(MUTED)
        c.drawString(bx + 1.5, y - 5.5, str(i + 1))
        c.setFillColor(white)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.9)
        c.roundRect(bx, y - 7 - ch, cw, ch, 2.5, fill=1, stroke=1)
        for j, op in enumerate(opciones):
            c.setFont('DejaVuSans-Bold', osize)
            c.setFillColor(NAVY_SOFT)
            c.drawCentredString(bx + cw * (j + 0.5) / k, y - 7 - ch + 6.6, op)
    return y - 7 - ch - 8


def build_lectura(c, cfg):
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
    c.drawRightString(W - MARGIN, y, 'Sin tocar el piano')
    y -= 28

    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'Agudeza visual y auditiva')
    y -= 15
    y = _wrap(c, cfg['intro'], MARGIN, y, 'DejaVuSans', 9, CONTENT_W, 11.4, MUTED)
    y -= 10

    # ---------------- PARTE 1 · LEER -------------------------------------
    y = seccion(c, y, '1', 'Leer', cfg['sub_leer'])
    y = chuleta(c, y, cfg['chuleta_pitches'], cfg['chuleta_nombres'],
                clef=cfg.get('chuleta_clef', 'treble'),
                titulo=cfg.get('chuleta_titulo', 'LAS NOTAS DE ESTA PARTITURA'))
    for ej in cfg['ejercicios']:
        y = _ej_heading(c, y, ej['num'], ej['titulo'], ej['pista'])
        y = _lineas(c, y, ej['events'], cfg['time_sig'],
                    bars_per_line=ej.get('bars_per_line', BARS_PER_LINE),
                    gap=ej.get('gap', cfg.get('gap', GAP)),
                    clef=ej.get('clef', 'treble'),
                    key_sig=ej.get('key_sig', cfg.get('key_sig')))
        y -= ej.get('extra_gap', 2)
    if cfg.get('crono'):
        y = crono(c, y, cfg['crono'])
    y -= 12

    # ---------------- PARTE 2 · ESCUCHAR ---------------------------------
    esc = cfg['escucha']
    y = seccion(c, y, '2', 'Escuchar', esc['sub'])
    y = caja_profe(c, y, esc['profe'])
    for f in esc['filas']:
        y = fila_respuestas(c, y, f['letra'], f['titulo'], f['pista'],
                            f['n'], f['opciones'])

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y
