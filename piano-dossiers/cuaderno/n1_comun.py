# -*- coding: utf-8 -*-
"""Componentes compartidos por los meses del cuaderno de adultos: diagramas de pentagrama, claves, teclado y manos."""
from n1_base import *
from n1_base import _abs_idx
from reportlab.lib.colors import HexColor
from notation import draw_staff, draw_clef, draw_note, note_y
import nens_dib

CREMA_T = HexColor('#EADFC0')
SEC = 'abcdef'
N = lambda dd, p=None: ('n', dd) if p is None else ('n', dd, p)
R = lambda dd: ('r', dd)


def fig_celda(d, silencio_=False, dot=False, gap=3.7):
    """Celda de tabla con una figura (o su silencio), centrada vertical y horizontalmente."""
    def f(c, cx, cy, w, hh):
        if silencio_:
            silencio(c, cx, cy, gap * 1.15, d, linea=False)
        else:
            nf = FIG[d][0]
            alto = gap * (3.4 + 0.95 * max(0, nf - 2)) + gap * 0.5 if FIG[d][2] else gap
            figura(c, cx - gap * 0.6, cy - alto / 2.0 + gap * 0.5, gap, d, linea=False, dot=dot)
    return f


def suma_items(items):
    return sum((it[1] if it[0] == 'x' else BEATS[it[1]]) for it in items)


def diag_pentagrama():
    """Pentagrama numerado (lineas y espacios) y las siete notas de Do a Do."""
    h = 124

    def f(c, x, y, w):
        g = 10.0
        xs, ws = x + 4, 150
        ys = draw_staff(c, xs, y - 30, ws, g)
        draw_clef(c, xs + 4, ys[-1], g, 'treble')
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY)
        c.drawString(xs, y - 8, 'LÍNEAS Y ESPACIOS')
        for k in range(5):
            c.setFont('DejaVuSans-Bold', 7.2)
            c.setFillColor(OCRE)
            c.drawString(xs + ws + 8, ys[-1 - k] - 2.5, '%d.ª línea' % (k + 1))
        for k in range(4):
            c.setFont('DejaVuSans', 7.0)
            c.setFillColor(AZUL)
            c.drawString(xs + ws + 62, ys[-1 - k] + g / 2 - 2.5, ['1.er', '2.º', '3.er', '4.º'][k] + ' espacio')
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(OCRE)
        c.drawString(xs, ys[-1] - 20, 'se cuentan de abajo arriba  ↑')
        xr = x + 300
        wr = w - 300
        ys2 = draw_staff(c, xr, y - 30, wr, g)
        bot2 = ys2[-1]
        draw_clef(c, xr + 4, bot2, g, 'treble')
        notas = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
        nm = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do']
        lt = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
        x0 = xr + 46
        paso = (wr - 52) / 8.0
        for k, p in enumerate(notas):
            cx = x0 + paso * (k + 0.5)
            draw_note(c, cx, bot2, ys2[0], g, p, dur='w', clef='treble')
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY)
            c.drawCentredString(cx, bot2 - 26, nm[k])
            c.setFont('DejaVuSans', 7.0)
            c.setFillColor(MUTED)
            c.drawCentredString(cx, bot2 - 36, lt[k])
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY)
        c.drawString(xr, y - 8, 'DE DO A DO (LETRAS EN NOTACIÓN ANGLOSAJONA)')
    return Blk(h, f)


def diag_claves():
    """Clave de sol (2.ª linea = Sol) y clave de fa (4.ª linea = Fa), cada una con su nota de referencia."""
    h = 96

    def f(c, x, y, w):
        g = 10.0
        xs = x + 4
        ys = draw_staff(c, xs, y - 30, 200, g)
        draw_clef(c, xs + 4, ys[-1], g, 'treble')
        c.setStrokeColor(OCRE)
        c.setLineWidth(2.2)
        c.line(xs + 52, ys[-2], xs + 200, ys[-2])
        draw_note(c, xs + 150, ys[-1], ys[0], g, 'G4', dur='w', clef='treble')
        c.setFont('DejaVuSans-Bold', 8.2)
        c.setFillColor(OCRE)
        c.drawCentredString(xs + 100, ys[-1] - 26, '2.ª línea = SOL')
        xb = x + 262
        yb = draw_staff(c, xb, y - 30, 200, g)
        draw_clef(c, xb + 4, yb[-1], g, 'bass')
        c.setStrokeColor(OCRE)
        c.setLineWidth(2.2)
        c.line(xb + 50, yb[1], xb + 200, yb[1])
        draw_note(c, xb + 150, yb[-1], yb[0], g, 'F3', dur='w', clef='bass')
        c.setFillColor(OCRE)
        c.setFont('DejaVuSans-Bold', 8.2)
        c.drawCentredString(xb + 100, yb[-1] - 26, '4.ª línea = FA')
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY)
        c.drawString(xs, y - 8, 'CLAVE DE SOL: LA ESPIRAL RODEA LA 2.ª LÍNEA')
        c.drawString(xb, y - 8, 'CLAVE DE FA: LOS DOS PUNTOS RODEAN LA 4.ª LÍNEA')
    return Blk(h, f)


