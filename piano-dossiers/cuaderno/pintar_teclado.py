# -*- coding: utf-8 -*-
"""Hojas para PINTAR en blanco y negro (A4 apaisado): el teclado de las notas y tres
   ejercicios a juego. Todo en contorno, sin rellenos de gris, para imprimir y colorear.

   Las alturas de las notas se calculan con `engine/notation.note_y`, no a ojo:
   DO central con su rayita, RE justo debajo de la primera línea, MI sobre ella, etc.

   Se ejecuta con:  python3 pintar_teclado.py   ->  ../output/Pintar_Teclado_y_Notas.pdf
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
import notation as nt                                        # noqa: E402
from reportlab.pdfgen import canvas                          # noqa: E402
from reportlab.lib.colors import black, white                # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth         # noqa: E402

W, H = 841.89, 595.276
OUT = os.path.join(HERE, '..', 'output', 'Pintar_Teclado_y_Notas.pdf')
BOLD = 'DejaVuSans-Bold'

# (nombre, altura, color con el que se pintaba la tecla)
NOTAS = [('DO', 'C4', 'ROJO'), ('RE', 'D4', 'NARANJA'), ('MI', 'E4', 'AMARILLO'),
         ('FA', 'F4', 'VERDE'), ('SOL', 'G4', 'AZUL'), ('LA', 'A4', 'MORADO'),
         ('SI', 'B4', 'GRIS'), ('DO', 'C5', 'ROJO')]


# ---------------------------------------------------------------- utilidades
def trazo(c, w=2.0, cap=1, join=1):
    c.setStrokeColor(black)
    c.setLineWidth(w)
    c.setLineCap(cap)
    c.setLineJoin(join)


def letras(c, cx, y, txt, size, rim=1.9, fat=1.5, sep=2.6, align='c'):
    """Letras gordas HUECAS: contorno negro, interior blanco para pintar."""
    ws = [stringWidth(ch, BOLD, size) for ch in txt]
    total = sum(ws) + sep * (len(txt) - 1)
    x = cx - total / 2 if align == 'c' else cx
    c.saveState()
    for ch, w in zip(txt, ws):
        if ch != ' ':
            for modo, lw, col in ((1, (fat + rim) * 2, black), (2, fat * 2, white)):
                t = c.beginText(x, y)
                t.setFont(BOLD, size)
                t.setTextRenderMode(modo)
                c.setLineWidth(lw)
                c.setLineJoin(1)
                c.setLineCap(1)
                c.setStrokeColor(col)
                c.setFillColor(col)
                t.textOut(ch)
                c.drawText(t)
        x += w + sep
    c.restoreState()
    c.setFillColor(black)
    return total


def texto(c, x, y, txt, size=10, font='DejaVuSans', align='l', col=black):
    c.setFillColor(col)
    c.setFont(font, size)
    if align == 'c':
        c.drawCentredString(x, y, txt)
    elif align == 'r':
        c.drawRightString(x, y, txt)
    else:
        c.drawString(x, y, txt)


def caja(c, x, y, w, h, r=8, lw=2.2, fill=True, dash=None):
    trazo(c, lw)
    if dash:
        c.setDash(*dash)
    c.setFillColor(white)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1 if fill else 0)
    c.setDash()


def marco(c):
    caja(c, 12, 12, W - 24, H - 24, r=18, lw=3.2, fill=False)
    caja(c, 19, 19, W - 38, H - 38, r=13, lw=1.0, fill=False, dash=(1, 4))


def estrella(c, cx, cy, r, giro=0):
    pts = []
    for i in range(10):
        a = math.pi / 2 + giro + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.46
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    trazo(c, 2.0)
    c.setFillColor(white)
    c.drawPath(p, stroke=1, fill=1)


def cabeza(c, cx, cy, rx, ry, giro=-20, grosor=2.0, rayada=False):
    c.saveState()
    c.translate(cx, cy)
    c.rotate(giro)
    trazo(c, grosor)
    c.setFillColor(white)
    c.ellipse(-rx, -ry, rx, ry, stroke=1, fill=1)
    if rayada:                       # la negra va "rellena": rayas para pintar encima
        p = c.beginPath()
        p.ellipse(-rx, -ry, rx, ry)
        c.clipPath(p, stroke=0, fill=0)
        trazo(c, 1.1, cap=0)
        k = -rx
        while k < rx + ry:
            c.line(k, -ry, k + ry * 1.6, ry)
            k += max(3.2, rx * 0.38)
    c.restoreState()


def negra_deco(c, x, y, s=1.0, corchea=False, rayada=True):
    """Una nota de adorno: cabeza hueca, plica y, si toca, el corchete."""
    cabeza(c, x, y, 9 * s, 6.5 * s, rayada=rayada)
    trazo(c, 2.4 * s, cap=0)
    c.line(x + 8.2 * s, y + 2 * s, x + 8.2 * s, y + 38 * s)
    if corchea:
        p = c.beginPath()
        p.moveTo(x + 8.2 * s, y + 38 * s)
        p.curveTo(x + 16 * s, y + 31 * s, x + 24 * s, y + 25 * s, x + 18 * s, y + 13 * s)
        p.curveTo(x + 21 * s, y + 24 * s, x + 14 * s, y + 28 * s, x + 8.2 * s, y + 29 * s)
        p.close()
        c.setFillColor(white)
        c.drawPath(p, stroke=1, fill=1)


def pareja_deco(c, x, y, s=1.0):
    cabeza(c, x, y, 8 * s, 5.8 * s, rayada=True)
    cabeza(c, x + 26 * s, y + 4 * s, 8 * s, 5.8 * s, rayada=True)
    trazo(c, 2.2 * s, cap=0)
    c.line(x + 7.3 * s, y + 2 * s, x + 7.3 * s, y + 36 * s)
    c.line(x + 33.3 * s, y + 6 * s, x + 33.3 * s, y + 40 * s)
    p = c.beginPath()
    p.moveTo(x + 7.3 * s, y + 36 * s)
    p.lineTo(x + 33.3 * s, y + 40 * s)
    p.lineTo(x + 33.3 * s, y + 32 * s)
    p.lineTo(x + 7.3 * s, y + 28 * s)
    p.close()
    c.setFillColor(white)
    c.drawPath(p, stroke=1, fill=1)


def pareja_plana(c, x, y, s=1.0):
    """Dos corcheas unidas por una barra, en la misma linea (para las hojas de ritmo)."""
    d = 30 * s
    cabeza(c, x, y, 10 * s, 7.2 * s, rayada=True)
    cabeza(c, x + d, y, 10 * s, 7.2 * s, rayada=True)
    trazo(c, 2.6, cap=0)
    top = y + 46 * s
    c.line(x + 9.4 * s, y + 2 * s, x + 9.4 * s, top)
    c.line(x + d + 9.4 * s, y + 2 * s, x + d + 9.4 * s, top)
    p = c.beginPath()
    p.moveTo(x + 9.4 * s, top)
    p.lineTo(x + d + 9.4 * s, top)
    p.lineTo(x + d + 9.4 * s, top - 7 * s)
    p.lineTo(x + 9.4 * s, top - 7 * s)
    p.close()
    c.setFillColor(white)
    c.drawPath(p, stroke=1, fill=1)


def cara(c, cx, cy, r, mejillas=True):
    c.setFillColor(black)
    for dx in (-0.36, 0.36):
        c.circle(cx + dx * r, cy + 0.14 * r, r * 0.09, stroke=0, fill=1)
    trazo(c, max(1.6, r * 0.06))
    c.arc(cx - r * 0.3, cy - r * 0.34, cx + r * 0.3, cy + r * 0.04, 200, 140)
    if mejillas:
        trazo(c, 1.2)
        c.setFillColor(white)
        for dx in (-0.58, 0.58):
            c.circle(cx + dx * r, cy - 0.12 * r, r * 0.13, stroke=1, fill=1)


def sol(c, cx, cy, r):
    trazo(c, 3.2)
    for i in range(12):
        a = i * math.pi / 6
        c.line(cx + (r + 7) * math.cos(a), cy + (r + 7) * math.sin(a),
               cx + (r + 19 + 5 * (i % 2)) * math.cos(a), cy + (r + 19 + 5 * (i % 2)) * math.sin(a))
    trazo(c, 2.6)
    c.setFillColor(white)
    c.circle(cx, cy, r, stroke=1, fill=1)
    cara(c, cx, cy, r)


def nube(c, cx, cy, s=1.0):
    circ = [(-46, -6, 22), (-20, 12, 28), (14, 16, 31), (44, -2, 24), (0, -10, 26)]
    trazo(c, 2.6)
    c.setFillColor(white)
    for dx, dy, r in circ:
        c.circle(cx + dx * s, cy + dy * s, r * s, stroke=1, fill=0)
    c.roundRect(cx - 60 * s, cy - 36 * s, 120 * s, 26 * s, 13 * s, stroke=1, fill=0)
    for dx, dy, r in circ:                      # el relleno blanco borra los trazos interiores
        c.circle(cx + dx * s, cy + dy * s, r * s - 1.3, stroke=0, fill=1)
    c.roundRect(cx - 60 * s + 1.3, cy - 36 * s + 1.3, 120 * s - 2.6, 26 * s - 2.6, 13 * s, stroke=0, fill=1)
    c.rect(cx - 46 * s, cy - 30 * s, 90 * s, 30 * s, stroke=0, fill=1)
    cara(c, cx, cy + 4 * s, 24 * s)


def arcoiris(c, cx, base, rx, ry, bandas=6, paso=14):
    trazo(c, 2.0)
    for i in range(bandas + 1):
        a, b = rx - i * paso, ry - i * paso * ry / rx
        c.arc(cx - a, base - b, cx + a, base + b, 0, 180)


def buho(c, cx, cy, s=1.0):
    """Misol Misol, en contorno."""
    trazo(c, 2.4 * s)
    c.setFillColor(white)
    # orejas
    for sg in (-1, 1):
        p = c.beginPath()
        p.moveTo(cx + sg * 30 * s, cy + 52 * s)
        p.lineTo(cx + sg * 38 * s, cy + 78 * s)
        p.lineTo(cx + sg * 14 * s, cy + 62 * s)
        p.close()
        c.drawPath(p, stroke=1, fill=1)
    # alas y cuerpo
    for sg in (-1, 1):
        c.ellipse(cx + sg * 44 * s - 11 * s, cy - 24 * s, cx + sg * 44 * s + 11 * s, cy + 34 * s,
                  stroke=1, fill=1)
    c.ellipse(cx - 42 * s, cy - 44 * s, cx + 42 * s, cy + 60 * s, stroke=1, fill=1)
    # barriga con plumitas
    c.ellipse(cx - 24 * s, cy - 38 * s, cx + 24 * s, cy + 6 * s, stroke=1, fill=1)
    trazo(c, 1.6 * s)
    for k in range(3):
        for dx in (-12, 0, 12):
            yy = cy - 28 * s + k * 12 * s
            c.arc(cx + dx * s - 7 * s, yy - 4 * s, cx + dx * s + 7 * s, yy + 6 * s, 200, 140)
    # ojos
    trazo(c, 2.2 * s)
    c.setFillColor(white)
    for sg in (-1, 1):
        c.circle(cx + sg * 16 * s, cy + 36 * s, 14 * s, stroke=1, fill=1)
        c.setFillColor(black)
        c.circle(cx + sg * 16 * s + 2 * s * sg * -1, cy + 35 * s, 5.2 * s, stroke=0, fill=1)
        c.setFillColor(white)
    # pico
    p = c.beginPath()
    p.moveTo(cx - 6 * s, cy + 26 * s)
    p.lineTo(cx + 6 * s, cy + 26 * s)
    p.lineTo(cx, cy + 16 * s)
    p.close()
    c.setFillColor(white)
    c.drawPath(p, stroke=1, fill=1)
    # patitas
    trazo(c, 2.2 * s)
    for sg in (-1, 1):
        c.line(cx + sg * 12 * s, cy - 44 * s, cx + sg * 12 * s, cy - 52 * s)
        c.line(cx + sg * 12 * s - 5 * s, cy - 52 * s, cx + sg * 12 * s + 5 * s, cy - 52 * s)


def pentagrama(c, x, ytop, w, gap):
    trazo(c, 1.1, cap=0)
    for i in range(5):
        c.line(x, ytop - i * gap, x + w, ytop - i * gap)
    return ytop - 4 * gap          # linea de abajo (Mi4)


def cabeza_redonda(c, cx, cy, gap):
    """Redonda grande y hueca: se pinta entera."""
    trazo(c, 1.9)
    c.setFillColor(white)
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


def nombre_pie(c, texto_extra=''):
    texto(c, 40, 30, 'Nombre:', 11, BOLD)
    trazo(c, 1.2, cap=0)
    c.setDash(1, 3)
    c.line(96, 28, 250, 28)
    c.setDash()
    if texto_extra:
        texto(c, W - 40, 30, texto_extra, 9, 'DejaVuSans', 'r')


def cabecera(c, l1, l2=None, size=44, y1=520, y2=476):
    marco(c)
    letras(c, W / 2, y1, l1, size)
    if l2:
        letras(c, W / 2, y2, l2, size)


# ------------------------------------------------------------- hoja 1: teclado
def hoja_teclado(c):
    marco(c)
    letras(c, W / 2, 506, 'EL TECLADO DE', 46)
    letras(c, W / 2, 458, 'LAS NOTAS', 46)
    sol(c, 98, 498, 36)
    nube(c, 752, 494, 1.05)
    estrella(c, 190, 446, 16)
    estrella(c, 668, 452, 13, 0.3)
    negra_deco(c, 62, 396, 1.0, corchea=True)
    pareja_deco(c, 112, 420, 0.8)
    negra_deco(c, 735, 398, 1.0)
    negra_deco(c, 785, 404, 0.9, corchea=True)

    # arcoiris detras de las teclas
    arcoiris(c, W / 2, 296, 372, 128, bandas=6, paso=17)

    kw, gp = 88, 8.7
    x0 = (W - (8 * kw + 7 * gp)) / 2
    ytop, ybot = 292, 128
    for i, (nombre, alt, color) in enumerate(NOTAS):
        x = x0 + i * (kw + gp)
        caja(c, x, ybot - 8, kw, ytop - ybot, r=11, lw=2.6)        # sombra / peana
        caja(c, x, ybot, kw, ytop - ybot, r=11, lw=2.8)
        letras(c, x + kw / 2, ytop - 52, nombre, 30 if len(nombre) < 3 else 25,
               rim=1.6, fat=1.2, sep=1.8)
        # mini pentagrama con clave y la nota
        gap = 7.4
        sy = ybot + 56
        yb = pentagrama(c, x + 10, sy, kw - 20, gap)
        nt.draw_clef(c, x + 11, yb, gap)
        ny = nt.note_y(yb, gap, alt)
        nx = x + kw - 27
        if alt == 'C4':
            rayita(c, nx, ny, gap * 0.95)
        cabeza_redonda(c, nx, ny, gap * 1.15)
        # etiqueta del color
        caja(c, x + 6, 84, kw - 12, 22, r=9, lw=1.8)
        texto(c, x + kw / 2, 91, color, 9.5, BOLD, 'c')

    estrella(c, 48, 66, 13)
    estrella(c, W - 50, 62, 15, 0.2)
    texto(c, W / 2, 58, 'Pinta cada tecla del color que dice su etiqueta... ¡y el arcoíris también!',
          10.5, BOLD, 'c')
    nombre_pie(c)
    c.showPage()


# ---------------------------------------------------- hoja 2: teclas del piano
def hoja_piano(c):
    cabecera(c, 'LAS TECLAS DEL PIANO', None, 40, 512)
    estrella(c, 70, 500, 15)
    estrella(c, W - 70, 505, 13, 0.3)
    pareja_deco(c, W - 130, 430, 0.8)
    negra_deco(c, 50, 392, 0.85)

    # instrucciones
    pasos = [('1', 'Pinta de AZUL los grupos de DOS teclas negras.'),
             ('2', 'Pinta de VERDE los grupos de TRES teclas negras.'),
             ('3', 'Pinta de ROJO todas las teclas DO (a la izquierda de las dos negras).'),
             ('4', 'Escribe en cada cajita el nombre de la nota.')]
    yy = 470
    for n_, t in pasos:
        trazo(c, 2.2)
        c.setFillColor(white)
        c.circle(86, yy + 4, 11, stroke=1, fill=1)
        texto(c, 86, yy, n_, 12, BOLD, 'c')
        texto(c, 106, yy, t, 12, 'DejaVuSans')
        yy -= 29

    # teclado de dos octavas
    nb = 14
    kx0, kw = 40, (W - 80) / nb
    ytop, ybot = 330, 190
    trazo(c, 2.2)
    for i in range(nb):
        c.setFillColor(white)
        c.roundRect(kx0 + i * kw, ybot, kw, ytop - ybot, 5, stroke=1, fill=1)
    # negras: despues de DO, RE, FA, SOL, LA
    pos = [0, 1, 3, 4, 5]
    for octv in range(2):
        for p_ in pos:
            i = octv * 7 + p_
            bx = kx0 + (i + 1) * kw - 0.31 * kw
            trazo(c, 2.4)
            c.setFillColor(white)
            c.roundRect(bx, ytop - 92, 0.62 * kw, 92, 4, stroke=1, fill=1)
    # cajitas de nombre
    nombres = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'] * 2
    for i, nm in enumerate(nombres):
        x = kx0 + i * kw + 4
        caja(c, x, 150, kw - 8, 30, r=8, lw=1.6, dash=(3, 2))
        if nm == 'DO':
            letras(c, x + (kw - 8) / 2, 158, 'DO', 14, rim=1.0, fat=0.9, sep=1.2)
    texto(c, W / 2, 128, '¡DO ya está escrito! Sigue tú: RE, MI, FA, SOL, LA, SI... y otra vez DO, RE, MI.',
          10.5, 'DejaVuSans', 'c')

    # truco con buho
    caja(c, 40, 52, 520, 62, r=12, lw=2.0)
    texto(c, 100, 94, 'El truco de Misol Misol', 10.5, BOLD)
    texto(c, 100, 78, 'En el piano las teclas negras van en grupos de DOS y de TRES.', 9.5)
    texto(c, 100, 64, 'El DO es siempre la tecla blanca justo ANTES de las dos negras.', 9.5)
    buho(c, 66, 70, 0.42)
    # mini ejemplo
    estrella(c, 640, 90, 14)
    estrella(c, 700, 70, 10, 0.4)
    negra_deco(c, 740, 60, 0.9)
    nombre_pie(c)
    c.showPage()


# ------------------------------------------------ hoja 3: pinta la melodia
def hoja_melodia(c):
    cabecera(c, 'PINTA LA MELODÍA', None, 40, 524)
    sol(c, 80, 520, 22)
    nube(c, W - 90, 516, 0.7)

    # leyenda de colores (los mismos del teclado)
    texto(c, W / 2, 486, 'Pinta cada nota del color de su tecla y escribe su nombre en la cajita.', 11, BOLD, 'c')
    tw, tg = 84, 7
    tx0 = (W - (8 * tw + 7 * tg)) / 2
    for i, (nm, alt, color) in enumerate(NOTAS):
        x = tx0 + i * (tw + tg)
        caja(c, x, 440, tw, 38, r=9, lw=1.8)
        texto(c, x + tw / 2, 461, nm, 12, BOLD, 'c')
        texto(c, x + tw / 2, 447, color, 8.5, 'DejaVuSans', 'c')

    gap = 9.5
    lineas = [
        (396, ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'], 'Sube por la escalera'),
        (276, ['E4', 'D4', 'C4', 'D4', 'E4', 'E4', 'E4'], 'Baja y sube'),
        (156, ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4'], '¿Qué canción es?'),
    ]
    for k, (ytop, notas, etiqueta) in enumerate(lineas):
        texto(c, 44, ytop + 16, '%d · %s' % (k + 1, etiqueta), 10.5, BOLD)
        if k == 2:
            trazo(c, 1.2, cap=0)
            c.setDash(1, 3)
            c.line(222, ytop + 14, 440, ytop + 14)
            c.setDash()
            texto(c, 452, ytop + 16, 'Pista: se canta de noche, mirando al cielo.', 9.5)
        yb = pentagrama(c, 44, ytop, W - 88, gap)
        nt.draw_clef(c, 50, yb, gap)
        paso = (W - 88 - 90) / 8.0
        for kk, alt in enumerate(notas):
            nx = 44 + 96 + kk * paso + paso / 2 - 10
            ny = nt.note_y(yb, gap, alt)
            if alt == 'C4':
                rayita(c, nx, ny, gap)
            cabeza_redonda(c, nx, ny, gap * 1.1)
            caja(c, nx - 22, yb - 52, 44, 24, r=7, lw=1.4, dash=(3, 2))
    estrella(c, W - 60, 60, 14)
    negra_deco(c, W - 120, 46, 0.7, corchea=True)
    pareja_deco(c, 300, 40, 0.65)
    nombre_pie(c)
    c.showPage()


# ---------------------------------------------------- hoja 4: pinta el ritmo
def figura(c, tipo, cx, base, s=1.0):
    """Una figura en contorno. La negra lleva la cabeza rayada ('rellena')."""
    if tipo == 'w':
        cabeza_redonda(c, cx, base, 13 * s)
        return
    cabeza(c, cx, base, 11 * s, 7.8 * s, giro=-20, grosor=2.2, rayada=(tipo in ('q', 'e')))
    trazo(c, 2.6, cap=0)
    c.line(cx + 10 * s, base + 2 * s, cx + 10 * s, base + 46 * s)
    if tipo == 'e':
        p = c.beginPath()
        p.moveTo(cx + 10 * s, base + 46 * s)
        p.curveTo(cx + 22 * s, base + 38 * s, cx + 34 * s, base + 28 * s, cx + 26 * s, base + 12 * s)
        p.curveTo(cx + 28 * s, base + 28 * s, cx + 20 * s, base + 33 * s, cx + 10 * s, base + 34 * s)
        p.close()
        c.setFillColor(white)
        c.drawPath(p, stroke=1, fill=1)


def linea_ritmo(c, x0, yc, bw, compases, titulo):
    """Una linea de 4 compases de 4/4 sobre una sola raya. `yc` es la raya."""
    trazo(c, 1.6, cap=0)
    c.line(x0, yc, x0 + 4 * bw, yc)
    for b in range(5):
        c.line(x0 + b * bw, yc + 20, x0 + b * bw, yc - 20)
    trazo(c, 3.2, cap=0)
    c.line(x0 + 4 * bw - 4, yc + 20, x0 + 4 * bw - 4, yc - 20)
    texto(c, x0, yc + 54, titulo, 9.5, BOLD)
    golpes = {'w': 4, 'h': 2, 'q': 1, 'ee': 1}
    for b, comp in enumerate(compases):
        total = sum(golpes[f] for f in comp)
        ancho = bw - 40
        xx = x0 + b * bw + 22
        for f in comp:
            dur = golpes[f]
            tam = dur * ancho / total
            if f == 'ee':
                pareja_plana(c, xx + tam / 2 - 25, yc, 0.9)
            else:
                figura(c, f, xx + tam / 2 - 4, yc, 0.95)
            xx += tam


def hoja_ritmo(c):
    cabecera(c, 'PINTA EL RITMO', None, 40, 524)
    sol(c, 80, 520, 22)
    buho(c, W - 86, 498, 0.5)
    texto(c, W / 2, 486, 'Elige un color para cada figura, pinta su casilla redonda y luego las figuras de abajo.',
          10.5, BOLD, 'c')

    figs = [('w', 'REDONDA', '4 golpes'), ('h', 'BLANCA', '2 golpes'),
            ('q', 'NEGRA', '1 golpe'), ('e', 'CORCHEA', 'medio golpe')]
    cw, cg = 180, 14
    cx0 = (W - (4 * cw + 3 * cg)) / 2
    for i, (tp, nm, gl) in enumerate(figs):
        x = cx0 + i * (cw + cg)
        caja(c, x, 346, cw, 124, r=12, lw=2.2)
        trazo(c, 2.0)
        c.setFillColor(white)
        c.circle(x + cw - 20, 448, 12, stroke=1, fill=1)
        texto(c, x + cw - 20, 427, 'mi color', 7.5, 'DejaVuSans', 'c')
        figura(c, tp, x + 36, 388, 1.25)
        texto(c, x + 70, 444, nm, 11.5, BOLD)
        texto(c, x + 70, 428, gl, 9.5)
        nb = {'w': 4, 'h': 2, 'q': 1, 'e': 1}[tp]
        for k in range(nb):
            trazo(c, 1.6)
            c.setFillColor(white)
            if tp == 'e':
                c.circle(x + 84, 400, 6, stroke=1, fill=1)
                c.line(x + 84, 394, x + 84, 406)
            else:
                c.circle(x + 84 + k * 17, 400, 6, stroke=1, fill=1)

    ritmos = [
        [['q', 'q', 'h'], ['w'], ['h', 'q', 'q'], ['ee', 'ee', 'h']],
        [['ee', 'ee', 'q', 'q'], ['h', 'q', 'q'], ['q', 'ee', 'q', 'q'], ['w']],
    ]
    bw = (W - 100) / 4.0
    linea_ritmo(c, 50, 272, bw, ritmos[0], 'Ritmo 1')
    linea_ritmo(c, 50, 168, bw, ritmos[1], 'Ritmo 2')

    # tercera linea para inventar
    yc = 66
    trazo(c, 1.6, cap=0)
    c.line(50, yc, 50 + 4 * bw, yc)
    for b in range(5):
        c.line(50 + b * bw, yc + 20, 50 + b * bw, yc - 20)
    trazo(c, 3.2, cap=0)
    c.line(50 + 4 * bw - 4, yc + 20, 50 + 4 * bw - 4, yc - 20)
    texto(c, 50, yc + 28, 'Ritmo 3 · ¡inventa el tuyo! Dibuja figuras (cada compás suma CUATRO golpes) y píntalas.', 9.5, BOLD)
    nombre_pie(c)
    c.showPage()


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle('El teclado de las notas · hojas para pintar')
    hoja_teclado(c)
    hoja_piano(c)
    hoja_melodia(c)
    hoja_ritmo(c)
    c.save()
    print('generado', OUT)


if __name__ == '__main__':
    main()
