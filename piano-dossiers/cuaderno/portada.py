# -*- coding: utf-8 -*-
"""Portada e indice del CUADERNO (formato nuevo, escrito de cero).

   Diferencias de fondo con la portada antigua:
   - Paleta de la marca real (azul noche del logo T-Clas), no verde.
   - El indice no lista "dificultad en estrellas" (que no dice nada), sino
     QUE SE TRABAJA en cada pieza: es la columna que convierte el listado en
     un plan de curso legible de un vistazo.
   - El repertorio se agrupa por etapa tecnica (no por mes), para que se vea
     el arco pedagogico: Do mayor -> primera armadura -> retos -> a duo.
"""
import os
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

for _n, _p in [('DejaVuSans', 'DejaVuSans.ttf'), ('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf'),
               ('DejaVuSerif', 'DejaVuSerif.ttf'), ('DejaVuSerif-Bold', 'DejaVuSerif-Bold.ttf')]:
    try:
        pdfmetrics.registerFont(TTFont(_n, f'/usr/share/fonts/truetype/dejavu/{_p}'))
    except Exception:
        pass

W, H = 595.276, 841.89
MARGIN = 52
CONTENT_W = W - 2 * MARGIN

# Paleta tomada del logo real
NAVY = HexColor('#1A2332')
NAVY_SOFT = HexColor('#3C4A5E')
CREAM = HexColor('#FDFBF6')
RULE = HexColor('#C9CFD8')
INK = HexColor('#232323')
MUTED = HexColor('#7C838F')
ACCENT = HexColor('#8C6A3F')


# Textos que ni encogiendo hasta el minimo caben en su hueco. Se apuntan aqui
# en vez de fallar: quien los mira es el auditor, que los saca todos de una
# vez. Sin esto, un texto que se sale de SU CAJA (no del margen de la pagina)
# no lo ve nadie hasta que el dosier esta impreso -- paso de verdad, con
# "Ninguna negra ni bemol" pisando la casilla de al lado en una ficha.
NO_CABEN = []


def _fit(text, font, size, max_w, floor=7.0, caja=False):
    """Encoge el texto hasta que quepa en max_w, sin bajar de `floor`.

       `caja=True` quiere decir que max_w es una CAJA de verdad —una casilla,
       una tarjeta— y no un hueco holgado: si ni al minimo cabe, el texto se
       mete en la casilla de al lado y hay que apuntarlo. En los sitios donde
       max_w lleva margen de sobra (un pie de foto que ocupa el ancho de la
       hoja) pasarse un pelo no se ve, y marcarlo solo produce ruido."""
    while size > floor and stringWidth(text, font, size) > max_w:
        size -= 0.25
    if caja and stringWidth(text, font, size) > max_w + 0.5:
        NO_CABEN.append((text[:60], round(max_w, 1), round(size, 2)))
    return size


def _clip(text, font, size, max_w):
    """Recorta el texto a lo que quepa en max_w, con puntos suspensivos.
       Para sitios donde el ancho no depende del texto (un tramo de la barra
       de forma) y encoger la fuente ya no basta."""
    if max_w <= 0:
        return ''
    if stringWidth(text, font, size) <= max_w:
        return text
    for k in range(len(text) - 1, 0, -1):
        recorte = text[:k].rstrip() + '…'
        if stringWidth(recorte, font, size) <= max_w:
            return recorte
    return ''


