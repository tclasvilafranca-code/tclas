import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de  a-sky-full-of-stars-coldplay.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song3 = dict(
  num=3, title='A Sky Full of Stars', subtitle='Coldplay · con Avicii',
  tonalidad='Fa mayor', compas='4/4', tempo='Enérgico ♩≈100', forma='Estribillo repetido',
  dificultad='Nivel medio', manos='Acordes en contratiempo',
  la_cancion='Un himno pop de Coldplay en Fa mayor. Hoy: el acento en el contratiempo, la energía que llega justo después del tiempo fuerte.',
  difficult_cc='cc. 1–4', difficult_title='El acento en el contratiempo: la energía que no cae donde se espera',
  reto='sentir el silencio en el tiempo fuerte y entrar con precisión justo en el "y".',
  truco='cuenta "1-y-2-y" en voz alta, marcando el silencio, hasta que el contratiempo salga sin pensarlo.',
  sabias_que='"A Sky Full of Stars" (2014) de Coldplay fue coescrita y producida junto al DJ sueco Avicii, mezclando el rock con la música electrónica de baile.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('A4', 3), ('G4', 2)]] +
                     [{'pitch': 'F4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca siempre la tecla negra Sib.',
  estudiar_steps=['Toca la posición de 5 dedos en Fa, sintiendo el Sib.',
                   'Practica el contratiempo con una sola nota, contando en voz alta.',
                   'Añade el acorde entero en contratiempo, sin perder el silencio.',
                   'Junta ambas manos muy despacio, subiendo el tempo poco a poco.'],
  checklist_items=['Reconozco el Sib de un vistazo', 'Siento el silencio antes de entrar',
                    'El acorde entra justo en el contratiempo', 'Mantengo el tempo sin acelerar'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · OCTUBRE',
  total_songs=22,
)

cfg3 = dict(
  kicker='VALENTINA · OCTUBRE · A SKY FULL OF STARS (COLDPLAY)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F3', 'A3', 'C4'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F3', 'A3', 'C4']],
  song_title='A Sky Full of Stars', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: silencio-corchea-negra, el contratiempo, en 4/4.',
  rhythm_events=[{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'q'}] * 2,
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

    out_path = os.path.join(OUT_DIR, "Valentina_03_A_Sky_Full_Of_Stars.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
