import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'DESPACITO_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song11 = dict(
  num=11, title='Despacito', subtitle='Luis Fonsi & Daddy Yankee',
  tonalidad='La menor', compas='4/4', tempo='Reggaetón ♩≈89', forma='Verso-estribillo',
  dificultad='Un reto de contraste', manos='Melodía + acordes',
  la_cancion='Un reggaetón en La menor. Aquí el reto es de energía: el verso suena íntimo y contenido, y el estribillo se abre grande, con el mismo dibujo rítmico pero otra intensidad.',
  difficult_cc='cc. 1–8', difficult_title='El contraste verso-estribillo',
  reto='tocar la misma clase de frase con dos energías completamente distintas, sin que suenen igual.',
  truco='imagina que el verso lo cuentas en voz baja y el estribillo lo gritas con alegría.',
  sabias_que='"Despacito" fue la canción más escuchada de la década de 2010 y el primer vídeo en superar los 5.000 millones de reproducciones en YouTube.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('E5', 5), ('D5', 4)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: los acordes Lam, Rem y Mim.',
  ritmo_texto='Ritmo: compás de 4/4, reggaetón — el mismo dibujo suena distinto según la energía que le pongas.',
  estudiar_steps=['Busca LA menor y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: los acordes, con calma primero.',
                   'Mano derecha sola: el verso íntimo, luego el estribillo grande.',
                   'Las dos manos juntas: siente el contraste completo entre las dos partes.'],
  checklist_items=['Encuentro LA menor y pongo bien los dedos.', 'El verso suena contenido, casi hablado.',
                    'El estribillo se abre con energía real.', 'Las dos manos cambian de intensidad juntas.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · MARZO',
  total_songs=21,
)

cfg11 = dict(
  kicker='EVA · MARZO · DESPACITO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mim...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Despacito', song_key='La menor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en La menor (i, iv, v...).',
  progression=['Lam', 'Rem', 'Mim', 'Lam', 'Rem', 'Mim', 'Lam', 'Rem'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras que cambian de energía entre verso y estribillo.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 4 + [{'pitch': 'A4', 'dur': 'q'}] * 4,
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

    out_path = os.path.join(OUT_DIR, 'Eva_11_Despacito.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
