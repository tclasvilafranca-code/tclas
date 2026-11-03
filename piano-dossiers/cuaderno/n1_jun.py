# -*- coding: utf-8 -*-
"""JUNIO · Acordes y acompanamiento."""
from n1_base import *
from n1_base import _abs_idx
from n1_comun import *

MES = 'Junio'
PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
# (cifrado, nombre, fundamental, tercera, quinta)
TRIADAS = [('C', 'Do mayor', 'C4', 'E4', 'G4'), ('Dm', 'Re menor', 'D4', 'F4', 'A4'), ('Em', 'Mi menor', 'E4', 'G4', 'B4'),
           ('F', 'Fa mayor', 'F4', 'A4', 'C5'), ('G', 'Sol mayor', 'G4', 'B4', 'D5'), ('Am', 'La menor', 'A3', 'C4', 'E4')]


def semitonos(a, b):
    """Semitonos entre dos notas naturales (b por encima de a)."""
    def n(p):
        return PC[p[0]] + 12 * int(p[-1])
    return n(b) - n(a)


def construir(d):
    d.nuevo('Junio · Acordes')
    d.add(banda_mes('Junio', 'Etapa 3', 'Acordes y acompañamiento',
                    'Qué es un acorde, tríadas mayores y menores, funciones armónicas y primeras cadencias para acompañar.'))
    d.add(caja('dato', 'La tríada', [
        'Un **acorde** son tres o más sonidos que suenan a la vez. El más sencillo es la **tríada**: tres notas separadas por **terceras**, es decir, una nota, la que está dos grados por encima '
        '(**tercera**) y la que está cuatro grados por encima (**quinta**). La nota de la que se parte es la **fundamental** y da nombre al acorde. En **estado fundamental** '
        'la fundamental es la nota más grave.',
        'Según la distancia entre sus notas, la tríada es **mayor** (tercera mayor, 4 semitonos, más tercera menor, 3 semitonos) o **menor** (tercera menor y después tercera mayor). '
        'El modo, mayor o menor, determina el carácter: el mayor suena más luminoso, el menor más sombrío.']),
        sistema('Tríadas de la escala de Do mayor sobre cada grado (estado fundamental)',
                [{'pitches': [t[2], t[3], t[4]], 'dur': 'h'} for t in TRIADAS[:4]] + [], ts=(4, 4), alto=118),
        sistema('… y las dos restantes', [{'pitches': [t[2], t[3], t[4]], 'dur': 'h'} for t in TRIADAS[4:]], ts=(4, 4), alto=118),
        tabla([60, 100, 90, 120, 121], [[t[0], t[1], '%s – %s – %s' % (nombre(t[2]), nombre(t[3]), nombre(t[4])),
                                         '%d + %d semitonos' % (semitonos(t[2], t[3]), semitonos(t[3], t[4])), 'mayor' if semitonos(t[2], t[3]) == 4 else 'menor']
                                        for t in TRIADAS], ['Cifrado', 'Acorde', 'Notas', 'Distancias', 'Modo'], alto=19, size=8.6))
    d.add(caja('nota', 'El cifrado de acordes', [
        'En canciones, libros de acordes y partituras de pop los acordes se indican con **letras**: C = Do, D = Re, E = Mi, F = Fa, G = Sol, A = La, B = Si. La letra sola indica acorde '
        '**mayor** (C = Do mayor); una **m** añadida indica **menor** (Am = La menor).']))
    d.add(ejercicio(1, 'Construir tríadas',
                    ['La primera nota de cada fila es la fundamental. Escribe la **tercera** y la **quinta** (hacia arriba, en estado fundamental) y escribe el nombre de las tres notas.'],
                    'Construir acordes sobre la tríada sin memorizarlos: saltando una nota entre cada dos.'))
    ej1 = [('C', 'C4'), ('F', 'F4'), ('G', 'G4'), ('Am', 'A3'), ('Dm', 'D4'), ('Em', 'E4')]
    s1 = []
    for k in range(0, 6, 3):
        sub = ej1[k:k + 3]
        notas = []
        bajo = []
        for cif, raiz in sub:
            tri = [raiz, mover(raiz, 2), mover(raiz, 4)]
            notas += [raiz, None, None]
            bajo += [cif, '_', '_']
            s1.append('%s: %s' % (cif, ' – '.join(nombre(p) for p in tri)))
        d.add(fila_notas('treble', notas, 'w', bajo=bajo, titulo='%s)' % SEC[k // 3], barras=3, caja_ancho=26))
    sol(MES, 1, 'Construir tríadas', ['; '.join(s1) + '.'])
    d.add(ejercicio(2, 'Modo de cada acorde',
                    ['Cuenta los semitonos entre las notas del acorde (ayúdate del teclado) y decide si es mayor o menor.'],
                    'Distinguir a oído y a la vista el modo mayor del menor.'))
    pr = [('Do – Mi – Sol', 'C4', 'E4', 'G4'), ('Re – Fa – La', 'D4', 'F4', 'A4'), ('Fa – La – Do', 'F4', 'A4', 'C5'), ('Mi – Sol – Si', 'E4', 'G4', 'B4'), ('Sol – Si – Re', 'G4', 'B4', 'D5')]
    d.add(tabla([130, 120, 120, 121], [[a, '', '', ''] for a, *_ in pr], ['Notas', '1.ª → 3.ª (semitonos)', '3.ª → 5.ª (semitonos)', 'Modo'], alto=24, size=9))
    sol(MES, 2, 'Modo de cada acorde', ['; '.join('%s: %d + %d → %s' % (a, semitonos(x, y), semitonos(y, z), 'mayor' if semitonos(x, y) == 4 else 'menor') for a, x, y, z in pr) + '.'])
    d.add(ejercicio(3, 'Reconocer acordes',
                    ['Escribe el cifrado de cada acorde (C, Dm, Em, F, G o Am). Identifica primero la fundamental y comprueba si la tercera está a 4 o a 3 semitonos.'],
                    'Leer acordes de un vistazo para acompañar canciones.'))
    r = rnd(63)
    orden = list(range(6))
    r.shuffle(orden)
    ac = [TRIADAS[i] for i in orden[:4]]
    d.add(sistema('Escribe el cifrado debajo de cada acorde', [{'pitches': [t[2], t[3], t[4]], 'dur': 'h'} for t in ac], ts=(4, 4), alto=120))
    d.add(lineas_escribir(1, 'Cifrados:   ______     ______     ______     ______', 22))
    sol(MES, 3, 'Reconocer acordes', ['  ·  '.join(t[0] for t in ac) + '.'])

    # ---- funciones y cadencia
    d.add(caja('dato', 'Funciones armónicas y cadencia', [
        'Los acordes de una tonalidad se agrupan en tres funciones principales: **tónica** (grado I: reposo, punto de partida y de llegada), **subdominante** (grado IV: movimiento, aleja de la tónica) '
        'y **dominante** (grado V: tensión, pide volver a la tónica). La secuencia **I – IV – V – I** es la cadencia más básica y sirve de esqueleto a un gran número de canciones.',
        'En Do mayor: **C – F – G – C**. En Sol mayor: **G – C – D – G**. En Fa mayor: **F – B♭ – C – F**.']))
    d.add(sistema_piano('Cadencia I – IV – V – I en Do mayor (acordes en la derecha, fundamental en la izquierda)',
                        [{'pitches': ['C4', 'E4', 'G4'], 'dur': 'w'}, {'pitches': ['F4', 'A4', 'C5'], 'dur': 'w'}],
                        [{'pitch': 'C3', 'dur': 'w'}, {'pitch': 'F3', 'dur': 'w'}], alto=190),
          sistema_piano('… continuación', [{'pitches': ['G4', 'B4', 'D5'], 'dur': 'w'}, {'pitches': ['C4', 'E4', 'G4'], 'dur': 'w'}],
                        [{'pitch': 'G2', 'dur': 'w'}, {'pitch': 'C3', 'dur': 'w'}], alto=190))
    d.add(ejercicio(4, 'Cadencias en otras tonalidades',
                    ['Escribe la cadencia I – IV – V – I en Sol mayor y en Fa mayor: tres notas por acorde, en estado fundamental, en clave de sol. Usa la armadura indicada.'],
                    'Aplicar la misma estructura en tonalidades distintas.'))
    d.add(sistema('a) Sol mayor (G – C – D – G)', [{'rest': True, 'dur': 'w'}] * 4, key_sig='Sol mayor', alto=96),
          sistema('b) Fa mayor (F – B♭ – C – F)', [{'rest': True, 'dur': 'w'}] * 4, key_sig='Fa mayor', alto=96))
    sol(MES, 4, 'Cadencias en otras tonalidades',
        ['a) G: Sol–Si–Re · C: Do–Mi–Sol · D: Re–Fa♯–La · G: Sol–Si–Re.  b) F: Fa–La–Do · B♭: Si♭–Re–Fa · C: Do–Mi–Sol · F: Fa–La–Do.'])

    d.add(caja('piano', 'Al piano: acordes de la mano izquierda', [
        'La izquierda toca los tres sonidos de cada acorde **a la vez** (digitación **5 – 3 – 1**), con el peso del brazo y sin golpear. Primero cada acorde por separado hasta que la mano lo reconozca; después la cadencia seguida. '
        'Cuando salga, toca la melodía de la derecha sobre ella.']))
    lh = [{'pitches': ['C3', 'E3', 'G3'], 'dur': 'w'}, {'pitches': ['F3', 'A3', 'C4'], 'dur': 'w'}, {'pitches': ['G2', 'B2', 'D3'], 'dur': 'w'}, {'pitches': ['C3', 'E3', 'G3'], 'dur': 'w'}]
    d.add(sistema('Cadencia I – IV – V – I con la mano izquierda en acordes (Do mayor)', lh, clef='bass', alto=116))
    d.add(par('**Reto:** toca el Himno de la Alegría (noviembre y abril) con la derecha y, con la izquierda, un acorde de **C** en los compases 1 y 3 y de **G** en los compases 2 y 4.', 9.3, NAVY_SOFT))
    sol(MES, 'Al piano', 'Acordes de la mano izquierda', ['C = Do Mi Sol · F = Fa La Do · G = Sol Si Re (una octava más grave para quedar en la zona de la izquierda).'])
