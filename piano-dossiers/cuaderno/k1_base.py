# -*- coding: utf-8 -*-
"""MI CUADERNO DE PIANO · NIVEL 1 · KIDS (castellano) — marco de componentes.

   Diseño TCLAS niños (Mussol Misol, paneles con pestaña, cajas con icono, letra Andika) adaptado a un alumno con
   TEA + TDAH. Principios (se aplican en TODAS las páginas, siempre igual para que sea predecible):

     · cada página tiene la MISMA estructura: título → Mussol (UNA frase) → un panel con pasos numerados → «HECHO»
     · UNA actividad por página (máximo dos tareas pequeñas), mucho espacio en blanco, sin decoración que distraiga
     · instrucciones cortas, literales y en orden (nada de metáforas ni bromas con doble sentido)
     · casilla «HECHO ✓» al final de cada actividad: ver el progreso motiva y permite parar sin perder el hilo
     · después de 2 actividades, una PAUSA ACTIVA fija (mover el cuerpo) y al final del mes el TABLERO de logros
     · color solo en las notas (cada nota, siempre el mismo color); el resto, en blanco y negro para colorear

   Todos los componentes son bloques de `n1_base` (Blk): se apilan con `Doc.add(...)` y se reparten en páginas."""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
import n1_base as B
from n1_base import Doc, Blk, W, H, SOLUCIONES, sol, rnd, nombre, mover, posicion, GAP, BEATS
import nens_tclas as K
from nens_tclas import (SANS, SANSB, SERIFB, ETQ, NAVY, NAVY_SOFT, CREMA, WARM, OCRE, MUTED, RULE, SOMBRA, INK, COL, rr, trac, txt)
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
import notation as nt
from notation import note_y, draw_staff, draw_clef, ledger_lines_needed
from nens_tclas import alt_par, par as kpar
from dibujo_mano import ManoCanvas, lineas_texto
from mussol import mussol
import nens_dib

# --- geometria infantil: margen 40, pie a 40
M = 40.0
CW = W - 2 * M
B.MARGIN = M
B.CONTENT_W = CW
B.TOP = H - 60.0
B.BOTTOM = 56.0

NOMBRES = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
COLNOM = dict(DO='rojo', RE='naranja', MI='amarillo', FA='verde', SOL='azul', LA='lila', SI='gris')
LETRA2NOM = dict(C='DO', D='RE', E='MI', F='FA', G='SOL', A='LA', B='SI')
KICKER = 'MI CUADERNO DE PIANO  ·  NIVEL 1 KIDS'
MES_ACTUAL = ['']          # lo cambia cada mes (cabecera derecha)


def nom_nota(p):
    return LETRA2NOM[p[0]]


def col_nota(p):
    return HexColor(COL[nom_nota(p)])


# ------------------------------------------------------------------ marco de pagina
def k_marco(c, kicker, derecha, n):
    c.setFillColor(CREMA)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.rect(0, H - 9, W, 9, stroke=0, fill=1)
    txt(c, M, H - 32, KICKER, 9.2, ETQ, OCRE)
    txt(c, W - M, H - 32, derecha, 9.2, ETQ, MUTED, 'r')
    trac(c, 0.8, RULE)
    c.line(M, 40, W - M, 40)
    txt(c, W / 2, 22, 'El Cuaderno del Pianista  ·  T-Clas', 9, SANS, MUTED, 'c')
    txt(c, W - M, 22, str(n), 10, SANSB, NAVY, 'r')
    txt(c, M, 22, 'KIDS', 9.5, ETQ, OCRE)


B.marco = k_marco
B._fuente = lambda bold, size=None: 'Andika-Bold' if bold else 'Andika'


# ------------------------------------------------------------------ texto
def _alto(txt_, size, ancho, lead=None, bold=False):
    return alt_par(txt_, size, ancho, lead or size * 1.38, SANSB if bold else SANS)


def K_par(texto, size=13, col=INK, despues=8, bold=False):
    h = _alto(texto, size, CW, None, bold) + despues

    def f(c, x, y, w):
        kpar(c, x, y - size, texto, size, w, size * 1.38, SANSB if bold else SANS, col)
    return Blk(h, f)


