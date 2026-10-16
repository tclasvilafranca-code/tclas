# -*- coding: utf-8 -*-
"""Utilidades para las hojas de pintar y de color: trazo "hecho a mano", tipografías de
   rotulador y los dibujos sueltos (sol, nube, estrellas, notas, arcoíris).

   `ManoCanvas` es un canvas de ReportLab cuyo `line`, `circle`, `ellipse`, `roundRect`,
   `rect` y `arc` dibujan el contorno con un temblor suave, como a lápiz. Solo tiembla
   lo que lleva trazo: los rellenos sin contorno (las máscaras blancas) salen exactos.

   Tipografías (todas instaladas con apt, licencia libre y con acentos catalanes):
     - 'Sketch'  Cabin Sketch Bold, para los títulos
     - 'Hand'    DKG Bold (fonts-dkg-handwriting), letra de mano para los textos
     - 'Fat'     Leckerli One, rotulador gordo para las hojas de color
"""
import math
import os
import random

from reportlab.lib.colors import black, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

_F = {
    'Sketch': '/usr/share/fonts/truetype/cabinsketch/CabinSketch-Bold.ttf',
    'Hand': '/usr/share/fonts/truetype/fifthhorseman/dkgBd.ttf',
    'Fat': '/usr/share/fonts/truetype/leckerli-one/LeckerliOne-Regular.ttf',
}
for _n, _p in _F.items():
    pdfmetrics.registerFont(TTFont(_n, _p))

W, H = 841.89, 595.276


class ManoCanvas(canvas.Canvas):
    def __init__(self, *a, seed=11, amp=0.9, **k):
        super().__init__(*a, **k)
        self._rng = random.Random(seed)
        self.amp = amp

    # ---- nucleo: temblor suave a lo largo de un trazo
    def _wob(self, pts, closed=False, amp=None):
        amp = self.amp if amp is None else amp
        n = len(pts)
        s = [0.0]
        for i in range(1, n):
            s.append(s[-1] + math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]))
        per = s[-1] + (math.hypot(pts[0][0] - pts[-1][0], pts[0][1] - pts[-1][1]) if closed else 0.0)
        if per < 1e-6 or amp <= 0:
            return pts
        amp = amp * min(1.0, (per / 70.0) ** 0.6)
        r = self._rng
        ks = [max(1, round(per / r.uniform(34, 52))), max(1, round(per / r.uniform(13, 21)))]
        ph = [r.uniform(0, 2 * math.pi) for _ in ks]
        out = []
        for i, (x, y) in enumerate(pts):
            if closed:
                a, b = pts[(i - 1) % n], pts[(i + 1) % n]
            else:
                a, b = pts[max(0, i - 1)], pts[min(n - 1, i + 1)]
            tx, ty = b[0] - a[0], b[1] - a[1]
            ln = math.hypot(tx, ty) or 1.0
            nx, ny = -ty / ln, tx / ln
            d = amp * (0.72 * math.sin(2 * math.pi * ks[0] * s[i] / per + ph[0]) +
                       0.28 * math.sin(2 * math.pi * ks[1] * s[i] / per + ph[1]))
            out.append((x + nx * d, y + ny * d))
        return out

    def _trazar(self, pts, closed, stroke, fill):
        p = self.beginPath()
        p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        if closed:
            p.close()
        self.drawPath(p, stroke=stroke, fill=fill)

    @staticmethod
    def _tramo(a, b, paso=5.0):
        n = max(2, int(math.hypot(b[0] - a[0], b[1] - a[1]) / paso) + 1)
        return [(a[0] + (b[0] - a[0]) * i / (n - 1), a[1] + (b[1] - a[1]) * i / (n - 1)) for i in range(n)]

    # ---- primitivas
    def line(self, x1, y1, x2, y2):
        pts = self._wob(self._tramo((x1, y1), (x2, y2)))
        self._trazar(pts, False, 1, 0)

    def ellipse(self, x1, y1, x2, y2, stroke=1, fill=0):
        if not stroke:
            return super().ellipse(x1, y1, x2, y2, stroke=stroke, fill=fill)
        cx, cy, rx, ry = (x1 + x2) / 2.0, (y1 + y2) / 2.0, abs(x2 - x1) / 2.0, abs(y2 - y1) / 2.0
        per = math.pi * (3 * (rx + ry) - math.sqrt((3 * rx + ry) * (rx + 3 * ry)))
        n = max(24, int(per / 4))
        pts = [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n))
               for i in range(n)]
        self._trazar(self._wob(pts, True), True, 1, fill)

    def circle(self, x, y, r, stroke=1, fill=0):
        self.ellipse(x - r, y - r, x + r, y + r, stroke=stroke, fill=fill)

    def poly(self, pts, stroke=1, fill=0, closed=True):
        """Polígono (o poligonal abierta) con las aristas a mano."""
        todo = []
        seq = list(pts) + ([pts[0]] if closed else [])
        for a, b in zip(seq, seq[1:]):
            todo.extend(self._tramo(a, b)[:-1])
        todo.append(seq[-1])
        if closed:
            todo = todo[:-1]
        self._trazar(self._wob(todo, closed), closed, stroke, fill)

    def rect(self, x, y, w, h, stroke=1, fill=0):
        if not stroke:
            return super().rect(x, y, w, h, stroke=stroke, fill=fill)
        self.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], 1, fill)

    def roundRect(self, x, y, w, h, radius, stroke=1, fill=0):
        if not stroke:
            return super().roundRect(x, y, w, h, radius, stroke=stroke, fill=fill)
        r = max(0.1, min(radius, w / 2.0, h / 2.0))
        k = 7
        pts = []
        for (cx, cy, a0) in ((x + w - r, y + r, -90), (x + w - r, y + h - r, 0),
                             (x + r, y + h - r, 90), (x + r, y + r, 180)):
            for i in range(k + 1):
                a = math.radians(a0 + 90.0 * i / k)
                pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        todo = []
        for a, b in zip(pts, pts[1:] + pts[:1]):
            todo.extend(self._tramo(a, b)[:-1])
        self._trazar(self._wob(todo, True), True, 1, fill)

    def arc(self, x1, y1, x2, y2, startAng=0, extent=90):
        cx, cy, rx, ry = (x1 + x2) / 2.0, (y1 + y2) / 2.0, abs(x2 - x1) / 2.0, abs(y2 - y1) / 2.0
        per = abs(math.radians(extent)) * (rx + ry) / 2.0
        n = max(8, int(per / 4))
        pts = [(cx + rx * math.cos(math.radians(startAng + extent * i / n)),
                cy + ry * math.sin(math.radians(startAng + extent * i / n))) for i in range(n + 1)]
        self._trazar(self._wob(pts, False), False, 1, 0)


