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
    """Parte 'Bb4' / 'F#4' / 'An4' / 'C4' en (letra, alteracion, octava).

       'n' es el BECUADRO. Hace falta en cualquier pieza con alteraciones
       contra la armadura (el La natural de un Cm/A en Mi bemol mayor, por
       ejemplo): sin el, esa nota se escribe mal y suena mal."""
    letter = pitch[0]
    rest = pitch[1:]
    accidental = None
    if rest and rest[0] in ('#', 'b', 'n'):
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
        # proporcional al tamano: con 1.3 fijo, una cabeza dibujada a tamano de
        # carta (gap 20) sale con un contorno de pelo. En el cuaderno el gap es
        # 7-9 y max() devuelve 1.3 exacto, asi que no cambia ni una pagina.
        c.setLineWidth(max(1.3, gap * 0.13))
        c.ellipse(-rx, -ry, rx, ry, fill=0, stroke=1)
    c.restoreState()

def draw_accidental(c, cx, cy, gap, accidental):
    sym = {'#': '\u266F', 'b': '\u266D', 'n': '\u266E'}[accidental]
    c.setFont('DejaVuSans', gap * 1.85)
    c.setFillColor(INK)
    dy = gap * 0.68 if accidental in ('#', 'n') else gap * 0.6
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
    """Draws a rest symbol centred vertically in the staff.

       El puntillo va SIEMPRE a la derecha del simbolo y a la altura del tercer
       espacio, como en cualquier edicion. Antes las duraciones con puntillo
       ('h.', 'q.', 'e.') no entraban en ninguna rama y la funcion no dibujaba
       NADA: quedaba un hueco en blanco en el compas y el auditor lo daba por
       bueno porque si le contaba los tiempos. Salieron 20 casos ya impresos."""
    mid = staff_bottom_y + 2 * gap
    base = dur.rstrip('.')
    puntillos = len(dur) - len(base)
    c.setFillColor(INK)
    if base == 'q':
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, mid - gap * 0.95, '\U0001D13D')
    elif base in ('h', 'w'):
        # El silencio de blanca SE APOYA sobre la linea del medio y el de
        # redonda CUELGA de la cuarta linea. Son rectangulos, no glifos: los
        # de FreeSerif salian de 0.2 espacios de grueso (un guion casi
        # invisible) y encima colocados un espacio arriba de donde van, o sea
        # el silencio de blanca en el sitio del de redonda.
        w = gap * 1.15
        h = gap * 0.5
        y0 = mid if base == 'h' else mid + gap - h
        c.rect(cx - w / 2.0, y0, w, h, fill=1, stroke=0)
    elif base == 'e':
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, mid - gap * 0.6, '\U0001D13E')
    elif base == 's':
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, mid - gap * 0.6, '\U0001D13F')
    # Uno o DOS puntillos. El segundo va justo detras del primero y a la misma
    # altura, como en cualquier edicion: no es un adorno, cambia la duracion
    # (ver DUR_BEATS), y el Gladiator de Aida abre con un silencio de corchea
    # con puntillo y una negra con DOBLE puntillo.
    c.setFillColor(INK)
    for k in range(puntillos):
        c.circle(cx + gap * (0.85 + 0.42 * k), mid + gap * 0.5, gap * 0.14,
                 fill=1, stroke=0)

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
    filled = dur.rstrip('.') in ('q', 'e', 's')
    draw_notehead(c, cx, cy, gap, filled=filled)
    c.setFillColor(INK)
    for _k in range(len(dur) - len(dur.rstrip('.'))):
        c.circle(cx + gap * (1.05 + 0.42 * _k), cy + gap * 0.15, gap * 0.14,
                 fill=1, stroke=0)
    stem_x_off = gap * 0.6
    if stem_dir is None:
        stem_dir = 'down' if cy > staff_bottom_y + 2 * gap else 'up'
    stem_len = gap * 3.4
    # Ni la redonda ni la redonda con puntillo llevan plica. La comparacion
    # tiene que ser contra la figura BASE: con `dur != 'w'` a secas, la 'w.'
    # salia con plica, que no existe en ninguna edicion.
    if dur.rstrip('.') != 'w':
        c.setStrokeColor(INK)
        c.setLineWidth(max(1.3, gap * 0.115))
        if stem_dir == 'up':
            sx = cx + stem_x_off
            stem_top = stem_end_y if stem_end_y is not None else cy + stem_len
            c.line(sx, cy, sx, stem_top)
        else:
            sx = cx - stem_x_off
            stem_top = stem_end_y if stem_end_y is not None else cy - stem_len
            c.line(sx, cy, sx, stem_top)
        if dur.rstrip('.') in ('e', 's') and beam_to is None:
            # curved flag (filled bezier, not a straight wedge). La semicorchea
            # lleva DOS corchetes: el segundo cuelga un espacio mas abajo (o mas
            # arriba, si la plica va hacia abajo), que es como se graba de verdad.
            n_flags = 2 if dur.rstrip('.') == 's' else 1
            for k in range(n_flags):
                off = k * gap * 0.9 * (-1 if stem_dir == 'up' else 1)
                fx, fy = sx, stem_top + off
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
    filled = dur.rstrip('.') in ('q', 'e', 's')
    for cy in cys:
        draw_notehead(c, cx, cy, gap, filled=filled)
    c.setFillColor(INK)
    for _k in range(len(dur) - len(dur.rstrip('.'))):
        for cy in cys:
            c.circle(cx + gap * (1.05 + 0.42 * _k), cy + gap * 0.15, gap * 0.14,
                     fill=1, stroke=0)
    if dur.rstrip('.') != 'w':
        avg = sum(cys) / len(cys)
        stem_dir = 'down' if avg > staff_bottom_y + 2 * gap else 'up'
        c.setStrokeColor(INK)
        c.setLineWidth(1.3)
        if stem_dir == 'up':
            sx = cx + gap * 0.6
            stem_top = max(cys) + gap * 3.4
            c.line(sx, min(cys), sx, stem_top)
        else:
            sx = cx - gap * 0.6
            # a down stem normally reaches min(cys) - gap*3.4, but that path
            # runs straight through the label drawn just below the chord --
            # stop it short of the label instead of slicing through the text
            stem_top = min(cys) - gap * 1.05 if label else min(cys) - gap * 3.4
            c.line(sx, max(cys), sx, stem_top)
        if dur.rstrip('.') in ('e', 's'):
            # chords are never beamed (draw_system has no beam support for
            # 'pitches' events), so an eighth chord always gets its own flag --
            # same curved-bezier flag as draw_note, anchored at the stem tip.
            # La semicorchea lleva dos corchetes, igual que en draw_note.
            for _k in range(2 if dur.rstrip('.') == 's' else 1):
                _off = _k * gap * 0.9 * (-1 if stem_dir == 'up' else 1)
                fx, fy = sx, stem_top + _off
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