def K_espacio(h):
    return Blk(h, lambda c, x, y, w: None)


def K_titulo(mes, titulo, frase):
    """Cabecera de mes / tema: pildora ocre con el mes, titulo serif, una frase."""
    h = 34 + 46 + _alto(frase, 13.5, CW) + 14

    def f(c, x, y, w):
        pw = stringWidth(mes.upper(), ETQ, 10) + 22
        rr(c, x, y - 22, pw, 20, 10, fill=OCRE, lw=0)
        txt(c, x + pw / 2, y - 16, mes.upper(), 10, ETQ, white, 'c')
        ts_ = 32
        while stringWidth(titulo, SERIFB, ts_) > w and ts_ > 20:
            ts_ -= 1
        txt(c, x, y - 62, titulo, ts_, SERIFB, NAVY)
        trac(c, 3, OCRE)
        c.line(x, y - 72, x + 46, y - 72)
        kpar(c, x, y - 92, frase, 13.5, w, 13.5 * 1.38, SANS, NAVY_SOFT)
    return Blk(h, f)


def K_titulo_act(num, titulo, mes=''):
    """Titulo de una actividad: numero grande + titulo (siempre en el mismo sitio)."""
    def f(c, x, y, w):
        c.setFillColor(OCRE)
        c.circle(x + 20, y - 24, 20, stroke=0, fill=1)
        txt(c, x + 20, y - 31, str(num), 22, SANSB if str(num) != '★' else 'DejaVuSans-Bold', white, 'c')
        ts_ = 26
        while stringWidth(titulo, SERIFB, ts_) > w - 56 and ts_ > 16:
            ts_ -= 1
        txt(c, x + 52, y - 32, titulo, ts_, SERIFB, NAVY)
        trac(c, 3, OCRE)
        c.line(x + 52, y - 42, x + 98, y - 42)
    return Blk(58, f, keep_next=True)


# ------------------------------------------------------------------ Mussol Misol
def _guia(c, x, ytop, ample, text, color=False, size=13, h=None):
    """Mussol Misol como guia (misma figura y globo que los Pekes, con el rotulo en castellano)."""
    y = ytop - h
    mussol(c, x + 40, y + h / 2 - 2, 0.42, color=color, lw=2.8)
    bx = x + 86
    rr(c, bx + 3.4, y - 3.4, ample - 86, h, 11, fill=SOMBRA, lw=0)
    rr(c, bx, y, ample - 86, h, 11, fill=white, lw=1.7, col=NAVY)
    c.setFillColor(white)
    trac(c, 1.7, NAVY)
    c.poly([(bx + 1, y + h / 2 + 10), (bx - 13, y + h / 2), (bx + 1, y + h / 2 - 10)], 1, 1)
    c.setStrokeColor(white)
    c.setLineWidth(3)
    c.line(bx + 1, y + h / 2 + 8, bx + 1, y + h / 2 - 8)
    txt(c, bx + 16, y + h - 20, 'MUSSOL MISOL DICE', 9.2, ETQ, OCRE)
    kpar(c, bx + 16, y + h - 40, text, size, ample - 86 - 32, size * 1.38, SANS, INK)
    c.setDash()


def K_mussol(texto, color=False, size=13):
    h = max(80, alt_par(texto, size, CW - 126, size * 1.38) + 40)

    def f(c, x, y, w):
        _guia(c, x, y, w, texto, color, size, h)
    return Blk(h + 12, f, keep_next=True)


# ------------------------------------------------------------------ panel con pestana
def K_panel(num, titulo, interior, pad=16, fondo=white):
    """Panel con borde grueso y pestana (numero + titulo). `interior` = lista de Blk apilados."""
    interior = list(interior)
    h_in = sum(b.h for b in interior)
    h = 34 + h_in + 12

    def f(c, x, y, w):
        yt = y - 16
        K.panell(c, x, yt, w, h, titulo, num, fons=fondo)
        yy = yt - 30
        for b in interior:
            b.f(c, x + pad, yy, w - 2 * pad)
            yy -= b.h
    return Blk(h + 22, f)