# ------------------------------------------------------------------ trazo y texto
def trazo(c, w=2.0, cap=1, join=1, col=black):
    c.setStrokeColor(col)
    c.setLineWidth(w)
    c.setLineCap(cap)
    c.setLineJoin(join)


def texto(c, x, y, txt, size=11, font='Hand', align='l', col=black):
    txt = txt.replace('\u2019', "'")          # la letra de mano no trae el apóstrofo tipográfico
    c.setFillColor(col)
    c.setFont(font, size)
    if align == 'c':
        c.drawCentredString(x, y, txt)
    elif align == 'r':
        c.drawRightString(x, y, txt)
    else:
        c.drawString(x, y, txt)


def letras_huecas(c, cx, y, txt, size, rim=1.8, fat=1.4, sep=2.4, giro=2.2, font='Sketch',
                  align='c', semilla=3):
    """Letras gordas HUECAS (contorno negro, interior blanco para pintar), cada una un poco
       torcida y fuera de la línea, como rotuladas a mano."""
    rnd = random.Random(semilla)
    ws = [stringWidth(ch, font, size) for ch in txt]
    total = sum(ws) + sep * (len(txt) - 1)
    x = cx - total / 2 if align == 'c' else cx
    c.saveState()
    for ch, w in zip(txt, ws):
        if ch != ' ':
            c.saveState()
            c.translate(x + w / 2, y + rnd.uniform(-1.8, 1.8))
            c.rotate(rnd.uniform(-giro, giro))
            for modo, lw, col in ((1, (fat + rim) * 2, black), (2, fat * 2, white)):
                t = c.beginText(-w / 2, 0)
                t.setFont(font, size * rnd.uniform(0.97, 1.03))
                t.setTextRenderMode(modo)
                c.setLineWidth(lw)
                c.setLineJoin(1)
                c.setLineCap(1)
                c.setStrokeColor(col)
                c.setFillColor(col)
                t.textOut(ch)
                c.drawText(t)
            c.restoreState()
        x += w + sep
    c.restoreState()
    c.setFillColor(black)
    return total


def caja(c, x, y, w, h, r=8, lw=2.2, fill=True, dash=None, col=black, relleno=white):
    trazo(c, lw, col=col)
    if dash:
        c.setDash(*dash)
    c.setFillColor(relleno)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1 if fill else 0)
    c.setDash()


def marco(c, col=black):
    caja(c, 12, 12, W - 24, H - 24, r=18, lw=3.0, fill=False, col=col)
    caja(c, 19, 19, W - 38, H - 38, r=13, lw=1.0, fill=False, dash=(1, 4), col=col)