# Duraciones que entiende el motor, en tiempos de negra. Vive a nivel de modulo
# para que el auditor use EXACTAMENTE la misma tabla que el dibujante: cuando
# estaban duplicadas, anadir una figura nueva en un sitio y no en el otro hacia
# que el auditor contase mal los compases sin avisar.
# La REDONDA CON PUNTILLO ('w.') vale seis tiempos y es lo que llena un compas
# de 12/8, que es como esta escrito el Perfect de Aida. Se anadio con la pieza:
# antes el compas de 12/8 no tenia ninguna figura capaz de llenarlo y
# `relleno.figura_compas` devolvia una redonda, que se queda a dos tiempos.
# El DOBLE PUNTILLO ('h..', 'q..', 'e..') anade la mitad del primer puntillo:
# una negra con doble puntillo vale 1 + 1/2 + 1/4 = 1,75 tiempos. Entro en el
# motor con el Gladiator de Aida (arr. A. C. Escobes), que abre con negra de
# doble puntillo + semicorchea cuatro veces seguidas; escribirlo con un solo
# puntillo habria dejado el compas en 3,5 tiempos y el auditor lo habria
# cazado, pero escribirlo "parecido" habria sido contarle otro ritmo.
DUR_BEATS = {'w.': 6.0, 'w': 4.0, 'h..': 3.5, 'h.': 3.0, 'h': 2.0,
             'q..': 1.75, 'q.': 1.5, 'q': 1.0,
             'e..': 0.875, 'e.': 0.75, 'e': 0.5, 's.': 0.375, 's': 0.25}