def K_pasos(lista, size=13, iconos=None):
    """Pasos numerados (circulo ocre + frase corta). `iconos`: lista opcional de glifos DejaVu por paso."""
    ancho = CW - 32 - 40 - 34
    alts = [max(30, _alto(t, size, ancho) + 8) for t in lista]

    def f(c, x, y, w):
        yy = y
        for k, (t, hh) in enumerate(zip(lista, alts)):
            K.quadrat(c, x, yy - 26, k + 1, 24)
            kpar(c, x + 36, yy - 18, t, size, w - 40, size * 1.38, SANS, INK)
            yy -= hh
    return Blk(sum(alts) + 6, f)


def K_caja(etiqueta, texto, icono=None, size=12.5):
    ancho = CW - 28
    h = 52 + _alto(texto, size, ancho) + 14

    def f(c, x, y, w):
        K.caixa_t(c, x, y, w, h, etiqueta, texto, size, icona=icono)
    return Blk(h + 10, f)


K_ICO = {'RECUERDA': '★', '¿SABÍAS QUE…?': '?', 'ESCUCHA': '♪', 'PRUEBA': '▶', 'TRUCO': '★'}


def K_cajita(etiqueta, texto, size=12.5):
    return K_caja(etiqueta, texto, K_ICO.get(etiqueta, '★'), size)


def K_hecho(texto='¡HECHO!'):  # va DENTRO del panel (asi nunca queda sola en otra pagina)
    """Casilla de final de actividad: SIEMPRE abajo a la derecha."""
    def f(c, x, y, w):
        bw = 170
        rr(c, x + w - bw, y - 40, bw, 36, 18, fill=WARM, lw=1.7, col=OCRE)
        txt(c, x + w - bw + 18, y - 28, texto, 13, ETQ, OCRE)
        trac(c, 1.8, OCRE)
        c.setFillColor(white)
        c.circle(x + w - 30, y - 22, 13, stroke=1, fill=1)
        c.setDash()
    return Blk(52, f)


# ------------------------------------------------------------------ pausas activas (siempre las mismas, en este orden)
PAUSAS = [
    ('Estira los dedos', ['Abre las manos con los dedos muy separados.', 'Cuenta hasta 5.', 'Ciérralas despacio. Repite 3 veces.']),
    ('Aplaude el pulso', ['Aplaude 4 veces despacio.', 'Aplaude 4 veces más rápido.', 'Aplaude 4 veces despacio otra vez.']),
    ('Respira', ['Pon las manos sobre la barriga.', 'Respira por la nariz contando 4.', 'Suelta el aire por la boca. Repite 3 veces.']),
    ('Camina al ritmo', ['Levántate de la silla.', 'Camina marcando 8 pasos al ritmo del metrónomo.', 'Vuelve a sentarte.']),
    ('Sacude las manos', ['Deja los brazos sueltos.', 'Sacude las manos 10 segundos.', 'Pon las manos quietas sobre las piernas.']),
    ('Presiona la pared', ['Pon las palmas en una pared.', 'Empuja suave contando 5.', 'Suelta y sacude las manos.']),
]


def K_pausa(k=0):
    """Pausa activa: mismo formato y mismo lugar siempre. Tres pasos cortos + casilla."""
    tit, pasos = PAUSAS[k % len(PAUSAS)]
    ancho = CW - 28 - 40
    h = 58 + sum(max(22, _alto(t, 12.5, ancho) + 6) for t in pasos) + 12

    def f(c, x, y, w):
        rr(c, x + 3, y - h - 3, w, h, 7, fill=HexColor('#DCCFB0'), lw=0)
        rr(c, x, y - h, w, h, 7, fill=HexColor('#EDF3E6'), lw=1.7, col=HexColor('#4F7A5A'))
        c.setFillColor(HexColor('#4F7A5A'))
        c.circle(x + 26, y - 26, 15, stroke=0, fill=1)
        txt(c, x + 26, y - 31.3, '↻', 16, 'DejaVuSans-Bold', white, 'c')
        txt(c, x + 50, y - 22, 'PAUSA ACTIVA', 10.5, ETQ, HexColor('#4F7A5A'))
        txt(c, x + 50, y - 40, tit, 14, SANSB, INK)
        yy = y - 62
        for i, t in enumerate(pasos):
            K.quadrat(c, x + 16, yy - 20, i + 1, 22)
            kpar(c, x + 48, yy - 14, t, 12.5, w - 70, 12.5 * 1.38, SANS, INK)
            yy -= max(22, _alto(t, 12.5, ancho) + 6)
        rr(c, x + w - 54, y - h + 12, 38, 30, 15, fill=white, lw=1.4, col=OCRE)
    return Blk(h + 12, f)


