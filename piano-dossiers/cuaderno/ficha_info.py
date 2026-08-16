# -*- coding: utf-8 -*-
"""Ficha de información de una partitura: la hoja que va justo detrás de la
   partitura. Esquemática y visual — nada de prosa larga.

   Bloques:
     1. Cabecera + tira de datos (tonalidad, compás, nº de compases, carácter)
     2. MAPA DE LA PIEZA — barra segmentada con las secciones reales
     3. DÓNDE VAN LAS MANOS — teclado dibujado con las teclas de arranque
     4. LO ESPECIAL DE ESTA PARTITURA — los hechos concretos de ESTA edición
     5. EL RETO / EL TRUCO
     6. ¿SABÍAS QUE?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap, _clip)

BLUE = HexColor('#3E6E8F')
WARM = HexColor('#F4EFE3')
PANEL = HexColor('#F3F1EA')

# El pie de pagina escribe con la base en 26 y sube unos 7 pt: por debajo de
# esto la ultima caja se le monta encima.
SUELO_FICHA = 34

WHITE_SEQ = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
BLACK_AFTER = {0, 1, 3, 4, 5}   # hay tecla negra tras Do, Re, Fa, Sol, La


def draw_keyboard(c, x, y_top, n_white, kw, kh, marks=None, start_idx=0):
    """Teclado esquemático.
       marks: {indice_blanca_global: (color, etiqueta, nivel)} — el nivel
       (0, 1, ...) escalona la etiqueta hacia arriba para que dos teclas
       vecinas no solapen sus rótulos."""
    marks = marks or {}
    bw, bh = kw * 0.60, kh * 0.62

    for i in range(n_white):
        gi = start_idx + i
        kx = x + i * kw
        col = marks.get(gi, (None, None, 0))[0]
        c.setFillColor(col if col else white)
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.8)
        c.rect(kx, y_top - kh, kw, kh, fill=1, stroke=1)
        name = WHITE_SEQ[gi % 7]
        c.setFont('DejaVuSans-Bold' if col else 'DejaVuSans', 6.6)
        c.setFillColor(white if col else MUTED)
        c.drawCentredString(kx + kw / 2, y_top - kh + 6, name)

    for i in range(n_white):
        gi = start_idx + i
        if (gi % 7) in BLACK_AFTER and i < n_white - 1:
            bx = x + (i + 1) * kw - bw / 2
            c.setFillColor(NAVY)
            c.setStrokeColor(NAVY)
            c.setLineWidth(0.6)
            c.rect(bx, y_top - bh, bw, bh, fill=1, stroke=1)

    # Rotulos: se desplazan lateralmente (dx) para que dos teclas vecinas no
    # solapen, y la guia va en "V" desde la tecla hasta el rotulo.
    for gi, mk in marks.items():
        col, label = mk[0], mk[1]
        dx = mk[2] if len(mk) > 2 else 0
        if label is None:
            continue
        i = gi - start_idx
        kx = x + i * kw + kw / 2
        lx = kx + dx
        ly = y_top + 11
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(col)
        c.drawCentredString(lx, ly, label)
        c.setStrokeColor(col)
        c.setLineWidth(1.1)
        c.line(kx, y_top + 1, kx, y_top + 4)
        c.line(kx, y_top + 4, lx, ly - 3)
    return y_top - kh


def keyboard_row(c, y, pasos, legend=None, kh=46, n_white=8, start_idx=0):
    """Fila de mini-teclados que muestran cómo evoluciona la posición de las
       manos a lo largo de la pieza. Cada paso: (titulo, {idx: color}).
       Es el bloque que explica de un vistazo el juego real de la pieza."""
    n = len(pasos)
    gapx = 20
    kbw = (CONTENT_W - gapx * (n - 1)) / n
    kw = kbw / n_white
    lowest = y
    for i, (titulo, keys) in enumerate(pasos):
        bx = MARGIN + i * (kbw + gapx)
        c.setFont('DejaVuSans-Bold', 8.2)
        c.setFillColor(NAVY)
        c.drawString(bx, y, titulo)
        marks = {gi: (col, None) for gi, col in keys.items()}
        bot = draw_keyboard(c, bx, y - 12, n_white, kw, kh,
                            marks=marks, start_idx=start_idx)
        lowest = min(lowest, bot)
        if i < n - 1:
            c.setFillColor(MUTED)
            c.setFont('DejaVuSans-Bold', 12)
            c.drawCentredString(bx + kbw + gapx / 2, y - 12 - kh / 2 - 4, '›')

    if legend:
        ly = lowest - 14
        lx = MARGIN
        for col, txt in legend:
            c.setFillColor(col)
            c.roundRect(lx, ly - 6.5, 9, 9, 1.5, fill=1, stroke=0)
            c.setFont('DejaVuSans-Bold', 7.6)
            c.setFillColor(col)
            c.drawString(lx + 13, ly - 4.5, txt)
            lx += 13 + stringWidth(txt, 'DejaVuSans-Bold', 7.6) + 22
        lowest = ly - 10
    return lowest


def tarjetas(c, y, items):
    """Fila de tarjetas para niveles altos: compases / nombre / explicacion.
       Sustituye a los mini-teclados, que a partir de cierto nivel sobran.
       La altura se calcula con el texto mas largo: si se fija a ojo, la
       tarjeta mas cargada se desborda por abajo y pisa lo que venga debajo."""
    n = len(items)
    sep = 10
    bw = (CONTENT_W - sep * (n - 1)) / n
    nmax = 1
    for _, _, texto in items:
        cnt, ln = 1, ''
        for wd in texto.split():
            t = (ln + ' ' + wd).strip()
            if stringWidth(t, 'DejaVuSans', 6.9) > bw - 18:
                cnt += 1; ln = wd
            else:
                ln = t
        nmax = max(nmax, cnt)
    h = 40 + nmax * 8.6
    for i, (cc, nombre, texto) in enumerate(items):
        bx = MARGIN + i * (bw + sep)
        c.setFillColor(PANEL)
        c.roundRect(bx, y - h, bw, h, 4, fill=1, stroke=0)
        c.setFillColor(BLUE)
        c.rect(bx, y - h, bw, 2.6, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 7.0)
        c.setFillColor(MUTED)
        # NO se pone en mayusculas: 'Cm' pasaria a 'CM', que en cifrado
        # americano es Do MAYOR. Un error musical de verdad.
        c.drawString(bx + 9, y - 13, cc)
        ns = _fit(nombre, 'DejaVuSerif-Bold', 11.5, bw - 18, floor=8.0, caja=True)
        c.setFont('DejaVuSerif-Bold', ns)
        c.setFillColor(NAVY)
        c.drawString(bx + 9, y - 28, nombre)
        _wrap(c, texto, bx + 9, y - 38, 'DejaVuSans', 6.9, bw - 18, 8.6, MUTED)
    return y - h


def _qr_block(c, x, y, w, png_path, titulo, texto, h=78):
    """Cuadro con el QR de audio. El título va arriba a todo el ancho del
       cuadro (si se pone al lado del QR no cabe y se sale del margen)."""
    c.setFillColor(PANEL)
    c.roundRect(x, y - h, w, h, 4, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(x, y - h, 3, h, fill=1, stroke=0)

    tsize = _fit(titulo.upper(), 'DejaVuSans-Bold', 7.4, w - 24, floor=6.0)
    c.setFont('DejaVuSans-Bold', tsize)
    c.setFillColor(NAVY)
    c.drawString(x + 12, y - 15, titulo.upper())

    # el QR se come casi todo el alto del recuadro: cuando la caja tiene que
    # encoger, lo que no puede encoger con ella es el codigo (si baja de unos
    # 40 pt el movil ya no lo lee)
    qs = min(h - 28, 52)
    qy = y - 21 - qs
    try:
        c.drawImage(png_path, x + 12, qy, qs, qs, mask='auto')
    except Exception:
        pass
    tx = x + 12 + qs + 10
    _wrap(c, texto, tx, y - 32, 'DejaVuSans', 8, w - (tx - x) - 12, 10.6, INK)
    return y - h


def _section_title(c, x, y, text, w=None):
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(NAVY)
    c.drawString(x, y, text.upper())
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.3)
    c.line(x, y - 5, x + 22, y - 5)
    return y - 18


def _fact_strip(c, y, facts):
    """Tira de 4 datos duros, en cajas iguales."""
    n = len(facts)
    gapx = 8
    bw = (CONTENT_W - gapx * (n - 1)) / n
    bh = 48
    for i, (label, value) in enumerate(facts):
        bx = MARGIN + i * (bw + gapx)
        c.setFillColor(PANEL)
        c.roundRect(bx, y - bh, bw, bh, 4, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.rect(bx, y - bh, 2.6, bh, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', _fit(label.upper(), 'DejaVuSans-Bold', 6.6,
                                          bw - 18, floor=5.2, caja=True))
        c.setFillColor(MUTED)
        c.drawString(bx + 10, y - 15, label.upper())
        size = _fit(value, 'DejaVuSerif-Bold', 13, bw - 18, floor=6.6, caja=True)
        c.setFont('DejaVuSerif-Bold', size)
        c.setFillColor(NAVY)
        c.drawString(bx + 10, y - 34, value)
    return y - bh - 26


def _map_bar(c, y, secciones, total_compases):
    """Barra segmentada con la forma real de la pieza."""
    bh = 36
    x = MARGIN
    for (etq, desde, hasta, desc, col) in secciones:
        frac = (hasta - desde + 1) / total_compases
        sw = CONTENT_W * frac
        c.setFillColor(col)
        c.roundRect(x, y - bh, sw, bh, 3, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 10)
        c.setFillColor(white)
        # Un tramo de un solo compas sobre un total de 32 mide 15 pt: ahi no
        # cabe nada. Se recorta a lo que quepa antes que dejarlo salir del
        # bloque, que es lo que hacia (y lo pillo el auditor de margenes).
        aw = sw - 14
        c.drawString(x + 9, y - 15, _clip(etq, 'DejaVuSans-Bold', 10, aw))
        dsize = _fit(desc, 'DejaVuSans', 7.4, aw, floor=5.6)
        c.setFont('DejaVuSans', dsize)
        c.drawString(x + 9, y - 27, _clip(desc, 'DejaVuSans', dsize, aw))
        c.setFont('DejaVuSans', 6.8)
        c.setFillColor(MUTED)
        c.drawString(x, y - bh - 10, f'c. {desde}')
        x += sw + 3
    c.setFont('DejaVuSans', 6.8)
    c.setFillColor(MUTED)
    c.drawRightString(MARGIN + CONTENT_W, y - bh - 10, f'c. {total_compases}')
    return y - bh - 30


def _bullets(c, x, y, w, items, dot=NAVY, size=8.6, leading=11.6):
    for it in items:
        c.setFillColor(dot)
        # el punto va sobre la PRIMERA linea del item: _wrap dibuja esa linea
        # con la base en y, asi que hay que subirlo, no bajarlo. Puesto debajo
        # de la base se colaba entre la primera y la segunda linea.
        c.circle(x + 2.4, y + size * 0.30, 1.7, fill=1, stroke=0)
        y = _wrap(c, it, x + 11, y, 'DejaVuSans', size, w - 11, leading, INK)
        y -= 3.5
    return y


def _rhythm_stack(c, x, y, w, bloques, time_sig):
    """El patrón rítmico de cada sección, uno debajo del otro, con notación
       real. Es un compás por sección: ilustra el dibujo, no es un ejercicio."""
    gap = 6.4
    for blq in bloques:
        etq, desc, events, color = blq[0], blq[1], blq[2], blq[3]
        clef = blq[4] if len(blq) > 4 else 'treble'
        key_sig = blq[5] if len(blq) > 5 else None
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(color)
        c.drawString(x, y, etq)
        # el rotulo se coloca DESPUES de medir la etiqueta: con un hueco fijo
        # de 14 pt, una etiqueta de dos letras se come la primera palabra
        ex = x + stringWidth(etq, 'DejaVuSans-Bold', 8.4) + 7
        ds = _fit(desc, 'DejaVuSans', 8, w - (ex - x), floor=6.2)
        c.setFont('DejaVuSans', ds)
        c.setFillColor(MUTED)
        c.drawString(ex, y, desc)
        top, bot = draw_system(c, x, y - 24, w, gap, events,
                               clef=clef, time_sig=time_sig, key_sig=key_sig)
        y = bot - 30
    return y + 8


def _lineas_texto(texto, w, size):
    cnt, tmp = 1, ''
    for word in texto.split(' '):
        t = (tmp + ' ' + word).strip()
        if stringWidth(t, 'DejaVuSans', size) <= w:
            tmp = t
        else:
            cnt += 1
            tmp = word
    return cnt


def _alto_note_box(texto, w, size=8.4, leading=11.4):
    """Lo que va a medir la caja, sin dibujarla. Hace falta para repartir el
       espacio del pie de la ficha antes de empezar a pintar."""
    return 24 + _lineas_texto(texto, w - 22, size) * leading


def _note_box(c, x, y, w, titulo, texto, color, h=None, suelo=None):
    """Recuadro de texto. Si se da `suelo`, la letra encoge hasta que la caja
       quepa por encima de esa altura.

       Sin ese ajuste, un '¿Sabías que...?' un poco mas largo de lo normal
       bajaba hasta pisar el pie de pagina — y pasaba de verdad en ocho de las
       veinte canciones, con el texto del pie impreso encima del recuadro."""
    size, leading = 8.4, 11.4
    if suelo is not None and h is None:
        while size > 6.6:
            alto = 24 + _lineas_texto(texto, w - 22, size) * leading
            if y - alto >= suelo:
                break
            size -= 0.2
            leading = size * 1.357
    h = h or (24 + _lineas_texto(texto, w - 22, size) * leading)
    c.setFillColor(PANEL)
    c.roundRect(x, y - h, w, h, 4, fill=1, stroke=0)
    c.setFillColor(color)
    c.rect(x, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.4)
    c.setFillColor(color)
    c.drawString(x + 12, y - 14, titulo.upper())
    _wrap(c, texto, x + 12, y - 26, 'DejaVuSans', size, w - 22, leading, INK)
    return y - h


def build_ficha(c, cfg):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, cfg['kicker'].upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, 'Ficha de la partitura')
    y -= 30

    tsize = _fit(cfg['titulo'], 'DejaVuSerif-Bold', 26, CONTENT_W)
    c.setFont('DejaVuSerif-Bold', tsize)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, cfg['titulo'])
    y -= 15
    c.setFont('DejaVuSans', 9)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y, cfg['autor'])
    y -= 20

    y = _fact_strip(c, y, cfg['datos'])

    # El mapa solo se dibuja si el numero de compases esta VERIFICADO. En
    # ediciones donde la deteccion de barras no es fiable se omite antes que
    # imprimir un total inventado.
    if cfg.get('secciones') and cfg.get('total_compases'):
        y = _section_title(c, MARGIN, y, 'Mapa de la pieza')
        y = _map_bar(c, y, cfg['secciones'], cfg['total_compases'])
        y -= 4

    col_w = (CONTENT_W - 22) / 2
    right_x = MARGIN + col_w + 22

    # --- el bloque central cambia segun el nivel ---
    # iniciacion: teclados que muestran como se abren las manos.
    # avanzado: tarjetas de armonia (que acorde arpegia la izquierda y por que),
    # porque a ese nivel el dibujo del teclado ya no aporta nada.
    if cfg.get('apertura'):
        ap = cfg['apertura']
        y = _section_title(c, MARGIN, y, ap['titulo'])
        y = keyboard_row(c, y, ap['pasos'], legend=ap['leyenda'])
        y -= 6
        c.setFont('DejaVuSans', 8.2)
        y = _wrap(c, ap['pie'], MARGIN, y, 'DejaVuSans', 8.2, CONTENT_W, 11.2, MUTED)
        y -= 18
    elif cfg.get('armonia'):
        ar = cfg['armonia']
        y = _section_title(c, MARGIN, y, ar['titulo'])
        y = tarjetas(c, y, ar['tarjetas'])
        y -= 16
        y = _wrap(c, ar['pie'], MARGIN, y, 'DejaVuSans', 8.2, CONTENT_W, 11.2, MUTED)
        y -= 18

    # --- dos columnas: lo especial / el dibujo de cada parte ---
    y_col = y
    yl = _section_title(c, MARGIN, y_col, 'Lo especial de esta partitura')
    yl = _bullets(c, MARGIN, yl, col_w, cfg['especial'])

    yr = _section_title(c, right_x, y_col, cfg.get('titulo_ritmos', 'Un compás de cada mano'))
    # El titulo anterior ("el dibujo de cada parte") no se entendia: nadie
    # sabia que estaba mirando. Ahora se dice literalmente lo que es.
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(MUTED)
    yr = _wrap(c, cfg.get('pie_ritmos') or
               'Un solo compás de ejemplo, para ver de un vistazo qué hace cada mano en esta pieza. '
               'MI = mano izquierda, MD = mano derecha.',
               right_x, yr - 1, 'DejaVuSans', 7.6, col_w, 9.6, MUTED)
    yr -= 4
    yr = _rhythm_stack(c, right_x, yr, col_w, cfg['ritmos'], cfg['time_sig'])

    # --- el pie de la ficha: reto/truco y luego sabías que + QR ------------
    #
    # Estas dos filas son las que se salían de la hoja. Se reparte el espacio
    # ANTES de dibujar nada, y en este orden: primero se aprietan los huecos
    # entre filas (que no se ven), luego encoge el recuadro del QR y por
    # último la letra del "¿Sabías que…?". Al revés, lo primero que se perdía
    # era lo único que hay que poder leer de lejos.
    y = min(yl, yr)
    sep1, sep2 = 18.0, 14.0
    h_qr = 78.0
    h_reto = max(_alto_note_box(cfg['reto'], col_w),
                 _alto_note_box(cfg['truco'], col_w))
    falta = SUELO_FICHA - (y - sep1 - h_reto - sep2 - h_qr)
    if falta > 0:
        margen1, margen2 = sep1 - 7.0, sep2 - 6.0
        recorte = min(falta, margen1 + margen2)
        sep1 -= recorte * margen1 / (margen1 + margen2)
        sep2 -= recorte * margen2 / (margen1 + margen2)
        falta -= recorte
    if falta > 0:
        h_qr = max(66.0, h_qr - falta)
    y -= sep1

    yb = _note_box(c, MARGIN, y, col_w, 'El reto', cfg['reto'], ACCENT)
    yb2 = _note_box(c, right_x, y, col_w, 'El truco', cfg['truco'], BLUE)
    y = min(yb, yb2) - sep2

    sab_w = CONTENT_W * 0.63
    qr_x = MARGIN + sab_w + 14
    qr_w = CONTENT_W - sab_w - 14
    ysab = _note_box(c, MARGIN, y, sab_w, '¿Sabías que…?', cfg['sabias'], NAVY_SOFT,
                     suelo=SUELO_FICHA)
    yqr = y
    if cfg.get('qr'):
        yqr = _qr_block(c, qr_x, y, qr_w, cfg['qr']['png'],
                        cfg['qr']['titulo'], cfg['qr']['texto'],
                        h=max(h_qr, y - ysab))
    y = min(ysab, yqr)

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    # devuelve la y final como las demas hojas: asi el auditor comprueba
    # tambien la ficha, que antes se quedaba fuera por ir en dos columnas.
    return y
