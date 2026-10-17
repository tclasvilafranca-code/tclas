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

PASOS = [
    ('Un golpe cada vez',
     'Cada golpe de la izquierda son seis notas que forman un dibujo. Toca solo el primer '
     'golpe, despacio, diez veces seguidas sin fallar. Después, el siguiente.'),
    ('Parejo y despacio',
     'Con el metrónomo lento, todas las notas iguales y la primera de cada golpe un poquito '
     'más fuerte. Si te aceleras, vuelve a bajar.'),
    ('De memoria',
     'Aprende el dibujo con los ojos puestos en la partitura y luego sin mirar la mano. '
     'Tu mano izquierda tiene que poder tocar sola mientras tú piensas en la derecha.'),
    ('Une poco a poco',
     'Dos golpes, luego un compás, luego dos compases. Sube el metrónomo un punto solo '
     'cuando te salga tres veces seguidas.'),
]

TECNICA = [
    'Muñeca suelta y hombros bajos: si te cansas, estás apretando.',
    'Dedos curvos, cerca de las teclas, sonido ligero y parejo.',
    'Cuenta en voz alta los golpes: 1-2-3, 4-5-6… sin dejar de contar cuando cambie el compás.',
]

BLOQUES_TXT = [
    (1, 'cc. 1-2', 'La entrada'),
    (2, 'cc. 3-4', 'Más rápido: el dibujo de la izquierda'),
    (3, 'cc. 5-6', 'Cambia el compás: 9/8 y 6/8'),
    (4, 'cc. 7-12', 'Cierre de la frase y vuelta'),
    (5, 'cc. 13-14', 'Vuelve la entrada: repásala'),
    (6, 'cc. 15-22', 'Repetición: la izquierda, una octava más grave'),
    (7, 'cc. 23-28', 'Primera y segunda vez, y final'),
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
    c.drawRightString(W - MARGIN, y, 'Cómo estudiarla')
    y -= 32
    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'La mano izquierda')
    y -= 16
    y = _wrap(c, 'La izquierda es la base de la pieza: un dibujo de seis notas que se repite. '
                 'Si ella anda sola, la derecha se coloca encima con calma. Estúdiala en cuatro pasos.',
              MARGIN, y, 'DejaVuSans', 9.4, CONTENT_W, 12.6, MUTED)
    y -= 18
    ancho = (CONTENT_W - 14) / 2
    alto = 128
    for i, (tit, txt) in enumerate(PASOS):
        x = MARGIN + (i % 2) * (ancho + 14)
        top = y - (i // 2) * (alto + 14)
        c.setFillColor(PANEL)
        c.roundRect(x, top - alto, ancho, alto, 5, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.rect(x, top - alto, 3, alto, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 40)
        c.setFillColor(HexColor('#D9D2BF'))
        c.drawString(x + 16, top - 46, str(i + 1))
        c.setFont('DejaVuSerif-Bold', 13)
        c.setFillColor(NAVY)
        c.drawString(x + 52, top - 32, tit)
        _wrap(c, txt, x + 16, top - 62, 'DejaVuSans', 9, ancho - 32, 12.4, INK)
    y -= 2 * (alto + 14) + 4
    # tecnica
    th = 24 + len(TECNICA) * 17
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - th, CONTENT_W, th, 5, fill=1, stroke=0)
    c.setFillColor(HexColor('#8C6A3F'))
    c.rect(MARGIN, y - th, 3, th, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawString(MARGIN + 16, y - 16, 'LA TÉCNICA, EN TRES FRASES')
    yy = y - 34
    for t in TECNICA:
        c.setFillColor(HexColor('#8C6A3F'))
        c.circle(MARGIN + 19, yy + 3, 2, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('DejaVuSans', 9)
        c.drawString(MARGIN + 28, yy, t)
        yy -= 17
    y -= th + 26
    # bloques
    c.setFont('DejaVuSans-Bold', 8)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'LOS BLOQUES DE LA PARTITURA · uno por clase, o dos si te sale rápido')
    y -= 12
    for b, cc, txt in BLOQUES_TXT:
        col = [x for x in an.BLOQUES if x[0] == b][0][4]
        c.setFillColor(col)
        c.circle(MARGIN + 9, y - 3, 7.5, fill=1, stroke=0)
        c.setFillColor(HexColor('#FFFFFF'))
        c.setFont('DejaVuSerif-Bold', 9)
        c.drawCentredString(MARGIN + 9, y - 6, str(b))
        c.setFillColor(NAVY)
        c.setFont('DejaVuSerif-Bold', 9)
        c.drawString(MARGIN + 26, y - 5.5, cc)
        c.setFillColor(INK)
        c.setFont('DejaVuSans', 9)
        c.drawString(MARGIN + 92, y - 5.5, txt)
        y -= 19
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(n))
    c.showPage()
    return y


def main():
    os.makedirs(OUT, exist_ok=True)
    import mayores_guia as g
    from cancion import _mezcla_compases
    from hoja_taller import build_taller
    from hoja_pauta import build_pauta
    ficha.CFG['page_num'] = 1
    ficha.main()
    kicker = 'Demo · pieza 1 · The Heart Asks Pleasure First'
    tmp = os.path.join(OUT, '_plan.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    tal = dict(kicker=kicker, page_num=2, time_sig=(12, 8), key_sig=None, gap=6.6, semilla=31,
               nivel_lectura=1, titulo='Dedos y ojos', esquina='Antes de la partitura',
               compases_extra=_mezcla_compases((12, 8), 5031),
               compases_extra_leer=_mezcla_compases((12, 8), 6031),
               intro='Cinco minutos antes de abrir la partitura. Arriba se TOCA y abajo se LEE EN '
                     'VOZ ALTA, sin tocar nada. Son notas de La menor, que es la tonalidad de la '
                     'pieza, y conviene empezar despacio: la pieza va en semicorcheas.')
    g.pagina_manos(c, 2)
    g.paginas_bloques(c, 3)
    c.save()
    an.OFFSET = 4
    anot = os.path.join(OUT, 'DEMO_Partitura_por_bloques.pdf')
    npag = an.main(anot)
    ult = 4 + npag
    pau = os.path.join(OUT, '_pauta.pdf')
    c = canvas.Canvas(pau, pagesize=(W, H))
    build_pauta(c, dict(kicker=kicker, page_num=ult + 1, titulo_pauta='Para escribir',
                        pie_pauta='la clave la pones tú · copia un compás, escribe la escala de '
                                  'La menor o inventa algo'))
    c.save()
    wr = PdfWriter()
    orden = [('DEMO_Ficha_Heart.pdf', None), ('_plan.pdf', None), (anot, 'abs'), (pau, 'abs')]
    for f, ab in orden:
        ruta = f if ab else os.path.join(OUT, f)
        for pg in PdfReader(ruta).pages:
            wr.add_page(pg)
    dst = os.path.join(OUT, 'DEMO_Dosier_Heart.pdf')
    with open(dst, 'wb') as fh:
        wr.write(fh)
    os.remove(tmp)
    os.remove(pau)
    print(dst, len(wr.pages), 'paginas')


if __name__ == '__main__':
    main()
