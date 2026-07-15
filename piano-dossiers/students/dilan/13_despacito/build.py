import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'DESPACITO_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song13 = dict(
  num=13, title='Despacito', subtitle='Luis Fonsi & Daddy Yankee · arr. Unai Karam',
  tonalidad='La menor', compas='4/4', tempo='Moderato ♩≈76', forma='Estrofa-estribillo',
  dificultad='Un reto rítmico', manos='Ostinato + melodía',
  la_cancion='Un reggaetón muy conocido, en La menor. El reto no son las notas: es un dibujo rítmico repetido (ostinato) en la mano izquierda, agrupado 3+3+2.',
  difficult_cc='cc. 1–4', difficult_title='Ostinato sincopado 3+3+2',
  reto='que la izquierda repita su dibujo rítmico sin contagiarse del ritmo de la melodía.',
  truco='practica la izquierda sola contando en voz alta "1-2-3, 1-2-3, 1-2" hasta que sea automático.',
  sabias_que='"Despacito" (2017) fue durante mucho tiempo el vídeo más visto de la historia de YouTube, y ayudó a popularizar el reguetón a nivel mundial.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('C5', 3), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h', 'number': 1}],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=24,
)

cfg13 = dict(
  kicker='DILAN · ABRIL · DESPACITO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mim...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Despacito', song_key='La menor',
  progression_desc='Estos acordes sostienen la canción. Escribe el grado de cada uno en La menor (i, iv, v...).',
  progression=['Lam', 'Rem', 'Mim', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: el dibujo 3+3+2 en corcheas, típico del reguetón.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'e', 'beam': g} for g in [0, 0, 0, 1, 1, 1, 2, 2]] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song13)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg13)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_13_Despacito.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