def _wrap(c, text, x, y, font, size, max_w, leading, color):
    c.setFont(font, size)
    c.setFillColor(color)
    line = ''
    for word in text.split(' '):
        test = (line + ' ' + word).strip()
        if stringWidth(test, font, size) <= max_w:
            line = test
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def build_cover(c, logo_path, alumno, subtitulo, curso):
    """Portada: fondo crema, logo grande centrado, titulo y alumno."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # marco fino
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.rect(MARGIN * 0.62, MARGIN * 0.62, W - MARGIN * 1.24, H - MARGIN * 1.24, fill=0, stroke=1)

    logo_size = 196
    y = H - 215
    try:
        c.drawImage(logo_path, (W - logo_size) / 2, y - logo_size, logo_size, logo_size,
                    mask='auto', preserveAspectRatio=True)
    except Exception:
        pass
    y -= logo_size + 52

    c.setFont('DejaVuSerif-Bold', 30)
    c.setFillColor(NAVY)
    c.drawCentredString(W / 2, y, 'El Cuaderno')
    y -= 34
    c.drawCentredString(W / 2, y, 'del Pianista')
    y -= 30

    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(W / 2 - 62, y, W / 2 + 62, y)
    y -= 30

    size = _fit(alumno.upper(), 'DejaVuSans-Bold', 16, CONTENT_W - 40)
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(NAVY_SOFT)
    c.drawCentredString(W / 2, y, alumno.upper())
    y -= 20

    c.setFont('DejaVuSans', 10.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, subtitulo)
    y -= 15
    c.drawCentredString(W / 2, y, curso)

    c.setFont('DejaVuSans', 8)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, MARGIN * 0.62 + 16, 'T-CLAS  ·  DESPIERTA TU SONIDO INTERIOR')
    c.showPage()


BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')

# Color de cada tipo de semana. El repaso y el concierto tienen que verse de
# lejos: son las semanas que se saltan cuando se va con retraso, y justamente
# son las que no hay que saltarse.
_COLOR_TIPO = {
    'obra': NAVY_SOFT,
    'especial': ACCENT,
    'repaso': BLUE,
    'concierto': NAVY,
}


def build_plan_curso(c, alumno, plan, page_num=3, titulo='El curso, semana a semana',
                     nota=None):
    """La pagina que reparte las piezas del cuaderno en el curso escolar.

       plan: [(nombre_del_mes, [(n_semana, texto, tipo), ...]), ...]

       Es la unica pagina del cuaderno que mira el curso entero de una vez, y
       sirve para dos cosas distintas: la profesora ve si va con retraso, y el
       alumno ve cuanto queda para lo que le apetece tocar. Por eso las
       semanas especiales (Halloween, Navidad, el concierto) van marcadas: son
       las fechas que el alumno se sabe de memoria y alrededor de las cuales
       se ordena todo lo demas.

       El plan es una propuesta, no un horario: si una pieza pide tres semanas
       se le dan, y se recorta de las de repaso. Eso lo dice la propia hoja."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    total = sum(len(s) for _, s in plan)
    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, '%s  ·  PLAN DE CURSO' % alumno.upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, '%d semanas · de septiembre a julio' % total)
    y -= 27

    c.setFont('DejaVuSerif-Bold', 23)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, titulo)
    y -= 14
    y = _wrap(c, nota or
              ('Las %d semanas del curso, repartidas. Cada pieza tiene dos semanas: la primera para '
               'leerla y desmontarla, la segunda para montarla entera. Es una propuesta, no un horario: '
               'si una pieza pide tres semanas se le dan y se recorta de las de repaso.' % total),
              MARGIN, y, 'DejaVuSans', 8.8, CONTENT_W, 11.0, MUTED)
    y -= 9

    # leyenda
    lx = MARGIN
    for etq, tipo in (('pieza nueva', 'obra'), ('semana señalada', 'especial'),
                      ('repaso', 'repaso'), ('concierto', 'concierto')):
        c.setFillColor(_COLOR_TIPO[tipo])
        c.circle(lx + 3, y - 3, 3, fill=1, stroke=0)
        c.setFont('DejaVuSans', 7.6)
        c.setFillColor(MUTED)
        c.drawString(lx + 10, y - 5.6, etq)
        lx += 10 + stringWidth(etq, 'DejaVuSans', 7.6) + 20
    y -= 16

    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(MARGIN, y, W - MARGIN, y)
    y -= 16

    # dos columnas de meses
    col_w = (CONTENT_W - 22) / 2.0
    mitad = (len(plan) + 1) // 2
    columnas = [plan[:mitad], plan[mitad:]]
    y_top = y

    # La altura de linea se calcula para que la columna mas larga acabe justo
    # encima del pie. Con un valor fijo sobraba un tercio de hoja en blanco:
    # aqui no hay nada que anadir, asi que lo que se hace es repartir el aire.
    ALTO_MES, SEP_MES = 15.0, 9.0
    n_meses = max(len(col) for col in columnas)
    n_sem = max(sum(len(s) for _, s in col) for col in columnas)
    rh = (y_top - 56 - n_meses * (ALTO_MES + SEP_MES)) / n_sem
    rh = min(max(rh, 13.0), 21.0)

    for ci, meses in enumerate(columnas):
        x = MARGIN + ci * (col_w + 22)
        yy = y_top
        for mes, semanas in meses:
            c.setFont('DejaVuSans-Bold', 9.2)
            c.setFillColor(NAVY)
            c.drawString(x, yy, mes.upper())
            c.setStrokeColor(NAVY)
            c.setLineWidth(1.3)
            c.line(x, yy - 5, x + 20, yy - 5)
            yy -= ALTO_MES

            for n, texto, tipo in semanas:
                col = _COLOR_TIPO.get(tipo, NAVY_SOFT)
                relleno = tipo in ('especial', 'concierto')
                base = yy - rh / 2.0 - 2.4          # centrado en su fila
                c.setFillColor(col if relleno else PANEL)
                c.roundRect(x, base - 3.9, 19, 13, 2.5, fill=1, stroke=0)
                c.setFont('DejaVuSans-Bold', 6.8)
                c.setFillColor(white if relleno else col)
                c.drawCentredString(x + 9.5, base, str(n))

                fuente = 'DejaVuSans' if tipo == 'obra' else 'DejaVuSans-Bold'
                ts = _fit(texto, fuente, 7.9, col_w - 25, floor=6.0)
                c.setFont(fuente, ts)
                c.setFillColor(INK if tipo == 'obra' else col)
                c.drawString(x + 25, base, _clip(texto, fuente, ts, col_w - 25))
                yy -= rh
            yy -= SEP_MES

    _footer(c, page_num)
    c.showPage()
    return page_num


