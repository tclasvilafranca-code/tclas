# -*- coding: utf-8 -*-
"""Ficha de Can't Help Falling in Love para Dilan (nivel avanzado)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import segno
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from pypdf import PdfWriter, PdfReader
from portada import W, H
from ficha_info import build_ficha
from dilan_02_data import arpegio, RE, FAm, SIm

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                          ' cant-help-falling-in-love-.pdf')
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
YT_URL = 'https://www.youtube.com/results?search_query=elvis+presley+cant+help+falling+in+love'

CFG = dict(
    kicker='Dilan · canción 2 · nivel avanzado',
    titulo='Can’t Help Falling in Love',
    autor='Elvis Presley (1961) · arr. Seb Alejandro · edición con letra y cifrados',
    page_num=4,
    datos=[('Tonalidad', 'Re mayor'), ('Compás', '3/4'),
           ('Mano izq.', 'Acorde roto'), ('Mano dcha.', '1 nota por compás'),
           ('Extras', 'Letra + cifrados')],
    armonia=dict(
        titulo='El acorde roto de la mano izquierda',
        tarjetas=[
            ('C. 1  ·  CIFRADO D', 'Re mayor',
             'Re3 · Fa♯3 · La3 · Re4 · La3 · Fa♯3. Sube y baja el acorde entero.'),
            ('C. 2  ·  CIFRADO F♯m', 'Fa♯ menor',
             'Fa♯3 · La3 · Do♯4 · Mi4 · Do♯4 · La3. Mismo gesto, otro acorde.'),
            ('C. 3  ·  CIFRADO Bm', 'Si menor',
             'Si2 · Re3 · Fa♯3 · Si3 · Fa♯3 · Re3. Baja de registro, no de dibujo.'),
            ('CC. 5–6', 'La mayor',
             'La2 · Do♯3 · Mi3 · La3 · Mi3 · Do♯3. La dominante de la tonalidad.'),
        ],
        pie='El dibujo NUNCA cambia: fundamental, tercera, quinta, octava, y de vuelta. Lo único que '
            'cambia es sobre qué acorde lo haces. Si te aprendes el gesto una vez, la canción entera '
            'es leer cifrados, no leer notas.',
    ),
    time_sig=(3, 4),
    ritmos=[
        ('MI', 'seis corcheas: el acorde roto',
         arpegio(*RE), OCRE, 'bass', 'Re mayor'),
        ('MD', 'una blanca con puntillo, con su sílaba',
         [{'pitch': 'D4', 'dur': 'h.'}], AZUL, 'treble', 'Re mayor'),
    ],
    especial=[
        'La edición trae los CIFRADOS impresos: D, F♯m, Bm, G, A, A7… úsalos, son fiables.',
        'También trae la LETRA. Cántala mientras tocas: te marca el fraseo sola.',
        'La derecha toca UNA nota por compás. Todo el movimiento lo hace la izquierda.',
        'Armadura de dos sostenidos: todos los Fa y todos los Do son ♯.',
        'Hay barra de repetición: la primera parte se toca dos veces, con letra distinta.',
        'La sección F♯m – C♯7 del final es la única que sale de la tonalidad.',
    ],
    reto='Que la izquierda suene igual de floja en las seis corcheas. El acorde roto tiende a marcar '
         'de más la primera nota de cada compás, y entonces la canción se convierte en un vals.',
    truco='Toca la izquierda sola cantando la letra por encima. Si la voz se te va detrás de la mano, '
          'es que estás acentuando. Y lee los cifrados en voz alta antes de tocar: "Re, Fa sostenido '
          'menor, Si menor…". Media canción es saber dónde estás.',
    sabias='La melodía no es de 1961: viene de "Plaisir d’amour", una romanza francesa que Jean-Paul '
           'Égide Martini escribió en 1784. Elvis la grabó para la película "Blue Hawaii" y se convirtió '
           'en la canción con la que cerraba sus conciertos.',
    qr=dict(titulo='Escucha la versión de Elvis',
            texto='Fíjate en lo despacio que va. La prisa es el enemigo de esta canción.',
            png=None),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    qr = os.path.join(OUT_DIR, '_qr_d2.png')
    segno.make(YT_URL, error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    CFG['qr']['png'] = qr
    tmp = os.path.join(HERE, '_f2_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H)); build_ficha(c, CFG); c.save()
    wr = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    for p in PdfReader(tmp).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_02_CantHelp_Partitura_y_Ficha.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp); os.remove(qr)
    print('generated', out)


if __name__ == '__main__':
    main()
