import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'NEL', '- A COMME AMOUR _ Richard Clayderman_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song12 = dict(
  num=12, title='A comme Amour', subtitle='Richard Clayderman · Paul de Senneville',
  tonalidad='Mi menor', compas='4/4', tempo='♩≈69', forma='Estrofa',
  dificultad='Un reto de precisión', manos='Acordes sostenidos + arpegio rápido',
  la_cancion='Una pieza instrumental de Richard Clayderman en Mi menor. El reto es de precisión: un arpegio corto y rápido tiene que aterrizar exactamente sobre el pulso.',
  difficult_cc='cc. 1–4', difficult_title='La carrera que aterriza justo en el tiempo',
  reto='que el arpegio caiga exactamente sobre el pulso, sin adelantarse ni atrasarse.',
  truco='cuenta en voz alta mientras tocas el arpegio, muy despacio al principio, hasta clavar la caída sobre el tiempo.',
  sabias_que='"A comme Amour" (1983) de Richard Clayderman es una de sus piezas más conocidas; su nombre en francés significa "A de Amor".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('G4', 3), ('F#4', 2), ('A4', 4), ('G4', 3), ('B4', 5)]] +
                     [{'pitch': 'E4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mi menor',
  posicion_texto='Mano derecha en posición de MI menor (un dedo por tecla, el 2 en Fa#); izquierda: los acordes Mim, Si y Lam (con el Re# de la sensible).',
  ritmo_texto='Ritmo: compás de 4/4, con un arpegio corto y rápido que aterriza justo sobre el pulso.',
  estudiar_steps=['Busca MI y tócala 3 veces (tu nota casa).',
                   'El arpegio rápido, muy despacio al principio, contando en voz alta.',
                   'Los acordes Mim-Si-Lam con la izquierda.',
                   'Las dos manos juntas, con el arpegio cayendo siempre en su sitio.'],
  checklist_items=['Encuentro MI y pongo bien los dedos.', 'El arpegio aterriza justo sobre el pulso.',
                    'Sé los acordes Mim, Si y Lam de memoria.', 'Las dos manos juntas sin que el pulso tiemble.'],
  nivel_kicker='NEL · NIVEL MEDIO-ALTO · MARZO',
  total_songs=22,
)

cfg12 = dict(
  kicker='NEL · MARZO · A COMME AMOUR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Si, Lam...) y di si es mayor o menor.',
  chords=[['E2', 'G2', 'B2'], ['B2', 'D#3', 'F#3'], ['A2', 'C3', 'E3'], ['E2', 'G2', 'B2']],
  song_title='A comme Amour', song_key='Mi menor',
  progression_desc='Estos son los acordes reales de la pieza. Escribe el grado de cada uno en Mi menor (i, iv, V...).',
  progression=['Mim', 'Si', 'Lam', 'Mim'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: arpegio en corcheas que resuelve en notas largas, en 4/4.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'e'}, {'pitch': 'B4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'},
                 {'pitch': 'B4', 'dur': 'h'}, {'pitch': 'E4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song12)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg12)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Nel_12_A_Comme_Amour.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
