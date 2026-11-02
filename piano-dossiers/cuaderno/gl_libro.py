# -*- coding: utf-8 -*-
"""GLOSARIO MUSICAL · T-Clas (curso 2026/27).

   python3 gl_libro.py            -> entrega/GLOSARIO_MUSICAL_TCLAS.pdf
   BN=1 python3 gl_libro.py       -> version blanco y negro

   Parte del glosario hecho en Canva (22 paginas), corregido y ampliado. Cada entrada lleva su simbolo dibujado
   con el motor de notacion; el indice alfabetico del final da la pagina de cada termino."""
import io
import os
import sys
import unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import n1_base
from gl_base import *
from gl_base import _TREBLE_SHARP_POS, _TREBLE_FLAT_POS
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import nens_dib

n1_base.KICKER = 'GLOSARIO MUSICAL  ·  T-CLAS'
import n1_base as _nb
CREMA_T = HexColor('#EADFC0')
ASSETS = os.path.join(HERE, '..', 'assets')
TERMINOS = []          # (termino, seccion) para el indice


def entradas(d, lista):
    for e, blk in zip(lista, bloque_entradas(lista)):
        d.marca('t:' + e['term'])
        TERMINOS.append(e['term'])
        d.add(blk)


# ------------------------------------------------------------------ portada
def portada(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.rect(MARGIN * 0.62, MARGIN * 0.62, W - MARGIN * 1.24, H - MARGIN * 1.24, fill=0, stroke=1)
    c.setFillColor(NAVY)
    c.rect(18, H - 24, W - 36, 6, fill=1, stroke=0)
    try:
        c.drawImage(os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), W / 2 - 55, H - 190, 110, 110, mask='auto', preserveAspectRatio=True)
    except Exception:
        pass
    c.setFillColor(OCRE)
    c.setFont('DejaVuSans-Bold', 10)
    c.drawCentredString(W / 2, H - 214, 'CURSO 2026 / 27')
    c.setFillColor(NAVY)
    c.setFont('DejaVuSerif-Bold', 40)
    c.drawCentredString(W / 2, H - 275, 'Glosario')
    c.drawCentredString(W / 2, H - 322, 'musical')
    c.setStrokeColor(OCRE)
    c.setLineWidth(1.4)
    c.line(W / 2 - 40, H - 340, W / 2 + 40, H - 340)
    g = 9.0
    xs, ws = MARGIN + 20, W - 2 * MARGIN - 40
    ys = draw_staff(c, xs, H - 400, ws, g)
    draw_clef(c, xs + 4, ys[-1], g, 'treble')
    pits = ['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'C4']
    paso = (ws - 60) / 7.0
    for k, p in enumerate(pits):
        draw_note(c, xs + 56 + paso * (k + 0.5), ys[-1], ys[0], g, p, 'q', clef='treble')
    teclado(c, MARGIN, 190, W - 2 * MARGIN, 120, desde=('C', 4), n_blancas=15)
    c.setFillColor(NAVY)
    c.setFont('DejaVuSerif-Bold', 15)
    c.drawCentredString(W / 2, 148, 'Términos, signos y conceptos del piano')
    c.setFillColor(OCRE)
    c.setFont('DejaVuSans-Bold', 9.4)
    c.drawCentredString(W / 2, 130, 'EL CUADERNO DEL PIANISTA  ·  T-CLAS')
    c.showPage()


# ------------------------------------------------------------------ piano (diagramas)
def diag_piano():
    h = 262

    def f(c, x, y, w):
        cx = x + w / 2.0
        yb = y - h + 8
        nens_dib.piano(c, cx, yb, 1.0, color=False)

        def P(px, py):          # px/py en la imagen de prueba (1.54 px/pt) -> pt reales
            return cx + (px / 1.54 - 130), yb + ((260 - py / 1.54) - 20)
        etiquetas = [('Tapa', P(200, 45), 'izq'), ('Atril', P(200, 112), 'izq'), ('Teclado', P(200, 235), 'izq'),
                     ('Caja de resonancia', P(300, 150), 'der'), ('Pedales', P(200, 358), 'der'), ('Patas', P(330, 350), 'der')]
        # etiquetas colocadas en los lados con lineas de llamada
        izq = [('Tapa', P(130, 45)), ('Atril', P(130, 112)), ('Teclado', P(130, 235))]
        der = [('Caja de resonancia', P(330, 150)), ('Mueble', P(330, 300)), ('Pedales', P(215, 358)), ('Patas', P(345, 350))]
        c.setStrokeColor(OCRE)
        c.setLineWidth(0.8)
        for k, (t, (ax, ay)) in enumerate(izq):
            ly = y - 38 - k * 62 if k < 2 else y - 140
            lx = x + 70
            c.line(lx + 4, ly, ax, ay)
            c.setFont('DejaVuSans-Bold', 8.6)
            c.setFillColor(NAVY)
            c.drawRightString(lx, ly - 3, t)
        for k, (t, (ax, ay)) in enumerate(der):
            ly = y - 52 - k * 46
            lx = x + w - 78
            c.setStrokeColor(OCRE)
            c.line(lx - 4, ly, ax, ay)
            c.setFont('DejaVuSans-Bold', 8.6)
            c.setFillColor(NAVY)
            c.drawString(lx, ly - 3, t)
    return Blk(h, f)


def diag_mecanismo():
    h = 92

    def f(c, x, y, w):
        pasos = [('TECLA', 'se pulsa'), ('MECÁNICA', 'transmite el impulso'), ('MARTILLO', 'golpea la cuerda y rebota'), ('CUERDA', 'vibra libremente'),
                 ('TABLA ARMÓNICA', 'amplifica el sonido')]
        bw, gp = 84, 17.5
        x0 = x
        for k, (t, sub) in enumerate(pasos):
            xx = x0 + k * (bw + gp)
            c.setFillColor(PANEL)
            c.setStrokeColor(NAVY)
            c.setLineWidth(1.0)
            c.roundRect(xx, y - 62, bw, 50, 5, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.circle(xx + 10, y - 18, 7, fill=1, stroke=0)
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSans-Bold', 8)
            c.drawCentredString(xx + 10, y - 20.6, str(k + 1))
            c.setFillColor(NAVY)
            c.setFont('DejaVuSans-Bold', 7.2)
            c.drawCentredString(xx + bw / 2 + 6, y - 32, t)
            pinta_lineas(c, lineas(sub, bw - 10, 6.8), xx + 5, y - 38, 6.8, 8.6, MUTED, centrado_w=bw - 10)
            if k < 4:
                c.setStrokeColor(OCRE)
                c.setLineWidth(1.4)
                c.line(xx + bw + 2, y - 37, xx + bw + gp - 3, y - 37)
                p = c.beginPath()
                p.moveTo(xx + bw + gp - 3, y - 37)
                p.lineTo(xx + bw + gp - 8, y - 33.5)
                p.lineTo(xx + bw + gp - 8, y - 40.5)
                p.close()
                c.setFillColor(OCRE)
                c.drawPath(p, fill=1, stroke=0)
        c.setFont('DejaVuSans', 8)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 80, 'Al soltar la tecla, el apagador vuelve a posarse sobre la cuerda y la detiene.')
    return Blk(h, f)


def diag_dedos():
    def f(c, x, y, w):
        kw = 21
        teclado(c, x + 20, y - 60, w - 40, 54, desde=('G', 3), n_blancas=14, etiqueta_blancas=False)
        # etiqueta Do central
        k0 = x + 20
        ww = (w - 40) / 14.0
        # Do4 es la 5.ª blanca desde G3 (G A B C -> indice 3)
        xd = k0 + ww * 3.5
        c.setFillColor(OCRE)
        c.circle(xd, y - 54, 3.6, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(NAVY)
        c.drawCentredString(xd, y - 76, 'DO CENTRAL')
        c.setStrokeColor(OCRE)
        c.setLineWidth(1.0)
        c.line(k0, y - 86, xd - 10, y - 86)
        c.line(xd + 10, y - 86, k0 + 14 * ww, y - 86)
        c.setFont('DejaVuSans-Bold', 7.2)
        c.setFillColor(OCRE)
        c.drawString(k0 + 20, y - 97, '◄  territorio de la clave de fa (mano izquierda)')
        c.drawRightString(k0 + 14 * ww - 20, y - 97, 'territorio de la clave de sol (mano derecha)  ►')
        nens_dib.ma_real(c, x + 135, y - 273, 0.85, esq=True, dits=True, color=False)
        nens_dib.ma_real(c, x + 355, y - 273, 0.85, esq=False, dits=True, color=False)
    return Blk(310, f)


# ------------------------------------------------------------------ tablas especiales
def tabla_equivalencias():
    figs = ['w', 'h', 'q', 'e', 's', 'f', 'g']
    h = 8 * 26 + 24

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'TABLA DE EQUIVALENCIAS · cuántas figuras de cada columna caben en una figura de cada fila')
        x0 = x + 70
        cw = (w - 70) / 7.0
        yh = y - 18
        c.setFillColor(CREMA2)
        c.rect(x, yh - 26, w, 26, fill=1, stroke=0)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.0)
        c.line(x, yh - 26, x + w, yh - 26)
        c.line(x, yh, x + w, yh)
        for j, d_ in enumerate(figs):
            fig_celda_local(c, x0 + cw * (j + 0.5), yh - 13, d_)
        for i, a in enumerate(figs):
            yy = yh - 26 - (i + 1) * 26
            if i % 2 == 0:
                c.setFillColor(PANEL)
                c.rect(x, yy, w, 26, fill=1, stroke=0)
            c.setStrokeColor(RULE)
            c.setLineWidth(0.5)
            c.line(x, yy, x + w, yy)
            fig_celda_local(c, x + 35, yy + 13, a)
            for j, b in enumerate(figs):
                if j >= i:
                    n = 2 ** (j - i)
                    c.setFillColor(INK if j > i else MUTED)
                    c.setFont('DejaVuSans-Bold', 9)
                    c.drawCentredString(x0 + cw * (j + 0.5), yy + 9, str(n))
    return Blk(h, f)