# Cuantos corchetes/barras lleva cada figura: la corchea una, la semicorchea dos.
DUR_FLAGS = {'e': 1, 'e.': 1, 'e..': 1, 's': 2, 's.': 2}


def beats_de(e):
    """Lo que dura UN evento, en tiempos de negra.

       Es el unico sitio donde se aplica el 2/3 del tresillo. Cualquier modulo
       que sume duraciones tiene que llamar aqui: cuando hoja_piano lo calculaba
       por su cuenta, un compas con tresillos se partia en lineas por donde no
       tocaba y el auditor cantaba compases incompletos."""
    b = DUR_BEATS[e['dur']]
    return b * (2.0 / 3.0) if e.get('tresillo') else b


def draw_articulacion(c, cx, cy, gap, tipo, stem_dir='up', staff_bottom_y=None, staff_top_y=None):
    """Staccato, acento y calderon.

       Van al lado CONTRARIO de la plica, que es la convencion de grabado: si la
       plica sube, la marca va debajo de la cabeza, y al reves. El calderon es la
       excepcion y va siempre encima del pentagrama."""
    c.setFillColor(INK)
    c.setStrokeColor(INK)
    below = (stem_dir == 'up')
    d = -1 if below else 1
    y = cy + d * gap * 1.15
    if tipo == 'staccato':
        c.circle(cx, y, gap * 0.16, fill=1, stroke=0)
    elif tipo == 'acento':
        c.setLineWidth(1.2)
        w = gap * 0.55
        p = c.beginPath()
        p.moveTo(cx - w, y + gap * 0.28)
        p.lineTo(cx + w, y)
        p.lineTo(cx - w, y - gap * 0.28)
        c.drawPath(p, fill=0, stroke=1)
    elif tipo == 'tenuto':
        c.setLineWidth(1.3)
        c.line(cx - gap * 0.5, y, cx + gap * 0.5, y)
    elif tipo == 'calderon':
        top = (staff_top_y if staff_top_y is not None else cy) + gap * 1.6
        c.setLineWidth(1.2)
        p = c.beginPath()
        p.moveTo(cx - gap * 0.9, top)
        p.curveTo(cx - gap * 0.9, top + gap * 1.15, cx + gap * 0.9, top + gap * 1.15,
                  cx + gap * 0.9, top)
        c.drawPath(p, fill=0, stroke=1)
        c.circle(cx, top + gap * 0.32, gap * 0.15, fill=1, stroke=0)


