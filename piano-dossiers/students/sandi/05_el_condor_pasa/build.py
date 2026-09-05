import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_IMG = os.path.join(HERE, '..', 'source', 'SANDI', ' EL CONDOR PASA.jpg')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song5 = dict(
  num=5, title='El Cóndor Pasa', subtitle='Melodía tradicional andina · Daniel Alomía Robles, arr. Peter Edvinsson',
  tonalidad='Re menor', compas='4/4', tempo='Moderato', forma='Estrofa',
  dificultad='Nivel avanzado', manos='Melodía + acompañamiento en corcheas repetidas',
  la_cancion='La célebre melodía andina, en Re menor. El acompañamiento se basa en acordes repetidos en corcheas: el reto es mantenerlos firmes y regulares sin que la muñeca se agarrote.',
  difficult_cc='Toda la pieza', difficult_title='El acompañamiento en corcheas repetidas: firmeza sin rigidez',
  reto='repetir el mismo acorde muchas veces seguidas sin que el brazo se tense, manteniendo un sonido firme y uniforme.',
  truco='piensa en pequeños rebotes relajados de la muñeca, no en golpes secos del brazo entero: la firmeza viene del control, no de la fuerza.',
  sabias_que='"El Cóndor Pasa" (1913), de Daniel Alomía Robles, está basada en música tradicional andina y fue declarada Patrimonio Cultural de la Nación en Perú.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('A4', 5), ('G4', 4), ('F4', 3), ('E4', 2)]],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa', 'Sol', 'La', 'Sib', 'Do'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re menor',
  posicion_texto='Mano derecha en posición de RE menor: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Repite un acorde cualquiera en corcheas durante un minuto, buscando la relajación de la muñeca.',
      'Practica el acompañamiento de Fa y Do7 en corcheas, sin tensarte.',
      'Añade la melodía con la derecha sobre ese acompañamiento ya relajado.',
      'Junta todo, comprobando que las corcheas no pierden firmeza al añadir la melodía.',
  ],
  checklist_items=[
      '¿Las corcheas repetidas suenan iguales entre sí, sin acentos accidentales?',
      '¿Mi muñeca permanece relajada durante la repetición?',
      '¿Reconozco los acordes Fa, Do7 y A7 de esta tonalidad?',
      '¿Puedo tocar la pieza entera sin que el brazo se fatigue de más?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · NOVIEMBRE',
  total_songs=16,
)

cfg5 = dict(
  kicker='SANDI · NOVIEMBRE · EL CÓNDOR PASA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Fa, Do7, A7...) y di si es mayor, menor o de séptima.',
  chords=[['D3', 'F3', 'A3'], ['F2', 'A2', 'C3'], ['C2', 'E2', 'G2', 'Bb2'], ['A2', 'C#3', 'E3', 'G3']],
  song_title='El Cóndor Pasa', song_key='Re menor',
  progression_desc='Estos son algunos acordes de la canción. Escribe el grado de cada uno en Re menor (i, III, V7...).',
  progression=['Rem', 'Fa', 'A7', 'Rem'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: las corcheas repetidas, en 4/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'e'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')
    source_path = os.path.join(HERE, '_source.pdf')

    from reportlab.lib.utils import ImageReader
    img = ImageReader(SOURCE_IMG)
    iw, ih = img.getSize()
    scale = min(W / iw, H / ih)
    c = canvas.Canvas(source_path, pagesize=(W, H))
    c.drawImage(SOURCE_IMG, (W - iw * scale) / 2, (H - ih * scale) / 2, iw * scale, ih * scale)
    c.showPage()
    c.save()

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
    for path in (source_path, theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_05_El_Condor_Pasa.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (source_path, theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
