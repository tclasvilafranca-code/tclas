import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' poema-de-amor-joan-manuel-serrat_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song19 = dict(
  num=19, title='Poema de Amor', subtitle='Joan Manuel Serrat',
  tonalidad='Sol menor', compas='4/4', tempo='Andante ♩≈80', forma='Recitado + estrofa',
  dificultad='Un reto de libertad', manos='Melodía libre + acordes',
  la_cancion='Una canción de Serrat, en Sol menor. Empieza marcada "Recitado": sin pulso fijo, como si se declamara un poema.',
  difficult_cc='cc. 1–4', difficult_title='El recitado: libertad total',
  reto='no medir el recitado con el metrónomo en la cabeza — dejar que suene como se habla.',
  truco='di la frase en voz alta primero (sin cantar, casi hablando), y luego toca imitando ese mismo fraseo libre.',
  sabias_que='Joan Manuel Serrat es célebre por poner música a poemas (Machado, Hernández...); "Poema de Amor" nace de esa misma tradición de canción-poesía.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('Bb4', 3), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Solm',
  posicion_texto='Mano derecha en posición de SOL menor (el 3 en el Sib); izquierda: acordes Solm, Re7 y Fa.',
  ritmo_texto='Ritmo: compás de 4/4, pero el recitado inicial no tiene pulso fijo — solo la estrofa entra en tempo.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'Di la frase del recitado en voz alta, casi hablando.',
                   'Los acordes Solm-Re7-Fa con la izquierda, uno por compás.',
                   'Las dos manos juntas: recitado libre, luego con pulso.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'Sé los acordes Solm, Re7 y Fa de memoria.',
                    'Mi recitado suena libre, no medido.', 'Junto las dos manos, libre y luego con pulso.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · MAYO',
  total_songs=24,
)

cfg19 = dict(
  kicker='DILAN · MAYO · POEMA DE AMOR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Re7, Fa...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['D3', 'F#3', 'C4'], ['F2', 'A2', 'C3'], ['G2', 'Bb2', 'D3']],
  song_title='Poema de Amor', song_key='Sol menor',
  progression_desc='Estos acordes sostienen la canción. Escribe el grado de cada uno en Sol menor (i, V7, VII...).',
  progression=['Solm', 'Re7', 'Solm', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: dos corcheas, negra, negra con puntillo, corchea — el dibujo del recitado.',
  rhythm_events=[{'pitch': 'D5', 'dur': d} for d in ['e', 'e', 'q', 'q.', 'e']] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song19)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg19)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_19_Poema_De_Amor.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
