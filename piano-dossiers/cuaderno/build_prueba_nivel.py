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

   DOS EJES, cruzados en cada uno de los tres niveles (Fácil / Medio /
   Intermedio):

   1. DOS TIPOS DE HOJA POR NIVEL.
        AGUDEZA VISUAL — notas SUELTAS, todas del mismo valor (sin ritmo que
        leer): solo hay que decir el nombre de cada nota, rápido. Se dibujan
        con `notation.draw_headless_note` —cabeza sin plica, pensada
        exactamente para esto— para que no se lea como "aquí hay una negra"
        sino solo como "esto es un Mi".
        LECTURA RÍTMICA — lo que ya había: la línea completa, con las
        figuras y silencios del nivel, para ver si además de la nota lee
        también el ritmo.

   2. NIÑOS (5-9 años) FRENTE A ADOLESCENTES (10-16). La diferencia NO es
      solo el tamaño de la letra (aunque también: pauta grande para niños,
      el mismo gap "para escribir a mano" de `hoja_pauta.py`). Es el
      contenido:
        - REGISTRO: un niño de Fácil se queda en la posición de cinco dedos
          de toda la vida (Do a Sol, ni una nota más); un adolescente
          arranca ya con la octava entera. El registro de cada tramo NO
          sale del generador (que está pensado para progresar semana a
          semana en un único alumno, no para separar edades de golpe): se
          le inyecta aparte, sustituyendo `generador_lectura.REGISTRO`
          justo antes de generar esa hoja y devolviéndolo a su sitio
          después — mismo truco de "cambiar y devolver" que ya se usa en
          `juego_contrasena_puerta.py` para quitar el pentagrama o la barra
          de compás.
        - RITMO: los niños no pasan de corcheas sueltas ni en su tramo más
          alto; los adolescentes llegan en Intermedio a silencios a
          contratiempo y saltos más grandes.
        - CLAVE DE FA: un niño se queda en clave de sol las tres hojas (a
          esa edad, cuando llega la izquierda es otro proceso aparte); un
          adolescente ya lee las dos claves desde Medio.

   Cada hoja es AUTOSUFICIENTE (se van a fotocopiar sueltas, una por
   alumno, no en orden) y remata con una franja para que la profesora
   marque el resultado en el momento — nada de tener que rellenar una
   plantilla aparte después.

   Uso:  python3 build_prueba_nivel.py
