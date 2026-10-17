# -*- coding: utf-8 -*-
"""MUSOL MISOL — el buho profesor que acompana todo el dosier infantil.

   Pedido explicito del cliente: "en cada hoja o bloque de aprendizaje salga
   el Musol Misol... que pueda ir explicando cosas". Es el personaje que ya
   existia en el Canva original (la cancion "Mussol Misol Misol" de la
   portada) -- aqui se dibuja de cero, en vector puro, porque el dosier nuevo
   es en blanco y negro y no hay un PNG del personaje que reutilizar.

   Dibujado en trazo negro grueso sobre blanco -- el estilo "libro ilustrado
   infantil", no el estilo "partitura" del resto del motor. Por eso vive en
   su propio modulo y no en `notation.py` ni en `juegos_comun.py`.
"""
import math
import os
import sys

from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

INK = HexColor('#1A1A1A')
PAPER = white


def wrap_lines(texto, font, size, max_w):
    """Parte `texto` en lineas que quepan en `max_w` -- version que
       DEVUELVE la lista de lineas en vez de dibujarlas (la `_wrap` de
       `portada.py` dibuja directamente, y aqui el globo necesita saber
       cuantas lineas va a tener antes de centrar el texto dentro)."""
    lineas = []
    linea = ''
    for palabra in texto.split(' '):
        prueba = (linea + ' ' + palabra).strip()
        if stringWidth(prueba, font, size) <= max_w:
            linea = prueba
        else:
            if linea:
                lineas.append(linea)
            linea = palabra
    if linea:
        lineas.append(linea)
    return lineas


def musol_misol(c, cx, cy, r, pose='normal'):
    """El buho, centrado en (cx, cy): `cy` cae a la altura de su barriga
       (el centro visual del cuerpo), no de toda la caja -- con un radio r,
       ocupa aprox. 2.3r de alto y 1.8r de ancho.

       `pose`: 'normal' (las dos alas pegadas) o 'saluda' (un ala levantada,
       para la portada o los momentos de celebracion)."""
    c.saveState()
    c.setStrokeColor(INK)
    c.setFillColor(PAPER)
    c.setLineJoin(1)
    c.setLineCap(1)

    # --- patas, debajo del cuerpo -----------------------------------
    c.setLineWidth(r * 0.09)
    for sgn in (-1, 1):
        fx = cx + sgn * r * 0.26
        fy = cy - r * 0.98
        c.line(fx, fy, fx, fy - r * 0.16)
        for d in (-0.09, 0, 0.09):
            c.line(fx, fy - r * 0.16, fx + d * r, fy - r * 0.27)

    # --- alas, DETRAS del cuerpo -------------------------------------
    # forma de "gota" gordita pegada al costado -- bastante mas ancha que el
    # primer intento, o se leia como una simple raya doblando el contorno
    # del cuerpo en vez de una ala de verdad.
    c.setLineWidth(r * 0.085)
    c.setFillColor(PAPER)
    for sgn in (-1, 1):
        p = c.beginPath()
        if pose == 'saluda' and sgn == 1:
            p.moveTo(cx + sgn * r * 0.50, cy + r * 0.50)
            p.curveTo(cx + sgn * r * 0.95, cy + r * 0.95,
                     cx + sgn * r * 1.05, cy + r * 1.55,
                     cx + sgn * r * 0.72, cy + r * 1.78)
            p.curveTo(cx + sgn * r * 0.78, cy + r * 1.40,
                     cx + sgn * r * 0.55, cy + r * 0.95,
                     cx + sgn * r * 0.32, cy + r * 0.78)
            p.close()
        else:
            p.moveTo(cx + sgn * r * 0.58, cy + r * 0.45)
            p.curveTo(cx + sgn * r * 1.20, cy + r * 0.30,
                     cx + sgn * r * 1.28, cy - r * 0.45,
                     cx + sgn * r * 0.70, cy - r * 0.85)
            p.curveTo(cx + sgn * r * 0.95, cy - r * 0.20,
                     cx + sgn * r * 0.92, cy + r * 0.15,
                     cx + sgn * r * 0.58, cy + r * 0.45)
            p.close()
        c.drawPath(p, fill=1, stroke=1)

    # --- cuerpo --------------------------------------------------------
    c.setLineWidth(r * 0.10)
    c.setFillColor(PAPER)
    c.ellipse(cx - r * 0.86, cy - r * 0.98, cx + r * 0.86, cy + r * 0.86, fill=1, stroke=1)

    # --- orejas / mechones ----------------------------------------------
    for sgn in (-1, 1):
        p = c.beginPath()
        p.moveTo(cx + sgn * r * 0.34, cy + r * 0.80)
        p.curveTo(cx + sgn * r * 0.30, cy + r * 1.10,
                 cx + sgn * r * 0.40, cy + r * 1.32,
                 cx + sgn * r * 0.56, cy + r * 1.38)
        p.curveTo(cx + sgn * r * 0.44, cy + r * 1.14,
                 cx + sgn * r * 0.50, cy + r * 0.92,
                 cx + sgn * r * 0.60, cy + r * 0.78)
        p.close()
        c.drawPath(p, fill=1, stroke=1)

    # --- barriga con plumitas -------------------------------------------
    c.setLineWidth(r * 0.055)
    bx0, bx1 = cx - r * 0.46, cx + r * 0.46
    by0, by1 = cy - r * 0.86, cy + r * 0.40
    c.ellipse(bx0, by0, bx1, by1, fill=0, stroke=1)
    filas = 3
    for fi in range(filas):
        fy = by0 + (fi + 0.5) * (by1 - by0) / filas
        ancho_fila = (bx1 - bx0) * (1.0 - fi * 0.12)
        n = 4 - (fi == filas - 1)
        x0f = cx - ancho_fila / 2.0
        paso = ancho_fila / n
        for k in range(n):
            axc = x0f + (k + 0.5) * paso
            c.arc(axc - paso * 0.42, fy - paso * 0.3, axc + paso * 0.42, fy + paso * 0.55,
                 startAng=200, extent=140)

    # --- ojos, grandes y redondos (la cara de "ensenando") --------------
    er = r * 0.40
    for sgn in (-1, 1):
        exc = cx + sgn * r * 0.40
        eyc = cy + r * 0.52
        c.setLineWidth(r * 0.075)
        c.setFillColor(PAPER)
        c.circle(exc, eyc, er, fill=1, stroke=1)
        c.setFillColor(INK)
        pupx = exc + (sgn * r * 0.05 if pose != 'saluda' else sgn * r * 0.08)
        c.circle(pupx, eyc - r * 0.03, er * 0.42, fill=1, stroke=0)
        c.setFillColor(PAPER)
        c.circle(pupx + er * 0.14, eyc + er * 0.16, er * 0.12, fill=1, stroke=0)

    # --- cejas (dan la expresion simpatica/sorprendida) ------------------
    c.setLineWidth(r * 0.065)
    for sgn in (-1, 1):
        exc = cx + sgn * r * 0.40
        c.line(exc - r * 0.22, cy + r * 0.88, exc + sgn * r * 0.04, cy + r * 1.00)

    # --- pico -------------------------------------------------------------
    c.setFillColor(INK)
    p = c.beginPath()
    p.moveTo(cx, cy + r * 0.18)
    p.lineTo(cx - r * 0.13, cy + r * 0.02)
    p.lineTo(cx + r * 0.13, cy + r * 0.02)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # --- birrete de profesor, ladeado -------------------------------------
    c.saveState()
    c.translate(cx + r * 0.12, cy + r * 1.30)
    c.rotate(-9)
    c.setFillColor(INK)
    c.setLineWidth(r * 0.05)
    c.setStrokeColor(INK)
    half = r * 0.52
    p = c.beginPath()
    p.moveTo(-half, 0); p.lineTo(0, half * 0.62); p.lineTo(half, 0)
    p.lineTo(0, -half * 0.62); p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.setFillColor(PAPER)
    c.ellipse(-r * 0.14, -r * 0.30, r * 0.14, -r * 0.08, fill=1, stroke=1)
    c.setStrokeColor(INK)
    c.setLineWidth(r * 0.035)
    c.line(half * 0.55, half * 0.15, half * 0.55, -half * 0.55)
    c.setFillColor(INK)
    c.circle(half * 0.55, -half * 0.60, r * 0.045, fill=1, stroke=0)
    c.restoreState()

    c.restoreState()


