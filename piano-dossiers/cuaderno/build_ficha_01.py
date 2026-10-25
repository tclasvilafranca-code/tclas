# -*- coding: utf-8 -*-
"""Ficha de la partitura 1 de Arnau: Chopsticks.

   Todos los datos están LEÍDOS de la edición real (arr. Gilbert
   DeBenedetti), midiendo el PDF fuente, no supuestos. La transcripción
   completa y el método de medida están en TRANSCRIPCION_01_CHOPSTICKS.md:
     - las dos manos leen en clave de Sol, sobre un único pentagrama
     - la indicación impresa "Only use finger 2, both hands"
     - la apertura real: cc. 1-2 en 2ª (Fa-Sol), cc. 3-4 en 3ª (Mi-Sol),
       cc. 5-6 en 6ª (Re-Si), cc. 7-8 en 8ª (Do-Do). La 5ª no sale nunca.
     - silencios de negra en los cc. 15-16: las dos manos callan a la vez
     - ni una sola dinámica escrita en toda la pieza
     - 32 compases, dos secciones (cc. 1-16 negras, cc. 17-32 blanca+negra)
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
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU', ' Chopsticks.pdf')

IZQ = HexColor('#8C6A3F')
DCHA = HexColor('#3E6E8F')

# Búsqueda de YouTube en vez de un vídeo concreto: un enlace de búsqueda no
# se puede quedar muerto si el canal borra el vídeo, y el cuaderno es papel
# que dura todo el curso.
YT_URL = 'https://www.youtube.com/results?search_query=chopsticks+piano+euphemia+allen'

# índice de tecla blanca: 0=Do 1=Re 2=Mi 3=Fa 4=Sol 5=La 6=Si
CFG = dict(
    kicker='Arnau · canción 1',
    titulo='Chopsticks',
    autor='Tradicional · arr. Gilbert DeBenedetti',
    page_num=4,
    datos=[
        ('Tonalidad', 'Do mayor'),
        ('Compás', '3/4'),
        ('Compases', '32'),
        ('Tempo de estudio', '60 → 112'),
        ('Carácter', 'Vals, juego'),
    ],
    total_compases=32,
    secciones=[
        ('A', 1, 16, 'El picoteo: negras sin parar', DCHA),
        ('B', 17, 32, 'El vals: blanca + negra', IZQ),
    ],
    apertura=dict(
        titulo='Cómo se abren las manos',
        pasos=[
            ('cc. 1–2  ·  2ª', {3: IZQ, 4: DCHA}),    # Fa + Sol
            ('cc. 3–4  ·  3ª', {2: IZQ, 4: DCHA}),    # Mi + Sol
            ('cc. 5–6  ·  6ª', {1: IZQ, 6: DCHA}),    # Re + Si
            ('cc. 7–8  ·  8ª', {0: IZQ, 7: DCHA}),    # Do + Do
        ],
        leyenda=[(IZQ, 'MANO IZQUIERDA · dedo 2'), (DCHA, 'MANO DERECHA · dedo 2')],
        pie='Las manos se abren en espejo: la izquierda baja Fa-Mi-Re-Do mientras la derecha '
            'sube hasta el Do de arriba. Luego el camino se hace al revés y vuelven a juntarse. '
            'En los cc. 1–4 la derecha ni se mueve: solo anda la izquierda.',
    ),
    time_sig=(3, 4),
    ritmos=[
        ('A', 'tres golpes iguales',
         [{'pitches': ['F4', 'G4'], 'dur': 'q'}] * 3, DCHA),
        ('B', 'una larga y una corta',
         [{'pitches': ['F4', 'G4'], 'dur': 'h'}, {'pitches': ['F4', 'G4'], 'dur': 'q'}], IZQ),
    ],
    especial=[
        'Las dos manos leen en CLAVE DE SOL, en un solo pentagrama. No hay clave de Fa.',
        'La partitura lo dice: solo el DEDO 2 de cada mano, de principio a fin.',
        'Las manos van en ESPEJO: cuando una sube, la otra baja exactamente lo mismo.',
        'En los cc. 15–16 las dos manos callan A LA VEZ en el segundo tiempo.',
        'En la parte B las dos manos tocan la misma melodía separadas por una 3ª.',
        'No hay ni una dinámica escrita: el fuerte y el suave los decides tú.',
        'Ni una alteración: todo teclas blancas.',
    ],
    reto='Los cc. 15–16 y 31–32. Ahí hay un silencio en medio y las manos tienen que saltar de '
         'una 8ª a una 2ª: el salto entero ocurre DENTRO del silencio.',
    truco='Cuenta "UN-dos-tres" en voz alta SIEMPRE, también en los silencios: el silencio no es '
          'para descansar, es para viajar. Los dedos 2 firmes, como dos palillos.',
    sabias='La escribió una chica de 16 años, Euphemia Allen, en 1877, y la publicó con el '
           'nombre falso de "Arthur de Lulli". El título original era "The Celebrated Chop Waltz": '
           'viene del gesto de cortar con el canto de la mano, no de los palillos de comer.',
    qr=dict(titulo='Escúchala antes de tocarla',
            texto='Oye la pieza varias veces antes de sentarte al piano.',
            png=None),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    qr_png = os.path.join(OUT_DIR, '_qr_chopsticks.png')
    segno.make(YT_URL, error='m').save(qr_png, scale=10, border=2,
                                       dark='#1A2332', light='#F3F1EA')
    CFG['qr']['png'] = qr_png

    tmp = os.path.join(HERE, '_ficha_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_ficha(c, CFG)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for p in PdfReader(tmp).pages:
        writer.add_page(p)
    out = os.path.join(OUT_DIR, 'Arnau_01_Chopsticks_Partitura_y_Ficha.pdf')
    with open(out, 'wb') as f:
        writer.write(f)
    os.remove(tmp)
    os.remove(qr_png)
    print('generated', out)


if __name__ == '__main__':
    main()
