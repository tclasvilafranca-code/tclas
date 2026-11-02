# -*- coding: utf-8 -*-
"""OCTUBRE · Líneas, espacios y dirección de las notas."""
from k1_base import *
from k1_comun import *
from n1_base import _abs_idx

MES = 'Octubre'


def pares_mov(r, pool, n=6):
    movs = ['↑', '↓', '=', '↑', '↓', '=']
    r.shuffle(movs)
    out = []
    for m in movs[:n]:
        a = r.choice(pool[1:-1])
        if m == '=':
            b = a
        else:
            cand = [p for p in pool if (_abs_idx(p) > _abs_idx(a)) == (m == '↑') and p != a]
            b = r.choice(cand)
        out.append((a, b))
    return out


def K_pares(pares, gap=11.0):
    """Pares de notas con una casilla grande debajo donde el niño dibuja la flecha."""
    n = len(pares)
    h = 4 * gap + gap * 6.5 + 40

    def f(c, x, y, w):
        top = y - gap * 2
        yb = K.pauta(c, x, top, w, gap, 'treble')
        cur = x + 4 + gap * 5.4
        slot = (x + w - 10 - cur) / float(n)
        for k, (a, b) in enumerate(pares):
            cx = cur + slot * (k + 0.5)
            for dx, p in ((-slot * 0.2, a), (slot * 0.2, b)):
                cy = note_y(yb, gap, p, 'treble')
                for ly in ledger_lines_needed(yb, top, cy, gap):
                    trac(c, 1.0, NAVY_SOFT)
                    c.line(cx + dx - gap, ly, cx + dx + gap, ly)
                KB._cabeza(c, cx + dx, cy, gap, col_nota(p), plica=None)
            K.caseta(c, cx - 20, yb - gap * 4.2 - 36, 40, 36, 8)
    return Blk(h, f)


def construir(d):
    KB.MES_ACTUAL[0] = MES
    d.nuevo('Octubre')
    d.add(K_titulo('Octubre', 'Líneas, espacios y dirección', 'Este mes miro si una nota está en una línea o en un espacio, y si sube o baja.'),
          K_mussol('Una nota puede estar sobre una línea o en un espacio. También puede subir o bajar.'),
          K_panel('', 'MI PLAN DEL MES', [K_plan(['Distingo línea y espacio.', 'Veo si una nota sube, baja o se repite.', 'Dibujo notas que suben y notas que bajan.', 'Conozco las notas con rayita (líneas adicionales).'])]))
    d.nuevo()
    d.add(K_titulo('Octubre', 'Sube y baja', 'Cuanto más arriba está una nota, más aguda suena.'),
          K_mussol('Más arriba en el pentagrama: sonido más agudo. Más abajo: sonido más grave.'),
          K_panel('', 'MIRA', [K_notas('treble', ['C4', 'E4', 'G4', 'B4', 'D5', 'F5'], titulo='Suben: cada nota suena más aguda'), K_espacio(10),
                               K_notas('treble', ['F5', 'D5', 'B4', 'G4', 'E4', 'C4'], titulo='Bajan: cada nota suena más grave')]),
          K_cajita('RECUERDA', 'Líneas y espacios van subiendo. Arriba = agudo. Abajo = grave.'))
    d.nuevo()
    d.add(K_titulo('Octubre', 'Notas con rayita', 'Algunas notas no caben dentro del pentagrama.'),
          K_mussol('Si una nota está fuera del pentagrama, se le pone una rayita corta. Se llama línea adicional.'),
          K_panel('', 'MIRA', [K_notas('treble', ['C4', 'D4', 'A5', 'B5'], titulo='Rayita debajo y rayita encima'), K_espacio(4)]),
          K_cajita('RECUERDA', 'DO está justo debajo del pentagrama y lleva una rayita. Es el DO central del piano.'))

    # 1 linea o espacio
    r = rnd(104)
    ps = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5']
    notas = r.sample(ps, 6)
    actividad(d, 1, '¿Línea o espacio?', 'Mira si la nota está sobre una línea o entre dos líneas.',
              ['Mira cada nota.', 'Si está sobre una línea, escribe L en su casilla.', 'Si está en un espacio, escribe E.'],
              [K_notas('treble', notas, rotulos='caja', color=False, gap=12)])
    sol(MES, 1, '¿Línea o espacio?', ['L = línea, E = espacio: ' + ' · '.join('%s' % ('L' if (_abs_idx(p) - _abs_idx('E4')) % 2 == 0 else 'E') for p in notas)])

    # 2 notas en movimiento
    r = rnd(202)
    par6 = pares_mov(r, ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5'], 6)
    actividad(d, 2, 'Notas en movimiento', 'Cada pareja de notas hace un movimiento.',
              ['Mira las dos notas de cada pareja.', 'Si la segunda sube, dibuja una flecha hacia arriba ↑.', 'Si baja, flecha hacia abajo ↓. Si es la misma, un círculo ○.'],
              [K_pares(par6)])
    sol(MES, 2, 'Notas en movimiento', ['  '.join('↑' if _abs_idx(b) > _abs_idx(a) else ('↓' if _abs_idx(b) < _abs_idx(a) else '○') for a, b in par6)])

    # 3 camino ascendente / 4 descendente
    actividad(d, 3, 'Camino hacia arriba', 'Las notas suben como una escalera. Después de SI vuelve DO.',
              ['La primera nota de cada fila ya está dibujada.', 'Dibuja las siguientes, una más arriba cada vez.', 'Píntalas de su color.'],
              [K_notas('treble', ['C4'] + [None] * 7, nombres=NOMBRES + ['DO'], titulo='A) Desde DO'), K_espacio(6),
               K_notas('treble', ['D4'] + [None] * 7, nombres=NOMBRES[1:] + ['DO', 'RE'], titulo='B) Desde RE')])
    sol(MES, 3, 'Camino hacia arriba', ['A) DO RE MI FA SOL LA SI DO · B) RE MI FA SOL LA SI DO RE'])
    d.nuevo('Octubre')
    d.add(K_titulo('Octubre', 'Pausa', 'Es momento de mover el cuerpo.'), K_mussol('Hacemos una pausa.'), K_pausa(1))
    actividad(d, 4, 'Camino hacia abajo', 'Ahora las notas bajan, como la lluvia.',
              ['La primera nota de cada fila ya está dibujada.', 'Dibuja las siguientes, una más abajo cada vez.', 'Píntalas de su color.'],
              [K_notas('treble', ['C5'] + [None] * 7, nombres=['DO', 'SI', 'LA', 'SOL', 'FA', 'MI', 'RE', 'DO'], titulo='A) Desde DO'), K_espacio(6),
               K_notas('treble', ['D5'] + [None] * 7, nombres=['RE', 'DO', 'SI', 'LA', 'SOL', 'FA', 'MI', 'RE'], titulo='B) Desde RE')])
    sol(MES, 4, 'Camino hacia abajo', ['A) DO SI LA SOL FA MI RE DO · B) RE DO SI LA SOL FA MI RE'])
    d.nuevo()
    d.add(K_titulo('Octubre', 'Mis logros', 'Mira todo lo que has hecho este mes.'), K_mussol('Pinta una casilla por cada cosa que ya sabes.'),
          K_panel('', 'TABLERO', [K_tablero('octubre', ['Sé si una nota está en línea o en espacio.', 'Sé si una nota sube o baja.', 'Sé dibujar un camino hacia arriba.', 'Sé dibujar un camino hacia abajo.', 'Sé qué es una rayita adicional.'])]))
