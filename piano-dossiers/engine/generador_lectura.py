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
# minimo en el que aparece: 0 = desde la primera cancion, 3 = solo para los
# alumnos avanzados.
#
# El NIVEL 3 se anadio cuando el cliente pidio que el nivel fuera de verdad
# distinto en cada cuaderno: hasta entonces "intermedio" y "avanzado" recibian
# exactamente el mismo material, porque el techo estaba en 2 y los dos llegaban
# igual. Lo que trae el 3 no son figuras nuevas —el motor no escribe
# semicorcheas ni tresillos— sino lo que de verdad cuesta leer: silencios en
# mitad del compas, notas largas que empiezan a contratiempo y corcheas que
# cruzan el golpe.
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
        (3, ['e', 'Re', 'e', 'e', 'q', 'q']),
        (3, ['q', 'e', 'e', 'Rq', 'q']),
        (3, ['Re', 'e', 'e', 'e', 'q.', 'e']),
        (3, ['q.', 'e', 'e', 'e', 'e', 'e']),
        (3, ['e', 'e', 'q.', 'e', 'q']),
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
        (3, ['e', 'Re', 'e', 'e', 'q']),
        (3, ['q.', 'e', 'e', 'e']),
        (3, ['e', 'e', 'e', 'e', 'e', 'e']),
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
        (3, ['e', 'Re', 'e', 'e']),
        (3, ['e', 'q.']),
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
        (3, ['e', 'Re', 'e', 'e', 'e', 'e']),
        (3, ['q', 'e', 'e', 'e', 'e']),
    ],
}

def _revisar_patrones():
    """Ningun patron puede dejar el compas a medias.

       Se comprueba al importar el modulo, y no en el auditor de cada alumno,
       porque un patron malo no rompe una pieza: rompe TODAS las que caigan en
       ese nivel y ese compas, y eso se ve tarde. Paso de verdad al estrenar
       el nivel 3: tres de los patrones nuevos sumaban 4,5 o 5 tiempos."""
    dur = {'w': 4.0, 'h.': 3.0, 'h': 2.0, 'q.': 1.5, 'q': 1.0, 'e.': 0.75,
           'e': 0.5}
    malos = []
    for ts, lista in PATRONES.items():
        entero = ts[0] * (4.0 / ts[1])
        for nivel, pat in lista:
            total = sum(dur[f[1:] if f.startswith('R') else f] for f in pat)
            if abs(total - entero) > 1e-6:
                malos.append('%s nivel %d: %s suma %g y el compas son %g'
                             % (ts, nivel, ' '.join(pat), total, entero))
    if malos:
        raise ValueError('patrones que no llenan el compas:\n  ' + '\n  '.join(malos))


_revisar_patrones()


# Patrones de RELAJACION. Aqui no se entrena nada: se toca para soltar el
# brazo cuando ya esta cansado. Lo que hace lenta a esta hoja NO es tener
# pocas notas — es el tempo, que va escrito arriba. El pentagrama va lleno.
#
#   - nada mas corto que la negra: en cuanto hay corcheas, la mano corre;
#   - un silencio de vez en cuando, no en todos los compases: es el hueco
#     para soltar la mano encima de las teclas;
#   - el compas se llena, para que haya musica de verdad que tocar.
#
# El motor no dibuja silencios con puntillo, asi que aqui no aparecen.
PATRONES_RELAX = {
    (4, 4): [
        ['h', 'h'],
        ['q', 'q', 'h'],
        ['h', 'q', 'q'],
        ['q', 'q', 'q', 'q'],
        ['h.', 'q'],
        ['q', 'h', 'q'],
        ['w'],
        ['h', 'q', 'Rq'],
        ['q', 'q', 'Rh'],
    ],
    (3, 4): [
        ['h', 'q'],
        ['q', 'q', 'q'],
        ['q', 'h'],
        ['h.'],
        ['q', 'q', 'Rq'],
    ],
}

# La progresion sobre la que se escribe la hoja de relajacion. Es lo que hace
# que unas notas al azar suenen a musica y no a ejercicio: cada compas tiene
# su acorde, las notas salen de ese acorde y la linea acaba siempre en la
# tonica. En grados de la escala (0 = tonica), asi vale igual en mayor y en
# menor: I - vi - IV - V - I - IV - V - I, que en menor es i - VI - iv - v - i.
PROGRESION = [0, 5, 3, 4, 0, 3, 4, 0]

# Tonica de cada tonalidad. Hace falta para saber que grado es cada nota y
# poder construir los acordes; la armadura ya pone los bemoles y sostenidos.
TONICA = {
    'Do mayor': 'C', 'La menor': 'A', 'Sol mayor': 'G', 'Mi menor': 'E',
    'Re mayor': 'D', 'Si menor': 'B', 'La mayor': 'A', 'Fa# menor': 'F',
    'Fa mayor': 'F', 'Re menor': 'D', 'Sib mayor': 'B', 'Si♭ mayor': 'B',
    'Mib mayor': 'E', 'Mi♭ mayor': 'E', 'Sol menor': 'G', 'Do menor': 'C',
    'Mi mayor': 'E', 'Do# menor': 'C', 'La♭ mayor': 'A', 'Lab mayor': 'A',
}

