# -*- coding: utf-8 -*-
"""Motor de maquetacion COMUN para el taller de practica de cualquier cancion.
   Toda la logica de espaciado ya esta verificada (sin solapes, sin desbordes);
   cada cancion solo aporta su propio contenido musical importando este modulo."""
from reportlab.lib.colors import HexColor, white
from notation import *
from notation import _parse_pitch

W, H = 595.276, 841.89
MARGIN = 46
CONTENT_W = W - 2 * MARGIN
STAR_FULL, STAR_EMPTY = '\u2605', '\u2606'


def after_system(gap):
    """Vertical drop from a staff's bottom line to the next caption's baseline.
       (Verified safe clearance for numbers/labels below any staff content.)"""
    return gap * 3.5


def before_staff(gap, events=None, clef='treble'):
    """Vertical drop from a caption's baseline to the next staff's top line.
       If a note in `events` sits high enough to need ledger lines above the
       staff, the default clearance isn't enough -- the note (and its
       accidental, if any) would reach up into the caption above it."""
    base = gap * 1.5
    if not events:
        return base
    top_line = 4 * gap  # staff top relative to a staff_bottom_y of 0
    max_over, over_has_acc = 0.0, False
    for e in events:
        pitches = e.get('pitches') or ([e['pitch']] if 'pitch' in e else [])
        for p in pitches:
            cy = note_y(0, gap, p, clef=clef)
            over = cy - top_line
            if over > max_over:
                max_over, over_has_acc = over, bool(_parse_pitch(p)[1])
    if max_over <= 0:
        return base
    extra = max_over + (gap * 1.3 if over_has_acc else gap * 0.4)
    return max(base, extra)


def stars(level, total=4):
    return STAR_FULL * level + STAR_EMPTY * (total - level)


def exercises_header(c, kicker, subtitle_right):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    c.setFillColor(DARKGREEN)
    c.rect(0, H - 5, W, 5, fill=1, stroke=0)
    y = H - 32
    subtitle_w = stringWidth(subtitle_right, 'DejaVuSans', 8.8)
    kicker_avail_w = (W - MARGIN - subtitle_w - 14) - MARGIN
    kicker_text = kicker.upper()
    size = 8.8
    while size > 6.5 and stringWidth(kicker_text, 'DejaVuSans-Bold', size) > kicker_avail_w:
        size -= 0.2
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y, kicker_text)
    c.setFont('DejaVuSans', 8.8)
    c.setFillColor(GRAY)
    c.drawRightString(W - MARGIN, y, subtitle_right)
    y -= 22
    c.setFont('DejaVuSerif-Bold', 19)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Ficha de práctica al piano')
    return y - 20


def exercises_footer(c, page_num):
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(HexColor('#8A8A8A'))
    c.drawCentredString(W / 2, 22, 'El Cuaderno del Pianista · T-Clas')
    c.drawRightString(W - MARGIN, 22, str(page_num))


def exercise_heading(c, y, num, title, level, desc):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    c.setFillColor(DARKGREEN)
    c.roundRect(MARGIN, y - 17, 20, 20, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 10, y - 12.5, str(num))
    c.setFont('DejaVuSans', 12.5)
    c.setFillColor(GOLD)
    stars_w = stringWidth(stars(level), 'DejaVuSans', 12.5)
    c.drawRightString(W - MARGIN, y - 11.5, stars(level))
    title_avail_w = (W - MARGIN - stars_w - 10) - (MARGIN + 28)
    size = 11.8
    while size > 9.5 and stringWidth(title, 'DejaVuSans-Bold', size) > title_avail_w:
        size -= 0.3
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(INK)
    c.drawString(MARGIN + 28, y - 12, title)
    yy = wrap_text_common(c, desc, MARGIN + 28, y - 25, 'DejaVuSans', 8.9, CONTENT_W - 28, 11.8, color=GRAY)
    return yy


def wrap_text_common(c, text, x, y, font, size, max_w, leading, color):
    from reportlab.pdfbase.pdfmetrics import stringWidth
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


def system_caption(c, x, y, text):
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(DARKGREEN)
    c.drawString(x, y, text)


def system_block(c, x0, w0, y, gap, caption, events, clef='treble', time_sig=(4, 4)):
    """Draws a captioned staff system and returns the y just below it,
    already positioned for the *next* caption (safe, non-overlapping)."""
    system_caption(c, x0, y, caption)
    y -= before_staff(gap, events, clef)
    top, bot = draw_system(c, x0, y, w0, gap, events, clef=clef, time_sig=time_sig)
    return bot - after_system(gap)


def grand_staff_block(c, x0, w0, y_top, gap, treble_events, bass_events, caption, grand_gap_mult=7.3, time_sig=(4, 4)):
    """Draws a captioned two-stave (treble+bass) system, with the vertical gap
       between the staves verified wide enough to clear fingering numbers."""
    system_caption(c, x0, y_top, caption)
    yy = y_top - before_staff(gap, treble_events, 'treble')
    t_top, t_bot = draw_system(c, x0, yy, w0, gap, treble_events, clef='treble', time_sig=time_sig)
    yy2 = t_bot - gap * grand_gap_mult
    b_top, b_bot = draw_system(c, x0, yy2, w0, gap, bass_events, clef='bass', time_sig=time_sig)
    return b_bot - after_system(gap)