# ------------------------------------------------------------------ notas de colores sobre pentagrama
def _cabeza(c, cx, cy, gap, color=None, hueca=False, plica=None):
    trac(c, 1.3, NAVY)
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-18)
    c.setFillColor(color if color is not None else NAVY)
    if hueca:
        c.setFillColor(white)
    c.ellipse(-gap * 0.72, -gap * 0.52, gap * 0.72, gap * 0.52, stroke=1, fill=1)
    if hueca:
        trac(c, max(1.4, gap * 0.15), NAVY)
        c.ellipse(-gap * 0.72, -gap * 0.52, gap * 0.72, gap * 0.52, stroke=1, fill=0)
    c.restoreState()
    if plica:
        trac(c, 1.4, NAVY)
        if plica == 'up':
            c.line(cx + gap * 0.66, cy + gap * 0.1, cx + gap * 0.66, cy + gap * 3.2)
        else:
            c.line(cx - gap * 0.66, cy - gap * 0.1, cx - gap * 0.66, cy - gap * 3.2)


def K_notas(clef, notas, rotulos='nombre', color=True, gap=12.0, titulo=None, hueca=False, fantasma=False, plica=False,
            ancho_nota=None, texto_bajo=None, nombres=None):
    """Fila de notas grandes sobre pentagrama.
       notas: pitches ('C4'…) o None (hueco que el niño completa).
       rotulos: 'nombre' (escrito, en el color de la nota) | 'caja' (casilla para escribir el nombre) | None.
       fantasma: la nota se dibuja punteada (para repasar con lapiz). color: cabeza del color de la nota."""
    n = len(notas)
    sup = max([note_y(0.0, gap, p, clef) - 4 * gap for p in notas if p] + [0])
    inf = max([-note_y(0.0, gap, p, clef) for p in notas if p] + [0])
    pad_up = max(gap * 1.8, sup + gap * 1.4) + (plica and gap * 2.6 or 0) * 0
    pad_dn = max(gap * 2.6, inf + gap * 1.6) + (30 if rotulos else 6)
    tit = 18 if titulo else 0
    h = tit + pad_up + 4 * gap + pad_dn

    def f(c, x, y, w):
        if titulo:
            txt(c, x, y - 12, titulo, 11, ETQ, OCRE)
        top = y - tit - pad_up
        yb = K.pauta(c, x, top, w, gap, clef)
        cur = x + 4 + gap * (5.4 if clef == 'treble' else 4.6)
        slot = (x + w - 10 - cur) / float(n)
        for k, p in enumerate(notas):
            cx = cur + slot * (k + 0.5)
            if p:
                cy = note_y(yb, gap, p, clef)
                for ly in ledger_lines_needed(yb, top, cy, gap):
                    trac(c, 1.0, NAVY_SOFT)
                    c.line(cx - gap * 1.0, ly, cx + gap * 1.0, ly)
                if fantasma:
                    trac(c, 1.2, NAVY_SOFT, (2.2, 2.2))
                    c.setFillColor(white)
                    c.saveState()
                    c.translate(cx, cy)
                    c.rotate(-18)
                    c.ellipse(-gap * 0.72, -gap * 0.52, gap * 0.72, gap * 0.52, stroke=1, fill=0)
                    c.restoreState()
                    c.setDash()
                else:
                    sd = None
                    if plica:
                        sd = 'down' if cy > yb + 2 * gap else 'up'
                    _cabeza(c, cx, cy, gap, col_nota(p) if color else None, hueca=hueca, plica=sd)
            if nombres and nombres[k]:
                nm = nombres[k]
                c.setFillColor(HexColor(COL[nm]) if color else white)
                trac(c, 1.2, NAVY)
                c.circle(cx, yb - max(gap * 2.8, inf + gap * 1.6) - 2, 10.5, stroke=1, fill=1)
                txt(c, cx, yb - max(gap * 2.8, inf + gap * 1.6) - 6.2, nm, 8.4 if len(nm) > 2 else 9.4, SANSB, INK, 'c')
            elif rotulos == 'nombre' and p:
                nm = nom_nota(p)
                yl = yb - max(gap * 2.8, inf + gap * 1.6) - 2
                c.setFillColor(HexColor(COL[nm]) if color else white)
                trac(c, 1.2, NAVY)
                c.circle(cx, yl, 10.5, stroke=1, fill=1)
                txt(c, cx, yl - 4.2, nm, 8.4 if len(nm) > 2 else 9.4, SANSB, INK, 'c')
            elif rotulos == 'caja':
                K.caseta(c, cx - 22, yb - max(gap * 2.8, inf + gap * 1.6) - 8, 44, 24)
    return Blk(h, f)


