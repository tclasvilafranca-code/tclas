import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'Canon de Pachelbel_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song3 = dict(
  num=3, title='Canon en Re', subtitle='Johann Pachelbel, arr. Jim Paterson',
  tonalidad='Re mayor', compas='4/4', tempo='Andante', forma='Tema y variaciones sobre ostinato',
  dificultad='Nivel avanzado', manos='Ostinato + melodía progresivamente elaborada',
  la_cancion='El célebre Canon de Pachelbel, en Re mayor. Toda la pieza se construye sobre un bajo ostinato de ocho acordes que se repite sin cambiar, mientras la melodía se vuelve cada vez más elaborada por encima.',
  difficult_cc='Toda la pieza', difficult_title='El bajo ostinato: la misma progresión, una y otra vez',
  reto='mantener el ostinato absolutamente regular mientras la melodía se acelera y se complica encima.',
  truco='memoriza el ostinato de ocho acordes (Re-La-Sim-F#m-Sol-Re-Sol-La) hasta poder tocarlo sin mirar, para que la mano izquierda quede libre de atención mientras la derecha se concentra en la melodía.',
  sabias_que='El Canon de Pachelbel (c. 1680-1706) fue redescubierto en el siglo XX y hoy es una de las progresiones armónicas más influyentes de la música popular, reutilizada en cientos de canciones.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('A4', 5), ('G4', 4), ('F#4', 3), ('E4', 2)]],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El Fa# y el Do# son las alteraciones de esta tonalidad.',
  estudiar_steps=[
      'Memoriza el ostinato de ocho acordes con la izquierda, sin mirar las teclas.',
      'Toca el ostinato en bucle, cada vez más rápido, sin que tiemble.',
      'Añade la melodía sencilla (blancas) con la derecha, encima del ostinato.',
      'Aumenta la densidad de la melodía (corcheas) sin que el ostinato varíe ni un ápice.',
  ],
  checklist_items=[
      '¿El ostinato suena exactamente igual en cada repetición?',
      '¿Reconozco los ocho acordes de memoria?',
      '¿La melodía puede acelerarse sin que la izquierda se contagie?',
      '¿Puedo tocar la pieza entera manteniendo la regularidad del bajo?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · OCTUBRE',
  total_songs=16,
)

cfg3 = dict(
  kicker='SANDI · OCTUBRE · CANON EN RE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, La, Sim, F#m, Sol...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['A2', 'C#3', 'E3'], ['B2', 'D3', 'F#3'], ['F#2', 'A2', 'C#3']],
  song_title='Canon en Re', song_key='Re mayor',
  progression_desc='Este es el ostinato completo de ocho acordes. Escribe el grado de cada uno en Re mayor (I, V, vi, iii...).',
  progression=['Re', 'La', 'Sim', 'F#m', 'Sol', 'Re', 'Sol', 'La'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el ostinato en blancas, en 4/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'h'}] * 4,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song3)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg3)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_03_Canon_De_Pachelbel.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
