# -*- coding: utf-8 -*-
"""Ultima hoja del dosier: SOLTANDO DEDOS.

   Rediseno pedido por el cliente. Antes eran cuatro gestos sueltos con su
   explicacion al lado; ahora es la hoja entera de pentagramas, como el
   calentamiento, pero con el material pensado para lo contrario: alli se
   despierta la mano, aqui se suelta.

   El esquema de relajacion no es un adorno del texto, esta metido en las
   notas y es lo unico que hace que esta hoja no sea otro calentamiento:

     1. LO QUE LA HACE LENTA ES EL TEMPO, NO LA FALTA DE NOTAS. Va escrito
        arriba (Muy lento, ♩=50) y el pentagrama va lleno. Una hoja medio
        vacia no relaja: aburre, y el alumno la pasa.
     2. ESTO SUENA. Las notas no son aleatorias: cada compas tiene su acorde
        (I - vi - IV - V, o i - VI - iv - v en menor), las notas salen de ese
        acorde, entre medias cae alguna nota de paso y cada linea cierra en
        la tonica. Tocar algo que suena mal tensa; tocar algo que suena bien
        es la mitad del ejercicio.
     3. NADA MAS CORTO QUE LA NEGRA. En cuanto aparecen corcheas la mano se
        pone a correr y se agarrota.
     4. SALTOS PEQUENOS. Un salto grande obliga a estirar la mano, y estirar
        es justo lo contrario de soltar.
     5. UNA MANO POR LINEA, ALTERNANDO. Mientras una toca, la otra se queda
        muerta encima del teclado, que es donde de verdad descansa.

   Y abajo, pequeno, el sitio donde la profesora escribe los deberes de ESA
   semana. Sin casillas de comprobacion: es una nota, no un examen.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from generador_lectura import hoja as generar_hoja
from hoja_calentamiento import cabecera, rellenar, pie
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')

GAP = 6.8
# Lo que se reserva abajo para los deberes. Subio de 74 a 88 al meter la linea
# "A LA CLASE": la tarea de la semana no se acaba en casa, vuelve a la clase, y
# esa linea dice con que hay que volver.
ALTO_DEBERES = 88


def deberes(c, y, titulo='ESTA SEMANA, EN CASA', lineas=3, sub=None, tarea=None):
    """El recuadro de deberes, al pie. Pequeno a proposito: es para UNA
       semana, no un registro del curso. Sin casillas de hecho / no hecho.

       Si viene `tarea` (norma de variedad del cliente), el recuadro trae ya
       escrita la tarea de esa semana y deja UNA raya libre para que la
       profesora anada lo suyo. Sin `tarea` se comporta como antes: rayas
       vacias. Antes de esto los 37 dosieres de Dilan y Eva llevaban el mismo
       recuadro en blanco, que es justo lo que la norma no quiere."""
    h = ALTO_DEBERES
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)

    cabeza = tarea['etiqueta'] if tarea else titulo
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 14, y - 15, cabeza)
    tw = stringWidth(cabeza, 'DejaVuSans-Bold', 8.6)
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 14 + tw + 10, y - 15,
                 sub or ('para esta semana' if tarea
                         else 'lo escribe la profesora al final de la clase'))

    if tarea:
        yy = _wrap(c, tarea['texto'], MARGIN + 14, y - 27, 'DejaVuSans', 7.8,
                   CONTENT_W - 28, 10.4, INK)
        # La tarea no muere en casa: vuelve a la clase. Dilan y Eva vienen a
        # clase igual que Jose Maria, y esta linea es su equivalente del
        # recuadro "para la proxima clase" del formato de adulto.
        if tarea.get('clase'):
            c.setFont('DejaVuSans-Bold', 6.8)
            c.setFillColor(ACCENT)
            c.drawString(MARGIN + 14, yy - 3, 'A LA CLASE:')
            c.setFont('DejaVuSans', 7.4)
            c.setFillColor(INK)
            c.drawString(MARGIN + 14 + stringWidth('A LA CLASE:', 'DejaVuSans-Bold', 6.8) + 6,
                         yy - 3, tarea['clase'])
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(MARGIN + 14, y - h + 12, MARGIN + CONTENT_W - 14, y - h + 12)
        c.setFont('DejaVuSans', 6.6)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + 14, y - h + 4, 'y lo que apunte la profesora')
        return y - h - 8

    yy = y - 30
    paso = (h - 34) / lineas
    for _ in range(lineas):
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(MARGIN + 14, yy, MARGIN + CONTENT_W - 14, yy)
        yy -= paso
    return y - h - 8


def build_relax(c, cfg):
    ton = cfg.get('key_sig')
    nombre_ton = ton if ton else 'Do mayor'
    intro = ('Lo último de la clase, con el brazo ya cansado. No es un ejercicio: es dejar de hacer '
             'fuerza. Lo que lo hace lento es el tempo de aquí abajo, no las notas — esto es música de '
             'verdad, sobre los acordes de %s, y cada línea acaba en su nota de casa. Una línea cada '
             'mano, alternando: mientras una toca, la otra descansa encima de las teclas.' % nombre_ton)
    reglas = cfg.get('reglas_relax') or ['EL BRAZO CAE, NO EMPUJA',
                                         'EN CADA SILENCIO, SUELTA LA MANO',
                                         'SI SUENA FUERTE, ES QUE APRIETAS']

    y = cabecera(c, cfg, 'Soltando dedos', 'Relajación · para terminar', intro, reglas)

    # El tempo escrito, como en cualquier partitura. Es la pieza clave de esta
    # hoja: lo que la hace lenta es esto, no tener el pentagrama medio vacio.
    tempo = cfg.get('tempo_relax', 'Muy lento   ♩ = 50')
    c.setFont('DejaVuSans-Bold', 11)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y - 9, tempo)
    c.setFont('DejaVuSans', 7.8)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + stringWidth(tempo, 'DejaVuSans-Bold', 11) + 12, y - 9,
                 'con el metrónomo puesto · si no llegas a soltar la mano entre nota y nota, bájalo más')
    y -= 20

    lineas = generar_hoja(nombre_ton, semilla=2000 + cfg.get('semilla', 1),
                          n_lineas=20, nivel=0, relax=True,
                          compases_extra=cfg.get('compases_relax') or [(4, 4), (4, 4), (3, 4)])
    y_caja = 48 + ALTO_DEBERES
    y, _ = rellenar(c, y, lineas, gap=cfg.get('gap', GAP), key_sig=ton,
                    suelo=y_caja + 12)

    deberes(c, y_caja, lineas=cfg.get('lineas_deberes', 3),
            sub=cfg.get('sub_deberes'), tarea=cfg.get('tarea'))
    y = y_caja - ALTO_DEBERES
    pie(c, cfg)
    return y
