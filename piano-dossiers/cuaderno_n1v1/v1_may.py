# -*- coding: utf-8 -*-
"""MAYO · La ligadura y el puntillo."""
from v1_base import *
from v1_base import _abs_idx
from page_layout_common import system_block
from fractions import Fraction

MES = 'Mayo'
SEC = 'abcdef'
N = lambda dd, p=None: ('n', dd) if p is None else ('n', dd, p)
R = lambda dd: ('r', dd)
V = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'h.': 3.0, 'q.': 1.5, 'w.': 6.0, 'e.': 0.75}


def sistema(titulo, ev, ts=(4, 4), alto=110, clef='treble'):
    return Blk(alto, lambda c, x, y, w: system_block(c, x, w, y, GAP + 0.6, titulo, ev, clef=clef, time_sig=ts))


def tx(v):
    s = '%g' % v
    return s.replace('.5', ' ½') if '.5' in s else s


def construir(d):
    d.nuevo('Mayo · La ligadura y el puntillo')
    d.add(banda_mes('Mayo', '3.er trimestre', 'La ligadura y el puntillo',
                    'Dos recursos para escribir cualquier duración: unir notas y alargarlas con un punto.'))
    d.add(caja('dato', 'Dos formas de alargar una nota', [
        '▸ **Ligadura de prolongación:** une dos notas **del mismo sonido** para que se toquen como una sola, **sumando sus valores**. '
        'Es muy común cuando una nota se prolonga **de un compás a otro**, porque una figura no puede cruzar la barra de compás.',
        '▸ **Puntillo:** el punto a la derecha de una figura la alarga **la mitad de su valor**: una blanca con puntillo dura 3 tiempos.',
        '▸ **Ligadura de expresión (legato):** si une notas **distintas**, no suma tiempos: indica que se toquen **ligadas**, sin cortar el sonido entre una y otra. '
        'Se dibuja igual (un arco), pero significa otra cosa; fíjate siempre en si las notas son iguales o diferentes.',
        'Estos recursos dan **flexibilidad** a la escritura: permiten duraciones que no existen como figura suelta.']),
        sistema('Ligadura de prolongación: la blanca y la negra suman 3 tiempos',
                [{'pitch': 'G4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h', 'lig': True},
                 {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'F4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'h'}], alto=100),
        sistema('Ligadura de expresión (legato): notas distintas, no se suman tiempos',
                [{'pitch': 'E4', 'dur': 'q', 'lig': True}, {'pitch': 'F4', 'dur': 'q', 'lig': True}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'},
                 {'pitch': 'D4', 'dur': 'h'}, {'pitch': 'C4', 'dur': 'h'}], alto=100))

    # ---- Ejercicio 1: la ligadura
    d.add(ejercicio(1, 'La ligadura',
                    ['Observa las parejas de notas ligadas y escribe **cuánto dura en total** cada nota (suma los valores de las dos).',
                     'Después, escribe con **una sola figura** (con o sin puntillo) lo que valen: dos blancas, dos negras, una blanca y una negra…'],
                    'Identificar visualmente la ligadura y comprender su función.'))
    lig = [
        [{'pitch': 'C5', 'dur': 'h', 'lig': True}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'},
         {'pitch': 'A4', 'dur': 'q', 'lig': True}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h'}],
        [{'pitch': 'E4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'h', 'lig': True}, {'pitch': 'C5', 'dur': 'w'}],
    ]
    tot = [('C5: blanca + negra', 3.0, 'A4: negra + negra', 2.0), ('C5: blanca + redonda', 6.0, '', 0)]
    for k, ev in enumerate(lig):
        d.add(sistema('%s) %s' % (SEC[k], 'Escribe cuánto dura cada nota ligada: ____ tiempos' + ('   y   ____ tiempos' if k == 0 else '')), ev, alto=104))
    d.add(lista(['Dos blancas ligadas = ______ (una sola figura).', 'Dos negras ligadas = ______.', 'Blanca + negra ligadas = ______.',
                 'Redonda + blanca ligadas = ______.'], marca='▸', size=9.6, sep=5))
    sol(MES, 1, 'La ligadura',
        ['a) C5: blanca + negra = 3 tiempos; A4: negra + negra = 2 tiempos.  b) C5: blanca + redonda = 6 tiempos.',
         'Dos blancas = redonda · Dos negras = blanca · Blanca + negra = blanca con puntillo · Redonda + blanca = redonda con puntillo (6 tiempos).'])

    # ---- Ejercicio 2: puntillo en contexto
    d.add(ejercicio(2, 'El puntillo en contexto',
                    ['Escribe la duración exacta de cada figura con puntillo en subdivisiones más pequeñas.',
                     'Recuerda: el punto suma la mitad. Si te pierdes, pasa todo a la figura más pequeña.'],
                    'Interiorizar que el puntillo añade la mitad del valor y expresarlo en subdivisiones reales.'))
    ppt = [('Negra con puntillo', 'corcheas', Fraction(3, 2) / Fraction(1, 2)), ('Blanca con puntillo', 'negras', Fraction(3)),
           ('Corchea con puntillo', 'semicorcheas', Fraction(3, 4) / Fraction(1, 4)), ('Redonda con puntillo', 'blancas', Fraction(6, 2)),
           ('Semicorchea con puntillo', 'fusas', Fraction(3, 8) / Fraction(1, 8))]
    d.add(lista(['%s = ______ %s.' % (a, b) for a, b, _ in ppt] + ['Semicorchea con puntillo = ______ semifusas.'], marca='▸', size=9.8, sep=6))
    sol(MES, 2, 'El puntillo en contexto', ['  ·  '.join('%s = %d %s' % (a, int(v), b) for a, b, v in ppt) + '  ·  Semicorchea con puntillo = 6 semifusas.'])

    d.add(caja('tip', 'El «salto» del puntillo', [
        'Una **negra con puntillo seguida de una corchea** (1 ½ + ½ = 2 tiempos) da a la música un ritmo **saltarín y vivo**, muy típico de la danza, el jazz y las canciones populares. '
        'Lo oirás en la última frase de «Jingle Bells» («all the **way**»). El puntillo no solo alarga: **cambia el carácter** de lo que se toca.']))

    # ---- Ejercicio 3: lectura
    d.add(ejercicio(3, 'Lectura con pulso y subdivisión',
                    ['Lee cada línea en voz alta marcando el pulso con el pie: **TA** para las negras y blancas, **TI-TI** para las corcheas y **SHH** para los silencios.',
                     'Cuenta en la cabeza lo que dura cada nota y sigue siempre el mismo pulso: la ligadura hace que **no se vuelva a atacar** la segunda nota.'],
                    'Sentir el «empuje» de cada nota dentro del pulso y su subdivisión.'))
    lect = [
        ('a) Con puntillo', [[N('q.'), N('e'), N('q'), N('q')], [N('h.'), N('q')], [N('q.'), N('e'), N('q.'), N('e')]]),
        ('b) Con silencios', [[N('q'), N('q'), R('q'), N('q')], [N('q.'), N('e'), R('h')], [N('h.'), R('q')]]),
    ]
    for tit, comp in lect:
        d.add(fila_compases(comp, ts=(4, 4), titulo=tit))

    # ---- Ejercicio 4: creativa
    d.add(ejercicio(4, 'Aplicación creativa',
                    ['Escribe un **motivo** de un compás en 4/4 que use al menos **un puntillo**, **una ligadura** y **un silencio**.',
                     'Repite el motivo **tres veces** con una variación rítmica distinta cada vez (cambia la posición del puntillo, invierte corcheas y semicorcheas, desplaza acentos…). '
                     'Señala cuál versión alarga más y por qué.'],
                    'Convertir la teoría del puntillo en música con dirección y carácter.'))
    d.add(pauta_vacia('treble', 1, (4, 4), titulo='Motivo'), pauta_vacia('treble', 1, (4, 4), titulo='Variación 1'),
          pauta_vacia('treble', 1, (4, 4), titulo='Variación 2'), pauta_vacia('treble', 1, (4, 4), titulo='Variación 3'))
    sol(MES, 3, 'Lectura con pulso y subdivisión', ['Cada compás de a) y b) suma 4 tiempos. Con ligadura, la segunda nota no se vuelve a tocar.'])
    sol(MES, 4, 'Aplicación creativa', ['Ejercicio libre. Criterios: 4/4, un puntillo, una ligadura de prolongación y un silencio; cada variación suma 4 tiempos.'])

    # ---- Al piano
    d.add(caja('piano', 'Al piano: la segunda frase del Himno de la Alegría', [
        'La melodía repite el principio, pero **acaba distinto**: el compás final lleva un **puntillo** (negra con puntillo + corchea) y termina en la tónica, Do. '
        'Tócala con la derecha, posición de Do.']))
    himno2 = [('E4', 'q', 3), ('E4', 'q', 3), ('F4', 'q', 4), ('G4', 'q', 5), ('G4', 'q', 5), ('F4', 'q', 4), ('E4', 'q', 3), ('D4', 'q', 2),
              ('C4', 'q', 1), ('C4', 'q', 1), ('D4', 'q', 2), ('E4', 'q', 3), ('D4', 'q.', 2), ('C4', 'e', 1), ('C4', 'h', 1)]
    ev = [{'pitch': p, 'dur': dd, 'number': n} for p, dd, n in himno2]
    d.add(sistema('Himno de la Alegría · L. van Beethoven (tema, 2.ª frase)', ev, alto=108))
    sol(MES, 'Himno (2.ª frase)', 'Himno de la Alegría (2.ª frase)', ['Mi Mi Fa Sol · Sol Fa Mi Re · Do Do Re Mi · Re. Do Do. Último compás: negra con puntillo + corchea + blanca = 4 tiempos.'])
