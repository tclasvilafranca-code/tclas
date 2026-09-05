import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de  Lucia_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title='Lucía', subtitle='Joan Manuel Serrat',
  tonalidad='La menor', compas='4/4', tempo='Andante ♩≈78', forma='Estrofa',
  dificultad='Nivel medio', manos='Acompañamiento en olas con matiz + melodía',
  la_cancion='Una canción de Serrat, en La menor. Hoy: el matiz que crece y decrece dentro de cada ola del acompañamiento, para que no suene siempre igual.',
  difficult_cc='cc. 1–8', difficult_title='El matiz que crece y decrece dentro de cada ola',
  reto='sentir cómo cada ola respira, subiendo un poco de volumen hacia el centro y calmándose otra vez.',
  truco='imagina que cada ola es una pequeña ola de mar: sube, y vuelve a bajar, sin golpes bruscos.',
  sabias_que='"Lucía" (1975) de Joan Manuel Serrat es una de sus canciones de amor más conocidas y versionadas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('C5', 3), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · MAYO',
  total_songs=22,
)

cfg17 = dict(
  kicker='VALENTINA · MAYO · LUCÍA (JOAN MANUEL SERRAT)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A3', 'B3'), ('A3', 'C4'), ('A3', 'D4'), ('A3', 'E4'), ('A3', 'F4'), ('A3', 'A4')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi7...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'A3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2', 'D3'], ['C3', 'E3', 'A3']],
  song_title='Lucía', song_key='La menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en La menor (i, iv, V...).',
  progression=['Lam', 'Rem', 'Mi7', 'Lam'],
  progression_mode='names',
  rhythm_desc='Lee y marca el ritmo real: la ola en corcheas, en 4/4.',
  rhythm_events=[{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A2', 'C3', 'A2', 'C3'] * 2)],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_17_Lucia.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
