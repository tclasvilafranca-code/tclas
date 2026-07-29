"""Mini motor de notacion musical para el Cuaderno del Pianista - T-Clas."""
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
import math

pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSerif', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSerif-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'))

DARKGREEN = HexColor('#3E5448')
CREAM = HexColor('#F5F1E6')
MAROON = HexColor('#7A2E35')
GOLD = HexColor('#B98A2E')
GRAY = HexColor('#333333')
LIGHTLINE = HexColor('#B8B2A2')
INK = HexColor('#1A1A1A')

# Generic diatonic step index, one step = half a line-gap
_LETTER_VAL = {'C':0,'D':1,'E':2,'F':3,'G':4,'A':5,'B':6}

def _parse_pitch(pitch):
    """Splits 'Bb4' / 'F#4' / 'C4' into (letter, accidental_or_None, octave)."""
    letter = pitch[0]
    rest = pitch[1:]
    accidental = None
    if rest and rest[0] in ('#', 'b'):
        accidental = rest[0]
        rest = rest[1:]
    octv = int(rest)
    return letter, accidental, octv

def _abs_idx(pitch):
    letter, _acc, octv = _parse_pitch(pitch)
    return octv * 7 + _LETTER_VAL[letter]

_TREBLE_REF = _abs_idx('E4')   # bottom line of treble staff
_BASS_REF = _abs_idx('G2')     # bottom line of bass staff
_ALTO_REF = _abs_idx('F3')     # bottom line of alto (Do) clef staff -- C4 sits on the middle line

def note_y(staff_bottom_y, gap, pitch, clef='treble'):
    ref = {'treble': _TREBLE_REF, 'bass': _BASS_REF}.get(clef, _ALTO_REF)
    idx = _abs_idx(pitch) - ref
    return staff_bottom_y + idx * (gap / 2.0)

def draw_staff(c, x, top_y, w, gap=9, lines=5):
    c.setStrokeColor(GRAY)
    c.setLineWidth(0.8)
    ys = []
    for i in range(lines):
        y = top_y - i * gap
        ys.append(y)
        c.line(x, y, x + w, y)
    return ys  # top to bottom

def draw_barline(c, x, top_y, bottom_y, thick=False, final=False):
    c.setStrokeColor(GRAY)
    if final:
        c.setLineWidth(1)
        c.line(x, top_y, x, bottom_y)
        c.setLineWidth(2.6)
        c.line(x + 4, top_y, x + 4, bottom_y)
    else:
        c.setLineWidth(1.1 if thick else 0.8)
        c.line(x, top_y, x, bottom_y)

pdfmetrics.registerFont(TTFont('FreeSerif', '/usr/share/fonts/truetype/freefont/FreeSerif.ttf'))

def draw_clef(c, x, staff_bottom_y, gap, clef='treble'):
    c.setFillColor(INK)
    if clef == 'treble':
        # Calibrated against the actual FreeSerif glyph outline (U+1D11E) so the
        # spiral "eye" lands exactly on the G4 line (2nd line from bottom).
        fsize = gap * 5.038
        baseline = staff_bottom_y + gap * 0.318
        c.setFont('FreeSerif', fsize)
        c.drawString(x, baseline, '\U0001D11E')
    elif clef == 'bass':
        # Calibrated so the two dots of the F-clef (U+1D122) straddle the F3 line.
        fsize = gap * 5.426
        baseline = staff_bottom_y - gap * 0.062
        c.setFont('FreeSerif', fsize)
        c.drawString(x, baseline, '\U0001D122')
    else:  # 'alto' / 'do' -- C-clef (U+1D121), calibrated so its waist sits on the given line
        fsize = gap * 7.23
        baseline = staff_bottom_y - gap * 0.714
        c.setFont('FreeSerif', fsize)
        c.drawString(x, baseline, '\U0001D121')

