# -*- coding: utf-8 -*-
"""Generador de HOJAS LLENAS de notas.

   Lo que pidio el cliente para el calentamiento y para la agudeza visual es
   lo mismo en los dos casos: la hoja entera de pentagramas, de arriba abajo,
   con notas de verdad — figuras variadas, silencios, compases distintos y
   las dos claves del piano. Escribir eso a mano para veinte canciones no
   tiene sentido, asi que se genera.

   Dos reglas que vienen de antes y siguen valiendo:

   1. ANTI-SECUENCIA. Si las notas siguen un patron, el alumno lo adivina y
      deja de leer. Por eso los saltos y los ritmos se eligen al azar, y se
      comprueba que ninguna linea repita la celula de la anterior.

   2. CUADRAR. Cada linea suma compases enteros, siempre. Los patrones
      ritmicos estan definidos por compas y por eso no puede fallar; el
      auditor lo comprueba igual.

   El azar va con semilla fija (el numero de cancion), asi que la hoja de la
   cancion 7 es siempre la misma hoja: se puede reimprimir y el alumno no se
   encuentra con otra cosa.
"""
import random

# Las figuras que el motor sabe escribir. No hay semicorcheas ni fusas: si se
# anaden aqui sin anadirlas al motor, la hoja sale muda.
DUR = {'w': 4.0, 'h.': 3.0, 'h': 2.0, 'q.': 1.5, 'q': 1.0, 'e': 0.5}

# Patrones de un compas, por compas y por dificultad. El indice es el nivel
# minimo en el que aparece: 0 = desde la primera cancion, 2 = solo al final.
PATRONES = {
    (4, 4): [
        (0, ['q', 'q', 'q', 'q']),
        (0, ['h', 'q', 'q']),
        (0, ['q', 'q', 'h']),
        (0, ['h', 'h']),
        (0, ['w']),
        (0, ['q', 'q', 'q', 'Rq']),
        (1, ['Rq', 'q', 'q', 'q']),
        (1, ['e', 'e', 'q', 'q', 'q']),
        (1, ['q', 'q', 'e', 'e', 'q']),
        (1, ['h.', 'q']),
        (1, ['q.', 'e', 'h']),
        (1, ['h', 'Rq', 'q']),
        (2, ['q.', 'e', 'q', 'q']),
        (2, ['e', 'e', 'e', 'e', 'h']),
        (2, ['q', 'Rq', 'q', 'q']),
        (2, ['Re', 'e', 'q', 'q', 'q']),
        (2, ['e', 'e', 'e', 'e', 'e', 'e', 'q']),
        (2, ['h', 'q.', 'e']),
    ],
    (3, 4): [
        (0, ['q', 'q', 'q']),
        (0, ['h', 'q']),
        (0, ['q', 'h']),
        (0, ['h.']),
        (0, ['q', 'q', 'Rq']),
        (1, ['Rq', 'q', 'q']),
        (1, ['e', 'e', 'q', 'q']),
        (1, ['q', 'e', 'e', 'q']),
        (1, ['q.', 'e', 'q']),
        (2, ['e', 'e', 'e', 'e', 'q']),
        (2, ['q', 'Rq', 'q']),
        (2, ['Re', 'e', 'q', 'q']),
    ],
    (2, 4): [
        (0, ['q', 'q']),
        (0, ['h']),
        (0, ['q', 'Rq']),
        (1, ['e', 'e', 'q']),
        (1, ['q', 'e', 'e']),
        (1, ['q.', 'e']),
        (2, ['e', 'e', 'e', 'e']),
        (2, ['Rq', 'q']),
    ],
    (6, 8): [
        (0, ['q.', 'q.']),
        (0, ['e', 'e', 'e', 'e', 'e', 'e']),
        (0, ['h.']),
        (1, ['q.', 'e', 'e', 'e']),
        (1, ['e', 'e', 'e', 'q.']),
        (1, ['q', 'e', 'q', 'e']),
        (2, ['q.', 'q', 'e']),
        (2, ['e', 'e', 'e', 'q', 'e']),
    ],
}

