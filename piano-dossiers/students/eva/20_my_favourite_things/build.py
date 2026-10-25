import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'my-favourite-things-the-sound-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song20 = dict(
  num=20, title='My Favourite Things', subtitle='Richard Rodgers & Oscar Hammerstein II · "Sonrisas y lágrimas"',
  tonalidad='Mi menor', compas='3/4', tempo='Rápido ♩≈160', forma='Vals-estrofa',
  dificultad='Un reto de fraseo', manos='Melodía apoyada + acordes',
  la_cancion='Un vals de "Sonrisas y lágrimas", en Mi menor y muy rápido. Aquí el reto no es la velocidad: es el apoyo natural del vals, ese pequeño peso que cae en el primer tiempo de cada compás.',
  difficult_cc='cc. 1–8', difficult_title='El apoyo del vals, sin que suene golpeado',
  reto='sentir el primer tiempo de cada compás con un poquito más de peso, sin acentuarlo como un golpe.',
  truco='deja caer el peso del brazo (no de los dedos) en el primer tiempo, y "flota" en los otros dos.',
  sabias_que='"My Favourite Things" (1959) es de "The Sound of Music"; con los años se ha convertido también en un clásico de jazz, versionado por John Coltrane.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)]] +
                     [{'pitch': 'E4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mim',
  posicion_texto='Mano derecha en posición de MI menor (el 2 en el Fa#); izquierda: acordes Mim, Re, Lam y Do.',
  ritmo_texto='Ritmo: compás de 3/4 (vals), rápido — pero el apoyo se siente igual de claro rápido que despacio.',
  estudiar_steps=['Busca MI y tócala 3 veces (tu nota casa).',
                   'La melodía sola, sintiendo el apoyo al empezar cada compás.',
                   'Los acordes Mim-Re-Lam-Do con la izquierda, sin prisa.',
                   'Las dos manos juntas, con el mismo apoyo siempre en el mismo sitio.'],
  checklist_items=['Encuentro MI y pongo bien los dedos.', 'Siento el apoyo en el primer tiempo, sin golpear.',
                    'Sé los acordes Mim, Re, Lam y Do de memoria.', 'El apoyo no se pierde cuando junto las manos.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=21,
)

cfg20 = dict(
  kicker='EVA · JUNIO · MY FAVOURITE THINGS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Re, Lam, Do...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['D3', 'F#3', 'A3'], ['C3', 'E3', 'A3'], ['C3', 'E3', 'G3']],
  song_title='My Favourite Things', song_key='Mi menor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Mi menor (i, VII, VI, iv...).',
  progression=['Mim', 'Re', 'Lam', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras de vals, sintiendo el apoyo en el primer tiempo de cada compás.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q'}] * 12,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song20)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg20)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_20_My_Favourite_Things.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
