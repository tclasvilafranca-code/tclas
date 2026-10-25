import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'Copia de carol-of-the-bells   NAVIDAD.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song6 = dict(
  num=6, title='Carol of the Bells', subtitle='Mykola Leontovych, arr. Jim Paterson',
  tonalidad='Sol menor', compas='3/4', tempo='Allegro', forma='Estrofa con ostinato',
  dificultad='Nivel avanzado', manos='Ostinato melódico + armonía cambiante',
  la_cancion='El célebre villancico ucraniano, en Sol menor. La mano derecha repite un motivo de cuatro notas, como una campana, mientras la izquierda cambia de acorde debajo: el ostinato está en la melodía, no en el bajo.',
  difficult_cc='Toda la pieza', difficult_title='El ostinato en la melodía: la campana que repite',
  reto='mantener el motivo de campana absolutamente inalterado mientras la armonía de abajo cambia constantemente.',
  truco='memoriza el motivo de campana hasta que la mano lo toque sin pensar, y solo entonces presta atención a los cambios de acorde de la izquierda.',
  sabias_que='"Carol of the Bells" (1916), de Mykola Leontovych, se basa en un canto de Año Nuevo ucraniano ("Shchedryk") y no menciona campanas ni Navidad en su letra original.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol menor',
  posicion_texto='Mano derecha en posición de SOL menor: Sol(1) La(2) Sib(3) Do(4) Re(5). El Sib y el Mib son las alteraciones de esta tonalidad.',
  estudiar_steps=[
      'Aprende el motivo de campana de memoria, sin mirar las teclas.',
      'Repítelo en bucle hasta que sea completamente automático.',
      'Añade los acordes de la izquierda uno a uno, sin que la campana varíe.',
      'Junta todo a tempo, comprobando que el ostinato no se contagia de los cambios armónicos.',
  ],
  checklist_items=[
      '¿El motivo de campana suena exactamente igual en cada repetición?',
      '¿Reconozco los acordes Solm, Dom y Re por su sonido?',
      '¿La campana se mantiene estable aunque la armonía cambie?',
      '¿Puedo tocar la pieza entera con el ostinato inalterado?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · NOVIEMBRE',
  total_songs=16,
)

cfg6 = dict(
  kicker='SANDI · NOVIEMBRE · CAROL OF THE BELLS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Dom, Re...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['C2', 'Eb2', 'G2'], ['D2', 'F#2', 'A2'], ['G2', 'Bb2', 'D3']],
  song_title='Carol of the Bells', song_key='Sol menor',
  progression_desc='Estos son algunos acordes de la canción. Escribe el grado de cada uno en Sol menor (i, iv, V...).',
  progression=['Solm', 'Dom', 'Re', 'Solm'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el motivo de campana, en 3/4.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'e', 'beam': i // 4} for i in range(8)],
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song6)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg6)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_06_Carol_Of_The_Bells.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
