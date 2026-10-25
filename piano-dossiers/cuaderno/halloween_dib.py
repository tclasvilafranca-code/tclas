# -*- coding: utf-8 -*-
"""Dibujos de Halloween a mano alzada (ManoCanvas), para pintar: todo con el interior blanco.
   Cada funcion dibuja centrada en (cx, cy) y a escala `s` (1.0 = unos 100 pt de alto)."""
import math

from reportlab.lib.colors import black, white

from dibujo_mano import trazo, caja


def _T(cx, cy, s):
    return lambda x, y: (cx + x * s, cy + y * s)


def _poli(c, T, pts, lw=2.2, fill=1, closed=True, relleno=white):
    trazo(c, lw)
    c.setFillColor(relleno)
    c.poly([T(*p) for p in pts], 1, fill, closed=closed)


def _el(c, T, s, x, y, rx, ry, lw=2.2, fill=1, giro=0, relleno=white):
    trazo(c, lw)
    c.setFillColor(relleno)
    c.saveState()
    px, py = T(x, y)
    c.translate(px, py)
    c.rotate(giro)
    c.ellipse(-rx * s, -ry * s, rx * s, ry * s, stroke=1, fill=fill)
    c.restoreState()


def _curva(p0, p1, p2, p3, n=10):
    out = []
    for i in range(n + 1):
        t = i / float(n)
        u = 1 - t
        out.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return out


# ------------------------------------------------------------------ carbassa
def carbassa(c, cx, cy, s=1.0, cara=True, lw=2.4):
    T = _T(cx, cy, s)
    # tija
    _poli(c, T, [(-7, 38), (-3, 58), (9, 56), (6, 36)], lw)
    _poli(c, T, [(6, 52), (22, 62), (34, 50), (22, 54), (14, 44)], lw * 0.8)
    # gajos laterales, luego el central
    _el(c, T, s, -34, 0, 30, 40, lw)
    _el(c, T, s, 34, 0, 30, 40, lw)
    _el(c, T, s, -17, 0, 26, 44, lw)
    _el(c, T, s, 17, 0, 26, 44, lw)
    _el(c, T, s, 0, 0, 20, 46, lw)
    if cara:
        trazo(c, lw)
        for sg in (-1, 1):
            c.setFillColor(black)
            c.poly([T(sg * 28, 22), T(sg * 12, 24), T(sg * 20, 8)], 1, 1)
        c.poly([T(-5, 2), T(5, 2), T(0, -8)], 1, 1)
        c.setFillColor(black)
        pts = [(-34, -14), (-24, -24), (-14, -14), (-6, -26), (0, -14), (6, -26), (14, -14),
               (24, -24), (34, -14), (26, -34), (0, -40), (-26, -34)]
        c.poly([T(*p) for p in pts], 1, 1)
        c.setFillColor(white)
        for x in (-14, 0, 14):
            c.poly([T(x - 4, -30), T(x + 4, -30), T(x, -37)], 0, 1)


# ------------------------------------------------------------------ fantasma
def fantasma(c, cx, cy, s=1.0, cara=True, brazos=True, lw=2.4, expr='bu'):
    T = _T(cx, cy, s)
    pts = []
    for i in range(0, 181, 12):
        a = math.radians(i)
        pts.append((38 * math.cos(a), 28 + 44 * math.sin(a)))
    pts += [(-38, 28), (-40, -20), (-38, -48)]
    # ondas del bajo
    n = 5
    base = []
    for k in range(n * 2 + 1):
        x = -38 + k * (76.0 / (n * 2))
        y = -52 if k % 2 == 0 else -38
        base.append((x, y))
    cuerpo = [(38, -48), (40, -20)][::-1] if False else []
    cuerpo = []
    for i in range(0, 181, 12):
        a = math.radians(i)
        cuerpo.append((38 * math.cos(a), 28 + 44 * math.sin(a)))
    cuerpo += [(-38, 10), (-40, -30)] + base + [(40, -30), (38, 10)]
    # el orden: arco de derecha a izquierda, baja por la izquierda, ondas hacia la derecha, sube
    _poli(c, T, cuerpo, lw)
    if brazos:
        _el(c, T, s, -46, 6, 14, 8, lw * 0.9, giro=-20)
        _el(c, T, s, 46, 30, 14, 8, lw * 0.9, giro=30)
    if cara:
        trazo(c, lw)
        for sg in (-1, 1):
            c.setFillColor(black)
            c.ellipse(*T(sg * 15 - 6, 36), *T(sg * 15 + 6, 18), stroke=1, fill=1)
        c.setFillColor(black)
        if expr == 'bu':
            c.ellipse(*T(-8, 12), *T(8, -10), stroke=1, fill=1)
        else:
            c.arc(*T(-14, 8), *T(14, -8), 200, 140)


