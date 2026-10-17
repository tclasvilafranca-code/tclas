import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_IMG = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', ' ADAGIO_.jpg')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song20 = dict(
  num=20, title='Adagio', subtitle='Tomaso Albinoni · arr. A. L. Christopherson',
  tonalidad='La menor', compas='3/4', tempo='Adagio ♩≈60', forma='Tema con dinámica',
  dificultad='Para disfrutar, sin prisa', manos='Viaje de volumen + acordes',
  la_cancion='El célebre Adagio de Albinoni, en este arreglo transportado a La menor (el original está en Sol menor). Aquí cuidamos que el volumen viaje de piano a forte y de vuelta, sin miedo a los cambios.',
  difficult_cc='cc. 1–9', difficult_title='El viaje del volumen: de piano a forte, sin miedo',
  reto='atreverse a los cambios de volumen que pide la partitura, sin quedarse siempre igual de flojo.',
  truco='marca mentalmente "ahora suave", "ahora un poco más", "ahora fuerte" antes de cada frase, como si fueran escalones.',
  sabias_que='Este "Adagio" se atribuye tradicionalmente a Albinoni, pero en realidad fue compuesto en buena parte por el musicólogo Remo Giazotto en el siglo XX, a partir de un fragmento original.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: los acordes Lam, Rem y Mi (con el Sol# de la sensible), sin prisa.',
  ritmo_texto='Ritmo: compás de 3/4, muy lento — el volumen viaja de piano a forte, sin miedo.',
  estudiar_steps=['Busca LA y tócala 3 veces (tu nota casa).',
                   'La frase suave, sin prisa, sintiendo el piano.',
                   'Los acordes Lam-Rem-Mi con la izquierda.',
                   'Las dos manos juntas, dejando que el volumen viaje.'],
  checklist_items=['Encuentro LA y pongo bien los dedos.', 'Me atrevo a tocar fuerte cuando toca.',
                    'Sé los acordes Lam, Rem y Mi de memoria.', 'Las dos manos juntas, sin miedo a los cambios.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · JUNIO',
  total_songs=21,
)

cfg20 = dict(
  kicker='JOSÉ MARÍA · JUNIO · ADAGIO (ALBINONI)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D3', 'F3', 'A3'], ['E3', 'G#3', 'B3'], ['A2', 'C3', 'E3']],
  song_title='Adagio', song_key='La menor',
  progression_desc='Estos son los acordes de la pieza. Escribe el grado de cada uno en La menor (i, iv, V...).',
  progression=['Lam', 'Rem', 'Mi', 'Lam'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: notas largas y tranquilas, en 3/4.',
  rhythm_events=[{'pitch': 'C5', 'dur': 'h.'}] * 3,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')
    source_path = os.path.join(HERE, '_source.pdf')

    from reportlab.lib.utils import ImageReader
    img = ImageReader(SOURCE_IMG)
    iw, ih = img.getSize()
    scale = min(W / iw, H / ih)
    c = canvas.Canvas(source_path, pagesize=(W, H))
    c.drawImage(SOURCE_IMG, (W - iw * scale) / 2, (H - ih * scale) / 2, iw * scale, ih * scale)
    c.showPage()
    c.save()

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song20)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg20)
    c.save()

    writer = PdfWriter()
    for path in (source_path, theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'JoseMaria_20_Adagio_Albinoni.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (source_path, theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
