# -*- coding: utf-8 -*-
"""ENERO · Notas adicionales y lectura en las dos claves."""
from n1_base import *
from n1_base import _abs_idx
from n1_comun import *

MES = 'Enero'


def construir(d):
    d.nuevo('Enero · Notas adicionales')
    d.add(banda_mes('Enero', 'Etapa 1', 'Notas adicionales',
                    'Lectura fuera del pentagrama, el Do central como eje entre las dos claves y trabajo de velocidad de lectura.'))
    d.add(caja('dato', 'Líneas adicionales', [
        'Cuando una nota excede el registro del pentagrama se escribe sobre **líneas adicionales**: trazos cortos del mismo grosor y a la misma distancia que las líneas del pentagrama. '
        'Cada nota lleva solo las necesarias para alcanzarla. Se denominan **superiores** si se sitúan por encima de la 5.ª línea e **inferiores** si se sitúan por debajo de la 1.ª. '
        'Cuanto más arriba se escribe una nota, más aguda es.',
        'La lectura fuera del pentagrama no requiere contar línea a línea desde el principio: se parte de **notas de referencia** que se reconocen de inmediato y se avanza desde la más cercana.']),
        fila_notas('treble', ['A3', 'C4', 'D4', 'G5', 'A5', 'B5', 'C6'], 'w', bajo=['La', 'Do', 'Re', 'Sol', 'La', 'Si', 'Do'],
                   titulo='Clave de sol · adicionales inferiores (La3, Do4) y superiores (La5, Do6)'),
        fila_notas('bass', ['C2', 'E2', 'F2', 'B3', 'C4', 'D4', 'E4'], 'w', bajo=['Do', 'Mi', 'Fa', 'Si', 'Do', 'Re', 'Mi'],
                   titulo='Clave de fa · adicionales inferiores (Do2, Mi2) y superiores (Do4, Mi4)'),
        tabla([110, 190, 191], [['Clave de sol', 'Do4 (1.ª) · La3 (2.ª)', 'La5 (1.ª) · Do6 (2.ª)'], ['Clave de fa', 'Mi2 (1.ª) · Do2 (2.ª)', 'Do4 (1.ª) · Mi4 (2.ª)']],
              ['Notas de referencia', 'Adicionales inferiores', 'Adicionales superiores'], alto=22, size=8.8),
        caja('nota', 'Un único pentagrama de once líneas', [
            'Las claves de sol y de fa forman, en conjunto, un pentagrama continuo de **once líneas**, con el **Do central** en la línea intermedia, que no se dibuja '
            'completa: se escribe como línea adicional bajo la clave de sol o sobre la de fa. Por eso una misma nota puede escribirse en las dos claves.']))

    d.add(ejercicio(1, 'Lectura de notas adicionales',
                    ['La primera nota de cada fila es la nota de referencia (Do en clave de sol, Fa en clave de fa) y va nombrada. Cuenta a partir de ella y nombra las demás.',
                     'Las notas de las filas incluyen adicionales superiores e inferiores.'],
                    'Leer fuera del pentagrama apoyándote en una nota de referencia.'))
    r = rnd(104)
    pt = ['A3', 'B3', 'D4', 'E4', 'F4', 'G4', 'A4', 'G5', 'A5', 'B5', 'C6']
    pb = ['C2', 'D2', 'E2', 'F2', 'G2', 'B3', 'C4', 'D4', 'E4', 'G3', 'A3']
    bl, s1 = bloque_lectura(r, 'treble', 2, 'Clave de sol', pool=pt)
    bl2, s1b = bloque_lectura(r, 'bass', 2, 'Clave de fa', pool=pb)
    s1b = [t.replace('a)', 'c)').replace('b)', 'd)') for t in s1b]
    for k, bb in enumerate(bl2):
        pass
    d.add(*bl, *bl2)
    sol(MES, 1, 'Lectura de notas adicionales', s1 + s1b)

    d.add(ejercicio(2, 'Dirección melódica',
                    ['Indica en la casilla si cada par de notas **asciende** (↑), **desciende** (↓) o **repite** el sonido (=). Después nombra las notas.'],
                    'Percibir la dirección de la melodía antes de identificar cada nota.'))
    r = rnd(202)
    sol2 = []
    for k, clef in enumerate(['treble', 'bass']):
        pool = pt + ['E4', 'G4', 'C5'] if clef == 'treble' else pb + ['G2', 'D3', 'A3']
        movs = ['↑', '↓', '=', '↑', '↓', '=']
        r.shuffle(movs)
        pares = []
        for m in movs:
            a = r.choice(pool)
            if m == '=':
                b = a
            else:
                cand = [p for p in pool if (_abs_idx(p) > _abs_idx(a)) == (m == '↑') and p != a]
                b = r.choice(cand) if cand else a
            pares.append((a, b))
        d.add(fila_pares(clef, pares, titulo='%s) %s' % (SEC[k], 'Clave de sol' if clef == 'treble' else 'Clave de fa')))
        sol2.append('%s) ' % SEC[k] + '  '.join('%s %s-%s' % ('↑' if _abs_idx(b) > _abs_idx(a) else ('↓' if _abs_idx(b) < _abs_idx(a) else '='), nombre(a), nombre(b)) for a, b in pares))
    sol(MES, 2, 'Dirección melódica', sol2)

    d.add(ejercicio(3, 'Secuencias por grados',
                    ['La primera nota de cada fila está escrita. Escribe las siete siguientes **por grados conjuntos** (una posición cada vez), subiendo o bajando según se indica, y nombra todas.'],
                    'Dominar el desplazamiento por grados conjuntos desde cualquier punto del pentagrama.'))
    cas = [('treble', 'A3', True), ('bass', 'E2', True), ('treble', 'C6', False), ('bass', 'E4', False)]
    s3 = []
    for k, (clef, ini, sube) in enumerate(cas):
        ps = [mover(ini, j if sube else -j) for j in range(8)]
        d.add(fila_notas(clef, [ps[0]] + [None] * 7, 'w', bajo='linea', titulo='%s) Desde %s, %s' % (SEC[k], nombre(ini, True), 'subiendo' if sube else 'bajando')))
        s3.append('%s) %s' % (SEC[k], ' · '.join(nombre(p) for p in ps)))
    sol(MES, 3, 'Secuencias por grados', s3)

    d.add(ejercicio(4, 'Una nota, dos claves',
                    ['En la primera fila cada nota aparece escrita en las dos claves: es la misma tecla. Escribe su nombre.',
                     'En la segunda solo aparece en clave de sol: escríbela en clave de fa, en el mismo sonido.'],
                    'Entender que ambas claves comparten registro y moverse con soltura entre ellas.'))
    cols = ['A3', 'B3', 'C4', 'D4', 'E4', 'G3']
    cols2 = ['G3', 'A3', 'B3', 'C4', 'D4', 'E4']
    d.add(gran_pauta_notas(cols, cols, titulo='a) Nombra cada nota'))
    d.add(gran_pauta_notas(cols2, [None] * 6, titulo='b) Escríbela en clave de fa', linea_nombre=False))
    sol(MES, 4, 'Una nota, dos claves', ['a) ' + ' · '.join(nombre(p) for p in cols) + '.',
                                         'b) ' + ' · '.join('%s (%s)' % (nombre(p), posicion(p, 'bass')) for p in cols2) + '.'])

    d.add(ejercicio(5, 'Velocidad de lectura',
                    ['Lee en voz alta cada fila (nombres de las notas, sin parar) y anota el tiempo. Repite al cabo de unos días: el objetivo es reducir el tiempo y los errores.'],
                    'Convertir la lectura en un proceso automático y medir el progreso.'))
    r = rnd(505)
    filas5, s5 = [], []
    for clef, tit in (('treble', 'Clave de sol'), ('bass', 'Clave de fa')):
        pool = pt + ['E4', 'F4', 'G4', 'A4', 'B4', 'C5'] if clef == 'treble' else pb + ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3']
        ps = []
        while len(ps) < 8:
            p = r.choice(pool)
            if not ps or (p != ps[-1] and abs(_abs_idx(p) - _abs_idx(ps[-1])) <= 5):
                ps.append(p)
        d.add(fila_notas(clef, ps, 'q', bajo='nada', barras=4, titulo='%s' % tit))
        s5.append('%s: %s' % (tit, ' · '.join(nombre(p) for p in ps)))
    d.add(tabla([120, 90, 90, 90, 101], [['1.ª lectura', '', '', '', ''], ['2.ª lectura', '', '', '', ''], ['3.ª lectura', '', '', '', '']],
                ['', 'Fecha', 'Tiempo (s)', 'Errores', 'Observaciones'], alto=22, size=8.6, alin=['l', 'c', 'c', 'c', 'l']))
    sol(MES, 5, 'Velocidad de lectura', s5)

    d.add(caja('piano', 'Al piano: la zona del Do central', [
        'Estas dos piezas cruzan el Do central. Antes de tocar, **nombra todas las notas**; la digitación la decides tú: busca la posición de mano que no obligue a saltos.']))
    d.add(sistema('Ejercicio de lectura en la zona del Do central (mano derecha)',
                  [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'E4', 'G4', 'E4', 'A3', 'B3', 'C4', 'D4']] + [{'pitch': 'C4', 'dur': 'w'}], alto=112))
    au = [('C', 'q'), ('C', 'q'), ('C', 'q'), ('D', 'q'), ('E', 'h'), ('D', 'h'), ('C', 'q'), ('E', 'q'), ('D', 'q'), ('D', 'q'), ('C', 'w')]
    rh = [{'pitch': l + '4', 'dur': dd} for l, dd in au]
    lh = [{'pitch': 'C3', 'dur': 'w'}] * 4
    d.add(sistema_piano('Au clair de la lune con bordón en la mano izquierda (la izquierda sostiene el Do)', rh, lh, alto=200))
    sol(MES, 'Al piano', 'Zona del Do central',
        ['Primera pieza: Do Re Mi Re · Do Mi Sol Mi · La Si Do Re · Do (La y Si, bajo el Do central, en adicionales inferiores). Segunda: melodía en la derecha; la izquierda sostiene un Do durante cada compás.'])