# ------------------------------------------------------------------ murcielago
def murcielago(c, cx, cy, s=1.0, lw=2.2):
    T = _T(cx, cy, s)
    for sg in (-1, 1):
        ala = [(sg * 8, 6), (sg * 30, 22), (sg * 56, 24), (sg * 74, 10), (sg * 66, -4),
               (sg * 56, 2), (sg * 46, -12), (sg * 34, -2), (sg * 22, -16), (sg * 12, -6)]
        _poli(c, T, ala, lw)
    _el(c, T, s, 0, 0, 12, 18, lw)
    _el(c, T, s, 0, 20, 9, 8, lw)
    _poli(c, T, [(-8, 25), (-12, 38), (-3, 28)], lw * 0.9)
    _poli(c, T, [(8, 25), (12, 38), (3, 28)], lw * 0.9)
    trazo(c, 1.6)
    c.setFillColor(black)
    for sg in (-1, 1):
        c.circle(*T(sg * 3.5, 21), 1.6 * s, stroke=0, fill=1)


# ------------------------------------------------------------------ sombrero de bruja
def sombrero(c, cx, cy, s=1.0, lw=2.4, torcido=-8):
    c.saveState()
    c.translate(cx, cy)
    c.rotate(torcido)
    T = _T(0, 0, s)
    _poli(c, T, [(-24, 8), (-16, 60), (-4, 96), (14, 120), (10, 100), (22, 80), (28, 40), (34, 8)], lw)
    _el(c, T, s, 5, 6, 58, 12, lw)
    _poli(c, T, [(-22, 16), (32, 16), (30, 26), (-21, 26)], lw * 0.8)
    trazo(c, 1.6)
    c.setFillColor(white)
    c.rect(*T(0, 14), 6 * s, 14 * s, stroke=1, fill=1)
    c.restoreState()


# ------------------------------------------------------------------ luna
def luna(c, cx, cy, r=40, lw=2.6):
    trazo(c, lw)
    c.setFillColor(white)
    n = 36
    ext = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
           for a in range(100, 261, 8)]
    r2 = r * 0.82
    cx2 = cx + r * 0.48
    inn = [(cx2 + r2 * math.cos(math.radians(a)), cy + r2 * math.sin(math.radians(a)))
           for a in range(250, 109, -8)]
    c.poly(ext + inn, 1, 1)
    # cara
    c.setFillColor(black)
    c.circle(cx - r * 0.55, cy + r * 0.12, 2.2, stroke=0, fill=1)
    c.arc(cx - r * 0.72, cy - r * 0.45, cx - r * 0.18, cy - r * 0.05, 220, 100)


# ------------------------------------------------------------------ caldero
def caldero(c, cx, cy, s=1.0, lw=2.4):
    T = _T(cx, cy, s)
    for sg in (-1, 1):
        _poli(c, T, [(sg * 38, -46), (sg * 52, -66), (sg * 42, -68), (sg * 30, -50)], lw * 0.9)
    _el(c, T, s, 0, -6, 56, 44, lw)
    _el(c, T, s, 0, 34, 56, 14, lw)
    _el(c, T, s, 0, 36, 44, 8, lw * 0.8, relleno=white)
    trazo(c, lw * 0.8)
    c.setFillColor(white)
    for (x, y, r) in ((-22, 56, 9), (4, 70, 12), (28, 58, 7), (14, 90, 6)):
        c.circle(*T(x, y), r * s, stroke=1, fill=1)
    trazo(c, 1.6)
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 22 * s)
    # cara/rotulo sencillo: una estrella y puntos
    for (x, y) in ((-20, -6), (0, -16), (20, -6)):
        c.circle(*T(x, y), 2.2 * s, stroke=0, fill=1)


# ------------------------------------------------------------------ arana
def arana(c, cx, cy, s=1.0, lw=2.0, hilo=0):
    T = _T(cx, cy, s)
    if hilo:
        trazo(c, 1.3)
        c.line(cx, cy + 14 * s, cx, cy + hilo)
    trazo(c, lw)
    for sg in (-1, 1):
        for k, (dy, ex, ey) in enumerate(((10, 30, 26), (4, 38, 6), (-2, 38, -16), (-8, 28, -34))):
            pts = [(sg * 8, dy), (sg * (8 + ex * 0.5), dy + ey * 0.8 + 6), (sg * (8 + ex), dy + ey)]
            c.poly([T(*p) for p in pts], 1, 0, closed=False)
    _el(c, T, s, 0, 0, 14, 16, lw)
    _el(c, T, s, 0, 18, 8, 8, lw)
    trazo(c, 1.5)
    c.setFillColor(black)
    for sg in (-1, 1):
        c.circle(*T(sg * 3, 20), 1.7 * s, stroke=0, fill=1)


