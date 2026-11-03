# -*- coding: utf-8 -*-
"""Dosier personal de apuntes — portada + 44 bloques de (1 hoja de apuntes +
   2 hojas de pauta), para tomar notas en un curso profesional de piano.

   Reutiliza la MISMA portada que los dosieres de alumno (`portada.build_cover`)
   y el MISMO motor de pentagramas profesional que ya usa el resto del
   cuaderno (`hoja_pauta`, que a su vez usa `notation.draw_staff`) — nada se
   reinventa, esto es la misma calidad de imprenta del resto del proyecto,
   aplicada a un cuaderno personal en vez de a un dosier de alumno.

   POR QUÉ 44 BLOQUES: el curso del estudio se organiza en 44 sesiones — el
   mismo número de semanas que ya usa `build_plan_curso` para un curso
   completo (septiembre a julio). No se inventa contenido por sesión: cada
   bloque trae solo la etiqueta "SESIÓN N" y líneas en blanco para fecha y
   tema — eso lo rellena quien toma la clase, no el generador.

   LA HOJA DE APUNTES no es una hoja en blanco a secas: lleva renglones finos
   (como una libreta normal) para que la letra salga recta, más una línea de
   fecha y una de tema arriba. Las DOS HOJAS DE PAUTA por bloque son
   pentagramas de verdad, sin clave ni compás (la pone quien escribe), con el
   mismo pautado grande pensado para escribir a mano que ya usa
   `hoja_pauta.py` en el resto del cuaderno — aquí con la cabecera reducida a
   una sola línea para que el pentagrama gane todo el alto que se pueda.

   Uso:  python3 build_apuntes_personal.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))

from reportlab.pdfgen import canvas                                          # noqa: E402
from notation import draw_staff, BLEED_SAFE                                  # noqa: E402
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,   # noqa: E402
                     INK, MUTED, ACCENT, build_cover)

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', 'output')

# --------------------------------------------------------------------------
# Los datos de la portada — cambia estos tres si quieres otro nombre o curso.
# --------------------------------------------------------------------------
TITULAR = 'Apuntes de piano'
SUBTITULO = 'Curso profesional de piano'
CURSO = 'Cuaderno de apuntes · 44 sesiones'

N_BLOQUES = 44
PIE = 'El Cuaderno del Pianista  ·  T-Clas'


def _cabecera_fina(c, y_top, izq, der):
    """La cabecera comun a las tres hojas de un bloque: una franja azul fina
       arriba (el mismo gesto de marca de `hoja_pauta.py`) y UNA sola linea
       de texto — para que en las hojas de pauta el pentagrama se coma todo
       el alto que se pueda, que es justo lo que se pidio."""
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)
    y = y_top
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, y, izq.upper())
    c.setFont('DejaVuSans', 8.6)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, der)
    y -= 10
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(MARGIN, y, W - MARGIN, y)
    return y


def _pie(c, page_num):
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, PIE)
    c.drawRightString(W - MARGIN, 26, str(page_num))


# --------------------------------------------------------------------------
# La hoja de apuntes: renglones finos, con una linea de fecha y una de tema.
# --------------------------------------------------------------------------
RENGLON = 22.4       # separacion entre renglones — la de una libreta normal
SUELO = 46


def _hoja_apuntes(c, num_bloque, page_num):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    y = _cabecera_fina(c, H - 40, 'Sesión %d' % num_bloque, 'Apuntes')
    y -= 26

    # las dos lineas de cabecera del propio bloque: fecha y tema, para que
    # cada sesion quede identificada sin que el generador se invente nada
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'FECHA')
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(MARGIN + 42, y - 2, MARGIN + 150, y - 2)
    c.drawString(MARGIN + 168, y, 'TEMA')
    c.line(MARGIN + 206, y - 2, W - MARGIN, y - 2)
    y -= 30

    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    n = int((y - SUELO) // RENGLON)
    extra = (y - SUELO - n * RENGLON) / n if n else 0
    paso = RENGLON + extra
    for _i in range(n):
        y -= paso
        c.line(MARGIN, y, W - MARGIN, y)

    _pie(c, page_num)
    c.showPage()


# --------------------------------------------------------------------------
# Las dos hojas de pauta: el mismo pentagrama grande de `hoja_pauta.py`,
# calculado para llenar exactamente el hueco que deja la cabecera fina.
# --------------------------------------------------------------------------
GAP = 8.6            # mismo pentagrama "grande" de hoja_pauta.py — pensado
                      # para escribir a mano, no para imprimir una partitura
AIRE = 3.15           # el mismo margen entre pentagramas: sin el, una nota
                      # que se sale de un pentagrama invade el de al lado


def _hoja_pauta(c, num_bloque, mitad, page_num):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    y = _cabecera_fina(c, H - 40, 'Sesión %d' % num_bloque, 'Pauta %d/2' % mitad)
    y -= 20

    paso = GAP * (4 + AIRE)
    n = int((y - SUELO) // paso)
    extra = (y - SUELO - n * paso) / n if n else 0
    for _i in range(n):
        draw_staff(c, MARGIN, y, CONTENT_W, gap=GAP)
        y -= paso + extra

    _pie(c, page_num)
    c.showPage()


# --------------------------------------------------------------------------
def construir():
    os.makedirs(OUT_DIR, exist_ok=True)
    ruta = os.path.join(OUT_DIR, 'Apuntes_personales_piano.pdf')
    c = canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle(TITULAR)

    build_cover(c, os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), TITULAR, SUBTITULO, CURSO)

    page_num = 2
    for bloque in range(1, N_BLOQUES + 1):
        _hoja_apuntes(c, bloque, page_num)
        page_num += 1
        _hoja_pauta(c, bloque, 1, page_num)
        page_num += 1
        _hoja_pauta(c, bloque, 2, page_num)
        page_num += 1

    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('Apuntes personales · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
