# -*- coding: utf-8 -*-
"""Material de apoyo para las hojas "al piano", derivado de la propia pieza.

   POR QUE EXISTE. Al escribir las dos manos en su sistema de piano —sol arriba,
   fa abajo, que es como se lee el piano— el bloque de manos juntas dejo de
   caber con los demas y el cliente decidio darle una segunda hoja. Eso dejo 88
   piezas con las dos hojas a medio llenar, y el estandar del proyecto es claro:
   una hoja a medias no se entrega, se llena.

   QUE NO ES. No es relleno. Estas funciones NO inventan una melodia: construyen
   escalas, arpegios y giros SOBRE LA TONALIDAD DE LA PIEZA, que es material de
   tecnica de toda la vida y lo que un profesor escribiria a mano en el margen.
   Los rotulos —lo que se le pide al alumno y por que— se escriben a mano en
   cada pieza; aqui solo viven las notas, para que no se cuele una nota que no
   pertenece a la tonalidad.

   COMO SE USA. En el archivo de la cancion:

       from relleno import escala, arpegio, giro

       dict(num=4, titulo='...', pista='andamio en Sol mayor · ...',
            sistemas=[dict(cap='a) ...', events=escala('Sol mayor', 'G4'), bars=2)])

   La regla de no repetirse entre alumnos sigue vigente y la comprueba
   `cruzar_<alumno>.py`: por eso todas admiten `desde`, `sentido` y `figura`,
   que es lo que separa la escala de un alumno de la del de al lado.
"""
import re

# Los siete grados de cada tonalidad, en orden, con su alteracion escrita como
# la escribe el motor ('Bb4', 'F#4'). No se deduce de la armadura al vuelo
# porque las menores armonicas alteran el septimo grado y eso hay que decidirlo,
# no adivinarlo: aqui van las escalas NATURALES, y si una pieza necesita la
# sensible alterada se escribe a mano en su archivo.
GRADOS = {
    'Do mayor':  ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'Sol mayor': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'Re mayor':  ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'La mayor':  ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'Mi mayor':  ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'Fa mayor':  ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
    'Sib mayor': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
    'Mib mayor': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
    'Lab mayor': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
    'La menor':  ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Mi menor':  ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'Si menor':  ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
    'Re menor':  ['D', 'E', 'F', 'G', 'A', 'Bb', 'C'],
    'Sol menor': ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'],
    'Do menor':  ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
    'Fa menor':  ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'],
    'Fa# menor': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
    'Do# menor': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
    'Re dórico': ['D', 'E', 'F', 'G', 'A', 'B', 'C'],
}

_ORDEN = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def _parte(p):
    m = re.match(r'^([A-G])([b#]?)(-?\d+)$', str(p))
    if not m:
        raise ValueError('altura rara: %r' % (p,))
    return m.group(1), m.group(2), int(m.group(3))


def _sube(letra, octava, pasos):
    """Sube `pasos` grados diatonicos desde una letra, llevando la octava."""
    i = _ORDEN.index(letra) + pasos
    return _ORDEN[i % 7], octava + i // 7


def _en_tono(tono, letra, octava):
    """La misma letra con la alteracion que le toca en esa tonalidad."""
    for g in GRADOS[tono]:
        if g[0] == letra:
            return '%s%d' % (g, octava)
    return '%s%d' % (letra, octava)


def escala(tono, desde, notas=8, sentido='sube', figura='q', **extra):
    """Los grados de la tonalidad, seguidos, desde la nota que se le diga.

       Es el ejercicio mas viejo que hay y sigue siendo el que mas arregla:
       coloca la mano en el tono de la pieza antes de tocarla."""
    letra, _alt, octava = _parte(desde)
    fuera = []
    for k in range(notas):
        paso = k if sentido == 'sube' else -k
        l, o = _sube(letra, octava, paso)
        fuera.append(dict(pitch=_en_tono(tono, l, o), dur=figura, **extra))
    return fuera


def arpegio(tono, desde, figura='q', ida_vuelta=True, **extra):
    """El acorde de la tonalidad desplegado: 1-3-5-8 y de vuelta 8-5-3-1.

       Ocho notas justas, o sea dos compases de cuatro por cuatro, y cierra en
       la nota de partida: un arpegio que acaba colgando en el aire hace que el
       alumno acelere para terminar cuanto antes."""
    letra, _alt, octava = _parte(desde)
    subida = [_en_tono(tono, *_sube(letra, octava, paso)) for paso in (0, 2, 4, 7)]
    camino = subida + list(reversed(subida)) if ida_vuelta else subida
    return [dict(pitch=p, dur=figura, **extra) for p in camino]


def giro(tono, centro, figura='q', **extra):
    """El giro de siempre alrededor de una nota: la de arriba, la de abajo, y
       vuelta. Es lo que suelta un dedo agarrotado sin cambiar de posicion."""
    letra, _alt, octava = _parte(centro)
    arriba = _en_tono(tono, *_sube(letra, octava, 1))
    abajo = _en_tono(tono, *_sube(letra, octava, -1))
    c = _en_tono(tono, letra, octava)
    return [dict(pitch=p, dur=figura, **extra)
            for p in (c, arriba, c, abajo, c, arriba, c, c)]


def cadencia(tono, bajo, figura='w'):
    """I - IV - V - I en la mano izquierda, en estado fundamental.

       Los tres acordes que sostienen casi todo el repertorio del cuaderno.
       Saberlos de memoria en el tono de la pieza es lo que permite acompanar
       sin leer, y es teoria que se toca, no que se estudia."""
    letra, _alt, octava = _parte(bajo)
    fuera = []
    for grado in (0, 3, 4, 0):
        raiz_l, raiz_o = _sube(letra, octava, grado)
        notas = []
        for paso in (0, 2, 4):
            l, o = _sube(raiz_l, raiz_o, paso)
            notas.append(_en_tono(tono, l, o))
        fuera.append(dict(pitches=notas, dur=figura))
    return fuera
