# -*- coding: utf-8 -*-
"""EJEMPLO v2 del nuevo formato de dosier de ejercicios (bloques
   pedagogicos por nivel), aplicado a 'Can't Help Falling in Love' (Elvis
   Presley, Re mayor, 3/4), Nivel BASICO.
   Cambios sobre la v1, pedidos tras revision:
   - Se descartan (de momento) los bloques 5 (juegos) y 7 (creatividad).
   - Ejercicios de mas de una linea de pentagrama (multi_system_block),
     como una partitura real, en vez de un unico sistema muy denso.
   - Armadura real (key_sig='Re mayor') en TODOS los pentagramas: el
     sostenido ya no se repite en cada nota, se indica una vez tras la
     clave, como en una partitura de verdad.
   - Compases (3/4) verticalmente centrados en el pentagrama (fix en el
     motor, notation.draw_time_sig)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from bloques_layout import (W, H, MARGIN, CONTENT_W, page_header, page_footer, bloque_heading,
                             nota_estilo, answer_box_row, blank_staff, system_block,
                             grand_staff_block, multi_system_block, wrap_text_common,
                             GRAY, INK, DARKGREEN)

HERE = os.path.dirname(__file__)
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN', " cant-help-falling-in-love-.pdf")
OUT_DIR = os.path.join(HERE, '..', 'output')

TS = (3, 4)
KEY = 'Re mayor'
KICKER = "EJEMPLO · NIVEL BÁSICO · CAN'T HELP FALLING IN LOVE"

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']
FAsm = ['F#2', 'A2', 'C#3']
SIm = ['B2', 'D3', 'F#3']


def page1(c):
    y = page_header(c, KICKER, 'Página 1/3')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    y = wrap_text_common(c, 'Ejemplo v2: armadura real (ya no se repite el sostenido en cada nota), '
                             'compases centrados, y ejercicios a varias líneas cuando la frase lo pide. '
                             'Re mayor, 3/4, vals de Elvis Presley. Nivel Básico.',
                          MARGIN, y, 'DejaVuSans', 9.2, CONTENT_W, 12.6, color=GRAY)
    y -= 10
    gap = 7.4

    # BLOQUE 1 · Calentamiento físico (texto, sin pentagrama)
    y = bloque_heading(c, y, 1, 'Antes de sentarse a tocar la pieza. Sin piano o con la tapa cerrada.')
    from bloques_layout import bullet_list_2col
    y = bullet_list_2col(c, y, [
        'Rutina de 5 minutos: rotación de muñecas + apertura y cierre de manos + estiramiento de dedos.',
        'Ejercicio de "araña": caminar los dedos sobre la tapa cerrada del piano antes de tocar.',
        'Estiramiento cruzado de brazo y hombro, 10-20 segundos por lado.',
        'Progresión de "A Dozen a Day" (Libro 2): ejercicios ya transponibles a otras tonalidades, como rutina diaria antes de esta pieza.',
    ], dot_color=DARKGREEN)
    y -= 14

    # BLOQUE 2 · Técnica al piano (con pentagrama, aplicado a Re mayor / la pieza)
    y = bloque_heading(c, y, 2, 'Aplicado a la tonalidad y a la textura reales de la canción. Armadura de Re mayor en todos los pentagramas.')
    y -= 4

    ev_rh = [{'pitch': p, 'dur': 'q'} for p in
             ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'D5', 'C#5', 'B4', 'A4', 'G4', 'F#4', 'E4', 'D4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Escala de Re mayor, una octava, mano derecha', ev_rh, clef='treble', time_sig=TS, key_sig=KEY)
    ev_lh = [{'pitch': p, 'dur': 'q'} for p in
             ['D3', 'C#3', 'B2', 'A2', 'G2', 'F#2', 'E2', 'D2', 'E2', 'F#2', 'G2', 'A2', 'B2', 'C#3', 'D3']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) La misma escala, mano izquierda, una octava abajo', ev_lh, clef='bass', time_sig=TS, key_sig=KEY)
    y -= 6

    treb_ost = [{'pitch': p, 'dur': 'h.'} for p in ['D4', 'F#4', 'E4', 'D4']]
    bass_ost = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in enumerate(['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 4)]
    y = grand_staff_block(c, MARGIN, CONTENT_W, y, gap, treb_ost, bass_ost,
                           'c) El acompañamiento real: bajo de vals en la izquierda, melodía larga en la derecha',
                           grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)
    y = nota_estilo(c, y, 'Nota de estilo (Bloque F — Clasicismo): este dibujo es un bajo de Alberti/vals. '
                          'Aísla solo el patrón Re-Fa#-La-Fa#, suelto y muy regular, antes de unirlo a la melodía.')

    pattern = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')] * 3
    ev_chords = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'd) Acordes I–IV–V en Re mayor, encadenados', ev_chords, clef='bass', time_sig=TS, key_sig=KEY)

    page_footer(c, 1)
    c.showPage()


def page2(c):
    y = page_header(c, KICKER, 'Página 2/3')
    gap = 7.4

    # BLOQUE 3 · Lectura, ritmo e interpretación -- a VARIAS lineas, como
    # una partitura real, en vez de un unico sistema.
    y = bloque_heading(c, y, 3, 'Un fragmento real y largo de la partitura, repartido en dos líneas — como en la partitura de verdad.')
    y -= 4
    ev_a = [{'pitch': p, 'dur': 'q'} for p in
            ['D4', 'E4', 'F#4', 'A4', 'F#4', 'E4', 'D4', 'C#4', 'D4', 'E4', 'F#4', 'D4',
             'F#4', 'G4', 'A4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'F#4', 'G4', 'A4', 'D4']]
    y = multi_system_block(c, MARGIN, CONTENT_W, y, gap,
                            'a) Los primeros 8 compases, mano derecha sola, sin parar el pulso',
                            ev_a, clef='treble', time_sig=TS, key_sig=KEY, bars_per_line=4)
    y -= 10
    ev_b = [{'pitch': p, 'dur': 'q'} for p in
            ['D4', 'E4', 'F#4', 'A4', 'F#4', 'D4', 'E4', 'F#4', 'A4', 'G4', 'F#4', 'D4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) Lectura por patrones: marca con "P" cada paso y con "S" cada salto', ev_b, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 10

    # BLOQUE 4 · Entrenamiento auditivo (oral, sin escribir)
    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, el alumno responde en voz alta (no se escribe).')
    y -= 4
    ev_c1 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(RE, None), (FAsm, None), (SOL, None), (SIm, None)]]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Toca cada acorde: ¿mayor o menor?', ev_c1, clef='bass', time_sig=TS, key_sig=KEY)
    ev_c2 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(RE, None), (SOL, None), (LA, None), (RE, None), (SOL, None), (LA, None), (RE, None), (SOL, None)]]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) La progresión real de la canción: ¿dónde está el I, el IV y el V?', ev_c2, clef='bass', time_sig=TS, key_sig=KEY)

    page_footer(c, 2)
    c.showPage()


def page3(c):
    y = page_header(c, KICKER, 'Página 3/3')
    gap = 7.4

    # BLOQUE 6 · Teoría y dictado escritos
    y = bloque_heading(c, y, 6, 'Aquí sí se escribe: sobre papel, con la partitura o de oído.')
    y -= 4
    pattern6a = [(RE, 'Re'), (SIm, 'Sim'), (SOL, 'Sol'), (LA, 'La')] * 3
    ev_a = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern6a]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Análisis armónico: escribe el grado de cada acorde (I, vi, IV, V)', ev_a, clef='bass', time_sig=TS, key_sig=KEY)
    y = answer_box_row(c, MARGIN, y - 4, 12, (CONTENT_W - 11 * 4) / 12, gap=4)
    y -= 16

    ev_b = [{'pitch': p, 'dur': 'q'} for p in
            ['D4', 'E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'D4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) Ficha de digitación: escribe el número de dedo bajo cada nota', ev_b, clef='treble', time_sig=TS, key_sig=KEY)
    y = answer_box_row(c, MARGIN, y - 4, 12, (CONTENT_W - 11 * 4) / 12, gap=4)
    y -= 16

    top, bot = blank_staff(c, MARGIN, y, CONTENT_W, gap, clef='treble', time_sig=TS, n_bars=2)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y + 4, 'c) Dictado rítmico (2 compases): escucha y escribe las figuras')
    y = bot - gap * 3.4

    y = wrap_text_common(c, 'Los bloques 5 (juegos) y 7 (creatividad) se han retirado de esta versión del '
                             'dosier — quedan pendientes de revisión antes de reincorporarlos.',
                          MARGIN, y, 'DejaVuSans', 8.4, CONTENT_W, 11.5, color=GRAY)

    page_footer(c, 3)
    c.showPage()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    ex_path = os.path.join(HERE, '_ejemplo_bloques.pdf')
    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    page3(c)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for p in PdfReader(ex_path).pages:
        writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Ejemplo_Nuevo_Formato_Bloques.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)
    os.remove(ex_path)
    print('generated', out_path)


if __name__ == '__main__':
    main()
