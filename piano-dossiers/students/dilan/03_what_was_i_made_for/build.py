import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_worksheet_generic import build_worksheet

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'what-was-i-made-for-billie-eilish.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song3 = dict(
  num=3, title='What Was I Made For?', subtitle='Billie Eilish · de la película "Barbie" (2023)',
  tonalidad='Do mayor', compas='4/4', tempo='Lento ♩≈78', forma='Estrofa',
  dificultad='Fácil, con oído', manos='Melodía + acordes largos',
  la_cancion='Una balada muy desnuda: pocas notas, mucho silencio, y una pregunta que se queda en el aire. Ideal para cantar mientras tocas.',
  difficult_cc='cc. 1–2', difficult_title='Contar el silencio y entrar a tiempo',
  reto='contar los compases vacíos por dentro y entrar en el momento exacto, sin adelantarte.',
  truco='cuenta "1-2-3-4" en voz baja en cada compás de silencio, como si ya estuvieras tocando.',
  sabias_que='Billie Eilish escribió esta canción con su hermano Finneas para la película "Barbie" (2023). Ganó el Oscar a la Mejor Canción Original en 2024.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · OCTUBRE',
  total_songs=5,
)

cfg3 = {
 'kicker': 'DILAN · OCTUBRE · WHAT WAS I MADE FOR?',
 'sec1_treble': ['Do', 'Mi', 'Sol', 'Do', 'Re', 'Fa', 'La', 'Do'],
 'sec1_bass': ['Sol', 'Si', 'Re', 'Sol', 'La', 'Do', 'Mi', 'Sol'],
 'sec2_title': 'Marca dónde hay un compás de silencio',
 'sec2_desc': 'Con una X, marca en el aire debajo de la línea dónde crees que iría un compás de silencio en este patrón. Luego dibuja la plica de las notas.',
 'sec2_pitches': ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4'],
 'sec3_title': 'Colorea solo las notas DO (tu nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de azul únicamente las que sean DO. Las demás, déjalas en blanco.',
 'sec3_treble': ['C4', 'E4', 'G4', 'C4', 'D4', 'C4', 'F4', 'E4', 'C4', 'A4', 'G4', 'C4'],
 'sec3_bass': ['C3', 'E3', 'G3', 'C3', 'D3', 'C3', 'F3', 'E3', 'C3', 'A3', 'G3', 'C3'],
 'pista_text': 'en clave de Sol, DO está en la primera línea adicional bajo el pentagrama (con su rayita); en clave de Fa, DO está en el segundo espacio.',
 'quiz_pitches': ['C4', 'E4', 'G4', 'D4', 'F4', 'A4', 'C4'],
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    work_path = os.path.join(HERE, '_worksheet.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song3)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(work_path, pagesize=(W, H))
    build_worksheet(c, cfg3)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, work_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_03_What_Was_I_Made_For.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, work_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
