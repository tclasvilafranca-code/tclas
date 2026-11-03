import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de Adagio en sol menor. Albinoni.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song10 = dict(
  num=10, title='Adagio en Sol menor', subtitle='Tomaso Albinoni · adaptación para piano',
  tonalidad='Sol menor', compas='3/4', tempo='Adagio ♩≈54', forma='Frase libre (estilo barroco)',
  dificultad='Nivel medio', manos='Melodía ligada + acordes largos',
  la_cancion='Una pieza barroca lenta y expresiva en Sol menor. Hoy: el ligado real, cambiando de dedo sobre la misma tecla sin cortar nunca el sonido.',
  difficult_cc='cc. 1–8', difficult_title='El ligado real: cambiar de dedo sin que se note',
  reto='sustituir un dedo por otro sobre la misma tecla sin volver a tocarla, para que el sonido no se corte.',
  truco='practica muy despacio el cambio de dedo sobre una sola nota sostenida, sintiendo el peso pasar de un dedo a otro.',
  sabias_que='El "Adagio en Sol menor" atribuido a Albinoni fue en realidad reconstruido en el siglo XX por el musicólogo Remo Giazotto a partir de un fragmento manuscrito.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol menor',
  posicion_texto='Mano derecha en posición de SOL menor: Sol(1) La(2) Sib(3) Do(4) Re(5). El dedo 3 toca la tecla negra Sib.',
  estudiar_steps=['Toca la posición de 5 dedos en Sol menor, sintiendo el Sib.',
                   'Practica el cambio de dedo sobre una sola nota sostenida.',
                   'Toca la frase entera cuidando que no haya ningún corte de sonido.',
                   'Junta ambas manos muy despacio, dejando sonar los acordes largos.'],
  checklist_items=['Reconozco el Sib de un vistazo', 'Cambio de dedo sin volver a tocar la tecla',
                    'La frase suena ligada, sin cortes', 'Los acordes de la izquierda duran todo el compás'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · FEBRERO',
  total_songs=22,
)

cfg10 = dict(
  kicker='VALENTINA · FEBRERO · ADAGIO EN SOL MENOR (ALBINONI)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Dom, Rem...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['C3', 'Eb3', 'G3'], ['D3', 'F3', 'A3'], ['G2', 'Bb2', 'D3']],
  song_title='Adagio en Sol menor', song_key='Sol menor',
  progression_desc='Estos son los acordes de la pieza. Escribe el grado de cada uno en Sol menor (i, iv, v...).',
  progression=['Solm', 'Dom', 'Rem', 'Solm'],
  progression_mode='names',
  rhythm_desc='Lee y marca el ritmo real: notas largas ligadas, en 3/4.',
  rhythm_events=[{'pitch': p, 'dur': 'h.'} for p in ['G4', 'A4']],
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song10)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg10)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_10_Adagio_Sol_Menor.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
