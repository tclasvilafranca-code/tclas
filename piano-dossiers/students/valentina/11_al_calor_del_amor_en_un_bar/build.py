import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de al-calor-del-amor-en-un-bar.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song11 = dict(
  num=11, title='Al Calor del Amor en un Bar', subtitle='Gabinete Caligari',
  tonalidad='Mi menor', compas='4/4', tempo='Allegretto ♩≈120', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Escala cromática + acordes',
  la_cancion='Una canción de rock español en Mi menor. Hoy: la subida cromática, una escalera de semitonos que empuja hacia el estribillo.',
  difficult_cc='cc. 5–8', difficult_title='La subida cromática hacia el estribillo',
  reto='tocar todos los semitonos, blancos y negros, sin saltarte ninguno y sin frenar antes de llegar arriba.',
  truco='cuenta en voz alta cada tecla mientras subes, sintiendo que la tensión crece con cada semitono.',
  sabias_que='"Al Calor del Amor en un Bar" (1986) de Gabinete Caligari es uno de los himnos del rock español de los años 80.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)]] +
                     [{'pitch': 'E4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mi menor',
  posicion_texto='Mano derecha en posición de MI: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca siempre la tecla negra Fa#.',
  estudiar_steps=['Toca la posición de 5 dedos en Mi menor, sintiendo el Fa#.',
                   'Practica la escala cromática muy despacio, semitono a semitono.',
                   'Añade el acorde de la izquierda, sostenido y firme.',
                   'Junta ambas manos, dejando que la subida empuje sin frenar.'],
  checklist_items=['Reconozco el Fa# de un vistazo', 'No me salto ningún semitono al subir',
                    'Mantengo el acorde de la izquierda sin moverme', 'La subida no frena hasta el final'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · ABRIL',
  total_songs=22,
)

cfg11 = dict(
  kicker='VALENTINA · ABRIL · AL CALOR DEL AMOR EN UN BAR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Sim, Lam...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['D3', 'F#3', 'B3'], ['C3', 'E3', 'A3'], ['E3', 'G3', 'B3']],
  song_title='Al Calor del Amor en un Bar', song_key='Mi menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Mi menor (i, iv, v...).',
  progression=['Mim', 'Sim', 'Lam', 'Mim'],
  progression_mode='names',
  rhythm_desc='Lee y marca el ritmo real: la escalera cromática en negras, en 4/4.',
  rhythm_events=[{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'F#4', 'G4']],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song11)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg11)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_11_Al_Calor_Del_Amor_En_Un_Bar.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
