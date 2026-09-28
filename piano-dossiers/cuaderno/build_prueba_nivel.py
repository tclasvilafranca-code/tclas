# -*- coding: utf-8 -*-
"""PRUEBA DE NIVEL — para los alumnos nuevos, antes de decidir qué álbum
   les toca. Nueve alumnos, media hora de clase cada uno, sitio nuevo: hace
   falta saber de un vistazo quién lee redondas y quién ya lee corcheas
   sueltas, y hacerlo SIN inventar el ejercicio a mano cada vez.

   Reutiliza el mismo motor que ya lleva la "agudeza visual" de cada dosier
   (`engine/generador_lectura.py`): líneas que SUMAN el compás entero y que
   nunca repiten la célula anterior (anti-secuencia), construidas nota a
   nota por GRADOS DE LA ESCALA — no notas sueltas al azar, así que aunque
   no sea una melodía copiada de ningún sitio, se mueve como una y no salta
   como una lista de números. Es justo el "que suene a algo" que se pidió.

   DOS CUADERNILLOS, tres hojas cada uno — Fácil, Medio e Intermedio, en el
   mismo orden en que suben los escalones de `niveles.py`:

     NIÑOS         — pauta grande (el mismo gap "para escribir a mano" de
                     `hoja_pauta.py`), siempre en clave de sol, y las
                     instrucciones sin ningún tecnicismo (la misma norma que
                     ya usa el formato corto de Arnau: nada de "anacrusa").
     ADOLESCENTES  — pauta de tamaño normal, con las DOS claves del piano a
                     partir del nivel medio (un adolescente que empieza
                     suele tardar menos en juntar las dos manos que un
                     niño), instrucciones en lenguaje directo.

   Cada hoja es AUTOSUFICIENTE (se van a fotocopiar sueltas, una por
   alumno, no en orden) y remata con una franja para que la profesora
   marque el resultado en el momento — nada de tener que rellenar una
   plantilla aparte después.

   Uso:  python3 build_prueba_nivel.py
"""
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from notation import draw_system, BLEED_SAFE                                 # noqa: E402
from page_layout_common import before_staff, after_system                    # noqa: E402
from generador_lectura import hoja as generar_hoja                           # noqa: E402
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,   # noqa: E402
                     INK, MUTED, ACCENT, _fit, _wrap)

SALIDA = os.path.join(HERE, '..', 'output')

NUM_W = 17
SUELO = 46
PANEL = HexColor('#F3F1EA')
ALTO_RESULTADO = 96

# --------------------------------------------------------------------------
# LOS TRES NIVELES. `nivel` es el mismo parámetro del generador que ya usan
# calentamiento y agudeza visual (0 a 3); aquí se para en 2 porque el
# generador no dibuja semicorcheas —el techo real de "difícil" en
# `niveles.py`— y en una PRUEBA DE UN VISTAZO lo que separa a un alumno de
# otro es sobre todo el ritmo suelto y el silencio a contratiempo, que ya
# entran de sobra en el nivel 2.
# --------------------------------------------------------------------------
NIVELES = [
    dict(clave='facil', nombre='Fácil', nivel_gen=0,
        que='redondas, blancas y negras'),
    dict(clave='medio', nombre='Medio', nivel_gen=1,
        que='entran las corcheas y algún silencio'),
    dict(clave='intermedio', nombre='Intermedio', nivel_gen=2,
        que='ritmos más sueltos, con silencios a contratiempo'),
]

TEXTOS = {
    'ninos': dict(
        kicker='PRUEBA DE NIVEL · NIÑOS',
        instr=('Lee cada línea en voz alta diciendo el nombre de las notas. Si ya sabes '
              'dónde están en el piano, tócalas también. Da igual si te equivocas: '
              'lo que importa es ver hasta dónde llegas sin atascarte.'),
        gap=8.6,
        dos_claves_desde=None,     # nunca — el niño se queda en clave de sol
    ),
    'adolescentes': dict(
        kicker='PRUEBA DE NIVEL · ADOLESCENTES',
        instr=('Lee cada línea en voz alta y, si puedes, tócala al piano. No hace falta '
              'que salga perfecta: el objetivo es ver con qué soltura lees, no corregir '
              'cada fallo.'),
        gap=7.2,
        dos_claves_desde='medio',  # clave de sol y de fa desde el nivel medio
    ),
}