# Registro comodo por clave: de la mas grave a la mas aguda, en grados de la
# escala. Se amplia con el nivel, pero poco: esto se toca y se lee de un
# vistazo, y a partir de dos lineas adicionales deja de leerse y se descifra.
REGISTRO = {
    'treble': (('C4', 'G5'), ('A3', 'C6')),
    'bass':   (('G2', 'C4'), ('D2', 'E4')),
}

# El nivel 3 lee mas arriba y mas abajo todavia: dos lineas adicionales por
# cada lado, que es donde un alumno avanzado deja de reconocer la nota de un
# vistazo y tiene que leerla de verdad.
REGISTRO_ANCHO = {
    'treble': ('F3', 'F6'),
    'bass':   ('A1', 'A4'),
}

# Cuantos compases entran comodos en una linea, por compas. Cinco compases de
# 4/4 con corcheas no caben: salen apretados y el alumno pierde el sitio.
COMPASES_LINEA = {(4, 4): 4, (3, 4): 5, (2, 4): 6, (6, 8): 4}

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
    if nivel >= 3:
        lo, hi = REGISTRO_ANCHO[clef]
    else:
        lo, hi = ancho if nivel >= 2 else estrecho
    return list(range(_midi(lo), _midi(hi) + 1))


def _elige_patron(rng, time_sig, nivel, relax=False):
    if relax:
        return list(rng.choice(PATRONES_RELAX[tuple(time_sig)]))
    ops = [p for lvl, p in PATRONES[tuple(time_sig)] if lvl <= nivel]
    return list(rng.choice(ops))


def _elige_altura(rng, grados, grado_de, pos, permitidos, bajar=True, salto=4):
    """La siguiente nota: de las que valen (las del acorde, o cualquiera si es
       nota de paso), la que esta cerca — y, en igualdad, la de abajo."""
    cand = [i for i in range(len(grados))
            if grado_de(grados[i]) in permitidos and 0 < abs(i - pos) <= salto]
    if not cand:
        cand = [i for i in range(len(grados)) if grado_de(grados[i]) in permitidos]
    if not cand:
        return pos

    def peso(i):
        w = 1.0 / (abs(i - pos) + 0.5)
        return w * 1.7 if (bajar and i < pos) else w

    total = sum(peso(i) for i in cand)
    r, acc = rng.random() * total, 0.0
    for i in cand:
        acc += peso(i)
        if acc >= r:
            return i
    return cand[-1]


def linea_relax(rng, tonalidad, clef, time_sig, compases):
    """Una linea de relajacion: llena de figuras, pero sobre una progresion.

       Cada compas tiene su acorde y las notas salen de el; entre dos notas
       del acorde cae de vez en cuando una nota de paso, que es lo que hace
       que la linea suene a melodia y no a arpegio de estudio. Y la ultima
       nota es siempre la tonica: una linea que se queda colgada no relaja a
       nadie, aunque las notas sean largas."""
    grados = escala_grados(tonalidad, clef, 0)
    raiz = _LETRAS.index(TONICA.get(tonalidad or 'Do mayor', 'C'))

    def grado_de(p):
        return (p - raiz) % 7

    pos = len(grados) // 2
    eventos = []
    for compas in range(compases):
        fund = PROGRESION[compas % len(PROGRESION)]
        acorde = {fund % 7, (fund + 2) % 7, (fund + 4) % 7}
        patron = _elige_patron(rng, time_sig, 0, relax=True)
        ultimo_compas = compas == compases - 1
        for k, fig in enumerate(patron):
            if fig.startswith('R'):
                eventos.append({'rest': True, 'dur': fig[1:]})
                continue
            # la ultima nota de la linea cierra en la tonica
            resto = [f for f in patron[k + 1:] if not f.startswith('R')]
            if ultimo_compas and not resto:
                permitidos = {0}
            elif k == 0 or rng.random() < 0.72:
                permitidos = acorde
            else:
                permitidos = set(range(7))      # nota de paso
            pos = _elige_altura(rng, grados, grado_de, pos, permitidos,
                                bajar=rng.random() < 0.6)
            eventos.append({'pitch': _nombre(grados[pos]), 'dur': fig})
    return eventos