def K_pauta_vacia(clef='treble', n=1, gap=10.0, titulo=None, ts=None):
    """Pentagramas vacios (n filas) para dibujar. Con la clave dibujada."""
    tit = 18 if titulo else 0
    fila = 4 * gap + gap * 3.4
    h = tit + n * fila + 6

    def f(c, x, y, w):
        if titulo:
            txt(c, x, y - 12, titulo, 11, ETQ, OCRE)
        for i in range(n):
            top = y - tit - gap * 1.7 - i * fila
            yb = K.pauta(c, x, top, w, gap, clef)
            if ts:
                nt.draw_time_sig(c, x + 4 + gap * 5.4 + gap * 1.2, yb, gap, top=str(ts[0]), bottom=str(ts[1]))
    return Blk(h, f)


def K_clave_fantasma(clef='treble', gap=10.0, n=5, titulo=None):
    """Pentagrama con claves punteadas para repasar con el lapiz y un hueco para hacer la propia."""
    tit = 18 if titulo else 0
    h = tit + 4 * gap + gap * 3.6 + 8

    def f(c, x, y, w):
        if titulo:
            txt(c, x, y - 12, titulo, 11, ETQ, OCRE)
        top = y - tit - gap * 1.8
        yb = K.pauta(c, x, top, w, gap, None)
        c.saveState()
        c.setFillAlpha(0.22)
        for k in range(n):
            nt.draw_clef(c, x + 8 + k * 56, yb, gap, clef)
        c.restoreState()
    return Blk(h, f)


# ------------------------------------------------------------------ teclado
def K_teclado(nb=8, inici=0, resalta=None, noms=None, color=False, h=84, dits=None, titulo=None, ancho=None, casillas=False):
    tit = 18 if titulo else 0
    hh = tit + h + 14 + (36 if casillas else 0)

    def f(c, x, y, w):
        if titulo:
            txt(c, x, y - 12, titulo, 11, ETQ, OCRE)
        ww = ancho or w
        x0 = x + (w - ww) / 2.0
        yb = y - tit - h - 6
        K.teclat(c, x0, yb, ww, h, nb=nb, resalta=resalta, noms=noms, color=color, dits=dits, inici=inici)
        if casillas:
            kw = ww / float(nb)
            for i in range(nb):
                K.caseta(c, x0 + i * kw + kw * 0.1, yb - 32, kw * 0.8, 26, 6)
    return Blk(hh, f)


