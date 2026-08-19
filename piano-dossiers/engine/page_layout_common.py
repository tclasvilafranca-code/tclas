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


def after_system(gap, events=None, clef='treble'):
    """Vertical drop from a staff's bottom line to the next caption's baseline.
       A chord label is drawn below the chord's lowest note (see draw_chord);
       if that note also needs ledger lines below the staff, the default
       clearance isn't enough and the label collides with the next caption."""
    base = gap * 3.5
    if not events:
        return base
    max_under = 0.0
    for e in events:
        if not e.get('label'):
            continue
        pitches = e.get('pitches') or ([e['pitch']] if 'pitch' in e else [])
        if not pitches:
            continue
        lowest_cy = min(note_y(0, gap, p, clef=clef) for p in pitches)
        label_y = min(lowest_cy, 0) - gap * 1.6
        label_bottom = label_y - gap * 0.85 * 0.22
        under = -label_bottom
        if under > max_under:
            max_under = under
    # y lo mismo por abajo: una plica hacia abajo desde un acorde agudo baja
    # 3.4 gaps y se planta encima del rotulo del sistema siguiente.
    max_plica = 0.0
    for e in events:
        alc = _alcance(gap, e, clef)
        if alc is None:
            continue
        max_under = max(max_under, -alc[1])
        max_plica = max(max_plica, -alc[3])
    salida = base
    if max_under > 0:
        salida = max(salida, max_under + gap * 0.6)
    if max_plica > 0:
        salida = max(salida, max_plica + gap * 0.15)

    # El vocabulario de expresion tambien cuelga por debajo del pentagrama y
    # hay que reservarle sitio, o se planta encima del rotulo del sistema
    # siguiente: paso con el primer "sempre legato" que se dibujo.
    # El matiz (bot - 2.6 gaps) y el regulador (bot - 2.65) ya caben en el
    # hueco base de 3.5 gaps: no piden nada extra. El pedal y la ligadura si.
    if any(e.get('pedal') for e in events):
        # 'Ped.' apoya su linea base en bot - 4.4 gaps y no tiene descendentes:
        # con 5.0 va sobrado. Reservar 6.2 sacaba una pieza fuera de pagina.
        salida = max(salida, gap * 5.0)
    if any(e.get('lig') for e in events):
        # la ligadura arranca en la cabeza mas grave y se abre hasta 2.8 gaps
        bajo = 0.0
        for e in events:
            alc = _alcance(gap, e, clef)
            if alc is not None:
                bajo = min(bajo, alc[1])
        salida = max(salida, -bajo + gap * 3.4)
    return salida


STEM_LEN = 3.4          # el mismo valor que usan draw_note y draw_chord


def _alcance(gap, e, clef):
    """Hasta donde llega un evento, distinguiendo CABEZAS de PLICAS.
       Coordenadas relativas a staff_bottom_y = 0.

       Hay que mirar las dos cosas por separado porque piden holguras
       distintas: una cabeza fuera del pentagrama arrastra lineas adicionales
       y a veces una alteracion delante, y necesita aire; una plica es una
       raya de 1.3 pt y con que no toque basta.

       La plica no se puede ignorar: un acorde cuya nota mas grave esta muy
       por debajo del pentagrama lleva la plica hacia ARRIBA desde esa nota y
       acaba 3.4 gaps por encima de la mas aguda. Midiendo solo las cabezas,
       ese acorde parecia caber y la plica subia a atravesar el rotulo."""
    pitches = e.get('pitches') or ([e['pitch']] if 'pitch' in e else [])
    if not pitches:
        return None
    cys = [note_y(0, gap, p, clef=clef) for p in pitches]
    alto = plica_alto = max(cys)
    bajo = plica_bajo = min(cys)
    if e.get('dur') != 'w':
        if sum(cys) / len(cys) <= 2 * gap:           # misma regla que el motor
            plica_alto = max(cys) + gap * STEM_LEN
        else:
            plica_bajo = min(cys) - gap * STEM_LEN
    acc = any(_parse_pitch(p)[1] for p in pitches)
    return alto, bajo, plica_alto, plica_bajo, acc


