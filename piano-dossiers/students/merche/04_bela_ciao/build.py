import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', ' bela-ciao.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song4 = dict(
  num=4, title='Bela Ciao', subtitle='La Casa de Papel · arr. Anderson Miranda Fernandes',
  tonalidad='Mi menor', compas='2/4', tempo='Moderato', forma='Estrofa',
  dificultad='Nivel básico', manos='Melodía sincopada + acordes, con sensible alterado',
  la_cancion='La versión de "Bela Ciao" popularizada por La Casa de Papel, en Mi menor. Cerca del final aparece un Re sostenido: el "sensible" que tira con fuerza hacia el Mi.',
  difficult_cc='cc. 22–24', difficult_title='La nota que despierta: el sensible de Mi menor',
  reto='reconocer el Re sostenido y sentir cómo "tira" hacia el Mi, sin confundirlo con el Re natural.',
  truco='toca despacio Re-Re sostenido-Mi varias veces, y nota cómo el Re sostenido pide resolver en el Mi.',
  sabias_que='"Bela Ciao" es un canto popular italiano de origen antiguo, adoptado como himno antifascista, que alcanzó fama mundial gracias a la serie La Casa de Papel.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('F#4', 2), ('E4', 1), ('F#4', 2)]] +
                     [{'pitch': 'E4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mi menor',
  posicion_texto='Mano derecha en posición de MI menor: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El Fa# es la única tecla negra de esta posición.',
  estudiar_steps=[
      'Encuentra el Mi central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Mi menor (Mi-Sol-Si) con la izquierda, con calma.',
      'Busca el Re sostenido y siente cómo "tira" hacia el Mi.',
      'Junta las manos despacio: la izquierda sostiene su acorde, la derecha canta la melodía sincopada.',
  ],
  checklist_items=[
      '¿Reconozco el Re sostenido sin dudar?',
      '¿Toco el acorde de Mi menor con seguridad?',
      '¿La melodía sincopada suena natural, sin tropiezos?',
      '¿Puedo tocar la canción entera sin pararme?',
  ],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · OCTUBRE',
  total_songs=28,
)

cfg4 = dict(
  kicker='MERCÈ · OCTUBRE · BELA CIAO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Lam, Si...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['A2', 'C3', 'E3'], ['B2', 'D#3', 'F#3'], ['E3', 'G3', 'B3']],
  song_title='Bela Ciao', song_key='Mi menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Mi menor (i, iv, V...).',
  progression=['Mim', 'Lam', 'Si', 'Mim'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la síncopa con silencio de corchea, en 2/4.',
  rhythm_events=([{'rest': True, 'dur': 'e'}] + [{'pitch': 'B4', 'dur': 'e'}] * 3) * 2,
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song4)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg4)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_04_Bela_Ciao.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
