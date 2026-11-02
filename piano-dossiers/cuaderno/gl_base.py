# -*- coding: utf-8 -*-
"""GLOSARIO MUSICAL T-CLAS: componentes (entradas con simbolo, tablas, simbolos dibujados con el motor)."""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n1_base import *                                       # noqa: F401,F403  (Doc, Blk, caja, par, h2, tabla, teclado, figura, silencio ...)
from n1_base import _abs_idx
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from notation import (draw_staff, draw_clef, draw_time_sig, draw_barline, draw_note, draw_rest, draw_notehead, note_y,
                      draw_articulacion, draw_ligadura, draw_regulador, draw_tresillo, draw_ottava, draw_casilla,
                      draw_repeticion, draw_gracia, draw_accidental, _TREBLE_SHARP_POS, _TREBLE_FLAT_POS)

for _n, _p in (('FreeSerifBI', 'FreeSerifBoldItalic.ttf'), ('FreeSerifI', 'FreeSerifItalic.ttf')):
    try:
        pdfmetrics.registerFont(TTFont(_n, '/usr/share/fonts/truetype/freefont/' + _p))
    except Exception:
        pass


# ------------------------------------------------------------------ pentagrama en miniatura
def celda_pauta(fn=None, clef=None, ts=None, gap=4.6, ancho=None, lineas_=True):
    """Devuelve una funcion g(c, cx, cy, w, h) que dibuja un pentagrama pequeno centrado en la celda
       y llama a fn(c, ctx) para dibujar lo que se quiera encima (ctx: x0, x1, cur, top, bot, gap, clef)."""
    def g(c, cx, cy, w, h):
        W = ancho or (w - 10)
        x0 = cx - W / 2.0
        top = cy + 2 * gap
        ys = draw_staff(c, x0, top, W, gap)
        bot = ys[-1]
        cur = x0 + 3
        if clef:
            draw_clef(c, cur, bot, gap, clef)
            cur += gap * (5.0 if clef == 'treble' else 4.4)
        if ts:
            draw_time_sig(c, cur + gap * 0.8, bot, gap, top=str(ts[0]), bottom=str(ts[1]))
            cur += gap * 2.8
        ctx = dict(x0=x0, x1=x0 + W, cur=cur, top=ys[0], bot=bot, gap=gap, clef=clef or 'treble')
        if fn:
            fn(c, ctx)
    return g


def nota_en(c, ctx, x, pitch, dur='q', stem=None):
    return draw_note(c, x, ctx['bot'], ctx['top'], ctx['gap'], pitch, dur=dur, stem_dir=stem, clef=ctx['clef'])


def barra(c, ctx, x, final=False):
    draw_barline(c, x, ctx['top'], ctx['bot'], final=final)


def reparto(ctx, n, margen=0.0):
    """x de n notas repartidas en el espacio util de la mini pauta."""
    a = ctx['cur'] + 4 + margen
    b = ctx['x1'] - 6
    return [a + (b - a) * (k + 0.5) / n for k in range(n)]


# ------------------------------------------------------------------ simbolos concretos
def g_clave(clef):
    return celda_pauta(clef=clef, gap=4.6, ancho=88)


def g_llave():
    def g(c, cx, cy, w, h):
        gap = 3.6
        x0 = cx - 46
        W = 92
        t1 = cy + 17
        y1 = draw_staff(c, x0, t1, W, gap)
        t2 = cy - 4
        y2 = draw_staff(c, x0, t2, W, gap)
        draw_clef(c, x0 + 3, y1[-1], gap, 'treble')
        draw_clef(c, x0 + 3, y2[-1], gap, 'bass')
        c.setStrokeColor(INK)
        c.setLineWidth(1.2)
        c.line(x0, y1[0], x0, y2[-1])
        p = c.beginPath()
        xb = x0 - 3
        p.moveTo(xb + 3, y1[0])
        p.curveTo(xb - 6, y1[0] - 10, xb + 3, (y1[0] + y2[-1]) / 2 + 4, xb - 5, (y1[0] + y2[-1]) / 2)
        p.curveTo(xb + 3, (y1[0] + y2[-1]) / 2 - 4, xb - 6, y2[-1] + 10, xb + 3, y2[-1])
        c.setLineWidth(1.4)
        c.drawPath(p, stroke=1, fill=0)
    return g


