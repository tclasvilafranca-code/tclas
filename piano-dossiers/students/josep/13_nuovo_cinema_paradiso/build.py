import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', '-NuovoCinemaParadiso.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song13 = dict(
  num=13, title='Nuovo Cinema Paradiso', subtitle='Ennio Morricone',
  tonalidad='Sib mayor', compas='4/4 / 2/4 (mixto)', tempo='♩≈84', forma='Tema',
  dificultad='Un reto de compás', manos='Melodía + acordes, compás cambiante',
  la_cancion='El tema principal de la película "Nuovo Cinema Paradiso" (Ennio Morricone), en Sib mayor. El reto es de compás: la música alterna entre 4/4 y 2/4 sin avisar.',
  difficult_cc='cc. 1–8', difficult_title='El compás que cambia: contar 4 y luego contar 2',
  reto='sentir el cambio de pulso cuando la música pasa de 4/4 a 2/4, sin perder el hilo ni acelerarse.',
  truco='cuenta en voz alta "1-2-3-4" y luego "1-2, 1-2" al llegar al cambio, para sentir físicamente la diferencia.',
  sabias_que='"Nuovo Cinema Paradiso" (1988), de Ennio Morricone junto a su hijo Andrea, ganó el Óscar a la mejor película extranjera ese mismo año.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('F5', 5), ('Eb5', 4)]] +
                     [{'pitch': 'Bb4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sib', quinta_solfege='Fa',
  keyboard_notes=['Sib', 'Do', 'Re', 'Mib', 'Fa', 'Sol', 'La'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sib',
  posicion_texto='Mano derecha en posición de SIB mayor (un dedo por tecla, dedos 4 y 5 en teclas negras); izquierda: los acordes Sib, Fa, Solm y Mib.',
  ritmo_texto='Ritmo: el compás cambia entre 4/4 y 2/4 — hay que sentir el cambio de pulso cada vez.',
  estudiar_steps=['Busca SIB y tócala 3 veces (tu nota casa).',
                   'La frase en 4/4, contando "1-2-3-4" en voz alta.',
                   'La misma frase en 2/4, contando ahora "1-2, 1-2".',
                   'Las dos manos juntas, sintiendo el cambio de compás sin perder el hilo.'],
  checklist_items=['Encuentro SIB y pongo bien los dedos.', 'Siento el cambio entre 4/4 y 2/4.',
                    'Sé los acordes Sib, Fa, Solm y Mib de memoria.', 'Las dos manos juntas sin perder el pulso.'],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=22,
)

cfg13 = dict(
  kicker='JOSEP · ABRIL · NUOVO CINEMA PARADISO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SIB, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('Bb4', 'C5'), ('Bb4', 'D5'), ('Bb4', 'Eb5'), ('Bb4', 'F5'), ('Bb4', 'G5'), ('Bb4', 'Bb5')],
  chords_desc='Identifica cada acorde: nómbralo (Sib, Fa, Solm, Mib...) y di si es mayor o menor.',
  chords=[['Bb2', 'D3', 'F3'], ['F2', 'A2', 'C3'], ['G2', 'Bb2', 'D3'], ['Eb2', 'G2', 'Bb2']],
  song_title='Nuovo Cinema Paradiso', song_key='Sib mayor',
  progression_desc='Estos son los acordes reales de la pieza. Escribe el grado de cada uno en Sib mayor (I, IV, V, vi...).',
  progression=['Sib', 'Fa', 'Solm', 'Mib'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: negras que cambian de compás, entre 4/4 y 2/4.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song13)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg13)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_13_Nuovo_Cinema_Paradiso.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
