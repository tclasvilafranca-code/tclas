import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', 'cant-help-falling-in-love-elvis-presley_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title="Can't Help Falling in Love", subtitle='Elvis Presley',
  tonalidad='Re mayor', compas='3/4', tempo='Balada lenta ♩≈72', forma='Estrofa',
  dificultad='Para disfrutar, sin prisa', manos='Volumen suave + acordes',
  la_cancion='Una balada lenta de Elvis Presley, en Re mayor. Aquí cuidamos que el volumen suave no pierda el sonido — tocar bajito no significa tocar sin fuerza.',
  difficult_cc='cc. 1–9', difficult_title='El volumen bajito que no se pierde',
  reto='que el sonido llegue claro y presente aunque se toque muy suave, sin que se apague.',
  truco='apoya el dedo con decisión pero deja el brazo relajado — la suavidad viene de la velocidad, no de la falta de apoyo.',
  sabias_que='La melodía viene de "Plaisir d\'Amour" (1784), una antigua canción francesa. Elvis Presley la adaptó en 1961 para la película "Blue Hawaii".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('E4', 2), ('D4', 1)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE (un dedo por tecla, el 3 en el Fa#); izquierda: los acordes Re, Sol y La, sin prisa.',
  ritmo_texto='Ritmo: compás de 3/4, un vals lento — el volumen se mantiene suave y presente, sin apagarse.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'Las notas suaves, sintiendo que el sonido no se pierde.',
                   'Los acordes Re-Sol-La con la izquierda, sin prisa.',
                   'Las dos manos juntas, manteniendo el volumen bajito y claro.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'El sonido suave no se apaga ni se pierde.',
                    'Sé los acordes Re, Sol y La de memoria.', 'Las dos manos juntas, tranquilas y suaves.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · ABRIL',
  total_songs=21,
)

cfg17 = dict(
  kicker="JOSÉ MARÍA · ABRIL · CAN'T HELP FALLING IN LOVE",
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['A2', 'C#3', 'E3'], ['D3', 'F#3', 'A3']],
  song_title="Can't Help Falling in Love", song_key='Re mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas suaves y tranquilas, en 3/4.',
  rhythm_events=[{'pitch': 'F#4', 'dur': 'h.'}] * 3,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'JoseMaria_17_Cant_Help_Falling_In_Love.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
