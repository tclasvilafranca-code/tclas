import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de DESPACITO_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song12 = dict(
  num=12, title='Despacito', subtitle='Luis Fonsi & Daddy Yankee · arr. Unai Karam',
  tonalidad='La menor', compas='4/4', tempo='Moderato ♩≈76', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Ostinato en octavas + melodía',
  la_cancion='El reggaetón de Luis Fonsi, en La menor. Hoy: el ostinato 3+3+2, pero en octavas, con más peso y alcance en la izquierda.',
  difficult_cc='cc. 1–4', difficult_title='El ostinato en octavas: el mismo dibujo, con más peso',
  reto='mantener el dibujo rítmico 3+3+2 firme mientras la mano abarca la octava entera en cada golpe.',
  truco='practica primero solo con una nota hasta que el ritmo salga solo; luego añade la octava sin tensar la muñeca.',
  sabias_que='"Despacito" (2017) de Luis Fonsi y Daddy Yankee fue durante años el vídeo más visto de la historia de YouTube.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('C5', 3), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · ABRIL',
  total_songs=22,
)

cfg12 = dict(
  kicker='VALENTINA · ABRIL · DESPACITO (LUIS FONSI & DADDY YANKEE)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A3', 'B3'), ('A3', 'C4'), ('A3', 'D4'), ('A3', 'E4'), ('A3', 'F4'), ('A3', 'A4')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mim...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'A3'], ['D2', 'F2', 'A2'], ['E2', 'G2', 'B2'], ['C3', 'E3', 'A3']],
  song_title='Despacito', song_key='La menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en La menor (i, iv, v...).',
  progression=['Lam', 'Rem', 'Mim', 'Lam'],
  progression_mode='names',
  rhythm_desc='Lee y marca el ritmo real: el ostinato 3+3+2 en octavas, en 4/4.',
  rhythm_events=[{'pitches': ['A2', 'A3'], 'dur': 'e', 'beam': g} for g in [0, 0, 0, 1, 1, 1, 2, 2]],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song12)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg12)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_12_Despacito.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