# ------------------------------------------------------------------ dibujos sueltos
def estrella(c, cx, cy, r, giro=0, relleno=white, col=black, lw=2.0):
    pts = []
    for i in range(10):
        a = math.pi / 2 + giro + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.46
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    trazo(c, lw, col=col)
    c.setFillColor(relleno)
    c.poly(pts, 1, 1)


def cabeza(c, cx, cy, rx, ry, giro=-20, grosor=2.0, rayada=False, relleno=white):
    c.saveState()
    c.translate(cx, cy)
    c.rotate(giro)
    trazo(c, grosor)
    c.setFillColor(relleno)
    c.ellipse(-rx, -ry, rx, ry, stroke=1, fill=1)
    if rayada:
        p = c.beginPath()
        p.ellipse(-rx, -ry, rx, ry)
        c.clipPath(p, stroke=0, fill=0)
        trazo(c, 1.1, cap=0)
        k = -rx
        while k < rx + ry:
            c.line(k, -ry, k + ry * 1.6, ry)
            k += max(3.2, rx * 0.38)
    c.restoreState()


def _bezier(p0, p1, p2, p3, n=10):
    out = []
    for i in range(n + 1):
        t = i / float(n)
        u = 1 - t
        out.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return out


def corchete(c, x, y, s, relleno=white):
    """El corchete (la banderita) de una corchea cuya plica termina en (x, y)."""
    pts = (_bezier((x, y), (x + 8 * s, y - 7 * s), (x + 16 * s, y - 12 * s), (x + 9 * s, y - 25 * s), 8) +
           _bezier((x + 9 * s, y - 25 * s), (x + 11 * s, y - 14 * s), (x + 5 * s, y - 9 * s),
                   (x, y - 8 * s), 8))
    trazo(c, 2.2 * s)
    c.setFillColor(relleno)
    c.poly(pts, 1, 1)


def negra_deco(c, x, y, s=1.0, corchea=False, rayada=True):
    cabeza(c, x, y, 9 * s, 6.5 * s, rayada=rayada)
    trazo(c, 2.4 * s, cap=0)
    c.line(x + 8.2 * s, y + 2 * s, x + 8.2 * s, y + 38 * s)
    if corchea:
        corchete(c, x + 8.2 * s, y + 38 * s, s)


def pareja_deco(c, x, y, s=1.0):
    cabeza(c, x, y, 8 * s, 5.8 * s, rayada=True)
    cabeza(c, x + 26 * s, y + 4 * s, 8 * s, 5.8 * s, rayada=True)
    trazo(c, 2.2 * s, cap=0)
    c.line(x + 7.3 * s, y + 2 * s, x + 7.3 * s, y + 36 * s)
    c.line(x + 33.3 * s, y + 6 * s, x + 33.3 * s, y + 40 * s)
    trazo(c, 2.2 * s)
    c.setFillColor(white)
    c.poly([(x + 7.3 * s, y + 36 * s), (x + 33.3 * s, y + 40 * s),
            (x + 33.3 * s, y + 32 * s), (x + 7.3 * s, y + 28 * s)], 1, 1)


def pareja_plana(c, x, y, s=1.0):
    d = 30 * s
    cabeza(c, x, y, 10 * s, 7.2 * s, rayada=True)
    cabeza(c, x + d, y, 10 * s, 7.2 * s, rayada=True)
    trazo(c, 2.6, cap=0)
    top = y + 46 * s
    c.line(x + 9.4 * s, y + 2 * s, x + 9.4 * s, top)
    c.line(x + d + 9.4 * s, y + 2 * s, x + d + 9.4 * s, top)
    trazo(c, 2.4)
    c.setFillColor(white)
    c.poly([(x + 9.4 * s, top), (x + d + 9.4 * s, top), (x + d + 9.4 * s, top - 7 * s),
            (x + 9.4 * s, top - 7 * s)], 1, 1)


def cara(c, cx, cy, r, mejillas=True, col=black):
    c.setFillColor(col)
    for dx in (-0.36, 0.36):
        c.circle(cx + dx * r, cy + 0.14 * r, r * 0.09, stroke=0, fill=1)
    trazo(c, max(1.6, r * 0.06), col=col)
    c.arc(cx - r * 0.3, cy - r * 0.34, cx + r * 0.3, cy + r * 0.04, 200, 140)
    if mejillas:
        trazo(c, 1.2, col=col)
        c.setFillColor(white)
        for dx in (-0.58, 0.58):
            c.circle(cx + dx * r, cy - 0.12 * r, r * 0.13, stroke=1, fill=1)