def diag_grupos(n_blancas=15, desde=('C', 4), alto=88):
    h = alto + 62

    def f(c, x, y, w):
        kw = w / float(n_blancas)
        yb = y - 22 - alto
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'GRUPOS DE DOS Y DE TRES TECLAS NEGRAS')
        teclado(c, x, yb, w, alto, desde=desde, n_blancas=n_blancas, etiqueta_blancas=True,
                marcas={'C4': CREMA_T, 'C5': CREMA_T, 'C6': CREMA_T}, do_central=True)
        for o in (0, 1):
            x2 = x + (o * 7) * kw
            c.setStrokeColor(OCRE)
            c.setLineWidth(1.4)
            c.line(x2 + kw * 0.7, y - 22, x2 + kw * 2.3, y - 22)
            c.line(x2 + kw * 3.7, y - 22, x2 + kw * 6.3, y - 22)
            c.setFont('DejaVuSans-Bold', 8)
            c.setFillColor(OCRE)
            c.drawCentredString(x2 + kw * 1.5, y - 18, '2')
            c.drawCentredString(x2 + kw * 5.0, y - 18, '3')
        c.setFont('DejaVuSans', 7.2)
        c.setFillColor(MUTED)
        c.drawString(x, yb - 13, 'Cada Do está a la izquierda de un grupo de dos negras. El punto marca el Do central (C4).')
    return Blk(h, f)


def manos_dedos():
    """Las dos manos con los dedos numerados."""
    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 8.6)
        c.setFillColor(NAVY)
        c.drawCentredString(x + 120, y - 12, 'MANO IZQUIERDA')
        c.drawCentredString(x + 360, y - 12, 'MANO DERECHA')
        nens_dib.ma_real(c, x + 120, y - 152, 0.85, esq=True, dits=True, color=False)
        nens_dib.ma_real(c, x + 360, y - 152, 0.85, esq=False, dits=True, color=False)
    return Blk(216, f)


def cinco_dedos_teclas():
    """Posicion de cinco dedos sobre el Do en cada mano."""
    def f(c, x, y, w):
        kw = 44
        for lab, dits, yy in (('DERECHA', [1, 2, 3, 4, 5], y - 4), ('IZQUIERDA', [5, 4, 3, 2, 1], y - 56)):
            c.setFont('DejaVuSans-Bold', 8)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, yy - 28, lab)
            for i in range(5):
                xx = x + 90 + i * kw
                c.setFillColor(BLANCO)
                c.setStrokeColor(NAVY)
                c.setLineWidth(1)
                c.roundRect(xx, yy - 46, kw, 46, 4, fill=1, stroke=1)
                c.setFillColor(NAVY)
                c.circle(xx + kw / 2, yy - 13, 8, fill=1, stroke=0)
                c.setFillColor(BLANCO)
                c.setFont('DejaVuSans-Bold', 8.6)
                c.drawCentredString(xx + kw / 2, yy - 16, str(dits[i]))
                c.setFillColor(INK)
                c.setFont('DejaVuSans-Bold', 8)
                c.drawCentredString(xx + kw / 2, yy - 40, ['DO', 'RE', 'MI', 'FA', 'SOL'][i])
            c.setFont('DejaVuSans', 7.4)
            c.setFillColor(MUTED)
            c.drawString(x + 90 + 5 * kw + 14, yy - 28, 'Do central → Sol' if lab == 'DERECHA' else 'Do grave → Sol')
    return Blk(116, f)


def lectura_ancla(r, clef, n=8, filas=3, pool=None):
    """Filas de notas para nombrar contando desde la nota de referencia: Do (clave de sol) o Fa (clave de fa).
       La primera nota de cada fila es la referencia y va nombrada; el resto se nombra contando desde ella."""
    if clef == 'treble':
        ancla = 'C4'
        base = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'D4']
    else:
        ancla = 'F3'
        base = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'E2', 'F2']
    pool = list(pool) if pool else base
    out = []
    for _ in range(filas):
        ps = [ancla]
        while len(ps) < n:
            p = r.choice(pool)
            if p != ps[-1] and abs(_abs_idx(p) - _abs_idx(ps[-1])) <= 5:
                ps.append(p)
        out.append(ps)
    return out


