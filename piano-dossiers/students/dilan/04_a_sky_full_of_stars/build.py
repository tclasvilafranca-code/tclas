import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_worksheet_generic import build_worksheet

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' a-sky-full-of-stars-coldplay.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song4 = dict(
  num=4, title='A Sky Full of Stars', subtitle='Coldplay · con Avicii',
  tonalidad='Fa mayor', compas='4/4', tempo='Enérgico ♩≈100', forma='Estribillo repetido',
  dificultad='Un reto rítmico', manos='Acordes rítmicos, manos juntas',
  la_cancion='Un himno pop-electrónico de Coldplay. Las dos manos golpean el mismo pulso "largo-corto" a la vez, como un solo instrumento.',
  difficult_cc='cc. 1–4', difficult_title='El pulso largo-corto firme',
  reto='mantener el pulso largo-corto exacto en las dos manos a la vez, sin acelerar.',
  truco='cuenta "larga-y-corta" muy despacio antes de tocarlo, sintiendo dónde cae la nota corta.',
  sabias_que='Coldplay grabó esta canción junto al DJ y productor Avicii en 2014, mezclando el rock de la banda con sonido electrónico de baile.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA (un dedo por tecla, el 4 en el Sib); izquierda: acordes Fa, Sib y Do con el pulso largo-corto.',
  ritmo_texto='Ritmo: compás de 4/4, enérgico — el pulso largo-corto (negra con puntillo + corchea) se repite todo el rato.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: el pulso largo-corto, muy despacio.',
                   'Mano derecha sola: los acordes con el mismo pulso.',
                   'Las dos manos juntas: como un solo instrumento, sin acelerar.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'El pulso largo-corto suena firme.',
                    'Toco el Sib con el dedo 4 sin fallar.', 'Las dos manos golpean juntas, a la vez.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · OCTUBRE',
  total_songs=5,
)

cfg4 = {
 'kicker': 'DILAN · OCTUBRE · A SKY FULL OF STARS',
 'sec1_treble': ['Fa', 'La', 'Do', 'Fa', 'Sol', 'Sib', 'Re', 'Fa'],
 'sec1_bass': ['Do', 'Mi', 'Sol', 'Do', 'Sib', 'Re', 'Fa', 'Do'],
 'sec2_title': 'Marca el pulso largo-corto y dibuja la plica',
 'sec2_desc': 'Rodea cada pareja de notas (larga-corta) del pulso. Luego dibújales la plica en la dirección correcta.',
 'sec2_pitches': ['F4', 'F4', 'Bb4', 'Bb4', 'C5', 'C5', 'F4', 'F4', 'Bb4', 'Bb4', 'C5', 'C5'],
 'sec3_title': 'Colorea solo las notas FA (tu nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de naranja únicamente las que sean FA. Las demás, déjalas en blanco.',
 'sec3_treble': ['F4', 'A4', 'C5', 'F4', 'Bb4', 'F4', 'G4', 'A4', 'F4', 'D5', 'C5', 'F4'],
 'sec3_bass': ['F3', 'A3', 'C4', 'F3', 'Bb3', 'F3', 'G3', 'A3', 'F3', 'D4', 'C4', 'F3'],
 'pista_text': 'en clave de Sol, FA está en el primer espacio; en clave de Fa, FA está en la cuarta línea.',
 'quiz_pitches': ['F4', 'A4', 'C5', 'G4', 'Bb4', 'D5', 'F4'],
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    work_path = os.path.join(HERE, '_worksheet.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song4)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(work_path, pagesize=(W, H))
    build_worksheet(c, cfg4)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, work_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_04_A_Sky_Full_Of_Stars.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, work_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
