import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' SOLDADITO DE HIERRO _ Nil Moliner_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song5 = dict(
  num=5, title='Soldadito de Hierro', subtitle='Nil Moliner · arr. Campamento Musical Bye Bye Beethoven',
  tonalidad='La menor', compas='4/4', tempo='Enérgico ♩≈84', forma='Estrofa',
  dificultad='Un reto rítmico ligero', manos='Melodía + acordes',
  la_cancion='Una canción española muy rítmica, en La menor: la mano derecha se mueve en grupos de tres notas, ligera y rápida, mientras la izquierda sostiene acordes largos.',
  difficult_cc='cc. 1–4', difficult_title='Grupos de tres, ligeros y rápidos',
  reto='mover los grupos de tres con ligereza, sin que se atropellen ni se frenen.',
  truco='practica cada grupo de tres muy despacio, como un giro pequeño de la muñeca, y ve acelerando poco a poco.',
  sabias_que='"Soldadito de Hierro" es del cantautor español Nil Moliner. La armadura no lleva alteraciones, pero la armonía real (Lam-Rem-Mi7-Lam) confirma que está en La menor, no en Do mayor: la misma armadura puede pertenecer a dos tonalidades relativas distintas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('E5', 5), ('D5', 4)]] +
                     [{'pitch': 'C5', 'dur': 'h', 'number': 3}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Lam',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: acordes Lam, Rem y Mi7 (el V7 lleva Sol sostenido).',
  ritmo_texto='Ritmo: compás de 4/4, enérgico — los grupos de tres notas se mueven ligeros dentro de cada tiempo.',
  estudiar_steps=['Busca LA y tócala 3 veces (tu nota casa).',
                   'Mano derecha sola: los grupos de tres, muy despacio al principio.',
                   'Acordes Lam-Rem-Mi7 con la izquierda, uno por compás.',
                   'Las dos manos juntas: lento primero, luego un poco más rápido.'],
  checklist_items=['Encuentro LA y pongo bien los dedos.', 'Los grupos de tres suenan ligeros, no atropellados.',
                    'Toco el Mi7 con el Sol sostenido, sin fallar.', 'Junto las dos manos con precisión.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · NOVIEMBRE',
  total_songs=24,
)

cfg5 = dict(
  kicker='DILAN · NOVIEMBRE · SOLDADITO DE HIERRO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi, Do...) y di si es mayor o menor.',
  chords=[['A4', 'C5', 'E5'], ['D4', 'F4', 'A4'], ['E4', 'G#4', 'B4'], ['C4', 'E4', 'G4']],
  song_title='Soldadito de Hierro', song_key='La menor',
  progression_desc='Estos son los 4 acordes que abren la canción y que se repiten. Escribe el grado de cada uno en La menor (i, iv, V7...).',
  progression=['Lam', 'Rem', 'Mi7', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas en el primer compás, grupos de tres ligeros en el segundo.',
  rhythm_events=([{'pitch': 'B4', 'dur': 'q'}] * 4 +
                 [{'pitch': 'B4', 'dur': 'e', 'beam': 0}] * 3 + [{'pitch': 'B4', 'dur': 'q'}] +
                 [{'pitch': 'B4', 'dur': 'e', 'beam': 1}] * 3),
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song5)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg5)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_05_Soldadito_De_Hierro.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
