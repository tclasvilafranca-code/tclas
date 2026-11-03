import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' Lucia_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='Lucía', subtitle='Joan Manuel Serrat',
  tonalidad='La menor', compas='4/4', tempo='♩≈84', forma='Estrofa narrativa',
  dificultad='Un reto narrativo', manos='Dinámica narrativa + acordes',
  la_cancion='Una canción de Serrat en La menor que cuenta una historia real. Aquí el reto es que la dinámica siga el relato: tranquilo al principio, intenso en el momento clave, y calmado otra vez.',
  difficult_cc='cc. 1–8', difficult_title='La dinámica que cuenta la historia',
  reto='cambiar de piano a forte y de vuelta a piano siguiendo el sentido de la letra, no de forma mecánica.',
  truco='lee la letra antes de tocar y decide dónde "sube la voz" la historia — ahí es donde crece el volumen.',
  sabias_que='"Lucía" es una de las canciones más versionadas del repertorio de Serrat; Joaquín Sabina la definió como una de las mejores canciones de amor en español.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('E5', 5), ('D5', 4)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: los acordes Lam, Rem y Mi7.',
  ritmo_texto='Ritmo: compás de 4/4 — deja que la dinámica narre la historia, no solo el ritmo.',
  estudiar_steps=['Busca LA menor y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: los acordes, sintiendo el Mi7.',
                   'Mano derecha sola: la frase en tres momentos de la historia (piano, forte, piano).',
                   'Las dos manos juntas: deja que la dinámica cuente el relato completo.'],
  checklist_items=['Encuentro LA menor y pongo bien los dedos.', 'Sigo la letra para decidir dónde crece el volumen.',
                    'El clímax suena realmente más fuerte que el resto.', 'Las dos manos narran juntas la historia.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · MAYO',
  total_songs=21,
)

cfg16 = dict(
  kicker='EVA · MAYO · LUCÍA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi7...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Lucía', song_key='La menor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en La menor (i, iv, V7...).',
  progression=['Lam', 'Rem', 'Mi7', 'Lam', 'Rem', 'Mi7', 'Lam', 'Rem'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras que cambian de intensidad con la historia.',
  rhythm_events=[{'pitch': 'C5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song16)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg16)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_16_Lucia.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
