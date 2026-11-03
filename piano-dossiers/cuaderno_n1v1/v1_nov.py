# -*- coding: utf-8 -*-
"""NOVIEMBRE · El teclado y su organizacion."""
from v1_base import *
from v1_base import _abs_idx
from reportlab.lib.colors import HexColor
import nens_dib

MES = 'Noviembre'
SEC = 'abcdef'
ROJO_T = HexColor('#F4C2BC')
VERDE_T = HexColor('#C9E3CC')
AZUL_T = HexColor('#C5D8EA')
CREMA_T = HexColor('#EADFC0')


def diag_grupos():
    """Dos octavas con los grupos de 2 y 3 teclas negras marcados y el Do de cada grupo."""
    h = 150

    def f(c, x, y, w):
        kw = w / 15.0
        yb = y - 118
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'EL PATRÓN SE REPITE: GRUPOS DE DOS Y DE TRES TECLAS NEGRAS')
        teclado(c, x, yb, w, 88, desde=('C', 4), n_blancas=15, etiqueta_blancas=True,
                marcas={'C4': CREMA_T, 'C5': CREMA_T, 'C6': CREMA_T}, do_central=True)
        # llaves sobre los grupos (por posicion de negras: C#,D# = 2 ; F#,G#,A# = 3)
        for o in (0, 1):
            x2 = x + (o * 7) * kw
            c.setStrokeColor(OCRE)
            c.setLineWidth(1.4)
            c.line(x2 + kw * 0.7, y - 24, x2 + kw * 2.3, y - 24)
            c.line(x2 + kw * 3.7, y - 24, x2 + kw * 6.3, y - 24)
            c.setFont('DejaVuSans-Bold', 8)
            c.setFillColor(OCRE)
            c.drawCentredString(x2 + kw * 1.5, y - 20, '2')
            c.drawCentredString(x2 + kw * 5.0, y - 20, '3')
        c.setFont('DejaVuSans', 7)
        c.setFillColor(MUTED)
        c.drawString(x, yb - 12, 'Cada Do está justo a la izquierda de un grupo de dos negras. El punto marca el Do central.')
    return Blk(h, f)


def diag_semitonos():
    """Una octava con los 12 sonidos y los semitonos senalados."""
    h = 120

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'DOCE SONIDOS POR OCTAVA, TODOS A UN SEMITONO DE DISTANCIA')
        kw = w / 8.0
        yb = y - 100
        teclado(c, x, yb, w, 70, desde=('C', 4), n_blancas=8, etiqueta_blancas=True,
                rotulos={'C#4': 'Do♯', 'D#4': 'Re♯', 'F#4': 'Fa♯', 'G#4': 'Sol♯', 'A#4': 'La♯'}, tam_fuente=7.4)
        # semitonos naturales: Mi-Fa y Si-Do
        c.setStrokeColor(ROJO)
        c.setLineWidth(1.4)
        for k in (2, 6):
            xx = x + (k + 1) * kw
            c.line(xx, yb - 3, xx, yb + 70)
            c.setFont('DejaVuSans-Bold', 7.6)
            c.setFillColor(ROJO)
            c.drawCentredString(xx, yb - 12, 'semitono')
    return Blk(h, f)


