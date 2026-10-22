import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' a-sky-full-of-stars-coldplay.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song4 = dict(
  num=4, title='A Sky Full of Stars', subtitle='Coldplay · con Avicii',
  tonalidad='Fa mayor', compas='4/4', tempo='Enérgico ♩≈125', forma='Estrofa-estribillo',
  dificultad='Un reto de firmeza', manos='Acordes marcados + melodía',
  la_cancion='Un himno pop de Coldplay en Fa mayor. Aquí el reto es la firmeza: acordes marcados y repetidos que nunca deben acelerar ni perder fuerza.',
  difficult_cc='cc. 1–8', difficult_title='Los acordes marcados, sin acelerar',
  reto='mantener cada acorde repetido exactamente igual de fuerte, sin que el pulso se dispare.',
  truco='cuenta en voz alta mientras tocas los acordes — si dejas de contar, sueles acelerar sin darte cuenta.',
  sabias_que='La canción usa un sintetizador y un piano real grabados juntos; en directo, Chris Martin la toca con luces LED en el público para simular el cielo estrellado del título.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('A4', 3), ('G4', 2)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA (el 4 en la tecla negra Sib); izquierda: los acordes Fa, Sib y Do, marcados y firmes.',
  ritmo_texto='Ritmo: compás de 4/4, enérgico — los acordes marcan el pulso como un metrónomo.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: los acordes marcados, contando en voz alta.',
                   'Mano derecha sola: la melodía, sin dejarte llevar por la prisa.',
                   'Las dos manos juntas: firmes, sin acelerar ni un compás.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Los acordes suenan igual de fuertes siempre.',
                    'No acelero cuando los acordes se repiten.', 'Junto las dos manos, con firmeza.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · OCTUBRE',
  total_songs=21,
)

cfg4 = dict(
  kicker='EVA · OCTUBRE · A SKY FULL OF STARS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F3', 'A3', 'C4'], ['Bb3', 'D4', 'F4'], ['C3', 'E3', 'G3'], ['F3', 'A3', 'C4']],
  song_title='A Sky Full of Stars', song_key='Fa mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa', 'Sib', 'Do', 'Fa', 'Sib'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de los acordes: negras firmes y regulares, sin ninguna variación.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
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

    out_path = os.path.join(OUT_DIR, 'Eva_04_A_Sky_Full_Of_Stars.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
