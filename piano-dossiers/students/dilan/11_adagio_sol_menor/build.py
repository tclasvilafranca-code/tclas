import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'Adagio en sol menor. Albinoni.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song8 = dict(
  num=11, title='Adagio en Sol menor', subtitle='Tomaso Albinoni · adaptación para piano',
  tonalidad='Sol menor', compas='3/4', tempo='Adagio ♩≈54', forma='Frase libre (estilo barroco)',
  dificultad='Un reto de fraseo', manos='Melodía + acordes',
  la_cancion='Una pieza barroca lenta y expresiva, en Sol menor. Aquí no hay ritmo difícil: el reto es tocar con fraseo, como si cantaras cada frase.',
  difficult_cc='cc. 1–8', difficult_title='Fraseo legato: cantar con las manos',
  reto='conectar cada nota con la siguiente sin cortes, dejando que la frase respire igual que si la cantaras.',
  truco='canta la frase en voz alta antes de tocarla, y luego intenta que el piano suene tan conectado como tu voz.',
  sabias_que='"Adagio" es una indicación de tempo (muy despacio, con calma), no un título — muchas piezas barrocas se conocen solo por su tempo, dejando la expresión entera al intérprete.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('Bb4', 3), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Solm',
  posicion_texto='Mano derecha en posición de SOL menor (un dedo por tecla, el 3 en el Sib); izquierda: acordes Solm, Dom y Rem.',
  ritmo_texto='Ritmo: compás de 3/4, muy lento — cuenta con calma, dejando que cada nota suene todo lo que dura.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'Canta la frase antes de tocarla, luego tócala igual de conectada.',
                   'Los acordes Solm-Dom-Rem con la izquierda, uno por compás.',
                   'Las dos manos juntas, dejando que la frase respire.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'Toco la frase ligada, sin cortes entre notas.',
                    'Sé los acordes Solm, Dom y Rem de memoria.', 'Junto las dos manos con calma, sin prisa.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · MARZO',
  total_songs=24,
)

cfg8 = dict(
  kicker='DILAN · MARZO · ADAGIO EN SOL MENOR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Dom, Rem...) y di si es mayor o menor.',
  chords=[['G3', 'Bb3', 'D4'], ['C4', 'Eb4', 'G4'], ['D4', 'F4', 'A4'], ['G3', 'Bb3', 'D4']],
  song_title='Adagio en Sol menor', song_key='Sol menor',
  progression_desc='Estos son los acordes que sostienen la pieza. Escribe el grado de cada uno en Sol menor (i, iv, v...).',
  progression=['Solm', 'Dom', 'Rem', 'Solm'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas, con una nota final que se sostiene tres tiempos.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 6 + [{'pitch': 'D5', 'dur': 'h.'}],
  rhythm_time_sig=(3, 4),
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

    out_path = os.path.join(OUT_DIR, 'Dilan_11_Adagio_En_Sol_Menor.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