def draw_time_sig(c, x, staff_bottom_y, gap, top='4', bottom='4'):
    """Numeros centrados cada uno en su mitad del pentagrama: el de arriba
       entre la linea central y la linea superior, el de abajo entre la
       linea inferior y la central (offset ~0.3*gap para compensar que la
       altura visual de un digito es ~0.7x el tamano de fuente)."""
    c.setFont('DejaVuSans-Bold', gap * 2.0)
    c.setFillColor(INK)
    c.drawCentredString(x, staff_bottom_y + gap * 2.3, top)
    c.drawCentredString(x, staff_bottom_y + gap * 0.3, bottom)

# --- Armadura (key signature): sostenidos/bemoles dibujados UNA vez tras
#     la clave, en vez de repetir la alteracion en cada nota. -----------
SHARP_ORDER = ['F', 'C', 'G', 'D', 'A', 'E', 'B']
FLAT_ORDER = ['B', 'E', 'A', 'D', 'G', 'C', 'F']

# Posicion (letra+octava) de cada alteracion de la armadura, en el orden de
# SHARP_ORDER/FLAT_ORDER, para cada clave -- calculada para que caiga cerca
# del pentagrama (misma logica de note_y que ya usa el resto del motor: la
# octava no afecta la posicion salvo por el propio calculo de note_y).
_TREBLE_SHARP_POS = ['F5', 'C5', 'G5', 'D5', 'A4', 'E5', 'B4']
_TREBLE_FLAT_POS = ['B4', 'E5', 'A4', 'D5', 'G4', 'C5', 'F4']
_BASS_SHARP_POS = ['F3', 'C3', 'G3', 'D3', 'A2', 'E3', 'B2']
_BASS_FLAT_POS = ['B2', 'E3', 'A2', 'D3', 'G2', 'C3', 'F2']

# Armaduras usadas en el proyecto (tonalidad -> (tipo, nº de alteraciones)).
# Las tonalidades menores comparten armadura con su relativa mayor.
_KEY_SIGNATURES = {
    'Do mayor': ('', 0), 'La menor': ('', 0),
    'Sol mayor': ('#', 1), 'Mi menor': ('#', 1),
    'Re mayor': ('#', 2), 'Si menor': ('#', 2),
    'La mayor': ('#', 3), 'Fa# menor': ('#', 3), 'Fa sostenido menor': ('#', 3),
    'Mi mayor': ('#', 4), 'Do# menor': ('#', 4), 'Do sostenido menor': ('#', 4),
    'Fa mayor': ('b', 1), 'Re menor': ('b', 1),
    'Sib mayor': ('b', 2), 'Sol menor': ('b', 2),
    'Mib mayor': ('b', 3), 'Do menor': ('b', 3),
    'Lab mayor': ('b', 4), 'Fa menor': ('b', 4),
    'Re dórico': ('b', 1),  # armadura de Fa mayor (Re dorico es un modo relativo)
}


def get_key_signature(tonalidad):
    """tonalidad: string como 'Re mayor'. Devuelve (tipo, [letras en orden
       de impresion]) o ('', []) si no hay armadura o no se reconoce."""
    acc_type, n = _KEY_SIGNATURES.get(tonalidad, ('', 0))
    if not n:
        return '', []
    order = SHARP_ORDER if acc_type == '#' else FLAT_ORDER
    return acc_type, order[:n]


def draw_key_signature(c, x, staff_bottom_y, gap, clef, tonalidad):
    """Dibuja la armadura justo despues de la clave. Devuelve el cursor_x
       avanzado (igual a x si la tonalidad no tiene alteraciones)."""
    acc_type, letters = get_key_signature(tonalidad)
    if not letters:
        return x
    pos_table = {
        ('treble', '#'): _TREBLE_SHARP_POS, ('treble', 'b'): _TREBLE_FLAT_POS,
        ('bass', '#'): _BASS_SHARP_POS, ('bass', 'b'): _BASS_FLAT_POS,
    }.get((clef, acc_type))
    if pos_table is None:
        return x
    order = SHARP_ORDER if acc_type == '#' else FLAT_ORDER
    sym = '♯' if acc_type == '#' else '♭'
    dy = gap * 0.68 if acc_type == '#' else gap * 0.6
    c.setFont('DejaVuSans', gap * 1.85)
    c.setFillColor(INK)
    # El avance tiene que salir del ancho REAL del glifo: con un paso fijo de
    # 1.05*gap el simbolo es mas ancho que su hueco y la armadura se monta
    # encima del compas que viene detras.
    step = max(gap * 1.05, stringWidth(sym, 'DejaVuSans', gap * 1.85) * 0.95)
    cx = x
    for letter in letters:
        pos_pitch = pos_table[order.index(letter)]
        cy = note_y(staff_bottom_y, gap, pos_pitch, clef=clef)
        c.drawString(cx, cy - dy, sym)
        cx += step
    return cx + gap * 0.9