def draw_ligadura(c, x1, y1, x2, y2, gap, arriba=True, tipo='fraseo'):
    """Ligadura de union (tie) o de fraseo (slur).

       Se dibuja como un arco relleno de grosor variable -- fino en las puntas y
       grueso en el centro -- que es lo que la distingue de una linea curva a
       secas. `arriba` decide de que lado se curva."""
    d = 1 if arriba else -1
    ancho = abs(x2 - x1)
    # Un arco de fraseo largo tiene que abrirse de verdad o parece una raya. Y
    # los dos extremos arrancan a la MISMA altura (la mas exterior de las dos
    # notas), como en cualquier edicion: si cada punta sigue a su nota, un salto
    # melodico deja la ligadura torcida.
    base = (max(y1, y2) if arriba else min(y1, y2))
    y1 = y2 = base
    alto = min(gap * 2.8, max(gap * 0.7, ancho * 0.085)) * d
    ym = base + alto
    grosor = gap * 0.17
    c.setFillColor(INK)
    p = c.beginPath()
    p.moveTo(x1, y1)
    p.curveTo(x1 + ancho * 0.25, ym, x2 - ancho * 0.25, ym, x2, y2)
    p.curveTo(x2 - ancho * 0.25, ym - grosor * d, x1 + ancho * 0.25, ym - grosor * d, x1, y1)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def draw_matiz(c, cx, y, gap, texto):
    """Matiz dinamico (p, mp, mf, f, ff, pp, sf...) bajo el pentagrama.

       Va en cursiva-negrita como en cualquier edicion; usamos la serif del
       proyecto porque DejaVu no trae los glifos de dinamica de SMuFL."""
    c.setFont('DejaVuSerif-Bold', gap * 1.45)
    c.setFillColor(INK)
    c.drawString(cx, y, texto)
    return stringWidth(texto, 'DejaVuSerif-Bold', gap * 1.45)


def draw_regulador(c, x1, x2, y, gap, cerrando=False):
    """Regulador de crescendo (abre) o diminuendo (cierra)."""
    c.setStrokeColor(INK)
    c.setLineWidth(0.9)
    h = gap * 0.55
    if not cerrando:
        c.line(x1, y, x2, y + h)
        c.line(x1, y, x2, y - h)
    else:
        c.line(x1, y + h, x2, y)
        c.line(x1, y - h, x2, y)


def draw_pedal(c, x1, x2, y, gap):
    """La marca de pedal: 'Ped.' con su linea y el corchete de suelta."""
    c.setFont('DejaVuSerif-Bold', gap * 1.25)
    c.setFillColor(INK)
    c.drawString(x1, y, 'Ped.')
    w = stringWidth('Ped.', 'DejaVuSerif-Bold', gap * 1.25)
    c.setStrokeColor(INK)
    c.setLineWidth(0.9)
    if x2 > x1 + w + gap * 0.5:
        yy = y + gap * 0.15
        c.line(x1 + w + gap * 0.3, yy, x2, yy)
        c.line(x2, yy, x2, yy + gap * 0.7)


def draw_tresillo(c, x1, x2, y, gap, arriba=True):
    """El 3 del tresillo con su corchete."""
    xm = (x1 + x2) / 2.0
    c.setStrokeColor(INK)
    c.setLineWidth(0.9)
    d = 1 if arriba else -1
    gancho = gap * 0.4 * d
    hueco = gap * 0.55
    c.line(x1, y, xm - hueco, y)
    c.line(xm + hueco, y, x2, y)
    c.line(x1, y, x1, y - gancho)
    c.line(x2, y, x2, y - gancho)
    c.setFont('DejaVuSerif-Bold', gap * 1.0)
    c.setFillColor(INK)
    c.drawCentredString(xm, y - gap * 0.35, '3')


def draw_repeticion(c, x, top_y, bottom_y, gap, abre=True):
    """Barra de repeticion: doble barra con los dos puntos al lado que toca."""
    c.setStrokeColor(GRAY)
    gruesa, fina = 2.6, 1.0
    if abre:
        c.setLineWidth(gruesa)
        c.line(x, top_y, x, bottom_y)
        c.setLineWidth(fina)
        c.line(x + 4, top_y, x + 4, bottom_y)
        px = x + 8
    else:
        c.setLineWidth(fina)
        c.line(x, top_y, x, bottom_y)
        c.setLineWidth(gruesa)
        c.line(x + 4, top_y, x + 4, bottom_y)
        px = x - 4
    mid = (top_y + bottom_y) / 2.0
    c.setFillColor(GRAY)
    c.circle(px, mid + gap * 0.5, gap * 0.16, fill=1, stroke=0)
    c.circle(px, mid - gap * 0.5, gap * 0.16, fill=1, stroke=0)


