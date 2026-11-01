# -*- coding: utf-8 -*-
"""ABRIL · Clave de fa y manos juntas."""
from n1_base import *
from n1_base import _abs_idx
from n1_comun import *

MES = 'Abril'


def construir(d):
    d.nuevo('Abril · Clave de fa y manos juntas')
    d.add(banda_mes('Abril', 'Etapa 2', 'Clave de fa y manos juntas',
                    'Lectura de las notas graves y primera coordinación de las dos manos sobre el sistema de piano.'))
    d.add(caja('dato', 'La clave de fa', [
        'La **clave de fa** se usa para el registro grave: mano izquierda del piano, violonchelo, trombón, fagot o tuba. Se escribe al inicio del pentagrama y sus **dos puntos rodean la 4.ª línea**, que es **Fa**.',
        'Las notas siguen el mismo orden, pero **no coinciden con las de la clave de sol**: la 1.ª línea es Mi en sol y **Sol en fa**. '
        'Líneas, de abajo arriba: **Sol – Si – Re – Fa – La**. Espacios: **La – Do – Mi – Sol**. Se lee por tanto de forma independiente, tomando el Fa de la 4.ª línea como referencia.']),
        fila_notas('bass', ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3'], 'w', bajo=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol', 'La'],
                   titulo='De la 1.ª línea (Sol) a la 5.ª (La), por líneas y espacios'),
        caja('tip', 'Leer con el cuerpo', [
            'Asocia cada nota grave con la tecla y con la posición de tu **mano izquierda** antes de tocar: visualizar la nota en el teclado y anticipar el movimiento '
            'refuerza la lectura. En pasajes rápidos o repetidos, no dependas solo de la vista: tu mano debe conocer el camino.']))
    d.add(ejercicio(1, 'Lectura desde el Fa',
                    ['La primera nota de cada fila es el **Fa de la 4.ª línea**, ya nombrado. Cuenta a partir de él y nombra las demás.'],
                    'Leer con seguridad en clave de fa, partiendo de su nota de referencia.'))
    r = rnd(301)
    pb = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'F2', 'E2', 'B3', 'C4']
    bl, s1 = bloque_lectura(r, 'bass', 4, 'Clave de fa', pool=pb)
    d.add(*bl)
    sol(MES, 1, 'Lectura desde el Fa', s1)
    d.add(ejercicio(2, 'Transcribir de clave de sol a clave de fa',
                    ['Escribe cada melodía **una octava más grave**, en clave de fa. Para bajar una octava, cada nota desciende siete posiciones (línea→espacio, siete veces): '
                     'el Mi de la 1.ª línea de sol pasa a ser el Mi del 3.er espacio de fa. Comprueba el resultado en el piano.'],
                    'Dominar la correspondencia entre las dos claves y el concepto de octava.'))
    t1 = ['E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4']
    t2 = ['C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'C5']
    d.add(gran_pauta_notas(t1, [None] * 8, titulo='a) Una octava más grave', linea_nombre=False, dur='q'),
          gran_pauta_notas(t2, [None] * 8, titulo='b) Una octava más grave', linea_nombre=False, dur='q'))
    sol(MES, 2, 'Transcribir de sol a fa',
        ['a) ' + ' · '.join('%s (%s)' % (nombre(mover(p, -7)), posicion(mover(p, -7), 'bass')) for p in t1),
         'b) ' + ' · '.join('%s (%s)' % (nombre(mover(p, -7)), posicion(mover(p, -7), 'bass')) for p in t2)])
    d.add(ejercicio(3, 'Ritmo y cuenta en clave de fa',
                    ['Cada compás está escrito en clave de fa sobre la nota Re. Escribe debajo el número de cada golpe (1 y 2 y …) y toca el ritmo con la mano izquierda sobre una sola tecla.'],
                    'Trasladar la lectura rítmica al registro grave sin perder el pulso.'))
    rit = [('a) 4/4', (4, 4), [[N('q', 'D3'), N('q', 'D3'), N('h', 'D3')], [N('e', 'F3'), N('e', 'F3'), N('q', 'F3'), N('h', 'F3')], [N('q', 'A2'), R('q'), N('q', 'A2'), R('q')]]),
           ('b) 3/4', (3, 4), [[N('q', 'D3'), N('q', 'D3'), N('q', 'D3')], [N('h', 'F3'), N('q', 'F3')], [N('e', 'A2'), N('e', 'A2'), N('e', 'A2'), N('e', 'A2'), N('q', 'A2')]])]
    for tit, ts, comp in rit:
        d.add(fila_compases(comp, ts=ts, clef='bass', pitch='D3', titulo=tit, rotulos=['______'] * len(comp)))
    sol(MES, 3, 'Ritmo en clave de fa', ['Se cuenta «1 2 3 4» (4/4) o «1 2 3» (3/4), con «y» en las corcheas. Cada compás suma los tiempos de su cifra.'])

    # ---- manos juntas
    d.add(caja('dato', 'El sistema de piano: leer las dos manos a la vez', [
        'En el **sistema de piano** las dos claves se unen con una llave y se leen **en vertical**: las notas que están una sobre otra suenan **a la vez**. Todo lo que cae en la misma vertical '
        'debe tocarse junto, incluso cuando las dos manos escriben figuras distintas (por ejemplo, la derecha en negras sobre una redonda de la izquierda).',
        'Tocar a dos manos exige **independencia**. El método: leer cada mano por separado hasta dominarla, después **juntar por compases**, siempre despacio, '
        'y solo acelerar cuando se pueda tocar sin mirar las manos.']))
    d.add(ejercicio(4, 'Análisis del sistema de piano',
                    ['Para cada fragmento contesta con los nombres de las notas que suenan **en el primer tiempo** de cada compás (derecha / izquierda).'],
                    'Leer en vertical y asociar cada nota con su mano.'))
    f1 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4']] + [{'pitch': 'G4', 'dur': 'w'}], [{'pitch': 'C3', 'dur': 'w'}, {'pitch': 'G2', 'dur': 'w'}])
    f2 = ([{'pitch': 'E4', 'dur': 'h'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'C4', 'dur': 'h.'}], [{'pitch': 'C3', 'dur': 'q'}, {'pitch': 'E3', 'dur': 'q'}, {'pitch': 'G3', 'dur': 'q'}, {'pitch': 'G2', 'dur': 'h.'}])
    d.add(sistema_piano('a) 4/4', f1[0], f1[1], alto=190), sistema_piano('b) 3/4', f2[0], f2[1], ts=(3, 4), alto=190))
    d.add(tabla([120, 185, 186], [['Fragmento a) compás 1', '', ''], ['Fragmento a) compás 2', '', ''], ['Fragmento b) compás 1', '', ''], ['Fragmento b) compás 2', '', '']],
                ['', 'Mano derecha', 'Mano izquierda'], alto=24, size=8.6, alin=['l', 'c', 'c']))
    sol(MES, 4, 'Análisis del sistema de piano', ['a) c. 1: Do4 / Do3 · c. 2: Sol4 / Sol2.   b) c. 1: Mi4 / Do3 · c. 2: Do4 / Sol2.'])
    d.add(caja('piano', 'Al piano: Himno de la Alegría a dos manos', [
        'La derecha toca la melodía que ya conoces; la izquierda sostiene una **redonda por compás**, alternando Do y Sol (el grado I y el grado V). Estudia primero cada mano sola, '
        'después de dos en dos compases. La digitación de la izquierda queda a tu criterio: elige la que no te obligue a saltos.']))
    h = [('E', 'q', 3), ('E', 'q', 3), ('F', 'q', 4), ('G', 'q', 5), ('G', 'q', 5), ('F', 'q', 4), ('E', 'q', 3), ('D', 'q', 2),
         ('C', 'q', 1), ('C', 'q', 1), ('D', 'q', 2), ('E', 'q', 3), ('E', 'q.', 3), ('D', 'e', 2), ('D', 'h', 2)]
    rh = [{'pitch': l + '4', 'dur': dd, 'number': n} for l, dd, n in h]
    d.add(sistema_piano('Himno de la Alegría · compases 1 y 2', rh[:8], [{'pitch': 'C3', 'dur': 'w'}, {'pitch': 'G2', 'dur': 'w'}], alto=190),
          sistema_piano('Himno de la Alegría · compases 3 y 4', rh[8:], [{'pitch': 'C3', 'dur': 'w'}, {'pitch': 'G2', 'dur': 'w'}], alto=190))
    sol(MES, 'Himno a dos manos', 'Himno de la Alegría a dos manos',
        ['Derecha: Mi Mi Fa Sol · Sol Fa Mi Re · Do Do Re Mi · Mi. Re Re. Izquierda: Do (redonda), Sol (redonda), Do (redonda), Sol (redonda).'])
