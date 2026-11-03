# -*- coding: utf-8 -*-
"""OCTUBRE · Lineas adicionales superiores e inferiores."""
from v1_base import *
from v1_base import _abs_idx

MES = 'Octubre'
SEC = 'abcdef'


def seq(inicio, n, sube=True):
    return [mover(inicio, k if sube else -k) for k in range(n)]


def construir(d):
    d.nuevo('Octubre · Líneas adicionales')
    d.add(banda_mes('Octubre', '1.er trimestre', 'Líneas adicionales',
                    'Las notas que se salen del pentagrama por arriba y por abajo, y cómo leerlas sin contar desde cero.'))
    d.add(caja('dato', 'Más allá de las cinco líneas', [
        'El pentagrama solo tiene cinco líneas, pero el piano tiene muchas más notas. Para escribir las que quedan fuera '
        'se añaden unos trazos cortos: las **líneas adicionales**. Se dibujan **igual de separadas que las del pentagrama** y '
        'cada nota lleva solo las que necesita para llegar hasta ella.',
        'Cuanto más arriba se escribe una nota, **más aguda**; cuanto más abajo, **más grave**. Las líneas adicionales '
        'pueden ser **superiores** (por encima de la 5.ª línea) o **inferiores** (por debajo de la 1.ª).']),
        fila_notas('treble', ['A3', 'B3', 'C4', 'D4', 'G5', 'A5', 'B5', 'C6'], 'w',
                   bajo=['La', 'Si', 'Do', 'Re', 'Sol', 'La', 'Si', 'Do'],
                   titulo='Clave de sol: dos adicionales inferiores (La, Do central) y dos superiores (La, Do agudo)'),
        fila_notas('bass', ['C2', 'D2', 'E2', 'F2', 'B3', 'C4', 'D4', 'E4'], 'w',
                   bajo=['Do', 'Re', 'Mi', 'Fa', 'Si', 'Do', 'Re', 'Mi'],
                   titulo='Clave de fa: el mismo Do central cuelga ahora de la 1.ª línea adicional superior'),
        caja('nota', 'El Do central, la nota que las dos claves comparten', [
            'En clave de sol, el **Do central** está en la 1.ª línea adicional **inferior**; en clave de fa, en la 1.ª línea '
            'adicional **superior**. Es **la misma nota** y la misma tecla del piano (la del centro del teclado): '
            'por eso se llama «central». Lo comprobarás con ejercicios en este mes y al tocar en noviembre.',
            'La clave de fa se estudia a fondo en marzo. Como adelanto, sus **líneas** (de abajo arriba) son '
            '**Sol – Si – Re – Fa – La** y sus **espacios**, **La – Do – Mi – Sol**.']))

    d.add(caja('tip', 'Analizando las notas adicionales en la partitura', [
        '▸ Antes de tocar, **localiza** las notas adicionales y **cuenta cuántas líneas** tienen, por encima o por debajo.',
        '▸ Apóyate en **notas guía**: Do central (1.ª adicional inferior en sol), La agudo (1.ª adicional superior) y Do agudo (2.ª). '
        'Desde una guía, sube o baja nota a nota hasta la tuya.',
        '▸ Escribe a lápiz el nombre de las notas adicionales en tu partitura hasta que no lo necesites.']))

    # ---- Ejercicio 1: linea o espacio
    d.add(ejercicio(1, '¿Línea o espacio?',
                    ['Mira cada nota: todas están fuera del pentagrama. Sobre la raya escribe **L** si está sobre una línea '
                     'adicional o **E** si está en un espacio, y después su nombre (por ejemplo: L · Do).',
                     'Rodea de azul las que están en línea y de verde las que están en espacio, si quieres reforzar la vista.'],
                    'Distinguir de un vistazo si la nota ocupa línea o espacio, aunque no haya pentagrama alrededor.'))
    r = rnd(104)
    pool_t = ['A3', 'B3', 'C4', 'D4', 'G5', 'A5', 'B5', 'C6']
    pool_b = ['C2', 'D2', 'E2', 'F2', 'B3', 'C4', 'D4', 'E4']
    sol1 = []
    for k, (clef, pool, tit) in enumerate([('treble', pool_t, 'Clave de sol'), ('treble', pool_t, 'Clave de sol'),
                                          ('bass', pool_b, 'Clave de fa')]):
        ps = r.sample(pool, 8)
        d.add(fila_notas(clef, ps, 'q', bajo='linea', titulo='%s) %s' % (SEC[k], tit), caja_ancho=40))
        sol1.append('%s) %s' % (SEC[k], ' · '.join('%s %s' % ('L' if (_abs_idx(p) - (_abs_idx('E4') if clef == 'treble' else _abs_idx('G2'))) % 2 == 0 else 'E', nombre(p)) for p in ps)))
    sol(MES, 1, '¿Línea o espacio?', sol1)

    # ---- Ejercicio 2: movimiento
    d.add(ejercicio(2, 'Notas en movimiento',
                    ['Cada par de notas es un movimiento. Dibuja en la casilla: una flecha **hacia arriba** si la segunda nota es más aguda, '
                     '**hacia abajo** si es más grave, o un **círculo** si se queda a la misma altura.',
                     'Después, di el nombre de las dos notas en voz alta.'],
                    'Percibir hacia dónde va la melodía antes de saber qué nota es: la base de leer a primera vista.'))
    r = rnd(202)
    sol2 = []
    for k, clef in enumerate(['treble', 'treble', 'bass']):
        pool = pool_t + ['E4', 'G4', 'C5'] if clef == 'treble' else pool_b + ['G2', 'D3', 'A3']
        pares = []
        movs = ['↑', '↓', '=', '↑', '↓', '=']
        r.shuffle(movs)
        for m in movs:
            a = r.choice(pool)
            if m == '=':
                b = a
            else:
                cand = [p for p in pool if (_abs_idx(p) > _abs_idx(a)) == (m == '↑') and p != a]
                b = r.choice(cand) if cand else a
            pares.append((a, b))
        d.add(fila_pares(clef, pares, titulo='%s) %s' % (SEC[k], 'Clave de sol' if clef == 'treble' else 'Clave de fa')))
        sol2.append('%s) ' % SEC[k] + '  '.join('%s' % ('↑' if _abs_idx(b) > _abs_idx(a) else ('↓' if _abs_idx(b) < _abs_idx(a) else '○')) for a, b in pares))
    sol(MES, 2, 'Notas en movimiento', sol2 + ['↑ sube · ↓ baja · ○ se repite.'])

    # ---- Ejercicios 3 y 4: caminos
    d.add(ejercicio(3, 'Camino musical ascendente',
                    ['La primera nota de cada camino ya está escrita. **Sube** nota a nota hasta completar ocho: dibuja cada nota '
                     'en el pentagrama y escribe su nombre debajo.',
                     'Sube siempre una línea o un espacio cada vez, sin saltarte ninguno.'],
                    'Asociar el movimiento ascendente con el espacio del pentagrama y practicar la escala de cualquier punto.'))
    sol3 = []
    for k, (clef, ini) in enumerate([('treble', 'A3'), ('bass', 'E2'), ('treble', 'C4')]):
        ps = seq(ini, 8, True)
        d.add(fila_notas(clef, [ps[0]] + [None] * 7, 'w', bajo='linea', titulo='%s) Empieza en %s' % (SEC[k], nombre(ini))))
        sol3.append('%s) %s' % (SEC[k], ' · '.join(nombre(p) for p in ps)))
    sol(MES, 3, 'Camino ascendente', sol3)
    d.add(ejercicio(4, 'Camino musical descendente',
                    ['Ahora al revés: **baja** nota a nota hasta completar ocho. Dibuja cada nota y escribe su nombre.',
                     'Si te pierdes, vuelve a la nota guía más cercana (Do central o La agudo) y sigue desde ahí.'],
                    'Dominar la dirección contraria, que casi siempre cuesta más.'))
    sol4 = []
    for k, (clef, ini) in enumerate([('treble', 'C6'), ('bass', 'E4'), ('treble', 'G4')]):
        ps = seq(ini, 8, False)
        d.add(fila_notas(clef, [ps[0]] + [None] * 7, 'w', bajo='linea', titulo='%s) Empieza en %s' % (SEC[k], nombre(ini))))
        sol4.append('%s) %s' % (SEC[k], ' · '.join(nombre(p) for p in ps)))
    sol(MES, 4, 'Camino descendente', sol4)

    # ---- Ejercicio 5: mismo sonido, dos claves
    d.add(ejercicio(5, 'El mismo sonido, escrito de dos maneras',
                    ['En la primera fila cada nota está escrita en **las dos claves**: es la misma tecla del piano. Escribe su nombre.',
                     'En la segunda, solo está escrita en clave de sol: **dibújala en clave de fa**, en el mismo lugar del teclado.'],
                    'Entender que las dos claves forman un único pentagrama continuo y que el Do central está en medio.'))
    cols = ['A3', 'B3', 'C4', 'D4', 'E4', 'G3']
    d.add(gran_pauta_notas(cols, cols, titulo='a) ¿Cómo se llama cada nota?'))
    cols2 = ['G3', 'A3', 'B3', 'C4', 'D4', 'E4']
    d.add(gran_pauta_notas(cols2, [None] * 6, titulo='b) Dibújala en clave de fa', linea_nombre=False))
    sol(MES, 5, 'El mismo sonido, en dos claves',
        ['a) ' + ' · '.join(nombre(p) for p in cols) + '.',
         'b) en clave de fa: ' + ' · '.join('%s (%s)' % (nombre(p), posicion(p, 'bass')) for p in cols2) + '.'])