def before_staff(gap, events=None, clef='treble'):
    """Vertical drop from a caption's baseline to the next staff's top line.
       If a note in `events` sits high enough to need ledger lines above the
       staff -- o si su plica sube por encima -- the default clearance isn't
       enough: the note (and its accidental, if any) would reach up into the
       caption above it."""
    base = gap * 1.5
    if not events:
        return base
    top_line = 4 * gap  # staff top relative to a staff_bottom_y of 0
    max_over, over_has_acc, max_plica = 0.0, False, 0.0
    for e in events:
        alc = _alcance(gap, e, clef)
        if alc is None:
            continue
        over = alc[0] - top_line
        if over > max_over:
            max_over, over_has_acc = over, alc[4]
        max_plica = max(max_plica, alc[2] - top_line)
    extra = base
    if max_over > 0:
        extra = max(extra, max_over + (gap * 1.3 if over_has_acc else gap * 0.4))
    if max_plica > 0:
        extra = max(extra, max_plica + gap * 0.15)
    return extra


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


# --- Bloques pedagogicos (Dosier Exhaustivo de Ejercicios de Piano por Nivel) ---
# Bloques 5 (juegos) y 7 (creatividad) se descartaron por decision del cliente.
BLOQUE_COLOR = {
    1: HexColor('#6B7A8F'), 2: DARKGREEN, 3: HexColor('#3E6E8F'),
    4: GOLD, 6: MAROON,
}
BLOQUE_NOMBRE = {
    1: 'Calentamiento físico', 2: 'Técnica al piano', 3: 'Lectura, ritmo e interpretación',
    4: 'Entrenamiento auditivo', 6: 'Teoría y dictado',
}


def bloque_heading(c, y, num, desc, extra=''):
    """Cabecera de bloque pedagogico: badge numerado de color propio + nombre
       fijo del bloque (igual en todos los alumnos/canciones, para que el
       alumno reconozca siempre el mismo bloque) + descripcion especifica de
       esta cancion."""
    from reportlab.pdfbase.pdfmetrics import stringWidth
    color = BLOQUE_COLOR[num]
    nombre = BLOQUE_NOMBRE[num]
    c.setFillColor(color)
    c.roundRect(MARGIN, y - 19, 23, 23, 4, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 11.5)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 11.5, y - 14, str(num))
    c.setFont('DejaVuSans-Bold', 11.3)
    c.setFillColor(INK)
    titulo = f'Bloque {num} · {nombre}' + (f' — {extra}' if extra else '')
    size = 11.3
    while size > 8.8 and stringWidth(titulo, 'DejaVuSans-Bold', size) > CONTENT_W - 31:
        size -= 0.3
    c.setFont('DejaVuSans-Bold', size)
    c.drawString(MARGIN + 31, y - 13.5, titulo)
    yy = wrap_text_common(c, desc, MARGIN + 31, y - 26, 'DejaVuSans', 8.5, CONTENT_W - 31, 11.3, color=GRAY)
    return yy - 3


def bullet_list(c, y, items, x0=MARGIN, w=CONTENT_W, font_size=8.7, leading=11.6, color=INK, dot_color=None):
    for item in items:
        c.setFillColor(dot_color or INK)
        c.circle(x0 + 2.3, y - 3.2, 1.5, fill=1, stroke=0)
        y = wrap_text_common(c, item, x0 + 11, y, 'DejaVuSans', font_size, w - 11, leading, color=color)
        y -= 2.5
    return y


def bullet_list_2col(c, y, items, x0=MARGIN, w=CONTENT_W, font_size=8.7, leading=11.6, dot_color=None):
    half = (len(items) + 1) // 2
    col_w = (w - 22) / 2
    y_left = bullet_list(c, y, items[:half], x0=x0, w=col_w, font_size=font_size, leading=leading, dot_color=dot_color)
    y_right = bullet_list(c, y, items[half:], x0=x0 + col_w + 22, w=col_w, font_size=font_size, leading=leading, dot_color=dot_color)
    return min(y_left, y_right)


