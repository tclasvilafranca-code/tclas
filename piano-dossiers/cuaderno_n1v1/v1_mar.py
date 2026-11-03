# -*- coding: utf-8 -*-
"""MARZO · Trabajando en clave de fa."""
from v1_base import *
from v1_base import _abs_idx
from page_layout_common import system_block

MES = 'Marzo'
SEC = 'abcdef'
N = lambda dd, p=None: ('n', dd) if p is None else ('n', dd, p)
R = lambda dd: ('r', dd)


def construir(d):
    d.nuevo('Marzo · Trabajando en clave de fa')
    d.add(banda_mes('Marzo', '2.º trimestre', 'Trabajando en clave de fa',
                    'Las notas graves y la mano izquierda: dónde viven y cómo se leen.'))
    d.add(caja('dato', 'La clave de fa', [
        'La clave de fa se usa para las **notas graves**: la mano izquierda del piano, el violonchelo, el trombón, el fagot o la tuba. '
        'Se dibuja al principio del pentagrama y sus **dos puntos rodean la 4.ª línea**, que corresponde a la nota **Fa**.',
        'Como en clave de sol, las notas siguen en orden: **líneas** (de abajo arriba) **Sol – Si – Re – Fa – La**; **espacios** '
        '**La – Do – Mi – Sol**. **Cuidado:** la misma posición no es la misma nota que en clave de sol: la 1.ª línea es **Mi** en sol y **Sol** en fa.',
        'En el piano se leen **las dos claves a la vez**, mano derecha en sol y mano izquierda en fa: trabajar así desarrolla la '
        'coordinación entre las manos y la memoria de trabajo, porque hay que leer dos líneas a la vez y ejecutarlas.']),
        fila_notas('bass', ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3'], 'w',
                   bajo=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol', 'La'],
                   titulo='Clave de fa: de la 1.ª línea (Sol) a la 5.ª (La), subiendo por línea y espacio'),
        caja('tip', 'Asociar las notas graves con la sensación física', [
            'Antes de tocar, **visualiza** la nota en el teclado y en tu mano izquierda (o en tu voz grave). Esa conexión entre vista, sonido '
            'y tacto refuerza la lectura. En los pasajes repetidos o rápidos, imagina el **movimiento de la mano** hacia esa posición: '
            'así no dependes solo de la vista y mantienes el pulso y la subdivisión.']))

    # ---- Ejercicio 1: identificacion de notas
    d.add(ejercicio(1, 'Identificación de notas',
                    ['Observa el pentagrama en clave de fa y escribe el nombre de cada nota.',
                     'Después coloca **las mismas notas en clave de sol** (en las filas de abajo): suenan igual, solo cambia cómo se escriben.'],
                    'Mejorar la rapidez y la precisión al identificar notas graves.'))
    r = rnd(301)
    pool_b = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'F2', 'E2']
    sol1 = []
    for k in range(2):
        ps = []
        while len(ps) < 8:
            p = r.choice(pool_b)
            if not ps or (p != ps[-1] and abs(_abs_idx(p) - _abs_idx(ps[-1])) <= 4):
                ps.append(p)
        d.add(fila_notas('bass', ps, 'q', bajo='linea', barras=4, titulo='%s) Escribe el nombre' % SEC[k]))
        sol1.append('%s) %s' % (SEC[k], ' · '.join(nombre(p) for p in ps)))
    # mismas notas en clave de sol (cuatro notas compartidas con el rango del pentagrama de sol)
    comp = ['G3', 'A3', 'B3', 'C4', 'D4', 'E4']
    d.add(gran_pauta_notas([None] * 6, comp, titulo='c) Mira las notas de fa y escríbelas en clave de sol (suenan igual)', linea_nombre=False))
    sol1.append('c) en sol, en el mismo orden: ' + ' · '.join('%s (%s)' % (nombre(p), posicion(p, 'treble')) for p in comp))
    sol(MES, 1, 'Identificación de notas', sol1)

    # ---- Ejercicio 2: secuencia ritmica
    d.add(ejercicio(2, 'Secuencia rítmica y subdivisión',
                    ['Mira los compases siguientes. Pulsa con la mano o el pie cada compás y **subdivide con un número** al tiempo más pequeño: '
                     '1 y 2 y 3 y… si hay corcheas.',
                     'Escribe debajo de cada tiempo su número y, si corresponde, «y». Después, tócalos en la mano izquierda sobre una sola nota.'],
                    'Desarrollar el pulso y la subdivisión en registros graves y mejorar la percepción rítmica.'))
    rit = [
        ('a) 4/4', (4, 4), [[N('q', 'D3'), N('q', 'D3'), N('h', 'D3')], [N('e', 'F3'), N('e', 'F3'), N('q', 'F3'), N('h', 'F3')],
                              [N('q', 'A2'), R('q'), N('q', 'A2'), R('q')]]),
        ('b) 3/4', (3, 4), [[N('q', 'D3'), N('q', 'D3'), N('q', 'D3')], [N('h', 'F3'), N('q', 'F3')], [N('e', 'A2'), N('e', 'A2'), N('e', 'A2'), N('e', 'A2'), N('q', 'A2')]]),
        ('c) 2/4', (2, 4), [[N('e', 'D3'), N('e', 'D3'), N('q', 'D3')], [N('q', 'F3'), N('e', 'F3'), N('e', 'F3')], [N('h', 'A2')]]),
    ]
    for tit, ts, comp_ in rit:
        d.add(fila_compases(comp_, ts=ts, clef='bass', pitch='D3', titulo=tit, rotulos=['______'] * len(comp_)))
    sol(MES, 2, 'Secuencia rítmica y subdivisión',
        ['Cuenta: 4/4 → «1 2 3 4»; 3/4 → «1 2 3»; 2/4 → «1 2». Con corcheas: «1 y 2 y …». Cada compás suma los tiempos de su cifra.'])

    # ---- Ejercicio 3: mini melodia
    d.add(ejercicio(3, 'Mini melodía',
                    ['Escribe las notas de la lista en clave de fa (el primer Sol es el de la 1.ª línea). Después pon las figuras y el compás que creas que lleva.',
                     '¿Reconoces la melodía? Inténtalo cantándola con el nombre de las notas y busca su título.'],
                    'Combinar la lectura de notas, la memoria auditiva y el control rítmico en las notas graves.'))
    melodia = [('SOL SOL SOL DO MI', ['G2', 'G2', 'G2', 'C3', 'E3']),
               ('SOL SOL SOL DO MI', ['G2', 'G2', 'G2', 'C3', 'E3']),
               ('DO DO SI SI LA LA SOL', ['C3', 'C3', 'B2', 'B2', 'A2', 'A2', 'G2'])]
    for k, (txt, ps) in enumerate(melodia):
        d.add(fila_notas('bass', [None] * len(ps), 'q', bajo=[nm.capitalize() for nm in txt.split()], titulo='%d)  %s' % (k + 1, txt)))
    d.add(lineas_escribir(1, 'Título de la melodía: ________________________________    Compás: ______', 22))
    sol(MES, 3, 'Mini melodía',
        ['Notas (clave de fa): ' + ' / '.join(' '.join('%s(%s)' % (nombre(p), posicion(p, 'bass')) for p in ps) for _, ps in melodia) +
         ''+ '. Las figuras y el compás los decides tú al reconocer la melodía.'])

    # ---- Ejercicio 4: transcripcion de sol a fa
    d.add(ejercicio(4, 'Transcripción de clave de sol a clave de fa',
                    ['Observa la melodía en clave de sol y **escríbela en clave de fa una octava más grave**: la misma melodía, pero más abajo en el teclado.',
                     'Para pasar de sol a fa una octava más grave, **cada nota baja siete posiciones** (una octava): el Mi de la 1.ª línea en sol pasa a ser el Mi del 3.er espacio en fa. ¡Comprueba con tu oído!'],
                    'Mejorar la coordinación entre la clave de sol y la de fa.'))
    t1 = ['E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4']
    t2 = ['C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'C5']
    d.add(gran_pauta_notas(t1, [None] * 8, titulo='a) Una octava más grave', linea_nombre=False, dur='q'))
    d.add(gran_pauta_notas(t2, [None] * 8, titulo='b) Una octava más grave', linea_nombre=False, dur='q'))
    sol(MES, 4, 'Transcripción de sol a fa',
        ['a) ' + ' · '.join('%s (%s)' % (nombre(mover(p, -7)), posicion(mover(p, -7), 'bass')) for p in t1),
         'b) ' + ' · '.join('%s (%s)' % (nombre(mover(p, -7)), posicion(mover(p, -7), 'bass')) for p in t2),
         'Una octava = siete notas diatónicas: se baja 7 pasos (de línea a espacio, siete veces).'])

    # ---- Al piano: mano izquierda
    d.add(caja('piano', 'Al piano: el Himno de la Alegría con la mano izquierda', [
        'Es la misma melodía de noviembre, **una octava más grave**, con la mano izquierda. Fíjate en los dedos: en la izquierda el **5** va en el Do y el **1** '
        'en el Sol. Primero despacio, después de memoria.']))
    himno = [('E3', 'q', 3), ('E3', 'q', 3), ('F3', 'q', 2), ('G3', 'q', 1), ('G3', 'q', 1), ('F3', 'q', 2), ('E3', 'q', 3), ('D3', 'q', 4),
             ('C3', 'q', 5), ('C3', 'q', 5), ('D3', 'q', 4), ('E3', 'q', 3), ('E3', 'q.', 3), ('D3', 'e', 4), ('D3', 'h', 4)]
    ev = [{'pitch': p, 'dur': dd, 'number': n} for p, dd, n in himno]
    d.add(Blk(110, lambda c, x, y, w: system_block(c, x, w, y, GAP + 0.6, 'Himno de la Alegría · mano izquierda', ev, clef='bass', time_sig=(4, 4))))
    sol(MES, 'Himno (mano izquierda)', 'Himno de la Alegría (izquierda)', ['Notas: Mi Mi Fa Sol · Sol Fa Mi Re · Do Do Re Mi · Mi. Re Re (una octava bajo la versión de noviembre).'])
