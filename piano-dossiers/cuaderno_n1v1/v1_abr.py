# -*- coding: utf-8 -*-
"""ABRIL · Recordamos los silencios musicales."""
from v1_base import *
from v1_base import _abs_idx
from page_layout_common import system_block
from v1_sep import fig_celda

MES = 'Abril'
SEC = 'abcdef'
N = lambda dd, p=None: ('n', dd) if p is None else ('n', dd, p)
R = lambda dd: ('r', dd)


def construir(d):
    d.nuevo('Abril · Silencios musicales')
    d.add(banda_mes('Abril', '3.er trimestre', 'Recordamos los silencios',
                    'Cuando no suena nada, la música sigue: cómo se escriben, cómo se cuentan y para qué sirven.'))
    d.add(caja('dato', 'Un silencio es música también', [
        'En música hay momentos de silencio, y tienen un **valor rítmico igual** que el de las figuras. Cada figura tiene su silencio: '
        'redonda, blanca, negra, corchea, semicorchea, fusa y semifusa.',
        'Dos reglas de escritura que conviene no olvidar: el silencio de **redonda cuelga** de la 4.ª línea y el de **blanca se apoya** en la 3.ª. '
        'Y un detalle muy útil: el **silencio de redonda** sirve para indicar **un compás entero de silencio**, sea cual sea el compás '
        '(2/4, 3/4, 4/4…), no solo cuando dura cuatro tiempos.']),
        tabla([100, 190, 110, 91], [[fig_celda(x, True), NOM_SIL[x], FIG[x][4], fig_celda(x)] for x in ['w', 'h', 'q', 'e', 's']],
              ['Silencio', 'Nombre', 'Dura', 'Figura'], alto=30, size=8.6),
        caja('tip', 'Pausas mágicas', [
            'En música, **el silencio vale tanto como su figura**. Piensa en los silencios como **pausas mágicas** en las que no se toca, pero la música sigue sonando '
            'dentro de ti. **Respetarlos** es lo que hace que una pieza suene bien: un silencio acortado o ignorado es la señal más clara de que se está '
            'tocando «a trompicones».']))

    # ---- Ejercicio 1
    d.add(ejercicio(1, 'Elige el silencio correcto',
                    ['Une cada figura con el silencio que dura lo mismo.',
                     'Después rellena los huecos de los compases con **silencios** que completen el tiempo que falta.'],
                    'Comprender la función y la duración de los silencios en un compás.'))
    orden = ['q', 'h', 'e', 'w', 's']
    r = rnd(4)
    der = list(orden)
    r.shuffle(der)
    d.add(une([fig_celda(x) for x in orden], [fig_celda(x, True) for x in der], alto=32, izq_w=80, der_w=80, hueco=140))
    sol(MES, 1, 'Une figuras y silencios',
        ['Cada figura se une con el silencio del mismo nombre: ' + ' · '.join('%s ↔ %s' % (NOM_FIG[x].lower(), NOM_SIL[x].lower()) for x in orden) + '.'])
    rell = [
        ((3, 4), [[N('q'), ('x', 2)], [N('h'), ('x', 1)]], ['silencio de blanca', 'silencio de negra']),
        ((4, 4), [[N('h'), ('x', 2)], [N('q'), N('q'), ('x', 2)]], ['silencio de blanca', 'dos silencios de negra']),
    ]
    sol1 = []
    for k, (ts, comp, resp) in enumerate(rell):
        d.add(fila_compases(comp, ts=ts, titulo='%s) %d/%d' % (SEC[k], ts[0], ts[1])))
        sol1.append('%s) %d/%d: ' % (SEC[k], ts[0], ts[1]) + ' y '.join(resp) + ' (o combinaciones equivalentes).')
    sol(MES, '1 (huecos)', 'Rellena con silencios', sol1)

    # ---- Ejercicio 2: huecos ocultos
    d.add(ejercicio(2, 'Huecos ocultos',
                    ['En estos compases faltan silencios. Observa y completa los huecos con el silencio correcto para que cada compás sume sus tiempos.',
                     'Después escribe debajo el nombre de las notas (clave de fa).'],
                    'Entender cómo los silencios completan el ritmo en un compás.'))
    hu = [
        ((3, 4), [[N('q', 'A2'), ('x', 1), N('q', 'F3')], [N('h', 'D3'), ('x', 1)]]),
        ((4, 4), [[N('q', 'G2'), N('q', 'B2'), ('x', 2)], [('x', 1), N('q', 'D3'), N('h', 'F3')]]),
        ((2, 4), [[N('e', 'A3'), N('e', 'F3'), ('x', 1)], [('x', 1), N('q', 'D3')]]),
    ]
    sol2 = []
    for k, (ts, comp) in enumerate(hu):
        d.add(fila_compases(comp, ts=ts, clef='bass', titulo='%s) %d/%d' % (SEC[k], ts[0], ts[1]),
                            rotulos=['_____ _____ _____'] * len(comp)))
        sol2.append('%s) %d/%d: huecos de %s' % (SEC[k], ts[0], ts[1], ' y '.join('%g tiempo%s' % (it[1], '' if it[1] == 1 else 's') for m in comp for it in m if it[0] == 'x')))
    sol(MES, 2, 'Huecos ocultos', sol2 + ['Un hueco de 1 tiempo = silencio de negra; de 2 tiempos = silencio de blanca. Notas: A2 La · F3 Fa · D3 Re · G2 Sol · B2 Si · A3 La.'])

    # ---- Ejercicio 3: suena o calla
    d.add(ejercicio(3, '¿Suena o calla?',
                    ['Observa cada compás. Cuenta **cuántas notas suenan**, **cuántos silencios** hay y **cuántos tiempos callan** en total.',
                     'Escribe los tres números debajo.'],
                    'Reforzar la distinción entre sonidos y silencios y la lectura rítmica.'))
    cs = [
        ((4, 4), [[N('q'), R('q'), N('h')], [R('h'), N('q'), N('q')], [N('e'), N('e'), R('q'), N('h')]]),
        ((3, 4), [[N('h'), R('q')], [R('q'), N('q'), N('q')], [N('q'), R('q'), R('q')]]),
    ]
    sol3 = []
    for k, (ts, comp) in enumerate(cs):
        rot = ['suenan __  silencios __  callan __ t.'] * len(comp)
        d.add(fila_compases(comp, ts=ts, titulo='%s) %d/%d' % (SEC[k], ts[0], ts[1]), rotulos=rot))
        parts = []
        for j, m in enumerate(comp):
            parts.append('c.%d: suenan %d, silencios %d, callan %g' % (j + 1, sum(1 for it in m if it[0] == 'n'), sum(1 for it in m if it[0] == 'r'),
                                                                     sum(BEATS[it[1]] for it in m if it[0] == 'r')))
        sol3.append('%s) %s' % (SEC[k], ' · '.join(parts)))
    sol(MES, 3, '¿Suena o calla?', sol3)

    # ---- Ejercicio 4: imaginando compases
    d.add(ejercicio(4, 'Imaginando compases',
                    ['Compón dos compases con **notas, figuras y silencios**: uno para la mano derecha (clave de sol) y otro para la izquierda (clave de fa). '
                     'Usa al menos **dos silencios**.',
                     'Dale un título que lo inspire (alegre, tranquilo, misterioso…) y toca tu composición en el teclado.'],
                    'Aplicar el conocimiento creando un ritmo con notas, figuras y silencios.'))
    d.add(pauta_piano_vacia(2, (4, 4), titulo='Título: ________________________________'))
    sol(MES, 4, 'Imaginando compases', ['Ejercicio libre. Criterio: cada compás suma 4 tiempos y hay al menos dos silencios.'])

    # ---- Al piano
    d.add(caja('piano', 'Al piano: una pieza con silencios', [
        'Pieza corta para la **mano derecha**, posición de Do. Los silencios son parte de la música: **cuéntalos en voz alta** («1 2 3 4») '
        'y levanta suavemente la mano en cada uno.']))
    ev = [{'pitch': 'C4', 'dur': 'q', 'number': 1}, {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'G4', 'dur': 'h', 'number': 5},
          {'pitch': 'G4', 'dur': 'q', 'number': 5}, {'rest': True, 'dur': 'q'}, {'pitch': 'E4', 'dur': 'h', 'number': 3},
          {'pitch': 'F4', 'dur': 'q', 'number': 4}, {'pitch': 'D4', 'dur': 'q', 'number': 2}, {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'rest': True, 'dur': 'q'},
          {'pitch': 'C4', 'dur': 'w', 'number': 1}]
    d.add(Blk(110, lambda c, x, y, w: system_block(c, x, w, y, GAP + 0.6, 'Pieza con silencios (T-Clas, para este cuaderno)', ev,
                                                  clef='treble', time_sig=(4, 4))))
    sol(MES, 'Pieza con silencios', 'Pieza con silencios', ['Cuatro compases de 4/4: C E G(h) · G r E(h) · F D E r · C(w).'])
