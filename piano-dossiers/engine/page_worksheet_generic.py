# -*- coding: utf-8 -*-
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import *

W, H = 595.276, 841.89
MARGIN = 46
CONTENT_W = W - 2 * MARGIN


def wrap_text(c, text, x, y, font, size, max_w, leading, color=GRAY):
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split(' ')
    line = ''
    for w in words:
        test = (line + ' ' + w).strip()
        if stringWidth(test, font, size) <= max_w:
            line = test
        else:
            c.drawString(x, y, line)
            y -= leading
            line = w
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def header(c, kicker):
    c.setFillColor(DARKGREEN)
    c.rect(0, H - 5, W, 5, fill=1, stroke=0)
    y = H - 32
    c.setFont('DejaVuSans-Bold', 8.8)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y, kicker.upper())
    c.setFont('DejaVuSans', 8.8)
    c.setFillColor(GRAY)
    c.drawRightString(W - MARGIN, y, 'Trabajo sin piano')
    y -= 22
    c.setFont('DejaVuSerif-Bold', 16.5)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Ficha de lenguaje musical · escribe, dibuja y colorea')
    y -= 15
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Nombre: _______________________________________________        Fecha: ______________')
    return y - 20


def footer(c, page_num='5'):
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(HexColor('#8A8A8A'))
    c.drawCentredString(W / 2, 22, 'El Cuaderno del Pianista · T-Clas')
    c.drawRightString(W - MARGIN, 22, page_num)


def section_heading(c, y, num, title, desc):
    c.setFillColor(DARKGREEN)
    c.roundRect(MARGIN, y - 17, 20, 20, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 10, y - 12.5, str(num))
    c.setFont('DejaVuSans-Bold', 11.6)
    c.setFillColor(INK)
    c.drawString(MARGIN + 28, y - 12, title)
    yy = wrap_text(c, desc, MARGIN + 28, y - 25, 'DejaVuSans', 8.9, CONTENT_W - 28, 11.6)
    return yy


def clef_tag(c, x, y, text, color):
    c.setFillColor(color)
    c.setFont('DejaVuSans-Bold', 7.2)
    c.drawString(x, y, text)


def draw_write_target(c, x, staff_bottom_y, gap, label):
    c.setFont('DejaVuSans-Bold', gap * 0.8)
    c.setFillColor(DARKGREEN)
    c.drawCentredString(x, staff_bottom_y - gap * 2.5, label)


def draw_headless_note(c, cx, staff_bottom_y, staff_top_y, gap, pitch, clef='treble'):
    cy = note_y(staff_bottom_y, gap, pitch, clef=clef)
    for ly in ledger_lines_needed(staff_bottom_y, staff_top_y, cy, gap):
        draw_ledger(c, cx, ly, gap)
    draw_notehead(c, cx, cy, gap, filled=True)
    return cx, cy


def write_row(c, x0, w0, y, gap, clef, tag, tag_color, names):
    clef_tag(c, x0, y, tag, tag_color)
    y -= 10
    ys = draw_staff(c, x0, y, w0, gap=gap)
    top, bot = ys[0], ys[-1]
    draw_clef(c, x0 + 4, bot, gap, clef=clef)
    draw_barline(c, x0, top, bot)
    draw_barline(c, x0 + w0, top, bot, final=True)
    start_x = x0 + gap * 8.2
    step = (w0 - gap * 10.2) / (len(names) - 1)
    for i, nm in enumerate(names):
        draw_write_target(c, start_x + i * step, bot, gap, nm)
    return bot


def note_row_headless(c, x0, w0, y, gap, clef, tag, tag_color, pitches):
    clef_tag(c, x0, y, tag, tag_color)
    y -= 10
    ys = draw_staff(c, x0, y, w0, gap=gap)
    top, bot = ys[0], ys[-1]
    draw_clef(c, x0 + 4, bot, gap, clef=clef)
    draw_barline(c, x0, top, bot)
    draw_barline(c, x0 + w0, top, bot, final=True)
    start_x = x0 + gap * 8.2
    step = (w0 - gap * 10.2) / (len(pitches) - 1)
    for i, p in enumerate(pitches):
        draw_headless_note(c, start_x + i * step, bot, top, gap, p, clef=clef)
    return bot


def note_row_filled(c, x0, w0, y, gap, clef, tag, tag_color, pitches, with_timesig=False):
    clef_tag(c, x0, y, tag, tag_color)
    y -= 10
    ys = draw_staff(c, x0, y, w0, gap=gap)
    top, bot = ys[0], ys[-1]
    draw_clef(c, x0 + 4, bot, gap, clef=clef)
    cursor = x0 + gap * 8.6
    if with_timesig:
        draw_time_sig(c, x0 + gap * 5.4, bot, gap)
    draw_barline(c, x0, top, bot)
    step = (x0 + w0 - 10 - cursor) / (len(pitches) - 1)
    for i, p in enumerate(pitches):
        draw_note(c, cursor + i * step, bot, top, gap, p, dur='q', clef=clef)
    draw_barline(c, x0 + w0, top, bot, final=True)
    return bot