def g_linea_adicional():
    def fn(c, ctx):
        xs = reparto(ctx, 3)
        nota_en(c, ctx, xs[0], 'C4', 'w')
        nota_en(c, ctx, xs[1], 'E4', 'w')
        nota_en(c, ctx, xs[2], 'A5', 'w')
    return celda_pauta(fn, clef='treble', ancho=104)


def g_ts(top, bottom, notas=('q', 'q', 'q', 'q')):
    def fn(c, ctx):
        xs = reparto(ctx, len(notas))
        for x, d_ in zip(xs, notas):
            nota_en(c, ctx, x, 'B4', d_, 'up')
        barra(c, ctx, ctx['x1'] - 1, final=False)
    return celda_pauta(fn, clef='treble', ts=(top, bottom), ancho=112)


def g_simbolo_ts(sim):
    """C (4/4) o C cortada (2/2)."""
    def g(c, cx, cy, w, h):
        c.setFont('FreeSerif', 24)
        c.setFillColor(INK)
        c.drawCentredString(cx, cy - 8, sim)
    return g


def g_barra(tipo):
    def fn(c, ctx):
        top, bot, gap = ctx['top'], ctx['bot'], ctx['gap']
        a, b = ctx['x0'] + 18, ctx['x1'] - 18
        xm = (a + b) / 2
        if tipo == 'divisoria':
            nota_en(c, ctx, xm - 18, 'B4', 'q', 'up')
            barra(c, ctx, xm + 2)
            nota_en(c, ctx, xm + 20, 'B4', 'q', 'up')
        elif tipo == 'doble':
            barra(c, ctx, xm - 1.5)
            barra(c, ctx, xm + 2.5)
        elif tipo == 'final':
            barra(c, ctx, xm - 6)
            c.setLineWidth(2.6)
            c.setStrokeColor(INK)
            c.line(xm - 2, top, xm - 2, bot)
        elif tipo == 'rep_cierra':
            nota_en(c, ctx, xm - 22, 'B4', 'q', 'up')
            draw_repeticion(c, xm + 4, top, bot, gap, abre=False)
        elif tipo == 'rep_abre':
            draw_repeticion(c, xm - 6, top, bot, gap, abre=True)
            nota_en(c, ctx, xm + 22, 'B4', 'q', 'up')
        elif tipo == 'rep_ambas':
            draw_repeticion(c, ctx['x0'] + 12, top, bot, gap, abre=True)
            for xx in (xm - 8, xm + 8):
                nota_en(c, ctx, xx, 'B4', 'q', 'up')
            draw_repeticion(c, ctx['x1'] - 22, top, bot, gap, abre=False)
        elif tipo == 'casillas':
            a2 = ctx['x0'] + 10
            nota_en(c, ctx, a2 + 8, 'B4', 'q', 'up')
            nota_en(c, ctx, a2 + 22, 'B4', 'q', 'up')
            draw_repeticion(c, a2 + 34, top, bot, gap, abre=False)
            draw_casilla(c, a2 - 2, a2 + 40, top + gap * 1.5, gap, '1')
            draw_casilla(c, a2 + 46, ctx['x1'] - 4, top + gap * 1.5, gap, '2')
            nota_en(c, ctx, a2 + 62, 'B4', 'q', 'up')
            barra(c, ctx, ctx['x1'] - 8, final=False)
    return celda_pauta(fn, ancho=112, gap=4.4)


