import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de Santa-tell-me-ariana-grande.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song6 = dict(
  num=6, title='Santa Tell Me', subtitle='Ariana Grande',
  tonalidad='Mi menor', compas='4/4', tempo='Moderato ♩≈92', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Melodía en staccato + acordes',
  la_cancion='Una canción navideña de Ariana Grande, en Mi menor. Hoy: el staccato, notas cortas y precisas, con aire entre cada una.',
  difficult_cc='cc. 1–8', difficult_title='El staccato marcado: notas cortas y precisas',
  reto='soltar cada nota justo después de tocarla, sin que el sonido se alargue ni se pegue a la siguiente.',
  truco='imagina que la tecla quema: tócala y suelta rápido, como si te diera un pequeño calambre.',
  sabias_que='"Santa Tell Me" (2014) de Ariana Grande se ha convertido en un clásico navideño moderno, con más de mil millones de reproducciones cada diciembre.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)]] +
                     [{'pitch': 'E4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mi menor',
  posicion_texto='Mano derecha en posición de MI: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca siempre la tecla negra Fa#.',
  estudiar_steps=['Toca la posición de 5 dedos en Mi menor, sintiendo el Fa#.',
                   'Practica el staccato con una sola nota, soltando rápido.',
                   'Añade el acorde de la izquierda, sostenido y tranquilo.',
                   'Junta ambas manos muy despacio, subiendo el tempo poco a poco.'],
  checklist_items=['Reconozco el Fa# de un vistazo', 'Suelto cada nota justo después de tocarla',
                    'Mantengo el acorde de la izquierda sin moverme', 'Sigo el pulso sin acelerar'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · NOVIEMBRE',
  total_songs=22,
)

cfg6 = dict(
  kicker='VALENTINA · NOVIEMBRE · SANTA TELL ME (ARIANA GRANDE)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Lam, Sim...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['C3', 'E3', 'A3'], ['D3', 'F#3', 'B3'], ['E3', 'G3', 'B3']],
  song_title='Santa Tell Me', song_key='Mi menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Mi menor (i, iv, v...).',
  progression=['Mim', 'Lam', 'Sim', 'Mim'],
  progression_mode='names',
  rhythm_desc='Lee y marca el ritmo real: negras cortas en staccato, en 4/4.',
  rhythm_events=[{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4']],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song6)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg6)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_06_Santa_Tell_Me.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
