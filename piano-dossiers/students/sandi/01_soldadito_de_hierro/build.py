import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'SOLDADITO DE HIERRO _ Nil Moliner_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title='Soldadito de Hierro', subtitle='Nil Moliner · arr. Campamento Musical Bye Bye Beethoven',
  tonalidad='La menor', compas='4/4', tempo='Enérgico ♩≈84', forma='Estrofa',
  dificultad='Nivel avanzado', manos='Melodía en tresillos + acordes',
  la_cancion='Una canción española muy rítmica, en La menor: la mano derecha se mueve en grupos de tres notas mientras la izquierda sostiene acordes largos. Hoy el reto es de precisión: que cada tresillo dure exactamente lo mismo que el anterior.',
  difficult_cc='cc. 1–4', difficult_title='El tresillo constante: ni acelerar ni frenar',
  reto='mantener un pulso interno perfectamente regular en cada tresillo, sin acelerar en la excitación ni frenar en la fatiga.',
  truco='practica con metrónomo real antes de tocar de memoria: el oído se acostumbra a la duración exacta de cada tresillo.',
  sabias_que='"Soldadito de Hierro" es del cantautor español Nil Moliner. La armadura no lleva alteraciones, pero la armonía real (Lam-Rem-Mi7-Lam) confirma que está en La menor, no en Do mayor: la misma armadura puede pertenecer a dos tonalidades relativas distintas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('E5', 5), ('D5', 4)]] +
                     [{'pitch': 'C5', 'dur': 'h', 'number': 3}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Lam',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: acordes Lam, Rem y Mi7 (el V7 lleva Sol sostenido).',
  estudiar_steps=[
      'Marca el pulso con metrónomo antes de tocar nada.',
      'Mano derecha sola: los tresillos, exactamente iguales entre sí.',
      'Acordes Lam-Rem-Mi7 con la izquierda, inmóviles y firmes.',
      'Las dos manos juntas, comprobando que el tresillo no varía al juntarlas.',
  ],
  checklist_items=[
      '¿Cada tresillo dura exactamente lo mismo que el anterior?',
      '¿La izquierda permanece firme sin contagiarse del ritmo?',
      '¿Toco el Mi7 con el Sol sostenido, sin fallar?',
      '¿Puedo tocar la canción entera sin que el tempo fluctúe?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · SEPTIEMBRE',
  total_songs=16,
)

cfg1 = dict(
  kicker='SANDI · SEPTIEMBRE · SOLDADITO DE HIERRO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi7...) y di si es mayor o menor.',
  chords=[['A4', 'C5', 'E5'], ['D4', 'F4', 'A4'], ['E4', 'G#4', 'B4'], ['A4', 'C5', 'E5']],
  song_title='Soldadito de Hierro', song_key='La menor',
  progression_desc='Estos son los 4 acordes que abren la canción y que se repiten. Escribe el grado de cada uno en La menor (i, iv, V7...).',
  progression=['Lam', 'Rem', 'Mi7', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas en el primer compás, tresillos exactos en el segundo.',
  rhythm_events=([{'pitch': 'B4', 'dur': 'q'}] * 4 +
                 [{'pitch': 'B4', 'dur': 'e', 'beam': 0}] * 3 + [{'pitch': 'B4', 'dur': 'q'}] +
                 [{'pitch': 'B4', 'dur': 'e', 'beam': 1}] * 3),
  rhythm_time_sig=(4, 4),
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

    out_path = os.path.join(OUT_DIR, 'Sandi_01_Soldadito_De_Hierro.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
