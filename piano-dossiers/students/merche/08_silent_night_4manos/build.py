import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', ' silent-night-4-hands_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song8 = dict(
  num=8, title='Silent Night', subtitle='Villancico tradicional · a 4 manos',
  tonalidad='Do mayor', compas='3/4', tempo='Tranquilo', forma='Estrofa antifonal (a 4 manos)',
  dificultad='Nivel básico', manos='Melodía por turnos + acorde sostenido, a 4 manos',
  la_cancion='El villancico "Noche de Paz", en Do mayor, a cuatro manos. La melodía se turna entre las dos partes: mientras una canta, la otra guarda silencio, y luego se intercambian.',
  difficult_cc='cc. 1–8', difficult_title='El turno que se pasa: entrar después del silencio del otro',
  reto='entrar con seguridad justo cuando llega tu turno de melodía, después de contar el silencio de espera.',
  truco='mientras esperas tu turno, sigue contando los tres tiempos de cada compás en voz baja, sin perder la cuenta.',
  sabias_que='"Noche de Paz" (Stille Nacht) fue compuesta en 1818 por Franz Xaver Gruber para una parroquia austríaca, y hoy se canta en más de 300 idiomas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · NOVIEMBRE',
  total_songs=28,
)

cfg8 = dict(
  kicker='MERCÈ · NOVIEMBRE · SILENT NIGHT (A 4 MANOS)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Silent Night (4 manos)', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el turno de melodía y el silencio de espera, en 3/4.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'},
                 {'rest': True, 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}],
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song8)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg8)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_08_Silent_Night_4manos.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