def draw_notehead(c, cx, cy, gap, filled=True):
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-18)
    rx, ry = gap * 0.62, gap * 0.44
    if filled:
        c.setFillColor(INK)
        c.setStrokeColor(INK)
        c.ellipse(-rx, -ry, rx, ry, fill=1, stroke=0)
    else:
        c.setStrokeColor(INK)
        c.setLineWidth(1.3)
        c.ellipse(-rx, -ry, rx, ry, fill=0, stroke=1)
    c.restoreState()

def draw_accidental(c, cx, cy, gap, accidental):
    sym = '\u266F' if accidental == '#' else '\u266D'
    c.setFont('DejaVuSans', gap * 1.85)
    c.setFillColor(INK)
    dy = gap * 0.68 if accidental == '#' else gap * 0.6
    c.drawRightString(cx - gap * 0.95, cy - dy, sym)

def draw_ledger(c, cx, cy, gap):
    c.setStrokeColor(GRAY)
    c.setLineWidth(0.8)
    c.line(cx - gap * 0.95, cy, cx + gap * 0.95, cy)

def ledger_lines_needed(staff_bottom_y, staff_top_y, cy, gap):
    lines = []
    if cy < staff_bottom_y - 1:
        y = staff_bottom_y - gap
        while y >= cy - 1:
            lines.append(y)
            y -= gap
    elif cy > staff_top_y + 1:
        y = staff_top_y + gap
        while y <= cy + 1:
            lines.append(y)
            y += gap
    return lines

def draw_rest(c, cx, staff_bottom_y, staff_top_y, gap, dur='q'):
    """Draws a rest symbol centred vertically in the staff."""
    mid = staff_bottom_y + 2 * gap
    c.setFillColor(INK)
    if dur == 'q':
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, mid - gap * 0.95, '\U0001D13D')
    elif dur == 'h':
        c.setFont('FreeSerif', gap * 2.2)
        c.drawCentredString(cx, mid - gap * 0.3, '\U0001D13C')
    elif dur == 'w':
        c.setFont('FreeSerif', gap * 2.2)
        c.drawCentredString(cx, mid + gap * 0.35, '\U0001D13B')
    elif dur == 'e':
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, mid - gap * 0.6, '\U0001D13E')