def g_alteracion(tipo):
    """Nota con su alteracion delante."""
    def fn(c, ctx):
        xs = reparto(ctx, 1)
        x = xs[0] + 14
        gap = ctx['gap']
        if tipo in ('#', 'b', 'n'):
            nota_en(c, ctx, x, {'#': 'F#4', 'b': 'Bb4', 'n': 'Fn4'}[tipo], 'q', 'up')
        else:
            cy = note_y(ctx['bot'], gap, 'F4' if tipo == 'x' else 'B4', 'treble')
            draw_notehead(c, x, cy, gap, True)
            c.setStrokeColor(INK)
            c.setLineWidth(max(1.0, gap * 0.12))
            c.line(x + gap * 0.6, cy, x + gap * 0.6, cy + gap * 3.2)
            c.setFillColor(INK)
            c.setFont('FreeSerif', gap * 3.0)
            c.drawRightString(x - gap * 0.9, cy - gap * 0.65, '\U0001D12A' if tipo == 'x' else '\U0001D12B')
    return celda_pauta(fn, clef='treble', ancho=84, gap=5.4)


def g_dim(txt, size=15):
    def g(c, cx, cy, w, h):
        c.setFont('FreeSerifBI', size)
        c.setFillColor(INK)
        c.drawCentredString(cx, cy - size * 0.32, txt)
    return g


def g_regulador(cerrando=False, txt=''):
    def g(c, cx, cy, w, h):
        draw_regulador(c, cx - 32, cx + 32, cy - 2, 6.5, cerrando)
        if txt:
            c.setFont('FreeSerifI', 9.5)
            c.setFillColor(INK)
            c.drawCentredString(cx, cy + 9, txt)
    return g


def g_artic(tipo):
    def fn(c, ctx):
        xs = reparto(ctx, 1)
        x = xs[0]
        gap = ctx['gap']
        cx, cy, sd = nota_en(c, ctx, x, 'B4', 'q', 'up')
        if tipo in ('staccato', 'acento', 'tenuto', 'calderon'):
            draw_articulacion(c, x, cy, gap, tipo, sd, ctx['bot'], ctx['top'])
        elif tipo == 'marcato':
            y = cy - gap * 1.25
            c.setStrokeColor(INK)
            c.setLineWidth(1.2)
            p = c.beginPath()
            p.moveTo(x - gap * 0.5, y - gap * 0.45)
            p.lineTo(x, y + gap * 0.3)
            p.lineTo(x + gap * 0.5, y - gap * 0.45)
            c.drawPath(p, fill=0, stroke=1)
    return celda_pauta(fn, clef=None, ancho=50, gap=4.6)


def g_ligadura(iguales):
    def fn(c, ctx):
        xs = reparto(ctx, 2 if iguales else 3)
        gap = ctx['gap']
        pit = ['B4', 'B4'] if iguales else ['G4', 'A4', 'B4']
        ys = []
        for x, p in zip(xs, pit):
            cx, cy, sd = nota_en(c, ctx, x, p, 'h' if iguales and False else 'q', 'up')
            ys.append((x, cy))
        draw_ligadura(c, ys[0][0], ys[0][1] - gap * 0.9, ys[-1][0], ys[-1][1] - gap * 0.9, gap, arriba=False,
                      tipo='union' if iguales else 'fraseo')
    return celda_pauta(fn, clef='treble', ancho=96, gap=4.6)


def g_tresillo():
    def fn(c, ctx):
        xs = reparto(ctx, 3)
        gap = ctx['gap']
        for x in xs:
            nota_en(c, ctx, x, 'B4', 'e', 'up')
        yb = ctx['top'] + gap * 3.2
        # barra
        c.setStrokeColor(INK)
        c.setLineWidth(2.4)
        ty = note_y(ctx['bot'], gap, 'B4', 'treble') + gap * 3.4
        c.line(xs[0] + gap * 0.6, ty, xs[-1] + gap * 0.6, ty)
        draw_tresillo(c, xs[0], xs[-1] + gap * 0.6, ty + gap * 1.2, gap, arriba=True)
    return celda_pauta(fn, ancho=84, gap=4.4)


