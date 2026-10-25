import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'bella-ciao-piano-four-hands-easy-version.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song8 = dict(
  num=8, title='Bella Ciao', subtitle='Tradicional italiana (a 4 manos)',
  tonalidad='Sol menor', compas='4/4', tempo='♩≈100', forma='Estrofa',
  dificultad='Un reto de contratiempo', manos='Acompañamiento a contratiempo + melodía',
  la_cancion='Una canción popular italiana en Sol menor, pensada para tocar a 4 manos. El reto es rítmico: el acompañamiento no toca en el tiempo, sino en el hueco de después, como un rasgueo de guitarra.',
  difficult_cc='cc. 1–8', difficult_title='El contratiempo: entre los pulsos',
  reto='que el acorde caiga siempre en el mismo hueco, ni antes ni después, sin apoyarse en el tiempo fuerte.',
  truco='marca el pulso con el pie y toca el acorde justo cuando el pie sube, no cuando baja.',
  sabias_que='"Bella Ciao" era un canto de protesta popular italiano que se convirtió en símbolo internacional de resistencia durante el siglo XX.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol menor',
  posicion_texto='Mano derecha en posición de SOL menor (el 3 en la tecla negra Sib); izquierda: los acordes Solm, Dom y Re, en contratiempo.',
  ritmo_texto='Ritmo: compás de 4/4 — el acompañamiento suena siempre entre los pulsos, nunca encima.',
  estudiar_steps=['Busca SOL menor y tócala 3 veces (tu nota casa).',
                   'El contratiempo solo, contando el silencio con precisión.',
                   'La melodía sola, sintiendo dónde está el pulso de verdad.',
                   'Las dos manos juntas, sin que el contratiempo se adelante.'],
  checklist_items=['Encuentro SOL menor y pongo bien los dedos.', 'El acorde cae siempre en el mismo hueco.',
                    'Sé los acordes Solm, Dom y Re de memoria.', 'El contratiempo no se adelanta al juntar las manos.'],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=22,
)

cfg8 = dict(
  kicker='JOSEP · DICIEMBRE · BELLA CIAO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Dom, Re...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['C3', 'Eb3', 'G3'], ['D3', 'F#3', 'A3'], ['G2', 'Bb2', 'D3']],
  song_title='Bella Ciao', song_key='Sol menor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Sol menor (i, iv, V...).',
  progression=['Solm', 'Dom', 'Re', 'Solm'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real del acompañamiento: silencio-acorde-silencio-acorde, en 4/4.',
  rhythm_events=[{'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song8)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg8)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_08_Bella_Ciao.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
