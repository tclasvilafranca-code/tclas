import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de Amiga mia-alejandro Sanz.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song15 = dict(
  num=15, title='Amiga Mía', subtitle='Alejandro Sanz',
  tonalidad='Re mayor', compas='4/4', tempo='Lento ♩≈70', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Bajo en anacrusa + melodía',
  la_cancion='Una balada lenta de Alejandro Sanz, en Re mayor. Hoy: el bajo en anacrusa, un acorde que llega un poco antes del tiempo fuerte, empujando la frase hacia delante.',
  difficult_cc='cc. 1–8', difficult_title='El bajo en anacrusa: empezar antes del tiempo fuerte',
  reto='sentir el impulso de la anacrusa sin adelantarte de más ni quedarte corto en el tiempo.',
  truco='cuenta el compás completo en voz baja, y entra con el bajo justo un tiempo antes de donde esperarías.',
  sabias_que='"Amiga Mía" (1997) de Alejandro Sanz pertenece al álbum "Más", uno de los discos más vendidos de la música en español.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('F#4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.',
  estudiar_steps=['Toca la posición de 5 dedos en Re, sintiendo el Fa#.',
                   'Practica la anacrusa del bajo: silencio y luego el acorde, un poco antes del "1".',
                   'Añade la melodía por encima, sin cambiar el pulso.',
                   'Junta ambas manos muy despacio, sintiendo el impulso hacia delante.'],
  checklist_items=['Reconozco el Fa# de un vistazo', 'El bajo entra un poco antes del tiempo fuerte',
                    'No pierdo el pulso al anticipar el acorde', 'La melodía sigue tranquila por encima'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · MAYO',
  total_songs=22,
)

cfg15 = dict(
  kicker='VALENTINA · MAYO · AMIGA MÍA (ALEJANDRO SANZ)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['E2', 'A2', 'C#3'], ['D3', 'F#3', 'A3']],
  song_title='Amiga Mía', song_key='Re mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: silencio y anacrusa, en 4/4.',
  rhythm_events=[{'rest': True, 'dur': 'h.'}, {'pitch': 'D4', 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song15)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg15)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_15_Amiga_Mia.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