def telarana(c, x, y, r, esquina=0, lw=1.6):
    """Telaraña en una esquina (esquina=0: arriba-izquierda; 1: arriba-derecha)."""
    sg = 1 if esquina == 0 else -1
    trazo(c, lw)
    angs = [0, 18, 36, 54, 72, 90]
    for a in angs:
        rad = math.radians(a)
        c.line(x, y, x + sg * r * math.cos(rad), y - r * math.sin(rad))
    for k in range(1, 6):
        rk = r * k / 5.0
        pts = []
        for a in angs:
            rad = math.radians(a)
            pts.append((x + sg * rk * math.cos(rad), y - rk * math.sin(rad)))
        for i in range(len(pts) - 1):
            mx = (pts[i][0] + pts[i + 1][0]) / 2 - sg * 0.1 * rk
            my = (pts[i][1] + pts[i + 1][1]) / 2 + 0.1 * rk
            c.poly([pts[i], (mx, my), pts[i + 1]], 1, 0, closed=False)


# ------------------------------------------------------------------ calavera / hueso
def hueso(c, x1, y1, x2, y2, grosor=7, lw=2.0):
    ang = math.atan2(y2 - y1, x2 - x1)
    nx, ny = -math.sin(ang), math.cos(ang)
    trazo(c, lw)
    c.setFillColor(white)
    c.poly([(x1 + nx * grosor / 2, y1 + ny * grosor / 2), (x2 + nx * grosor / 2, y2 + ny * grosor / 2),
            (x2 - nx * grosor / 2, y2 - ny * grosor / 2), (x1 - nx * grosor / 2, y1 - ny * grosor / 2)],
           1, 1)
    for (x, y) in ((x1, y1), (x2, y2)):
        for sg in (-1, 1):
            c.circle(x + nx * sg * grosor * 0.75, y + ny * sg * grosor * 0.75, grosor * 0.75, stroke=1, fill=1)


def calavera(c, cx, cy, s=1.0, lw=2.3):
    T = _T(cx, cy, s)
    _el(c, T, s, 0, 8, 34, 32, lw)
    _poli(c, T, [(-20, -14), (20, -14), (18, -34), (-18, -34)], lw)
    trazo(c, lw)
    c.setFillColor(black)
    for sg in (-1, 1):
        c.ellipse(*T(sg * 15 - 9, 22), *T(sg * 15 + 9, 2), stroke=1, fill=1)
    c.poly([T(-4, -2), T(4, -2), T(0, -10)], 1, 1)
    trazo(c, 1.8)
    for k in (-12, -4, 4, 12):
        c.line(*T(k, -16), *T(k, -32))
    c.line(*T(-18, -22), *T(18, -22))


def esqueleto(c, cx, cy, s=1.0, lw=2.2, baile=0):
    """Esqueleto de pie; baile=1 levanta un brazo."""
    T = _T(cx, cy, s)
    calavera(c, cx, cy + 74 * s, s * 0.8, lw)
    # columna y costillas
    trazo(c, lw)
    c.line(*T(0, 44), *T(0, -6))
    for k, w in enumerate((26, 30, 28, 22)):
        y = 36 - k * 11
        c.setFillColor(white)
        c.ellipse(*T(-w, y + 5), *T(w, y - 5), stroke=1, fill=0)
    # pelvis
    _poli(c, T, [(-18, -8), (18, -8), (14, -26), (-14, -26)], lw)
    # brazos
    hueso(c, *T(-26, 38), *T(-54, 10), 6, lw * 0.9)
    hueso(c, *T(-54, 10), *T(-70, -18), 6, lw * 0.9)
    if baile:
        hueso(c, *T(26, 38), *T(54, 62), 6, lw * 0.9)
        hueso(c, *T(54, 62), *T(72, 92), 6, lw * 0.9)
    else:
        hueso(c, *T(26, 38), *T(54, 10), 6, lw * 0.9)
        hueso(c, *T(54, 10), *T(70, -18), 6, lw * 0.9)
    # piernas
    hueso(c, *T(-9, -24), *T(-22, -58), 7, lw * 0.9)
    hueso(c, *T(-22, -58), *T(-24, -92), 7, lw * 0.9)
    hueso(c, *T(9, -24), *T(24, -58), 7, lw * 0.9)
    hueso(c, *T(24, -58), *T(30, -90), 7, lw * 0.9)
    for (x, y) in ((-24, -94), (30, -92)):
        _el(c, T, s, x + (-6 if x < 0 else 6), y - 4, 14, 5, lw * 0.9)