def bloque_lectura(r, clef, filas, titulo_base, nombres_ancla=True, pool=None, maxsalto=4):
    """Devuelve (bloques, soluciones) de las filas de lectura con ancla."""
    bl, sols = [], []
    for k, ps in enumerate(lectura_ancla(r, clef, 8, filas, pool)):
        bajo = [nombre(ps[0])] + ['_'] * 7
        bl.append(fila_notas(clef, ps, 'q', bajo=bajo, barras=4, titulo='%s) %s' % (SEC[k], titulo_base)))
        sols.append('%s) %s' % (SEC[k], ' · '.join(nombre(p) for p in ps)))
    return bl, sols


def diag_semitonos():
    """Una octava con los doce sonidos y los semitonos naturales (Mi-Fa y Si-Do) marcados."""
    h = 120

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'DOCE SONIDOS POR OCTAVA, CADA UNO A UN SEMITONO DEL SIGUIENTE')
        kw = w / 8.0
        yb = y - 100
        teclado(c, x, yb, w, 70, desde=('C', 4), n_blancas=8, etiqueta_blancas=True,
                rotulos={'C#4': 'Do♯', 'D#4': 'Re♯', 'F#4': 'Fa♯', 'G#4': 'Sol♯', 'A#4': 'La♯'}, tam_fuente=7.4)
        c.setStrokeColor(ROJO)
        c.setLineWidth(1.4)
        for k in (2, 6):
            xx = x + (k + 1) * kw
            c.line(xx, yb - 3, xx, yb + 70)
            c.setFont('DejaVuSans-Bold', 7.6)
            c.setFillColor(ROJO)
            c.drawCentredString(xx, yb - 12, 'semitono')
    return Blk(h, f)


def diag_escala():
    """Teclado de una octava con los tonos y semitonos de la escala de Do mayor."""
    h = 124

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'ESCALA DE DO MAYOR: TONO · TONO · SEMITONO · TONO · TONO · TONO · SEMITONO')
        kw = w / 8.0
        yb = y - 104
        teclado(c, x, yb, w, 62, desde=('C', 4), n_blancas=8, etiqueta_blancas=True,
                marcas={'%s4' % L: HexColor('#EADFC0') for L in 'CDEFGAB'} | {'C5': HexColor('#EADFC0')})
        for i in range(7):
            xa = x + kw * (i + 0.5)
            xb = x + kw * (i + 1.5)
            semi = i in (2, 6)
            c.setStrokeColor(ROJO if semi else NAVY)
            c.setLineWidth(1.3)
            p = c.beginPath()
            p.moveTo(xa, yb + 66)
            p.curveTo(xa, yb + 80, xb, yb + 80, xb, yb + 66)
            c.drawPath(p, stroke=1, fill=0)
            c.setFont('DejaVuSans-Bold', 7.6)
            c.setFillColor(ROJO if semi else NAVY)
            c.drawCentredString((xa + xb) / 2, yb + 84, '½' if semi else '1')
    return Blk(h, f)


def diag_digitacion(escD, escI, dD_s, dD_b, dI_s, dI_b, key=None):
    """Escala ascendente y descendente de cada mano con su digitacion (sin armadura; las alteraciones van escritas)."""
    h = 184

    def f(c, x, y, w):
        g = 8.4
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'MANO DERECHA')
        c.drawString(x + w / 2 + 6, y - 8, 'MANO IZQUIERDA')
        for off, esc, clef, dsub, dbaj in ((0, escD, 'treble', dD_s, dD_b), (w / 2 + 6, escI, 'bass', dI_s, dI_b)):
            ww = w / 2 - 12
            for fila, (ps, dg, yy) in enumerate(((esc, dsub, y - 30), (list(reversed(esc)), dbaj, y - 112))):
                ys = draw_staff(c, x + off, yy, ww, g)
                draw_clef(c, x + off + 3, ys[-1], g, clef)
                x0 = x + off + 44
                paso = (ww - 50) / float(len(ps))
                for k, p in enumerate(ps):
                    cx = x0 + paso * (k + 0.5)
                    draw_note(c, cx, ys[-1], ys[0], g, p, 'q', clef=clef, stem_dir='up')
                    c.setFont('DejaVuSans-Bold', 8)
                    c.setFillColor(OCRE)
                    c.drawCentredString(cx, ys[-1] - 23, str(dg[k]))
    return Blk(h, f)