# Registro comodo por clave: de la mas grave a la mas aguda, en grados de la
# escala. Se amplia con el nivel.
REGISTRO = {
    'treble': (('C4', 'C6'), ('G3', 'A6')),
    'bass':   (('C2', 'C4'), ('F1', 'E4')),
}

_LETRAS = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def _midi(nombre):
    letra, octava = nombre[0], int(nombre[1:])
    return octava * 7 + _LETRAS.index(letra)


def _nombre(pos):
    return '%s%d' % (_LETRAS[pos % 7], pos // 7)


def escala_grados(tonalidad, clef, nivel):
    """Todas las notas de la escala dentro del registro de esa clave.
       Devuelve posiciones diatonicas, no nombres: asi los saltos se cuentan
       por grados y nunca sale una nota fuera de la tonalidad."""
    estrecho, ancho = REGISTRO[clef]
    lo, hi = ancho if nivel >= 2 else estrecho
    return list(range(_midi(lo), _midi(hi) + 1))


def _elige_patron(rng, time_sig, nivel):
    ops = [p for lvl, p in PATRONES[tuple(time_sig)] if lvl <= nivel]
    return list(rng.choice(ops))


def linea(rng, tonalidad, clef, time_sig, compases, nivel=1, salto_max=None):
    """Una linea de N compases llenos. Devuelve la lista de eventos.

       salto_max es cuantos grados puede moverse de una nota a la siguiente:
       en el calentamiento se toca, asi que conviene poco; en la agudeza se
       recita y puede saltar mas."""
    grados = escala_grados(tonalidad, clef, nivel)
    if salto_max is None:
        salto_max = 2 + nivel
    pos = rng.randrange(len(grados) // 4, 3 * len(grados) // 4)
    eventos = []
    for _ in range(compases):
        for fig in _elige_patron(rng, time_sig, nivel):
            if fig.startswith('R'):
                eventos.append({'rest': True, 'dur': fig[1:]})
                continue
            paso = rng.randint(-salto_max, salto_max)
            if paso == 0:
                paso = rng.choice((-1, 1))
            pos = max(0, min(len(grados) - 1, pos + paso))
            eventos.append({'pitch': _nombre(grados[pos]), 'dur': fig})
    return _barrar(eventos)


def _barrar(eventos, _contador=[7000]):
    """Une las corcheas seguidas bajo una barra. Sin esto cada corchea sale
       con su corchete y la hoja parece un ejercicio de solfeo, no musica."""
    i = 0
    while i < len(eventos):
        if eventos[i].get('dur') == 'e' and 'pitch' in eventos[i]:
            j = i
            while (j < len(eventos) and eventos[j].get('dur') == 'e'
                   and 'pitch' in eventos[j]):
                j += 1
            if j - i >= 2:
                _contador[0] += 1
                for k in range(i, j):
                    eventos[k]['beam'] = _contador[0]
            i = j
        else:
            i += 1
    return eventos


def hoja(tonalidad, semilla, n_lineas=12, nivel=1, compases=4,
         claves=('treble', 'bass'), compases_extra=(), salto_max=None):
    """La hoja entera: una lista de dicts listos para imprimir.

       Cada uno lleva su clave, su compas y sus eventos. Las claves se
       alternan y, a partir de cierto punto, se meten compases distintos del
       de la pieza para que el alumno no se acostumbre a uno solo."""
    rng = random.Random(semilla)
    base = compases_extra[0] if compases_extra else (4, 4)
    salida, anterior = [], None
    for i in range(n_lineas):
        clef = claves[i % len(claves)]
        ts = base
        if compases_extra and i >= 2:
            ts = compases_extra[i % len(compases_extra)]
        # cuantos compases caben depende de la figura mas corta que se use
        bars = compases if ts != (2, 4) else compases + 2
        for _ in range(6):                      # anti-secuencia: no repetir
            ev = linea(rng, tonalidad, clef, ts, bars, nivel, salto_max)
            firma = tuple(e.get('pitch', 'R') for e in ev[:6])
            if firma != anterior:
                break
        anterior = firma
        salida.append(dict(clef=clef, time_sig=ts, events=ev, bars=bars))
    return salida
