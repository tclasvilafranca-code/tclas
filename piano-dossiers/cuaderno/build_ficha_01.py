# -*- coding: utf-8 -*-
"""Ficha de la partitura 1 de Arnau: Chopsticks.
   Todos los datos están leídos de la partitura real (arr. Gilbert
   DeBenedetti), no supuestos:
     - las DOS manos leen en clave de Sol (medido en la edición)
     - la indicación impresa "Only use finger 2, both hands"
     - arranque: mano izquierda Fa4, mano derecha Sol4 (2ª)
     - en el c. 7 el intervalo se abre a 3ª (Mi–Sol)
     - 32 compases, dos secciones (cc. 1-16 negras, cc. 17-32 blanca+negra)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from pypdf import PdfWriter, PdfReader
from portada import W, H
from ficha_info import build_ficha, BLUE
from portada import ACCENT, NAVY_SOFT

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU', ' Chopsticks.pdf')

# indice de tecla blanca: 0=Do4 ... 4=Sol4
CFG = dict(
    kicker='Arnau · canción 1',
    titulo='Chopsticks',
    autor='Tradicional · arr. Gilbert DeBenedetti',
    page_num=4,
    datos=[
        ('Tonalidad', 'Do mayor'),
        ('Compás', '3/4'),
        ('Compases', '32'),
        ('Carácter', 'Vals, juego'),
    ],
    total_compases=32,
    secciones=[
        ('A', 1, 16, 'El picoteo: negras sin parar', HexColor('#3E6E8F')),
        ('B', 17, 32, 'El vals: blanca + negra', HexColor('#8C6A3F')),
    ],
    time_sig=(3, 4),
    ritmos=[
        ('A', 'cc. 1–16 · tres golpes iguales',
         [{'pitches': ['F4', 'G4'], 'dur': 'q'}] * 3, HexColor('#3E6E8F')),
        ('B', 'cc. 17–32 · una larga y una corta',
         [{'pitches': ['F4', 'G4'], 'dur': 'h'}, {'pitches': ['F4', 'G4'], 'dur': 'q'}],
         HexColor('#8C6A3F')),
    ],
    teclado=dict(
        n_white=8, start_idx=0,
        # el 3er valor es el desplazamiento lateral del rotulo (Fa y Sol son
        # teclas vecinas: sin separarlos, los dos textos se pisarian)
        marks={3: (HexColor('#8C6A3F'), 'IZQUIERDA · dedo 2', -46),
               4: (HexColor('#3E6E8F'), 'DERECHA · dedo 2', 46)},
        pie='Las dos manos empiezan juntas, pegadas: la izquierda en FA y la derecha en SOL. '
            'Son teclas vecinas — un intervalo de 2ª.',
    ),
    especial=[
        'Las dos manos leen en CLAVE DE SOL. No hay clave de Fa en toda la pieza.',
        'La partitura lo dice: solo se usa el DEDO 2 de cada mano, de principio a fin.',
        'Empieza con las manos pegadas (2ª: Fa–Sol) y en el c. 7 se abren a una 3ª (Mi–Sol).',
        'No hay ni una alteración: todo teclas blancas.',
    ],
    reto='Que las dos manos caigan exactamente a la vez. Si una se adelanta, se oye "doble" '
         'en vez de un solo golpe limpio.',
    truco='Cuenta "UN-dos-tres" en voz alta y deja caer las dos manos juntas en el "UN". '
          'Los dedos 2 firmes, como dos palillos.',
    sabias='La escribió una chica de 16 años, Euphemia Allen, en 1877, y la publicó con el '
           'nombre falso de "Arthur de Lulli". El título original era "The Celebrated Chop Waltz": '
           'el nombre viene del gesto de cortar con el canto de la mano, no de los palillos de comer.',
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
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
    print('generated', out)


if __name__ == '__main__':
    main()