def sol(c, cx, cy, r):
    trazo(c, 3.0)
    for i in range(12):
        a = i * math.pi / 6 + 0.08
        c.line(cx + (r + 7) * math.cos(a), cy + (r + 7) * math.sin(a),
               cx + (r + 18 + 6 * (i % 2)) * math.cos(a), cy + (r + 18 + 6 * (i % 2)) * math.sin(a))
    trazo(c, 2.6)
    c.setFillColor(white)
    c.circle(cx, cy, r, stroke=1, fill=1)
    cara(c, cx, cy, r)


def nube(c, cx, cy, s=1.0):
    circ = [(-46, -6, 22), (-20, 12, 28), (14, 16, 31), (44, -2, 24), (0, -10, 26)]
    trazo(c, 2.6)
    for dx, dy, r in circ:
        c.circle(cx + dx * s, cy + dy * s, r * s, stroke=1, fill=0)
    c.roundRect(cx - 60 * s, cy - 36 * s, 120 * s, 26 * s, 13 * s, stroke=1, fill=0)
    c.setFillColor(white)
    for dx, dy, r in circ:
        c.circle(cx + dx * s, cy + dy * s, r * s - 2.2, stroke=0, fill=1)
    c.roundRect(cx - 60 * s + 2.2, cy - 36 * s + 2.2, 120 * s - 4.4, 26 * s - 4.4, 13 * s,
                stroke=0, fill=1)
    c.rect(cx - 46 * s, cy - 30 * s, 90 * s, 30 * s, stroke=0, fill=1)
    cara(c, cx, cy + 4 * s, 24 * s)


def arcoiris(c, cx, base, rx, ry, bandas=6, paso=17):
    trazo(c, 2.0)
    for i in range(bandas + 1):
        a, b = rx - i * paso, ry - i * paso * ry / rx
        c.arc(cx - a, base - b, cx + a, base + b, 0, 180)


def pentagrama(c, x, ytop, w, gap, lw=1.1):
    trazo(c, lw, cap=0)
    a = c.amp
    c.amp = a * 0.35
    for i in range(5):
        c.line(x, ytop - i * gap, x + w, ytop - i * gap)
    c.amp = a
    return ytop - 4 * gap


def cabeza_redonda(c, cx, cy, gap, relleno=white):
    trazo(c, 1.9)
    c.setFillColor(relleno)
    c.ellipse(cx - gap * 0.82, cy - gap * 0.55, cx + gap * 0.82, cy + gap * 0.55, stroke=1, fill=1)
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-30)
    trazo(c, 1.2)
    c.ellipse(-gap * 0.24, -gap * 0.46, gap * 0.24, gap * 0.46, stroke=1, fill=0)
    c.restoreState()


def rayita(c, cx, y, gap):
    trazo(c, 1.4, cap=0)
    c.line(cx - gap * 1.25, y, cx + gap * 1.25, y)


def subrayado_ondulado(c, x1, x2, y, amp=2.6, lam=22, lw=2.0):
    """Una línea ondulada de rotulador, para subrayar títulos."""
    trazo(c, lw)
    pts = []
    n = max(8, int((x2 - x1) / 3))
    for i in range(n + 1):
        xx = x1 + (x2 - x1) * i / n
        pts.append((xx, y + amp * math.sin((xx - x1) / lam * 2 * math.pi)))
    a = c.amp
    c.amp = 0.3
    c.poly(pts, 1, 0, closed=False)
    c.amp = a


def flecha(c, x1, y1, x2, y2, curva=18, lw=2.0):
    """Flecha curvada dibujada a mano, de (x1,y1) hacia (x2,y2)."""
    mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy) or 1.0
    cx_, cy_ = mx - dy / ln * curva, my + dx / ln * curva
    pts = [((1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx_ + t * t * x2,
            (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy_ + t * t * y2) for t in [i / 14.0 for i in range(15)]]
    trazo(c, lw)
    c.poly(pts, 1, 0, closed=False)
    ang = math.atan2(pts[-1][1] - pts[-3][1], pts[-1][0] - pts[-3][0])
    for da in (2.6, -2.6):
        c.line(x2, y2, x2 - 9 * math.cos(ang + da * 0.28), y2 - 9 * math.sin(ang + da * 0.28))


def lineas_texto(txt, font, size, max_w):
    out, cur = [], ''
    for p in txt.split(' '):
        prueba = (cur + ' ' + p).strip()
        if stringWidth(prueba, font, size) <= max_w:
            cur = prueba
        else:
            out.append(cur)
            cur = p
    if cur:
        out.append(cur)
    return out
