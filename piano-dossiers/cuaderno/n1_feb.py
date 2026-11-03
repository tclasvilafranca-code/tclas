# -*- coding: utf-8 -*-
"""FEBRERO · La escala de Do mayor, alteraciones e intervalos."""
from n1_base import *
from n1_base import _abs_idx
from n1_comun import *

MES = 'Febrero'
ESC = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
ESC_B = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']
GRADOS = [('I', 'Do', 'tónica'), ('II', 'Re', 'supertónica'), ('III', 'Mi', 'mediante'), ('IV', 'Fa', 'subdominante'),
          ('V', 'Sol', 'dominante'), ('VI', 'La', 'superdominante'), ('VII', 'Si', 'sensible')]


def construir(d):
    d.nuevo('Febrero · Escala de Do mayor')
    d.add(banda_mes('Febrero', 'Etapa 2', 'Escala de Do mayor',
                    'Tonos y semitonos, alteraciones, construcción de la escala, grados e intervalos.'))
    d.add(caja('dato', 'Tono, semitono y alteraciones', [
        'La distancia más pequeña entre dos teclas contiguas del piano es el **semitono**; dos semitonos forman un **tono**. Entre Mi–Fa y Si–Do no hay tecla negra: '
        'son los dos **semitonos naturales** de la escala de Do.',
        'Las **alteraciones** modifican la altura de una nota: el **sostenido (♯)** la sube un semitono, el **bemol (♭)** la baja un semitono y el **becuadro (♮)** anula una alteración anterior. '
        'Cada tecla negra recibe dos nombres, según se alcance subiendo o bajando: Do♯ y Re♭ son la misma tecla (notas **enarmónicas**). Una alteración escrita ante una nota '
        'vale hasta el final de ese compás.']),
        diag_semitonos())
    d.add(ejercicio(1, 'Teclas negras',
                    ['Escribe en el primer teclado el nombre de cada negra como **sostenido** y en el segundo como **bemol**.',
                     'En el tercero, marca las notas de la lista: Do♯ · Mi♭ · Fa♯ · La♭ · Si♭.'],
                    'Identificar cualquier tecla del piano por sus dos nombres.'))
    d.add(bloque_teclado(h=66, desde=('C', 4), n_blancas=8, cajas={'%s#4' % L for L in 'CDFGA'}, titulo='a) Sostenidos'),
          bloque_teclado(h=66, desde=('C', 4), n_blancas=8, cajas={'%s#4' % L for L in 'CDFGA'}, titulo='b) Bemoles'),
          bloque_teclado(h=66, desde=('C', 4), n_blancas=8, titulo='c) Marca las teclas de la lista'))
    sol(MES, 1, 'Teclas negras', ['a) Do♯ Re♯ Fa♯ Sol♯ La♯.  b) Re♭ Mi♭ Sol♭ La♭ Si♭.  c) Do♯ = 1.ª negra · Mi♭ = 2.ª negra (Re♯) · Fa♯ = 3.ª negra · La♭ = 4.ª negra (Sol♯) · Si♭ = 5.ª negra (La♯).'])

    # ---------------------------------------------------------------- escala
    d.add(caja('dato', 'La escala de Do mayor', [
        'Una **escala** es una sucesión de notas por grados conjuntos. La de **Do mayor** no lleva ninguna alteración: son las ocho teclas blancas de un Do al siguiente. '
        'Su estructura de distancias —**T T S T T T S** (tono, tono, semitono, tono, tono, tono, semitono)— es la que define toda escala mayor, empiece en la nota que empiece.',
        'Cada nota ocupa un **grado**. Algunos tienen nombre propio: el I es la **tónica** (la nota de reposo), el IV la **subdominante**, el V la **dominante** y el VII la **sensible** '
        '(a un semitono de la tónica).']),
        diag_escala(),
        tabla([90, 100, 170], [[g[0], g[1], g[2]] for g in GRADOS], ['Grado', 'Nota en Do mayor', 'Nombre'], alto=17, size=8.4))
    d.add(h2('Digitación de la escala'))
    d.add(diag_digitacion(ESC, ESC_B, [1, 2, 3, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 3, 2, 1], [5, 4, 3, 2, 1, 3, 2, 1], [1, 2, 3, 1, 2, 3, 4, 5]),
          par('Con cinco dedos no se alcanza una octava: tras el 3 (mano derecha, subiendo) el **pulgar pasa por debajo** para ocupar el Fa, y al bajar el 3 pasa **por encima** del pulgar. '
              'En la mano izquierda ocurre al revés. El brazo acompaña a la mano; la muñeca no se tuerce.', 9.3))
    d.add(ejercicio(2, 'Estructura de la escala',
                    ['Escribe entre cada dos notas consecutivas si hay un **tono (T)** o un **semitono (S)**. Utiliza el teclado de arriba para comprobarlo.'],
                    'Entender la escala como una estructura de distancias, no como una lista de nombres.'))
    d.add(tabla([61] * 8, [['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do'], ['T/S:', '', '', '', '', '', '', '']], None, alto=24, size=9, zebra=False))
    sol(MES, 2, 'Estructura de la escala', ['Do–Re T · Re–Mi T · Mi–Fa S · Fa–Sol T · Sol–La T · La–Si T · Si–Do S (5 tonos y 2 semitonos).'])
    d.add(ejercicio(3, 'Escribir la escala con digitación',
                    ['La primera nota de cada fila está escrita. Completa la escala con sus nombres y anota encima el dedo de cada nota.',
                     'Mano derecha en clave de sol; mano izquierda en clave de fa.'],
                    'Fijar a la vez la grafía de la escala y su digitación.'))
    d.add(fila_notas('treble', ['C4'] + [None] * 7, 'q', bajo='linea', encima=[1] + [''] * 7, titulo='a) Mano derecha, subiendo'),
          fila_notas('treble', ['C5'] + [None] * 7, 'q', bajo='linea', encima=[5] + [''] * 7, titulo='b) Mano derecha, bajando'),
          fila_notas('bass', ['C3'] + [None] * 7, 'q', bajo='linea', encima=[5] + [''] * 7, titulo='c) Mano izquierda, subiendo'),
          fila_notas('bass', ['C4'] + [None] * 7, 'q', bajo='linea', encima=[1] + [''] * 7, titulo='d) Mano izquierda, bajando'))
    sol(MES, 3, 'Escala con digitación',
        ['a) Do Re Mi Fa Sol La Si Do — 1 2 3 1 2 3 4 5.  b) Do Si La Sol Fa Mi Re Do — 5 4 3 2 1 3 2 1.',
         'c) Do Re Mi Fa Sol La Si Do (grave) — 5 4 3 2 1 3 2 1.  d) Do Si La Sol Fa Mi Re Do — 1 2 3 1 2 3 4 5.'])

    # ---------------------------------------------------------------- intervalos
    d.add(caja('dato', 'Intervalos', [
        'Un **intervalo** es la distancia entre dos notas. Se mide **contando las dos notas extremas**: de Do a Mi hay tres notas (Do – Re – Mi), luego es una **tercera**. '
        'Sobre el pentagrama, de una línea a la línea siguiente hay una tercera; de una línea al espacio contiguo, una segunda. Si las dos notas son la misma, es un unísono; '
        'si hay ocho notas entre los extremos, una **octava**.']),
        tabla([66, 56, 56, 56, 56, 56, 56, 89], [['Do – Do', 'Do – Re', 'Do – Mi', 'Do – Fa', 'Do – Sol', 'Do – La', 'Do – Si', 'Do – Do agudo'],
                                                  ['unísono', '2.ª', '3.ª', '4.ª', '5.ª', '6.ª', '7.ª', '8.ª (octava)']], None, alto=24, size=7.6))
    d.add(ejercicio(4, 'Reconocer intervalos',
                    ['Escribe debajo de cada pareja el intervalo que forman. Cuenta incluyendo las dos notas; comprueba algunos en el teclado.'],
                    'Medir distancias a primera vista para leer en bloques en lugar de nota a nota.'))
    r = rnd(33)
    pares = []
    for _ in range(8):
        a = r.choice(['C4', 'D4', 'E4', 'F4', 'G4', 'A4'])
        k = r.choice([1, 2, 3, 4, 5, 6, 7])
        pares.append((a, mover(a, k)))
    s4 = []
    for fila in range(2):
        sub = pares[fila * 4:(fila + 1) * 4]
        d.add(fila_notas('treble', [p for pr in sub for p in pr], 'w', bajo='nada', barras=2, titulo='%s)' % SEC[fila]))

        def lin(c, x, y, w):
            cur0 = x + 4 + GAP * 5.4
            slot = (w - 8 - GAP * 5.4 - 4) / 8.0
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(0.6)
            for i in range(4):
                cx = cur0 + slot * (2 * i + 1)
                c.line(cx - 22, y - 12, cx + 22, y - 12)
        d.add(Blk(20, lin))
        s4.append('%s) ' % SEC[fila] + ' · '.join('%s–%s = %d.ª' % (nombre(a), nombre(b), _abs_idx(b) - _abs_idx(a) + 1) for a, b in sub))
    sol(MES, 4, 'Reconocer intervalos', s4)
    d.add(ejercicio(5, 'Construir intervalos',
                    ['Escribe la nota que forma con la dada el intervalo indicado (hacia arriba).'],
                    'Pasar del nombre del intervalo a su posición en el pentagrama.'))
    cons = [('C4', 3), ('D4', 5), ('E4', 4), ('G4', 6), ('F4', 5), ('A4', 3)]
    d.add(fila_notas('treble', [c_[0] for c_ in cons], 'w', bajo=['%d.ª' % c_[1] for c_ in cons], titulo='Nota dada y intervalo pedido (el segundo sonido se escribe a su derecha)'))
    sol(MES, 5, 'Construir intervalos', [' · '.join('%s + %d.ª = %s' % (nombre(a), n, nombre(mover(a, n - 1))) for a, n in cons) + '.'])

    # ---------------------------------------------------------------- al piano
    d.add(caja('piano', 'Al piano: escala a dos manos y con ritmos', [
        'Primero cada mano por separado, después juntas, **en movimiento paralelo** (las dos tocan la misma nota con una octava de diferencia). '
        'Usa metrónomo: empieza hacia ♩ = 60 y sube de 4 en 4 **solo cuando salga limpia tres veces seguidas**.']))
    rh = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(ESC, [1, 2, 3, 1, 2, 3, 4, 5])]
    lh = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(ESC_B, [5, 4, 3, 2, 1, 3, 2, 1])]
    d.add(sistema_piano('Escala de Do mayor a dos manos, subiendo (una octava de distancia entre ellas)', rh[:4], lh[:4], alto=190))
    d.add(sistema_piano('… continuación', rh[4:], lh[4:], alto=190))
    pats = [('Negras', [[N('q')] * 4, [N('q')] * 4]), ('Corcheas', [[N('e')] * 8, [N('e')] * 8]),
            ('Negra con puntillo y corchea', [[N('q.'), N('e'), N('q.'), N('e')], [N('q.'), N('e'), N('q.'), N('e')]]),
            ('Blanca y dos negras', [[N('h'), N('q'), N('q')], [N('h'), N('q'), N('q')]])]
    d.add(par('**Variantes rítmicas.** Toca la escala (una nota por golpe) con cada uno de estos ritmos:', 9.3, INK, despues=3))
    for k, (tit, comp) in enumerate(pats):
        d.add(fila_compases(comp, ts=(4, 4), titulo='%s) %s' % (SEC[k], tit)))
    d.add(tabla([100, 98, 98, 98, 97], [['♩ =', '', '', '', ''], ['Escala limpia (de 3)', '', '', '', '']],
                ['Semana', '1', '2', '3', '4'], alto=22, size=8.4, zebra=False))
    d.add(ejercicio(6, 'Composición breve en Do mayor',
                    ['Escribe una frase de **cuatro compases en 4/4**, en clave de sol y solo con notas de Do mayor. Debe empezar en una nota del acorde de Do (Do, Mi o Sol) y **terminar en Do** (la tónica).',
                     'Incluye al menos una blanca, un par de corcheas y un puntillo. Toca después tu frase.'],
                    'Aplicar la teoría en la práctica: componer obliga a decidir figuras, alturas y final.'))
    d.add(pauta_vacia('treble', 4, (4, 4), titulo='Mi frase'))
    sol(MES, 6, 'Composición breve', ['Libre. Criterios: 4 compases de 4/4, notas de Do mayor, empieza en Do/Mi/Sol, termina en Do, incluye blanca, dos corcheas y puntillo; cada compás suma 4 tiempos.'])
    sol(MES, 'Al piano', 'Escala a dos manos', ['Derecha: Do Re Mi Fa Sol La Si Do (1 2 3 1 2 3 4 5). Izquierda: la misma escala una octava más grave (5 4 3 2 1 3 2 1).'])