def globo_texto(c, x, y, w, h, texto, cola_x=None, cola_abajo=True,
                font='DejaVuSans', font_bold='DejaVuSans-Bold', size=9.6,
                leading=12.4, titulo=None):
    """Un globo de dialogo de comic, con la cola apuntando hacia Misol.
       (x, y) es la esquina inferior izquierda del globo. Si `cola_x` se da,
       la cola sale desde ahi (hacia abajo si `cola_abajo`, si no hacia
       arriba) -- para que apunte exactamente al pico del buho."""
    c.saveState()
    c.setStrokeColor(INK)
    c.setFillColor(PAPER)
    c.setLineWidth(1.6)
    rad = min(16, h * 0.28)
    c.roundRect(x, y, w, h, rad, fill=1, stroke=1)

    if cola_x is not None:
        tw = min(w * 0.16, 20)
        cola_x = max(x + tw, min(x + w - tw, cola_x))
        c.setFillColor(PAPER)
        p = c.beginPath()
        if cola_abajo:
            p.moveTo(cola_x - tw * 0.5, y + 1)
            p.lineTo(cola_x + tw * 0.5, y + 1)
            p.lineTo(cola_x, y - tw * 0.85)
        else:
            p.moveTo(cola_x - tw * 0.5, y + h - 1)
            p.lineTo(cola_x + tw * 0.5, y + h - 1)
            p.lineTo(cola_x, y + h + tw * 0.85)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        c.setStrokeColor(INK)
        c.setLineWidth(1.6)
        if cola_abajo:
            c.line(cola_x - tw * 0.5, y + 1, cola_x, y - tw * 0.85)
            c.line(cola_x + tw * 0.5, y + 1, cola_x, y - tw * 0.85)
        else:
            c.line(cola_x - tw * 0.5, y + h - 1, cola_x, y + h + tw * 0.85)
            c.line(cola_x + tw * 0.5, y + h - 1, cola_x, y + h + tw * 0.85)
        # tapa la costura donde la cola toca el globo
        c.setStrokeColor(PAPER)
        c.setLineWidth(2.0)
        c.line(cola_x - tw * 0.46, y + (0 if cola_abajo else h), cola_x + tw * 0.46, y + (0 if cola_abajo else h))

    pad = 14
    ty = y + h - pad - size
    tx = x + pad
    tw_max = w - pad * 2
    if titulo:
        c.setFont(font_bold, size + 0.6)
        c.setFillColor(INK)
        c.drawString(tx, ty, titulo)
        ty -= leading + 2
    c.setFont(font, size)
    c.setFillColor(INK)
    for line in wrap_lines(texto, font, size, tw_max):
        c.drawString(tx, ty, line)
        ty -= leading
    c.restoreState()
