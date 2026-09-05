import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' SOLDADITO DE HIERRO _ Nil Moliner_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song5 = dict(
  num=5, title='Soldadito de Hierro', subtitle='Nil Moliner',
  tonalidad='La menor', compas='4/4', tempo='Enérgico ♩≈100', forma='Estrofa-estribillo',
  dificultad='Un reto de construcción', manos='Melodía + crescendo',
  la_cancion='Una canción de Nil Moliner en La menor. Aquí el reto es la dinámica: la estrofa empieza íntima y crece hasta el estribillo con toda su fuerza.',
  difficult_cc='cc. 1–8', difficult_title='El crescendo que se construye',
  reto='crecer de piano a forte de forma gradual, sin dar el salto de golpe en un solo compás.',
  truco='piensa en tres escalones (p, mf, f) en vez de un interruptor de encendido/apagado.',
  sabias_que='"Soldadito de Hierro" habla de la lucha personal de Nil Moliner contra la ansiedad; el título hace referencia a sentirse fuerte por fuera aunque por dentro cueste.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('C5', 3), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: los acordes Lam, Rem y Mi7.',
  ritmo_texto='Ritmo: compás de 4/4, enérgico — cuenta con firmeza, dejando que el volumen crezca poco a poco.',
  estudiar_steps=['Busca LA y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: los acordes, sintiendo el Sol sostenido del Mi7.',
                   'Mano derecha sola: la frase en tres niveles de volumen (p, mf, f).',
                   'Las dos manos juntas: crece con las dos a la vez, sin que ninguna se adelante.'],
  checklist_items=['Encuentro LA menor y pongo bien los dedos.', 'El Mi7 lleva el Sol sostenido, no el natural.',
                    'Construyo el crescendo en pasos, no de golpe.', 'Las dos manos crecen juntas.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · NOVIEMBRE',
  total_songs=21,
)

cfg5 = dict(
  kicker='EVA · NOVIEMBRE · SOLDADITO DE HIERRO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi7...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Soldadito de Hierro', song_key='La menor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en La menor (i, iv, V7...).',
  progression=['Lam', 'Rem', 'Mi7', 'Lam', 'Rem', 'Mi7', 'Lam', 'Rem'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras que crecen de intensidad hacia el final.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 4 + [{'pitch': 'C5', 'dur': 'q'}] * 4,
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

    out_path = os.path.join(OUT_DIR, 'Eva_05_Soldadito_De_Hierro.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
