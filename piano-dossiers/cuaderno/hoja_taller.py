# -*- coding: utf-8 -*-
"""Hoja de TALLER: calentar los dedos y leer en voz alta, en la MISMA hoja.

   Formato pedido por el cliente para Arnau (10 anos, media hora de clase).
   En los cuadernos de nivel avanzado el calentamiento y la agudeza visual
   son dos hojas enteras; con media hora de clase eso no se mira. Aqui van
   las dos cosas en una sola hoja, partida por la mitad:

     ARRIBA · para los dedos  -> se toca. Saltos pequenos, porque hay que
       poder ponerlos con la mano sin mirar.
     ABAJO  · para la boca    -> NO se toca. Se dice el nombre de cada nota
       en voz alta. Saltos mas grandes y registro mas ancho, porque leer no
       cansa la mano.

   Y al pie, el recuadro de escucha, pequeno: lo dirige quien este al lado.

   Las dos mitades se generan (engine/generador_lectura.py) con semillas
   distintas, asi que no se parecen entre si ni se repiten de una cancion a
   otra. El numero de lineas no esta fijado: `rellenar` mete las que caben y
   reparte el hueco sobrante, que es lo que evita el palmo de papel en blanco
   al pie.

   El lenguaje de esta hoja va SIN TECNICISMOS a proposito. Donde en los
   cuadernos avanzados pone "registro", "tonalidad" o "anti-secuencia", aqui
   pone "notas agudas", "las notas de esta cancion" y "no te lo aprendas de
   memoria". Si una palabra tecnica hace falta de verdad, se explica en la
   misma linea en que aparece.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from generador_lectura import hoja as generar_hoja
from hoja_calentamiento import cabecera, rellenar, pie
from hoja_lectura import caja_escucha, ALTO_ESCUCHA
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')

GAP = 6.6
ALTO_BANDA = 19          # la banda que separa las dos mitades


def banda(c, y, texto, pista, color=ACCENT):
    """El rotulo que parte la hoja en dos. Sin el, el alumno toca la mitad de
       abajo — que es justo la que NO se toca."""
    h = ALTO_BANDA
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 3, fill=1, stroke=0)
    c.setFillColor(color)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 13, y - 13, texto)
    tw = stringWidth(texto, 'DejaVuSans-Bold', 8.6)
    size = _fit(pista, 'DejaVuSans', 7.8, CONTENT_W - tw - 40, floor=6.4)
    c.setFont('DejaVuSans', size)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 13 + tw + 12, y - 12.6, pista)
    return y - h - 9


def build_taller(c, cfg):
    ton = cfg.get('key_sig')
    nombre_ton = ton if ton else 'Do mayor'
    gap = cfg.get('gap', GAP)

    intro = cfg.get('intro') or (
        'Cinco minutos antes de abrir la partitura. Arriba se TOCA y abajo se LEE EN VOZ ALTA, sin '
        'tocar nada. Las dos mitades usan las notas de esta canción, así que cuando llegues a la '
        'partitura ya las tendrás en la mano y en la boca.')
    reglas = cfg.get('reglas') or ['ARRIBA SE TOCA', 'ABAJO SE LEE EN VOZ ALTA',
                                   'DESPACIO, QUE NO ES UNA CARRERA']

    y = cabecera(c, cfg, cfg.get('titulo', 'Dedos y ojos'),
                 cfg.get('esquina', 'Antes de la partitura'), intro, reglas)

    # --- mitad de arriba: se toca ------------------------------------------
    y = banda(c, y, 'PARA LOS DEDOS',
              cfg.get('pista_dedos',
                      'esto SÍ se toca · una mano cada vez, muy despacio, y no pares en los fallos'))
    dedos = generar_hoja(nombre_ton, semilla=cfg.get('semilla', 1),
                         n_lineas=14, nivel=cfg.get('nivel_lectura', 0),
                         compases=cfg.get('compases_linea', 4),
                         compases_extra=cfg.get('compases_extra',
                                                [(4, 4), (3, 4), (4, 4), (2, 4)]),
                         salto_max=cfg.get('salto_max', 3))

    # el reparto: la mitad de abajo necesita su banda, sus lineas y la caja de
    # escucha, asi que el suelo de la de arriba se calcula desde ahi.
    y_caja = 52 + ALTO_ESCUCHA
    # Cuanto hay que guardar abajo. Una linea entera (aire de arriba + las
    # cinco lineas + el sitio de las plicas que cuelgan) sale a unos 66 pt con
    # gap 6.6; con la cuenta corta se quedaban dos lineas y un palmo de papel
    # en blanco entre la ultima y el recuadro de escucha.
    n_leer = cfg.get('lineas_leer', 3)
    alto_leer = n_leer * 66 + ALTO_BANDA + 12
    suelo_dedos = y_caja + 14 + alto_leer

    y, cuantas = rellenar(c, y, dedos, gap=gap, key_sig=ton, suelo=suelo_dedos)

    # --- mitad de abajo: se lee, no se toca --------------------------------
    y = banda(c, y - 4, 'PARA LEER EN VOZ ALTA',
              cfg.get('pista_leer',
                      'esto NO se toca · di el nombre de cada nota, una por una, sin saltarte ninguna'),
              color=BLUE)
    leer = generar_hoja(nombre_ton, semilla=1000 + cfg.get('semilla', 1),
                        n_lineas=10, nivel=cfg.get('nivel_lectura', 0),
                        compases=cfg.get('compases_linea', 4),
                        compases_extra=cfg.get('compases_extra_leer',
                                               [(4, 4), (4, 4), (3, 4), (4, 4)]),
                        salto_max=cfg.get('salto_leer', 5))
    y, _ = rellenar(c, y, leer, gap=gap, key_sig=ton, desde=cuantas + 1,
                    suelo=y_caja + 14)

    preguntas = cfg.get('preguntas_escucha') or [
        ('A', 'Toco dos notas. ¿La segunda SUBE o BAJA?', ['↑', '↓'], 6),
        ('B', 'Toco una nota corta o larga. ¿Cuál era?', ['corta', 'larga'], 5),
        ('C', 'Toco dos veces. ¿Sonaron IGUAL o DISTINTO?', ['=', '≠'], 6),
    ]
    caja_escucha(c, y_caja, preguntas,
                 cfg.get('sub_escucha', 'no mires el teclado · rodea con lápiz lo que oigas'))
    pie(c, cfg)
    return y_caja - ALTO_ESCUCHA - 8