def construir(d):
    d.nuevo('Noviembre · El teclado y su organización')
    d.add(banda_mes('Noviembre', '1.er trimestre', 'El teclado y su organización',
                    'Teclas blancas y negras, octavas, sostenidos y bemoles: el mapa del piano.'))
    d.add(caja('dato', 'Un teclado, dos colores y un patrón', [
        'El teclado se forma con teclas **blancas** (las notas naturales: **Do, Re, Mi, Fa, Sol, La, Si**) y teclas **negras**, '
        'que quedan **agrupadas de dos en dos y de tres en tres**. Ese dibujo se repite una y otra vez a lo largo de todo el teclado.',
        'Cada repetición, de un Do al siguiente, es una **octava**: 7 blancas y 5 negras, 12 sonidos distintos. La nota '
        'se llama igual al principio y al final, pero **suena más aguda** en el segundo Do. Un piano completo tiene **88 teclas** '
        '(52 blancas y 36 negras).',
        'Las negras sirven de **referencia** para localizar las blancas: el **Do** está siempre a la izquierda del grupo de dos; '
        'el **Fa**, a la izquierda del grupo de tres; el **Mi** y el **Si** son las blancas que no tienen negra a su derecha.']),
        diag_grupos(),
        caja('tip', 'Entendiendo mejor el teclado', [
            '▸ **Patrón repetitivo:** aprende un grupo de dos y uno de tres y sabrás moverte por todo el piano.',
            '▸ **Importancia práctica:** conocer la organización permite encontrar las notas rápidamente, tocar escalas y acordes '
            'con precisión y leer partituras sin mirar las manos.',
            '▸ **Derecha o izquierda = agudo o grave:** hacia la derecha del teclado, los sonidos son más agudos; hacia la izquierda, más graves.']))

    # ---- Ejercicio 1: donde esta cada nota
    d.add(ejercicio(1, '¿Dónde está cada nota?',
                    ['Observa el teclado. Escribe en cada tecla blanca su nombre, empezando por el Do más grave y acabando en el Do más agudo.',
                     'Para un reto mayor, escribe también las teclas negras (por ejemplo, Do♯ y Re♯) en las casillas pequeñas.'],
                    'Que el cuerpo y la vista aprendan la organización del teclado: las octavas se repiten.'))
    blancas = {'%s%d' % (L, o) for o in (4, 5) for L in 'CDEFGAB'} | {'C6'}
    negras = {'%s#%d' % (L, o) for o in (4, 5) for L in 'CDFGA'}
    d.add(bloque_teclado(h=82, desde=('C', 4), n_blancas=15, cajas=blancas | negras, do_central=True,
                         titulo='Dos octavas desde el Do central'))
    sol(MES, 1, '¿Dónde está cada nota?',
        ['Blancas: Do Re Mi Fa Sol La Si Do Re Mi Fa Sol La Si Do. Negras (sostenidos, de izquierda a derecha): '
         'Do♯ Re♯ Fa♯ Sol♯ La♯ Do♯ Re♯ Fa♯ Sol♯ La♯ (también pueden escribirse como bemoles: Re♭ Mi♭ Sol♭ La♭ Si♭ …).'])

    # ---- sostenidos, bemoles, becuadro
    d.add(caja('dato', 'Sostenidos, bemoles y becuadros', [
        'Entre dos teclas blancas vecinas hay una negra, salvo entre **Mi–Fa** y **Si–Do**. La distancia entre dos teclas '
        'vecinas, sean del color que sean, es un **semitono**; dos semitonos forman un **tono**.',
        '▸ El **sostenido (♯)** sube la nota un semitono: Do♯ es la negra a la derecha de Do.',
        '▸ El **bemol (♭)** la baja un semitono: Re♭ es la negra a la izquierda de Re.',
        '▸ El **becuadro (♮)** anula una alteración anterior y devuelve la nota a su tecla blanca.',
        'Una misma tecla negra tiene **dos nombres**: Do♯ y Re♭ son la misma tecla. Se llaman notas **enarmónicas**. '
        'Cuál se usa depende de la tonalidad de la pieza, y lo verás con las escalas.']),
        diag_semitonos())

    d.add(ejercicio(2, 'Reconocimiento rápido y patrones de octavas',
                    ['En el **primer** teclado, escribe las notas naturales (blancas) de la octava.',
                     'En el **segundo**, escribe el nombre de cada negra como **sostenido** (Do♯, Re♯…).',
                     'En el **tercero**, escribe el nombre de cada negra como **bemol** (Re♭, Mi♭…).'],
                    'Identificar a primera vista las notas naturales y las alteradas, y ver que cada octava repite el dibujo.'))
    d.add(bloque_teclado(h=70, desde=('C', 4), n_blancas=8, cajas={'%s4' % L for L in 'CDEFGAB'} | {'C5'},
                         titulo='1.º  Notas naturales'))
    d.add(bloque_teclado(h=70, desde=('C', 4), n_blancas=8, cajas={'%s#4' % L for L in 'CDFGA'},
                         titulo='2.º  Sostenidos'))
    d.add(bloque_teclado(h=70, desde=('C', 4), n_blancas=8, cajas={'%s#4' % L for L in 'CDFGA'},
                         titulo='3.º  Bemoles'))
    sol(MES, 2, 'Reconocimiento rápido',
        ['1.º Do Re Mi Fa Sol La Si Do  ·  2.º Do♯ Re♯ Fa♯ Sol♯ La♯  ·  3.º Re♭ Mi♭ Sol♭ La♭ Si♭.'])

    # ---- Ejercicio 3: marcar alteraciones
    d.add(ejercicio(3, 'Teclas negras y alteraciones',
                    ['Marca en cada teclado las notas de la lista: **rojo** para los sostenidos, **verde** para los bemoles y **azul** '
                     'para las naturales. (En blanco y negro: ● sostenidos · ▲ bemoles · ■ naturales.)',
                     'Para terminar, escribe tu propia melodía de seis notas con ellas y tócala.'],
                    'Relacionar el nombre de la nota con su tecla, también en las alteradas.'))
    listas = [
        ('1)', 'Re♯ · Sol♭ · La♯ · Do · Fa♯', ['D#4', 'G#4', 'A#4', 'C4', 'F#4']),
        ('2)', 'Do♯ · Mi · La♭ · Si♭ · Fa', ['C#4', 'E4', 'G#4', 'A#4', 'F4']),
        ('3)', 'Re♭ · Sol♯ · Si · Mi♭ · La', ['C#4', 'G#4', 'B4', 'D#4', 'A4']),
    ]
    for t, texto, ks in listas:
        d.add(par('**%s**  %s' % (t, texto), 9.4, INK, despues=2))
        d.add(bloque_teclado(h=58, desde=('C', 4), n_blancas=8, titulo=None, etiqueta_blancas=False))
    d.add(lineas_escribir(1, 'Mi melodía de seis notas:', 22))
    sol(MES, 3, 'Teclas negras y alteraciones',
        ['1) Re♯ = Mi♭ (negra entre Re y Mi) · Sol♭ = Fa♯ · La♯ = Si♭ · Do (blanca) · Fa♯ (negra entre Fa y Sol).',
         '2) Do♯ = Re♭ · Mi · La♭ = Sol♯ · Si♭ = La♯ · Fa.   3) Re♭ = Do♯ · Sol♯ = La♭ · Si · Mi♭ = Re♯ · La.',
         'Fíjate: Re♯/Mi♭, Sol♭/Fa♯ y La♯/Si♭ son parejas enarmónicas (misma tecla).'])

    # ---- Ejercicio 4: grave o agudo
    d.add(ejercicio(4, '¿Grave o agudo? Del pentagrama al teclado',
                    ['Cada nota del pentagrama tiene una tecla marcada con una letra en el teclado. Escribe esa letra debajo de la nota.',
                     'Después, marca con **G** las teclas más graves que el Do central (a su izquierda) y con **A** las más agudas.'],
                    'Pasar de la partitura al instrumento: el camino que recorre la vista antes de la mano.'))
    notas = ['E4', 'C4', 'G4', 'A3', 'D5', 'B4']
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    r = rnd(8)
    orden = list(range(6))
    r.shuffle(orden)
    # teclas del teclado marcadas con la letra de la nota que representan (en orden mezclado)
    rot = {}
    for L, i in zip(letras, orden):
        rot[notas[i]] = L
    # teclado de A3 a D5 (para incluir A3)
    d.add(fila_notas('treble', [notas[i] for i in range(6)], 'q', bajo='linea', titulo='Escribe aquí la letra de la tecla'))

    def kb(c, x, y, w):
        teclado(c, x, y - 78, w, 74, desde=('A', 3), n_blancas=15, rotulos={k: v for k, v in rot.items()},
                marcas={k: CREMA_T for k in rot}, do_central=True, tam_fuente=9)
    d.add(Blk(86, lambda c, x, y, w: kb(c, x, y, w)))
    # grave/agudo: marcar G o A
    g_a = ['A3', 'G3', 'E5', 'C4', 'F5', 'D4']
    d.add(par('Marca con **G** (más grave) o **A** (más aguda) cada una de estas teclas, comparándola con el **Do central**:', 9.2, INK))
    d.add(fila_notas('treble', g_a, 'w', bajo='linea', caja_ancho=24, titulo='Tu respuesta: G o A'))
    sol(MES, 4, '¿Grave o agudo?',
        ['Letras: ' + ' · '.join('%s = %s (tecla de %s)' % (rot[notas[i]], nombre(notas[i]), nombre(notas[i], True)) for i in range(6)) + ' (se leen de izquierda a derecha en el pentagrama).',
         'G/A respecto al Do central: ' + ' · '.join('%s = %s' % (nombre(p, True), 'G' if _abs_idx(p) < _abs_idx('C4') else ('Do central' if p == 'C4' else 'A')) for p in g_a) + '.'])

    # ---- Al piano
    d.add(caja('piano', 'Manos al piano: el Do central y los territorios', [
        'La **mano derecha** toca normalmente las notas **agudas** (clave de sol) y la **izquierda** las **graves** (clave de fa). '
        'Las separa el **Do central**, la tecla blanca más cercana al centro del teclado, justo a la izquierda del grupo de dos negras del medio.',
        'Para tocar con comodidad: **dedos curvados**, como si sostuvieras una pelota pequeña; **muñecas rectas y relajadas**; '
        'toca con las **yemas**, como si caminaran sobre las teclas. Y **no hace falta golpear fuerte**: pulsa con suavidad pero con intención, como si acariciaras el teclado; si te cansas, estás tocando con demasiada fuerza.']))
    d.add(h2('Posición de cinco dedos sobre el Do'))

    def manos(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 8.6)
        c.setFillColor(NAVY)
        c.drawCentredString(x + 120, y - 12, 'MANO IZQUIERDA')
        c.drawCentredString(x + 360, y - 12, 'MANO DERECHA')
        nens_dib.ma_real(c, x + 120, y - 196, 0.95, esq=True, dits=True, color=False)
        nens_dib.ma_real(c, x + 360, y - 196, 0.95, esq=False, dits=True, color=False)
    d.add(Blk(216, manos))
    kt = {}

    def teclas_cinco(c, x, y, w):
        kw = 44
        for lab, nombres, dits, yy, esq in (('DERECHA', ['DO', 'RE', 'MI', 'FA', 'SOL'], [1, 2, 3, 4, 5], y - 4, False),
                                             ('IZQUIERDA', ['DO', 'RE', 'MI', 'FA', 'SOL'], [5, 4, 3, 2, 1], y - 56, True)):
            c.setFont('DejaVuSans-Bold', 8)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, yy - 28, lab)
            for i in range(5):
                xx = x + 90 + i * kw
                c.setFillColor(BLANCO)
                c.setStrokeColor(NAVY)
                c.setLineWidth(1)
                c.roundRect(xx, yy - 46, kw, 46, 4, fill=1, stroke=1)
                c.setFillColor(NAVY)
                c.circle(xx + kw / 2, yy - 13, 8, fill=1, stroke=0)
                c.setFillColor(BLANCO)
                c.setFont('DejaVuSans-Bold', 8.6)
                c.drawCentredString(xx + kw / 2, yy - 16, str(dits[i]))
                c.setFillColor(INK)
                c.setFont('DejaVuSans-Bold', 8)
                c.drawCentredString(xx + kw / 2, yy - 40, nombres[i])
            c.setFont('DejaVuSans', 7.4)
            c.setFillColor(MUTED)
            c.drawString(x + 90 + 5 * kw + 14, yy - 28, 'dedo 1 = polze · 5 = meñique' if False else ('Do central → Sol' if not esq else 'Do grave → Sol'))
    d.add(Blk(116, teclas_cinco))
    d.add(par('En la mano derecha el pulgar (1) va en el **Do central**; en la izquierda, el meñique (5) va en el **Do de una octava más grave** '
              'y el pulgar (1) en el **Sol**. Los dedos se numeran del pulgar (1) al meñique (5) en las dos manos.', 9.2, NAVY_SOFT))

    d.add(caja('piano', 'Primera melodía: Himno de la Alegría (Beethoven)', [
        'Toca con la mano derecha, posición de Do, sin mover la mano. Los números son los dedos. '
        'Las primeras cuatro frases son las que todo el mundo conoce.']))
    himno = [('E4', 'q', 3), ('E4', 'q', 3), ('F4', 'q', 4), ('G4', 'q', 5), ('G4', 'q', 5), ('F4', 'q', 4), ('E4', 'q', 3), ('D4', 'q', 2),
             ('C4', 'q', 1), ('C4', 'q', 1), ('D4', 'q', 2), ('E4', 'q', 3), ('E4', 'q.', 3), ('D4', 'e', 2), ('D4', 'h', 2)]
    ev = [{'pitch': p, 'dur': dd, 'number': n} for p, dd, n in himno]
    from page_layout_common import system_block
    d.add(Blk(110, lambda c, x, y, w: system_block(c, x, w, y, GAP + 0.6, 'Himno de la Alegría · L. van Beethoven (tema)', ev,
                                                  clef='treble', time_sig=(4, 4))))
    sol(MES, 'Himno de la Alegría', 'Himno de la Alegría',
        ['Notas: Mi Mi Fa Sol · Sol Fa Mi Re · Do Do Re Mi · Mi. Re Re. Compás 4/4: 4+4+4 y en el último compás, negra con puntillo + corchea + blanca = 4.'])
