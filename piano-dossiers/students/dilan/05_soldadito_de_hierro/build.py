import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_worksheet_generic import build_worksheet

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' SOLDADITO DE HIERRO _ Nil Moliner_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song5 = dict(
  num=5, title='Soldadito de Hierro', subtitle='Nil Moliner · arr. Campamento Musical Bye Bye Beethoven',
  tonalidad='Do mayor', compas='4/4', tempo='Enérgico ♩≈84', forma='Estrofa',
  dificultad='Un reto rítmico ligero', manos='Melodía + acordes',
  la_cancion='Una canción española muy rítmica: la mano derecha se mueve en grupos de tres notas, ligera y rápida, mientras la izquierda descansa en acordes largos.',
  difficult_cc='cc. 1–4', difficult_title='Grupos de tres, ligeros y rápidos',
  reto='mover los grupos de tres con ligereza, sin que se atropellen ni se frenen.',
  truco='practica cada grupo de tres muy despacio, como un giro pequeño de la muñeca, y ve acelerando poco a poco.',
  sabias_que='"Soldadito de Hierro" es del cantautor español Nil Moliner. Esta versión para piano forma parte del repertorio del Campamento Musical Bye Bye Beethoven.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · NOVIEMBRE',
  total_songs=5,
)

cfg5 = {
 'kicker': 'DILAN · NOVIEMBRE · SOLDADITO DE HIERRO',
 'sec1_treble': ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do'],
 'sec1_bass': ['Sol', 'Fa', 'Mi', 'Re', 'Do', 'Si', 'La', 'Sol'],
 'sec2_title': 'Marca cada grupo de tres y dibuja la plica',
 'sec2_desc': 'Rodea cada grupo de tres notas seguidas. Luego dibújales la plica en la dirección correcta.',
 'sec2_pitches': ['C4', 'D4', 'E4', 'C4', 'D4', 'E4', 'E4', 'F4', 'G4', 'E4', 'F4', 'G4'],
 'sec3_title': 'Colorea solo las notas DO (tu nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de rojo únicamente las que sean DO. Las demás, déjalas en blanco.',
 'sec3_treble': ['C4', 'D4', 'E4', 'C4', 'G4', 'C4', 'A4', 'F4', 'C4', 'E4', 'D4', 'C4'],
 'sec3_bass': ['C3', 'D3', 'E3', 'C3', 'G3', 'C3', 'A3', 'F3', 'C3', 'E3', 'D3', 'C3'],
 'pista_text': 'en clave de Sol, DO está en la primera línea adicional bajo el pentagrama (con su rayita); en clave de Fa, DO está en el segundo espacio.',
 'quiz_pitches': ['C4', 'D4', 'E4', 'F4', 'G4', 'B4', 'C4'],
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    work_path = os.path.join(HERE, '_worksheet.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song5)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(work_path, pagesize=(W, H))
    build_worksheet(c, cfg5)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, work_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_05_Soldadito_De_Hierro.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, work_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
