# -*- coding: utf-8 -*-
"""Generador de la ficha de TEORIA AVANZADA: para alumnos adolescentes o de
   nivel medio-alto, sustituye la ficha infantil de escribir/colorear/quiz por
   contenido mas serio -- intervalos, acordes, analisis armonico de la propia
   cancion (con cifrado romano o funcion tonal) y dictado ritmico.
   Parametrizado, igual que el resto de paginas genericas del motor."""
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import *
from notation import _parse_pitch, _abs_idx, _TREBLE_REF, _BASS_REF, _ALTO_REF

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
    c.drawRightString(W - MARGIN, y, 'Teoría y oído')
    y -= 22
    c.setFont('DejaVuSerif-Bold', 16.5)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Ficha de armonía y oído')
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


def _answer_line(c, x, y, w):
    c.setStrokeColor(LIGHTLINE)
    c.setLineWidth(0.7)
    c.line(x, y, x + w, y)


def _interval_chord_row(c, x0, w0, y, gap, clef, groups, tag):
    """Draws one staff with N stacked-note groups (2 or 3 notes each) spread
       across it, plus a blank answer line under each group."""
    c.setFont('DejaVuSans-Bold', 7.2)
    c.setFillColor(DARKGREEN)
    c.drawString(x0, y, tag)
    y -= 10
    ys = draw_staff(c, x0, y, w0, gap=gap)
    top, bot = ys[0], ys[-1]
    draw_clef(c, x0 + 4, bot, gap, clef=clef)
    draw_barline(c, x0, top, bot)
    draw_barline(c, x0 + w0, top, bot, final=True)
    start_x = x0 + gap * 8.2
    step = (w0 - gap * 10.2) / (len(groups) - 1) if len(groups) > 1 else 0
    for i, pitches in enumerate(groups):
        px = start_x + i * step
        draw_chord(c, px, bot, top, gap, pitches, dur='w', clef=clef)
        _answer_line(c, px - gap * 2.3, bot - gap * 2.6, gap * 4.6)
    # A low note carrying a sharp/flat can draw its accidental well below the
    # staff -- if it's lower than the usual clearance, push the next section
    # down further so its heading doesn't collide with the accidental glyph.
    clearance = gap * 3.6
    ref = {'treble': _TREBLE_REF, 'bass': _BASS_REF}.get(clef, _ALTO_REF)
    for pitches in groups:
        for p in pitches:
            _letter, acc, _oct = _parse_pitch(p)
            if not acc:
                continue
            cy = bot + (_abs_idx(p) - ref) * (gap / 2.0)
            if cy < bot:
                clearance = max(clearance, (bot - cy) + gap * 1.3)
    return bot - clearance


def _progression_row(c, x0, w0, y, chords, mode):
    """Draws the song's real chord sequence as text boxes with a blank line
       underneath each for the roman numeral / tonal function."""
    n = len(chords)
    box_w = w0 / n
    for i, chord_label in enumerate(chords):
        bx = x0 + i * box_w
        c.setFillColor(HexColor('#F6F3EA'))
        c.roundRect(bx + 3, y - 30, box_w - 6, 24, 4, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(INK)
        c.drawCentredString(bx + box_w / 2, y - 21, chord_label)
        _answer_line(c, bx + 10, y - 40, box_w - 20)
    hint = ('Escribe el grado (I, ii, iii, IV, V...) de cada acorde' if mode == 'roman'
            else 'Escribe si cada acorde es tónica (T), subdominante (SD) o dominante (D)')
    c.setFont('DejaVuSans', 7.8)
    c.setFillColor(GRAY)
    c.drawString(x0, y - 52, hint)
    return y - 66


def build_harmony_page(c, cfg):
    """cfg keys:
         kicker
         intervals_desc, intervals (6x (p1,p2))
         chords_desc, chords (4x [p1,p2,p3])
         song_title, song_key
         progression_desc, progression (chord label strings), progression_mode ('roman'|'function')
         rhythm_desc, rhythm_events, rhythm_time_sig
    """
    y = header(c, cfg['kicker'])
    gap = 8.6

    y = section_heading(c, y, 1, 'Reconoce el intervalo', cfg['intervals_desc'])
    y -= 14
    y = _interval_chord_row(c, MARGIN, CONTENT_W, y, gap, 'treble', cfg['intervals'], 'INTERVALOS')
    y -= 14

    y = section_heading(c, y, 2, 'Reconoce el acorde', cfg['chords_desc'])
    y -= 14
    y = _interval_chord_row(c, MARGIN, CONTENT_W, y, gap, 'treble', cfg['chords'], 'ACORDES')
    y -= 8

    y = section_heading(c, y, 3, f"Analiza la armonía de «{cfg['song_title']}»", cfg['progression_desc'])
    y -= 16
    y = _progression_row(c, MARGIN, CONTENT_W, y, cfg['progression'], cfg['progression_mode'])
    y -= 4

    y = section_heading(c, y, 4, 'Dictado rítmico', cfg['rhythm_desc'])
    y -= 14
    tsig = cfg.get('rhythm_time_sig', (4, 4))
    _top, bot = draw_system(c, MARGIN, y, CONTENT_W, 7.6, cfg['rhythm_events'], clef='treble', time_sig=tsig)
    y = bot - 7.6 * 2.6
    _answer_line(c, MARGIN, y, CONTENT_W)
    c.setFont('DejaVuSans', 7.8)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y - 12, 'Escribe la cuenta de cada compás (1, 2-y, 3...) o da las palmas mientras la marcas en voz alta.')

    footer(c)