def build_worksheet(c, cfg):
    """cfg keys: kicker, sec1_treble/sec1_bass/sec1_alto (8-note sequences, varied per song),
       sec2_title, sec2_desc, sec2_pitches (headless notes, treble),
       sec3_title, sec3_desc, sec3_treble (filled quarters), sec3_bass (filled quarters),
       pista_text, quiz_pitches (treble)."""
    y = header(c, cfg['kicker'])
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    # ============ SECTION 1: ESCRIBE LAS NOTAS (2 claves) ============
    y = section_heading(c, y, 1, cfg.get('sec1_title', 'Escribe cada nota en su sitio'),
                         cfg.get('sec1_desc', 'Dibuja el óvalo de la nota en la línea o espacio correcto (todavía sin plica).'))
    y -= 16
    bot1 = write_row(c, x0, w0, y, gap, 'treble', 'CLAVE DE SOL', DARKGREEN, cfg['sec1_treble'])
    y = bot1 - gap * 4.2
    bot2 = write_row(c, x0, w0, y, gap, 'bass', 'CLAVE DE FA', MAROON, cfg['sec1_bass'])
    y = bot2 - 30

    # ============ SECTION 2: TEMATICA (variable per song) + PLICA ============
    y = section_heading(c, y, 2, cfg['sec2_title'], cfg['sec2_desc'])
    y -= 14
    y2 = note_row_headless(c, x0, w0, y, gap, 'treble', 'CLAVE DE SOL', DARKGREEN, cfg['sec2_pitches'])
    y = y2 - 26

    # ============ SECTION 3: COLOREA (Sol y Fa) ============
    y = section_heading(c, y, 3, cfg['sec3_title'], cfg['sec3_desc'])
    y -= 14
    y3 = note_row_filled(c, x0, w0, y, gap, 'treble', 'CLAVE DE SOL', DARKGREEN, cfg['sec3_treble'], with_timesig=True)
    y = y3 - gap * 3.0
    y4 = note_row_filled(c, x0, w0, y, gap, 'bass', 'CLAVE DE FA', MAROON, cfg['sec3_bass'], with_timesig=True)
    y = y4 - 22

    pista_w = w0 - 20
    c.setFont('DejaVuSans', 8.4)
    # measure how many lines the pista text will need (without drawing yet)
    words = cfg['pista_text'].split(' ')
    line = ''
    n_lines = 1
    for w in words:
        test = (line + ' ' + w).strip()
        if stringWidth(test, 'DejaVuSans', 8.4) <= pista_w:
            line = test
        else:
            n_lines += 1
            line = w
    box_h = 22 + n_lines * 11.5

    c.setFillColor(HexColor('#EDE6D6'))
    c.setStrokeColor(LIGHTLINE)
    c.roundRect(x0, y - box_h, w0, box_h, 5, fill=1, stroke=1)
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(DARKGREEN)
    c.drawString(x0 + 10, y - 15, '\u266A Pista:')
    wrap_text(c, cfg['pista_text'], x0 + 10, y - 29, 'DejaVuSans', 8.4, pista_w, 11.5, color=INK)
    y -= box_h + 14

    # ============ SECTION 4: QUIZ RAPIDO ============
    y = section_heading(c, y, 4, '¿Qué nota es? Escribe el nombre debajo',
                         'Mira en qué línea o espacio está cada nota y escribe Do, Re, Mi, Fa, Sol, La o Si.')
    y -= 14
    ys7 = draw_staff(c, x0, y, w0, gap=gap)
    top7, bot7 = ys7[0], ys7[-1]
    draw_clef(c, x0 + 4, bot7, gap, clef='treble')
    draw_barline(c, x0, top7, bot7)
    draw_barline(c, x0 + w0, top7, bot7, final=True)
    quiz_notes = cfg['quiz_pitches']
    cursor3 = x0 + gap * 8.2
    step6 = (x0 + w0 - 10 - cursor3) / (len(quiz_notes) - 1)
    for i, p in enumerate(quiz_notes):
        px = cursor3 + i * step6
        draw_note(c, px, bot7, top7, gap, p, dur='q', clef='treble')
        c.setStrokeColor(LIGHTLINE)
        c.setLineWidth(0.7)
        c.line(px - gap * 1.1, bot7 - gap * 2.6, px + gap * 1.1, bot7 - gap * 2.6)
    y = bot7 - 34

    footer(c)