def draw_note(c, cx, staff_bottom_y, staff_top_y, gap, pitch, dur='q', stem_dir=None,
              number=None, label=None, beam_to=None, clef='treble', stem_end_y=None):
    """dur: 'q' quarter, 'h' half, 'w' whole, 'e' eighth (needs beam_to for beamed pair or flag alone)
       stem_end_y: if given (for beamed notes), the stem is drawn to exactly this y instead of
       the standard fixed-length stem, so every note in a beam reaches the same beam line."""
    cy = note_y(staff_bottom_y, gap, pitch, clef=clef)
    for ly in ledger_lines_needed(staff_bottom_y, staff_top_y, cy, gap):
        draw_ledger(c, cx, ly, gap)
    _letter, _acc, _oct = _parse_pitch(pitch)
    if _acc:
        draw_accidental(c, cx, cy, gap, _acc)
    filled = dur in ('q', 'e', 'q.', 'e.')
    draw_notehead(c, cx, cy, gap, filled=filled)
    if dur.endswith('.'):
        c.setFillColor(INK)
        c.circle(cx + gap * 1.05, cy + gap * 0.15, gap * 0.14, fill=1, stroke=0)
    stem_x_off = gap * 0.6
    if stem_dir is None:
        stem_dir = 'down' if cy > staff_bottom_y + 2 * gap else 'up'
    stem_len = gap * 3.4
    if dur != 'w':
        c.setStrokeColor(INK)
        c.setLineWidth(1.3)
        if stem_dir == 'up':
            sx = cx + stem_x_off
            stem_top = stem_end_y if stem_end_y is not None else cy + stem_len
            c.line(sx, cy, sx, stem_top)
        else:
            sx = cx - stem_x_off
            stem_top = stem_end_y if stem_end_y is not None else cy - stem_len
            c.line(sx, cy, sx, stem_top)
        if dur in ('e', 'e.') and beam_to is None:
            # curved flag (filled bezier, not a straight wedge)
            fx, fy = sx, stem_top
            c.setFillColor(INK)
            p = c.beginPath()
            if stem_dir == 'up':
                p.moveTo(fx, fy)
                p.curveTo(fx + gap * 0.15, fy - gap * 0.25, fx + gap * 0.95, fy - gap * 0.05,
                          fx + gap * 0.68, fy - gap * 1.25)
                p.curveTo(fx + gap * 0.62, fy - gap * 0.85, fx + gap * 0.22, fy - gap * 0.55,
                          fx, fy - gap * 0.35)
            else:
                p.moveTo(fx, fy)
                p.curveTo(fx + gap * 0.15, fy + gap * 0.25, fx + gap * 0.95, fy + gap * 0.05,
                          fx + gap * 0.68, fy + gap * 1.25)
                p.curveTo(fx + gap * 0.62, fy + gap * 0.85, fx + gap * 0.22, fy + gap * 0.55,
                          fx, fy + gap * 0.35)
            p.close()
            c.drawPath(p, fill=1, stroke=0)
    if number is not None:
        c.setFont('DejaVuSans-Bold', gap * 0.85)
        c.setFillColor(DARKGREEN)
        # a note near/above the top of the staff would otherwise push its
        # fingering number up into the caption drawn above the system --
        # cap how far above the staff top the number can rise
        ny = cy - gap * 1.55 if stem_dir == 'up' else min(cy + gap * 1.3, staff_top_y + gap * 0.6)
        c.drawCentredString(cx, ny, str(number))
    if label is not None:
        c.setFont('DejaVuSans', gap * 0.78)
        c.setFillColor(GRAY)
        ly2 = cy - gap * 1.55 if stem_dir == 'up' else min(cy + gap * 1.35, staff_top_y + gap * 0.6)
        if number is not None:
            ly2 -= gap * 0.95
        c.drawCentredString(cx, ly2, label)
    return cx, cy, stem_dir

def draw_chord(c, cx, staff_bottom_y, staff_top_y, gap, pitches, dur='h', clef='treble', label=None):
    """Draws a stacked block chord (all noteheads on one stem)."""
    cys = [note_y(staff_bottom_y, gap, p, clef=clef) for p in pitches]
    for cy in cys:
        for ly in ledger_lines_needed(staff_bottom_y, staff_top_y, cy, gap):
            draw_ledger(c, cx, ly, gap)
    # Two accidentals stacked close together (e.g. a 3rd or 4th apart) would
    # otherwise be drawn at the same x and their glyphs collide -- stagger
    # the lower one(s) further left, same as engraved notation does.
    acc_idx = [i for i, p in enumerate(pitches) if _parse_pitch(p)[1]]
    acc_idx.sort(key=lambda i: -cys[i])  # top to bottom
    stagger = {}
    last_cy = None
    level = 0
    for i in acc_idx:
        if last_cy is not None and (last_cy - cys[i]) < gap * 1.7:
            level += 1
        else:
            level = 0
        stagger[i] = level
        last_cy = cys[i]
    for i, (p, cy) in enumerate(zip(pitches, cys)):
        _letter, _acc, _oct = _parse_pitch(p)
        if _acc:
            draw_accidental(c, cx - stagger.get(i, 0) * gap * 1.05, cy, gap, _acc)
    filled = dur in ('q', 'q.')
    for cy in cys:
        draw_notehead(c, cx, cy, gap, filled=filled)
    if dur.endswith('.'):
        c.setFillColor(INK)
        for cy in cys:
            c.circle(cx + gap * 1.05, cy + gap * 0.15, gap * 0.14, fill=1, stroke=0)
    if dur != 'w':
        avg = sum(cys) / len(cys)
        stem_dir = 'down' if avg > staff_bottom_y + 2 * gap else 'up'
        c.setStrokeColor(INK)
        c.setLineWidth(1.3)
        if stem_dir == 'up':
            sx = cx + gap * 0.6
            c.line(sx, min(cys), sx, max(cys) + gap * 3.4)
        else:
            sx = cx - gap * 0.6
            # a down stem normally reaches min(cys) - gap*3.4, but that path
            # runs straight through the label drawn just below the chord --
            # stop it short of the label instead of slicing through the text
            stem_bottom = min(cys) - gap * 1.05 if label else min(cys) - gap * 3.4
            c.line(sx, max(cys), sx, stem_bottom)
    if label:
        c.setFont('DejaVuSans-Bold', gap * 0.85)
        c.setFillColor(DARKGREEN)
        # clear of the chord's lowest note AND of the staff itself -- a chord
        # whose lowest note sits inside/near the staff (e.g. a root note on
        # a middle line) would otherwise place the label on top of a staff line
        label_y = min(min(cys), staff_bottom_y) - gap * 1.6
        c.drawCentredString(cx, label_y, label)