def nota_estilo(c, y, texto, height=32, label=None):
    """Caja destacada para una nota transversal (categorias A-H del dosier:
       ergonomia, estrategia de estudio, estilo historico, etc.)."""
    c.setFillColor(HexColor('#F4EFE3'))
    c.roundRect(MARGIN, y - height, CONTENT_W, height, 5, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(MARGIN, y - height, 3, height, fill=1, stroke=0)
    txt = f'{label}: {texto}' if label else texto
    wrap_text_common(c, txt, MARGIN + 12, y - 12, 'DejaVuSans', 8.2, CONTENT_W - 24, 11.0, color=HexColor('#5A4A20'))
    return y - height - 8


def answer_box_row(c, x0, y, n_boxes, box_w, box_h=15, gap=6):
    """Fila de casillas en blanco (p.ej. para digitacion, nombres de nota o
       grados I/IV/V que el alumno rellena a mano)."""
    c.setStrokeColor(LIGHTLINE)
    c.setLineWidth(0.7)
    x = x0
    for _ in range(n_boxes):
        c.roundRect(x, y - box_h, box_w, box_h, 2, fill=0, stroke=1)
        x += box_w + gap
    return y - box_h


def blank_staff(c, x, top_y, width, gap, clef='treble', time_sig=(4, 4), n_bars=2):
    """Pentagrama vacio (clave + compas + compases marcados, sin notas) para
       un dictado ritmico o de notas: el alumno escribe encima lo que
       escucha."""
    ys = draw_staff(c, x, top_y, width, gap=gap)
    top, bot = ys[0], ys[-1]
    cursor_x = x + 4
    draw_clef(c, cursor_x, bot, gap, clef=clef)
    cursor_x += gap * (5.4 if clef == 'treble' else 4.6)
    draw_time_sig(c, cursor_x, bot, gap, top=str(time_sig[0]), bottom=str(time_sig[1]))
    cursor_x += gap * 3.0
    draw_barline(c, x, top, bot)
    avail_w = (x + width - 8) - cursor_x
    for i in range(1, n_bars):
        draw_barline(c, cursor_x + avail_w * i / n_bars, top, bot)
    draw_barline(c, x + width - 4, top, bot, final=True)
    return top, bot


def system_block(c, x0, w0, y, gap, caption, events, clef='treble', time_sig=(4, 4), key_sig=None,
                  show_time=True):
    """Draws a captioned staff system and returns the y just below it,
    already positioned for the *next* caption (safe, non-overlapping).
    key_sig: nombre de tonalidad (ej. 'Re mayor') para dibujar la armadura
    real en vez de repetir la alteracion en cada nota."""
    system_caption(c, x0, y, caption)
    y -= before_staff(gap, events, clef)
    top, bot = draw_system(c, x0, y, w0, gap, events, clef=clef, time_sig=time_sig,
                            key_sig=key_sig, show_time=show_time)
    return bot - after_system(gap, events, clef)


def multi_system_block(c, x0, w0, y, gap, caption, events, clef='treble', time_sig=(4, 4),
                        key_sig=None, bars_per_line=4, line_gap_mult=1.9, spacing='linear'):
    """Como system_block, pero reparte una frase larga en VARIAS lineas de
       pentagrama (como una partitura real) en vez de un unico sistema muy
       denso. Una sola clave/armadura+compas al inicio de cada linea (el
       compas solo se repite en la primera, como en una partitura real).
       bars_per_line: cuantos compases caben en cada linea."""
    dur_beats = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'q.': 1.5, 'h.': 3.0, 'e.': 0.75}
    beats_per_bar = time_sig[0] * (4.0 / time_sig[1])
    line_beats = beats_per_bar * bars_per_line

    lines, current, current_beats = [], [], 0.0
    for e in events:
        current.append(e)
        current_beats += dur_beats[e['dur']]
        if current_beats >= line_beats - 1e-6:
            lines.append(current)
            current, current_beats = [], 0.0
    if current:
        lines.append(current)

    system_caption(c, x0, y, caption)
    y -= before_staff(gap, lines[0], clef)
    for i, line_events in enumerate(lines):
        top, bot = draw_system(c, x0, y, w0, gap, line_events, clef=clef, time_sig=time_sig,
                                key_sig=key_sig, show_time=(i == 0), spacing=spacing)
        last = i == len(lines) - 1
        y = bot - (after_system(gap, line_events, clef) if last else gap * line_gap_mult)
    return y


