# -*- coding: utf-8 -*-
"""Paginas nuevas del cuaderno de Pedro: APERTURA visual de cada mes y pagina «AL PIANO» con digitacion,
   pieza, metronomo y plan de practica. Todo el contenido musical sale de datos escritos aqui y comprobables."""
from v1_base import *
from v1_base import _abs_idx
from reportlab.lib.colors import HexColor
from page_layout_common import system_block
import nens_dib

CREMA_T = HexColor('#EADFC0')
AZUL_T = HexColor('#C5D8EA')
NOTA_COL = dict(C='#E4392B', D='#F28C0E', E='#F9C80E', F='#76B82A', G='#2E86C8', A='#A58AC9', B='#A7A397')

# ---------------------------------------------------------------- datos por mes
# objetivos (4), vocabulario (6), teclas resaltadas, plan de 4 semanas, y la pagina «al piano»
MESES = {
    'Septiembre': dict(
        n=1, tri='1.er trimestre', titulo='Notación y figuras', lema='El alfabeto de la música escrita',
        obj=[('Leer', 'las siete notas en clave de sol'), ('Contar', 'la duración de cada figura y silencio'),
             ('Escribir', 'la clave, las notas y sus plicas'), ('Entender', 'el puntillo y el pulso')],
        voc=['pentagrama', 'clave de sol', 'figura', 'silencio', 'plica', 'puntillo'],
        teclas={'C4': 'Do', 'D4': 'Re', 'E4': 'Mi', 'F4': 'Fa', 'G4': 'Sol', 'A4': 'La', 'B4': 'Si'},
        plan=['Pentagrama, clave de sol y nombre de las notas', 'Figuras: nombre y valor', 'Silencios y puntillo', 'Plicas, sopa de letras y repaso'],
        piano=dict(
            titulo='Posición de cinco dedos sobre el Do', mano='d', dedos=[('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5)],
            pieza=('Au clair de la lune · canción tradicional francesa · mano derecha', 'treble', (4, 4),
                   [('C4', 'q', 1), ('C4', 'q', 1), ('C4', 'q', 1), ('D4', 'q', 2), ('E4', 'h', 3), ('D4', 'h', 2), ('C4', 'q', 1), ('E4', 'q', 3),
                    ('D4', 'q', 2), ('D4', 'q', 2), ('C4', 'w', 1)]),
            pasos=['Pon el pulgar (1) sobre el Do central y un dedo en cada tecla blanca.', 'Toca cada nota diciendo su nombre en voz alta.',
                   'Toca la pieza a ♩ = 60 contando 1-2-3-4.', 'Repite tres veces seguidas sin errores antes de subir el metrónomo.'])),
    'Octubre': dict(
        n=2, tri='1.er trimestre', titulo='Líneas adicionales', lema='Leer más allá del pentagrama',
        obj=[('Reconocer', 'las notas fuera del pentagrama'), ('Localizar', 'el Do central en las dos claves'),
             ('Percibir', 'si la melodía sube, baja o se repite'), ('Escribir', 'caminos de notas ascendentes y descendentes')],
        voc=['línea adicional', 'Do central', 'grave', 'agudo', 'ascendente', 'descendente'],
        teclas={'A3': 'La', 'B3': 'Si', 'C4': 'Do', 'D4': 'Re', 'E4': 'Mi'},
        plan=['Notas adicionales inferiores', 'Notas adicionales superiores', 'Dirección melódica y caminos', 'Dos claves, una nota: repaso'],
        piano=dict(
            titulo='La zona del Do central', mano='d', dedos=[('A3', None), ('B3', None), ('C4', 1), ('D4', 2), ('E4', 3)],
            pieza=('Ejercicio de lectura en la zona del Do central · mano derecha', 'treble', (4, 4),
                   [('C4', 'q', 1), ('D4', 'q', 2), ('E4', 'q', 3), ('D4', 'q', 2), ('C4', 'q', 1), ('E4', 'q', 3), ('G4', 'q', 5), ('E4', 'q', 3),
                    ('A3', 'q', None), ('B3', 'q', None), ('C4', 'q', 1), ('D4', 'q', 2), ('C4', 'w', 1)]),
            pasos=['Nombra en voz alta todas las notas antes de tocar.', 'Localiza las dos notas bajo el Do central (La y Si) en el teclado.',
                   'Toca despacio; la digitación de La y Si es tuya: elige la que no obligue a saltos.', 'Escribe a lápiz el nombre de las notas con rayita.'])),
    'Noviembre': dict(
        n=3, tri='1.er trimestre', titulo='El teclado', lema='El mapa del piano',
        obj=[('Encontrar', 'cualquier nota blanca en el teclado'), ('Distinguir', 'sostenidos, bemoles y becuadros'),
             ('Colocar', 'las manos y los dedos con soltura'), ('Tocar', 'tu primera melodía con las dos claves a la vista')],
        voc=['octava', 'tecla blanca', 'tecla negra', 'sostenido', 'bemol', 'becuadro'],
        teclas={'C4': 'Do', 'D4': 'Re', 'E4': 'Mi', 'F4': 'Fa', 'G4': 'Sol', 'A4': 'La', 'B4': 'Si', 'C5': 'Do'},
        plan=['Teclas blancas y negras; octavas', 'Sostenidos, bemoles y becuadros', 'Manos al piano: Do central y territorios', 'Grave o agudo; Himno de la Alegría'],
        piano=dict(
            titulo='Mano izquierda: cinco dedos sobre el Do grave', mano='i', dedos=[('C3', 5), ('D3', 4), ('E3', 3), ('F3', 2), ('G3', 1)],
            pieza=('Mary Had a Little Lamb · canción tradicional · mano izquierda', 'bass', (4, 4),
                   [('E3', 'q', 3), ('D3', 'q', 4), ('C3', 'q', 5), ('D3', 'q', 4), ('E3', 'q', 3), ('E3', 'q', 3), ('E3', 'h', 3), ('D3', 'q', 4),
                    ('D3', 'q', 4), ('D3', 'h', 4), ('E3', 'q', 3), ('G3', 'q', 1), ('G3', 'h', 1)]),
            pasos=['Coloca el meñique (5) sobre el Do grave; el pulgar (1) queda sobre el Sol.', 'Toca cada tecla de la posición diciendo el dedo: 5-4-3-2-1.',
                   'Toca la melodía muy despacio, con la cuenta en voz alta.', 'Cuando salga limpia, repítela una octava más aguda con la mano derecha.'])),
    'Diciembre': dict(
        n=4, tri='1.er trimestre', titulo='Escala de Do mayor', lema='La base de todo lo que vendrá',
        obj=[('Tocar', 'la escala de Do mayor con su digitación'), ('Construir', 'la escala con tonos y semitonos'),
             ('Medir', 'la distancia entre dos notas: el intervalo'), ('Crear', 'una pequeña melodía con las notas de la escala')],
        voc=['escala', 'tono', 'semitono', 'grado', 'intervalo', 'digitación'],
        teclas={'C4': 'Do', 'D4': 'Re', 'E4': 'Mi', 'F4': 'Fa', 'G4': 'Sol', 'A4': 'La', 'B4': 'Si', 'C5': 'Do'},
        plan=['Escala subiendo y bajando, mano derecha', 'Escala con la mano izquierda', 'Intervalos y ritmos sobre la escala', 'Mi melodía navideña'],
        piano=dict(
            titulo='Escala de Do mayor: el paso del pulgar', mano='d', dedos=[('C4', 1), ('D4', 2), ('E4', 3), ('F4', 1), ('G4', 2), ('A4', 3), ('B4', 4), ('C5', 5)],
            pieza=('Jingle Bells · J. Pierpont (1857) · primera frase · mano derecha', 'treble', (4, 4),
                   [('E4', 'q', 3), ('E4', 'q', 3), ('E4', 'h', 3), ('E4', 'q', 3), ('E4', 'q', 3), ('E4', 'h', 3), ('E4', 'q', 3), ('G4', 'q', 5),
                    ('C4', 'q.', 1), ('D4', 'e', 2), ('E4', 'w', 3)]),
            pasos=['Toca la escala subiendo con 1-2-3, el pulgar pasa por debajo y sigue 1-2-3-4-5.', 'Baja con 5-4-3-2-1, el 3 pasa por encima del pulgar.',
                   'Sin mirar la mano: tu oído debe reconocer la escala.', 'Toca la frase de Jingle Bells a tempo constante.'])),
    'Enero': dict(
        n=5, tri='2.º trimestre', titulo='Los compases', lema='La caja donde cabe el tiempo',
        obj=[('Sumar', 'figuras hasta llenar el compás'), ('Deducir', 'la cifra de compás de un ritmo'),
             ('Separar', 'compases con las barras'), ('Detectar', 'la figura que sobra')],
        voc=['compás', 'barra de compás', '2/4 · 3/4 · 4/4', 'tiempo', 'tiempo fuerte', 'cifra'],
        teclas={'C4': 'Do', 'E4': 'Mi', 'G4': 'Sol'},
        plan=['Completar compases de 2, 3 y 4 tiempos', 'Compases secretos', 'Colocar las barras de compás', 'Descubrir al intruso y dictado rítmico'],
        piano=dict(
            titulo='Cuenta y acento: fuerte – débil', mano='d', dedos=[('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5)],
            pieza=('Twinkle, Twinkle, Little Star · melodía tradicional · mano derecha', 'treble', (4, 4),
                   [('C4', 'q', 1), ('C4', 'q', 1), ('G4', 'q', 5), ('G4', 'q', 5), ('A4', 'q', 5), ('A4', 'q', 5), ('G4', 'h', 5), ('F4', 'q', 4),
                    ('F4', 'q', 4), ('E4', 'q', 3), ('E4', 'q', 3), ('D4', 'q', 2), ('D4', 'q', 2), ('C4', 'h', 1)]),
            pasos=['Cuenta «1-2-3-4» y da un golpe más fuerte en el 1 de cada compás.', 'Toca la melodía marcando ese acento con el peso del brazo, sin golpear.',
                   'Cuenta cuántos compases tiene y dónde está cada barra.', 'Repite con metrónomo a ♩ = 60 y a ♩ = 72.'])),
    'Febrero': dict(
        n=6, tri='2.º trimestre', titulo='Ritmo y subdivisión', lema='Un mismo pulso, mil dibujos',
        obj=[('Dividir', 'cada tiempo en dos y en cuatro'), ('Leer', 'ritmos con corcheas y semicorcheas'),
             ('Comparar', 'duraciones sin equivocarte'), ('Aplaudir', 'ritmos con pulso constante')],
        voc=['pulso', 'ritmo', 'subdivisión', 'corchea', 'semicorchea', 'barra'],
        teclas={'C4': 'Do', 'D4': 'Re', 'E4': 'Mi', 'F4': 'Fa', 'G4': 'Sol'},
        plan=['Ritmo de las palabras', 'Ritmos del día a día', '¿Qué figura dura más?', 'Ritmo y palmas con metrónomo'],
        piano=dict(
            titulo='La escala de cinco notas con ritmos', mano='d', dedos=[('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5)],
            pieza=('Ejercicio rítmico: una nota por tiempo y dos por tiempo · mano derecha', 'treble', (4, 4),
                   [('C4', 'e', 1), ('D4', 'e', 2), ('E4', 'e', 3), ('F4', 'e', 4), ('G4', 'q', 5), ('E4', 'q', 3), ('G4', 'e', 5), ('F4', 'e', 4),
                    ('E4', 'e', 3), ('D4', 'e', 2), ('C4', 'h', 1)]),
            pasos=['Primero toca todo en negras (una nota por golpe).', 'Después en corcheas: dos notas por golpe, a ♩ = 60.',
                   'Mantén el pulso con el pie y cambia solo la subdivisión.', 'Sube el metrónomo de 4 en 4 cuando salga limpio tres veces.'])),
    'Marzo': dict(
        n=7, tri='2.º trimestre', titulo='Clave de fa', lema='La voz grave del piano',
        obj=[('Leer', 'las notas graves en clave de fa'), ('Pasar', 'una melodía de clave de sol a clave de fa'),
             ('Mantener', 'el pulso con la mano izquierda'), ('Combinar', 'las dos claves en el sistema de piano')],
        voc=['clave de fa', 'registro grave', 'mano izquierda', 'octava', 'transcribir', 'sistema de piano'],
        teclas={'C3': 'Do', 'D3': 'Re', 'E3': 'Mi', 'F3': 'Fa', 'G3': 'Sol', 'A3': 'La', 'B3': 'Si', 'C4': 'Do'},
        plan=['Identificar notas en clave de fa', 'Ritmo y subdivisión en el registro grave', 'Una mini melodía en clave de fa', 'Transcribir de sol a fa'],
        piano=dict(
            titulo='Himno de la Alegría con la mano izquierda', mano='i', dedos=[('C3', 5), ('D3', 4), ('E3', 3), ('F3', 2), ('G3', 1)],
            pieza=('Himno de la Alegría · L. van Beethoven · mano izquierda (una octava más grave)', 'bass', (4, 4),
                   [('E3', 'q', 3), ('E3', 'q', 3), ('F3', 'q', 2), ('G3', 'q', 1), ('G3', 'q', 1), ('F3', 'q', 2), ('E3', 'q', 3), ('D3', 'q', 4),
                    ('C3', 'q', 5), ('C3', 'q', 5), ('D3', 'q', 4), ('E3', 'q', 3), ('E3', 'q.', 3), ('D3', 'e', 4), ('D3', 'h', 4)]),
            pasos=['Coloca el meñique sobre el Do grave y el pulgar sobre el Sol.', 'Nombra las notas de la melodía leyendo en clave de fa.',
                   'Toca muy despacio con la cuenta en voz alta.', 'Cuando la domines, tócala de memoria sin mirar las teclas.'])),
    'Abril': dict(
        n=8, tri='3.er trimestre', titulo='Los silencios', lema='La música también calla',
        obj=[('Reconocer', 'los cuatro silencios y su valor'), ('Completar', 'compases con silencios'),
             ('Distinguir', 'qué suena y qué calla'), ('Respetar', 'las pausas al tocar')],
        voc=['silencio', 'pausa', 'redonda', 'blanca', 'compás de espera', 'valor'],
        teclas={'C4': 'Do', 'E4': 'Mi', 'G4': 'Sol'},
        plan=['Elegir el silencio correcto', 'Huecos ocultos', '¿Suena o calla?', 'Imaginar compases con silencios'],
        piano=dict(
            titulo='Tocar el silencio: cuenta sin sonar', mano='d', dedos=[('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5)],
            pieza=('Pieza con silencios · T-Clas · mano derecha', 'treble', (4, 4),
                   [('C4', 'q', 1), ('E4', 'q', 3), ('G4', 'h', 5), ('G4', 'q', 5), ('rest', 'q', None), ('E4', 'h', 3), ('F4', 'q', 4), ('D4', 'q', 2),
                    ('E4', 'q', 3), ('rest', 'q', None), ('C4', 'w', 1)]),
            pasos=['Cuenta en voz alta «1-2-3-4» también en los silencios.', 'En cada silencio levanta suavemente la mano de las teclas.',
                   'Comprueba que cada compás suma cuatro tiempos.', 'Toca de seguido sin parar en los silencios.'])),
    'Mayo': dict(
        n=9, tri='3.er trimestre', titulo='Ligadura y puntillo', lema='Alargar el sonido',
        obj=[('Distinguir', 'ligadura de prolongación y de expresión'), ('Calcular', 'la duración con puntillo'),
             ('Sumar', 'tiempos de notas ligadas'), ('Sentir', 'el ritmo saltarín del puntillo')],
        voc=['ligadura', 'puntillo', 'legato', 'prolongación', 'tiempo y medio', 'compás'],
        teclas={'C4': 'Do', 'D4': 'Re', 'E4': 'Mi', 'F4': 'Fa', 'G4': 'Sol'},
        plan=['La ligadura', 'El puntillo en contexto', 'Lectura con pulso y subdivisión', 'Aplicación creativa'],
        piano=dict(
            titulo='Segunda frase del Himno: el puntillo', mano='d', dedos=[('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5)],
            pieza=('Himno de la Alegría · L. van Beethoven · 2.ª frase · mano derecha', 'treble', (4, 4),
                   [('E4', 'q', 3), ('E4', 'q', 3), ('F4', 'q', 4), ('G4', 'q', 5), ('G4', 'q', 5), ('F4', 'q', 4), ('E4', 'q', 3), ('D4', 'q', 2),
                    ('C4', 'q', 1), ('C4', 'q', 1), ('D4', 'q', 2), ('E4', 'q', 3), ('D4', 'q.', 2), ('C4', 'e', 1), ('C4', 'h', 1)]),
            pasos=['Estudia primero el último compás: negra con puntillo + corchea + blanca.', 'Di «ta-i ti-ta-a» mientras lo palmeas.',
                   'Toca la frase entera sin acortar el puntillo.', 'Sube el metrónomo solo cuando el puntillo suene exacto.'])),
    'Junio': dict(
        n=10, tri='3.er trimestre', titulo='Repaso y concierto', lema='Todo lo aprendido, sobre el escenario',
        obj=[('Repasar', 'los diez temas del curso'), ('Preparar', 'una pieza para tocarla de seguido'),
             ('Evaluar', 'lo que sabes con un test'), ('Disfrutar', 'del concierto final')],
        voc=['repaso', 'recital', 'programa', 'memoria', 'tempo', 'expresión'],
        teclas={'C4': 'Do', 'D4': 'Re', 'E4': 'Mi', 'F4': 'Fa', 'G4': 'Sol', 'A4': 'La', 'B4': 'Si', 'C5': 'Do'},
        plan=['Elegir la pieza y analizarla', 'Estudiar por partes: aislar, reducir, reinsertar', 'Test de repaso y dibujo musical', 'Ensayo y concierto'],
        piano=dict(
            titulo='Preparar el concierto', mano='d', dedos=[('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5)],
            pieza=('Escribe aquí el comienzo de tu pieza de concierto', None, None, []),
            pasos=['Elige una pieza del curso o de tu repertorio.', 'Estúdiala por trozos de dos compases y únelos.',
                   'Tócala una vez entera sin parar, como en el concierto.', 'Tócala delante de alguien y anota cómo ha ido.'])),
}


# ---------------------------------------------------------------- piezas de dibujo
def banner(mes, d_):
    """Banda azul noche con el numero de tema, el mes y el lema."""
    h = 118

    def f(c, x, y, w):
        c.setFillColor(NAVY)
        c.roundRect(x, y - h, w, h, 8, fill=1, stroke=0)
        c.setFillColor(OCRE)
        c.roundRect(x, y - h, 6, h, 3, fill=1, stroke=0)
        c.setFillColor(HexColor('#2A3A52'))
        c.setFont('DejaVuSerif-Bold', 96)
        c.drawRightString(x + w - 14, y - h + 14, '%02d' % d_['n'])
        c.setFillColor(HexColor('#C9B58A'))
        c.setFont('DejaVuSans-Bold', 9)
        c.drawString(x + 24, y - 26, '%s · %s' % (mes.upper(), d_['tri'].upper()))
        c.setFillColor(BLANCO)
        c.setFont('DejaVuSerif-Bold', 29)
        c.drawString(x + 24, y - 64, d_['titulo'])
        c.setFillColor(HexColor('#D9DEE6'))
        c.setFont('DejaVuSerif', 11.5)
        c.drawString(x + 24, y - 90, d_['lema'])
    return Blk(h + 12, f)


def cards(obj):
    """Cuatro objetivos en tarjetas 2x2 con verbo grande."""
    ch = 66
    h = 2 * ch + 12

    def f(c, x, y, w):
        cw = (w - 12) / 2.0
        for k, (verbo, txt) in enumerate(obj):
            cx = x + (k % 2) * (cw + 12)
            cy = y - (k // 2) * (ch + 12)
            c.setFillColor(SOMBRA)
            c.roundRect(cx + 1.6, cy - ch - 1.6, cw, ch, 6, fill=1, stroke=0)
            c.setFillColor(PANEL)
            c.setStrokeColor(RULE)
            c.setLineWidth(0.6)
            c.roundRect(cx, cy - ch, cw, ch, 6, fill=1, stroke=1)
            c.setFillColor(OCRE)
            c.circle(cx + 24, cy - ch / 2.0, 14, fill=1, stroke=0)
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSerif-Bold', 15)
            c.drawCentredString(cx + 24, cy - ch / 2.0 - 5.4, str(k + 1))
            c.setFillColor(NAVY)
            c.setFont('DejaVuSerif-Bold', 13)
            c.drawString(cx + 48, cy - 25, verbo)
            pinta_lineas(c, lineas(txt, cw - 60, 8.8), cx + 48, cy - 29, 8.8, 11.6, INK)
    return Blk(h + 8, f)


def chips(palabras, titulo='VOCABULARIO DEL MES'):
    h = 52

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 9, titulo)
        xx, yy = x, y - 36
        for t in palabras:
            tw = stringWidth(t, 'DejaVuSans-Bold', 9.4) + 22
            if xx + tw > x + w:
                xx, yy = x, yy - 26
            c.setFillColor(BLANCO)
            c.setStrokeColor(NAVY)
            c.setLineWidth(1.0)
            c.roundRect(xx, yy - 4, tw, 21, 10.5, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.setFont('DejaVuSans-Bold', 9.4)
            c.drawCentredString(xx + tw / 2, yy + 3, t)
            xx += tw + 8
    return Blk(h + 8, f)


def teclado_mes(teclas, titulo='LAS NOTAS DEL MES EN EL TECLADO'):
    """Teclado de 15 blancas con las notas del mes pintadas con su color."""
    h = 118

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 9, titulo)
        low = min(teclas, key=lambda k: _abs_idx(k))
        octv = int(low[-1])
        marcas = {k: HexColor(NOTA_COL[k[0]]) for k in teclas}
        rot = {k: v for k, v in teclas.items()}
        teclado(c, x, y - h + 8, w, 86, desde=('C', max(octv - 1, 2) if octv < 4 else 3), n_blancas=22 if octv < 4 else 22,
                marcas=marcas, rotulos=rot, do_central=False, tam_fuente=7.4)
    return Blk(h + 8, f)


def plan_semanas(plan):
    h = 18 + 4 * 30

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 9, 'MI PLAN DE CUATRO SEMANAS')
        for k, t in enumerate(plan):
            yy = y - 18 - k * 30
            c.setFillColor(PANEL if k % 2 == 0 else BLANCO)
            c.setStrokeColor(RULE)
            c.setLineWidth(0.6)
            c.roundRect(x, yy - 26, w, 26, 5, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.roundRect(x + 6, yy - 21, 58, 16, 8, fill=1, stroke=0)
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSans-Bold', 8.2)
            c.drawCentredString(x + 35, yy - 16.2, 'SEMANA %d' % (k + 1))
            c.setFillColor(INK)
            c.setFont('DejaVuSans', 9.2)
            c.drawString(x + 74, yy - 17, t)
            c.setStrokeColor(OCRE)
            c.setLineWidth(1.2)
            c.roundRect(x + w - 28, yy - 20, 14, 14, 3, fill=0, stroke=1)
    return Blk(h + 8, f)


def autoevaluacion(items):
    """Antes de empezar: ¿que se ya? Escala 1-5."""
    h = 16 + len(items) * 26

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 9, 'ANTES DE EMPEZAR: ¿QUÉ SÉ YA? (1 = nada · 5 = lo domino)')
        for k, t in enumerate(items):
            yy = y - 16 - k * 26
            c.setFillColor(INK)
            c.setFont('DejaVuSans', 9.2)
            c.drawString(x + 4, yy - 17, t)
            for j in range(5):
                c.setStrokeColor(NAVY)
                c.setLineWidth(1.0)
                c.setFillColor(BLANCO)
                c.circle(x + w - 120 + j * 25, yy - 13, 9, fill=1, stroke=1)
                c.setFillColor(MUTED)
                c.setFont('DejaVuSans', 8)
                c.drawCentredString(x + w - 120 + j * 25, yy - 15.8, str(j + 1))
    return Blk(h + 8, f)


# ---------------------------------------------------------------- pagina AL PIANO
def dedos_teclado(dedos, mano):
    """Teclado con la posicion de la mano: circulos con el dedo sobre cada tecla."""
    h = 168

    def f(c, x, y, w):
        teclas = [k for k, _ in dedos]
        low = min(teclas, key=lambda k: _abs_idx(k))
        i0 = BLANCAS.index(low[0])
        o0 = int(low[-1])
        ini = (BLANCAS[max(i0 - 1, 0) if i0 > 0 else 0], o0)
        nb = 9
        kw = w / float(nb)
        yb = y - h + 16
        marcas = {k: HexColor(NOTA_COL[k[0]]) for k in teclas}
        teclado(c, x, yb, w, 92, desde=ini, n_blancas=nb, marcas=marcas, tam_fuente=8)
        # posiciones de las teclas
        for k, dd in dedos:
            idx = (_abs_idx(k) - _abs_idx('%s%d' % ini))
            if idx < 0 or idx >= nb:
                continue
            cx = x + idx * kw + kw / 2.0
            c.setFillColor(NAVY)
            c.circle(cx, yb + 46, 10, fill=1, stroke=0)
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSans-Bold', 10.5)
            c.drawCentredString(cx, yb + 42.2, str(dd) if dd else '?')
            c.setFillColor(INK)
            c.setFont('DejaVuSans-Bold', 8.2)
            c.drawCentredString(cx, yb + 6, NOMBRE[k[0]])
        c.setFont('DejaVuSans-Bold', 8.2)
        c.setFillColor(OCRE)
        c.drawString(x, y - 8, ('MANO DERECHA' if mano == 'd' else 'MANO IZQUIERDA') + ' · el círculo indica el dedo (1 = pulgar … 5 = meñique)')
    return Blk(h + 8, f)


def metronomo_tabla():
    h = 20 + 3 * 22

    def f(c, x, y, w):
        c.setFillColor(NAVY)
        c.roundRect(x, y - 18, w, 18, 3, fill=1, stroke=0)
        cols = ['SEMANA', '♩ =', 'LIMPIA 3 VECES', 'LO QUE HE NOTADO']
        xs = [0.0, 0.14, 0.28, 0.5]
        for t, fx in zip(cols, xs):
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSans-Bold', 7.6)
            c.drawString(x + fx * w + 8, y - 12.4, t)
        for r in range(3):
            yy = y - 18 - (r + 1) * 22
            if r % 2 == 0:
                c.setFillColor(PANEL)
                c.rect(x, yy, w, 22, fill=1, stroke=0)
            c.setStrokeColor(RULE)
            c.setLineWidth(0.5)
            c.line(x, yy, x + w, yy)
            c.setFillColor(NAVY)
            c.setFont('DejaVuSans-Bold', 9)
            c.drawString(x + 10, yy + 7, str(r + 1))
            for j in range(3):
                c.setStrokeColor(NAVY_SOFT)
                c.roundRect(x + 0.28 * w + 10 + j * 26, yy + 4, 14, 14, 3, fill=0, stroke=1)
    return Blk(h + 10, f)


def sistema_pieza(titulo, clef, ts, notas):
    """Pieza con digitacion; los silencios van como ('rest', dur, None)."""
    ev = []
    for p, d_, n in notas:
        if p == 'rest':
            ev.append({'rest': True, 'dur': d_})
        else:
            e = {'pitch': p, 'dur': d_}
            if n:
                e['number'] = n
            ev.append(e)
    # corcheas seguidas dentro de un mismo tiempo: barra
    t, grp, bid = 0.0, {}, 0
    for i, e in enumerate(ev):
        if not e.get('rest') and e['dur'] == 'e':
            grp.setdefault(int(t + 1e-6), []).append(i)
        t += BEATS[e['dur']]
    for g_, idx in sorted(grp.items()):
        if len(idx) >= 2 and all(idx[k + 1] == idx[k] + 1 for k in range(len(idx) - 1)):
            for i in idx:
                ev[i]['beam'] = bid
            bid += 1
    return Blk(140, lambda c, x, y, w: system_block(c, x, w, y - 12, GAP + 0.8, titulo, ev, clef=clef, time_sig=ts))


def pasos_numerados(pasos):
    alts = [max(24, len(lineas(t, CONTENT_W - 48, 9.4)) * 12.8 + 8) for t in pasos]

    def f(c, x, y, w):
        yy = y
        for k, (t, hh) in enumerate(zip(pasos, alts)):
            c.setFillColor(OCRE)
            c.circle(x + 11, yy - 12, 10, fill=1, stroke=0)
            c.setFillColor(BLANCO)
            c.setFont('DejaVuSerif-Bold', 11.5)
            c.drawCentredString(x + 11, yy - 16, str(k + 1))
            pinta_lineas(c, lineas(t, w - 40, 9.4), x + 30, yy - 2, 9.4, 12.8, INK)
            yy -= hh
    return Blk(sum(alts) + 8, f)


# ---------------------------------------------------------------- paginas
def apertura(d, mes):
    m = MESES[mes]
    d.nuevo('%s · %s' % (mes, m['titulo']))
    voc_auto = ['Conozco el vocabulario del mes', 'Sé hacer los ejercicios del tema', 'Sé tocar el ejercicio «al piano»']
    d.add(banner(mes, m), cards(m['obj']), chips(m['voc']), teclado_mes(m['teclas']), plan_semanas(m['plan']), autoevaluacion(voc_auto))


def al_piano(d, mes):
    m = MESES[mes]['piano']
    d.nuevo('%s · Al piano' % mes)

    def cab(c, x, y, w):
        c.setFillColor(VERDE)
        c.roundRect(x, y - 44, w, 44, 8, fill=1, stroke=0)
        c.setFillColor(BLANCO)
        c.circle(x + 28, y - 22, 15, fill=1, stroke=0)
        c.setFillColor(VERDE)
        c.setFont('DejaVuSans-Bold', 16)
        c.drawCentredString(x + 28, y - 28, '♫')
        c.setFillColor(BLANCO)
        c.setFont('DejaVuSans-Bold', 8.2)
        c.drawString(x + 54, y - 17, 'AL PIANO · %s' % mes.upper())
        c.setFont('DejaVuSerif-Bold', 15.5)
        c.drawString(x + 54, y - 35, m['titulo'])
    d.add(Blk(56, cab), dedos_teclado(m['dedos'], m['mano']))
    d.add(h2('Cómo se practica'), pasos_numerados(m['pasos']))
    tit, clef, ts, notas = m['pieza']
    if notas:
        d.add(sistema_pieza(tit, clef, ts, notas))
    else:
        d.add(pauta_vacia('treble', 4, (4, 4), titulo=tit), pauta_vacia('bass', 4, (4, 4)))
    d.add(h2('Registro del metrónomo'), metronomo_tabla())
    d.add(pauta_vacia('treble', 2, None, titulo='Anota aquí un fragmento que te cueste y escríbelo de memoria'))