def figura_blanca(c, cx, cy, gap, d_):
    figura(c, cx, cy, gap, d_, linea=False)


def fig_celda_local(c, cx, cy, d_, gap=3.7):
    nf = FIG[d_][0]
    alto = gap * (3.4 + 0.95 * max(0, nf - 2)) + gap * 0.5 if FIG[d_][2] else gap
    figura(c, cx - gap * 0.6, cy - alto / 2.0 + gap * 0.5, gap, d_, linea=False)


def tabla_figuras_silencios():
    """Figura, silencio, nombre y valor (tabla de referencia)."""
    ords = ['w', 'h', 'q', 'e', 's', 'f', 'g']
    filas = [[fig_cel(x), fig_cel(x, True), NOM_FIG[x], FIG[x][4]] for x in ords]
    return tabla([100, 100, 150, 141], filas, ['Figura', 'Silencio', 'Nombre', 'Valor (negra = 1)'], alto=32, size=9.2)


def fig_cel(d_, silencio_=False, gap=3.7):
    def f(c, cx, cy, w, hh):
        if silencio_:
            silencio(c, cx, cy, gap * 1.35, d_, linea=False)
        else:
            fig_celda_local(c, cx, cy, d_, gap)
    return f


def draw_armadura(c, x, bot, gap, tipo, n):
    sym = '♯' if tipo == '#' else '♭'
    pos = _TREBLE_SHARP_POS if tipo == '#' else _TREBLE_FLAT_POS
    dy = gap * 0.68 if tipo == '#' else gap * 0.6
    c.setFont('DejaVuSans', gap * 1.85)
    c.setFillColor(INK)
    step = max(gap * 1.0, stringWidth(sym, 'DejaVuSans', gap * 1.85) * 0.95)
    cx = x
    for i in range(n):
        c.drawString(cx, note_y(bot, gap, pos[i], 'treble') - dy, sym)
        cx += step


def tabla_armaduras():
    sost = [('Do M', 'La m'), ('Sol M', 'Mi m'), ('Re M', 'Si m'), ('La M', 'Fa♯ m'), ('Mi M', 'Do♯ m'), ('Si M', 'Sol♯ m'), ('Fa♯ M', 'Re♯ m'), ('Do♯ M', 'La♯ m')]
    bem = [('Do M', 'La m'), ('Fa M', 'Re m'), ('Si♭ M', 'Sol m'), ('Mi♭ M', 'Do m'), ('La♭ M', 'Fa m'), ('Re♭ M', 'Si♭ m'), ('Sol♭ M', 'Mi♭ m'), ('Do♭ M', 'La♭ m')]
    FIL = 78
    h = 2 * (16 + 2 * FIL) + 14

    def f(c, x, y, w):
        gap = 5.0
        cw = w / 4.0
        yy = y
        for tit, lista_, tipo in (('SOSTENIDOS · cada sostenido nuevo sube una quinta (orden: Fa – Do – Sol – Re – La – Mi – Si)', sost, '#'),
                                  ('BEMOLES · cada bemol nuevo baja una quinta (orden: Si – Mi – La – Re – Sol – Do – Fa)', bem, 'b')):
            c.setFont('DejaVuSans-Bold', 7.4)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, yy - 9, tit)
            yy -= 16
            for n_ in range(8):
                col, fila = n_ % 4, n_ // 4
                x0 = x + col * cw + 4
                ytop = yy - fila * FIL - 26
                ys = draw_staff(c, x0, ytop, cw - 12, gap)
                draw_clef(c, x0 + 1, ys[-1], gap, 'treble')
                draw_armadura(c, x0 + gap * 5.2, ys[-1], gap, tipo, n_)
                c.setFont('DejaVuSans-Bold', 6.8)
                c.setFillColor(OCRE)
                c.drawString(x0, ys[0] + 12, ('%d %s' % (n_, 'sostenido' + ('s' if n_ > 1 else '') if tipo == '#' else 'bemol' + ('es' if n_ > 1 else ''))) if n_ else 'sin alteraciones')
                c.setFont('DejaVuSans-Bold', 9)
                c.setFillColor(NAVY)
                c.drawCentredString(x0 + (cw - 12) / 2, ys[-1] - 17, lista_[n_][0])
                c.setFont('DejaVuSans', 8)
                c.setFillColor(MUTED)
                c.drawCentredString(x0 + (cw - 12) / 2, ys[-1] - 28, lista_[n_][1])
            yy -= 2 * FIL
    return Blk(h, f)


