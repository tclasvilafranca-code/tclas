# -*- coding: utf-8 -*-
"""Pagina 'Como dividir la pieza en bloques' + montaje de la DEMO completa:
   ficha · plan por bloques · partitura anotada por bloques."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from pypdf import PdfReader, PdfWriter
from portada import W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, INK, MUTED, _wrap
from ficha_info import PANEL
import build_mayores_demo as ficha
import mayores_anotar as an

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, 'entrega')

# (bloque, compases, que se trabaja, en clase, en casa, marcas con anillo)
FILAS = [
    (1, 'cc. 1-2', 'La entrada, "Con moto": La menor, Sol mayor y La menor en inversión, y Re mayor, '
                   'con pedal. Una figura de semicorcheas que se repite.',
     'Izquierda sola, luego derecha sola; juntas a media velocidad.',
     'Izquierda de memoria, 5 minutos al día.', '① tempo  ② mf'),
    (2, 'cc. 3-4', 'Più mosso (corchea = 180). La izquierda dibuja seis semicorcheas por '
                   'golpe; la derecha pone la melodía encima, con acentos en el c. 3.',
     'La izquierda sola hasta que ande sola; luego la derecha con los acentos (>).',
     'Izquierda sola con metrónomo lento; sube un punto al día.', '① Più mosso  ② f'),
    (3, 'cc. 5-6', 'El compás cambia: 9/8 (tres golpes) y 6/8 (dos). Las semicorcheas no '
                   'frenan: cambia cuántas caben antes de volver a empezar.',
     'Cuenta en voz alta 1-2-3 / 1-2-3 / 1-2-3 y 1-2-3 / 1-2-3 mientras tocas la izquierda.',
     'Los dos compases en bucle, con metrónomo y contando.', '① 9/8  ② 6/8  ③ vuelve 12/8'),
    (4, 'cc. 7-12', 'La cadencia sobre la dominante (Mi con cuarta suspendida → Mi mayor → La menor, '
                    'cc. 7-8) y la vuelta de 9-12, que repite el camino de 3-8 con otro 9/8 y otro 6/8.',
     'Leer los cc. 9-12 como "el bloque 3 con otras notas": solo cambian las alturas.',
     'Cada compás con su cuenta; después, de corrido hasta el c. 12.',
     '① cadencia  ② 9/8  ③ 6/8  ④ 12/8'),
    (5, 'cc. 13-14', 'Vuelve la entrada: es el bloque 1. No es material nuevo.',
     'Tocarla de memoria, sin partitura.', 'Dos pasadas seguidas sin parar.', '—'),
    (6, 'cc. 15-22', 'Empieza la repetición (barra con puntos). La izquierda va escrita con '
                     '8va en los cc. 15-16 y entran acordes nuevos: Do mayor y quintas vacías de Mi y de Re (sin tercera).',
     'Primero la izquierda con el 8va (suena una octava más grave); después la derecha.',
     'Un sistema por día: cc. 15-16, 17-18, 19-20, 21-22.', '① repetición  ② 8va (ottava bassa)'),
    (7, 'cc. 23-28', 'Casilla 1ª (cc. 23-24) la primera vez; la segunda vez se salta a la '
                     'casilla 2ª (cc. 25-26). Final en doble barra (cc. 27-28).',
     'Dibujar el recorrido con el dedo sobre la partitura: ¿por dónde pasas la 2ª vez?',
     'La pieza entera, de principio a fin, una vez al día.', '① 1ª  ② 2ª  ③ doble barra'),
]


def pagina(c, n):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(18, H - 24, W - 36, 6, fill=1, stroke=0)
    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'DEMO · PIEZA 1 · THE HEART ASKS PLEASURE FIRST')
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, 'Plan por bloques')
    y -= 30
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'Cómo dividir la pieza')
    y -= 15
    y = _wrap(c, 'Siete bloques, marcados con un color y un número sobre la partitura de las páginas siguientes. '
                 'En clase se trabaja el bloque; en casa se repasa con la misma tabla. Orden de '
                 'siempre: izquierda sola, derecha sola, juntas despacio, y solo al final a tempo.',
              MARGIN, y, 'DejaVuSans', 8.6, CONTENT_W, 11.6, MUTED)
    y -= 12
    colw = [30, 54, 176, 100, 95]
    xs = [MARGIN]
    for w in colw[:-1]:
        xs.append(xs[-1] + w + 8)
    for i, t in enumerate(['BLOQUE', 'COMPASES', 'QUÉ SE TRABAJA', 'EN CLASE', 'EN CASA']):
        c.setFont('DejaVuSans-Bold', 6.8)
        c.setFillColor(MUTED)
        c.drawString(xs[i] + (0 if i else 0), y, t)
    y -= 8
    for (b, cc, que, clase, casa, marcas) in FILAS:
        col = [x for x in an.BLOQUES if x[0] == b][0][4]
        alto = 0
        # altura = la columna mas larga
        from reportlab.pdfbase.pdfmetrics import stringWidth

        def lineas(t, w, size=7.8):
            n, cur = 1, ''
            for pal in t.split():
                prueba = (cur + ' ' + pal).strip()
                if stringWidth(prueba, 'DejaVuSans', size) > w and cur:
                    n += 1
                    cur = pal
                else:
                    cur = prueba
            return n
        nl = max(lineas(que, colw[2]), lineas(clase, colw[3]), lineas(casa, colw[4]))
        alto = nl * 10.4 + 26
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - alto, CONTENT_W, alto, 4, fill=1, stroke=0)
        c.setFillColor(col)
        c.rect(MARGIN, y - alto, 4, alto, fill=1, stroke=0)
        c.circle(xs[0] + 14, y - alto / 2, 10, fill=1, stroke=0)
        c.setFillColor(HexColor('#FFFFFF'))
        c.setFont('DejaVuSerif-Bold', 12)
        c.drawCentredString(xs[0] + 14, y - alto / 2 - 4.2, str(b))
        c.setFillColor(NAVY)
        c.setFont('DejaVuSerif-Bold', 10)
        c.drawString(xs[1], y - alto / 2 - 3.5, cc)
        for i, t in ((2, que), (3, clase), (4, casa)):
            c.setFillColor(INK)
            _wrap(c, t, xs[i], y - 13, 'DejaVuSans', 7.8, colw[i], 10.4, INK)
        c.setFont('DejaVuSans', 6.6)
        c.setFillColor(col)
        c.drawString(xs[2], y - alto + 6, 'Señala con lápiz:  ' + marcas)
        y -= alto + 7
    y -= 8
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - 56, CONTENT_W, 56, 4, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(MARGIN, y - 56, 2.6, 56, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN + 12, y - 14, 'CÓMO LEER LA PARTITURA ANOTADA')
    _wrap(c, 'La ficha numerada y el paréntesis del margen izquierdo dicen en qué bloque estás. '
             'Los recuadros con número son las cosas que hay que mirar antes de tocar: el compás, '
             'el tempo, el matiz, el 8va, las repeticiones. Tacha el número con lápiz cuando lo '
             'tengas.', MARGIN + 12, y - 25, 'DejaVuSans', 8, CONTENT_W - 24, 10.6, INK)
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(n))
    c.showPage()
    return y


def main():
    os.makedirs(OUT, exist_ok=True)
    ficha.main()
    tmp = os.path.join(OUT, '_plan.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    y = pagina(c, 3)
    c.save()
    print('y final plan', y)
    anot = os.path.join(OUT, 'DEMO_Partitura_por_bloques.pdf')
    an.main(anot)
    wr = PdfWriter()
    for f in ('DEMO_Ficha_Heart.pdf', '_plan.pdf', 'DEMO_Partitura_por_bloques.pdf'):
        for p in PdfReader(os.path.join(OUT, f)).pages:
            wr.add_page(p)
    dst = os.path.join(OUT, 'DEMO_Dosier_Heart.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    os.remove(tmp)
    print(dst)


if __name__ == '__main__':
    main()
