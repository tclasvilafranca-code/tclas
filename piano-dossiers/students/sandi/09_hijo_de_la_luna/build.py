import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'Hijo-de-la-luna-Mecano_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title='Hijo de la Luna', subtitle='Mecano, arr. Unai Karam',
  tonalidad='Re menor', compas='6/8', tempo='♩.=58', forma='Estrofa',
  dificultad='Nivel avanzado', manos='Melodía sincopada + acordes',
  la_cancion='El clásico de Mecano, en Re menor (transportada desde el Mi menor original). Cada grupo melódico empieza con un silencio de corchea antes de las notas: hay que sentirlo con la misma precisión que una nota.',
  difficult_cc='Toda la pieza', difficult_title='El silencio que abre el compás: entrar tarde, sin prisa',
  reto='sentir el silencio inicial con precisión exacta, sin anticipar la entrada ni tocar antes de tiempo.',
  truco='cuenta el silencio en voz alta ("y-uno") antes de entrar, hasta que la espera se sienta tan natural como una nota.',
  sabias_que='"Hijo de la Luna" (1986), de Mecano, está compuesta originalmente en Mi menor; este arreglo la transporta a Re menor para facilitar su interpretación.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
                      enumerate(['D4', 'E4', 'F4', 'G4', 'A4', 'G4'])],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa', 'Sol', 'La', 'Sib', 'Do'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re menor',
  posicion_texto='Mano derecha en posición de RE menor: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Cuenta en voz alta el silencio inicial antes de cada grupo, sin tocar nada.',
      'Añade las notas después del silencio, manteniendo el mismo pulso.',
      'Practica los acordes Rem-Do-La7 con la izquierda, firmes y tranquilos.',
      'Junta las manos, comprobando que el silencio no se acorta al añadir el acompañamiento.',
  ],
  checklist_items=[
      '¿Siento el silencio inicial con la misma precisión que una nota?',
      '¿Entro exactamente a tiempo, sin anticiparme?',
      '¿Reconozco los acordes Rem, Do y La7 de esta tonalidad?',
      '¿Puedo tocar la pieza entera sin adelantar ninguna entrada?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · ENERO',
  total_songs=16,
)

cfg9 = dict(
  kicker='SANDI · ENERO · HIJO DE LA LUNA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Do, La7...) y di si es mayor, menor o de séptima.',
  chords=[['D2', 'F2', 'A2'], ['C2', 'E2', 'G2'], ['A1', 'C#2', 'E2', 'G2'], ['D2', 'F2', 'A2']],
  song_title='Hijo de la Luna', song_key='Re menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re menor (i, III, V7...).',
  progression=['Rem', 'Do', 'La7', 'Rem'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: silencio-nota-nota, en 6/8.',
  rhythm_events=[{'rest': True, 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}] * 2,
  rhythm_time_sig=(6, 8),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song9)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg9)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_09_Hijo_De_La_Luna.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
