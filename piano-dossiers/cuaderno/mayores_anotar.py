# -*- coding: utf-8 -*-
"""Anota ENCIMA de la partitura original los bloques de aprendizaje.

   La partitura (PDF de Drive, con copyright) no se toca: se le superpone una
   capa transparente con bandas de color por bloque, una etiqueta por bloque y
   anillos sobre lo importante. El resultado va a `entrega/` (no se versiona).
"""
import io
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from pypdf import PdfReader, PdfWriter
from portada import W, H                                       # noqa: F401  (registra fuentes)
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(__file__)
SRC = os.path.join(HERE, '..', 'students', 'demo', 'source', 'Heart-Asks-Pleasure-First.pdf')
PAGE_H = 841.89
OFFSET = 0

# (alto_arriba, alto_abajo) de cada sistema en pt DESDE ARRIBA, medidos sobre el PDF a 144 dpi
SIST = {
    1: [(215.5, 293.5), (370.0, 450.5), (509.0, 590.0), (652.5, 736.5)],
    2: [(85.5, 163.5), (219.5, 303.0), (375.5, 453.0), (528.5, 598.5), (672.0, 749.5)],
    3: [(85.5, 163.5), (224.0, 305.0), (390.0, 467.5), (536.0, 614.0), (676.0, 754.0)],
}
# compases por sistema, en orden de lectura
COMPASES = {1: [(1, 2), (3, 4), (5, 6), (7, 8)],
            2: [(9, 10), (11, 12), (13, 14), (15, 16), (17, 18)],
            3: [(19, 20), (21, 22), (23, 24), (25, 26), (27, 28)]}

BLOQUES = [
    (1, 1, 2, 'Entrada', HexColor('#3E6E8F')),
    (2, 3, 4, 'El dibujo de Più mosso', HexColor('#8C6A3F')),
    (3, 5, 6, 'Cambia el compás', HexColor('#A0453A')),
    (4, 7, 12, 'La cadencia y la vuelta', HexColor('#4F7A5A')),
    (5, 13, 14, 'Vuelve la entrada', HexColor('#3E6E8F')),
    (6, 15, 22, 'Repetición y octavas', HexColor('#6B5B95')),
    (7, 23, 28, 'Casillas y final', HexColor('#8C6A3F')),
]


def bloque_de(compas):
    for b in BLOQUES:
        if b[1] <= compas <= b[2]:
            return b


