import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'my-favourite-things-the-sound-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song22 = dict(
  num=22, title='My Favourite Things', subtitle='Richard Rodgers & Oscar Hammerstein II · "Sonrisas y lágrimas"',
  tonalidad='Mi menor', compas='3/4', tempo='Rápido ♩≈160', forma='Vals-estrofa',
  dificultad='Un reto de método', manos='Melodía + acordes',
  la_cancion='Un vals de "Sonrisas y lágrimas", en Mi menor y muy rápido. El reto no es una técnica concreta: es un método de estudio.',
  difficult_cc='cc. 1–8', difficult_title='Subir la velocidad poco a poco',
  reto='no intentar tocarlo rápido a la primera — la velocidad se construye en pasos.',
  truco='aprende cada frase a ♩≈80, y solo cuando salga sin fallos, sube 10-15 de metrónomo. Repite hasta llegar a ♩≈160.',
  sabias_que='"My Favourite Things" (1959) es de el musical "The Sound of Music"; con los años se ha convertido también en un clásico de jazz, versionado por John Coltrane.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)]] +
                     [{'pitch': 'E4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mim',
  posicion_texto='Mano derecha en posición de MI menor (el 2 en el Fa#); izquierda: acordes Mim, Do, Lam y Re.',
  ritmo_texto='Ritmo: compás de 3/4 (vals), rápido — practica siempre más despacio de lo que crees necesario.',
  estudiar_steps=['Busca MI y tócala 3 veces (tu nota casa).',
                   'La frase de la melodía a ♩≈80, muy controlada.',
                   'Los acordes Mim-Do-Lam-Re con la izquierda, uno por compás.',
                   'Las dos manos juntas, subiendo la velocidad solo paso a paso.'],
  checklist_items=['Encuentro MI y pongo bien los dedos.', 'Sé tocar la frase despacio sin ningún fallo.',
                    'Sé los acordes Mim, Do, Lam y Re de memoria.', 'Subo la velocidad solo cuando ya sale limpio.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=24,
)

cfg22 = dict(
  kicker='DILAN · JUNIO · MY FAVOURITE THINGS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Do, Lam, Re...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['C3', 'E3', 'G3'], ['C3', 'E3', 'A3'], ['D3', 'F#3', 'A3']],
  song_title='My Favourite Things', song_key='Mi menor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Mi menor (i, VI, iv, VII...).',
  progression=['Mim', 'Do', 'Lam', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras de vals, tres por compás.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q'}] * 12,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song22)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg22)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_22_My_Favourite_Things.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
