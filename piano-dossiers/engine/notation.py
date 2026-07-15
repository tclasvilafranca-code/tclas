"""Mini motor de notacion musical para el Cuaderno del Pianista - T-Clas."""
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
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
    c.setFont('DejaVuSans-Bold', gap * 2.0)
    c.setFillColor(INK)
    c.drawCentredString(x, staff_bottom_y + gap * 1.6, top)
    c.drawCentredString(x, staff_bottom_y - gap * 0.15, bottom)

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
    c.setFont('DejaVuSans', gap * 1.35)
    c.setFillColor(INK)
    dy = gap * 0.42 if accidental == '#' else gap * 0.55
    c.drawRightString(cx - gap * 0.85, cy - dy, sym)

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
            # simple flag
            fx, fy = sx, stem_top
            c.setLineWidth(1.3)
            if stem_dir == 'up':
                c.line(fx, fy, fx + gap * 0.9, fy - gap * 0.9)
            else:
                c.line(fx, fy, fx + gap * 0.9, fy + gap * 0.9)
    if number is not None:
        c.setFont('DejaVuSans-Bold', gap * 0.85)
        c.setFillColor(DARKGREEN)
        ny = cy - gap * 1.55 if stem_dir == 'up' else cy + gap * 1.3
        c.drawCentredString(cx, ny, str(number))
    if label is not None:
        c.setFont('DejaVuSans', gap * 0.78)
        c.setFillColor(GRAY)
        ly2 = cy - gap * 1.55 if stem_dir == 'up' else cy + gap * 1.35
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
    for p, cy in zip(pitches, cys):
        _letter, _acc, _oct = _parse_pitch(p)
        if _acc:
            draw_accidental(c, cx, cy, gap, _acc)
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
            c.line(sx, max(cys), sx, min(cys) - gap * 3.4)
    if label:
        c.setFont('DejaVuSans-Bold', gap * 0.85)
        c.setFillColor(DARKGREEN)
        c.drawCentredString(cx, min(cys) - gap * 1.6, label)

def draw_beam(c, x1, y1, x2, y2, stem_dir='up', gap=9):
    c.setStrokeColor(INK)
    c.setLineWidth(3.2)
    c.line(x1, y1, x2, y2)

def draw_system(c, x, top_y, width, gap, events, clef='treble', time_sig=(4, 4),
                 show_clef=True, show_time=True):
    """events: list of dicts with keys:
         pitch (str) OR pitches (list, for a chord)
         dur: 'w','h','q','e'
         number (fingering, optional), label (optional)
         beam (optional group id -- consecutive same-id eighth notes get a beam)
       Draws one full-width staff system with proportionally spaced bar lines
       and returns (top_y, bottom_y) of the staff so systems can be stacked."""
    ys = draw_staff(c, x, top_y, width, gap=gap)
    top, bot = ys[0], ys[-1]
    cursor_x = x + 4
    if show_clef:
        draw_clef(c, cursor_x, bot, gap, clef=clef)
        cursor_x += gap * (5.4 if clef == 'treble' else 4.6)
    if show_time:
        draw_time_sig(c, cursor_x, bot, gap, top=str(time_sig[0]), bottom=str(time_sig[1]))
        cursor_x += gap * 3.0
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

    def x_for_beat(beat_pos):
        frac = beat_pos / total_beats if total_beats else 0
        n_bars_passed = sum(1 for bbeat in bar_beats if bbeat <= beat_pos + 1e-9)
        return cursor_x + frac * avail_w + n_bars_passed * BAR_SLOT

    positions = []
    beat_pos = 0.0
    for e in events:
        positions.append(x_for_beat(beat_pos))
        beat_pos += dur_beats[e['dur']]

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
            draw_chord(c, px, bot, top, gap, e['pitches'], dur=e['dur'], clef=clef, label=e.get('label'))
        else:
            beam_id = e.get('beam')
            suppress_flag = beam_id is not None
            forced_dir = group_stem_dir.get(beam_id) if beam_id is not None else None
            stem_end = group_beam_y.get(beam_id) if beam_id is not None else None
            cx, cy, sd = draw_note(c, px, bot, top, gap, e['pitch'], dur=e['dur'],
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
