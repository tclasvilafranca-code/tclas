import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'La lista de schindlers.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song15 = dict(
  num=15, title="Theme from Schindler's List", subtitle='John Williams',
  tonalidad='Sol menor', compas='4/4', tempo='Expresivo ♩≈66', forma='Tema con variaciones',
  dificultad='Un reto expresivo', manos='Melodía + acordes',
  la_cancion='El tema principal de la banda sonora de "La lista de Schindler", en Sol menor. Vive del regulador: crecer y apagarse dentro de una misma frase.',
  difficult_cc='cc. 1–8', difficult_title='El regulador dentro de la frase',
  reto='que la frase crezca y se apague sola, sin golpes de volumen bruscos.',
  truco='dibuja con la mano en el aire la forma de una ola mientras tocas: sube con el crescendo, baja con el diminuendo.',
  sabias_que='John Williams compuso este tema para el violinista Itzhak Perlman en la película de 1993; ganó el Oscar a la Mejor Banda Sonora ese mismo año.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('Bb4', 3), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Solm',
  posicion_texto='Mano derecha en posición de SOL menor (el 3 en el Sib); izquierda: acordes Solm, Rem y Dom.',
  ritmo_texto='Ritmo: compás de 4/4, expresivo — sin metrónomo estricto, dejando que la frase respire.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'La frase sola, dibujando el crescendo-diminuendo en el aire.',
                   'Los acordes Solm-Rem-Dom con la izquierda, uno por compás.',
                   'Las dos manos juntas, dejando que el regulador mande.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'Sé los acordes Solm, Rem y Dom de memoria.',
                    'Mi frase crece y se apaga sin golpes bruscos.', 'Junto las dos manos con el regulador.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=24,
)

cfg15 = dict(
  kicker="DILAN · ABRIL · THEME FROM SCHINDLER'S LIST",
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Rem, Dom...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['D3', 'F3', 'A3'], ['C3', 'Eb3', 'G3'], ['G2', 'Bb2', 'D3']],
  song_title="Theme from Schindler's List", song_key='Sol menor',
  progression_desc='Estos acordes sostienen el tema. Escribe el grado de cada uno en Sol menor (i, iv, v...).',
  progression=['Solm', 'Rem', 'Dom', 'Solm'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas, con una nota final que se sostiene.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'q'}] * 6 + [{'pitch': 'D4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song15)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg15)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_15_Schindlers_List.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
