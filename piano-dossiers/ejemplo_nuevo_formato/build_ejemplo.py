# -*- coding: utf-8 -*-
"""EJEMPLO del nuevo formato de dosier de ejercicios (7 bloques pedagogicos
   por nivel), aplicado a 'Can't Help Falling in Love' (Elvis Presley, Re
   mayor, 3/4), Nivel BASICO. Pentagramas mas largos/densos que en el
   formato anterior (menos 'sparse'), diseño por bloques con badges de
   color propios."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from bloques_layout import (W, H, MARGIN, CONTENT_W, page_header, page_footer, bloque_heading,
                             bullet_list_2col, bullet_list, nota_estilo, answer_box_row,
                             blank_staff, system_block, grand_staff_block, wrap_text_common,
                             GRAY, INK, DARKGREEN)

HERE = os.path.dirname(__file__)
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN', " cant-help-falling-in-love-.pdf")
OUT_DIR = os.path.join(HERE, '..', 'output')

TS = (3, 4)
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
    y = wrap_text_common(c, 'Ejemplo aplicando el nuevo dosier de 7 bloques a una pieza real: Re mayor, 3/4, '
                             'vals de Elvis Presley. Nivel Básico. Los pentagramas se han alargado para aprovechar '
                             'todo el ancho de la página, en vez de sistemas cortos y dispersos.',
                          MARGIN, y, 'DejaVuSans', 9.2, CONTENT_W, 12.6, color=GRAY)
    y -= 10
    gap = 7.4

    # BLOQUE 1 · Calentamiento físico (texto, sin pentagrama)
    y = bloque_heading(c, y, 1, 'Antes de sentarse a tocar la pieza. Sin piano o con la tapa cerrada.')
    y = bullet_list_2col(c, y, [
        'Rutina de 5 minutos: rotación de muñecas + apertura y cierre de manos + estiramiento de dedos.',
        'Ejercicio de "araña": caminar los dedos sobre la tapa cerrada del piano antes de tocar.',
        'Estiramiento cruzado de brazo y hombro, 10-20 segundos por lado.',
        'Progresión de "A Dozen a Day" (Libro 2): ejercicios ya transponibles a otras tonalidades, como rutina diaria antes de esta pieza.',
    ], dot_color=DARKGREEN)
    y -= 12

    # BLOQUE 2 · Técnica al piano (con pentagrama, aplicado a Re mayor / la pieza)
    y = bloque_heading(c, y, 2, 'Aplicado a la tonalidad y a la textura reales de la canción.')
    y -= 4

    ev_rh = [{'pitch': p, 'dur': 'q'} for p in
             ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'D5', 'C#5', 'B4', 'A4', 'G4', 'F#4', 'E4', 'D4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Escala de Re mayor, una octava, mano derecha', ev_rh, clef='treble', time_sig=TS)
    ev_lh = [{'pitch': p, 'dur': 'q'} for p in
             ['D3', 'C#3', 'B2', 'A2', 'G2', 'F#2', 'E2', 'D2', 'E2', 'F#2', 'G2', 'A2', 'B2', 'C#3', 'D3']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) La misma escala, mano izquierda, una octava abajo', ev_lh, clef='bass', time_sig=TS)
    y -= 6

    treb_ost = [{'pitch': p, 'dur': 'h.'} for p in ['D4', 'F#4', 'E4', 'D4']]
    bass_ost = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in enumerate(['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 4)]
    y = grand_staff_block(c, MARGIN, CONTENT_W, y, gap, treb_ost, bass_ost,
                           'c) El acompañamiento real: bajo de vals en la izquierda, melodía larga en la derecha',
                           grand_gap_mult=7.3, time_sig=TS)
    y = nota_estilo(c, y, 'Nota de estilo (Bloque F — Clasicismo): este dibujo es un bajo de Alberti/vals. '
                          'Aísla solo el patrón Re-Fa#-La-Fa#, suelto y muy regular, antes de unirlo a la melodía.')

    pattern = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')] * 3
    ev_chords = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'd) Acordes I–IV–V en Re mayor, encadenados', ev_chords, clef='bass', time_sig=TS)

    page_footer(c, 1)
    c.showPage()


def page2(c):
    y = page_header(c, KICKER, 'Página 2/3')
    gap = 7.4

    # BLOQUE 3 · Lectura, ritmo e interpretación
    y = bloque_heading(c, y, 3, 'Sobre un fragmento real de la partitura, manos separadas primero.')
    y -= 4
    ev_a = [{'pitch': p, 'dur': 'q'} for p in
            ['D4', 'E4', 'F#4', 'A4', 'F#4', 'E4', 'D4', 'C#4', 'D4', 'E4', 'F#4', 'D4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Los primeros 4 compases, mano derecha sola, sin parar el pulso', ev_a, clef='treble', time_sig=TS)
    ev_b = [{'pitch': p, 'dur': 'q'} for p in
            ['D4', 'E4', 'F#4', 'A4', 'F#4', 'D4', 'E4', 'F#4', 'A4', 'G4', 'F#4', 'D4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) Lectura por patrones: marca con "P" cada paso y con "S" cada salto', ev_b, clef='treble', time_sig=TS)
    y -= 10

    # BLOQUE 4 · Entrenamiento auditivo (oral, sin escribir)
    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, el alumno responde en voz alta (no se escribe).')
    y -= 4
    ev_c1 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(RE, None), (FAsm, None), (SOL, None), (SIm, None)]]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Toca cada acorde: ¿mayor o menor?', ev_c1, clef='bass', time_sig=TS)
    ev_c2 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(RE, None), (SOL, None), (LA, None), (RE, None), (SOL, None), (LA, None), (RE, None), (SOL, None)]]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) La progresión real de la canción: ¿dónde está el I, el IV y el V?', ev_c2, clef='bass', time_sig=TS)
    y -= 10

    # BLOQUE 5 · Juegos pedagógicos (texto, sin pentagrama)
    y = bloque_heading(c, y, 5, 'Para cerrar el bloque técnico con algo lúdico, 5-8 minutos.')
    y = bullet_list_2col(c, y, [
        'Bingo de símbolos musicales: forte, piano, ligadura, staccato.',
        '"Roba el corazón del intervalo": cartas de intervalos que se ganan al identificarlos bien.',
        'Carrera de escalas: quién completa primero la escala de Re mayor sin errores de digitación.',
        'Memoria armónica: el profesor toca Re-Sol-La en distinto orden, el alumno adivina la secuencia.',
    ], dot_color=DARKGREEN)

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
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Análisis armónico: escribe el grado de cada acorde (I, vi, IV, V)', ev_a, clef='bass', time_sig=TS)
    y = answer_box_row(c, MARGIN, y - 4, 12, (CONTENT_W - 11 * 4) / 12, gap=4)
    y -= 12

    ev_b = [{'pitch': p, 'dur': 'q'} for p in
            ['D4', 'E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'D4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) Ficha de digitación: escribe el número de dedo bajo cada nota', ev_b, clef='treble', time_sig=TS)
    y = answer_box_row(c, MARGIN, y - 4, 12, (CONTENT_W - 11 * 4) / 12, gap=4)
    y -= 14

    top, bot = blank_staff(c, MARGIN, y, CONTENT_W, gap, clef='treble', time_sig=TS, n_bars=2)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y + 4, 'c) Dictado rítmico (2 compases): escucha y escribe las figuras')
    y = bot - gap * 3.4

    # BLOQUE 7 · Creatividad (texto, sin pentagrama)
    y = bloque_heading(c, y, 7, 'Para terminar la sesión con algo propio del alumno.')
    y = bullet_list(c, y, [
        'Varía rítmicamente la frase ya aprendida (cambia las negras por corcheas), modelo de las "Twinkle Variations" de Suzuki.',
        'Improvisación guiada: inventa una melodía sencilla sobre el mismo bajo de vals de la izquierda (Re-Fa#-La-Fa#).',
        'Compón una mini melodía de 4 compases usando solo los grados I-IV-V de Re mayor (Re, Sol, La).',
    ], dot_color=DARKGREEN)

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
