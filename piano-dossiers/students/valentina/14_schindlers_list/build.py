import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de La lista de schindlers.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song14 = dict(
  num=14, title="Theme from Schindler's List", subtitle='John Williams',
  tonalidad='Sol menor', compas='4/4', tempo='Expresivo ♩≈66', forma='Tema con variaciones',
  dificultad='Nivel medio', manos='Octava grave sostenida + melodía',
  la_cancion='El tema de John Williams, en Sol menor. Hoy: la octava grave que sostiene todo el color, un bajo profundo y resonante bajo la melodía.',
  difficult_cc='cc. 1–8', difficult_title='La octava grave que sostiene todo el color',
  reto='alcanzar y sostener la octava en el registro más grave del piano sin tensar la mano ni perder el color.',
  truco='toca primero solo la nota grave y escucha cuánto tiempo resuena antes de añadir la octava completa.',
  sabias_que='El tema de "La lista de Schindler" (1993) de John Williams fue interpretado en el violín solista por Itzhak Perlman en la banda sonora original.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol menor',
  posicion_texto='Mano derecha en posición de SOL menor: Sol(1) La(2) Sib(3) Do(4) Re(5). El dedo 3 toca la tecla negra Sib.',
  estudiar_steps=['Toca la posición de 5 dedos en Sol menor, sintiendo el Sib.',
                   'Practica la octava grave sola, escuchando su resonancia.',
                   'Añade la melodía por encima, dejando sonar la octava entera.',
                   'Junta ambas manos muy despacio, cuidando el color grave.'],
  checklist_items=['Reconozco el Sib de un vistazo', 'Alcanzo la octava grave sin tensar la mano',
                    'Dejo resonar la octava todo el compás', 'La melodía flota clara sobre el color grave'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · MAYO',
  total_songs=22,
)

cfg14 = dict(
  kicker="VALENTINA · MAYO · THEME FROM SCHINDLER'S LIST",
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Rem, Dom...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['D3', 'F3', 'A3'], ['C3', 'Eb3', 'G3'], ['G2', 'Bb2', 'D3']],
  song_title="Theme from Schindler's List", song_key='Sol menor',
  progression_desc='Estos son los acordes del tema. Escribe el grado de cada uno en Sol menor (i, iv, v...).',
  progression=['Solm', 'Rem', 'Dom', 'Solm'],
  progression_mode='names',
  rhythm_desc='Lee y marca el ritmo real: la nota larga y grave, en 4/4.',
  rhythm_events=[{'pitches': ['G2', 'G3'], 'dur': 'w'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song14)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg14)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_14_Schindlers_List.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