def _index_header(c, alumno, continuacion=False):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, f'{alumno.upper()}  ·  REPERTORIO' + ('  (CONTINUACIÓN)' if continuacion else ''))
    y -= 26
    c.setFont('DejaVuSerif-Bold', 21)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'Índice del cuaderno' if not continuacion else 'Índice (continuación)')
    y -= 16

    if not continuacion:
        c.setFont('DejaVuSans', 8.8)
        c.setFillColor(MUTED)
        c.drawString(MARGIN, y, 'La columna de la derecha es el plan del curso: qué entra con cada pieza.')
        y -= 12
    y -= 6
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(MARGIN, y, W - MARGIN, y)
    return y - 22


def _footer(c, page_num):
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(page_num))


def build_index(c, alumno, etapas, start_page=2):
    """etapas: lista de (titulo_etapa, subtitulo, [fila, ...]) donde fila es
       dict(num, titulo, autor, tonalidad, compas, trabaja)."""
    COL_SKILL_W = 196
    COL_KEY_X = MARGIN + CONTENT_W - COL_SKILL_W - 84
    ROW_H = 23.5
    page = start_page
    y = _index_header(c, alumno)

    for etapa, sub, filas in etapas:
        need = 30 + ROW_H * min(len(filas), 2)
        if y - need < 56:
            _footer(c, page)
            c.showPage()
            page += 1
            y = _index_header(c, alumno, continuacion=True)

        c.setFillColor(NAVY)
        c.setFont('DejaVuSans-Bold', 9.6)
        c.drawString(MARGIN, y, etapa.upper())
        tw = stringWidth(etapa.upper(), 'DejaVuSans-Bold', 9.6)
        # El subtitulo va pegado detras del titulo de la etapa, asi que el
        # ancho que le queda depende de lo largo que sea el titulo: escrito a
        # pelo se salia del margen derecho (7 pt en el indice de Nel, con
        # "TONALIDADES NUEVAS, Y UNA MARCHA DE VERDAD").
        libre = CONTENT_W - tw - 10
        ssize = _fit(sub, 'DejaVuSans', 8.4, libre)
        c.setFont('DejaVuSans', ssize)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + tw + 10, y, _clip(sub, 'DejaVuSans', ssize, libre))
        y -= 6
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.4)
        c.line(MARGIN, y, MARGIN + 26, y)
        y -= 13

        for row in filas:
            if y - ROW_H < 50:
                _footer(c, page)
                c.showPage()
                page += 1
                y = _index_header(c, alumno, continuacion=True)

            c.setFont('DejaVuSerif-Bold', 11)
            c.setFillColor(ACCENT)
            c.drawRightString(MARGIN + 17, y - 10, str(row['num']))

            tsize = _fit(row['titulo'], 'DejaVuSans-Bold', 10.2, COL_KEY_X - (MARGIN + 26) - 12)
            c.setFont('DejaVuSans-Bold', tsize)
            c.setFillColor(INK)
            c.drawString(MARGIN + 26, y - 6, row['titulo'])

            asize = _fit(row['autor'], 'DejaVuSans', 7.7, COL_KEY_X - (MARGIN + 26) - 12)
            c.setFont('DejaVuSans', asize)
            c.setFillColor(MUTED)
            c.drawString(MARGIN + 26, y - 16, row['autor'])

            c.setFont('DejaVuSans', 8)
            c.setFillColor(NAVY_SOFT)
            c.drawString(COL_KEY_X, y - 6, row['tonalidad'])
            c.setFillColor(MUTED)
            c.drawString(COL_KEY_X, y - 16, row['compas'])

            sx = MARGIN + CONTENT_W - COL_SKILL_W
            c.setStrokeColor(RULE)
            c.setLineWidth(0.7)
            c.line(sx - 12, y - 20, sx - 12, y + 2)
            ssize = _fit(row['trabaja'], 'DejaVuSans', 8.5, COL_SKILL_W, floor=7.0)
            c.setFont('DejaVuSans', ssize)
            c.setFillColor(NAVY)
            c.drawString(sx, y - 10, row['trabaja'])

            y -= ROW_H
            c.setStrokeColor(HexColor('#E8E4DC'))
            c.setLineWidth(0.6)
            c.line(MARGIN, y + 5, W - MARGIN, y + 5)

        y -= 9

    _footer(c, page)
    c.showPage()
    return page
