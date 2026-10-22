import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'Santa-tell-me-ariana-grande.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=7, title='Santa Tell Me', subtitle='Ariana Grande',
  tonalidad='Mi menor', compas='4/4', tempo='Moderato ♩≈92', forma='Estrofa-estribillo',
  dificultad='Un reto de técnica', manos='Cruce de manos',
  la_cancion='Una canción navideña pop en Mi menor. Tiene un pasaje donde la mano izquierda salta por encima de la derecha para tocar notas agudas.',
  difficult_cc='cc. 4', difficult_title='Cruce de manos',
  reto='que la mano izquierda salte arriba con seguridad, sin dudar ni chocar con la derecha.',
  truco='practica cada mano por separado muy despacio, mirando dónde cae la izquierda antes de juntarlas.',
  sabias_que='"Santa Tell Me" (2014) fue uno de los primeros grandes éxitos navideños de Ariana Grande, y desde entonces vuelve a las listas de éxitos cada diciembre.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)]] +
                     [{'pitch': 'E4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mim',
  posicion_texto='Mano derecha en posición de MI menor (un dedo por tecla, el 2 en el Fa#); izquierda: acordes Mim, Lam y Sim.',
  ritmo_texto='Ritmo: compás de 4/4, moderato — cuenta con firmeza, sobre todo justo antes del salto de manos.',
  estudiar_steps=['Busca MI y tócala 3 veces (tu nota casa).',
                   'Practica el salto de la izquierda sola, muy despacio.',
                   'Los acordes Mim-Lam-Sim con la izquierda, uno por compás.',
                   'Las dos manos juntas: primero sin cruce, luego con el salto.'],
  checklist_items=['Encuentro MI y pongo bien los dedos.', 'Sé los acordes Mim, Lam y Sim de memoria.',
                    'Mi mano izquierda salta arriba sin dudar.', 'Junto las dos manos con el cruce, sin chocar.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=24,
)

cfg7 = dict(
  kicker='DILAN · DICIEMBRE · SANTA TELL ME',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Lam, Sim...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['A2', 'C3', 'E3'], ['B2', 'D3', 'F#3'], ['E3', 'G3', 'B3']],
  song_title='Santa Tell Me', song_key='Mi menor',
  progression_desc='Estos acordes sostienen la canción. Escribe el grado de cada uno en Mi menor (i, iv, v...).',
  progression=['Mim', 'Lam', 'Sim', 'Mim'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras firmes, con un pequeño silencio antes del salto de manos.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q'}] * 3 + [{'rest': True, 'dur': 'q'}] +
                [{'pitch': 'B4', 'dur': 'q'}] * 3 + [{'pitch': 'B4', 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song7)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg7)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_07_Santa_Tell_Me.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