def linea(rng, tonalidad, clef, time_sig, compases, nivel=1, salto_max=None,
          relax=False):
    """Una linea de N compases llenos. Devuelve la lista de eventos.

       salto_max es cuantos grados puede moverse de una nota a la siguiente:
       en el calentamiento se toca, asi que conviene poco; en la agudeza se
       recita y puede saltar mas; en relajacion, casi nada — un salto obliga a
       estirar la mano, y estirar es lo contrario de soltar."""
    grados = escala_grados(tonalidad, clef, 0 if relax else nivel)
    if salto_max is None:
        salto_max = 2 if relax else 2 + nivel
    ultimo = len(grados) - 1
    centro = ultimo / 2.0
    pos = rng.randrange(len(grados) // 4, 3 * len(grados) // 4)
    # En compas de subdivision ternaria las corcheas van de tres en tres; en
    # los demas, de dos en dos, una barra por tiempo.
    por_barra = 3 if tuple(time_sig) == (6, 8) else 2
    eventos = []
    for _ in range(compases):
        compas = []
        for fig in _elige_patron(rng, time_sig, nivel, relax):
            if fig.startswith('R'):
                compas.append({'rest': True, 'dur': fig[1:]})
                continue
            paso = rng.randint(-salto_max, salto_max)
            if paso == 0:
                paso = rng.choice((-1, 1))
            # En relajacion la linea tiende a bajar: el brazo cae solo, y una
            # linea que sube pide fuerza justo cuando se busca lo contrario.
            if relax and rng.random() < 0.62:
                paso = -abs(paso)
            # Vuelta al centro. Un paseo al azar sin esto acaba pegado a un
            # extremo del registro y se queda ahi: media hoja colgando de
            # cuatro lineas adicionales, que ya no se lee, se descifra.
            fuera = abs(pos - centro) / centro if centro else 0
            if fuera > 0.5 and rng.random() < fuera:
                paso = -abs(paso) if pos > centro else abs(paso)
            nueva = pos + paso
            if nueva < 0 or nueva > ultimo:
                nueva = pos - paso          # rebota, no se pega al tope
            pos = max(0, min(ultimo, nueva))
            compas.append({'pitch': _nombre(grados[pos]), 'dur': fig})
        eventos.extend(_barrar(compas, por_barra))
    return eventos


def _barrar(eventos, por_barra=2, _contador=[7000]):
    """Une las corcheas seguidas bajo una barra. Sin esto cada corchea sale
       con su corchete y la hoja parece un ejercicio de solfeo, no musica.

       Se llama COMPAS A COMPAS y agrupa de `por_barra` en `por_barra`: una
       barra no puede cruzar la linea divisoria ni juntar dos tiempos. Antes
       se llamaba sobre la linea entera y salian barras de ocho corcheas
       pasando por encima del compas siguiente."""
    i = 0
    while i < len(eventos):
        if eventos[i].get('dur') == 'e' and 'pitch' in eventos[i]:
            j = i
            while (j < len(eventos) and eventos[j].get('dur') == 'e'
                   and 'pitch' in eventos[j]):
                j += 1
            for ini in range(i, j, por_barra):
                fin = min(ini + por_barra, j)
                if fin - ini >= 2:
                    _contador[0] += 1
                    for k in range(ini, fin):
                        eventos[k]['beam'] = _contador[0]
            i = j
        else:
            i += 1
    return eventos


def hoja(tonalidad, semilla, n_lineas=12, nivel=1, compases=4,
         claves=('treble', 'bass'), compases_extra=(), salto_max=None,
         relax=False):
    """La hoja entera: una lista de dicts listos para imprimir.

       Cada uno lleva su clave, su compas y sus eventos. Las claves se
       alternan y, a partir de cierto punto, se meten compases distintos del
       de la pieza para que el alumno no se acostumbre a uno solo.

       Con relax=True cambia el material entero: figuras largas, silencios y
       saltos minimos. Las claves siguen alternando, y ahi eso ya no es
       variedad sino parte del ejercicio — mientras una mano toca, la otra
       esta muerta encima de las teclas, que es donde de verdad descansa."""
    rng = random.Random(semilla)
    base = compases_extra[0] if compases_extra else (4, 4)
    if relax and base not in PATRONES_RELAX:
        base = (4, 4)
    salida, anterior = [], None
    for i in range(n_lineas):
        clef = claves[i % len(claves)]
        ts = base
        if compases_extra and i >= 2:
            ts = compases_extra[i % len(compases_extra)]
        if relax and ts not in PATRONES_RELAX:
            ts = base
        bars = COMPASES_LINEA.get(ts, compases)
        if relax:
            # cuatro compases por linea: con las figuras largas de relajacion
            # es lo que llena el pentagrama sin apretarlo
            bars = 4
        for _ in range(6):                      # anti-secuencia: no repetir
            ev = (linea_relax(rng, tonalidad, clef, ts, bars) if relax else
                  linea(rng, tonalidad, clef, ts, bars, nivel, salto_max))
            firma = tuple(e.get('pitch', 'R') for e in ev[:6])
            if firma != anterior:
                break
        anterior = firma
        salida.append(dict(clef=clef, time_sig=ts, events=ev, bars=bars))
    return salida
