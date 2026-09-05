import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'NEL', 'cant-help-falling-in-love--elvis-presley_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title="Can't Help Falling in Love", subtitle='Elvis Presley · arr. Seb Alejandro',
  tonalidad='Re mayor', compas='3/4', tempo='Balada lenta ♩≈72', forma='Estrofa',
  dificultad='Un reto de criterio musical', manos='Melodía expresiva + acordes',
  la_cancion='Un vals lento en Re mayor. Aquí el reto no es técnico: es un reto de criterio — aprender a estirar con gusto el final de una frase y volver al pulso sin que se note el "enganche".',
  difficult_cc='cc. 1–8', difficult_title='El rubato con criterio',
  reto='estirar solo donde la frase de verdad respira, y no en cualquier sitio — y volver siempre al pulso de fondo.',
  truco='cuenta el pulso por dentro incluso cuando estires una nota, así el rubato suena decidido y no como un despiste.',
  sabias_que='Elvis Presley grabó esta canción en 1961; su melodía está basada en "Plaisir d\'amour", una canción francesa del siglo XVIII.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('A4', 5), ('G4', 4)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE (el 3 en la tecla negra Fa#); izquierda: los acordes Re, Sol y La.',
  ritmo_texto='Ritmo: compás de 3/4 — deja que el rubato respire, pero sin perder el pulso de fondo.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'La frase a tempo giusto, sin estirar nada todavía.',
                   'La misma frase, ahora estirando su final con gusto.',
                   'Las dos manos juntas, con el rubato repartido entre ambas.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'Sé tocar la frase a tempo estricto.',
                    'Estiro el final de la frase con criterio, no al azar.', 'El pulso de fondo no se pierde nunca.'],
  nivel_kicker='NEL · NIVEL MEDIO-ALTO · SEPTIEMBRE',
  total_songs=22,
)

cfg1 = dict(
  kicker='NEL · SEPTIEMBRE · CAN\'T HELP FALLING IN LOVE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['E2', 'A2', 'C#3'], ['D3', 'F#3', 'A3']],
  song_title="Can't Help Falling in Love", song_key='Re mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras y una nota larga al final de la frase, en 3/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'},
                 {'pitch': 'A4', 'dur': 'h.'}] * 2,
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

    out_path = os.path.join(OUT_DIR, 'Nel_01_Cant_Help_Falling_In_Love.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