def g_adorno():
    def fn(c, ctx):
        xs = reparto(ctx, 1)
        gap = ctx['gap']
        draw_gracia(c, xs[0] - gap * 1.8, note_y(ctx['bot'], gap, 'A4', 'treble'), gap, ctx['bot'], ctx['top'])
        nota_en(c, ctx, xs[0], 'B4', 'q', 'up')
    return celda_pauta(fn, clef='treble', ancho=70, gap=4.6)


def g_octava(alta=True):
    def fn(c, ctx):
        xs = reparto(ctx, 3)
        gap = ctx['gap']
        for x, p in zip(xs, ['G5', 'A5', 'B5'] if alta else ['G3', 'A3', 'B3']):
            nota_en(c, ctx, x, p, 'q', 'down' if alta else 'up')
        if alta:
            draw_ottava(c, xs[0] - 4, xs[-1] + 4, ctx['top'] + gap * 3.5, gap)
        else:
            c.setFont('DejaVuSerif-Bold', gap * 1.05)
            c.setFillColor(INK)
            c.drawString(xs[0] - 4, ctx['bot'] - gap * 3.1, '8vb')
            c.setStrokeColor(INK)
            c.setDash(2, 2)
            c.line(xs[0] + 18, ctx['bot'] - gap * 2.7, xs[-1] + 4, ctx['bot'] - gap * 2.7)
            c.setDash()
    return celda_pauta(fn, clef='treble', ancho=100, gap=4.4)


def g_texto(txt, size=12.5, font='FreeSerifI'):
    def g(c, cx, cy, w, h):
        c.setFont(font, size)
        c.setFillColor(INK)
        c.drawCentredString(cx, cy - size * 0.3, txt)
    return g


def g_segno():
    def g(c, cx, cy, w, h):
        c.setFont('FreeSerif', 24)
        c.setFillColor(INK)
        c.drawCentredString(cx, cy - 8, '\U0001D10B')
    return g


def g_coda():
    def g(c, cx, cy, w, h):
        c.setFont('FreeSerif', 24)
        c.setFillColor(INK)
        c.drawCentredString(cx, cy - 8, '\U0001D10C')
    return g


def g_sincopa():
    def fn(c, ctx):
        xs = reparto(ctx, 4)
        gap = ctx['gap']
        nota_en(c, ctx, xs[0], 'B4', 'e', 'up')
        nota_en(c, ctx, xs[1] - 4, 'B4', 'q', 'up')
        nota_en(c, ctx, xs[2] + 2, 'B4', 'e', 'up')
        nota_en(c, ctx, xs[3], 'B4', 'q', 'up')
    return celda_pauta(fn, clef=None, ts=(4, 4), ancho=100, gap=4.0)


def g_contratiempo():
    def fn(c, ctx):
        xs = reparto(ctx, 4)
        gap = ctx['gap']
        for k, x in enumerate(xs):
            if k % 2 == 0:
                draw_rest(c, x, ctx['bot'], ctx['top'], gap, 'e')
            else:
                nota_en(c, ctx, x, 'B4', 'e', 'up')
    return celda_pauta(fn, clef=None, ts=(2, 4), ancho=92, gap=4.0)


def g_anacrusa():
    def fn(c, ctx):
        xs = reparto(ctx, 5)
        nota_en(c, ctx, xs[0], 'B4', 'q', 'up')
        barra(c, ctx, (xs[0] + xs[1]) / 2 + 2)
        for x in xs[1:]:
            nota_en(c, ctx, x, 'B4', 'q', 'up')
    return celda_pauta(fn, clef='treble', ts=(4, 4), ancho=104, gap=4.0)


def g_pedal():
    def g(c, cx, cy, w, h):
        c.setFont('FreeSerifI', 13)
        c.setFillColor(INK)
        c.drawString(cx - 38, cy - 3, 'Ped.')
        c.setStrokeColor(INK)
        c.setLineWidth(0.9)
        c.line(cx - 8, cy - 6, cx + 30, cy - 6)
        c.line(cx + 30, cy - 6, cx + 30, cy + 1)
        c.setFont('DejaVuSans', 11)
        c.drawString(cx - 44 + 70, cy - 5, '✱' if False else '')
    return g


