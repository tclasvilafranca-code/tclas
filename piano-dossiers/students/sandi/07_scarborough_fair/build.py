import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', ' scarborough-fair   Balada Inglesa_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=7, title='Scarborough Fair', subtitle='Balada tradicional inglesa, arr. Jim Paterson',
  tonalidad='Re dórico (armadura de 1 bemol, Sib)', compas='6/8 y 3/8 (mixto)', tempo='Andante', forma='Estrofa',
  dificultad='Nivel avanzado', manos='Melodía modal + compás cambiante',
  la_cancion='La célebre balada inglesa, de carácter modal (Re dórico, sin sensible alterada). El compás alterna constantemente entre 6/8 y 3/8: el pulso de la corchea debe mantenerse exactamente igual al cruzar de un compás a otro.',
  difficult_cc='Toda la pieza', difficult_title='El compás cambiante: 6/8 y 3/8, sin perder el pulso',
  reto='mantener la corchea a la misma velocidad exacta al pasar de un compás de 6/8 (dos pulsos) a uno de 3/8 (un pulso), sin acelerar ni frenar.',
  truco='cuenta siempre en corcheas, nunca en pulsos grandes: la corchea es la unidad que no cambia nunca, sea cual sea el compás.',
  sabias_que='"Scarborough Fair" es una balada inglesa tradicional cuyo origen se remonta posiblemente a una antigua balada escocesa ("The Elfin Knight"); su carácter modal (sin sensible) le da un sonido antiguo, casi medieval.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
                      enumerate(['D4', 'E4', 'F4', 'G4', 'A4', 'G4'])],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa', 'Sol', 'La', 'Sib', 'Do'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re (modo dórico)',
  posicion_texto='Mano derecha en posición de RE menor dórico: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración; no hay sensible (Do queda natural).',
  estudiar_steps=[
      'Marca la corchea con el pie, a un tempo constante, antes de tocar nada.',
      'Practica un compás de 6/8 solo, sintiendo los dos pulsos grandes.',
      'Practica un compás de 3/8 solo, sintiendo un único pulso grande, a la misma velocidad de corchea.',
      'Encadena varios compases alternando 6/8 y 3/8, sin que la corchea varíe.',
  ],
  checklist_items=[
      '¿La corchea suena igual de rápido en 6/8 que en 3/8?',
      '¿Reconozco el carácter modal, sin sensible alterada?',
      '¿Los acordes Rem, Do y Fa suenan firmes en cada pulso?',
      '¿Puedo tocar la pieza entera sin tropezar en los cambios de compás?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · DICIEMBRE',
  total_songs=16,
)

cfg7 = dict(
  kicker='SANDI · DICIEMBRE · SCARBOROUGH FAIR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Do, Fa...) y di si es mayor o menor.',
  chords=[['D2', 'F2', 'A2'], ['C2', 'E2', 'G2'], ['F2', 'A2', 'C3'], ['D2', 'F2', 'A2']],
  song_title='Scarborough Fair', song_key='Re dórico',
  progression_desc='Estos son los acordes característicos del modo. Escribe el grado de cada uno (i, III, iv...).',
  progression=['Rem', 'Do', 'Fa', 'Rem'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: corcheas en 6/8, luego en 3/8.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'e', 'beam': i // 3} for i in range(6)],
  rhythm_time_sig=(6, 8),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song7)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg7)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_07_Scarborough_Fair.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