def multi_grand_staff_block(c, x0, w0, y, gap, treble_events, bass_events, caption, grand_gap_mult=6.6,
                             time_sig=(4, 4), key_sig=None, bars_per_line=4, line_gap_mult=2.0):
    """Como multi_system_block, pero para un pentagrama DOBLE (sol+fa juntos,
       como una pagina de partitura de piano real): reparte una pieza larga
       en varias lineas, cada linea con su propio sol+fa. Una sola
       clave/armadura+compas al inicio de cada linea (el compas solo se
       repite en la primera). treble_events y bass_events deben sumar el
       mismo numero total de tiempos, y bars_per_line debe repartirlos en
       el mismo numero de compases por linea en ambas claves."""
    dur_beats = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'q.': 1.5, 'h.': 3.0, 'e.': 0.75}
    beats_per_bar = time_sig[0] * (4.0 / time_sig[1])
    line_beats = beats_per_bar * bars_per_line

    def _split(events):
        lines, current, current_beats = [], [], 0.0
        for e in events:
            current.append(e)
            current_beats += dur_beats[e['dur']]
            if current_beats >= line_beats - 1e-6:
                lines.append(current)
                current, current_beats = [], 0.0
        if current:
            lines.append(current)
        return lines

    treble_lines = _split(treble_events)
    bass_lines = _split(bass_events)
    n_lines = max(len(treble_lines), len(bass_lines))

    system_caption(c, x0, y, caption)
    y -= before_staff(gap, treble_lines[0] if treble_lines else None, 'treble')
    for i in range(n_lines):
        t_events = treble_lines[i] if i < len(treble_lines) else []
        b_events = bass_lines[i] if i < len(bass_lines) else []
        t_top, t_bot = draw_system(c, x0, y, w0, gap, t_events, clef='treble', time_sig=time_sig,
                                    key_sig=key_sig, show_time=(i == 0))
        yy2 = t_bot - gap * grand_gap_mult
        b_top, b_bot = draw_system(c, x0, yy2, w0, gap, b_events, clef='bass', time_sig=time_sig,
                                    key_sig=key_sig, show_time=(i == 0))
        last = i == n_lines - 1
        y = b_bot - (after_system(gap, b_events, 'bass') if last else gap * line_gap_mult)
    return y


def grand_staff_block(c, x0, w0, y_top, gap, treble_events, bass_events, caption, grand_gap_mult=7.3,
                       time_sig=(4, 4), key_sig=None):
    """Draws a captioned two-stave (treble+bass) system, with the vertical gap
       between the staves verified wide enough to clear fingering numbers."""
    system_caption(c, x0, y_top, caption)
    yy = y_top - before_staff(gap, treble_events, 'treble')
    t_top, t_bot = draw_system(c, x0, yy, w0, gap, treble_events, clef='treble', time_sig=time_sig, key_sig=key_sig)
    yy2 = t_bot - gap * grand_gap_mult
    b_top, b_bot = draw_system(c, x0, yy2, w0, gap, bass_events, clef='bass', time_sig=time_sig, key_sig=key_sig)
    return b_bot - after_system(gap, bass_events, 'bass')