"""
import os
import random
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import generador_lectura as genlec                                           # noqa: E402
from notation import (draw_system, draw_staff, draw_clef, draw_headless_note, # noqa: E402
                      BLEED_SAFE)
from page_layout_common import before_staff, after_system                    # noqa: E402
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,   # noqa: E402
                     INK, MUTED, ACCENT, _wrap)

SALIDA = os.path.join(HERE, '..', 'output')

NUM_W = 17
SUELO = 46
PANEL = HexColor('#F3F1EA')
ALTO_RESULTADO = 88


# --------------------------------------------------------------------------
# EL REGISTRO SE INYECTA, NO SE ADIVINA. `generador_lectura.escala_grados`
# lee dos diccionarios de módulo (REGISTRO, REGISTRO_ANCHO) que están
# calibrados para el progreso semanal DE UN alumno a lo largo de un curso —
# aquí hace falta lo contrario, separar de golpe un niño de 6 años de un
# adolescente de 15, así que cada tramo trae su propio registro y se
# sustituye justo antes de generar esa hoja.
# --------------------------------------------------------------------------
class _registro_propio(object):
    def __init__(self, treble, bass=None):
        self.treble = treble
        self.bass = bass or treble

    def __enter__(self):
        self._orig = dict(genlec.REGISTRO)
        genlec.REGISTRO = {
            'treble': (self.treble, self.treble),
            'bass': (self.bass, self.bass),
        }
        return self

    def __exit__(self, *_e):
        genlec.REGISTRO = self._orig
        return False


# --------------------------------------------------------------------------
# LOS TRES NIVELES, por grupo de edad. `nivel_ritmo` es el parámetro de
# siempre del generador (0 a 3, hasta dónde llega la selección de patrones
# rítmicos — se para en 2 porque el generador no dibuja semicorcheas).
# `registro_treble`/`registro_bass` son SOLO de este archivo: el tramo de
# teclado, en notas de verdad, que se le inyecta al generador para esa hoja.
# --------------------------------------------------------------------------
NIVELES_NINOS = [
    dict(clave='facil', nombre='Fácil', nivel_ritmo=0,
        registro_treble=('C4', 'G4'), registro_bass=None,
        salto_max=1, compases=2, claves=('treble',),
        que_ritmo='solo Do-Re-Mi-Fa-Sol · redondas, blancas y negras',
        que_notas='las cinco notas de la mano · Do-Re-Mi-Fa-Sol'),
    dict(clave='medio', nombre='Medio', nivel_ritmo=1,
        registro_treble=('C4', 'C5'), registro_bass=None,
        salto_max=2, compases=3, claves=('treble',),
        que_ritmo='la octava entera · entran algunas corcheas',
        que_notas='la octava entera, de Do a Do'),
    dict(clave='intermedio', nombre='Intermedio', nivel_ritmo=1,
        registro_treble=('C4', 'E5'), registro_bass=('C3', 'G3'),
        salto_max=3, compases=4, claves=('treble', 'bass'),
        que_ritmo='algún salto más y empieza la mano izquierda',
        que_notas='un poco más arriba, y ya con la mano izquierda'),
]

NIVELES_ADOLESCENTES = [
    dict(clave='facil', nombre='Fácil', nivel_ritmo=0,
        registro_treble=('C4', 'C5'), registro_bass=None,
        salto_max=2, compases=4, claves=('treble',),
        que_ritmo='la octava entera · redondas, blancas y negras',
        que_notas='la octava entera, de Do a Do'),
    dict(clave='medio', nombre='Medio', nivel_ritmo=1,
        registro_treble=('C4', 'D5'), registro_bass=('B2', 'C4'),
        salto_max=3, compases=4, claves=('treble', 'bass'),
        que_ritmo='las dos claves · corcheas y algún silencio',
        que_notas='las dos claves, un poco más ancho'),
    dict(clave='intermedio', nombre='Intermedio', nivel_ritmo=2,
        registro_treble=('A3', 'F6'), registro_bass=('F2', 'E4'),
        salto_max=4, compases=4, claves=('treble', 'bass'),
        que_ritmo='ritmo suelto, silencios a contratiempo',
        que_notas='todo el registro central del piano'),
]

GRUPOS = {
    'ninos': dict(
        kicker='PRUEBA DE NIVEL · NIÑOS (5-9 AÑOS)',
        niveles=NIVELES_NINOS,
        gap=8.6,
        instr_ritmo=('Lee cada línea en voz alta diciendo el nombre de las notas. Si ya '
                    'sabes dónde están en el piano, tócalas también. Da igual si te '
                    'equivocas: lo que importa es ver hasta dónde llegas sin atascarte.'),
        instr_notas=('Aquí no hay ritmo que contar: solo di el nombre de cada nota, lo '
                    'más rápido que puedas, de izquierda a derecha.'),
        semilla_base=4000,
    ),
    'adolescentes': dict(
        kicker='PRUEBA DE NIVEL · ADOLESCENTES (10-16 AÑOS)',
        niveles=NIVELES_ADOLESCENTES,
        gap=7.2,
        instr_ritmo=('Lee cada línea en voz alta y, si puedes, tócala al piano. No hace '
                    'falta que salga perfecta: el objetivo es ver con qué soltura lees, '
                    'no corregir cada fallo.'),
        instr_notas=('Sin ritmo, solo notas: di el nombre de cada una lo más rápido que '
                    'puedas, de izquierda a derecha.'),
        semilla_base=5000,
    ),
}

TIPOS = [
    dict(clave='notas', etiqueta='Agudeza visual', esquina='Lectura de notas'),
    dict(clave='ritmo', etiqueta='Lectura rítmica', esquina='Ritmo y notas'),
]


def cabecera(c, grupo_cfg, nivel_cfg, tipo_cfg, num, total):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, grupo_cfg['kicker'])
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, 'Hoja %d de %d' % (num, total))
    y -= 27

    titulo = '%s — %s' % (nivel_cfg['nombre'], tipo_cfg['etiqueta'])
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, titulo)
    y -= 17
    que = nivel_cfg['que_notas'] if tipo_cfg['clave'] == 'notas' else nivel_cfg['que_ritmo']
    y = _wrap(c, que, MARGIN, y, 'DejaVuSans', 9.6, CONTENT_W, 12.5, MUTED)
    y -= 3
    instr = grupo_cfg['instr_notas'] if tipo_cfg['clave'] == 'notas' else grupo_cfg['instr_ritmo']
    y = _wrap(c, instr, MARGIN, y, 'DejaVuSans', 9.2, CONTENT_W, 12.5, MUTED)
    y -= 9

    bh = 21
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - bh, 3, bh, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.0)
    c.setFillColor(NAVY)
    aviso = ('EN VOZ ALTA, DE UN TIRÓN · NO TE PARES A CORREGIR' if tipo_cfg['clave'] == 'notas'
            else 'EN VOZ ALTA, LÍNEA POR LÍNEA · NO TE SALTES NINGUNA')
    c.drawString(MARGIN + 13, y - 13.5, aviso)
    return y - bh - 12


# --------------------------------------------------------------------------
# LECTURA RÍTMICA — la línea completa (igual que antes), con las figuras y
# silencios del nivel.
# --------------------------------------------------------------------------
def rellenar_ritmo(c, y, lineas, gap, suelo):
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


# --------------------------------------------------------------------------
# AGUDEZA VISUAL — notas sueltas, TODAS del mismo valor (no hay ritmo que
# leer). El PASEO de notas —grados de la escala, rebote en los topes del
# registro, tirando siempre hacia el centro— es el mismo que usa
# `generador_lectura.linea()`, pero SIN pasar por su selección de patrones
# rítmicos: por compases, un patrón puede ser una sola redonda o dos
# blancas, y al tirar la duración (que aquí no pinta nada) la línea se
# quedaba con dos o tres notas sueltas en vez de una línea llena. Aquí se
# camina un número FIJO de notas por línea, siempre, sin que la cuenta
# dependa de qué patrón haya tocado en suerte.
# --------------------------------------------------------------------------
NOTAS_POR_LINEA = 8


def _paseo_notas(rng, grados, n, salto_max):
    ultimo = len(grados) - 1
    centro = ultimo / 2.0
    pos = (rng.randrange(len(grados) // 4, 3 * len(grados) // 4)
          if len(grados) >= 4 else len(grados) // 2)
    nombres = []
    for _ in range(n):
        paso = rng.randint(-salto_max, salto_max)
        if paso == 0:
            paso = rng.choice((-1, 1))
        # mismo rebote hacia el centro que usa `linea()`: sin esto, un
        # paseo al azar acaba pegado a un extremo del registro
        fuera = abs(pos - centro) / centro if centro else 0
        if fuera > 0.5 and rng.random() < fuera:
            paso = -abs(paso) if pos > centro else abs(paso)
        nueva = pos + paso
        if nueva < 0 or nueva > ultimo:
            nueva = pos - paso
        pos = max(0, min(ultimo, nueva))
        nombres.append(genlec._nombre(grados[pos]))
    return nombres


def _linea_de_notas(rng, tonalidad, clef, nivel_ritmo, salto_max):
    grados = genlec.escala_grados(tonalidad, clef, nivel_ritmo)
    return _paseo_notas(rng, grados, NOTAS_POR_LINEA, salto_max)


def _alto_linea_notas(gap, pitches, clef):
    """Cuánto ocupa una línea de agudeza visual: el mismo pentagrama de
       siempre, más lo que suba o baje cada nota por encima o por debajo —
       se mide con los mismos `before_staff`/`after_system` que usa la
       lectura rítmica, pasando cada nota como si fuera una negra suelta
       (sin plica no necesita más hueco, así que esto es conservador y
       nunca se queda corto)."""
    eventos = [{'pitch': p, 'dur': 'q'} for p in pitches]
    return (before_staff(gap, eventos, clef) + 4 * gap
            + after_system(gap, eventos, clef))


def rellenar_notas(c, y, lineas, gap, suelo):
    x = MARGIN + NUM_W
    ancho = CONTENT_W - NUM_W

    caben, usado = [], 0.0
    for ln in lineas:
        h = _alto_linea_notas(gap, ln['pitches'], ln['clef'])
        if y - usado - h < suelo:
            break
        caben.append((ln, h))
        usado += h
    if not caben:
        return y
    extra = min(16.0, max(0.0, (y - usado - suelo) / len(caben)))

    num = 1
    for ln, h in caben:
        pitches, clef = ln['pitches'], ln['clef']
        eventos = [{'pitch': p, 'dur': 'q'} for p in pitches]
        y -= before_staff(gap, eventos, clef) + extra / 2.0
        c.setFont('DejaVuSans-Bold', 8.2)
        c.setFillColor(ACCENT)
        c.drawRightString(MARGIN + NUM_W - 7, y - 2 * gap - 3, str(num))

        ys = draw_staff(c, x, y, ancho, gap=gap)
        top, bot = ys[0], ys[-1]
        draw_clef(c, x + 4, bot, gap, clef=clef)
        x0 = x + gap * (5.6 if clef == 'treble' else 4.8)
        paso = (x + ancho - 8 - x0) / max(1, len(pitches) - 1) if len(pitches) > 1 else 0
        for i, p in enumerate(pitches):
            draw_headless_note(c, x0 + i * paso, bot, top, gap, p, clef=clef)

        y = bot - after_system(gap, eventos, clef) - extra / 2.0
        num += 1
    return y


def caja_resultado(c, y, tipo_cfg):
    """La franja de abajo: lo rellena la profesora ahí mismo, en la propia
       clase — nada de plantilla aparte ni de pasar los datos después."""
    h = ALTO_RESULTADO
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)

    titulo = ('RESULTADO · LECTURA DE NOTAS' if tipo_cfg['clave'] == 'notas'
             else 'RESULTADO · LECTURA RÍTMICA')
    c.setFont('DejaVuSans-Bold', 9.2)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 15, y - 16, titulo)

    opciones = ['Lee fluido, sin dudar', 'Lee con dudas / se traba', 'No lee todavía']
    oy = y - 34
    for op in opciones:
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.9)
        c.rect(MARGIN + 15, oy - 8, 9, 9, fill=0, stroke=1)
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(INK)
        c.drawString(MARGIN + 30, oy - 6.3, op)
        oy -= 15

    lx = MARGIN + CONTENT_W * 0.46
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY)
    c.drawString(lx, y - 34, 'NIVEL ASIGNADO')
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(lx, y - 47, MARGIN + CONTENT_W - 10, y - 47)
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY)
    c.drawString(lx, y - 64, 'ÁLBUM RECOMENDADO')
    c.line(lx, y - 77, MARGIN + CONTENT_W - 10, y - 77)
    return y - h - 8


def pie(c, num):
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(num))
    c.showPage()


def construir_hoja(c, grupo_cfg, nivel_cfg, tipo_cfg, num, total, semilla):
    y = cabecera(c, grupo_cfg, nivel_cfg, tipo_cfg, num, total)
    y_caja = SUELO + ALTO_RESULTADO
    gap = grupo_cfg['gap']

    with _registro_propio(nivel_cfg['registro_treble'], nivel_cfg['registro_bass']):
        if tipo_cfg['clave'] == 'ritmo':
            lineas = genlec.hoja('Do mayor', semilla=semilla, n_lineas=24,
                                 nivel=nivel_cfg['nivel_ritmo'], compases=nivel_cfg['compases'],
                                 claves=nivel_cfg['claves'], salto_max=nivel_cfg['salto_max'])
            y = rellenar_ritmo(c, y, lineas, gap, y_caja + 12)
        else:
            rng = random.Random(semilla)
            claves = nivel_cfg['claves']
            lineas = []
            for i in range(24):
                clef = claves[i % len(claves)]
                pitches = _linea_de_notas(rng, 'Do mayor', clef, nivel_cfg['nivel_ritmo'],
                                          nivel_cfg['salto_max'])
                if pitches:
                    lineas.append(dict(pitches=pitches, clef=clef))
            y = rellenar_notas(c, y, lineas, gap, y_caja + 12)

    caja_resultado(c, y_caja, tipo_cfg)
    pie(c, num)


def construir(grupo):
    os.makedirs(SALIDA, exist_ok=True)
    nombre = 'Prueba_de_nivel_%s.pdf' % ('Ninos' if grupo == 'ninos' else 'Adolescentes')
    ruta = os.path.join(SALIDA, nombre)
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('Prueba de nivel · %s' % grupo)
    grupo_cfg = GRUPOS[grupo]

    hojas = [(nivel_cfg, tipo_cfg) for nivel_cfg in grupo_cfg['niveles'] for tipo_cfg in TIPOS]
    total = len(hojas)
    for i, (nivel_cfg, tipo_cfg) in enumerate(hojas):
        # semilla distinta por grupo, nivel Y tipo, para que ninguna hoja
        # repita la misma línea nota por nota
        semilla = grupo_cfg['semilla_base'] + i
        construir_hoja(c, grupo_cfg, nivel_cfg, tipo_cfg, i + 1, total, semilla)

    c.save()
    return ruta


def main(argv):
    for grupo in ('ninos', 'adolescentes'):
        ruta = construir(grupo)
        print('Prueba de nivel · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