def draw_beam(c, x1, y1, x2, y2, stem_dir='up', gap=9):
    c.setStrokeColor(INK)
    c.setLineWidth(3.2)
    c.line(x1, y1, x2, y2)

def draw_system(c, x, top_y, width, gap, events, clef='treble', time_sig=(4, 4),
                 show_clef=True, show_time=True, key_sig=None, spacing='linear'):
    """events: list of dicts with keys:
         pitch (str) OR pitches (list, for a chord)
         dur: 'w','h','q','e'
         number (fingering, optional), label (optional)
         beam (optional group id -- consecutive same-id eighth notes get a beam)
       key_sig: nombre de tonalidad (ej. 'Re mayor') -- si se da, dibuja la
         armadura tras la clave y las notas cuya alteracion coincide con la
         armadura se dibujan SIN el simbolo repetido (ya esta implicito).
       Draws one full-width staff system with proportionally spaced bar lines
       and returns (top_y, bottom_y) of the staff so systems can be stacked."""
    key_acc, key_letters_list = get_key_signature(key_sig) if key_sig else ('', [])
    key_letters = set(key_letters_list)

    def _disp(p):
        """Pitch a usar SOLO para decidir que dibujar (alteracion suprimida
           si ya la implica la armadura) -- la posicion en el pentagrama no
           depende de la alteracion, asi que esto no afecta el note_y."""
        if not key_acc:
            return p
        letter, acc, octv = _parse_pitch(p)
        if letter in key_letters and acc == key_acc:
            return f'{letter}{octv}'
        return p

    ys = draw_staff(c, x, top_y, width, gap=gap)
    top, bot = ys[0], ys[-1]
    cursor_x = x + 4
    if show_clef:
        draw_clef(c, cursor_x, bot, gap, clef=clef)
        cursor_x += gap * (5.4 if clef == 'treble' else 4.6)
    if key_sig:
        cursor_x = draw_key_signature(c, cursor_x, bot, gap, clef, key_sig)
    if show_time:
        # drawCentredString centers the numeral on cursor_x, so a two-digit
        # numerator/denominator (e.g. '12') extends further left than a
        # single digit and can collide with the clef glyph -- nudge right.
        extra_digits = max(len(str(time_sig[0])), len(str(time_sig[1]))) - 1
        cursor_x += gap * 0.85 * extra_digits
        draw_time_sig(c, cursor_x, bot, gap, top=str(time_sig[0]), bottom=str(time_sig[1]))
        cursor_x += gap * 3.0
    # If the very first event is a chord with several close-together
    # accidentals, draw_chord staggers them leftward (see draw_chord) so they
    # don't collide with each other -- make sure that leftmost column still
    # clears the time signature / clef instead of running into it.
    if events:
        first_pitches = events[0].get('pitches') or ([events[0]['pitch']] if 'pitch' in events[0] else [])
        acc_cys = sorted((note_y(bot, gap, p, clef=clef) for p in first_pitches if _parse_pitch(_disp(p))[1]), reverse=True)
        max_level, level, last_cy = 0, 0, None
        for cy in acc_cys:
            level = level + 1 if (last_cy is not None and last_cy - cy < gap * 1.7) else 0
            max_level = max(max_level, level)
            last_cy = cy
        cursor_x += max_level * gap * 1.05
    draw_barline(c, x, top, bot)

    dur_beats = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'q.': 1.5, 'h.': 3.0, 'e.': 0.75}
    beats_per_bar = time_sig[0] * (4.0 / time_sig[1])
    total_beats = sum(dur_beats[e['dur']] for e in events)
    raw_avail_w = (x + width - 8) - cursor_x

    # Interior bar-line beat positions (strictly before the end of the system)
    bar_beats = []
    bb = beats_per_bar
    while bb < total_beats - 1e-6:
        bar_beats.append(bb)
        bb += beats_per_bar

    # Reserve real horizontal space for each interior bar line so it never
    # lands exactly on top of a notehead (which starts the following bar).
    BAR_SLOT = gap * 1.7
    avail_w = raw_avail_w - len(bar_beats) * BAR_SLOT
    if avail_w < raw_avail_w * 0.4:  # safety floor for very short/busy systems
        avail_w = raw_avail_w * 0.4

    # Espaciado horizontal. 'linear' (por defecto) reparte el ancho en
    # proporcion directa a la duracion -- es lo que ha usado todo el material
    # anterior, y se conserva para no alterarlo. 'engraved' usa la convencion
    # real de grabado musical: el ancho crece con la RAIZ de la duracion
    # (duracion^0.6), de modo que una redonda ocupa ~2.3x una negra en vez de
    # 4x. Sin esto, los pasajes de notas largas quedan vacios y los de notas
    # cortas apelmazados.
    if spacing == 'engraved' and events:
        ws = [dur_beats[e['dur']] ** 0.6 for e in events]
        tw = sum(ws) or 1.0
        cum_beat, cum_w = [0.0], [0.0]
        for e, w in zip(events, ws):
            cum_beat.append(cum_beat[-1] + dur_beats[e['dur']])
            cum_w.append(cum_w[-1] + w)

        def _frac(beat_pos):
            for i in range(len(cum_beat) - 1):
                if cum_beat[i] - 1e-9 <= beat_pos <= cum_beat[i + 1] + 1e-9:
                    span = cum_beat[i + 1] - cum_beat[i]
                    t = 0.0 if span <= 0 else (beat_pos - cum_beat[i]) / span
                    return (cum_w[i] + t * (cum_w[i + 1] - cum_w[i])) / tw
            return beat_pos / total_beats if total_beats else 0.0
    else:
        def _frac(beat_pos):
            return beat_pos / total_beats if total_beats else 0.0

    def x_for_beat(beat_pos):
        n_bars_passed = sum(1 for bbeat in bar_beats if bbeat <= beat_pos + 1e-9)
        return cursor_x + _frac(beat_pos) * avail_w + n_bars_passed * BAR_SLOT

    positions = []
    beat_pos = 0.0
    for e in events:
        positions.append(x_for_beat(beat_pos))
        beat_pos += dur_beats[e['dur']]

    # A fingering number sits right under/over its note; if the very next
    # note carries an accidental and the two are packed close together (short
    # systems, e.g. the theory page's mini-staff), the accidental's glyph can
    # reach back and collide with that number. Nudge this note (and every
    # later one, so spacing stays monotonic) a little to the right.
    MIN_ACC_GAP = gap * 2.3
    for i in range(1, len(events)):
        if events[i - 1].get('number') is None:
            continue
        curr_pitches = events[i].get('pitches') or ([events[i]['pitch']] if 'pitch' in events[i] else [])
        if not any(_parse_pitch(_disp(p))[1] for p in curr_pitches):
            continue
        gap_here = positions[i] - positions[i - 1]
        if gap_here < MIN_ACC_GAP:
            delta = MIN_ACC_GAP - gap_here
            for k in range(i, len(positions)):
                positions[k] += delta

    # bar lines, centred in their own reserved slot (clear of the note after them)
    for bbeat in bar_beats:
        bx = x_for_beat(bbeat) - BAR_SLOT * 0.55
        draw_barline(c, bx, top, bot)

    # Pre-scan beam groups so every note sharing a beam uses ONE consistent
    # stem direction (otherwise a pair straddling the middle line would get
    # mismatched up/down stems that can't be joined by a single beam).
    group_cys = {}
    for e, px in zip(events, positions):
        beam_id = e.get('beam')
        if beam_id is not None and 'pitch' in e:
            cy = note_y(bot, gap, e['pitch'], clef=clef)
            group_cys.setdefault(beam_id, []).append(cy)
    group_stem_dir = {}
    group_beam_y = {}
    for gid, cys in group_cys.items():
        avg_cy = sum(cys) / len(cys)
        d = 'down' if avg_cy > bot + 2 * gap else 'up'
        group_stem_dir[gid] = d
        if d == 'up':
            group_beam_y[gid] = max(cy + gap * 3.4 for cy in cys)
        else:
            group_beam_y[gid] = min(cy - gap * 3.4 for cy in cys)

    # draw notes / chords, collecting beam groups
    beam_groups = {}
    for i, (px, e) in enumerate(zip(positions, events)):
        if e.get('rest'):
            draw_rest(c, px, bot, top, gap, dur=e['dur'])
        elif 'pitches' in e:
            draw_chord(c, px, bot, top, gap, [_disp(p) for p in e['pitches']], dur=e['dur'], clef=clef, label=e.get('label'))
        else:
            beam_id = e.get('beam')
            suppress_flag = beam_id is not None
            forced_dir = group_stem_dir.get(beam_id) if beam_id is not None else None
            stem_end = group_beam_y.get(beam_id) if beam_id is not None else None
            cx, cy, sd = draw_note(c, px, bot, top, gap, _disp(e['pitch']), dur=e['dur'],
                                    number=e.get('number'), label=e.get('label'),
                                    beam_to=True if suppress_flag else None, clef=clef,
                                    stem_dir=forced_dir, stem_end_y=stem_end)
            if beam_id is not None:
                beam_groups.setdefault(beam_id, []).append((px, cy, sd))

    for gid, pts in beam_groups.items():
        if len(pts) >= 2:
            sd = pts[0][2]
            stem_top = group_beam_y[gid]
            x_off = gap * 0.6 if sd == 'up' else -gap * 0.6
            x1 = pts[0][0] + x_off
            x2 = pts[-1][0] + x_off
            draw_beam(c, x1, stem_top, x2, stem_top, gap=gap)

    draw_barline(c, x + width, top, bot, final=True)
    return top, bot


