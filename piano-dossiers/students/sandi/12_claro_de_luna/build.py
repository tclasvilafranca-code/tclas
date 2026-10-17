import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', ' Claro de luna Beethoven.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song12 = dict(
  num=12, title='Claro de Luna', subtitle='"Moonlight" Sonata Op.27 No.2 · Beethoven, arr. Gilbert DeBenedetti',
  tonalidad='La menor (simplificada, sin alteraciones)', compas='2/4', tempo='Adagio', forma='Tema con cruce de manos',
  dificultad='Nivel avanzado', manos='Arpegio fluido + melodía sostenida, con cruce de manos',
  la_cancion='La célebre Sonata "Claro de Luna" de Beethoven, en esta versión simplificada. Al principio la mano derecha toca el arpegio grave (escrito en clave de Fa) mientras la izquierda sostiene la melodía; después los papeles se intercambian.',
  difficult_cc='Toda la pieza', difficult_title='El cruce de manos: la melodía pasa de una mano a otra',
  reto='mantener el arpegio fluido y uniforme mientras la melodía cambia de mano, sin que se note el momento del cruce.',
  truco='practica cada mano por separado hasta que el arpegio sea automático, y solo entonces practica el cruce, prestando atención a preparar la mano con antelación.',
  sabias_que='Beethoven tituló esta sonata "Sonata quasi una fantasia"; el sobrenombre "Claro de Luna" se lo puso el crítico Ludwig Rellstab cinco años después de la muerte del compositor.',
  mini_staff_events=[{'pitch': p, 'dur': 'e'} for p in ['A3', 'C4', 'E4', 'A3']] +
                     [{'pitch': 'A2', 'dur': 'h'}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Posición de LA menor: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas en esta versión simplificada.',
  estudiar_steps=[
      'Practica el arpegio de La menor solo, fluido y uniforme, con una mano.',
      'Practica la melodía sostenida sola, con la otra mano.',
      'Junta ambas manos sin cruzar, cada una en su papel inicial.',
      'Practica el momento del cruce, preparando la mano con antelación para que no se note.',
  ],
  checklist_items=[
      '¿El arpegio suena fluido y uniforme, sin tropiezos?',
      '¿La melodía se sostiene sin apagarse antes de tiempo?',
      '¿Preparo la mano con antelación antes de cada cruce?',
      '¿Puedo tocar la pieza entera sin que se note el cambio de papeles?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · FEBRERO',
  total_songs=16,
)

cfg12 = dict(
  kicker='SANDI · FEBRERO · CLARO DE LUNA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A3', 'B3'), ('A3', 'C4'), ('A3', 'D4'), ('A3', 'E4'), ('A3', 'F4'), ('A3', 'A4')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Claro de Luna', song_key='La menor',
  progression_desc='Estos son los acordes que sostiene la armonía. Escribe el grado de cada uno en La menor (i, iv, V...).',
  progression=['Lam', 'Rem', 'Mi', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el arpegio en corcheas, en 2/4.',
  rhythm_events=[{'pitch': 'A3', 'dur': 'e'}] * 4,
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song12)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg12)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_12_Claro_De_Luna.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
