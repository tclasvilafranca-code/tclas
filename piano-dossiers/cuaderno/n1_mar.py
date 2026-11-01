# -*- coding: utf-8 -*-
"""MARZO · Ritmo y subdivision, ligadura y puntillo."""
from n1_base import *
from n1_comun import *
from fractions import Fraction

MES = 'Marzo'
VAL = {'redonda': Fraction(4), 'blanca': Fraction(2), 'negra': Fraction(1), 'corchea': Fraction(1, 2), 'semicorchea': Fraction(1, 4)}
PLU = {'redonda': 'redondas', 'blanca': 'blancas', 'negra': 'negras', 'corchea': 'corcheas', 'semicorchea': 'semicorcheas'}


def v(n, f_, pt=False):
    x = VAL[f_] * n
    return x * Fraction(3, 2) if pt else x


def txt(t):
    n, f_, pt = t
    return ('%d %s' % (n, PLU[f_] if n > 1 else f_)) + (' con puntillo' if pt else '')


def construir(d):
    d.nuevo('Marzo · Ritmo')
    d.add(banda_mes('Marzo', 'Etapa 2', 'Ritmo y subdivisión',
                    'El pulso y su división, la lectura rítmica, la ligadura de prolongación y el compás compuesto.'))
    d.add(caja('dato', 'Pulso, ritmo y subdivisión', [
        'El **pulso** es el latido regular sobre el que se organiza la música; el **ritmo** es la combinación de duraciones que se escribe sobre él. '
        'La **subdivisión** consiste en dividir cada tiempo en partes iguales: dos (corcheas) o cuatro (semicorcheas). Leer con soltura exige mantener el pulso '
        'constante mientras cambia la subdivisión.',
        'Para solfear el ritmo se usan sílabas: negra = **ta**, dos corcheas = **ti-ti**, cuatro semicorcheas = **ti-ka-ti-ka**, blanca = **ta-a**. '
        'Las corcheas y semicorcheas de un mismo tiempo se unen con **barras** para que se vea de un vistazo cómo se agrupan los tiempos.']),
        fila_compases([[N('q')] * 4, [N('e')] * 8, [N('s')] * 16], ts=(4, 4), titulo='Un mismo compás con un golpe, dos o cuatro sonidos por tiempo',
                      rotulos=['ta  ta  ta  ta', 'ti-ti  ti-ti  ti-ti  ti-ti', 'ti-ka-ti-ka  ×4'], ancho_rel=[0.9, 1.2, 2.4]))
    d.add(ejercicio(1, 'Lectura rítmica',
                    ['Lee cada línea en voz alta con las sílabas, marcando el pulso con el pie; después palmea el ritmo. En los silencios, deja las manos abiertas.',
                     'No te detengas si te equivocas: la lectura rítmica se entrena con continuidad. Empieza hacia ♩ = 60.'],
                    'Desarrollar la lectura automática del ritmo, independiente de las notas.'))
    lect = [
        ('a) 2/4', (2, 4), [[N('q'), N('e'), N('e')], [N('e'), N('e'), N('q')], [N('e'), N('e'), N('e'), N('e')], [N('q'), N('q')]]),
        ('b) 3/4', (3, 4), [[N('q'), N('e'), N('e'), N('q')], [N('q'), R('q'), N('q')], [N('e'), N('e'), N('e'), N('e'), N('q')], [N('h'), R('q')]]),
        ('c) 4/4', (4, 4), [[N('s'), N('s'), N('s'), N('s'), N('q'), N('q'), N('q')], [N('q'), N('s'), N('s'), N('s'), N('s'), N('q'), N('q')],
                           [N('e'), N('e'), N('s'), N('s'), N('s'), N('s'), N('q'), N('q')], [N('h'), N('q'), R('q')]]),
    ]
    for tit, ts, comp in lect:
        d.add(fila_compases(comp, ts=ts, titulo=tit))
    sol(MES, 1, 'Lectura rítmica', ['Todos los compases suman los tiempos de su cifra (2, 3 o 4). Los silencios se cuentan igual que las notas.'])
    d.add(ejercicio(2, 'Ritmo del texto',
                    ['Cada frase tiene un ritmo natural: una sílaba, un sonido. Dila en voz alta y escribe en el compás (4/4) un ritmo que la reproduzca. Hay varias soluciones válidas.'],
                    'Relacionar el ritmo hablado con la notación, útil para fijar el fraseo de una melodía.'))
    frases = ['Buenos días', 'Hasta mañana', 'Qué tal estás', 'Nos vemos el lunes']
    d.add(fila_compases([[('x', 4)] for _ in frases[:2]], ts=(4, 4), titulo='a)', rotulos=['«%s»' % f_ for f_ in frases[:2]]),
          fila_compases([[('x', 4)] for _ in frases[2:]], ts=(4, 4), titulo='b)', rotulos=['«%s»' % f_ for f_ in frases[2:]]))
    sol(MES, 2, 'Ritmo del texto', ['Respuesta libre. Ejemplo: «Bue-nos dí-as» = ti-ti ta ta (corchea, corchea, negra, negra). Criterio: una sílaba por sonido y el compás suma 4 tiempos.'])
    d.add(ejercicio(3, 'Comparar duraciones',
                    ['Escribe >, < o = en cada círculo según qué duración sea mayor.'],
                    'Dominar la equivalencia de las subdivisiones, también cuando intervienen puntillos.'))
    comps = [((2, 'corchea', False), (1, 'negra', False)), ((1, 'blanca', False), (3, 'negra', False)), ((4, 'semicorchea', False), (1, 'negra', False)),
             ((1, 'negra', True), (3, 'corchea', False)), ((1, 'redonda', False), (2, 'blanca', False)), ((3, 'semicorchea', False), (1, 'corchea', False)),
             ((1, 'blanca', True), (2, 'negra', False)), ((6, 'semicorchea', False), (1, 'negra', True))]
    filas, s3 = [], []

    def circ(c, cx, cy, w, h):
        c.setStrokeColor(NAVY)
        c.setLineWidth(0.9)
        c.circle(cx, cy, 8, fill=0, stroke=1)
    for a, b in comps:
        va, vb = v(*a), v(*b)
        s3.append('%s %s %s' % (txt(a), '>' if va > vb else ('<' if va < vb else '='), txt(b)))
        filas.append([txt(a), circ, txt(b)])
    d.add(tabla([190, 40, 190], filas, ['Primera', '', 'Segunda'], alto=22, size=9.4))
    sol(MES, 3, 'Comparar duraciones', ['; '.join('%d) %s' % (i + 1, s_) for i, s_ in enumerate(s3)) + '.'])

    # ---- ligadura
    d.add(caja('dato', 'La ligadura', [
        'La **ligadura de prolongación** une dos notas **del mismo sonido** y se tocan como una sola, **sumando sus duraciones**. Es imprescindible cuando una nota se prolonga '
        'de un compás al siguiente, ya que una figura no puede atravesar la barra de compás, y para escribir duraciones que no existen como figura.',
        'La **ligadura de expresión** (legato) se escribe igual, pero une notas **distintas**: no suma tiempos, indica que se toquen sin cortar el sonido entre ellas. '
        'Para distinguirlas basta mirar si las notas unidas son la misma.']),
        sistema('Prolongación: la blanca ligada a la negra suma 3 tiempos',
                [{'pitch': 'G4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h', 'lig': True},
                 {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'F4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'h'}], alto=100),
        sistema('Expresión (legato): notas distintas, no se suman tiempos',
                [{'pitch': 'E4', 'dur': 'q', 'lig': True}, {'pitch': 'F4', 'dur': 'q', 'lig': True}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'},
                 {'pitch': 'D4', 'dur': 'h'}, {'pitch': 'C4', 'dur': 'h'}], alto=100))
    d.add(ejercicio(4, 'Duración de las notas ligadas',
                    ['Escribe cuánto dura en total cada nota ligada y, después, con qué **una sola figura** se escribiría cada suma.'],
                    'Leer correctamente las notas ligadas, habituales al cruzar la barra de compás.'))
    lig = [
        [{'pitch': 'C5', 'dur': 'h', 'lig': True}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'},
         {'pitch': 'A4', 'dur': 'q', 'lig': True}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h'}],
        [{'pitch': 'E4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'h', 'lig': True}, {'pitch': 'C5', 'dur': 'w'}]]
    d.add(sistema('a) Do5: ____ tiempos    La4: ____ tiempos', lig[0], alto=104), sistema('b) Do5: ____ tiempos', lig[1], alto=104))
    d.add(lista(['Dos blancas ligadas = ______.', 'Dos negras ligadas = ______.', 'Blanca + negra ligadas = ______.', 'Redonda + blanca ligadas = ______.'], marca='▸', size=9.6, sep=5))
    sol(MES, 4, 'Duración de las notas ligadas',
        ['a) Do5: blanca + negra = 3 tiempos; La4: negra + negra = 2 tiempos.  b) Do5: blanca + redonda = 6 tiempos.  Dos blancas = redonda · dos negras = blanca · blanca + negra = blanca con puntillo · redonda + blanca = redonda con puntillo.'])
    d.add(ejercicio(5, 'El puntillo y su subdivisión',
                    ['Expresa cada figura con puntillo en la figura menor que se indica.'],
                    'Entender el puntillo como suma de una figura y su mitad.'))
    ppt = [('Negra con puntillo', 'corcheas', 3), ('Blanca con puntillo', 'negras', 3), ('Corchea con puntillo', 'semicorcheas', 3),
           ('Redonda con puntillo', 'blancas', 3), ('Blanca con puntillo', 'corcheas', 6)]
    d.add(lista(['%s = ______ %s.' % (a, b) for a, b, _ in ppt], marca='▸', size=9.6, sep=5))
    sol(MES, 5, 'El puntillo y su subdivisión', ['  ·  '.join('%s = %d %s' % (a, n, b) for a, b, n in ppt) + '.'])

    # ---- compas compuesto
    d.add(caja('nota', 'Compás compuesto: 6/8', [
        'En el compás de **6/8** la corchea es la unidad y se cuentan **seis corcheas**, agrupadas de tres en tres: dos tiempos, cada uno de **negra con puntillo**. '
        'El pulso se siente «de dos en dos» (uno-dos-tres, uno-dos-tres), con un balanceo típico de barcarolas y danzas. '
        'En un compás simple como 2/4, en cambio, cada tiempo se divide en dos.']),
        fila_compases([[N('e')] * 6, [N('q.'), N('q.')], [N('q.'), N('e'), N('e'), N('e')]], ts=(6, 8), agrupa=1.5, titulo='6/8: seis corcheas, dos negras con puntillo, y una combinación',
                      rotulos=['1 2 3  4 5 6', '1 — —  4 — —', '1 — —  4  5  6']))
    d.add(ejercicio(6, 'Lectura en 6/8',
                    ['Lee y palmea cada línea contando **dos pulsos por compás** (cada uno vale una negra con puntillo). Las corcheas se agrupan de tres en tres.'],
                    'Percibir la diferencia entre el compás compuesto y el simple.'))
    d.add(fila_compases([[N('e')] * 3 + [N('q.')], [N('q.'), N('e'), N('e'), N('e')], [N('q'), N('e'), N('q.')], [N('q.'), N('q.')]], ts=(6, 8), agrupa=1.5, titulo='a)'),
          fila_compases([[N('q.'), R('q.')], [N('e'), N('e'), N('e'), N('q'), N('e')], [N('q'), N('e'), N('q'), N('e')], [N('q.'), N('q.')]], ts=(6, 8), agrupa=1.5, titulo='b)'))
    sol(MES, 6, 'Lectura en 6/8', ['Cada compás de 6/8 suma 3 tiempos de negra (seis corcheas). Se cuenta «1 2 3 4 5 6» con acento en 1 y 4.'])

    # ---- al piano
    d.add(caja('piano', 'Al piano: Frère Jacques (canon tradicional)', [
        'Melodía tradicional francesa que combina negras, blancas y corcheas. Tócala con la mano derecha; cuando la domines, intenta tocarla como **canon** con otra persona entrando dos compases después.']))
    fj = [('C', 'q', 1), ('D', 'q', 2), ('E', 'q', 3), ('C', 'q', 1), ('C', 'q', 1), ('D', 'q', 2), ('E', 'q', 3), ('C', 'q', 1),
          ('E', 'q', 3), ('F', 'q', 4), ('G', 'h', 5), ('E', 'q', 3), ('F', 'q', 4), ('G', 'h', 5),
          ('G', 'e', 5), ('A', 'e', 5), ('G', 'e', 5), ('F', 'e', 4), ('E', 'q', 3), ('C', 'q', 1),
          ('G', 'e', 5), ('A', 'e', 5), ('G', 'e', 5), ('F', 'e', 4), ('E', 'q', 3), ('C', 'q', 1),
          ('C', 'q', 1), ('G', 'q', 5), ('C', 'h', 1), ('C', 'q', 1), ('G', 'q', 5), ('C', 'h', 1)]
    evs = []
    for i, (l, dd, n) in enumerate(fj):
        o = 3 if (l == 'G' and dd == 'q') else 4
        e_ = {'pitch': l + str(o), 'dur': dd}
        if i < 14:
            e_['number'] = n
        evs.append(e_)
    d.add(sistema('Frère Jacques · mano derecha (los compases 7 y 8 bajan al Sol grave; la digitación de la segunda mitad es libre)', evs[:14], alto=116))
    d.add(sistema('… compases 5 a 8', evs[14:], alto=116))
    d.add(h2('Dictado rítmico'))
    d.add(par('Tu profesor toca o palmea un ritmo de **dos compases**; escríbelo. Decide primero la cifra de compás.', 9.3),
          pauta_vacia('treble', 2, None, titulo='1)'), pauta_vacia('treble', 2, None, titulo='2)'))
    sol(MES, 'Frère Jacques y dictado', 'Frère Jacques',
        ['Do Re Mi Do · Do Re Mi Do · Mi Fa Sol(blanca) · Mi Fa Sol(blanca) · Sol La Sol Fa (corcheas) Mi Do · Sol La Sol Fa Mi Do · Do Sol(grave) Do(blanca) · Do Sol(grave) Do(blanca). Dictado: libre.'])
