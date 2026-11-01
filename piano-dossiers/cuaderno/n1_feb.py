# -*- coding: utf-8 -*-
"""FEBRERO · Ritmo y subdivision."""
from n1_base import *
from fractions import Fraction

MES = 'Febrero'
SEC = 'abcdef'
N = lambda dd: ('n', dd)
R = lambda dd: ('r', dd)

# valor de cada figura en tiempos de negra (fracciones exactas)
VAL = {'redonda': Fraction(4), 'blanca': Fraction(2), 'negra': Fraction(1), 'corchea': Fraction(1, 2),
       'semicorchea': Fraction(1, 4), 'fusa': Fraction(1, 8)}
PLURAL = {'redonda': 'redondas', 'blanca': 'blancas', 'negra': 'negras', 'corchea': 'corcheas', 'semicorchea': 'semicorcheas',
          'fusa': 'fusas'}


def valor(n, fig, puntillo=False):
    v = VAL[fig] * n
    return v * Fraction(3, 2) if puntillo else v


def construir(d):
    d.nuevo('Febrero · Ritmo y subdivisión')
    d.add(banda_mes('Febrero', '2.º trimestre', 'Ritmo y subdivisión',
                    'Cada tiempo se puede partir en trozos iguales: la herramienta para leer ritmos rápidos sin perderse.'))
    d.add(caja('dato', 'Pulso, ritmo y subdivisión', [
        'El **pulso** es el latido constante de la música: lo que marcas con el pie. El **ritmo** es la combinación de duraciones '
        '(largas, cortas, silencios) que se dibuja **sobre** ese pulso. Y la **subdivisión** consiste en partir cada tiempo en partes iguales: '
        'en **dos** (corcheas) o en **cuatro** (semicorcheas).',
        'Por ejemplo, en un compás de 4/4 hay cuatro tiempos, y cada tiempo se puede tocar entero, partido en dos o partido en cuatro. '
        'Si mantienes el pulso mientras cambias la subdivisión, el ritmo se vuelve cada vez más rápido sin que la música se acelere.']),
        fila_compases([[N('q')] * 4, [N('e')] * 8, [N('s')] * 16], ts=(4, 4), titulo='Un mismo compás, tres maneras de llenarlo: 1 = negra · 2 = corcheas · 4 = semicorcheas',
                       rotulos=['ta  ta  ta  ta', 'ti-ti  ti-ti  ti-ti  ti-ti', 'ti-ka-ti-ka × 4'], ancho_rel=[0.9, 1.2, 2.4]),
        caja('tip', 'Las palabras tienen ritmo', [
            'Al igual que las palabras tienen sílabas, la música usa figuras para marcar los tiempos. **Relacionar palabras con duraciones** ayuda a entender '
            'cómo se leen y se sienten los sonidos musicales: «man-za-na» son tres sílabas, tres sonidos.',
            'Dos corcheas seguidas se unen con una **barra** horizontal: así se ve de un vistazo a qué tiempo pertenece cada una. '
            'Cuando la música se agrupa por tiempos, se lee mucho más rápido.']))

    # ---- Ejercicio 1: palabras y figuras
    d.add(ejercicio(1, 'Ritmo de palabras y figuras',
                    ['Cada palabra tiene un ritmo: una sílaba = un sonido. Di la palabra marcando el pulso con el pie y escribe su ritmo en el compás de al lado.',
                     'Marca con un círculo las sílabas que van **más largas**. Hay varias soluciones válidas.'],
                    'Visualizar el ritmo y sentir cómo se relaciona con las figuras.'))
    palabras = [('sol', 'q'), ('lu-na', 'qq'), ('pla-ta-no', 'eeq'), ('ma-ri-po-sa', 'eeee'), ('pia-no', 'qq'), ('me-lo-co-tón', 'eeqq')]
    filas = []
    sol_p = []
    for w_, patt in palabras:
        pass
    comp, rot = [], []
    for w_, patt in palabras:
        comp.append([('x', 4)])
        rot.append('«%s»' % w_)
    d.add(fila_compases(comp[0:3], ts=(4, 4), titulo='a)', rotulos=rot[0:3]),
          fila_compases(comp[3:6], ts=(4, 4), titulo='b)', rotulos=rot[3:6]))
    ritmos_txt = {'q': 'una negra («ta»)', 'qq': 'dos negras («ta ta»)', 'eeq': 'dos corcheas y una negra («ti-ti ta»)',
                  'eeee': 'cuatro corcheas («ti-ti ti-ti»)', 'eeqq': 'dos corcheas y dos negras («ti-ti ta ta»)'}
    sol(MES, 1, 'Ritmo de palabras', ['Una posibilidad: ' + ' · '.join('%s = %s' % (w_, ritmos_txt[p]) for w_, p in palabras) + '. Otras respuestas son válidas si cada sílaba lleva un sonido y el compás suma 4 tiempos (rellena con silencios si faltan).'])

    # ---- Ejercicio 2: ritmos del dia a dia
    d.add(ejercicio(2, 'Ritmos del día a día',
                    ['La música está en todas partes: en cómo caminamos, en el tic-tac del reloj, en las gotas de lluvia. Piensa en **tres cosas** que hagan sonidos repetidos.',
                     'Escribe debajo de cada una el ritmo que le pondrías con las figuras que conoces. Ejemplo: una pelota que bota rápido puede ser dos corcheas seguidas.'],
                    'Asociar el ritmo musical a la vida cotidiana y fomentar la creatividad auditiva.'))
    for k in range(3):
        d.add(lineas_escribir(1, '%d)  Sonido: ________________________________' % (k + 1), 18),
              pauta_vacia('treble', 2, (4, 4)))

    # ---- Ejercicio 3: que figura dura mas
    d.add(ejercicio(3, '¿Qué figura dura más?',
                    ['Compara las dos duraciones de cada fila y escribe en el círculo **>** (la primera dura más), **<** (dura menos) o **=** (dura lo mismo).',
                     'Si te cuesta, sube todo a «tiempos de negra» y suma: una corchea = ½, una semicorchea = ¼.'],
                    'Mantener el pulso constante mientras se manejan subdivisiones complejas.'))
    comps = [
        ((2, 'corchea', False), (1, 'negra', False)),
        ((1, 'blanca', False), (3, 'negra', False)),
        ((4, 'semicorchea', False), (1, 'negra', False)),
        ((1, 'negra', True), (3, 'corchea', False)),
        ((1, 'redonda', False), (2, 'blanca', False)),
        ((3, 'semicorchea', False), (1, 'corchea', False)),
        ((1, 'blanca', True), (2, 'negra', False)),
        ((6, 'semicorchea', False), (1, 'negra', True)),
    ]

    def txt(t):
        n, f_, pt = t
        base = ('%d %s' % (n, PLURAL[f_] if n > 1 else f_)) if n > 1 else ('1 %s' % f_)
        return base + (' con puntillo' if pt else '')
    filas = []
    sol3 = []
    for (a, b) in comps:
        va, vb = valor(*a), valor(*b)
        signo = '>' if va > vb else ('<' if va < vb else '=')
        sol3.append('%s %s %s' % (txt(a), signo, txt(b)))

        def circ(c, cx, cy, w, h):
            c.setStrokeColor(NAVY)
            c.setLineWidth(0.9)
            c.circle(cx, cy, 8, fill=0, stroke=1)
        filas.append([txt(a), circ, txt(b)])
    d.add(tabla([190, 40, 190], filas, ['Primera', '', 'Segunda'], alto=24, size=9.6, zebra=True))
    sol(MES, 3, '¿Qué figura dura más?', ['; '.join('%d) %s' % (i + 1, s_) for i, s_ in enumerate(sol3)) + '.'])

    # completar con subdivision
    d.add(par('**Completa con subdivisiones.** Rellena cada hueco usando el tipo de figura que se indica:', 9.4, INK, despues=4))
    sub = [((2, 4), [[N('q'), ('x', 1)]], 'con dos corcheas'),
           ((4, 4), [[N('q'), N('q'), ('x', 2)]], 'con semicorcheas (ocho)'),
           ((3, 4), [[N('e'), N('e'), N('e'), N('e'), ('x', 1)]], 'con una negra')]
    for k, (ts, comp, ind) in enumerate(sub):
        d.add(fila_compases(comp, ts=ts, titulo='%s) %d/%d: rellena %s' % (SEC[k], ts[0], ts[1], ind)))
    sol(MES, '3 (subdivisiones)', 'Completa con subdivisiones',
        ['a) dos corcheas (1 tiempo)  ·  b) ocho semicorcheas (2 tiempos)  ·  c) una negra (1 tiempo).'])

    # ---- Ejercicio 4: ritmo y palmas
    d.add(ejercicio(4, 'Ritmo y palmas',
                    ['Lee cada línea marcando el pulso con el pie y palmeando las figuras. Di las sílabas: negra = **ta**, dos corcheas = **ti-ti**, '
                     'cuatro semicorcheas = **ti-ka-ti-ka**.',
                     'Repite cada línea hasta que salga sin dudar, y después tócala con una sola nota en el piano.'],
                    'Desarrollar la percepción auditiva y la coordinación entre lectura, pulso y ejecución.'))
    lect = [
        ('a) 2/4 con corcheas', (2, 4), [[N('q'), N('e'), N('e')], [N('e'), N('e'), N('q')], [N('e'), N('e'), N('e'), N('e')], [N('q'), N('q')]]),
        ('b) 3/4 con silencios', (3, 4), [[N('q'), N('e'), N('e'), N('q')], [N('q'), R('q'), N('q')], [N('e'), N('e'), N('e'), N('e'), N('q')], [N('h'), R('q')]]),
        ('c) 4/4 con semicorcheas', (4, 4), [[N('s'), N('s'), N('s'), N('s'), N('q'), N('q'), N('q')], [N('q'), N('s'), N('s'), N('s'), N('s'), N('q'), N('q')],
                                            [N('e'), N('e'), N('s'), N('s'), N('s'), N('s'), N('q'), N('q')], [N('h'), N('q'), R('q')]]),
    ]
    for tit, ts, comp in lect:
        d.add(fila_compases(comp, ts=ts, titulo=tit))

    d.add(caja('piano', 'Al piano: la escala con metrónomo', [
        'Toca la escala de Do mayor (mano derecha, una octava) con **corcheas** y después con **semicorcheas**. '
        'Usa un metrónomo: empieza **despacio (♩ = 60)** y sube de **4 en 4** solo cuando la escala salga **limpia tres veces seguidas**. '
        'Apunta aquí hasta dónde llegas cada semana:'],),
          tabla([100, 100, 100, 100, 91], [['Semana', '1', '2', '3', '4'], ['♩ =', '', '', '', ''], ['Notas limpias (de 3)', '', '', '', '']],
                None, alto=22, zebra=False, size=8.4))
    sol(MES, 'Ritmo y palmas', 'Ritmo y palmas', ['Todos los compases suman los tiempos de su cifra (2, 3 o 4). Cuenta los silencios como si fueran sonidos.'])