def marca(c, x, y, w, h, col, n, tipo='caja'):
    """Marca fina alrededor de lo importante; (x, y) es el centro, y desde arriba.
       Solo contorno: no tapa nada. El numero va en la esquina, fuera de la musica."""
    c.setStrokeColor(Color(col.red, col.green, col.blue, alpha=0.9))
    c.setLineWidth(1.0)
    x0, y0 = x - w / 2, PAGE_H - y - h / 2
    if tipo == 'ovalo':
        c.ellipse(x0, y0, x0 + w, y0 + h, stroke=1, fill=0)
    else:
        c.roundRect(x0, y0, w, h, 3, stroke=1, fill=0)
    cx, cy = x0 + w, y0 + h
    c.setFillColor(col)
    c.circle(cx, cy, 4.4, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont('DejaVuSans-Bold', 6)
    c.drawCentredString(cx, cy - 2.1, str(n))


def margen(c, bloque, top, bot, primero):
    """Parentesis fino en el margen izquierdo + ficha con el numero del bloque."""
    num, c1, c2, nombre, col = bloque
    t, b = PAGE_H - top, PAGE_H - bot
    c.setStrokeColor(col)
    c.setLineWidth(1.3)
    c.line(28, b, 28, t)
    c.line(28, t, 32, t)
    c.line(28, b, 32, b)
    c.setFillColor(col)
    c.circle(19.5, t - 9, 7, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont('DejaVuSerif-Bold', 9)
    c.drawCentredString(19.5, t - 12.1, str(num))
    c.saveState()
    c.setFillColor(col)
    c.setFont('DejaVuSans-Bold', 6.2)
    etq = 'cc. %d-%d' % (c1, c2) if primero else 'sigue'
    c.translate(22.5, t - 20)
    c.rotate(-90)
    c.drawString(0, 0, etq)
    c.restoreState()


LEAD = {'IZQ': (HexColor('#8C6A3F'), 'MANO IZQUIERDA'), 'DER': (HexColor('#3E6E8F'), 'MANO DERECHA'),
        'AMB': (HexColor('#1A2332'), 'LAS DOS'), 'OJO': (HexColor('#A0453A'), 'OJO')}


def _lineas(txt, w, font, size):
    out, cur = [], ''
    for pal in txt.split():
        t = (cur + ' ' + pal).strip()
        if stringWidth(t, font, size) > w and cur:
            out.append(cur)
            cur = pal
        else:
            cur = t
    if cur:
        out.append(cur)
    return out


def burbuja(c, x, y, w, tipo, txt, cola='arriba', cx=None):
    """Burbuja de texto: (x, y) esquina superior izquierda, y desde arriba.
       La cola sale por arriba o por abajo, en la x `cx`."""
    col, lead = LEAD[tipo]
    size = 6.9
    lin = _lineas(txt, w - 14, 'DejaVuSans', size)
    h = 12 + 9.2 * (len(lin) + 1)
    x0, y0 = x, PAGE_H - y - h
    cx = cx if cx is not None else x + 16
    c.setFillColor(HexColor('#FFFFFF'))
    c.setStrokeColor(col)
    c.setLineWidth(0.9)
    c.roundRect(x0, y0, w, h, 5, fill=1, stroke=1)
    p = c.beginPath()
    if cola == 'arriba':
        p.moveTo(cx - 4, y0 + h)
        p.lineTo(cx, y0 + h + 6)
        p.lineTo(cx + 4, y0 + h)
    else:
        p.moveTo(cx - 4, y0)
        p.lineTo(cx, y0 - 6)
        p.lineTo(cx + 4, y0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.drawPath(p, fill=1, stroke=0)
    c.setStrokeColor(col)
    c.line(cx - 4, y0 + h if cola == 'arriba' else y0, cx, y0 + h + 6 if cola == 'arriba' else y0 - 6)
    c.line(cx + 4, y0 + h if cola == 'arriba' else y0, cx, y0 + h + 6 if cola == 'arriba' else y0 - 6)
    # tapa el trazo de la burbuja bajo la cola
    c.setStrokeColor(HexColor('#FFFFFF'))
    c.setLineWidth(1.4)
    yb = y0 + h if cola == 'arriba' else y0
    c.line(cx - 3.2, yb, cx + 3.2, yb)
    c.setFont('DejaVuSans-Bold', 6.3)
    c.setFillColor(col)
    c.drawString(x0 + 7, PAGE_H - y - 10.5, lead)
    c.setFont('DejaVuSans', size)
    c.setFillColor(HexColor('#1A2332'))
    yy = PAGE_H - y - 10.5 - 9.4
    for l in lin:
        c.drawString(x0 + 7, yy, l)
        yy -= 9.2


# --- Recolocacion: la partitura se corta por sistemas (en los huecos en blanco medidos entre
# ellos) y se vuelve a montar con aire para las burbujas. Todo vectorial, sin reescalar.
# (pagina_origen, y_corte_arriba, y_corte_abajo, indice de sistema en SIST o None)
TIRAS = [
    (1, 44, 148, None),            # titulo y autor
    (1, 148, 322, (1, 0)), (1, 322, 482, (1, 1)), (1, 482, 620, (1, 2)), (1, 620, 765, (1, 3)),
    (2, 60, 193.5, (2, 0)), (2, 193.5, 340, (2, 1)), (2, 340, 481, (2, 2)),
    (2, 481, 638, (2, 3)), (2, 638, 785, (2, 4)),
    (3, 60, 199.5, (3, 0)), (3, 199.5, 348, (3, 1)), (3, 348, 498, (3, 2)),
    (3, 498, 639, (3, 3)), (3, 639, 775, (3, 4)),
]

# burbujas por sistema: (pagina, indice) -> [(sitio, ancho, tipo, texto, x_cola)]
# sitio: 'arriba' (la cola baja hacia la musica) o 'abajo' (la cola sube).
BURB = {
    (1, 0): [('arriba', 300, 'DER', 'Al principio hace dos cosas: arriba, notas largas que '
                                    'cantan; debajo, semicorcheas. Estudia cada voz sola.', 250),
             ('abajo', 238, 'IZQ', 'Empieza por aquí, tú sola: cada golpe son 6 notas. '
                                   'Despacio y parejo.', 150),
             ('abajo', 238, 'AMB', 'Cuenta 4 golpes por compás: 1-2-3, 4-5-6, 7-8-9, '
                                   '10-11-12.', 430)],
    (1, 1): [('arriba', 300, 'DER', 'Los acentos (>) marcan la melodía: tócalos un poco más '
                                    'fuertes que lo de debajo.', 190)],
    (1, 2): [('arriba', 330, 'OJO', 'El compás cambia: 9/8 son 3 golpes, 6/8 son 2. Cuenta '
                                    '1-2-3 en cada golpe y no frenes.', 350)],
    (1, 3): [('arriba', 300, 'AMB', 'Cierre de la frase: la tensión de Mi se resuelve en La '
                                    'menor. Afloja la mano al llegar.', 150),
             ('abajo', 270, 'IZQ', 'Las notas ligadas del bajo se mantienen: no se vuelven a '
                                   'tocar.', 130)],
    (2, 0): [('arriba', 300, 'AMB', 'Mismo camino que los cc. 3-8: ya lo conoces. Fíjate en '
                                    'los cambios a 9/8 y a 6/8.', 344)],
    (2, 1): [('arriba', 300, 'OJO', 'c. 11: 6/8 y luego 12/8. Cuenta 1-2-3 / 1-2-3 y después '
                                    'cuatro grupos de tres.', 75)],
    (2, 2): [('arriba', 300, 'AMB', 'cc. 13-14: otra vez la entrada. Tócala de memoria, es el '
                                    'bloque 1.', 120)],
    (2, 3): [('arriba', 330, 'AMB', 'Empieza la repetición. Acordes nuevos: C = Do, G = Sol, '
                                    'Am = La menor, E = Mi.', 60),
             ('abajo', 300, 'IZQ', '8va: toca la izquierda una octava más grave mientras dure '
                                   'la línea de puntos.', 230)],
    (3, 2): [('arriba', 330, 'OJO', 'La primera vez, al llegar a la casilla 1 vuelves al signo '
                                    'de repetición del c. 15.', 80)],
    (3, 3): [('arriba', 330, 'OJO', 'La segunda vez NO repitas: salta a la casilla 2 '
                                    '(cc. 25-26) y sigue hasta el final.', 80)],
    (3, 4): [('arriba', 300, 'AMB', 'Los dos últimos compases: baja el volumen y acaba con '
                                    'calma sobre la doble barra.', 540)],
}

# marcas: (pagina_origen, x, y, ancho, alto, bloque, numero, tipo)  [y en la pagina origen]
MARCAS = [
    (1, 76, 517, 17, 26, 3, 1, 'caja'), (1, 351, 516, 17, 26, 3, 2, 'caja'),
    (1, 545, 516, 19, 26, 3, 3, 'caja'),
    (2, 344, 93, 17, 26, 4, 1, 'caja'), (2, 72, 227, 17, 26, 4, 2, 'caja'),
    (2, 252, 227, 19, 26, 4, 3, 'caja'),
    (2, 50, 564, 12, 76, 6, 1, 'caja'), (2, 76, 621, 24, 14, 6, 2, 'ovalo'),
    (3, 72, 359, 15, 14, 7, 1, 'caja'), (3, 75, 507, 15, 14, 7, 2, 'caja'),
    (3, 555, 715, 14, 82, 7, 3, 'caja'),
]

GAP_TIRA = 6          # aire entre tiras
ALTO_PAG = 842 - 30 - 34


def _alto_burb(w, txt):
    lin = _lineas(txt, w - 14, 'DejaVuSans', 6.9)
    return 12 + 9.2 * (len(lin) + 1)


def disponer():
    """Reparte las tiras (y la banda de burbujas de cada una) en paginas nuevas.
       Devuelve [[(tira, y_nueva, arriba_h, abajo_h)]] por pagina."""
    paginas, cur, y = [], [], 30
    for t in TIRAS:
        pag, ya, yb, sid = t
        bs = BURB.get(sid, []) if sid else []
        alto_a = max([_alto_burb(w, tx) for (st, w, tp, tx, cx) in bs if st == 'arriba'] or [0])
        alto_b = max([_alto_burb(w, tx) for (st, w, tp, tx, cx) in bs if st == 'abajo'] or [0])
        ban_a = alto_a + 9 if alto_a else 0
        ban_b = alto_b + 9 if alto_b else 0
        total = ban_a + (yb - ya) + ban_b + GAP_TIRA
        if cur and y + total > 30 + ALTO_PAG:
            paginas.append(cur)
            cur, y = [], 30
        cur.append((t, y + ban_a, ban_a, ban_b))
        y += total
    paginas.append(cur)
    return paginas


def montar(salida):
    """PDF final: tiras de la partitura recolocadas + capa de anotaciones."""
    import pymupdf
    src = pymupdf.open(SRC)
    nuevo = pymupdf.open()
    paginas = disponer()
    for lista in paginas:
        pg = nuevo.new_page(width=595.276, height=PAGE_H)
        for (t, y0, ban_a, ban_b) in lista:
            pag, ya, yb, sid = t
            pg.show_pdf_page(pymupdf.Rect(0, y0, 595.276, y0 + (yb - ya)), src, pag - 1,
                             clip=pymupdf.Rect(0, ya, 595.276, yb))
    tmp = salida + '.base.pdf'
    nuevo.save(tmp)
    base = PdfReader(tmp)
    wr = PdfWriter()
    for i, lista in enumerate(paginas):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(595.276, PAGE_H))
        _anotar(c, lista, i + 1, len(paginas))
        c.save()
        buf.seek(0)
        pag = base.pages[i]
        pag.merge_page(PdfReader(buf).pages[0])
        wr.add_page(pag)
    with open(salida, 'wb') as f:
        wr.write(f)
    os.remove(tmp)
    return len(paginas)


def _anotar(c, lista, n, total):
    # offset: y_nueva = y_origen - ya + y0   (todas desde arriba)
    pos = {}
    for (t, y0, ban_a, ban_b) in lista:
        pos[t[3]] = (t, y0, ban_a, ban_b)
    segmentos = []
    for (t, y0, ban_a, ban_b) in lista:
        pag, ya, yb, sid = t
        if sid is None:
            continue
        sp, si = sid
        ts, bs = SIST[sp][si]
        c1, c2 = COMPASES[sp][si]
        b = bloque_de(c1)
        top = y0 + (ts - 24 - ya) if (sp, c1) not in ((3, 23), (3, 25)) else y0 + (ts - 34 - ya)
        top = max(top, y0 - 2)
        bot = y0 + (bs + 8 - ya)
        if segmentos and segmentos[-1][0] is b and abs(segmentos[-1][2] - top) < 40:
            segmentos[-1][2] = bot
        else:
            segmentos.append([b, top, bot, c1 == b[1]])
    for b, top, bot, primero in segmentos:
        col = b[4]
        c.setFillColor(Color(col.red, col.green, col.blue, alpha=0.055))
        c.roundRect(31, PAGE_H - bot, 543, bot - top, 4, fill=1, stroke=0)
        margen(c, b, top, bot, primero)
    for (pg_o, x, y, w, h, bn, n_, tipo) in MARCAS:
        for (t, y0, ban_a, ban_b) in lista:
            pag, ya, yb, sid = t
            if pag == pg_o and ya <= y <= yb:
                marca(c, x, y0 + (y - ya), w, h, [q for q in BLOQUES if q[0] == bn][0][4], n_, tipo)
    for (t, y0, ban_a, ban_b) in lista:
        pag, ya, yb, sid = t
        bs = BURB.get(sid, []) if sid else []
        xa, xb = 24, 24
        for (st, w, tp, tx, cx) in bs:
            if st == 'arriba':
                alto = _alto_burb(w, tx)
                burbuja(c, xa, y0 - ban_a + 4, w, tp, tx, 'abajo', min(max(cx, xa + 12), xa + w - 12))
                xa += w + 10
            else:
                burbuja(c, xb, y0 + (yb - ya) + 10, w, tp, tx, 'arriba', min(max(cx, xb + 12), xb + w - 12))
                xb += w + 10
    c.setFont('DejaVuSans', 6.4)
    c.setFillColor(HexColor('#7C838F'))
    c.drawString(34, 22, "Partitura: Michael Nyman, transcripción de David Jůna (DJ's Sheet Music "
                         "Archive). Anotaciones: T-Clas.")
    c.drawRightString(561, 22, str(n + OFFSET))


def main(salida):
    return montar(salida)


if __name__ == '__main__':
    out = os.path.join(HERE, 'entrega', 'DEMO_Partitura_por_bloques.pdf')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    print(main(out), 'paginas ->', out)