def draw_write_target(c, x, staff_bottom_y, gap, label, box=False):
    """Draws just the note-name prompt below a blank staff position (no notehead
       drawn) so the student can write the note themselves."""
    c.setFont('DejaVuSans-Bold', gap * 0.8)
    c.setFillColor(DARKGREEN)
    c.drawCentredString(x, staff_bottom_y - gap * 2.5, label)
    if box:
        c.setStrokeColor(LIGHTLINE)
        c.setLineWidth(0.6)
        r = gap * 0.75
        c.circle(x, staff_bottom_y - gap * 1.6, r * 0.35, stroke=1, fill=0)


def draw_headless_note(c, cx, staff_bottom_y, staff_top_y, gap, pitch, clef='treble', number=None):
    """Draws just a notehead (no stem) at the correct pitch, for a 'draw the
       stem yourself' exercise. Returns (cx, cy) for reference."""
    cy = note_y(staff_bottom_y, gap, pitch, clef=clef)
    for ly in ledger_lines_needed(staff_bottom_y, staff_top_y, cy, gap):
        draw_ledger(c, cx, ly, gap)
    draw_notehead(c, cx, cy, gap, filled=True)
    if number:
        c.setFont('DejaVuSans', gap * 0.7)
        c.setFillColor(HexColor('#B9AE9A'))
        c.drawCentredString(cx, staff_bottom_y - gap * 2.6, str(number))
    return cx, cy


print("notation engine ready")