def g_arpegio():
    def fn(c, ctx):
        xs = reparto(ctx, 3)
        gap = ctx['gap']
        for x, p in zip(xs, ['C4', 'E4', 'G4']):
            nota_en(c, ctx, x, p, 'q', 'up')
    return celda_pauta(fn, clef='treble', ancho=90, gap=4.4)


def g_acorde(pitches, clef='treble', dur='w', ancho=62):
    def fn(c, ctx):
        from notation import draw_chord
        xs = reparto(ctx, 1)
        draw_chord(c, xs[0], ctx['bot'], ctx['top'], ctx['gap'], pitches, dur=dur, clef=clef)
    return celda_pauta(fn, clef=clef, ancho=ancho, gap=4.4)


def g_teclas(desde, n, marcas=None, arco=None, h=24, ancho=88):
    """Miniteclado con un arco DEBAJO que une dos teclas (tono o semitono)."""
    def g(c, cx, cy, w, hh):
        x0 = cx - ancho / 2.0
        yb = cy - 4
        teclado(c, x0, yb, ancho, h, desde=desde, n_blancas=n, marcas=marcas or {}, grosor=0.6)
        if arco:
            kw = ancho / float(n)
            a, b_, txt_, col = arco
            xa, xb = x0 + kw * (a + 0.5), x0 + kw * (b_ + 0.5)
            c.setStrokeColor(col)
            c.setLineWidth(1.2)
            p = c.beginPath()
            p.moveTo(xa, yb - 3)
            p.curveTo(xa, yb - 14, xb, yb - 14, xb, yb - 3)
            c.drawPath(p, stroke=1, fill=0)
            c.setFont('DejaVuSans-Bold', 7)
            c.setFillColor(col)
            c.drawCentredString((xa + xb) / 2, yb - 22, txt_)
    return g


# ------------------------------------------------------------------ entradas
def E(term, texto, glyph=None, term2=None, alto=None):
    return dict(term=term, texto=texto, glyph=glyph, term2=term2, alto=alto)


def bloque_entradas(entradas, col_t=118, col_g=112, min_h=26):
    """Cada entrada es una fila-bloque: termino (negrita), simbolo y definicion. Zebra alterna."""
    out = []
    ancho = CONTENT_W
    for k, e in enumerate(entradas):
        tiene_g = e['glyph'] is not None
        w_txt = ancho - col_t - (col_g if tiene_g else 0) - 10
        ls = lineas(e['texto'], w_txt, 8.7)
        lt = lineas('**%s**' % e['term'], col_t - 12, 8.4)
        if e.get('term2'):
            lt = lt + lineas(e['term2'], col_t - 12, 7.6)
        alto = max(min_h, len(ls) * 11.6 + 12, len(lt) * 10.6 + 12, 40 if tiene_g else 0, e.get('alto') or 0)

        def f(c, x, y, w, e=e, ls=ls, lt=lt, alto=alto, tiene_g=tiene_g, k=k, w_txt=w_txt):
            if k % 2 == 0:
                c.setFillColor(PANEL)
                c.rect(x, y - alto, w, alto, fill=1, stroke=0)
            c.setStrokeColor(RULE)
            c.setLineWidth(0.5)
            c.line(x, y - alto, x + w, y - alto)
            th = len(lt) * 10.6
            yy = y - (alto - th) / 2.0 + 0.5
            for i, ln in enumerate(lt):
                pinta_lineas(c, [ln], x + 7, yy - i * 10.6, 8.4 if i == 0 or not e.get('term2') else 7.6, 10.6, NAVY if i == 0 else MUTED)
            if tiene_g:
                e['glyph'](c, x + col_t + col_g / 2.0, y - alto / 2.0, col_g, alto)
            tx = x + col_t + (col_g if tiene_g else 0) + 4
            pinta_lineas(c, ls, tx, y - (alto - len(ls) * 11.6) / 2.0 + 0.5, 8.7, 11.6, INK)
        out.append(Blk(alto, f))
    return out
