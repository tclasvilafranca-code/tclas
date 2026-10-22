import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'Santa-tell-me-ariana-grande.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=7, title='Santa Tell Me', subtitle='Ariana Grande',
  tonalidad='Mi menor', compas='4/4', tempo='Pop ♩≈100', forma='Estrofa-estribillo',
  dificultad='Un reto de estilo', manos='Melodía sincopada + acordes',
  la_cancion='Una canción navideña de Ariana Grande en Mi menor. Aquí el reto es de estilo: la síncopa pop, notas que llegan un poquito antes de lo que el oído espera.',
  difficult_cc='cc. 1–8', difficult_title='La síncopa: adelantarse al pulso',
  reto='sentir dónde "debería" caer la nota y adelantarla justo lo necesario, sin descuadrar el resto.',
  truco='cuenta las corcheas en voz alta (1-y-2-y-3-y-4-y) y entra siempre en el "y", nunca en el número.',
  sabias_que='Ariana Grande escribió "Santa Tell Me" en 2014 cuando tenía solo 21 años; se ha convertido en un clásico navideño moderno con cientos de millones de reproducciones cada diciembre.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('B4', 5), ('A4', 4)]] +
                     [{'pitch': 'E4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mi menor',
  posicion_texto='Mano derecha en posición de MI menor (el 2 en la tecla negra Fa#); izquierda: los acordes Mim, Lam y Sim.',
  ritmo_texto='Ritmo: compás de 4/4, con síncopa — las notas se adelantan al pulso, típico del pop.',
  estudiar_steps=['Busca MI menor y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: los acordes, marcando el pulso exacto.',
                   'Mano derecha sola: la síncopa, contando "1-y-2-y" en voz alta.',
                   'Las dos manos juntas: el pulso firme abajo, la síncopa suelta arriba.'],
  checklist_items=['Encuentro MI menor y pongo bien los dedos.', 'Siento dónde se adelanta la nota sincopada.',
                    'La izquierda no se contagia de la síncopa de la derecha.', 'Las dos manos suenan con soltura pop.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=21,
)

cfg7 = dict(
  kicker='EVA · DICIEMBRE · SANTA TELL ME',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Lam, Sim...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['A2', 'C3', 'E3'], ['B2', 'D3', 'F#3'], ['E3', 'G3', 'B3']],
  song_title='Santa Tell Me', song_key='Mi menor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Mi menor (i, iv, v...).',
  progression=['Mim', 'Sim', 'Lam', 'Sim', 'Mim', 'Lam', 'Sim', 'Mim'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la melodía: corcheas sincopadas, adelantadas al pulso.',
  rhythm_events=[{'rest': True, 'dur': 'e'}, {'pitch': 'B4', 'dur': 'q.'}] * 4,
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

    out_path = os.path.join(OUT_DIR, 'Eva_07_Santa_Tell_Me.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
