# -*- coding: utf-8 -*-
"""Paginas de estudio de la DEMO: manos (izquierda / derecha) y guia por bloques."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from portada import W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, INK, MUTED, _wrap
from ficha_info import PANEL
import mayores_anotar as an

OCRE = HexColor('#8C6A3F')
AZUL = HexColor('#3E6E8F')
BLANCO = HexColor('#FFFFFF')
GRIS = HexColor('#D9D2BF')

KICK = 'DEMO · PIEZA 1 · THE HEART ASKS PLEASURE FIRST'


def marco(c, derecha, n):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(18, H - 24, W - 36, 6, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, H - 44, KICK)
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, H - 44, derecha)
    c.setFont('DejaVuSans', 7.4)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(n))


def titulo(c, t, sub):
    y = H - 76
    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, t)
    y -= 16
    return _wrap(c, sub, MARGIN, y, 'DejaVuSans', 9.4, CONTENT_W, 12.6, MUTED)


# ------------------------------------------------------------------ manos
IZQ = [
    ('Un golpe cada vez',
     'Cada golpe son seis notas. Toca solo el primero, despacio, diez veces seguidas sin '
     'fallar. Después, el siguiente.'),
    ('Parejo y despacio',
     'Metrónomo lento, todas las notas iguales y la primera de cada golpe un poco más fuerte.'),
    ('De memoria',
     'Mira la partitura para aprender el dibujo y luego toca sin mirar la mano.'),
    ('Une poco a poco',
     'Dos golpes, un compás, dos compases. Sube el metrónomo un punto cuando te salga tres '
     'veces seguidas.'),
]
DER = [
    ('Dos voces',
     'Al principio la derecha hace dos cosas: arriba, notas largas que cantan; debajo, '
     'semicorcheas. Aprende cada voz por separado.'),
    ('Canta la melodía',
     'Toca solo la voz de arriba y cántala por dentro. Las notas con > van un poco más fuertes.'),
    ('Las semicorcheas, más suaves',
     'Añade las de abajo con menos sonido que la melodía: la melodía manda, ellas acompañan.'),
    ('Con la izquierda',
     'Cuando la izquierda ande sola, júntalas despacio. Si se rompe, vuelve a una sola mano.'),
]


def _columna(c, x, y, ancho, titulo_, color, pasos):
    c.setFillColor(color)
    c.roundRect(x, y - 30, ancho, 30, 5, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSerif-Bold', 14)
    c.drawString(x + 14, y - 20, titulo_)
    y -= 44
    for i, (t, txt) in enumerate(pasos, 1):
        alto = 104
        c.setFillColor(PANEL)
        c.roundRect(x, y - alto, ancho, alto, 5, fill=1, stroke=0)
        c.setFillColor(color)
        c.rect(x, y - alto, 3, alto, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 34)
        c.setFillColor(GRIS)
        c.drawString(x + 14, y - 38, str(i))
        c.setFont('DejaVuSerif-Bold', 11)
        c.setFillColor(NAVY)
        c.drawString(x + 42, y - 30, t)
        _wrap(c, txt, x + 14, y - 54, 'DejaVuSans', 8.6, ancho - 28, 11.8, INK)
        y -= alto + 10
    return y


def pagina_manos(c, n):
    marco(c, 'Cómo estudiarla', n)
    y = titulo(c, 'Mano izquierda y mano derecha',
               'Cada mano se aprende sola. Las dos juntas llegan al final, despacio.')
    y -= 18
    ancho = (CONTENT_W - 16) / 2
    ya = _columna(c, MARGIN, y, ancho, 'MANO IZQUIERDA', OCRE, IZQ)
    _columna(c, MARGIN + ancho + 16, y, ancho, 'MANO DERECHA', AZUL, DER)
    y = ya - 6
    h = 62
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawString(MARGIN + 16, y - 16, 'LA TÉCNICA, EN TRES FRASES')
    t = ['Muñeca suelta y hombros bajos: si te cansas, estás apretando.',
         'Dedos curvos, cerca de las teclas, sonido ligero y parejo.',
         'Cuenta en voz alta los golpes (1-2-3, 4-5-6…) y no pares cuando cambie el compás.']
    yy = y - 31
    for s in t:
        c.setFillColor(NAVY)
        c.circle(MARGIN + 19, yy + 3, 1.8, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('DejaVuSans', 8.6)
        c.drawString(MARGIN + 28, yy, s)
        yy -= 12
    c.showPage()


# ---------------------------------------------------------------- bloques
def dots(c, x, y, n, col, r=2.1, sep=5.6):
    c.setFillColor(col)
    for i in range(n):
        c.circle(x + i * sep, y, r, fill=1, stroke=0)
    return x + (n - 1) * sep


def grupos(c, x, y, ng, por, col, rot=None, r=2.0, sep=5.0, hueco=7, h=11):
    """ng cajitas con `por` puntos cada una; rot: etiqueta bajo cada cajita."""
    for g in range(ng):
        w = (por - 1) * sep + 10
        c.setFillColor(HexColor('#FFFFFF'))
        c.setStrokeColor(col)
        c.setLineWidth(0.8)
        c.roundRect(x, y - h / 2, w, h, 3, fill=1, stroke=1)
        dots(c, x + 5, y, por, col, r, sep)
        if rot:
            c.setFont('DejaVuSans', 6)
            c.setFillColor(MUTED)
            c.drawCentredString(x + w / 2, y - h / 2 - 7, rot[g] if isinstance(rot, list) else rot)
        x += w + hueco
    return x


def chip(c, x, y, txt, col, size=7.4, relleno=False):
    w = stringWidth(txt, 'DejaVuSans-Bold', size) + 12
    if relleno:
        c.setFillColor(col)
        c.roundRect(x, y - 7, w, 14, 7, fill=1, stroke=0)
        c.setFillColor(BLANCO)
    else:
        c.setFillColor(BLANCO)
        c.setStrokeColor(col)
        c.setLineWidth(0.9)
        c.roundRect(x, y - 7, w, 14, 7, fill=1, stroke=1)
        c.setFillColor(col)
    c.setFont('DejaVuSans-Bold', size)
    c.drawString(x + 6, y - 2.4, txt)
    return x + w


def flecha(c, x, y, col, largo=12):
    c.setStrokeColor(col)
    c.setFillColor(col)
    c.setLineWidth(1)
    c.line(x, y, x + largo - 3, y)
    p = c.beginPath()
    p.moveTo(x + largo, y)
    p.lineTo(x + largo - 4, y + 2.6)
    p.lineTo(x + largo - 4, y - 2.6)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    return x + largo + 4


def etq(c, x, y, txt, col=MUTED, size=6.6):
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(col)
    c.drawString(x, y, txt)


def d1(c, x, y, col):
    etq(c, x, y + 13, 'UN COMPÁS DE 12/8 = 4 GOLPES · cada golpe, 6 notas')
    grupos(c, x, y - 4, 4, 6, col, ['golpe 1', 'golpe 2', 'golpe 3', 'golpe 4'])


def d2(c, x, y, col):
    etq(c, x, y + 13, 'MÁS RÁPIDO · tres capas que suenan a la vez')
    filas = [('MD melodía', AZUL), ('MD semicorcheas', AZUL), ('MI semicorcheas', OCRE)]
    for i, (t, cc) in enumerate(filas):
        yy = y - 1 - i * 10
        c.setFont('DejaVuSans', 6)
        c.setFillColor(MUTED)
        c.drawString(x, yy - 2, t)
        xx = x + 76
        if i == 0:
            for k in range(4):
                c.setFillColor(cc)
                c.roundRect(xx + k * 40, yy - 3, 34, 6, 3, fill=1, stroke=0)
                c.setFillColor(BLANCO)
                c.setFont('DejaVuSans-Bold', 6)
                c.drawString(xx + k * 40 + 4, yy - 2, '>')
        else:
            for k in range(4):
                dots(c, xx + k * 40, yy, 6, cc, 1.6, 5.4)


def d3(c, x, y, col):
    etq(c, x, y + 13, 'LA CUENTA NO SE ROMPE · cada grupo de tres = un golpe')
    xx = x
    for nombre, ng in (('c. 5 · 9/8', 3), ('c. 6 · 6/8', 2), ('c. 7 · 12/8', 4)):
        c.setFont('DejaVuSans-Bold', 6.4)
        c.setFillColor(col)
        c.drawString(xx, y - 14, nombre)
        xx2 = grupos(c, xx, y - 2, ng, 3, col, None, 2.0, 5.0, 4, 10)
        xx = xx2 + 10


def d4(c, x, y, col):
    etq(c, x, y + 13, 'LA CADENCIA (cc. 7-8 y 12)  →  y los compases de cc. 9-12')
    xx = chip(c, x, y - 1, 'Mi con 4.ª', col)
    xx = flecha(c, xx + 3, y - 1, col)
    xx = chip(c, xx, y - 1, 'Mi mayor', col)
    xx = flecha(c, xx + 3, y - 1, col)
    xx = chip(c, xx, y - 1, 'La menor', col, relleno=True)
    xx += 18
    for t in ('12/8', '9/8', '6/8', '12/8'):
        xx = chip(c, xx, y - 1, t, col) + 3


def d5(c, x, y, col):
    etq(c, x, y + 13, 'ES EL BLOQUE 1')
    xx = chip(c, x, y - 1, 'cc. 13-14', col, relleno=True)
    xx = flecha(c, xx + 3, y - 1, col)
    chip(c, xx, y - 1, '= cc. 1-2', col)


def d6(c, x, y, col):
    etq(c, x, y + 13, 'EL 8va · lo escrito y lo que suena (mano izquierda)')
    c.setFont('DejaVuSans', 6.4)
    c.setFillColor(MUTED)
    c.drawString(x, y - 2, 'escrito')
    xx = chip(c, x + 40, y + 1, 'nota', col)
    xx = flecha(c, xx + 6, y + 1, col, 26)
    xx = chip(c, xx, y + 1, 'suena una octava más grave', col, relleno=True)
    c.setFont('DejaVuSans', 6.4)
    c.setFillColor(MUTED)
    c.drawString(x, y - 14, 'dura hasta donde acaba la línea de puntos')


def d7(c, x, y, col):
    etq(c, x, y + 13, 'EL RECORRIDO')
    xx = x
    pasos = [('1-22', False), ('1ª: 23-24', True), ('↩ 15-22', False),
             ('2ª: 25-26', True), ('27-28', False), ('FIN', True)]
    for t, r in pasos:
        xx = chip(c, xx, y - 1, t, col, 7, relleno=r)
        if t != 'FIN':
            xx = flecha(c, xx + 2, y - 1, col, 9)


DIAG = {1: d1, 2: d2, 3: d3, 4: d4, 5: d5, 6: d6, 7: d7}

# (bloque, compases, titulo, [(paso, texto)] x4)
GUIA = [
    (1, 'cc. 1-2', 'La entrada', [
        ('IZQUIERDA', 'Solo las 6 notas del primer golpe. Cuando salgan, el segundo, hasta '
                      'cuatro golpes seguidos.'),
        ('DERECHA', 'Primero la voz de arriba sola (notas largas); luego las semicorcheas de '
                    'abajo.'),
        ('JUNTAS', 'Un golpe cada vez: izquierda con melodía, y al final todo.'),
        ('A TEMPO', 'Los dos compases seguidos, sin parar, tres veces.')]),
    (2, 'cc. 3-4', 'Más rápido: Più mosso', [
        ('IZQUIERDA', 'El mismo tipo de dibujo, pero más deprisa: empieza muy por debajo de '
                      'la velocidad final.'),
        ('DERECHA', 'Los acentos (>) marcan la melodía: tócalos un poco más fuertes.'),
        ('JUNTAS', 'Primero el c. 3, luego el c. 4, luego los dos.'),
        ('A TEMPO', 'Meta: la corchea a 180, que pone tu partitura. Sube poco a poco.')]),
    (3, 'cc. 5-6', 'Cambia el compás', [
        ('IZQUIERDA', 'Cuenta en voz alta mientras tocas: 1-2-3 / 1-2-3 / 1-2-3 (9/8) y '
                      '1-2-3 / 1-2-3 (6/8).'),
        ('DERECHA', 'Igual, contando. Cada grupo de tres es un golpe: no frenes al cambiar.'),
        ('JUNTAS', 'Los tres compases en bucle: c. 5, c. 6 y la vuelta a 12/8 del c. 7.'),
        ('OJO', 'Lo que cambia es cuántos golpes caben en el compás, no la velocidad.')]),
    (4, 'cc. 7-12', 'Cierre de la frase y vuelta', [
        ('IZQUIERDA', 'En el c. 7 hay notas ligadas en el bajo: se mantienen, no se vuelven '
                      'a tocar.'),
        ('DERECHA', 'Los cc. 9-12 siguen el camino de los cc. 3-8: ten abierta esa página.'),
        ('JUNTAS', 'Un compás con su cuenta: c. 9 en 12/8, c. 10 en 9/8, c. 11 en 6/8, c. 12 '
                   'en 12/8.'),
        ('OJO', 'El c. 12 cierra la frase: termina con calma.')]),
    (5, 'cc. 13-14', 'Vuelve la entrada', [
        ('IZQUIERDA', 'Es el bloque 1: tócala de memoria.'),
        ('DERECHA', 'Igual: sin partitura.'),
        ('JUNTAS', 'Dos pasadas seguidas sin parar.'),
        ('OJO', 'Si fallas, vuelve a la página del bloque 1.')]),
    (6, 'cc. 15-22', 'La repetición', [
        ('IZQUIERDA', 'En los cc. 15-16 lleva 8va: lees lo escrito y lo tocas una octava más '
                      'grave.'),
        ('DERECHA', 'Entran acordes nuevos (Do mayor y quintas de Mi y de Re): lee la letra '
                    'que va encima.'),
        ('JUNTAS', 'Un sistema al día: cc. 15-16, 17-18, 19-20, 21-22.'),
        ('OJO', 'Acuérdate de la barra de repetición del c. 15.')]),
    (7, 'cc. 23-28', 'Primera y segunda vez', [
        ('IZQUIERDA', 'Las casillas 1ª (cc. 23-24) y 2ª (cc. 25-26) son casi iguales: '
                      'mira cuál tocas.'),
        ('DERECHA', 'Igual que la izquierda: lo difícil es acordarse de por dónde vas.'),
        ('JUNTAS', 'Recorre el camino con el dedo sobre la partitura antes de tocar.'),
        ('A TEMPO', 'La pieza entera, de principio a fin, una vez al día.')]),
]
COL_PASO = {'IZQUIERDA': OCRE, 'DERECHA': AZUL, 'JUNTAS': NAVY, 'A TEMPO': HexColor('#4F7A5A'),
            'OJO': HexColor('#A0453A')}


def tarjeta(c, y, b, cc, nombre, pasos):
    col = [x for x in an.BLOQUES if x[0] == b][0][4]
    alto = 142
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - alto, CONTENT_W, alto, 5, fill=1, stroke=0)
    c.setFillColor(col)
    c.rect(MARGIN, y - alto, 4, alto, fill=1, stroke=0)
    c.circle(MARGIN + 24, y - 20, 11, fill=1, stroke=0)
    c.setFillColor(BLANCO)
    c.setFont('DejaVuSerif-Bold', 13)
    c.drawCentredString(MARGIN + 24, y - 24.5, str(b))
    c.setFillColor(NAVY)
    c.setFont('DejaVuSerif-Bold', 12)
    c.drawString(MARGIN + 44, y - 24, cc)
    c.setFont('DejaVuSans', 10)
    c.setFillColor(INK)
    c.drawString(MARGIN + 44 + stringWidth(cc, 'DejaVuSerif-Bold', 12) + 10, y - 24, nombre)
    DIAG[b](c, MARGIN + 16, y - 56, col)
    ancho = (CONTENT_W - 32 - 3 * 10) / 4
    for i, (p, t) in enumerate(pasos):
        x = MARGIN + 16 + i * (ancho + 10)
        pc = COL_PASO[p]
        c.setFillColor(pc)
        c.rect(x, y - 84, ancho, 2, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 7)
        c.drawString(x, y - 96, p)
        _wrap(c, t, x, y - 108, 'DejaVuSans', 7.8, ancho, 9.8, INK)
    return y - alto - 10


def paginas_bloques(c, n0):
    for k, grupo in enumerate((GUIA[:4], GUIA[4:])):
        marco(c, 'Guía por bloques', n0 + k)
        if k == 0:
            y = titulo(c, 'Cómo tocar cada bloque',
                       'Cada bloque, en el mismo orden: izquierda, derecha, juntas y a tempo.')
            y -= 14
        else:
            y = H - 76
        for (b, cc, nom, pasos) in grupo:
            y = tarjeta(c, y, b, cc, nom, pasos)
        if k == 1:
            y -= 14
            items = ['Toco de memoria la izquierda de los bloques 1, 2 y 3.',
                     'Cuento los golpes en los cambios de compás sin pararme.',
                     'Sé por dónde paso la primera vez y por dónde la segunda.',
                     'Toco la pieza entera, de principio a fin, sin parar.',
                     'La grabo con el móvil y la escucho.']
            h = 40 + 22 * len(items)
            c.setFillColor(PANEL)
            c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
            c.setFillColor(NAVY)
            c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
            c.setFont('DejaVuSans-Bold', 8.4)
            c.drawString(MARGIN + 18, y - 22, 'ANTES DE DECIR «YA LA SÉ»')
            yy = y - 46
            for t in items:
                c.setStrokeColor(NAVY)
                c.setLineWidth(1)
                c.roundRect(MARGIN + 18, yy - 3, 11, 11, 2, fill=0, stroke=1)
                c.setFillColor(INK)
                c.setFont('DejaVuSans', 9.4)
                c.drawString(MARGIN + 38, yy, t)
                yy -= 22
        c.showPage()
