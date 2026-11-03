# -*- coding: utf-8 -*-
"""DICIEMBRE · Figuras, silencios y compas."""
from n1_base import *
from n1_comun import *

MES = 'Diciembre'
ORD = ['w', 'h', 'q', 'e', 's', 'f', 'g']


def construir(d):
    d.nuevo('Diciembre · Figuras, silencios y compás')
    d.add(banda_mes('Diciembre', 'Etapa 1', 'Figuras, silencios y compás',
                    'La duración de los sonidos y de las pausas, el puntillo y la organización del tiempo en compases.'))
    d.add(caja('dato', 'Las figuras musicales', [
        'Las **figuras** indican la **duración** de cada sonido. Se miden en **tiempos**, tomando como unidad la **negra** (♩ = 1 tiempo). '
        'De mayor a menor duración son: **redonda, blanca, negra, corchea, semicorchea, fusa y semifusa**. En este nivel se trabaja hasta la semicorchea; '
        'la fusa y la semifusa aparecen en repertorio más avanzado.',
        'Equivalencias: **1 redonda = 2 blancas = 4 negras = 8 corcheas = 16 semicorcheas = 32 fusas = 64 semifusas.**']),
        fila_figuras(gap=9.6, titulo='Orden, nombre y valor de las figuras'))
    d.add(ejercicio(1, 'Nombre, figura y valor',
                    ['Completa la tabla: en cada fila falta un dato (la figura, el nombre o el valor en tiempos).'],
                    'Asociar sin traducir la figura, su nombre y su duración.'))
    filas, sol1 = [], []
    for i, dd in enumerate(ORD):
        falta = i % 3
        filas.append([fig_celda(dd) if falta != 0 else '', NOM_FIG[dd] if falta != 1 else '', FIG[dd][4] if falta != 2 else ''])
        sol1.append('%s (%s) — falta %s' % (NOM_FIG[dd], FIG[dd][4], ['la figura', 'el nombre', 'el valor'][falta]))
    d.add(tabla([100, 150, 150], filas, ['Figura', 'Nombre', 'Valor'], alto=32, size=9.2))
    sol(MES, 1, 'Nombre, figura y valor', ['; '.join(sol1) + '.'])
    d.add(ejercicio(2, 'Equivalencias de duración',
                    ['Completa con el número que corresponda. Si dudas, pasa todo a tiempos de negra.'],
                    'Operar con duraciones, base de cualquier lectura rítmica.'))
    sumas = [('1 blanca = ___ negras', '2'), ('1 redonda = ___ blancas', '2'), ('1 negra = ___ corcheas', '2'), ('1 corchea = ___ semicorcheas', '2'),
             ('1 redonda = ___ corcheas', '8'), ('2 negras + 1 blanca = ___ tiempos', '4'), ('1 blanca + 1 negra + 2 corcheas = ___ tiempos', '4'),
             ('4 semicorcheas + 1 negra = ___ tiempos', '2'), ('3 corcheas + 1 negra = ___ tiempos', '2 ½'), ('1 blanca + 4 semicorcheas = ___ tiempos', '3')]
    d.add(lista([t for t, _ in sumas], marca='▸', size=9.6, sep=5))
    sol(MES, 2, 'Equivalencias de duración', ['  ·  '.join('%d) %s' % (k + 1, r_) for k, (_, r_) in enumerate(sumas))])

    # ---- puntillo
    d.add(caja('dato', 'El puntillo', [
        'Un **puntillo** a la derecha de una figura **añade la mitad de su valor**. Permite duraciones que no existen como figura independiente: '
        'la blanca con puntillo dura 3 tiempos, la negra con puntillo 1 ½.'],),
        tabla([120, 100, 130, 141], [[fig_celda('w'), 'Redonda · 4', '+ 2', '= 6 tiempos'], [fig_celda('h'), 'Blanca · 2', '+ 1', '= 3 tiempos'],
                                     [fig_celda('q'), 'Negra · 1', '+ ½', '= 1 ½ tiempos'], [fig_celda('e'), 'Corchea · ½', '+ ¼', '= ¾ de tiempo']],
              ['Figura', 'Valor', 'El puntillo suma', 'Con puntillo'], alto=32, size=9))
    d.add(ejercicio(3, 'Cálculo con puntillo',
                    ['Calcula la duración en tiempos.'], 'Leer con exactitud las figuras con puntillo, que modifican el ritmo de una frase.'))
    pc = [('Blanca con puntillo = ___ tiempos', '3'), ('Negra con puntillo = ___ tiempos', '1 ½'), ('Redonda con puntillo = ___ tiempos', '6'),
          ('Negra con puntillo + corchea = ___ tiempos', '2'), ('Blanca con puntillo + negra = ___ tiempos', '4'),
          ('Corchea con puntillo + semicorchea = ___ tiempo', '1')]
    d.add(lista([t for t, _ in pc], marca='▸', size=9.6, sep=5))
    sol(MES, 3, 'Cálculo con puntillo', ['  ·  '.join('%d) %s' % (k + 1, r_) for k, (_, r_) in enumerate(pc))])

    # ---- silencios
    d.add(caja('dato', 'Los silencios', [
        'A cada figura le corresponde un **silencio** de la misma duración. Su posición en el pentagrama está fijada: el **silencio de redonda cuelga de la 4.ª línea**, '
        'el **de blanca se apoya sobre la 3.ª**, y los demás se escriben centrados. El silencio de redonda sirve además para indicar **un compás completo de silencio**, '
        'sea cual sea la cifra del compás.'],),
        fila_silencios(gap=9.6, titulo='Silencios de redonda, blanca, negra, corchea, semicorchea, fusa y semifusa'))
    d.add(ejercicio(4, 'Silencios y figuras equivalentes',
                    ['Une cada silencio con la figura de igual duración y escribe cuántos tiempos dura.'],
                    'Reconocer los silencios a primera vista y asociarlos a su valor.'))
    orden = ['q', 'h', 'e', 'w', 's']
    r = rnd(4)
    der = list(orden)
    r.shuffle(der)
    d.add(une([fig_celda(x, True, gap=5.2) for x in orden], [fig_celda(x, gap=5.0) for x in der], alto=38, izq_w=90, der_w=60, hueco=120, sufijo='tiempos'))
    sol(MES, 4, 'Silencios y figuras equivalentes',
        ['Cada silencio con su figura: ' + ' · '.join('silencio de %s ↔ %s (%s)' % (NOM_FIG[x].lower(), NOM_FIG[x].lower(), FIG[x][4]) for x in orden) + '.'])

    # ---- compas
    d.add(caja('dato', 'El compás', [
        'El **compás** agrupa los tiempos de la música en bloques iguales, separados por **barras de compás**. Al principio de la pieza, tras la clave, una **cifra** lo define: '
        'el número de **arriba** indica cuántos tiempos tiene cada compás; el de **abajo**, qué figura equivale a un tiempo (4 = negra, 2 = blanca, 8 = corchea).',
        'Los compases simples más frecuentes son **2/4**, **3/4** y **4/4** (este último también se escribe **C**). Las duraciones de las notas y silencios de cada compás '
        'deben sumar exactamente su número de tiempos. El **primer tiempo es el más fuerte**: en 2/4, fuerte–débil; en 3/4, fuerte–débil–débil; en 4/4, fuerte–débil–semifuerte–débil.']),
        fila_compases([[N('q'), N('q')], [N('h')]], ts=(2, 4), titulo='2/4', rotulos=['1  2', '1 — 2']),
        fila_compases([[N('q'), N('q'), N('q')], [N('h'), N('q')]], ts=(3, 4), titulo='3/4', rotulos=['1  2  3', '1 — 2  3']),
        fila_compases([[N('q'), N('q'), N('q'), N('q')], [N('h'), N('h')]], ts=(4, 4), titulo='4/4', rotulos=['1  2  3  4', '1 — 2  3 — 4']))
    d.add(ejercicio(5, 'Completar compases',
                    ['Escribe en cada hueco figuras o silencios que completen el compás. Hay varias soluciones válidas.'],
                    'Sumar duraciones hasta completar el compás.'))
    ej = [((2, 4), [[N('q'), ('x', 1)], [N('e'), N('e'), R('e'), ('x', 0.5)]]),
          ((3, 4), [[N('q'), N('q'), ('x', 1)], [N('h'), ('x', 1)]]),
          ((4, 4), [[N('q'), N('q'), ('x', 2)], [N('h.'), ('x', 1)]])]
    s5 = []
    for k, (ts, comp) in enumerate(ej):
        rot = ['faltan %s' % ('½ tiempo' if it_[1] == 0.5 else ('%d tiempo%s' % (it_[1], '' if it_[1] == 1 else 's'))) for m in comp for it_ in m if it_[0] == 'x']
        d.add(fila_compases(comp, ts=ts, titulo='%s) %d/%d' % (SEC[k], ts[0], ts[1]), rotulos=rot))
        s5.append('%s) %d/%d: faltan ' % (SEC[k], ts[0], ts[1]) + ' y '.join('%g' % it_[1] for m in comp for it_ in m if it_[0] == 'x') + ' tiempos (p. ej. negra, dos corcheas, blanca…).')
    sol(MES, 5, 'Completar compases', s5)
    d.add(ejercicio(6, 'Deducir la cifra del compás',
                    ['Estos compases no llevan cifra. Suma sus tiempos y escribe debajo si son de 2/4, 3/4 o 4/4.'],
                    'Relacionar la duración de las figuras con la estructura del compás.'))
    sec6 = [[N('h'), N('q')], [N('q'), N('q')], [N('e'), N('e'), N('q'), N('q')], [N('h'), N('h')], [N('q.'), N('e'), N('q')],
            [N('q'), N('q'), R('q'), N('q')], [N('e'), N('e'), N('e'), N('e'), N('q')], [N('h'), R('q')], [N('w')]]
    s6 = []
    for k in range(3):
        grp = sec6[k * 3:(k + 1) * 3]
        d.add(fila_compases(grp, ts=None, titulo='%s)' % SEC[k], rotulos=['____ / ____'] * 3))
        s6.append('%s) ' % SEC[k] + ' · '.join('%g → %s' % (suma_items(m), {2: '2/4', 3: '3/4', 4: '4/4'}[int(suma_items(m))]) for m in grp))
    sol(MES, 6, 'Deducir la cifra del compás', s6)
    d.add(ejercicio(7, 'Corregir compases',
                    ['En cada compás hay una figura que sobra, de modo que no suma los tiempos de su cifra. Táchala y anota cuánto valía.'],
                    'Detectar errores de escritura rítmica, habitual al leer o copiar música.'))
    e7 = [((2, 4), [[N('h'), N('q')], [N('q'), N('h')]], 'una negra en cada compás'),
          ((3, 4), [[N('h'), N('q'), N('e'), N('e')], [N('h.'), N('q')]], 'una negra en cada compás'),
          ((4, 4), [[N('h'), N('q'), N('q'), N('e')], [N('w'), N('q')]], 'una corchea (1.º) y una negra (2.º)')]
    s7 = []
    for k, (ts, comp, resp) in enumerate(e7):
        d.add(fila_compases(comp, ts=ts, titulo='%s) %d/%d' % (SEC[k], ts[0], ts[1]), rotulos=['sobra: __________'] * 2))
        s7.append('%s) %d/%d: sobra %s.' % (SEC[k], ts[0], ts[1], resp))
    sol(MES, 7, 'Corregir compases', s7)

    # ---- al piano
    d.add(caja('piano', 'Lectura rítmica: palmas y cuenta', [
        'Lee cada línea marcando el pulso con el pie, **cuenta en voz alta** y palmea el ritmo. En los silencios, deja las manos abiertas sin dejar de contar. Empieza hacia ♩ = 60.']))
    lect = [((2, 4), [[N('q'), N('q')], [N('e'), N('e'), N('q')], [N('q'), R('q')], [N('h')]]),
            ((3, 4), [[N('q'), N('q'), N('q')], [N('h'), N('q')], [N('q'), N('e'), N('e'), N('q')], [N('h.')]]),
            ((4, 4), [[N('q'), N('q'), N('h')], [N('e'), N('e'), N('q'), R('q'), N('q')], [N('q.'), N('e'), N('h')], [N('w')]])]
    for k, (ts, comp) in enumerate(lect):
        d.add(fila_compases(comp, ts=ts, titulo='%s) %d/%d' % (SEC[k], ts[0], ts[1])))
    himno = [('E', 'q', 3), ('E', 'q', 3), ('F', 'q', 4), ('G', 'q', 5), ('G', 'q', 5), ('F', 'q', 4), ('E', 'q', 3), ('D', 'q', 2),
             ('C', 'q', 1), ('C', 'q', 1), ('D', 'q', 2), ('E', 'q', 3), ('E', 'q.', 3), ('D', 'e', 2), ('D', 'h', 2)]
    d.add(sistema('Himno de la Alegría · L. van Beethoven (tema de la 9.ª sinfonía) · mano derecha',
                  [{'pitch': l + '4', 'dur': dd, 'number': n} for l, dd, n in himno], alto=112))
    d.add(ejercicio(8, 'Análisis del Himno de la Alegría',
                    ['Contesta sobre la partitura de arriba. Es el mismo procedimiento con que se prepara cualquier pieza: antes de tocar, se analiza.'],
                    'Adquirir el hábito de leer la partitura antes de tocarla.'))
    d.add(tabla([260, 231], [['Clave', ''], ['Cifra de compás', ''], ['Figura de menor duración', ''], ['Nota más aguda y nota más grave', ''],
                              ['Compás en el que aparece un puntillo', ''], ['Número de compases', '']], ['Pregunta', 'Respuesta'], alto=26, alin=['l', 'l'], size=9))
    sol(MES, 8, 'Análisis del Himno de la Alegría',
        ['Clave de sol · 4/4 · corchea · más aguda Sol (G4), más grave Do (C4) · el compás 4 (negra con puntillo + corchea) · 4 compases.'])
    d.add(sistema('Jingle Bells · J. Pierpont (1857) · primera frase',
                  [{'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'h', 'number': 3},
                   {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'E4', 'dur': 'h', 'number': 3},
                   {'pitch': 'E4', 'dur': 'q', 'number': 3}, {'pitch': 'G4', 'dur': 'q', 'number': 5}, {'pitch': 'C4', 'dur': 'q.', 'number': 1},
                   {'pitch': 'D4', 'dur': 'e', 'number': 2}, {'pitch': 'E4', 'dur': 'w', 'number': 3}], alto=112))
    sol(MES, 'Lectura y piezas', 'Lectura rítmica y piezas',
        ['Cada compás de a), b) y c) suma 2, 3 y 4 tiempos. Jingle Bells: Mi Mi Mi(h) · Mi Mi Mi(h) · Mi Sol Do. Re · Mi(w).'])
