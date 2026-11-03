import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'La lista de schindlers.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song13 = dict(
  num=13, title="Theme from Schindler's List", subtitle='John Williams',
  tonalidad='Sol menor', compas='4/4', tempo='Adagio ♩≈60', forma='Tema con frases largas',
  dificultad='Un reto de fraseo', manos='Frase larga + acordes',
  la_cancion='El tema de la banda sonora de John Williams, en Sol menor. Aquí el reto es el fraseo: tocar una frase entera como una sola respiración, sin cortar el sonido.',
  difficult_cc='cc. 1–8', difficult_title='La frase de una sola respiración',
  reto='mantener el sonido conectado durante toda la frase larga, sin ninguna pausa de aire.',
  truco='canta la frase entera de un tirón antes de tocarla — si no te cabe en una respiración cantando, tampoco debe sonar cortada al piano.',
  sabias_que='El violinista Itzhak Perlman grabó el solo original de la película; esta versión de piano conserva la misma melodía larga y expresiva.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol menor',
  posicion_texto='Mano derecha en posición de SOL menor (el 3 en la tecla negra Sib); izquierda: los acordes Solm, Dom y Rem.',
  ritmo_texto='Ritmo: compás de 4/4, Adagio — deja que cada frase fluya sin cortes, como una sola respiración larga.',
  estudiar_steps=['Busca SOL menor y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: los acordes, sosteniendo el sonido.',
                   'Mano derecha sola: la frase entera, cantándola primero.',
                   'Las dos manos juntas: sin cortar el sonido en ningún momento.'],
  checklist_items=['Encuentro SOL menor y pongo bien los dedos.', 'Toco la frase entera sin cortar el sonido.',
                    'No hago pausas de aire donde no tocan.', 'Las dos manos suenan como una sola respiración.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=21,
)

cfg13 = dict(
  kicker='EVA · ABRIL · SCHINDLER’S LIST',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Dom, Rem...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['D3', 'F3', 'A3'], ['C3', 'Eb3', 'G3'], ['G2', 'Bb2', 'D3']],
  song_title="Theme from Schindler's List", song_key='Sol menor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Sol menor (i, iv, v...).',
  progression=['Solm', 'Rem', 'Dom', 'Rem', 'Solm', 'Dom', 'Rem', 'Solm'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la frase: negras que fluyen sin cortes, en 4/4.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song13)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg13)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_13_Schindlers_List.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