# ------------------------------------------------------------------ bruja en escoba
def bruja(c, cx, cy, s=1.0, lw=2.4):
    """Bruja de perfil (mira a la derecha) sentada en su escoba voladora."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-9)
    T = _T(0, 0, s)
    # cepillo de la escoba (detras) y palo
    _poli(c, T, [(52, -30), (112, -8), (98, -28), (114, -48), (52, -34)], lw * 0.9)
    trazo(c, 1.5)
    for k in range(5):
        c.line(*T(62 + k * 7, -30 - k * 1.5), *T(104 + k * 2, -12 - k * 8.5))
    trazo(c, lw + 0.6)
    c.line(*T(-100, -32), *T(56, -32))
    # falda que vuela hacia atras
    _poli(c, T, [(-18, -26), (-84, -10), (-96, -36), (-58, -30), (-30, -36)], lw)
    # torso
    _poli(c, T, [(-24, -30), (14, -30), (12, 26), (-18, 30)], lw)
    # pierna y bota
    _poli(c, T, [(0, -30), (34, -34), (34, -44), (-2, -42)], lw * 0.9)
    _el(c, T, s, 40, -40, 10, 7, lw * 0.9)
    # brazo hacia el palo
    _poli(c, T, [(6, 14), (36, -10), (44, -4), (14, 22)], lw * 0.9)
    _el(c, T, s, 44, -22, 6, 6, lw * 0.8)
    # cabeza
    _el(c, T, s, -4, 48, 20, 21, lw)
    _poli(c, T, [(14, 52), (30, 46), (15, 42)], lw * 0.8)            # nariz
    trazo(c, 1.8)
    c.setFillColor(black)
    c.circle(*T(6, 52), 2.2 * s, stroke=0, fill=1)
    c.arc(*T(0, 34), *T(14, 46), 200, 140)
    for k in range(4):                                                # pelo
        c.line(*T(-18, 56 - k * 6), *T(-44, 46 - k * 10))
    c.restoreState()
    sombrero(c, cx - 8 * s, cy + 66 * s, s * 0.62, lw, torcido=-6)


# ------------------------------------------------------------------ casa encantada
def casa(c, cx, cy, s=1.0, lw=2.4):
    T = _T(cx, cy, s)
    _poli(c, T, [(-70, -60), (70, -60), (70, 30), (-70, 30)], lw)
    _poli(c, T, [(-84, 30), (0, 94), (84, 30)], lw)
    _poli(c, T, [(-22, 30), (-22, 74), (-6, 74), (-6, 30)], lw * 0.8)  # chimenea
    trazo(c, lw)
    c.setFillColor(white)
    # puerta
    c.roundRect(*T(-14, -60), 28 * s, 44 * s, 12 * s, stroke=1, fill=1)
    c.setFillColor(black)
    c.circle(*T(8, -38), 2.2 * s, stroke=0, fill=1)
    # ventanas
    for (x, y) in ((-46, -4), (30, -4)):
        trazo(c, lw * 0.9)
        c.setFillColor(white)
        c.rect(*T(x, y), 26 * s, 30 * s, stroke=1, fill=1)
        c.line(*T(x + 13, y), *T(x + 13, y + 30))
        c.line(*T(x, y + 15), *T(x + 26, y + 15))
    # ventana del tejado: ojo
    _el(c, T, s, 0, 58, 12, 12, lw * 0.9)
    trazo(c, 1.8)
    c.setFillColor(black)
    c.circle(*T(0, 58), 4 * s, stroke=0, fill=1)


# ------------------------------------------------------------------ dulce / caramelo
def caramelo(c, cx, cy, s=1.0, lw=2.2):
    T = _T(cx, cy, s)
    _poli(c, T, [(-22, 0), (-44, 14), (-40, -2), (-44, -16)], lw * 0.9)
    _poli(c, T, [(22, 0), (44, 14), (40, -2), (44, -16)], lw * 0.9)
    _el(c, T, s, 0, 0, 24, 15, lw)
    trazo(c, 1.5)
    for k in (-12, 0, 12):
        c.line(*T(k - 4, 12), *T(k + 4, -12))


def estrellitas(c, pts, r=7):
    from dibujo_mano import estrella
    for (x, y, k) in pts:
        estrella(c, x, y, r * k, lw=1.6)
