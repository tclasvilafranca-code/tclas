import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de WRITING_S ON THE WALL _ Sam Smith_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song8 = dict(
  num=8, title="Writing's on the Wall", subtitle='Sam Smith · de la película "Spectre" (James Bond)',
  tonalidad='Fa mayor', compas='4/4', tempo='Lento expresivo ♩≈68', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Melodía con crescendo + acordes',
  la_cancion='La balada de James Bond, en Fa mayor. Hoy: el crescendo largo, construyendo la tensión escalón a escalón, sin saltos bruscos de volumen.',
  difficult_cc='cc. 1–8', difficult_title='El crescendo largo: construir tensión frase a frase',
  reto='subir el volumen en cuatro escalones claros, sin adelantarte al último de golpe.',
  truco='toca la misma frase cuatro veces seguidas, marcando mentalmente pp-p-mf-f como si subieras una escalera.',
  sabias_que='"Writing\'s on the Wall" (2015) de Sam Smith fue compuesta para la película de James Bond "Spectre" y ganó el Oscar a la Mejor Canción Original.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('A4', 3), ('G4', 2)]] +
                     [{'pitch': 'F4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca siempre la tecla negra Sib.',
  estudiar_steps=['Toca la posición de 5 dedos en Fa, sintiendo el Sib.',
                   'Practica la frase en pp, muy suave.',
                   'Repite la misma frase subiendo un escalón de volumen cada vez.',
                   'Junta ambas manos y deja que el crescendo llegue al forte sin prisa.'],
  checklist_items=['Reconozco el Sib de un vistazo', 'Empiezo de verdad en pp, casi sin sonido',
                    'Subo el volumen en escalones, no de golpe', 'Llego al forte con peso, sin golpear'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · ENERO',
  total_songs=22,
)

cfg8 = dict(
  kicker='VALENTINA · ENERO · WRITING’S ON THE WALL (SAM SMITH)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F3', 'A3', 'C4'], ['C3', 'E3', 'G3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3']],
  song_title="Writing's on the Wall", song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Do', 'Sib', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase que crece, en 4/4.',
  rhythm_events=[{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4']],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song8)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg8)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_08_Writings_On_The_Wall.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