# ------------------------------------------------------------------ unir con lineas (dos columnas grandes)
def K_une(izq, der, alto=46, ancho_izq=170, ancho_der=190):
    """izq/der: lista de str o callable(c, cx, cy, w, h). Dos columnas con puntos para unir con una linea."""
    n = len(izq)
    h = n * alto + 8

    def f(c, x, y, w):
        xl = x + 6
        xr = x + w - ancho_der - 6
        for k in range(n):
            cy = y - k * alto - alto / 2.0
            for col, items, xx, ww in ((0, izq, xl, ancho_izq), (1, der, xr, ancho_der)):
                it = items[k]
                if callable(it):
                    it(c, xx + ww / 2.0, cy, ww, alto)
                else:
                    rr(c, xx, cy - 18, ww, 36, 18, fill=white, lw=1.5, col=NAVY)
                    txt(c, xx + ww / 2.0, cy - 5, it, 13, SANSB, INK, 'c')
            c.setFillColor(OCRE)
            c.circle(xl + ancho_izq + 12, cy, 5, stroke=0, fill=1)
            c.circle(xr - 12, cy, 5, stroke=0, fill=1)
    return Blk(h, f)


# ------------------------------------------------------------------ casillas de respuesta grandes
def K_vf(afirmaciones, size=13):
    """Verdadero / Falso: cada frase con dos casillas grandes (V, F)."""
    ancho = CW - 32 - 120
    alts = [max(40, _alto(t, size, ancho) + 14) for t in afirmaciones]

    def f(c, x, y, w):
        yy = y
        for t, hh in zip(afirmaciones, alts):
            kpar(c, x, yy - 18, t, size, w - 120, size * 1.38, SANS, INK)
            for j, lab in enumerate(('V', 'F')):
                cx = x + w - 90 + j * 52
                c.setFillColor(white)
                trac(c, 1.8, NAVY)
                c.circle(cx, yy - hh / 2 + 4, 16, stroke=1, fill=1)
                txt(c, cx, yy - hh / 2 - 1, lab, 15, SANSB, NAVY, 'c')
            yy -= hh
    return Blk(sum(alts) + 6, f)


def K_opciones(pregunta, opciones, size=13):
    """Pregunta con opciones A/B/C en casillas grandes."""
    h = _alto(pregunta, size, CW - 32, None, True) + 8 + len(opciones) * 36 + 10

    def f(c, x, y, w):
        yy = kpar(c, x, y - size, pregunta, size, w, size * 1.38, SANSB, INK)
        yy -= 6
        for k, o in enumerate(opciones):
            c.setFillColor(white)
            trac(c, 1.6, NAVY)
            c.circle(x + 14, yy - 8, 12, stroke=1, fill=1)
            txt(c, x + 14, yy - 12.5, 'ABC'[k], 12, SANSB, NAVY, 'c')
            if callable(o):
                o(c, x + 60, yy - 8, 60, 30)
            else:
                txt(c, x + 38, yy - 12.5, o, 13, SANS, INK)
            yy -= 36
    return Blk(h, f)


def K_lineas(n=2, etiqueta=None, sep=30):
    h = n * sep + (20 if etiqueta else 0) + 6

    def f(c, x, y, w):
        yy = y
        if etiqueta:
            txt(c, x, yy - 13, etiqueta, 11, ETQ, OCRE)
            yy -= 20
        trac(c, 1.0, RULE)
        for k in range(n):
            c.line(x, yy - (k + 1) * sep + 8, x + w, yy - (k + 1) * sep + 8)
    return Blk(h, f)


def K_caja_dibujo(texto='Dibuja aquí', alto=140):
    def f(c, x, y, w):
        K.caseta(c, x, y - alto, w, alto, 8)
        txt(c, x + w / 2, y - alto + 10, texto, 10.5, SANS, MUTED, 'c')
    return Blk(alto + 8, f)


# ------------------------------------------------------------------ plantilla de actividad
def actividad(d, num, titulo, mussol_txt, pasos, interior, mes=None, fin=True):
    """UNA actividad por pagina, siempre con el mismo orden: titulo → Mussol (una frase) → panel con pasos → HECHO."""
    d.nuevo(mes if mes is not None else None)
    inner = [K_pasos(pasos), K_espacio(4)] + list(interior) + ([K_hecho()] if fin else [])
    d.add(K_titulo_act(num, titulo), K_mussol(mussol_txt), K_panel('', 'HAZLO ASÍ', inner))
