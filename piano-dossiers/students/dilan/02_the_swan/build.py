import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_worksheet_generic import build_worksheet

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'the-swan.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song2 = dict(
  num=2, title='The Swan (El Cisne)', subtitle='Camille Saint-Saëns · de "El Carnaval de los Animales"',
  tonalidad='Sol mayor', compas='3/4', tempo='Andante ♩≈96', forma='Tema con frases largas',
  dificultad='Un reto de control', manos='Melodía legato + arpegio',
  la_cancion='Una de las piezas más bellas del repertorio clásico: una melodía larga y serena que "canta" sobre un acompañamiento que fluye como el agua.',
  difficult_cc='cc. 1–8', difficult_title='El legato de verdad',
  reto='conectar cada nota con la siguiente sin cortar el sonido, sin golpes.',
  truco='imagina que la melodía es un solo movimiento continuo del brazo, sin saltos entre teclas.',
  sabias_que='Saint-Saëns compuso "El Cisne" en 1886 para "El Carnaval de los Animales", pero prohibió que se publicara en vida: temía que eclipsara el resto de su obra. No se estrenó en público hasta después de su muerte, en 1922.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('B4', 3), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  time_sig=(3, 4),
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL (un dedo por tecla); izquierda: arpegio fluido sobre Sol, Do y Re.',
  ritmo_texto='Ritmo: compás de 3/4, Andante — cuenta 1-2-3 por dentro, sin marcarlo con golpes.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: el arpegio fluido, como el agua.',
                   'Mano derecha sola, muy legato, sin levantar el dedo antes de tiempo.',
                   'Las dos manos juntas: despacio, dejando que la melodía respire.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'La izquierda fluye sin cortes.',
                    'La derecha conecta cada nota con la siguiente (legato).', 'Junto las dos manos, con calma.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · SEPTIEMBRE-OCTUBRE',
  total_songs=5,
)

cfg2 = {
 'kicker': 'DILAN · SEPTIEMBRE-OCTUBRE · THE SWAN',
 'sec1_treble': ['Sol', 'Si', 'Re', 'Sol', 'La', 'Do', 'Mi', 'Sol'],
 'sec1_bass': ['Re', 'Fa#', 'La', 'Re', 'Do', 'Mi', 'Sol', 'Re'],
 'sec2_title': 'Marca el arpegio del agua y dibuja la plica',
 'sec2_desc': 'Rodea cada grupo de tres notas (Sol-Si-Re) del arpegio fluido. Luego dibújales la plica en la dirección correcta.',
 'sec2_pitches': ['G4', 'B4', 'D5', 'G4', 'B4', 'D5', 'G4', 'B4', 'D5', 'G4', 'B4', 'D5'],
 'sec3_title': 'Colorea solo las notas SOL (tu nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de verde únicamente las que sean SOL. Las demás, déjalas en blanco.',
 'sec3_treble': ['G4', 'B4', 'D5', 'G4', 'A4', 'G4', 'C5', 'B4', 'G4', 'E4', 'D5', 'G4'],
 'sec3_bass': ['G3', 'B3', 'D4', 'G3', 'A3', 'G3', 'C4', 'B3', 'G3', 'E3', 'D4', 'G3'],
 'pista_text': 'en clave de Sol, SOL está en la segunda línea; en clave de Fa, SOL está en la primera línea, la de abajo.',
 'quiz_pitches': ['G4', 'B4', 'D5', 'A4', 'C5', 'E5', 'G4'],
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    work_path = os.path.join(HERE, '_worksheet.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song2)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(work_path, pagesize=(W, H))
    build_worksheet(c, cfg2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, work_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_02_The_Swan.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, work_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
