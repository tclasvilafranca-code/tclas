import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_worksheet_generic import build_worksheet

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' cant-help-falling-in-love-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title="Can't Help Falling in Love", subtitle='Elvis Presley · arr. Seb Alejandro',
  tonalidad='Re mayor', compas='3/4', tempo='Balada lenta ♩≈72', forma='Estrofa',
  dificultad='Fácil, con su punto', manos='Melodía + arpegio',
  la_cancion='Una balada lenta de Elvis Presley, ideal para cantar mientras tocas. La izquierda mece un arpegio de vals sin parar mientras la derecha canta.',
  difficult_cc='cc. 1–4', difficult_title='El arpegio de vals sin parar',
  reto='mantener el péndulo de la izquierda fluido mientras la derecha sostiene notas largas.',
  truco='aprende el dibujo de la izquierda solo, como un bucle automático, antes de añadir la melodía.',
  sabias_que='La melodía viene de "Plaisir d\'Amour" (1784), una antigua canción francesa. Elvis Presley la adaptó en 1961 para la película "Blue Hawaii".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('F#4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  time_sig=(3, 4),
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE (un dedo por tecla, el 3 en el Fa#); izquierda: arpegio de vals sobre Re, Sol y La.',
  ritmo_texto='Ritmo: compás de 3/4, un vals lento — cuenta 1-2-3 por dentro mientras la melodía sostiene la nota.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola, muy despacio, sintiendo el péndulo del vals.',
                   'Mano derecha sola: las notas largas, contando 1-2-3 por dentro.',
                   'Las dos manos juntas: lento primero, dejando que la izquierda fluya sola.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'La izquierda mece el vals sin pararse.',
                    'La derecha sostiene cada nota larga sin cortarla.', 'Junto las dos manos, tranquilo.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · SEPTIEMBRE',
  total_songs=5,
)

cfg1 = {
 'kicker': 'DILAN · SEPTIEMBRE · CAN’T HELP FALLING IN LOVE',
 'sec1_treble': ['Re', 'Fa#', 'La', 'Re', 'Mi', 'Sol', 'Si', 'Re'],
 'sec1_bass': ['La', 'Fa#', 'Re', 'La', 'Sol', 'Mi', 'Do#', 'La'],
 'sec2_title': 'Marca el arpegio del vals y dibuja la plica',
 'sec2_desc': 'Rodea cada grupo de tres notas (Re-Fa#-La) del arpegio. Luego dibújales la plica en la dirección correcta.',
 'sec2_pitches': ['D4', 'F#4', 'A4', 'D4', 'F#4', 'A4', 'D4', 'F#4', 'A4', 'D4', 'F#4', 'A4'],
 'sec3_title': 'Colorea solo las notas RE (tu nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de azul únicamente las que sean RE. Las demás, déjalas en blanco.',
 'sec3_treble': ['D4', 'F#4', 'A4', 'D4', 'E4', 'D4', 'G4', 'F#4', 'D4', 'B4', 'A4', 'D4'],
 'sec3_bass': ['D3', 'F#3', 'A3', 'D3', 'E3', 'D3', 'G3', 'F#3', 'D3', 'B3', 'A3', 'D3'],
 'pista_text': 'en clave de Sol, RE está justo debajo de la primera línea (sin rayita); en clave de Fa, RE está en la tercera línea, la del medio.',
 'quiz_pitches': ['D4', 'F#4', 'A4', 'E4', 'G4', 'B4', 'D4'],
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    work_path = os.path.join(HERE, '_worksheet.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song1)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(work_path, pagesize=(W, H))
    build_worksheet(c, cfg1)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, work_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_01_Cant_Help_Falling_In_Love.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, work_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