# ------------------------------------------------------------------ indice alfabetico
def sin_acentos(s):
    return ''.join(ch for ch in unicodedata.normalize('NFD', s) if unicodedata.category(ch) != 'Mn').lower()


def indice(d):
    terms = sorted(set(TERMINOS), key=sin_acentos)
    filas = []
    ini = None
    for t in terms:
        L = sin_acentos(t)[0].upper()
        if L != ini:
            ini = L
            filas.append(('L', L))
        filas.append(('T', t, d.prev.get('t:' + t, '·')))
    ncols = 3
    por_col = 50
    por_pag = ncols * por_col
    for p0 in range(0, len(filas), por_pag):
        chunk = filas[p0:p0 + por_pag]

        def f(c, x, y, w, chunk=chunk):
            cw = w / float(ncols)
            for k, fila in enumerate(chunk):
                col = k // por_col
                row = k % por_col
                xx = x + col * cw
                yy = y - row * 11.6
                if fila[0] == 'L':
                    c.setFont('DejaVuSerif-Bold', 10.5)
                    c.setFillColor(OCRE)
                    c.drawString(xx, yy - 10, fila[1])
                else:
                    c.setFont('DejaVuSans', 7.8)
                    c.setFillColor(INK)
                    t = fila[1]
                    while stringWidth(t, 'DejaVuSans', 7.8) > cw - 34:
                        t = t[:-2]
                    c.drawString(xx, yy - 9, t)
                    c.setFont('DejaVuSans-Bold', 7.8)
                    c.setFillColor(NAVY)
                    c.drawRightString(xx + cw - 14, yy - 9, str(fila[2]))
        d.add(Blk(por_col * 11.6 + 8, f))


