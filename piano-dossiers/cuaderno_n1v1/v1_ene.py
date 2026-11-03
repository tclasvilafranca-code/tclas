# -*- coding: utf-8 -*-
"""ENERO · Introduccion a los compases."""
from v1_base import *
from v1_base import _abs_idx
from fractions import Fraction

MES = 'Enero'
SEC = 'abcdef'
N = lambda dd, p=None: ('n', dd) if p is None else ('n', dd, p)
R = lambda dd: ('r', dd)


def suma(items):
    return sum(BEATS[i[1]] for i in items)


def gen_compas(r, bpb, pool, silencios=False):
    """Un compas que suma exactamente bpb tiempos con figuras de pool (y silencios opcionales)."""
    out = []
    quedan = bpb
    while quedan > 1e-9:
        cand = [d_ for d_ in pool if BEATS[d_] <= quedan + 1e-9]
        dd = r.choice(cand)
        kind = 'r' if (silencios and r.random() < 0.18 and out and out[-1][0] != 'r') else 'n'
        out.append((kind, dd))
        quedan -= BEATS[dd]
    return out


def construir(d):
    d.nuevo('Enero · Introducción a los compases')
    d.add(banda_mes('Enero', '2.º trimestre', 'Introducción a los compases',
                    'Cómo se organiza el tiempo: tiempos fuertes y débiles, las cifras del principio y las barras que separan los compases.'))
    d.add(caja('dato', 'El compás: una caja de tiempos', [
        'Un **compás** es una unidad de medida que organiza el tiempo de forma precisa. Funciona como una **caja** con un número '
        'determinado de tiempos, y las **barras de compás** (líneas verticales) la separan de la siguiente.',
        'Al principio de la pieza, tras la clave, hay **dos cifras** una sobre otra. La de **arriba** dice **cuántos tiempos** tiene cada '
        'compás; la de **abajo** dice **qué figura vale un tiempo** (4 = la negra, 2 = la blanca, 8 = la corchea).',
        'Los compases simples más habituales: **2/4** (dos tiempos), **3/4** (tres) y **4/4** (cuatro; también se escribe con una **C**). '
        'La duración de las notas y silencios de cada compás debe **sumar exactamente** esos tiempos.']),
        fila_compases([[N('q'), N('q')], [N('h')]], ts=(2, 4), titulo='2/4 · dos negras por compás (o una blanca)',
                      rotulos=['1  2', '1—2']),
        fila_compases([[N('q'), N('q'), N('q')], [N('h'), N('q')]], ts=(3, 4), titulo='3/4 · tres negras por compás',
                      rotulos=['1  2  3', '1—2  3']),
        fila_compases([[N('q'), N('q'), N('q'), N('q')], [N('h'), N('h')]], ts=(4, 4), titulo='4/4 · cuatro negras por compás',
                      rotulos=['1  2  3  4', '1—2  3—4']),
        caja('tip', 'El primer tiempo manda', [
            'En cada compás, el **primer tiempo es el más fuerte** (se acentúa un poco): **fuerte–débil** en 2/4, **fuerte–débil–débil** en 3/4 '
            '(como un vals) y **fuerte–débil–semifuerte–débil** en 4/4. Cuenta en voz alta con esa intención: la música «respira» así.',
            'En clave de lectura, **los silencios valen lo mismo que las figuras** a las que sustituyen: un silencio de blanca llena 2 tiempos de un compás igual que lo haría una blanca.']))

    # ---- Ejercicio 1: completa el compas
    d.add(ejercicio(1, 'Completa el compás',
                    ['Cada compás tiene un hueco punteado. Escribe en él las figuras o silencios que faltan para que el compás sume los tiempos de su cifra.',
                     'Hay muchas respuestas correctas: lo importante es que la suma salga exacta.'],
                    'Aprender a sumar duraciones hasta llenar un compás.'))
    ej1 = [
        ((2, 4), [[N('q'), ('x', 1)], [N('e'), N('e'), R('e'), ('x', 0.5)]]),
        ((3, 4), [[N('q'), N('q'), ('x', 1)], [N('h'), ('x', 1)]]),
        ((4, 4), [[N('q'), N('q'), ('x', 2)], [N('h.'), ('x', 1)]]),
    ]
    sol1 = []
    for k, (ts, comp) in enumerate(ej1):
        faltan = []
        for m in comp:
            f_ = sum(it[1] for it in m if it[0] == 'x')
            faltan.append('faltan %s tiempo%s' % (('%g' % f_).replace('0.5', '½').replace('.5', ' ½'), '' if f_ == 1 else 's'))
        d.add(fila_compases(comp, ts=ts, titulo='%s) Compás de %d/%d' % (SEC[k], ts[0], ts[1]), rotulos=faltan))
        sol1.append('%s) %d/%d: ' % (SEC[k], ts[0], ts[1]) + ' · '.join('compás %d: faltan %g (p. ej. %s)' % (j + 1, sum(it[1] for it in m if it[0] == 'x'),
                    {0.5: 'una corchea', 1: 'una negra o dos corcheas', 2: 'una blanca o dos negras'}[sum(it[1] for it in m if it[0] == 'x')]) for j, m in enumerate(comp)))
    sol(MES, 1, 'Completa el compás', sol1)

    # ---- Ejercicio 2: compases secretos
    d.add(ejercicio(2, 'Compases secretos',
                    ['Estos compases no llevan cifra. Suma los tiempos de cada uno y escribe debajo de qué compás se trata (2/4, 3/4 o 4/4).',
                     'Recuerda que en estos compases un tiempo es una negra.'],
                    'Desarrollar el conteo mental del ritmo y relacionar figuras con estructura.'))
    r = rnd(12)
    sec2 = [[N('h'), N('q')], [N('q'), N('q')], [N('e'), N('e'), N('q'), N('q')],
            [N('h'), N('h')], [N('q.'), N('e'), N('q')], [N('q'), N('q'), R('q'), N('q')], [N('e'), N('e'), N('e'), N('e'), N('q')],
            [N('h'), R('q')], [N('w')]]
    sol2 = []
    for k in range(3):
        grp = sec2[k * 3:(k + 1) * 3]
        d.add(fila_compases(grp, ts=None, titulo='%s)' % SEC[k], rotulos=['_____ / _____'] * 3))
        sol2.append('%s) ' % SEC[k] + ' · '.join('%g → %s' % (suma(m), {2: '2/4', 3: '3/4', 4: '4/4'}[int(suma(m))]) for m in grp))
    sol(MES, 2, 'Compases secretos', sol2)

    # ---- Ejercicio 3: divisiones musicales
    d.add(ejercicio(3, 'Divisiones musicales: las barras de compás',
                    ['Cada línea es una melodía escrita de seguido, sin barras. Dibuja con lápiz las **líneas divisorias** donde correspondan según la cifra de compás.',
                     'Comprueba que lo que queda entre dos barras suma exactamente los tiempos del compás.'],
                    'Aprender a separar compases: es lo primero que se hace al estudiar una partitura sin barras.'))
    r = rnd(77)
    plant = {(2, 4): [['q', 'q'], ['h'], ['e', 'e', 'q'], ['q', 'e', 'e']],
             (3, 4): [['q', 'q', 'q'], ['h', 'q'], ['q', 'h'], ['e', 'e', 'q', 'q'], ['q', 'e', 'e', 'q'], ['h.']],
             (4, 4): [['q', 'q', 'h'], ['h', 'h'], ['q', 'q', 'q', 'q'], ['e', 'e', 'q', 'h'], ['h', 'q', 'e', 'e'], ['q.', 'e', 'h']]}
    sol3 = []
    for k, (ts, nb) in enumerate([((2, 4), 4), ((3, 4), 4), ((4, 4), 3)]):
        bpb = ts[0] * 4.0 / ts[1]
        items, marks, t, ant = [], [], 0.0, None
        for _ in range(nb):
            m = r.choice([p for p in plant[ts] if p != ant])
            ant = m
            items.extend(('n', dd) for dd in m)
            t += bpb
            marks.append(t)
        d.add(fila_compases([items], ts=ts, titulo='%s) Compás de %d/%d: pon %d barras' % (SEC[k], ts[0], ts[1], nb - 1)))
        sol3.append('%s) %d/%d: barras tras los tiempos %s' % (SEC[k], ts[0], ts[1], ', '.join('%g' % m for m in marks[:-1])))
    sol(MES, 3, 'Divisiones musicales', sol3)

    # ---- Ejercicio 4: intruso
    d.add(ejercicio(4, 'Descubre al intruso',
                    ['En cada compás hay **una figura que sobra**: con ella, el compás se pasa de tiempos. Táchala y comprueba que sin ella la suma sale exacta.',
                     'Escribe debajo cuánto valía la figura que sobraba.'],
                    'Comprobar las igualdades entre tiempos y compases.'))
    e4 = [((2, 4), [[N('h'), N('q')], [N('q'), N('h')]], ['negra', 'negra']),
          ((3, 4), [[N('h'), N('q'), N('e'), N('e')], [N('h.'), N('q')]], ['negra', 'negra']),
          ((4, 4), [[N('h'), N('q'), N('q'), N('e')], [N('w'), N('q')]], ['corchea', 'negra'])]
    sol4 = []
    for k, (ts, comp, resp) in enumerate(e4):
        d.add(fila_compases(comp, ts=ts, titulo='%s) Compás de %d/%d' % (SEC[k], ts[0], ts[1]), rotulos=['sobra: ______________'] * 2))
        sol4.append('%s) %d/%d: sobra una %s en cada compás (%s).' % (SEC[k], ts[0], ts[1], resp[0] if resp[0] == resp[1] else '%s y una %s' % (resp[0], resp[1]),
                    ', '.join('suma %g = %g + %g' % (suma(m), suma(m) - (0.5 if rr == 'corchea' else 1), 0.5 if rr == 'corchea' else 1) for m, rr in zip(comp, resp))))
    sol(MES, 4, 'Descubre al intruso', sol4)

    # ---- Palmas por compases y dictado
    d.add(caja('piano', 'Lectura rítmica por compases', [
        'Lee cada línea marcando **el primer tiempo de cada compás con más fuerza**: así sentirás el compás. '
        'Cuenta en voz alta «1 2», «1 2 3» o «1 2 3 4», palmea las notas y abre las manos en los silencios.']))
    lect = [
        ((2, 4), [[N('q'), N('q')], [N('e'), N('e'), N('q')], [N('q'), R('q')], [N('h')]]),
        ((3, 4), [[N('q'), N('q'), N('q')], [N('h'), N('q')], [N('q'), N('e'), N('e'), N('q')], [N('h.')]]),
        ((4, 4), [[N('q'), N('q'), N('h')], [N('e'), N('e'), N('q'), R('q'), N('q')], [N('q.'), N('e'), N('h')], [N('w')]]),
    ]
    for k, (ts, comp) in enumerate(lect):
        d.add(fila_compases(comp, ts=ts, titulo='%s) %d/%d' % (SEC[k], ts[0], ts[1])))
    d.add(h2('Dictado rítmico'))
    d.add(par('Tu profesor o un compañero toca (o palmea) un ritmo de **dos compases**. Escríbelo aquí. Primero decide **en qué compás** va.', 9.2),
          pauta_vacia('treble', 2, None, titulo='1)'), pauta_vacia('treble', 2, None, titulo='2)'))
    sol(MES, 'Lectura rítmica y dictado', 'Lectura rítmica y dictado',
        ['Líneas a), b) y c): cada compás suma 2, 3 y 4 tiempos respectivamente. El dictado es libre: lo corrige el profesor.'])