def cabecera(c, grupo, nivel_cfg, num, total):
    t = TEXTOS[grupo]
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, t['kicker'])
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, 'Hoja %d de %d' % (num, total))
    y -= 27

    c.setFont('DejaVuSerif-Bold', 26)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, nivel_cfg['nombre'])
    tw = stringWidth(nivel_cfg['nombre'], 'DejaVuSerif-Bold', 26)
    c.setFont('DejaVuSans', 10.5)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + tw + 12, y - 1, nivel_cfg['que'])
    y -= 20
    y = _wrap(c, t['instr'], MARGIN, y, 'DejaVuSans', 9.2, CONTENT_W, 12.5, MUTED)
    y -= 9

    bh = 21
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - bh, 3, bh, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.0)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 13, y - 13.5, 'EN VOZ ALTA, LÍNEA POR LÍNEA · NO TE SALTES NINGUNA')
    return y - bh - 12


def rellenar(c, y, lineas, gap, suelo):
    x = MARGIN + NUM_W
    ancho = CONTENT_W - NUM_W

    def alto(ln):
        return (before_staff(gap, ln['events'], ln['clef']) + 4 * gap
                + after_system(gap, ln['events'], ln['clef']))

    caben, usado = [], 0.0
    for ln in lineas:
        if y - usado - alto(ln) < suelo:
            break
        caben.append(ln)
        usado += alto(ln)
    if not caben:
        return y
    extra = min(16.0, max(0.0, (y - usado - suelo) / len(caben)))

    num = 1
    for ln in caben:
        ev = ln['events']
        y -= before_staff(gap, ev, ln['clef']) + extra / 2.0
        c.setFont('DejaVuSans-Bold', 8.2)
        c.setFillColor(ACCENT)
        c.drawRightString(MARGIN + NUM_W - 7, y - 2 * gap - 3, str(num))
        top, bot = draw_system(c, x, y, ancho, gap, ev, clef=ln['clef'],
                               time_sig=ln['time_sig'], show_time=True,
                               spacing='engraved')
        y = bot - after_system(gap, ev, ln['clef']) - extra / 2.0
        num += 1
    return y


def caja_resultado(c, y):
    """La franja de abajo: lo rellena la profesora ahí mismo, en la propia
       clase — nada de plantilla aparte ni de pasar los datos después."""
    h = ALTO_RESULTADO
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)

    c.setFont('DejaVuSans-Bold', 9.4)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 15, y - 17, 'RESULTADO DE LA PRUEBA')

    opciones = ['Lee fluido, sin dudar', 'Lee con dudas / se traba', 'No lee todavía']
    oy = y - 36
    for op in opciones:
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.9)
        c.rect(MARGIN + 15, oy - 8, 9, 9, fill=0, stroke=1)
        c.setFont('DejaVuSans', 8.6)
        c.setFillColor(INK)
        c.drawString(MARGIN + 30, oy - 6.5, op)
        oy -= 16

    lx = MARGIN + CONTENT_W * 0.46
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(NAVY)
    c.drawString(lx, y - 36, 'NIVEL ASIGNADO')
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(lx, y - 50, MARGIN + CONTENT_W - 10, y - 50)
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(NAVY)
    c.drawString(lx, y - 68, 'ÁLBUM RECOMENDADO')
    c.line(lx, y - 82, MARGIN + CONTENT_W - 10, y - 82)
    return y - h - 8


def pie(c, num):
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(num))
    c.showPage()


def construir_hoja(c, grupo, nivel_cfg, num, total, semilla):
    t = TEXTOS[grupo]
    y = cabecera(c, grupo, nivel_cfg, num, total)

    claves = ('treble',)
    if t['dos_claves_desde'] is not None:
        orden = [n['clave'] for n in NIVELES]
        if orden.index(nivel_cfg['clave']) >= orden.index(t['dos_claves_desde']):
            claves = ('treble', 'bass')

    lineas = generar_hoja('Do mayor', semilla=semilla, n_lineas=20,
                          nivel=nivel_cfg['nivel_gen'], compases=4,
                          claves=claves, salto_max=2 + nivel_cfg['nivel_gen'])

    y_caja = SUELO + ALTO_RESULTADO
    y = rellenar(c, y, lineas, gap=t['gap'], suelo=y_caja + 12)
    caja_resultado(c, y_caja)
    pie(c, num)


def construir(grupo):
    os.makedirs(SALIDA, exist_ok=True)
    nombre = 'Prueba_de_nivel_%s.pdf' % ('Ninos' if grupo == 'ninos' else 'Adolescentes')
    ruta = os.path.join(SALIDA, nombre)
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('Prueba de nivel · %s' % grupo)

    total = len(NIVELES)
    for i, nivel_cfg in enumerate(NIVELES):
        # semilla distinta por grupo Y por nivel, para que las dos pruebas
        # (niños/adolescentes) no repitan la misma línea nota por nota
        semilla = (4000 if grupo == 'ninos' else 5000) + i
        construir_hoja(c, grupo, nivel_cfg, i + 1, total, semilla)

    c.save()
    return ruta


def main(argv):
    for grupo in ('ninos', 'adolescentes'):
        ruta = construir(grupo)
        print('Prueba de nivel · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
