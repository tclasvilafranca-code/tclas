import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de  cant-help-falling-in-love-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title="Can't Help Falling in Love", subtitle='Elvis Presley · arr. Seb Alejandro',
  tonalidad='Re mayor', compas='3/4', tempo='Balada lenta ♩≈72', forma='Estrofa',
  dificultad='Nivel medio', manos='Melodía en octavas + acordes',
  la_cancion='El clásico vals de Elvis Presley, en Re mayor. Hoy: la melodía en octavas, ampliando el alcance de la mano sin tensión.',
  difficult_cc='cc. 1–4', difficult_title='La melodía en octavas: ampliar el alcance sin tensión',
  reto='tocar cada octava sin apretar la mano, dejando la muñeca suelta y el brazo relajado.',
  truco='antes de tocar cada octava, respira y suelta el hombro: la mano se abre desde el brazo, no desde los dedos.',
  sabias_que='"Can\'t Help Falling in Love" (1961) de Elvis Presley está basada en una melodía francesa del siglo XVIII, "Plaisir d\'amour".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('F#4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.',
  estudiar_steps=['Toca la posición de 5 dedos en Re, sintiendo el Fa#.',
                   'Practica la frase primero con una sola nota, luego en octavas.',
                   'Añade el acorde de la izquierda sin prisa.',
                   'Junta ambas manos muy despacio, subiendo el tempo poco a poco.'],
  checklist_items=['Reconozco el Fa# de un vistazo', 'Toco las octavas sin apretar la mano',
                    'Mantengo el acorde de la izquierda sin moverme', 'Sigo el pulso del vals sin acelerar'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · SEPTIEMBRE',
  total_songs=22,
)

cfg1 = dict(
  kicker="VALENTINA · SEPTIEMBRE · CAN'T HELP FALLING IN LOVE",
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['A2', 'C#3', 'E3'], ['D3', 'F#3', 'A3']],
  song_title="Can't Help Falling in Love", song_key='Re mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el vaivén del vals, en 3/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'h.'}] * 2,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song1)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg1)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_01_Cant_Help_Falling_In_Love.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
