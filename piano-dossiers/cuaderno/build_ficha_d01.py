# -*- coding: utf-8 -*-
"""Ficha de El Cisne para Dilan (nivel avanzado).

   Diferencias respecto a una ficha de iniciación:
     - en vez de mini-teclados con la posición de la mano, tarjetas de
       ARMONÍA: qué acorde arpegia la izquierda y qué función cumple
     - la tira de datos incluye el arco de dinámicas, que en esta pieza es
       la mitad del trabajo
     - el reto no es de dedos, es de equilibrio entre las dos manos
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import segno
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from pypdf import PdfWriter, PdfReader
from portada import W, H
from ficha_info import build_ficha

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN', 'the-swan.pdf')

AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

YT_URL = 'https://www.youtube.com/results?search_query=saint-saens+le+cygne+the+swan+cello'

CFG = dict(
    kicker='Dilan · canción 1 · nivel avanzado',
    titulo='El Cisne',
    autor='Camille Saint-Saëns (1835–1921) · de "El Carnaval de los Animales" · rev. Ricardo Boppré',
    page_num=4,
    datos=[
        ('Tonalidad', 'Sol mayor'),
        ('Compás', '3/4'),
        ('Compases', '55'),
        ('Tempo', 'Andante ♩=96'),
        ('Dinámica', 'pp → mf → pp'),
    ],
    total_compases=55,
    secciones=[
        ('A', 1, 12, 'El tema, sobre pedal de Sol', AZUL),
        ('B', 13, 42, 'Modula: alteraciones y tensión', OCRE),
        ("A'", 43, 55, 'Vuelve el tema y se apaga', AZUL),
    ],
    armonia=dict(
        titulo='Qué arpegia la mano izquierda',
        tarjetas=[
            ('cc. 1–4', 'Sol mayor',
             'Sol2 · Re3 · Si3. El acorde de la tonalidad, en estado fundamental.'),
            ('cc. 5–7', 'La menor /Sol',
             'Sol2 · Mi3 · La3. El bajo no se mueve: cambian solo las dos notas de arriba.'),
            ('c. 8', 'Sol maj7',
             'Sol2 · Re3 · Fa♯3. El Fa♯ viene de la armadura, no está escrito.'),
            ('cc. 9–12', 'Sol mayor',
             'Vuelve el acorde del principio y cierra la primera frase.'),
        ],
        pie='Durante los doce primeros compases el bajo está clavado en Sol2: es un pedal. Todo el '
            'movimiento que oyes lo hacen las dos notas de arriba de la mano izquierda, que es '
            'justo lo que hay que aprender a tocar sin que se note.',
    ),
    time_sig=(3, 4),
    ritmos=[
        ('MI', 'seis corcheas, sin parar',
         [{'pitch': p, 'dur': 'e', 'beam': 1} for p in ['G2', 'D3', 'B3', 'D3', 'B3', 'D3']],
         OCRE, 'bass', 'Sol mayor'),
        ('MD', 'la melodía, en notas largas',
         [{'pitch': 'G5', 'dur': 'q'}, {'pitch': 'F5', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'}],
         AZUL, 'treble', 'Sol mayor'),
    ],
    especial=[
        'La izquierda no para: corcheas ligadas de principio a fin, 55 compases seguidos.',
        'Los cc. 7–9 son una escala de Sol mayor entera, de Mi4 a Sol5, escrita en la pieza.',
        'En los cc. 53–54 la mano izquierda se escribe en CLAVE DE SOL, y vuelve a Fa en el 55.',
        'La digitación viene impresa en las dos manos: úsala, está pensada.',
        'Los recuadros de compás de esta edición marcan el ÚLTIMO compás del sistema anterior.',
        'Toda la pieza vive entre pp y mf. El único mf está en el c. 43.',
    ],
    reto='Que las dos manos suenen a distinto volumen a la vez: la izquierda es agua de fondo y '
         'no puede taparse con la melodía. Es un problema de equilibrio, no de dedos.',
    truco='Estudia la izquierda sola hasta que te aburra, y después tócala mientras cantas la '
          'melodía en voz alta. Si al añadir la derecha la izquierda sube de volumen, es que aún '
          'no está automática.',
    sabias='Saint-Saëns escribió "El Carnaval de los Animales" en 1886 como una broma privada y '
           'prohibió publicarlo mientras viviera, por miedo a que le tomaran por un compositor '
           'poco serio. Hizo una sola excepción: El Cisne. Es la única pieza del Carnaval que se '
           'publicó en vida suya.',
    qr=dict(titulo='Escúchala tocada al violonchelo',
            texto='El original es para chelo y dos pianos. Oye cómo respira la frase antes de tocarla.',
            png=None),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    qr = os.path.join(OUT_DIR, '_qr_d1.png')
    segno.make(YT_URL, error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    CFG['qr']['png'] = qr
    tmp = os.path.join(HERE, '_fd_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_ficha(c, CFG)
    c.save()
    wr = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    for p in PdfReader(tmp).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_01_ElCisne_Partitura_y_Ficha.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp); os.remove(qr)
    print('generated', out)


if __name__ == '__main__':
    main()
