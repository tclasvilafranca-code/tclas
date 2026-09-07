# -*- coding: utf-8 -*-
"""Generador de teoria PARAMETRIZADO: cada cancion solo aporta un diccionario
   de datos; el diseno (verificado) es siempre el mismo."""
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import *

W, H = 595.276, 841.89
MARGIN = 46
CONTENT_W = W - 2 * MARGIN


def badge(c, x, y, text, w=17, h=17, bg=DARKGREEN, fg=white, fsize=9.2):
    c.setFillColor(bg)
    c.roundRect(x, y - h, w, h, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', fsize)
    c.setFillColor(fg)
    c.drawCentredString(x + w / 2, y - h + (h - fsize) / 2 + 1.5, text)


def _count_wrapped_lines(text, font, size, max_w):
    words = text.split(' ')
    line = ''
    n = 1
    for w in words:
        test = (line + ' ' + w).strip()
        if stringWidth(test, font, size) <= max_w:
            line = test
        else:
            n += 1
            line = w
    return n


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


def draw_keyboard(c, x, y_top, width, white_notes, highlight_idx=0, key_h=38):
    n = len(white_notes)
    key_w = width / n
    for i, note in enumerate(white_notes):
        kx = x + i * key_w
        is_home = (i == highlight_idx)
        c.setFillColor(HexColor('#EDE6D6') if is_home else white)
        c.setStrokeColor(GRAY)
        c.setLineWidth(0.8)
        c.rect(kx, y_top - key_h, key_w, key_h, fill=1, stroke=1)
        c.setFont('DejaVuSans-Bold' if is_home else 'DejaVuSans', 7.6)
        c.setFillColor(DARKGREEN if is_home else GRAY)
        c.drawCentredString(kx + key_w / 2, y_top - key_h + 6, note)
    return y_top - key_h


def build_theory_page(c, qr_path, song):
    """song is a dict with keys:
       num, title, subtitle, tonalidad, compas, tempo, forma, dificultad, manos,
       la_cancion, notas_texto (opcional, default estandar), difficult_cc,
       difficult_title, reto, truco, sabias_que, mini_staff_events (list of
       (pitch, finger_or_None) tuples using 'h' on the last as a half note),
       time_sig (default (4,4))
    """
    c.setFillColor(DARKGREEN)
    c.rect(0, H - 5, W, 5, fill=1, stroke=0)

    y = H - 34
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y, song.get('nivel_kicker', 'NIVEL 1 · EMPIEZO'))
    c.setFont('DejaVuSans', 8.6)
    c.setFillColor(GRAY)
    total_songs = song.get('total_songs', 20)
    c.drawRightString(W - MARGIN, y, f"Canción {song['num']} de {total_songs}")

    y -= 22
    title_avail_w = (W - MARGIN - 62 - 10) - MARGIN  # 62 == qr_size, defined just below
    title_size = 21
    while title_size > 13.5 and stringWidth(song['title'], 'DejaVuSerif-Bold', title_size) > title_avail_w:
        title_size -= 0.5
    c.setFont('DejaVuSerif-Bold', title_size)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, song['title'])
    c.setFont('DejaVuSans', 9.3)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y - 15, song['subtitle'] + '  ·  Partitura, teoría y taller de práctica')

    qr_size = 62
    qr_x = W - MARGIN - qr_size
    qr_y = y - 15 - 8
    c.drawImage(qr_path, qr_x, qr_y - qr_size, qr_size, qr_size, mask='auto')
    c.setFont('DejaVuSans-Bold', 7.3)
    c.setFillColor(DARKGREEN)
    c.drawRightString(qr_x + qr_size, qr_y - qr_size - 10, '\u266A Escúchala')
    c.setFont('DejaVuSans', 6.6)
    c.setFillColor(GRAY)
    c.drawRightString(qr_x + qr_size, qr_y - qr_size - 19, 'antes de tocar')
    qr_bottom = qr_y - qr_size - 19 - 6

    y -= 40
    y -= 12
    cols = [('TONALIDAD', song['tonalidad'], 1.05), ('COMPÁS', song['compas'], 0.55),
            ('TEMPO', song['tempo'], 1.3), ('FORMA', song['forma'], 1.15),
            ('DIFICULTAD', song['dificultad'], 1.35), ('MANOS', song['manos'], 1.35)]
    table_w = CONTENT_W - (qr_size + 14)
    weight_total = sum(w for _, _, w in cols)
    col_ws = [table_w * w / weight_total for _, _, w in cols]
    c.setStrokeColor(LIGHTLINE)
    c.setLineWidth(0.7)
    c.line(MARGIN, y, MARGIN + table_w, y)
    cy = y - 12
    cx = MARGIN
    for (lab, val, _w), col_w in zip(cols, col_ws):
        avail_w = col_w - 6
        c.setFont('DejaVuSans-Bold', 6.1)
        c.setFillColor(DARKGREEN)
        c.drawString(cx, cy, lab)
        size = 7.5
        while size > 5.2 and stringWidth(val, 'DejaVuSans-Bold', size) > avail_w:
            size -= 0.3
        shown = val
        while stringWidth(shown, 'DejaVuSans-Bold', size) > avail_w and len(shown) > 3:
            shown = shown[:-2]
        if shown != val:
            shown = shown.rstrip() + '…'
        c.setFont('DejaVuSans-Bold', size)
        c.setFillColor(INK)
        c.drawString(cx, cy - 11, shown)
        cx += col_w
    y = cy - 22
    c.setStrokeColor(LIGHTLINE)
    c.line(MARGIN, y, MARGIN + CONTENT_W, y)
    y -= 16
    y = min(y, qr_bottom - 14)

    col_gap = 18
    col_w2 = (CONTENT_W - col_gap) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w2 + col_gap
    ytop = y

    # ---------------- LEFT COLUMN ----------------
    ly = ytop
    badge(c, left_x, ly, 'I', fsize=9.0)
    c.setFont('DejaVuSans-Bold', 12.2)
    c.setFillColor(INK)
    c.drawString(left_x + 26, ly - 13, 'La canción')
    ly -= 27
    ly = wrap_text(c, song['la_cancion'], left_x, ly, 'DejaVuSans', 10.1, col_w2, 14.2)
    ly -= 14

    badge(c, left_x, ly, 'II', fsize=9.0)
    c.setFont('DejaVuSans-Bold', 12.2)
    c.setFillColor(INK)
    c.drawString(left_x + 26, ly - 13, 'Lo que aprendes')
    ly -= 27
    tonic = song.get('tonic_solfege', 'Do')
    quinta = song.get('quinta_solfege', 'Sol')
    ly = wrap_text(c, song.get('tonalidad_texto',
                      f'Tu tonalidad: {tonic.upper()}. La nota {tonic.upper()} es la "casa" y la 5ª ({quinta.upper()}) es el "imán" que tira '
                      f'para volver. En {song["tonalidad"]} todo son teclas blancas.'),
                   left_x, ly, 'DejaVuSans', 10.1, col_w2, 14.2)
    ly -= 14
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(DARKGREEN)
    c.drawString(left_x, ly, 'Las notas que usas en el teclado:')
    ly -= 16
    kb_notes = song.get('keyboard_notes', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'])
    kb_idx = song.get('keyboard_highlight', 0)
    ly = draw_keyboard(c, left_x, ly, col_w2, kb_notes, highlight_idx=kb_idx, key_h=38)
    ly -= 14
    ritmo_txt = song.get('ritmo_texto', f"Ritmo: compás de {song['compas']} — cuenta hasta el compás con regularidad.")
    ly = wrap_text(c, ritmo_txt, left_x, ly, 'DejaVuSans', 10.1, col_w2, 14.2)
    ly -= 12

    badge(c, left_x, ly, 'VI', fsize=8.6)
    c.setFont('DejaVuSans-Bold', 12.2)
    c.setFillColor(INK)
    c.drawString(left_x + 26, ly - 13, 'Cómo suena')
    ly -= 27
    ly = wrap_text(c, 'Tócala despacio y contento. Mejor lento y sin fallos que rápido y con tropiezos. ¡Disfruta!',
                   left_x, ly, 'DejaVuSans', 10.1, col_w2, 14.2)
    ly -= 12

    badge(c, left_x, ly, 'VII', fsize=8.2)
    c.setFont('DejaVuSans-Bold', 12.2)
    c.setFillColor(INK)
    c.drawString(left_x + 26, ly - 13, 'Lo que consigo')
    ly -= 26
    items = song.get('checklist_items', [
             f'Encuentro {tonic.upper()} y pongo bien los dedos.', 'Toco la melodía con la mano derecha.',
             'Hago los acordes con la izquierda.', 'Junto las dos manos despacio.'])
    checklist_w = col_w2 - 17
    for it in items:
        c.setStrokeColor(DARKGREEN)
        c.setLineWidth(1.0)
        c.rect(left_x + 2, ly - 8, 9, 9, fill=0, stroke=1)
        n_lines = _count_wrapped_lines(it, 'DejaVuSans', 9.7, checklist_w)
        wrap_text(c, it, left_x + 17, ly - 7, 'DejaVuSans', 9.7, checklist_w, 12.6, color=INK)
        ly -= 19 if n_lines <= 1 else 19 + (n_lines - 1) * 12.6
    ly -= 4
    c.setFont('DejaVuSans-Bold', 9.2)
    c.setFillColor(MAROON)
    ly = wrap_text(c, 'Meta de hoy: tocar el principio con las dos manos, ¡sin prisa!',
                   left_x, ly, 'DejaVuSans-Bold', 9.2, col_w2, 12.4)

    # ---------------- RIGHT COLUMN ----------------
    ry = ytop
    badge(c, right_x, ry, 'III', fsize=8.2)
    c.setFont('DejaVuSans-Bold', 12.2)
    c.setFillColor(INK)
    c.drawString(right_x + 26, ry - 13, song.get('posicion_titulo', 'A tocar — posición de Do'))
    ry -= 30
    gap = 8.4
    top_y, bot_y = draw_system(c, right_x, ry, col_w2, gap, song['mini_staff_events'],
                                clef='treble', time_sig=song.get('time_sig', (4, 4)))
    ry = bot_y - gap * 3.9  # extra clearance: a low note's fingering number can reach well below the staff
    ry = wrap_text(c, song.get('posicion_texto',
                      f'Mano derecha en posición de {tonic.upper()} (un dedo por tecla); izquierda: acordes {tonic.upper()}, FA y SOL.'),
                   right_x, ry, 'DejaVuSans', 9.8, col_w2 - 6, 13.6)
    ry -= 14

    badge(c, right_x, ry, 'IV', fsize=8.6)
    c.setFont('DejaVuSans-Bold', 12.2)
    c.setFillColor(INK)
    c.drawString(right_x + 26, ry - 13, 'Cómo estudiar')
    ry -= 26
    steps = song.get('estudiar_steps', [
             f'Busca {tonic.upper()} y tócala 3 veces (tu nota casa).',
             'Mano derecha sola, muy despacio. ♩=60',
             'Los acordes con la izquierda, uno por compás.',
             'Las dos manos juntas: lento primero, luego un poco más rápido.'])
    step_text_w = col_w2 - 24
    for i, s in enumerate(steps, 1):
        c.setFillColor(DARKGREEN)
        c.circle(right_x + 6, ry - 5, 6.2, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(white)
        c.drawCentredString(right_x + 6, ry - 7.7, str(i))
        yy = wrap_text(c, s, right_x + 18, ry - 7, 'DejaVuSans', 10.0, step_text_w, 12.4, color=INK)
        consumed = (ry - 7) - yy + 12.4
        ry -= max(19.5, consumed + 5)
    ry -= 8

    badge(c, right_x, ry, 'V', fsize=9.0)
    c.setFont('DejaVuSans-Bold', 12.2)
    c.setFillColor(INK)
    c.drawString(right_x + 26, ry - 13, 'La parte difícil')
    ry -= 28
    reto_lines = _count_wrapped_lines('El reto: ' + song['reto'], 'DejaVuSans', 8.4, col_w2 - 20)
    truco_lines = _count_wrapped_lines('El truco: ' + song['truco'], 'DejaVuSans', 8.4, col_w2 - 20)
    box_h = 29 + (reto_lines + truco_lines) * 11.6 + 6
    c.setFillColor(HexColor('#F6ECEC'))
    c.setStrokeColor(MAROON)
    c.setLineWidth(0.8)
    c.roundRect(right_x, ry - box_h, col_w2, box_h, 6, fill=1, stroke=1)
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(MAROON)
    c.drawString(right_x + 10, ry - 15, f"{song['difficult_cc']} · {song['difficult_title']}")
    yb = wrap_text(c, 'El reto: ' + song['reto'], right_x + 10, ry - 29, 'DejaVuSans', 8.4, col_w2 - 20, 11.6, color=INK)
    wrap_text(c, 'El truco: ' + song['truco'], right_x + 10, yb - 3, 'DejaVuSans', 8.4, col_w2 - 20, 11.6, color=INK)
    ry -= box_h + 18

    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(DARKGREEN)
    c.drawString(right_x, ry, '¿Sabías que…?')
    ry -= 15
    ry = wrap_text(c, song['sabias_que'], right_x, ry, 'DejaVuSans', 9.3, col_w2 - 6, 12.8)

    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(HexColor('#8A8A8A'))
    c.drawCentredString(W / 2, 22, 'El Cuaderno del Pianista · T-Clas')
