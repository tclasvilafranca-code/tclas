# -*- coding: utf-8 -*-
"""Prepara cant_stop_recto.pdf: gira la pagina 1 (apaisada, girada 90 grados) y recoloca sus tres
   sistemas de 6/6/5 compases en seis filas mas cortas (cc. 1-4, 5-6, 7-9, 10-12, 13-15, 16-17)
   a tamano natural, con la clave repetida al inicio de cada fila y su numero de compas.
   Los trozos salen del propio PDF, sin tocar una nota."""
import os
from PIL import Image, ImageDraw, ImageFont
import pymupdf

TOPS = [554, 1190, 1824]            # linea superior del pentagrama de agudos, por sistema (300 ppp)
BOTS = [904, 1540, 2174]            # linea inferior del pentagrama de graves
PX = 72.0 / 300.0
# (sistema, x_ini, x_fin, con_clave_repetida, numero de compas)
FILAS = [(0, 20, 2290, False, 1), (0, 2282, 3280, True, 5),
         (1, 20, 1570, False, 7), (1, 1566, 3280, True, 10),
         (2, 20, 2092, False, 13), (2, 2086, 3300, True, 16)]
CLAVE = (20, 190)


def preparar(origen, destino):
    if os.path.exists(destino) or not os.path.exists(origen):
        return
    d = pymupdf.open(origen)
    d[0].set_rotation(90)
    tmp = destino + '.png'
    d[0].get_pixmap(dpi=300).save(tmp)
    im = Image.open(tmp).convert('RGB')
    os.remove(tmp)
    try:
        fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 30)
    except OSError:
        fnt = ImageFont.load_default()
    filas = []
    for (s, x0, x1, clave, num) in FILAS:
        y0, y1 = TOPS[s] - 96, BOTS[s] + 62
        cont = im.crop((x0, y0, x1, y1))
        if clave:
            cl = im.crop((CLAVE[0], y0, CLAVE[1], y1))
            row = Image.new('RGB', (cl.width + cont.width, y1 - y0), 'white')
            row.paste(cl, (0, 0))
            row.paste(cont, (cl.width, 0))
        else:
            row = cont
        dr = ImageDraw.Draw(row)
        dr.rectangle((40, 0, 150, 52), fill='white')
        if num != 1:
            dr.text((72, 14), str(num), font=fnt, fill=(70, 70, 70))
        filas.append((row, num))
    titulo = im.crop((1000, 120, 2320, 250))
    out = pymupdf.open()
    ancho, alto = 595.276, 841.89

    def poner(pg, img, x, y):
        buf = os.path.join(os.path.dirname(destino), '_cs_tmp.png')
        img.save(buf)
        pg.insert_image(pymupdf.Rect(x, y, x + img.width * PX, y + img.height * PX), filename=buf)
        os.remove(buf)

    for k, grupo in enumerate((filas[:3], filas[3:])):
        pg = out.new_page(width=ancho, height=alto)
        y = 40
        if k == 0:
            poner(pg, titulo, (ancho - titulo.width * PX) / 2, 40)
            y = 120
        for (row, num) in grupo:
            poner(pg, row, 22, y)
            y += row.height * PX + 22
    out.save(destino)
