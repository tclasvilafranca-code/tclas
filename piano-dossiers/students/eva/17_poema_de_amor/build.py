import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' poema-de-amor-joan-manuel-serrat_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title='Poema de Amor', subtitle='Joan Manuel Serrat',
  tonalidad='Sol menor', compas='4/4', tempo='Libre ♩≈66', forma='Estrofa recitada',
  dificultad='Un reto de carácter', manos='Articulación contrastada',
  la_cancion='Una canción de Serrat en Sol menor. Aquí el reto es de carácter: frases ligadas y cantadas se alternan con frases marcadas y casi declamadas.',
  difficult_cc='cc. 1–8', difficult_title='Ligado contra marcado',
  reto='cambiar de articulación de una frase a otra sin que suene igual todo el rato.',
  truco='decide antes de tocar si esa frase "se canta" (ligada) o "se dice" (marcada), y exagéralo un poco al principio.',
  sabias_que='Joan Manuel Serrat es conocido por musicar poemas de Antonio Machado y Miguel Hernández; sus propias canciones también tienen ese aire de poema recitado.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol menor',
  posicion_texto='Mano derecha en posición de SOL menor (el 3 en la tecla negra Sib); izquierda: los acordes Solm, Fa y Re7.',
  ritmo_texto='Ritmo: compás de 4/4, libre — el carácter cambia entre lo ligado y lo marcado según la letra.',
  estudiar_steps=['Busca SOL menor y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: los acordes, con el Re7 sonando "de dominante".',
                   'Mano derecha sola: la misma frase ligada y luego marcada.',
                   'Las dos manos juntas: cambia de carácter según lo pida la frase.'],
  checklist_items=['Encuentro SOL menor y pongo bien los dedos.', 'Distingo claramente lo ligado de lo marcado.',
                    'No toco todo con el mismo carácter.', 'Las dos manos cambian de carácter juntas.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · MAYO',
  total_songs=21,
)

cfg17 = dict(
  kicker='EVA · MAYO · POEMA DE AMOR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Fa, Re7...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['F2', 'A2', 'C3'], ['D3', 'F#3', 'C4'], ['G2', 'Bb2', 'D3']],
  song_title='Poema de Amor', song_key='Sol menor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Sol menor (i, VI, V7...).',
  progression=['Solm', 'Fa', 'Re7', 'Solm', 'Fa', 'Re7', 'Solm', 'Fa'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras que alternan carácter ligado y marcado.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_17_Poema_De_Amor.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