# ------------------------------------------------------------------ contenido
def construir(d):
    # ============================================================ presentacion
    d.nuevo('Cómo usar el glosario')
    d.add(banda_mes('Presentación', 'Curso 2026/27', 'Cómo usar este glosario',
                    'Más de cien términos, signos y conceptos que aparecen en las partituras del curso, con su símbolo dibujado y su definición.'))
    d.add(caja('dato', 'Organización', [
        'Los términos se agrupan por temas, de lo más material a lo más abstracto: **el piano y la técnica**, **notas y pentagrama**, **duración, ritmo y compás**, '
        '**escalas, tonalidad, intervalos y acordes**, **expresión**, **signos y repeticiones** y **forma y conceptos generales**. Cada entrada lleva a la izquierda el **término**, '
        'en el centro su **símbolo** tal como se escribe en la partitura, y a la derecha la **definición**.',
        'Al final hay un **índice alfabético** con la página de cada término. Los valores de metrónomo son orientativos y varían según la fuente.']))
    d.add(h2('Contenido'))
    secs = [('I', 'El piano y la técnica', 'partes, pedales, posición de las manos y técnica de dedos', 'I'),
            ('II', 'Notas y pentagrama', 'pentagrama, claves, alturas, tonos y alteraciones', 'II'),
            ('III', 'Duración, ritmo y compás', 'figuras, silencios, puntillo, ligadura, compases', 'III'),
            ('IV', 'Escalas, tonalidad, intervalos y acordes', 'armaduras, escalas, intervalos, tríadas y cadencias', 'IV'),
            ('V', 'Expresión', 'articulación, matices, tempo y carácter', 'V'),
            ('VI', 'Signos y repeticiones', 'barras, repeticiones, D.C., D.S., coda, calderón, 8va y adornos', 'VI'),
            ('VII', 'Forma y conceptos generales', 'melodía, armonía, frase, forma y textura', 'VII'),
            ('', 'Índice alfabético', 'todos los términos con su página', 'Indice')]
    d.add(tabla([40, 180, 230, 41], [[a, '**%s**' % b, c_, str(d.prev.get('sec:' + k, '·'))] for a, b, c_, k in secs],
                ['Sec.', 'Tema', 'Incluye', 'Pág.'], alto=26, alin=['c', 'l', 'l', 'c'], size=8.6))

    # ============================================================ I. EL PIANO
    d.nuevo('I · El piano y la técnica')
    d.marca('sec:I')
    d.add(banda_mes('Sección I', 'El piano', 'El piano y la técnica', 'Cómo está hecho el instrumento, qué hacen los pedales y cómo se colocan las manos.'))
    d.marca('t:Partes del piano')
    TERMINOS.append('Partes del piano')
    d.add(h2('Partes del piano'), diag_piano())
    d.add(caja('dato', 'Cómo suena un piano', [
        'El piano es un instrumento de **cuerda percutida con teclado**: cada tecla acciona una mecánica que lanza un **martillo** de fieltro contra una o varias **cuerdas** tensadas sobre un bastidor; '
        'la vibración pasa a la **tabla armónica** (caja de resonancia), que la amplifica. Cuando se suelta la tecla, un **apagador** detiene la cuerda. '
        'Por eso se llama **pianoforte**: permite tocar suave (piano) y fuerte (forte) según la fuerza con que se pulsa la tecla.']),
        diag_mecanismo())
    d.nuevo()
    d.marca('t:Pedales')
    TERMINOS.append('Pedales')
    d.add(h2('Los pedales del piano'))

    def diag_ped():
        def f(c, x, y, w):
            cx = x + w / 2.0
            nens_dib.piano(c, cx, y - 214, 0.95, color=False)
            for px, tit in ((cx - 26, 'izq.'), (cx - 1, 'central'), (cx + 25, 'der.')):
                c.setFont('DejaVuSans-Bold', 7.4)
                c.setFillColor(OCRE)
                c.drawCentredString(px, y - 232, tit)
        return Blk(240, f)
    d.add(diag_ped())
    d.add(tabla([105, 150, 236], [
        ['**Pedal derecho**', 'Sustain · de resonancia · «fuerte»', 'Levanta todos los apagadores: las notas siguen sonando tras soltar las teclas y las cuerdas vibran por simpatía. Da resonancia y une frases; se cambia a cada cambio de armonía.'],
        ['**Pedal central**', 'Sostenuto', 'Mantiene solo las notas que estaban pulsadas al pisarlo, permitiendo tocar otras sin que se prolonguen. En muchos pianos verticales no es sostenuto, sino un pedal de **sordina** (para estudiar con poco volumen).'],
        ['**Pedal izquierdo**', 'Una corda · «suave»', 'Suaviza y vela el sonido. En el piano de cola desplaza la mecánica para que el martillo golpee menos cuerdas; en el vertical acerca los martillos a las cuerdas.'],
    ], ['Pedal', 'Nombre', 'Función'], alto=52, alin=['l', 'l', 'l'], size=8.4))
    d.marca('t:Ped. (signo de pedal)')
    TERMINOS.append('Ped. (signo de pedal)')
    entradas(d, [E('Signo de pedal', 'En la partitura **Ped.** indica pisar el pedal derecho y la línea con el gancho final (o el asterisco ✱) indica soltarlo. Pisar y soltar a tiempo con cada cambio de armonía evita que los sonidos se mezclen.', g_pedal(), 'Ped.')])
    TERMINOS.remove('Signo de pedal')

    d.marca('t:Tipos de piano')
    TERMINOS.append('Tipos de piano')
    d.add(tabla([120, 371], [
        ['**Piano vertical**', 'Cuerdas y tabla armónica en posición vertical, tras el mueble. Ocupa poco espacio; es el habitual en casas y escuelas.'],
        ['**Piano de cola**', 'Cuerdas en horizontal, con la tapa que se abre hacia arriba. Mecánica más rápida en la repetición de notas, más volumen y matices; típico de concierto.'],
        ['**Piano digital**', 'Reproduce el sonido electrónicamente (muestras de piano real) con un teclado de pesos graduados. Permite usar auriculares y no necesita afinación.'],
    ], ['Tipo', 'Características'], alto=30, alin=['l', 'l'], size=8.6))

    d.nuevo()
    d.marca('t:Posición de los dedos')
    TERMINOS.append('Posición de los dedos')
    d.add(h2('Posición de los dedos y territorio de las manos'))
    d.add(diag_dedos())
    d.add(par('Los dedos se numeran **del 1 (pulgar) al 5 (meñique) en las dos manos**. El **Do central** (Do4) divide el teclado en dos territorios habituales: a su izquierda, el de la **clave de fa** '
              '(mano izquierda, graves); a su derecha, el de la **clave de sol** (mano derecha, agudos). En la posición de cinco dedos sobre el Do, el pulgar derecho está en el Do central.', 9.0))
    d.marca('t:Técnica de dedos')
    TERMINOS.append('Técnica de dedos')
    d.add(h2('Técnica de dedos'))
    d.add(caja('dato', '1 · Posición básica de las manos', [
        '▸ Dedos curvados, como si sostuvieras una pelota pequeña; palmas ligeramente elevadas y muñecas relajadas.',
        '▸ Pulgar flexible: toca sobre su lateral, cerca de la punta, no con el pulpejo plano.',
        '▸ Evita tensar nudillos y brazo; el movimiento nace en los dedos con el apoyo de la muñeca y el peso del brazo.']),
        caja('dato', '2 · Independencia y fuerza de los dedos', [
            '▸ Cada dedo debe moverse sin arrastrar a los vecinos. El pulgar y el meñique necesitan más atención: son más cortos y débiles que los centrales.',
            '▸ Ejercicios sencillos: alternar dedos sobre una nota, escalas lentas y patrones de cinco dedos manteniendo la curva natural de la mano.']),
        caja('dato', '3 · Coordinación y agilidad', [
            '▸ La técnica busca movimientos ágiles, precisos y sin esfuerzo. El metrónomo ayuda a mantener un pulso constante y a coordinar las dos manos.',
            '▸ No «golpees» las teclas: toque ligero pero firme, con la yema del dedo.']),
        caja('dato', '4 · Uso del brazo y la muñeca', [
            '▸ Los dedos no trabajan solos: la muñeca acompaña, sobre todo en escalas largas y arpegios, y el brazo se desplaza con suavidad al recorrer varias octavas.',
            '▸ Así se reduce la fatiga y se previenen lesiones a largo plazo.']))
    d.add(caja('tip', '5 · Consejos de estudio', [
        '▸ Dedica 5–10 minutos diarios a ejercicios de dedos: es lo que marca la diferencia a largo plazo.',
        '▸ Manos y dedos relajados: la tensión produce una ejecución lenta e incómoda. Empieza despacio y aumenta la velocidad de forma progresiva.',
        '▸ Alterna patrones y combinaciones de dedos en las escalas para ganar independencia.',
        'Piensa en cada dedo como una voz independiente: no dejes que los fuertes hagan el trabajo de los débiles, y el sonido será más limpio y regular.']))

    # ============================================================ II. NOTAS Y PENTAGRAMA
    d.nuevo('II · Notas y pentagrama')
    d.marca('sec:II')
    d.add(banda_mes('Sección II', 'Altura', 'Notas y pentagrama', 'Cómo se nombran y se escriben los sonidos: pentagrama, claves, líneas adicionales, tonos y alteraciones.'))
    entradas(d, [
        E('Notas musicales', 'Los siete sonidos básicos. **Sistema latino:** Do – Re – Mi – Fa – Sol – La – Si. **Sistema anglosajón (cifrado):** C – D – E – F – G – A – B (La = A, Si = B). En notación alemana, B es el Si♭ y H el Si natural.',
          g_texto('C  D  E  F  G  A  B', 10.5, 'DejaVuSans-Bold')),
        E('Nota natural', 'La nota sin alterar: ni sostenido (♯) ni bemol (♭). Corresponde a las teclas blancas.'),
        E('Octava', 'Distancia entre una nota y la siguiente del mismo nombre (ocho notas contando ambas extremas). La frecuencia de la segunda es el doble. De Do a Do hay 7 teclas blancas y 5 negras. '
                    'Para distinguirlas se numeran: el Do central es el **Do4**.'),
        E('Registro', 'Zona del teclado a la que pertenece un sonido: **grave** (izquierda), **medio** y **agudo** (derecha). Un piano de 88 teclas va del La0 al Do8.'),
        E('Pentagrama', 'Cinco líneas paralelas y cuatro espacios, numerados de abajo arriba, sobre los que se escribe la música.', celda_pauta(ancho=88)),
        E('Pentagrama superior', 'En el piano se usa normalmente con la clave de sol y recoge las notas agudas (mano derecha).', g_clave('treble')),
        E('Pentagrama inferior', 'Normalmente con la clave de fa; recoge las notas graves (mano izquierda).', g_clave('bass')),
        E('Llave', 'Signo que une dos o más pentagramas que se leen a la vez (en el piano, sol y fa) formando el **sistema de piano**. Las notas situadas en la misma vertical suenan juntas.', g_llave()),
        E('Clave', 'Signo al principio del pentagrama que fija qué nota representa cada línea y espacio.'),
        E('Clave de sol', 'Su espiral rodea la **2.ª línea**, que es Sol (Sol4). Líneas de abajo arriba: Mi – Sol – Si – Re – Fa. Espacios: Fa – La – Do – Mi.', g_clave('treble')),
        E('Clave de fa', 'Sus dos puntos rodean la **4.ª línea**, que es Fa (Fa3). Líneas de abajo arriba: Sol – Si – Re – Fa – La. Espacios: La – Do – Mi – Sol.', g_clave('bass')),
        E('Clave de do', 'Fija el Do en la línea que rodea su centro: en la 3.ª línea (**clave de alto**, usada por la viola) o en la 4.ª (**clave de tenor**, usada por el violonchelo y el trombón en registros agudos). Poco usada en el piano.', g_clave('alto')),
        E('Línea adicional', 'Trazo corto, a la misma distancia que las líneas del pentagrama, que se añade por encima (superior) o por debajo (inferior) para escribir notas fuera de él. Cada nota lleva solo las que necesita.', g_linea_adicional()),
        E('Do central', 'La tecla Do más próxima al centro del teclado (Do4). Es la nota de enlace entre las dos claves: 1.ª línea adicional inferior en clave de sol y 1.ª superior en clave de fa.'),
        E('Tono', 'Distancia de **dos semitonos** entre dos notas (por ejemplo, de Do a Re). También se llama tono entero.', g_teclas(('C', 4), 3, {'C4': CREMA_T, 'D4': CREMA_T}, (0, 1, '1 tono', NAVY)), alto=52),
        E('Semitono', 'La distancia más pequeña entre dos teclas contiguas, blancas o negras (por ejemplo, Mi–Fa o Do–Do♯). Entre Mi–Fa y Si–Do hay semitono natural.', g_teclas(('E', 4), 3, {'E4': CREMA_T, 'F4': CREMA_T}, (0, 1, '½ tono', ROJO)), alto=52),
        E('Escala cromática', 'La que avanza **de semitono en semitono** utilizando todas las teclas, blancas y negras: doce sonidos por octava.'),
        E('Enarmonía', 'Dos notas que suenan igual y se escriben distinto: Do♯ = Re♭, Fa♯ = Sol♭. La escritura correcta depende de la tonalidad y de la dirección de la melodía.'),
    ])
    d.add(h2('Alteraciones'))
    entradas(d, [
        E('Alteración', 'Signo que se coloca **delante** de la nota y modifica su sonido. Una alteración accidental vale hasta el final del compás en el que aparece (y para esa octava); las de la armadura valen para toda la pieza.'),
        E('Sostenido (♯)', 'Sube la nota un semitono (medio tono).', g_alteracion('#')),
        E('Doble sostenido', 'Sube la nota un tono entero (dos semitonos).', g_alteracion('x')),
        E('Bemol (♭)', 'Baja la nota un semitono (medio tono).', g_alteracion('b')),
        E('Doble bemol', 'Baja la nota un tono entero (dos semitonos).', g_alteracion('bb')),
        E('Becuadro (♮)', 'Cancela el efecto de una alteración anterior (de la armadura o accidental) y devuelve la nota a su sonido natural.', g_alteracion('n')),
    ])

    # ============================================================ III. DURACION Y RITMO
    d.nuevo('III · Duración, ritmo y compás')
    d.marca('sec:III')
    d.add(banda_mes('Sección III', 'Tiempo', 'Duración, ritmo y compás', 'Cuánto dura cada sonido o silencio, cómo se agrupan en compases y cómo se organiza el tiempo.'))
    d.marca('t:Figuras y silencios')
    TERMINOS.append('Figuras y silencios')
    d.add(caja('dato', 'Figuras y silencios', [
        'Las **figuras** indican la duración de un sonido y los **silencios** la de una pausa. Se miden en **tiempos**, tomando como unidad la negra, aunque es una referencia relativa: '
        'lo que importa es la proporción entre ellas. Cada figura tiene su silencio equivalente.']),
        tabla_figuras_silencios(), tabla_equivalencias())
    entradas(d, [
        E('Silencio', 'Signo que indica una pausa con la misma duración que la figura de igual nombre. El de **redonda** cuelga de la 4.ª línea y el de **blanca** se apoya en la 3.ª; el de redonda sirve también para un compás entero de silencio, sea cual sea el compás.'),
        E('Puntillo', 'Punto a la derecha de una figura o un silencio: le añade **la mitad de su valor**. Blanca con puntillo = 2 + 1 = 3 tiempos; negra con puntillo = 1 + ½ = 1 ½.',
          lambda c, cx, cy, w, h: (figura(c, cx - 22, cy - 5, 3.9, 'h', linea=False, dot=True), figura(c, cx + 22, cy - 5, 3.9, 'q', linea=False, dot=True))),
        E('Doble puntillo', 'Dos puntos: el primero añade la mitad y el segundo la mitad del primero (un cuarto del valor). Negra con doble puntillo = 1 + ½ + ¼ = 1 ¾ tiempos.'),
        E('Ligadura de prolongación', 'Arco que une dos notas **del mismo sonido**: se tocan como una sola, sumando sus duraciones. Permite cruzar la barra de compás y escribir duraciones que no existen como figura.', g_ligadura(True)),
        E('Tresillo', 'Grupo de **tres notas de igual valor** que ocupan el tiempo de dos de ellas (tres corcheas en el tiempo de dos). Se marca con un **3**.', g_tresillo()),
        E('Pulso', 'El «latido» regular de la música, el que se marca con el pie o la mano. Los tiempos del compás son pulsos.'),
        E('Ritmo', 'Combinación de duraciones (sonidos y silencios) organizadas sobre el pulso.'),
        E('Subdivisión', 'Dividir cada pulso en partes más pequeñas e iguales para detallar el ritmo: en dos (corcheas), en cuatro (semicorcheas) o en tres (compases compuestos).'),
        E('Tempo', 'Velocidad de la pulsación. Se indica con un término italiano (Allegro…) o con una cifra de metrónomo: **♩ = 60** significa 60 negras por minuto (una por segundo).',
          g_texto('♩ = 60', 11.5, 'DejaVuSans-Bold')),
        E('Metrónomo', 'Aparato que marca un pulso regular a la velocidad que se elija (pulsos por minuto, bpm). Sirve para estudiar con pulso constante y subir la velocidad de forma gradual.',
          lambda c, cx, cy, w, h: nens_dib.metronom(c, cx, cy - 20, 0.42, color=False)),
        E('Síncopa', 'Sonido que **empieza en una parte débil** del compás (o del tiempo) y **se prolonga sobre la parte fuerte siguiente**, desplazando el acento.', g_sincopa()),
        E('Contratiempo', 'Sonido articulado en la parte débil del tiempo, **seguido de silencio en la parte fuerte**: la nota queda «a destiempo» respecto al pulso.', g_contratiempo()),
        E('Anacrusa', 'Una o varias notas que se tocan **antes del primer tiempo fuerte** (compás incompleto al inicio); el último compás de la pieza suele traer los tiempos que faltan.', g_anacrusa()),
        E('Polirritmo', 'Superposición de ritmos con distinta división del pulso: por ejemplo, dos contra tres (una mano toca dos notas por tiempo y la otra tres).'),
    ])
    d.add(h2('Compás'))
    entradas(d, [
        E('Compás', 'Unidad en que se organiza el tiempo musical: agrupa un número fijo de pulsos. La **cifra** del principio indica cuántos (número de arriba) y qué figura equivale a uno (número de abajo). El primer tiempo es el más fuerte.'),
        E('Compás simple', 'Cada pulso se divide en **2** partes iguales. Se siente como un latido regular y directo. Ejemplos: 2/4 (binario), 3/4 (ternario), 4/4 (cuaternario).'),
        E('Compás compuesto', 'Cada pulso se divide en **3** partes iguales (el pulso es una figura con puntillo). Ejemplos: 6/8, 9/8, 12/8.'),
        E('Compás de 4/4', 'Cuatro tiempos por compás; la negra vale un tiempo. Se escribe también con una **C** (compasillo). Acentos: fuerte – débil – semifuerte – débil.', g_ts(4, 4)),
        E('Compás de 2/4', 'Dos tiempos por compás; la negra vale un tiempo. Acentos: fuerte – débil. Típico de marchas.', g_ts(2, 4, ('q', 'q'))),
        E('Compás de 3/4', 'Tres tiempos por compás; la negra vale un tiempo. Acentos: fuerte – débil – débil. Es el compás del vals y del minueto.', g_ts(3, 4, ('q', 'q', 'q'))),
        E('Compás de 2/2', 'Dos tiempos por compás; la **blanca** es la unidad (vale un tiempo). Se escribe también con una C cortada (**¢**, compás de «alla breve»).', g_ts(2, 2, ('h', 'h'))),
        E('Compás de 3/8', 'Tres corcheas por compás; la corchea es la unidad. Se siente como **un solo pulso** (negra con puntillo).', g_ts(3, 8, ('e', 'e', 'e'))),
        E('Compás de 6/8', 'Seis corcheas por compás, agrupadas de tres en tres: **dos pulsos** de negra con puntillo.', g_ts(6, 8, ('e', 'e', 'e', 'e', 'e', 'e'))),
        E('Compás de 9/8', 'Nueve corcheas por compás: **tres pulsos** de negra con puntillo.', g_ts(9, 8, ('e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'))),
        E('Compás de 12/8', 'Doce corcheas por compás: **cuatro pulsos** de negra con puntillo.', g_ts(12, 8, ('e', 'e', 'e', 'e', 'e', 'e'))),
    ])

    # ============================================================ IV. ESCALAS, TONALIDAD, INTERVALOS, ACORDES
    d.nuevo('IV · Escalas, intervalos y acordes')
    d.marca('sec:IV')
    d.add(banda_mes('Sección IV', 'Armonía', 'Escalas, tonalidad y acordes', 'Cómo se organizan las notas: escalas, armaduras, intervalos, tríadas y cadencias.'))
    entradas(d, [
        E('Tonalidad', 'Sistema de relaciones entre las notas organizado alrededor de una **tónica** (la nota de reposo) y un **modo** (mayor o menor). Se nombra por la tónica: Do mayor, La menor…'),
        E('Armadura', 'Alteraciones escritas una sola vez tras la clave que valen para toda la pieza y definen su tonalidad. Cada tonalidad mayor comparte armadura con su relativa menor.'),
    ])
    d.add(tabla_armaduras())
    d.add(par('**M** = mayor · **m** = menor. Truco: la tónica mayor está **un semitono por encima del último sostenido**, y en bemoles es **el penúltimo bemol** (salvo con un solo bemol: Fa).', 8.8, NAVY_SOFT))
    entradas(d, [
        E('Tonalidades relativas', 'Dos tonalidades, una mayor y una menor, que **comparten armadura**: la menor empieza en la 6.ª nota de la mayor (Do mayor – La menor; Sol mayor – Mi menor).'),
        E('Escala', 'Sucesión ordenada de notas que sigue una estructura determinada de tonos y semitonos. Es la base de la música y define su sonoridad (alegre, triste, tensa…).'),
        E('Escala mayor', '**Tono – tono – semitono – tono – tono – tono – semitono.** Ejemplo en Do mayor: Do – Re – Mi – Fa – Sol – La – Si – Do.', g_teclas(('C', 4), 8, {'%s4' % L: CREMA_T for L in 'CDEFGAB'} | {'C5': CREMA_T}, None, ancho=100), alto=46),
        E('Escala menor natural', '**Tono – semitono – tono – tono – semitono – tono – tono.** Ejemplo en La menor: La – Si – Do – Re – Mi – Fa – Sol – La.'),
        E('Escala menor armónica', 'Como la natural pero con la **7.ª subida un semitono** (La – Si – Do – Re – Mi – Fa – Sol♯ – La), para tener sensible. Queda un intervalo de tono y medio entre el 6.º y el 7.º grado.'),
        E('Escala menor melódica', 'Al **subir** se elevan el 6.º y el 7.º grados (La – Si – Do – Re – Mi – Fa♯ – Sol♯ – La); al **bajar** se toca como la menor natural.'),
        E('Escala pentatónica', 'Escala de **cinco notas** por octava, sin semitonos. La pentatónica mayor de Do es Do – Re – Mi – Sol – La. Muy usada en el folclore, el blues y el pop.'),
        E('Grados de la escala', 'Lugar que ocupa cada nota (I a VII). Nombres: **I tónica · II supertónica · III mediante · IV subdominante · V dominante · VI superdominante · VII sensible** (la sensible está a un semitono de la tónica).'),
        E('Intervalo', 'Distancia entre dos notas. Se mide **contando los grados** que hay entre ellas, incluidos los dos extremos: de Do a Mi, tercera.'),
    ])
    d.marca('t:Tabla de intervalos')
    TERMINOS.append('Tabla de intervalos')
    d.add(tabla([170, 100, 221], [['2.ª menor', '1', 'Do – Re♭'], ['2.ª mayor', '2', 'Do – Re'], ['3.ª menor', '3', 'Do – Mi♭'], ['3.ª mayor', '4', 'Do – Mi'],
                                  ['4.ª justa', '5', 'Do – Fa'], ['4.ª aumentada (tritono)', '6', 'Do – Fa♯'], ['5.ª justa', '7', 'Do – Sol'], ['6.ª menor', '8', 'Do – La♭'],
                                  ['6.ª mayor', '9', 'Do – La'], ['7.ª menor', '10', 'Do – Si♭'], ['7.ª mayor', '11', 'Do – Si'], ['8.ª justa', '12', 'Do – Do agudo']],
                ['Intervalo', 'Semitonos', 'Ejemplo desde Do'], alto=17, size=8.2, alin=['l', 'c', 'l']))
    d.add(par('**Clasificación básica:** son **justos** la 4.ª, la 5.ª y la 8.ª; son **mayores o menores** la 2.ª, 3.ª, 6.ª y 7.ª. Si se amplía un semitono un intervalo justo o mayor, es **aumentado**; si se reduce un semitono un justo o menor, **disminuido**.', 8.8, NAVY_SOFT))
    entradas(d, [
        E('Acorde', 'Combinación de **tres o más notas** que suenan a la vez. El más común es el acorde de tres notas, la **tríada**.', g_acorde(['C4', 'E4', 'G4'])),
        E('Tríada mayor', '1.ª (fundamental) + 3.ª mayor + 5.ª justa. Sonoridad alegre y brillante. Ejemplo: Do mayor = Do – Mi – Sol (4 + 3 semitonos).', g_acorde(['C4', 'E4', 'G4'])),
        E('Tríada menor', '1.ª + 3.ª menor + 5.ª justa. Sonoridad triste o suave. Ejemplo: La menor = La – Do – Mi (3 + 4 semitonos).', g_acorde(['A3', 'C4', 'E4'])),
        E('Tríada aumentada y disminuida', '**Aumentada:** dos terceras mayores (Do – Mi – Sol♯), sonido tenso y abierto. **Disminuida:** dos terceras menores (Si – Re – Fa), sonido inestable.'),
        E('Inversiones', 'Un acorde no siempre se toca empezando por la fundamental. **Posición fundamental:** fundamental en el bajo (Do – Mi – Sol). **1.ª inversión:** la tercera en el bajo (Mi – Sol – Do). **2.ª inversión:** la quinta en el bajo (Sol – Do – Mi). Permiten encadenar acordes con menos saltos.'),
        E('Cifrado de acordes', 'Sistema de letras: C Do · D Re · E Mi · F Fa · G Sol · A La · B Si. La letra sola es **mayor** (C); una **m** indica menor (Am); un **7** añade la séptima menor (G7 = Sol – Si – Re – Fa).'),
        E('Séptima de dominante', 'Tríada del V grado con una séptima menor añadida: en Do mayor, G7 = Sol – Si – Re – Fa. Crea tensión que pide resolver en la tónica.'),
        E('Cadencia', 'Fórmula de acordes que da sensación de pausa o de final. La más básica es **I – IV – V – I** (en Do mayor: C – F – G – C); la que termina V → I se llama **perfecta**.'),
        E('Funciones armónicas', '**Tónica** (I): reposo. **Subdominante** (IV): movimiento que se aleja de la tónica. **Dominante** (V): tensión que pide volver a la tónica.'),
        E('Arpegio', 'Acorde cuyas notas se tocan **una tras otra**, no a la vez.', g_arpegio()),
        E('Unísono', 'Dos o más sonidos de **la misma altura** tocados a la vez (o varias voces o instrumentos tocando la misma melodía).'),
        E('Octavas (intervalo)', 'Intervalo entre dos notas del mismo nombre; la más aguda tiene el doble de frecuencia que la grave.'),
    ])

    # ============================================================ V. EXPRESION
    d.nuevo('V · Expresión')
    d.marca('sec:V')
    d.add(banda_mes('Sección V', 'Interpretación', 'Expresión', 'Cómo se tocan las notas: articulación, intensidad, velocidad y carácter.'))
    d.add(h2('Articulación y acentos'))
    entradas(d, [
        E('Picado (staccato)', 'Punto sobre o bajo la cabeza: la nota se toca **corta y separada**, con menos duración de la escrita.', g_artic('staccato')),
        E('Legato', 'Suave y conectado: se pasa de una nota a otra **sin cortar el sonido**. Se indica con una ligadura de expresión.', g_ligadura(False)),
        E('Acento', 'Signo > : se ataca la nota con **más énfasis** que las vecinas.', g_artic('acento')),
        E('Marcato', 'Signo ^ : más énfasis que el acento, con un ataque marcado y algo más corto.', g_artic('marcato')),
        E('Tenuto', 'Raya sobre o bajo la nota: se mantiene **todo su valor**, algo más sostenida y con ligero peso.', g_artic('tenuto')),
        E('Ligado (ligadura de expresión)', 'Arco sobre un grupo de notas **distintas**: forman una frase y se tocan ligadas (legato). No suma duraciones, a diferencia de la ligadura de prolongación.', g_ligadura(False)),
    ])
    d.add(h2('Matices (dinámica)'))
    entradas(d, [
        E('Pianissimo · pp', 'Muy suave.', g_dim('pp')), E('Piano · p', 'Suave.', g_dim('p')),
        E('Mezzo piano · mp', 'Medio suave.', g_dim('mp')), E('Mezzo forte · mf', 'Medio fuerte.', g_dim('mf')),
        E('Forte · f', 'Fuerte.', g_dim('f')), E('Fortissimo · ff', 'Muy fuerte.', g_dim('ff')),
        E('Pianississimo y fortississimo', '**ppp** (el más suave posible) y **fff** (el más fuerte posible): los extremos de la escala dinámica.', g_dim('ppp / fff', 11)),
        E('Sforzando · sf, sfz', 'Acento súbito y fuerte sobre una sola nota o acorde.', g_dim('sfz')),
        E('Fortepiano · fp', 'Fuerte al atacar y suave de inmediato.', g_dim('fp')),
        E('Crescendo · cresc.', 'Gradualmente más fuerte.', g_regulador(False, 'cresc.')),
        E('Diminuendo · dim. (decrescendo)', 'Gradualmente más suave: disminuye la intensidad.', g_regulador(True, 'dim.')),
    ])
    d.add(h2('Tempo y movimiento'))
    d.marca('t:Tabla de tempos')
    TERMINOS.append('Tabla de tempos')
    d.add(tabla([100, 190, 201], [
        ['Largo', 'Muy despacio, lento', '♩ ≈ 40–60'], ['Larghetto', 'Un poco más rápido que Largo', '♩ ≈ 60–66'], ['Adagio', 'Más rápido que Largo, más lento que Andante', '♩ ≈ 66–76'],
        ['Andante', 'Como el paso del caminante', '♩ ≈ 76–108'], ['Andantino', 'Un poco más rápido que Andante (su sentido ha variado con las épocas)', 'según la fuente'],
        ['Moderato', 'Moderado', '♩ ≈ 108–120'], ['Allegretto', 'Un poco más despacio que Allegro', '♩ ≈ 112–120'], ['Allegro', 'Rápido y vivaz', '♩ ≈ 120–156'],
        ['Vivace', 'Vivo, muy animado', '♩ ≈ 156–176'], ['Presto', 'Muy rápido, más que Allegro', '♩ ≈ 168–200'], ['Prestissimo', 'Lo más rápido posible, más que Presto', '♩ ≈ 200 o más'],
    ], ['Término', 'Significado', 'Metrónomo (orientativo)'], alto=19, size=8.4, alin=['l', 'l', 'c']))
    entradas(d, [
        E('Accelerando · accel.', 'Gradualmente más rápido.'), E('Poco accelerando · poco accel.', 'Un poco más rápido.'),
        E('Ritardando · rit.', 'Gradualmente más despacio.'), E('Rallentando · rall.', 'Casi sinónimo de ritardando: se va aflojando el movimiento.'),
        E('A tempo', 'Vuelve al tiempo original de la pieza.'), E('Rubato', 'Libertad de pulso: se toma tiempo de unas notas y se devuelve en otras, sin perder la medida general.'),
    ])
    d.add(h2('Carácter'))
    entradas(d, [
        E('Maestoso', 'Majestuoso.'), E('Solemne', 'Serio y grave, casi sagrado.'), E('Vigoroso', 'Enérgico y fuerte.'),
        E('Dolce', 'Dulce, suave.'), E('Cantabile', 'En estilo cantado: la melodía debe «cantar».'), E('Espressivo', 'Con expresión.'),
        E('Grazioso', 'Con gracia, ligero.'), E('Scherzando', 'Juguetón, bromista.'), E('Agitato', 'Agitado, inquieto.'), E('Con brio', 'Con ímpetu y vivacidad.'),
        E('Sostenuto', 'Sosteniendo los sonidos; a veces también algo más lento.'), E('Tranquillo', 'Tranquilo, sin prisa.'),
    ])

    # ============================================================ VI. SIGNOS Y REPETICIONES
    d.nuevo('VI · Signos y repeticiones')
    d.marca('sec:VI')
    d.add(banda_mes('Sección VI', 'Notación', 'Signos y repeticiones', 'Barras, repeticiones, saltos de lectura y otros signos de la partitura.'))
    entradas(d, [
        E('Línea divisoria', 'Línea fina vertical que separa un compás del siguiente.', g_barra('divisoria')),
        E('Doble barra', 'Dos líneas finas: marca el **final de una sección** o un cambio de armadura o de compás.', g_barra('doble')),
        E('Doble barra final', 'Una línea fina y otra gruesa: indica el **final de la pieza**.', g_barra('final')),
        E('Barra de repetición', 'Con dos puntos a un lado: toda la música anterior se repite, desde el principio o desde la barra de repetición de apertura.', g_barra('rep_cierra')),
        E('Barra de apertura', 'Dos puntos a la derecha de la doble barra: marca el punto de inicio de una repetición.', g_barra('rep_abre')),
        E('Barras de repetición', 'Si hay barra de apertura y de cierre, se repite **solo lo que queda entre las dos**.', g_barra('rep_ambas')),
        E('Casillas de repetición', 'Indican los distintos finales: la **1.ª casilla** se toca la primera vez; al repetir se salta y se toca la **2.ª**.', g_barra('casillas')),
    ])
    d.add(h2('Saltos de lectura'))
    entradas(d, [
        E('Da capo · D.C.', 'Repetir desde el principio.', g_texto('D.C.')),
        E('Fine', 'El final de la música (donde se termina tras un D.C. o D.S. al Fine).', g_texto('Fine')),
        E('Da capo al fine · D.C. al fine', 'Repetir desde el principio hasta la indicación **Fine**.', g_texto('D.C. al Fine')),
        E('Segno', 'Marca en forma de S cruzada a la que se vuelve con un D.S.', g_segno()),
        E('Dal segno · D.S.', 'Repetir desde el **segno**.', g_texto('D.S.')),
        E('Dal segno al fine · D.S. al fine', 'Repetir desde el segno hasta **Fine**.', g_texto('D.S. al Fine')),
        E('Coda', 'Sección final de una pieza; se indica con el signo de coda (⊕).', g_coda()),
        E('Al coda (to Coda)', 'Indica, al repetir, el punto en el que hay que saltar a la coda y seguir hasta el final.', g_texto('al Coda')),
        E('Da capo al coda · D.C. al coda', 'Repetir desde el principio hasta el signo de coda; entonces saltar a la coda y seguir hasta el final.', g_texto('D.C. al Coda')),
        E('Dal segno al coda · D.S. al coda', 'Repetir desde el segno hasta el signo de coda; entonces saltar a la coda y seguir hasta el final.', g_texto('D.S. al Coda')),
    ])
    d.add(h2('Otros signos'))
    entradas(d, [
        E('Calderón (corona)', 'Prolongación **indeterminada** de la duración de una nota o silencio, a criterio del intérprete.', g_artic('calderon')),
        E('Ottava alta · 8va', 'Las notas bajo la línea de puntos se tocan **una octava más aguda** de lo escrito.', g_octava(True)),
        E('Ottava bassa · 8vb', 'Las notas sobre la línea de puntos se tocan **una octava más grave** de lo escrito.', g_octava(False)),
        E('Notita de adorno', 'Nota pequeña (con raya si es breve) que se toca muy rápido **justo antes** de la nota a la que adorna y no cuenta en el compás.', g_adorno()),
        E('Trino · tr', 'Alternancia rápida entre una nota y la inmediata superior durante toda su duración.', g_texto('tr~~~~', 12)),
        E('Mordente', 'Adorno de tres notas: la principal, su vecina (superior o inferior) y otra vez la principal, muy rápidas.'),
        E('Glissando', 'Deslizamiento rápido sobre las teclas entre dos notas, pasando por todas las intermedias.'),
        E('Arpegiado (acorde roto)', 'Línea ondulada junto a un acorde: sus notas se tocan de abajo arriba, muy seguidas, y no todas a la vez.'),
    ])

    # ============================================================ VII. FORMA Y CONCEPTOS
    d.nuevo('VII · Forma y conceptos generales')
    d.marca('sec:VII')
    d.add(banda_mes('Sección VII', 'Conceptos', 'Forma y conceptos generales', 'Las ideas con las que se describe cualquier música: sus elementos, su forma y su textura.'))
    entradas(d, [
        E('Cualidades del sonido', '**Altura** (grave–agudo, depende de la frecuencia), **duración**, **intensidad** (fuerte–suave, depende de la amplitud) y **timbre** (lo que distingue un instrumento de otro).'),
        E('Elementos de la música', '**Melodía** (sucesión de sonidos de distinta altura con ritmo), **armonía** (sonidos simultáneos y su encadenamiento) y **ritmo** (organización de las duraciones).'),
        E('Melodía', 'Sucesión de sonidos de distinta altura que forma una idea musical con sentido y se percibe como una línea. Puede avanzar por grados conjuntos (pasos) o por saltos.'),
        E('Armonía', 'Combinación de sonidos simultáneos (acordes) y el modo en que se encadenan; da soporte y color a la melodía.'),
        E('Acompañamiento', 'Música que sostiene la melodía: acordes, arpegios o un patrón rítmico, normalmente en la mano izquierda.'),
        E('Motivo', 'La célula musical más pequeña con identidad propia (unas pocas notas); se repite y se transforma a lo largo de una obra.'),
        E('Frase', 'Unidad musical con sentido, normalmente de cuatro u ocho compases, que termina en una cadencia. Se divide en **semifrases** (pregunta y respuesta).'),
        E('Tema', 'Melodía principal de una obra o sección, sobre la que se construye el resto.'),
        E('Variación', 'Repetición de un tema con cambios (ritmo, armonía, adornos, registro) que se mantiene reconocible.'),
        E('Forma binaria y ternaria', '**Binaria (A–B):** dos secciones contrastantes. **Ternaria (A–B–A):** presentación, contraste y regreso del material inicial.'),
        E('Textura', '**Monodía:** una sola línea melódica. **Homofonía:** melodía con acompañamiento. **Polifonía:** varias líneas melódicas independientes a la vez (por ejemplo, un canon).'),
        E('Canon', 'Imitación: una melodía es repetida por otra voz **después de un cierto número de compases**, superponiéndose a la primera (por ejemplo, Frère Jacques).'),
        E('Estudio', 'Pieza breve pensada para trabajar un aspecto técnico concreto (escala, arpegio, independencia de manos…).'),
        E('Sonatina', 'Sonata breve y de menor dificultad técnica, muy frecuente en el repertorio de iniciación al piano.'),
        E('Minueto', 'Danza de origen francés en compás de 3/4, de carácter elegante y moderado.'),
        E('Vals', 'Danza en compás de 3/4 con acento marcado en el primer tiempo.'),
    ])

    # ============================================================ INDICE
    d.nuevo('Índice alfabético')
    d.marca('sec:Indice')
    d.add(banda_mes('Índice', 'Consulta', 'Índice alfabético', 'Todos los términos del glosario con la página en que se explican.'))
    indice(d)


def montar(c, prev, portada_=True):
    del TERMINOS[:]
    if portada_:
        portada(c)
    d = Doc(c, 2 if portada_ else 1, prev)
    construir(d)
    fin = d.fin()
    return d, fin


def main():
    out = os.path.join(HERE, 'entrega')
    os.makedirs(out, exist_ok=True)
    bn = os.environ.get('BN') == '1'
    buf = io.BytesIO()
    c1 = canvas.Canvas(buf, pagesize=(W, H))
    d1, _ = montar(c1, {})
    c1.save()
    dst = os.path.join(out, 'GLOSARIO_MUSICAL_TCLAS%s.pdf' % ('_BN' if bn else ''))
    c2 = canvas.Canvas(dst, pagesize=(W, H))
    c2.setTitle('Glosario musical · T-Clas')
    c2.setAuthor('T-Clas')
    d2, fin = montar(c2, d1.marcas)
    c2.save()
    print('paginas:', fin - 1, '->', dst)


if __name__ == '__main__':
    main()
