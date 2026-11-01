# -*- coding: utf-8 -*-
"""DICIEMBRE · Escala de Do mayor."""
from n1_base import *
from n1_base import _abs_idx
from reportlab.lib.colors import HexColor
from page_layout_common import system_block
from notation import draw_staff, draw_clef, draw_note, note_y

MES = 'Diciembre'
SEC = 'abcdef'
ESC = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
DIG_D_SUBE = [1, 2, 3, 1, 2, 3, 4, 5]
DIG_D_BAJA = [5, 4, 3, 2, 1, 3, 2, 1]
ESC_B = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']
DIG_I_SUBE = [5, 4, 3, 2, 1, 3, 2, 1]
DIG_I_BAJA = [1, 2, 3, 1, 2, 3, 4, 5]
GRADOS = [('I', 'Do', 'tónica'), ('II', 'Re', 'supertónica'), ('III', 'Mi', 'mediante'), ('IV', 'Fa', 'subdominante'),
          ('V', 'Sol', 'dominante'), ('VI', 'La', 'superdominante'), ('VII', 'Si', 'sensible')]


def diag_escala():
    """Teclado de una octava con tonos y semitonos."""
    h = 124

    def f(c, x, y, w):
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'LA ESCALA DE DO MAYOR: TONO · TONO · SEMITONO · TONO · TONO · TONO · SEMITONO')
        kw = w / 8.0
        yb = y - 104
        teclado(c, x, yb, w, 62, desde=('C', 4), n_blancas=8, etiqueta_blancas=True,
                marcas={'%s4' % L: HexColor('#EADFC0') for L in 'CDEFGAB'} | {'C5': HexColor('#EADFC0')})
        for i in range(7):
            xa = x + kw * (i + 0.5)
            xb = x + kw * (i + 1.5)
            semi = i in (2, 6)
            c.setStrokeColor(ROJO if semi else NAVY)
            c.setLineWidth(1.3)
            p = c.beginPath()
            p.moveTo(xa, yb + 66)
            p.curveTo(xa, yb + 80, xb, yb + 80, xb, yb + 66)
            c.drawPath(p, stroke=1, fill=0)
            c.setFont('DejaVuSans-Bold', 7.6)
            c.setFillColor(ROJO if semi else NAVY)
            c.drawCentredString((xa + xb) / 2, yb + 84, '½' if semi else '1')
    return Blk(h, f)


def diag_digitacion():
    h = 184

    def f(c, x, y, w):
        g = 8.4
        c.setFont('DejaVuSans-Bold', 7.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x, y - 8, 'MANO DERECHA')
        c.drawString(x + w / 2 + 6, y - 8, 'MANO IZQUIERDA')
        for off, esc, clef, dsub, dbaj, tit in ((0, ESC, 'treble', DIG_D_SUBE, DIG_D_BAJA, ''),
                                                (w / 2 + 6, ESC_B, 'bass', DIG_I_SUBE, DIG_I_BAJA, '')):
            ww = w / 2 - 12
            ys = draw_staff(c, x + off, y - 30, ww, g)
            draw_clef(c, x + off + 3, ys[-1], g, clef)
            x0 = x + off + 44
            paso = (ww - 50) / 8.0
            for k, p in enumerate(esc):
                cx = x0 + paso * (k + 0.5)
                draw_note(c, cx, ys[-1], ys[0], g, p, 'q', clef=clef, stem_dir='up' if True else None)
                c.setFont('DejaVuSans-Bold', 8)
                c.setFillColor(OCRE)
                c.drawCentredString(cx, ys[-1] - 23, str(dsub[k]))
            # bajada
            ys2 = draw_staff(c, x + off, y - 112, ww, g)
            draw_clef(c, x + off + 3, ys2[-1], g, clef)
            for k, p in enumerate(reversed(esc)):
                cx = x0 + paso * (k + 0.5)
                draw_note(c, cx, ys2[-1], ys2[0], g, p, 'q', clef=clef, stem_dir='up')
                c.setFont('DejaVuSans-Bold', 8)
                c.setFillColor(OCRE)
                c.drawCentredString(cx, ys2[-1] - 23, str(dbaj[k]))
    return Blk(h, f)


def lineas_pares():
    def f(c, x, y, w):
        cur0 = x + 4 + GAP * 5.4
        slot = (w - 8 - GAP * 5.4 - 4) / 8.0
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.6)
        for i in range(4):
            cx = cur0 + slot * (2 * i + 1)
            c.line(cx - 22, y - 12, cx + 22, y - 12)
    return Blk(20, f)