def draw_casilla(c, x1, x2, y, gap, numero='1'):
    """Casilla de primera / segunda vez."""
    c.setStrokeColor(GRAY)
    c.setLineWidth(0.9)
    c.line(x1, y, x2, y)
    c.line(x1, y, x1, y - gap * 0.85)
    c.setFont('DejaVuSans', gap * 0.85)
    c.setFillColor(GRAY)
    c.drawString(x1 + gap * 0.3, y - gap * 0.8, '%s.' % numero)


def ottava_y(gap, events, clef='treble'):
    """A que altura sobre la LINEA SUPERIOR va la base del "8va".

       Vive aqui y no en el layout porque la usan los dos: `draw_system` para
       dibujarlo y `before_staff` para reservarle el hueco. Si cada uno usara
       su propio numero, el 8va acabaria pisando el rotulo del sistema (que es
       justo lo que pasaba)."""
    top_line = 4 * gap
    alto = top_line
    for e in events:
        ps = e.get('pitches') or ([e['pitch']] if 'pitch' in e else [])
        if not ps:
            continue
        cys = [note_y(0, gap, p, clef=clef) for p in ps]
        alto = max(alto, max(cys))
        # la plica sube desde la nota mas aguda cuando el grupo esta bajo
        if (e.get('dur') or '').rstrip('.') != 'w' and sum(cys) / len(cys) <= 2 * gap:
            alto = max(alto, max(cys) + gap * 3.4)
    return (alto - top_line) + gap * 0.5


def draw_ottava(c, x1, x2, y, gap):
    """8va: suena una octava mas alto de lo escrito."""
    c.setFont('DejaVuSerif-Bold', gap * 1.05)
    c.setFillColor(INK)
    c.drawString(x1, y, '8va')
    w = stringWidth('8va', 'DejaVuSerif-Bold', gap * 1.05)
    if x2 > x1 + w + gap:
        c.setStrokeColor(INK)
        c.setLineWidth(0.7)
        yy = y + gap * 0.3
        c.setDash(2, 2)
        c.line(x1 + w + gap * 0.25, yy, x2, yy)
        c.setDash()
        c.line(x2, yy, x2, yy - gap * 0.55)

