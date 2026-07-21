import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', ' A COMME AMOUR _ Richard Clayderman_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song4 = dict(
  num=4, title='A comme Amour', subtitle='Richard Clayderman · Paul de Senneville',
  tonalidad='Mi menor', compas='4/4', tempo='♩≈69', forma='Estrofa',
  dificultad='Para disfrutar, sin prisa', manos='Acordes sostenidos + pasillo rápido',
  la_cancion='Una pieza instrumental de Richard Clayderman en Mi menor, muy conocida y muy tranquila de fondo. Aquí trabajamos, sin prisa, un pasillo corto de notas rápidas que decora la melodía.',
  difficult_cc='cc. 1–4', difficult_title='El agua que fluye: notas rápidas, sin apretar la mano',
  reto='dejar que la mano se deslice suelta por las notas rápidas, sin apretar ni un dedo y sin ponerse nervioso.',
  truco='practica primero muy despacio, casi parado, y ve soltando la mano poco a poco: no hace falta llegar rápido hoy mismo.',
  sabias_que='"A comme Amour" (1983) de Richard Clayderman es una de sus piezas más conocidas; su nombre en francés significa "A de Amor".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('B4', 5), ('A4', 4)]] +
                     [{'pitch': 'E4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mi menor',
  posicion_texto='Mano derecha en posición de MI menor (un dedo por tecla, el 2 en Fa#); izquierda: los acordes Mim, Lam y Si (con el Re# de la sensible), sin prisa.',
  ritmo_texto='Ritmo: compás de 4/4, con un pasillo corto de notas rápidas — pero sin ninguna prisa real, solo la mano suelta.',
  estudiar_steps=['Busca MI y tócala 3 veces (tu nota casa).',
                   'El pasillo de notas rápidas, muy despacio al principio, con la mano suelta.',
                   'Los acordes Mim-Lam-Si con la izquierda, sin prisa.',
                   'Las dos manos juntas, dejando que el agua fluya sin apretar.'],
  checklist_items=['Encuentro MI y pongo bien los dedos.', 'Las notas rápidas salen sueltas, sin apretar.',
                    'Sé los acordes Mim, Lam y Si de memoria.', 'Las dos manos juntas sin ninguna tensión.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · OCTUBRE',
  total_songs=21,
)

cfg4 = dict(
  kicker='JOSÉ MARÍA · OCTUBRE · A COMME AMOUR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Lam, Si...) y di si es mayor o menor.',
  chords=[['E2', 'G2', 'B2'], ['A2', 'C3', 'E3'], ['B2', 'D#3', 'F#3'], ['E2', 'G2', 'B2']],
  song_title='A comme Amour', song_key='Mi menor',
  progression_desc='Estos son los acordes reales de la pieza. Escribe el grado de cada uno en Mi menor (i, iv, V...).',
  progression=['Mim', 'Lam', 'Si', 'Mim'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: corcheas rápidas que resuelven en notas largas, en 4/4.',
  rhythm_events=[{'pitch': 'F#4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'},
                 {'pitch': 'A4', 'dur': 'h'}, {'pitch': 'F#4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song4)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg4)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'JoseMaria_04_A_Comme_Amour.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
