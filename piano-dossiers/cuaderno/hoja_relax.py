# -*- coding: utf-8 -*-
"""Ultima hoja del dosier: RELAJACION al piano y DIARIO de la semana.

   Dos cosas que el cuaderno no tenia y que pidio el cliente.

   1. Relajacion muscular AL PIANO, no de gimnasia: cuatro gestos cortos que
      se tocan de verdad, sobre la tonalidad de la pieza. Van al final porque
      es cuando el brazo esta cansado, que es justo cuando hacen falta.

   2. Un diario semanal para que la profesora escriba los deberes y el alumno
      marque la semana siguiente si los ha hecho. Es la unica parte del
      cuaderno que se rellena a mano en clase, y por eso ocupa media hoja: si
      las lineas son estrechas, nadie escribe en ellas.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system
from page_layout_common import before_staff, after_system
from hoja_calentamiento import cabecera, pie
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')

GAP = 6.8

# Tonica de cada tonalidad, para que los gestos de relajacion caigan en la
# tonalidad de la pieza y no en un Do de manual.
TONICA = {
    'Do mayor': 'C', 'La menor': 'A', 'Sol mayor': 'G', 'Mi menor': 'E',
    'Re mayor': 'D', 'Si menor': 'B', 'La mayor': 'A', 'Mi mayor': 'E',
    'Fa mayor': 'F', 'Re menor': 'D', 'Sib mayor': 'B', 'Si♭ mayor': 'B',
    'Mib mayor': 'E', 'Mi♭ mayor': 'E', 'Sol menor': 'G', 'Do menor': 'C',
}
_ESC = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def _grado(letra, octava, n):
    """La nota que esta n grados por encima de letra+octava, con la octava
       bien contada. Antes esto se apanaba con un .replace('4','3') y en las
       tonalidades altas (Sol, La, Si) la quinta se iba a la octava de arriba
       sin que nadie lo bajara: salian redondas colgando de cuatro lineas
       adicionales sobre la clave de fa."""
    i = _ESC.index(letra) + n
    return '%s%d' % (_ESC[i % 7], octava + i // 7)


def _octava_base(letra, clef):
    """Donde se coloca la tonica para que los cinco dedos caigan DENTRO del
       pentagrama y no en lineas adicionales."""
    if clef == 'bass':
        return 3 if letra in ('C', 'D', 'E', 'F') else 2
    return 4


def gestos(tonalidad):
    """Los cuatro gestos, ya transportados a la tonalidad de la pieza."""
    t = TONICA.get(tonalidad or 'Do mayor', 'C')
    ob, oa = _octava_base(t, 'bass'), _octava_base(t, 'treble')
    bajo = [_grado(t, ob, n) for n in range(5)]      # tonica..quinta, mano izq.
    alto = [_grado(t, oa, n) for n in range(5)]      # tonica..quinta, mano der.
    return [
        ('Dejar caer el brazo',
         'Levanta el brazo entero y déjalo caer sobre la tecla. No empujes con el dedo: '
         'que suene el peso. Después suelta y deja la mano muerta encima.',
         'bass', [{'pitch': bajo[0], 'dur': 'w'}, {'rest': True, 'dur': 'w'},
                  {'pitch': bajo[4], 'dur': 'w'}, {'rest': True, 'dur': 'w'}]),
        ('La muñeca respira',
         'Toca las dos notas ligadas subiendo la muñeca en la primera y bajándola en la '
         'segunda, como si respirara. El sonido tiene que salir sin golpe.',
         'treble', [{'pitch': alto[0], 'dur': 'h'}, {'pitch': alto[2], 'dur': 'h'},
                    {'pitch': alto[4], 'dur': 'h'}, {'pitch': alto[2], 'dur': 'h'},
                    {'pitch': alto[0], 'dur': 'w'}]),
        ('El acorde que se apoya',
         'Coloca las tres notas sin tocar, apoya el brazo hasta que suenen solas y '
         'aguántalas contando cuatro. Si el antebrazo está duro, empieza otra vez.',
         'bass', [{'pitches': [bajo[0], bajo[2], bajo[4]], 'dur': 'w'},
                  {'rest': True, 'dur': 'w'},
                  {'pitches': [bajo[0], bajo[2], bajo[4]], 'dur': 'w'},
                  {'rest': True, 'dur': 'w'}]),
        ('Cinco teclas, sin apretar',
         'Los cinco dedos, uno detrás de otro, tan flojo como puedas sin que deje de sonar. '
         'Este es el ejercicio con el que se termina siempre.',
         'treble', [{'pitch': alto[0], 'dur': 'h'}, {'pitch': alto[1], 'dur': 'h'},
                    {'pitch': alto[2], 'dur': 'h'}, {'pitch': alto[3], 'dur': 'h'},
                    {'pitch': alto[4], 'dur': 'w'}, {'pitch': alto[0], 'dur': 'w'}]),
    ]


def _gesto(c, y, num, titulo, texto, clef, events, key_sig, gap=GAP):
    c.setFillColor(BLUE)
    c.roundRect(MARGIN, y - 13, 16, 16, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 8, y - 9.5, str(num))
    c.setFont('DejaVuSans-Bold', 9.6)
    c.setFillColor(INK)
    c.drawString(MARGIN + 23, y - 9, titulo)
    y -= 21

    col = CONTENT_W * 0.46
    y_txt = _wrap(c, texto, MARGIN, y, 'DejaVuSans', 8.0, col - 10, 10.6, MUTED)

    x = MARGIN + col
    ancho = CONTENT_W - col
    y_st = y - before_staff(gap, events, clef)
    top, bot = draw_system(c, x, y_st, ancho, gap, events, clef=clef,
                           time_sig=(4, 4), show_time=False, key_sig=key_sig,
                           spacing='engraved')
    y_mus = bot - after_system(gap, events, clef)
    return min(y_txt, y_mus) - 8


ETIQUETAS_HECHO = ('sí', 'a medias', 'no')


def _ancho_hecho():
    """Lo que miden las tres casillas de '¿hecho?' juntas. Se mide en vez de
       fijarlo: con un ancho a ojo, el 'no' de la ultima se salia del margen
       derecho y el auditor lo cazaba en las veinte canciones."""
    total = 0
    for etq in ETIQUETAS_HECHO:
        total += 9 + 3 + stringWidth(etq, 'DejaVuSans', 6.6) + 10
    return total - 10


def diario(c, y, filas=5, titulo='El diario de la semana', suelo=46):
    """La tabla que rellena la profesora. Las lineas son anchas a proposito.

       Las filas se estiran hasta el pie de la hoja: el diario es lo ultimo
       que hay, asi que dejar papel en blanco debajo no sirve para nada y
       escribir a mano en una linea estrecha, si."""
    c.setFont('DejaVuSans-Bold', 10.4)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, titulo.upper())
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.4)
    c.line(MARGIN, y - 6, MARGIN + 26, y - 6)
    c.setFont('DejaVuSans', 8)
    c.setFillColor(MUTED)
    tw = stringWidth(titulo.upper(), 'DejaVuSans-Bold', 10.4)
    c.drawString(MARGIN + tw + 12, y,
                 'lo escribe la profesora · lo marca el alumno la semana siguiente')
    y -= 18

    col_fecha = 64
    col_check = _ancho_hecho()
    x_check = MARGIN + CONTENT_W - col_check
    c.setFont('DejaVuSans-Bold', 6.8)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 4, y - 8, 'SEMANA')
    c.drawString(MARGIN + col_fecha + 6, y - 8, 'QUÉ HAY QUE HACER EN CASA')
    c.drawRightString(MARGIN + CONTENT_W, y - 8, '¿HECHO?')
    y -= 13

    # cuantas filas caben con la altura minima, y luego se reparte el sobrante
    fh, sep = 30.0, 4.0
    caben = int((y - suelo + sep) // (fh + sep))
    filas = max(3, min(filas, caben))
    fh = min(44.0, (y - suelo + sep) / filas - sep)

    for _ in range(filas):
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - fh, col_fecha, fh, 3, fill=1, stroke=0)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(MARGIN + col_fecha + 8, y - fh + 7, x_check - 12, y - fh + 7)

        bx = x_check
        for etq in ETIQUETAS_HECHO:
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(0.8)
            c.setFillColor(white)
            c.rect(bx, y - fh + 9, 9, 9, fill=1, stroke=1)
            c.setFont('DejaVuSans', 6.6)
            c.setFillColor(MUTED)
            c.drawString(bx + 12, y - fh + 11.5, etq)
            bx += 9 + 3 + stringWidth(etq, 'DejaVuSans', 6.6) + 10
        y -= fh + sep
    return y + sep


def build_relax(c, cfg):
    ton = cfg.get('key_sig')
    intro = ('Lo último de cada dosier. Arriba, cuatro gestos que se tocan al piano para soltar el '
             'brazo cuando ya está cansado; abajo, el diario: lo que hay que hacer en casa y una '
             'casilla para marcarlo la semana siguiente.')
    reglas = ['NUNCA APRIETES PARA QUE SUENE', 'SI EL BRAZO SE PONE DURO, PARA', 'RESPIRA']

    y = cabecera(c, cfg, 'Soltar y anotar', 'Relajación · y el diario de la semana',
                 intro, reglas)

    for i, (titulo, texto, clef, events) in enumerate(gestos(ton), 1):
        y = _gesto(c, y, i, titulo, texto, clef, events, ton, gap=cfg.get('gap', GAP))

    y -= 10
    y = diario(c, y, filas=cfg.get('filas_diario', 8))
    pie(c, cfg)
    return y
