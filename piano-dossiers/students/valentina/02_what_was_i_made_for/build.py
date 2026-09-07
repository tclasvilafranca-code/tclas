import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de what-was-i-made-for-billie-eilish.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song2 = dict(
  num=2, title='What Was I Made For?', subtitle='Billie Eilish · de la película "Barbie" (2023)',
  tonalidad='Do mayor', compas='4/4', tempo='Lento ♩≈78', forma='Estrofa',
  dificultad='Nivel medio', manos='Melodía + acordes con séptima',
  la_cancion='Una balada muy desnuda de Billie Eilish. Hoy: acordes con séptima, un color más denso bajo la melodía, algo más avanzado que un acorde simple.',
  difficult_cc='cc. 1–4', difficult_title='Acordes con séptima: un color más denso bajo la melodía',
  reto='reconocer y sostener el acorde de séptima entero, sin simplificarlo a la tríada de siempre.',
  truco='toca primero la tríada sola, luego añade la 4ª nota encima: escucha cómo cambia el color.',
  sabias_que='Billie Eilish escribió esta canción con su hermano Finneas para la película "Barbie" (2023). Ganó el Oscar a la Mejor Canción Original en 2024.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · SEPTIEMBRE',
  total_songs=22,
)

cfg2 = dict(
  kicker='VALENTINA · SEPTIEMBRE · WHAT WAS I MADE FOR?',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es una tríada o tiene séptima.',
  chords=[['C3', 'E3', 'G3'], ['C3', 'E3', 'G3', 'B3'], ['F2', 'A2', 'C3', 'E3'], ['G2', 'B2', 'D3', 'F3']],
  song_title='What Was I Made For?', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas largas sobre acordes densos, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'w'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song2)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_02_What_Was_I_Made_For.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
