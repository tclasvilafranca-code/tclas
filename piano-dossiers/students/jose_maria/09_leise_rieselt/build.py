import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', '_leise-rieselt-(4 MANOS).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title='Leise rieselt der Schnee', subtitle='Villancico alemán · Eduard Ebel (a 4 manos)',
  tonalidad='Do mayor', compas='3/4', tempo='Piano, muy tranquila', forma='Estrofa',
  dificultad='Para disfrutar, sin prisa', manos='Notas sostenidas a 4 manos',
  la_cancion='Un villancico alemán muy tranquilo en Do mayor ("The Snow Falls Quietly"), pensado para tocar a 4 manos. Aquí las notas se sostienen varias veces seguidas sin volver a tocarlas.',
  difficult_cc='cc. 1–8', difficult_title='La nota que se sostiene, sin volver a tocarla',
  reto='apoyar la nota larga una sola vez y dejarla apagarse sola, sin la tentación de volver a tocarla.',
  truco='imagina un copo de nieve cayendo despacio: apóyate en la tecla y deja que el sonido se vaya solo, como el copo se posa.',
  sabias_que='"Leise rieselt der Schnee" (1895) es uno de los villancicos alemanes más queridos; su título significa "la nieve cae suavemente".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('C4', 1), ('D4', 2), ('E4', 3)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · DICIEMBRE',
  total_songs=21,
)

cfg9 = dict(
  kicker='JOSÉ MARÍA · DICIEMBRE · LEISE RIESELT DER SCHNEE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Leise rieselt der Schnee', song_key='Do mayor',
  progression_desc='Estos son los acordes de la pieza. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas largas y tranquilas, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h.'}] * 3,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song9)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg9)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'JoseMaria_09_Leise_Rieselt.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