def draw_system(c, x, top_y, width, gap, events, clef='treble', time_sig=(4, 4),
                 show_clef=True, show_time=True, key_sig=None, spacing='linear',
                 repetir=None, casilla=None, ottava=False):
    """events: list of dicts with keys:
         pitch (str) OR pitches (list, for a chord)
         dur: 'w','h.','h','q..','q.','q','e.','e','s.','s'  (ver DUR_BEATS)
         number (fingering, optional), label (optional)
         beam (optional group id -- consecutive same-id eighth notes get a beam)
         art: 'staccato' | 'acento' | 'tenuto' | 'calderon' (o lista de varias)
         lig: True -- liga esta nota con la siguiente que suene
         tresillo: id de grupo (o True) -- tres notas en el hueco de dos
         matiz: 'p' | 'mf' | 'f' ... -- se imprime bajo el pentagrama
         cresc / dim: nº de eventos que abarca el regulador
         pedal: nº de eventos que abarca la marca de pedal
       repetir: 'abre' | 'cierra' | 'ambas' -- barras de repeticion
       casilla: '1' | '2' -- casilla de primera / segunda vez
       ottava: True -- 8va sobre el sistema
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
        if acc == 'n':          # el becuadro contradice la armadura: se dibuja siempre
            return p
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

    # Una sola tabla de duraciones para todo el motor (ver DUR_BEATS). El
    # tresillo ocupa 2/3 de lo que dice su figura: tres notas en el hueco de dos.
    _beats = beats_de
    dur_beats = DUR_BEATS
    beats_per_bar = time_sig[0] * (4.0 / time_sig[1])
    total_beats = sum(_beats(e) for e in events)
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
        ws = [_beats(e) ** 0.6 for e in events]
        tw = sum(ws) or 1.0
        cum_beat, cum_w = [0.0], [0.0]
        for e, w in zip(events, ws):
            cum_beat.append(cum_beat[-1] + _beats(e))
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
        beat_pos += _beats(e)

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
    note_anchors = []   # (x, cy, stem_dir) por evento, para ligaduras y articulaciones
    for i, (px, e) in enumerate(zip(positions, events)):
        if e.get('rest'):
            draw_rest(c, px, bot, top, gap, dur=e['dur'])
            note_anchors.append(None)
        elif 'pitches' in e:
            draw_chord(c, px, bot, top, gap, [_disp(p) for p in e['pitches']], dur=e['dur'], clef=clef, label=e.get('label'))
            cys_e = [note_y(bot, gap, p, clef=clef) for p in e['pitches']]
            avg = sum(cys_e) / len(cys_e)
            sd_e = 'down' if avg > bot + 2 * gap else 'up'
            note_anchors.append((px, max(cys_e) if sd_e == 'down' else min(cys_e), sd_e))
        else:
            beam_id = e.get('beam')
            suppress_flag = beam_id is not None
            forced_dir = group_stem_dir.get(beam_id) if beam_id is not None else None
            stem_end = group_beam_y.get(beam_id) if beam_id is not None else None
            cx, cy, sd = draw_note(c, px, bot, top, gap, _disp(e['pitch']), dur=e['dur'],
                                    number=e.get('number'), label=e.get('label'),
                                    beam_to=True if suppress_flag else None, clef=clef,
                                    stem_dir=forced_dir, stem_end_y=stem_end)
            note_anchors.append((px, cy, sd))
            if beam_id is not None:
                beam_groups.setdefault(beam_id, []).append((px, cy, sd, e['dur']))

    for gid, pts in beam_groups.items():
        if len(pts) >= 2:
            sd = pts[0][2]
            stem_top = group_beam_y[gid]
            x_off = gap * 0.6 if sd == 'up' else -gap * 0.6
            x1 = pts[0][0] + x_off
            x2 = pts[-1][0] + x_off
            draw_beam(c, x1, stem_top, x2, stem_top, gap=gap)
            # Segunda barra para las semicorcheas del grupo. Si TODO el grupo son
            # semicorcheas, la barra recorre el grupo entero; si solo lo son
            # algunas (el clasico negra-con-puntillo + semicorchea), la segunda
            # barra se dibuja como un trocito colgando de la nota que la lleva.
            paso = gap * 0.62 * (-1 if sd == 'up' else 1)
            y2 = stem_top + paso
            n_flags = [DUR_FLAGS.get(p[3], 1) for p in pts]
            if min(n_flags) >= 2:
                draw_beam(c, x1, y2, x2, y2, gap=gap)
            else:
                for k, p in enumerate(pts):
                    if DUR_FLAGS.get(p[3], 1) < 2:
                        continue
                    bx = p[0] + x_off
                    vecino = pts[k - 1] if k > 0 else (pts[k + 1] if k + 1 < len(pts) else None)
                    if vecino is not None and DUR_FLAGS.get(vecino[3], 1) >= 2:
                        draw_beam(c, min(bx, vecino[0] + x_off), y2,
                                  max(bx, vecino[0] + x_off), y2, gap=gap)
                    else:
                        # muñón hacia el interior del grupo
                        d = -1 if k == len(pts) - 1 else 1
                        draw_beam(c, bx, y2, bx + d * gap * 0.85, y2, gap=gap)

    # --- Ligaduras, articulacion, tresillos y marcas de expresion -----------
    for i, e in enumerate(events):
        anc = note_anchors[i]
        if anc is None:
            continue
        px, cy, sd = anc
        for art in ([e['art']] if isinstance(e.get('art'), str) else (e.get('art') or [])):
            draw_articulacion(c, px, cy, gap, art, stem_dir=sd,
                              staff_bottom_y=bot, staff_top_y=top)
        # 'lig' ata esta nota con la siguiente que suene. Si lleva un numero,
        # es una ligadura de FRASEO que abarca esas notas: lig=7 arquea sobre
        # las siete que vienen detras, que es como se marca un "sempre legato".
        if e.get('lig'):
            salto = 1 if e['lig'] is True else int(e['lig'])
            j = i + 1
            saltadas = 0
            while j < len(events):
                if note_anchors[j] is not None:
                    saltadas += 1
                    if saltadas >= salto:
                        break
                j += 1
            if j < len(events) and note_anchors[j] is not None:
                px2, cy2, _sd2 = note_anchors[j]
                arriba = (sd == 'down')
                d = gap * (1.0 if arriba else -1.0)
                draw_ligadura(c, px + gap * 0.35, cy + d, px2 - gap * 0.35, cy2 + d,
                              gap, arriba=arriba)

    # tresillos: se agrupan los eventos consecutivos marcados con el mismo id
    tri = {}
    for i, e in enumerate(events):
        t = e.get('tresillo')
        if t is not None and note_anchors[i] is not None:
            tri.setdefault(t if t is not True else 'auto', []).append(note_anchors[i])
    for _tid, ancs in tri.items():
        if len(ancs) < 2:
            continue
        arriba = ancs[0][2] == 'up'
        ys = [a[1] for a in ancs]
        ty = (max(ys) + gap * 4.2) if arriba else (min(ys) - gap * 4.2)
        draw_tresillo(c, ancs[0][0] - gap * 0.4, ancs[-1][0] + gap * 0.4, ty, gap, arriba=arriba)

    # matices y reguladores, bajo el pentagrama
    y_din = bot - gap * 2.6
    for i, e in enumerate(events):
        if note_anchors[i] is None:
            continue
        px = note_anchors[i][0]
        if e.get('matiz'):
            draw_matiz(c, px - gap * 0.3, y_din, gap, e['matiz'])
        if e.get('cresc') or e.get('dim'):
            j = min(i + int(e.get('cresc') or e.get('dim')), len(events) - 1)
            px2 = positions[j]
            draw_regulador(c, px + gap * 1.2, px2, y_din + gap * 0.5, gap,
                           cerrando=bool(e.get('dim')))
        if e.get('pedal'):
            j = min(i + int(e['pedal']), len(events) - 1)
            draw_pedal(c, px, positions[j], bot - gap * 4.4, gap)

    # 8va sobre el sistema. La altura NO es fija: se apoya sobre la tinta que
    # de verdad hay en este sistema (cabezas fuera del pentagrama, plicas hacia
    # arriba, barras), con un margen de medio espacio. Con la altura fija de
    # 2.2 gaps que tenia antes, un sistema de notas graves dejaba un hueco
    # enorme y otro de notas agudas se le montaba encima; y como el hueco que
    # reserva `page_layout_common.before_staff` tiene que ser el mismo numero,
    # la version fija obligaba a reservar siempre el peor caso y una hoja llena
    # se salia por abajo. `ottava_y` calcula lo mismo en los dos sitios.
    if ottava and events:
        draw_ottava(c, positions[0], positions[-1] + gap,
                    top + ottava_y(gap, events, clef), gap)

    # barras de repeticion y casillas
    if repetir in ('abre', 'ambas'):
        draw_repeticion(c, x + 1, top, bot, gap, abre=True)
    if repetir in ('cierra', 'ambas'):
        draw_repeticion(c, x + width - 5, top, bot, gap, abre=False)
    if casilla:
        draw_casilla(c, x + 6, x + width * 0.45, top + gap * 1.5, gap, numero=str(casilla))

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