def construir(d):
    d.nuevo('Diciembre · Escala de Do mayor')
    d.add(banda_mes('Diciembre', '1.er trimestre', 'Escala de Do mayor',
                    'Ocho notas seguidas, una receta (tonos y semitonos) y una digitación: la base de todo lo que vendrá.'))
    d.add(caja('dato', 'La escala de Do mayor', [
        'Una **escala** es una sucesión de notas ordenadas de grave a agudo (o al revés). La de **Do mayor** es la más sencilla '
        'porque **no lleva ningún sostenido ni bemol**: son las **ocho teclas blancas** de un Do al siguiente: '
        '**DO – RE – MI – FA – SOL – LA – SI – DO**.',
        'Su sonido «de escala» sale de la **receta de distancias**: entre notas vecinas hay un **tono** (dos semitonos) salvo en '
        '**Mi–Fa** y **Si–Do**, donde hay un **semitono** (no hay tecla negra entre medias). Esa receta '
        '—**T T S T T T S**— define toda escala mayor, aunque empiece en otra nota.',
        'Es como aprender el abecedario de la música: se repite en muchas piezas.']),
        diag_escala(),
        caja('tip', 'Practicar la escala', [
            'Empieza **tocando despacio** cada nota y fíjate en los cambios de posición de los dedos. Repite varias veces hasta que puedas '
            'hacerla sin mirar. **Sube y baja** para sentir la dirección del sonido: es la misma escala, recorrida al revés.']))
    d.add(h2('Los números son la guía: la digitación'))
    d.add(diag_digitacion())
    d.add(par('Para llegar de un Do al siguiente con **cinco dedos**, la mano pasa **el pulgar por debajo** de los otros dedos '
              '(**paso del pulgar**): en la mano derecha, al subir, el pulgar entra en el Fa tras el 3; al bajar, el 3 pasa por encima del pulgar. '
              'En la izquierda ocurre al revés. Mueve el brazo con la mano, sin retorcer la muñeca.', 9.2, NAVY_SOFT))

    d.add(caja('nota', 'Cada nota tiene su grado', [
        'Las notas de la escala se numeran con cifras romanas, y varias tienen nombre propio: **I tónica** (la nota de la que parte la escala), '
        '**IV subdominante**, **V dominante** y **VII sensible** (a un semitono de la tónica, pide resolver en ella). '
        'Será el vocabulario de los acordes más adelante.']),
        tabla([90, 100, 170], [[g[0], g[1], g[2]] for g in GRADOS], ['Grado', 'Nota en Do mayor', 'Nombre'], alto=17, size=8.4))

    # ---- Ejercicio 1: secuencia de patrones
    d.add(ejercicio(1, 'Secuencia de patrones',
                    ['Escribe la escala de Do mayor **ascendente** y **descendente** con su digitación: la primera nota está puesta, '
                     'dibuja las demás y escribe el dedo sobre cada una.',
                     'Haz primero la clave de sol (mano derecha) y después la de fa (mano izquierda).'],
                    'Fortalecer la memoria musical y la capacidad de reconocer notas fuera de orden lineal.'))
    d.add(fila_notas('treble', ['C4'] + [None] * 7, 'q', bajo='linea', encima=[1] + [''] * 7, titulo='a) Mano derecha, subiendo (Do central → Do agudo)'))
    d.add(fila_notas('treble', ['C5'] + [None] * 7, 'q', bajo='linea', encima=[5] + [''] * 7, titulo='b) Mano derecha, bajando'))
    d.add(fila_notas('bass', ['C3'] + [None] * 7, 'q', bajo='linea', encima=[5] + [''] * 7, titulo='c) Mano izquierda, subiendo'))
    d.add(fila_notas('bass', ['C4'] + [None] * 7, 'q', bajo='linea', encima=[1] + [''] * 7, titulo='d) Mano izquierda, bajando'))
    sol(MES, 1, 'Secuencia de patrones',
        ['a) Do Re Mi Fa Sol La Si Do — dedos 1 2 3 1 2 3 4 5.   b) Do Si La Sol Fa Mi Re Do — 5 4 3 2 1 3 2 1.',
         'c) Do Re Mi Fa Sol La Si Do (grave) — dedos 5 4 3 2 1 3 2 1.   d) Do Si La Sol Fa Mi Re Do — 1 2 3 1 2 3 4 5.'])

    # ---- Ejercicio 2: patrones ritmicos
    d.add(ejercicio(2, 'La escala con ritmos',
                    ['Toca la escala de Do mayor (subiendo y bajando) con cada uno de estos ritmos: una nota por golpe. '
                     'Marca el pulso con el pie y no cambies de ritmo hasta que salga sin fallos.',
                     'Después **inventa tú un patrón** de dos compases con las figuras que quieras y tócalo con la escala.'],
                    'Que la escala deje de ser un ejercicio de dedos y se convierta en música, con pulso y con carácter.'))
    pats = [
        ('Negras: todas las notas iguales', [[('n', 'q')] * 4, [('n', 'q')] * 4]),
        ('Corcheas: dos notas por tiempo («ti-ti»)', [[('n', 'e')] * 8, [('n', 'e')] * 8]),
        ('Puntillo y corchea (salta: «ta-i ti»)', [[('n', 'q.'), ('n', 'e'), ('n', 'q.'), ('n', 'e')], [('n', 'q.'), ('n', 'e'), ('n', 'q.'), ('n', 'e')]]),
        ('Blanca y dos negras', [[('n', 'h'), ('n', 'q'), ('n', 'q')], [('n', 'h'), ('n', 'q'), ('n', 'q')]]),
    ]
    for k, (tit, comp) in enumerate(pats):
        d.add(fila_compases(comp, ts=(4, 4), titulo='%s) %s' % (SEC[k], tit)))
    d.add(pauta_vacia('treble', 2, (4, 4), titulo='e) Tu patrón'))
    sol(MES, 2, 'La escala con ritmos',
        ['Cada compás suma 4 tiempos. Con el ritmo a), 8 notas ocupan 2 compases; con b), 16 corcheas llenan 2 compases; '
         'en c) y d) cada compás reparte las notas por los patrones indicados y se repite la escala.'])

    # ---- Ejercicio 3: intervalos
    d.add(caja('dato', 'Intervalos: la distancia entre dos notas', [
        'Un **intervalo** es la distancia entre dos notas. Se cuenta **incluyendo las dos notas**: de Do a Mi hay tres notas '
        '(Do – Re – Mi), así que es un intervalo de **tercera** (3.ª). Se puede contar sobre el pentagrama: una nota en línea y la siguiente '
        'línea es una **tercera**; una línea y el siguiente espacio, una **segunda**.']),
        tabla([66, 56, 56, 56, 56, 56, 56, 89], [['Do – Do (igual)', 'Do – Re', 'Do – Mi', 'Do – Fa', 'Do – Sol', 'Do – La', 'Do – Si', 'Do – Do agudo'],
                                                  ['1.ª (unísono)', '2.ª', '3.ª', '4.ª', '5.ª', '6.ª', '7.ª', '8.ª (octava)']], None, alto=24, size=7.6, zebra=True))
    d.add(ejercicio(3, 'Secuencia de intervalos',
                    ['Escribe debajo de cada pareja de notas el intervalo que forman (2.ª, 3.ª, 4.ª, 5.ª, 6.ª, 7.ª u 8.ª). Cuenta incluyendo las dos notas.',
                     'Comprueba algunos en el teclado: coloca el dedo 1 en la primera nota y mira dónde cae la segunda.'],
                    'Medir distancias con la vista y con el oído: la base para leer en bloques y, más adelante, para los acordes.'))
    r = rnd(33)
    pares = []
    for _ in range(8):
        a = r.choice(['C4', 'D4', 'E4', 'F4', 'G4', 'A4'])
        k = r.choice([1, 2, 3, 4, 5, 6, 7])
        if _abs_idx(mover(a, k)) > _abs_idx('C6'):
            k = 2
        pares.append((a, mover(a, k)))
    # dos filas de 4 parejas: cada pareja = dos notas blancas (redondas) con una raya debajo
    sol3 = []
    for fila in range(2):
        sub = pares[fila * 4:(fila + 1) * 4]
        notas = [p for pr in sub for p in pr]
        d.add(fila_notas('treble', notas, 'w', bajo='nada', barras=2, titulo='%s)' % SEC[fila], ancho=CONTENT_W))
        d.add(lineas_pares())
        sol3.append('%s) ' % SEC[fila] + ' · '.join('%s–%s = %d.ª' % (nombre(a), nombre(b), (_abs_idx(b) - _abs_idx(a)) % 100 + 1) for a, b in sub))
    sol(MES, 3, 'Secuencia de intervalos', sol3)

    # ---- Ejercicio 4: mini melodia
    d.add(ejercicio(4, 'Mi mini melodía navideña',
                    ['Crea una melodía de **cuatro compases en 4/4** solo con las notas de la escala de Do mayor, en clave de sol. '
                     'Termina en **Do** (la tónica) para que suene «a final».',
                     'Ponle letra propia (o cambia la letra de una canción navideña que te guste) y tócala con la mano derecha.'],
                    'Usar la teoría para crear: es la mejor forma de comprobar que se ha entendido.'))
    ev = [{'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'h', 'number': 3},
          {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'h', 'number': 3},
          {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'G4', 'dur': 'q', 'number': 5}, {'pitch': 'C4', 'dur': 'q.', 'number': 1},
          {'pitch': 'D4', 'dur': 'e', 'number': 2}, {'pitch': 'E4', 'dur': 'w', 'number': 3}]
    d.add(Blk(110, lambda c, x, y, w: system_block(c, x, w, y, GAP + 0.6,
                                                  'Para inspirarte: «Jingle Bells» (J. Pierpont, 1857), primera frase', ev,
                                                  clef='treble', time_sig=(4, 4))))
    d.add(pauta_vacia('treble', 4, (4, 4), titulo='Tu melodía'),
          lineas_escribir(2, 'La letra', 22),
          caja('tip', 'Ideas para componer', [
              '▸ Empieza con un ritmo (por ejemplo, «ta ta ta-a») y colócale las notas después.',
              '▸ Mezcla **pasos** (notas vecinas) con algún **salto**; si todo son saltos suena nervioso, si todo son pasos, plano.',
              '▸ Repite una idea una vez: la repetición hace que la melodía se recuerde.',
              '▸ Comprueba que cada compás suma **4 tiempos** antes de tocarla.']))
    sol(MES, 4, 'Mi mini melodía navideña', ['Ejercicio libre. Criterios: cuatro compases de 4/4, solo notas de Do mayor, termina en Do.'])
