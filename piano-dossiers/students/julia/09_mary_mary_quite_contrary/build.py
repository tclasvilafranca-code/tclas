import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', 'Mary Mary Quite Contrary.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title='Mary Mary Quite Contrary', subtitle='Traditional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='2/4', tempo='Alegre', forma='Estrofa',
  dificultad='Nivel inicial', manos='Compás cortito + acordes',
  la_cancion='Una canción tradicional inglesa en Fa mayor. Hoy el compás es cortito: solo dos tiempos, hay que contar rápido sin perder ninguno.',
  difficult_cc='cc. 1–4', difficult_title='El compás cortito: solo dos tiempos',
  reto='contar "1-2, 1-2" con firmeza, sin dejar que el compás corto te pille por sorpresa.',
  truco='da un golpecito con el pie en cada compás nuevo, para sentir cuándo empieza cada uno.',
  sabias_que='"Mary Mary Quite Contrary" es una antigua rima infantil inglesa que aparece en libros de canciones desde el siglo XVIII.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2)]],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA mayor (un dedo por tecla); izquierda: los acordes Fa, Sib y Do.',
  ritmo_texto='Ritmo: compás de 2/4, cortito — cuenta rápido "1-2, 1-2".',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'El compás cortito, contando "1-2" en voz alta.',
                   'Los acordes Fa-Sib-Do con la izquierda.',
                   'Las dos manos juntas, sin perder ningún compás.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Cuento "1-2" sin perderme.',
                    'Sé los acordes Fa, Sib y Do de memoria.', 'Las dos manos juntas suenan seguras.'],
  nivel_kicker='JULIA · NIVEL INICIAL · NOVIEMBRE',
  total_songs=24,
)

cfg9 = dict(
  kicker='JULIA · NOVIEMBRE · MARY MARY QUITE CONTRARY',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Mary Mary Quite Contrary', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el compás cortito de dos tiempos, en 2/4.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song9)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg9)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Julia_09_Mary_Mary_Quite_Contrary.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
