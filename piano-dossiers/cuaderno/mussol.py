# -*- coding: utf-8 -*-
"""En Mussol Misol, dibujat en vectorial a partir del búho oficial del curso (el morado con
   birrete, vientre turquesa y pico naranja), en dos versiones:

     mussol(c, cx, cy, s, color=False)  -> en contorn, per pintar
     mussol(c, cx, cy, s, color=True)   -> a tot color, amb la paleta del personatge

   (cx, cy) és el centre de la panxa; amb s = 1 fa uns 200 pt d'alt. Necessita un
   `ManoCanvas` de `dibujo_mano` (si no, també funciona, però amb el traç recte).
"""
import math

from reportlab.lib.colors import HexColor, black, white

PAL = dict(cos='#9A97DC', ala='#6E69C4', panxa='#86DDD3', bec='#F6A33B', peu='#F6A33B',
           birret='#2B2A33', borla='#F4C430', ull='#FFFFFF', pupil='#25232E', tra='#2F2B5C')


def _c(color, clau):
    return HexColor(PAL[clau]) if color else white


def mussol(c, cx, cy, s=1.0, color=False, saluda=False, lw=3.0, bruixa=False):
    tra = HexColor(PAL['tra']) if color else black
    amp0 = getattr(c, 'amp', None)
    if amp0 is not None:
        c.amp = 0.45

    def T(x, y):
        return cx + x * s, cy + y * s

    def estil(clau, w=lw):
        c.setStrokeColor(tra)
        c.setLineWidth(w * max(s, 0.6) ** 0.5)
        c.setLineJoin(1)
        c.setLineCap(1)
        c.setFillColor(_c(color, clau))

    def poli(punts, clau, tancat=True, w=lw):
        estil(clau, w)
        c.poly([T(*p) for p in punts], 1, 1 if tancat else 0, closed=tancat) if hasattr(c, 'poly') else None

    def el(x, y, rx, ry, clau, gir=0, w=lw):
        estil(clau, w)
        c.saveState()
        c.translate(*T(x, y))
        c.rotate(gir)
        c.ellipse(-rx * s, -ry * s, rx * s, ry * s, stroke=1, fill=1)
        c.restoreState()

    # --- peus
    for sg in (-1, 1):
        el(sg * 26, -98, 18, 8, 'peu')
        estil('peu', 2.0)
        for dx in (-6, 6):
            c.line(*T(sg * 26 + dx, -104), *T(sg * 26 + dx * 0.8, -90))
    # --- orelles (plomes del cap)
    for sg in (-1, 1):
        poli([(sg * 74, 62), (sg * 62, 112), (sg * 28, 84)], 'cos')
    # --- ales (darrere el cos)
    if not saluda:
        el(-80, -2, 20, 52, 'ala', gir=12)
    # --- cos
    el(0, -2, 80, 96, 'cos')
    # --- panxa i plomes
    el(0, -34, 52, 54, 'panxa')
    estil('panxa', 1.8)
    c.setFillColor(_c(color, 'panxa'))
    for fila, (y, xs) in enumerate(((-12, (-26, 0, 26)), (-34, (-38, -13, 13, 38)), (-56, (-24, 0, 24)))):
        for x in xs:
            c.arc(*T(x - 12, y - 11), *T(x + 12, y + 9), 200, 140)
    # --- ales (davant)
    if saluda:
        el(-80, -2, 20, 52, 'ala', gir=12)
        el(92, 34, 20, 52, 'ala', gir=-48)
    else:
        el(80, -2, 20, 52, 'ala', gir=-12)
    # --- ulls
    for sg in (-1, 1):
        el(sg * 31, 34, 27, 28, 'ull')
        estil('pupil', 1.5)
        c.setFillColor(HexColor(PAL['pupil']) if color else black)
        c.circle(*T(sg * 29, 30), 12 * s, stroke=1, fill=1)
        c.setFillColor(white)
        c.circle(*T(sg * 29 + 4, 36), 4 * s, stroke=0, fill=1)
        c.circle(*T(sg * 29 - 4, 25), 2 * s, stroke=0, fill=1)
    # --- bec
    poli([(-11, 12), (11, 12), (0, -9)], 'bec')
    if bruixa:
        # --- barret de bruixa (Halloween) en lloc del birret
        poli([(-52, 86), (-34, 146), (-4, 178), (26, 204), (22, 166), (38, 128), (52, 88)],
             'birret' if color else 'cos')
        el(0, 86, 84, 15, 'birret' if color else 'cos')
        estil('borla', 2.0)
        poli([(-48, 96), (50, 96), (46, 112), (-46, 112)], 'borla', w=2.0)
        if amp0 is not None:
            c.amp = amp0
        return
    # --- birret: copa, tapa, botó i borla
    poli([(-50, 80), (50, 80), (44, 60), (-44, 60)], 'birret' if color else 'cos')
    poli([(-84, 88), (-3, 116), (86, 94), (3, 68)], 'birret' if color else 'cos')
    estil('birret' if color else 'cos', 1.6)
    if color:
        c.setFillColor(HexColor('#4A4955'))
    c.circle(*T(-2, 93), 6 * s, stroke=1, fill=1)
    estil('borla', 2.0)
    c.line(*T(86, 94), *T(86, 62))
    poli([(80, 62), (92, 62), (94, 40), (78, 40)], 'borla', w=2.2)
    estil('borla', 1.4)
    for dx in (-5, 0, 5):
        c.line(*T(86 + dx, 56), *T(86 + dx * 1.1, 42))

    if amp0 is not None:
        c.amp = amp0
