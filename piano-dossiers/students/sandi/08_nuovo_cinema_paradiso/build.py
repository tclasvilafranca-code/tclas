import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'Ennio Morricone-NuovoCinemaParadiso-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song8 = dict(
  num=8, title='Nuovo Cinema Paradiso', subtitle='Ennio Morricone, arr. A.C. Escobés',
  tonalidad='Re menor', compas='4/4 con compases de 2/4 (mixto)', tempo='Andante cantabile', forma='Estrofa',
  dificultad='Nivel avanzado', manos='Melodía cromática cantabile + acordes',
  la_cancion='El célebre tema de Ennio Morricone, en Re menor, con compases ocasionales de 2/4. La melodía se tiñe de notas cromáticas de paso que aportan color expresivo sin cambiar la tonalidad.',
  difficult_cc='Toda la pieza', difficult_title='El cromatismo expresivo: notas que colorean la melodía',
  reto='destacar cada nota cromática con delicadeza, dentro de un fraseo amplio y cantabile, sin acentuarla de más ni esconderla.',
  truco='canta la línea melódica en voz baja antes de tocarla: el oído encuentra solo el color exacto que necesita cada nota cromática.',
  sabias_que='"Nuovo Cinema Paradiso" (1988), con música de Ennio Morricone (y su hijo Andrea), ganó el Óscar a la Mejor Película Extranjera y es una de las bandas sonoras más queridas del cine italiano.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('A4', 5), ('G4', 4), ('F4', 3), ('E4', 2)]],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa', 'Sol', 'La', 'Sib', 'Do'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re menor',
  posicion_texto='Mano derecha en posición de RE menor: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de la armadura.',
  estudiar_steps=[
      'Canta la melodía en voz baja, notando dónde aparece cada color cromático.',
      'Toca la línea melódica sola, destacando esas notas con un toque más suave y expresivo.',
      'Añade el acorde sostenido de la izquierda, sin que rompa el fraseo cantabile.',
      'Junta todo, cuidando la dinámica y la expresión por encima del ritmo mecánico.',
  ],
  checklist_items=[
      '¿Reconozco cada nota cromática de paso en la partitura?',
      '¿Las destaco con delicadeza, sin acentuarlas de más?',
      '¿Mantengo un fraseo amplio y cantabile?',
      '¿Puedo tocar la pieza entera con expresión, no solo con precisión?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · DICIEMBRE',
  total_songs=16,
)

cfg8 = dict(
  kicker='SANDI · DICIEMBRE · NUOVO CINEMA PARADISO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Solm, La...) y di si es mayor o menor.',
  chords=[['D2', 'F2', 'A2'], ['G2', 'Bb2', 'D3'], ['A2', 'C#3', 'E3'], ['D2', 'F2', 'A2']],
  song_title='Nuovo Cinema Paradiso', song_key='Re menor',
  progression_desc='Estos son los acordes principales de la canción. Escribe el grado de cada uno en Re menor (i, iv, V...).',
  progression=['Rem', 'Solm', 'La', 'Rem'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía cantabile, en 4/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'q'}] * 4,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song8)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg8)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_08_Nuovo_Cinema_Paradiso.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
