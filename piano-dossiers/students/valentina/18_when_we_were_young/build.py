import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de WHEN WE WERE YOUNG _ Adele Dm_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song18 = dict(
  num=18, title='When We Were Young', subtitle='Adele',
  tonalidad='Re menor', compas='4/4', tempo='Lento ♩≈68', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Acordes con novena + melodía',
  la_cancion='Una balada de Adele, en Re menor. Hoy: el acorde con novena, un color más denso que la tríada simple.',
  difficult_cc='cc. 1–8', difficult_title='El acorde con novena: un color más denso',
  reto='reconocer y sostener el acorde con novena entero, sin simplificarlo a la tríada de siempre.',
  truco='toca primero la tríada sola, luego añade la novena encima: escucha cómo cambia el color, más melancólico.',
  sabias_que='"When We Were Young" (2015) de Adele ganó el Grammy a la Mejor Interpretación Pop Solista.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('F4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · MAYO',
  total_songs=22,
)

cfg18 = dict(
  kicker='VALENTINA · MAYO · WHEN WE WERE YOUNG (ADELE)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Fa, Sib...) y di si es una tríada o lleva novena.',
  chords=[['D3', 'F3', 'A3'], ['D3', 'F3', 'A3', 'E4'], ['F3', 'A3', 'C4'], ['Bb2', 'D3', 'F3']],
  song_title='When We Were Young', song_key='Re menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re menor (i, iv, VII...).',
  progression=['Rem', 'Fa', 'Sib', 'Fa'],
  progression_mode='names',
  rhythm_desc='Lee y marca el ritmo real: notas largas sobre el Rem9, en 4/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'w'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song18)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg18)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_18_When_We_Were_Young.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
