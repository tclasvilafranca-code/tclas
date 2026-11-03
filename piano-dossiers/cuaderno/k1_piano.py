# -*- coding: utf-8 -*-
"""KIDS: pagina «Al piano» de cada mes (mismo formato siempre) y mapa del curso."""
from k1_base import *
from k1_comun import *
import k1_base as KB

# mes: (titulo, mussol, mano, inicio_teclado(0=DO,..), nb, dedos{indice:num}, notas, clave, pasos)
PIANO = {
    'Septiembre': ('Mis dedos sobre las teclas', 'Pon la mano derecha sobre cinco teclas blancas. El pulgar, en DO.', 'derecha', 0, 8, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
                   ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4'], 'treble',
                   ['Pon el dedo 1 en DO y un dedo en cada tecla.', 'Toca despacio: DO, RE, MI, FA, SOL.', 'Baja: SOL, FA, MI, RE, DO.']),
    'Octubre': ('Notas que suben y bajan', 'Si la nota sube en el pentagrama, la tecla está más a la derecha.', 'derecha', 0, 8, {0: 1, 2: 3, 4: 5},
                ['C4', 'E4', 'G4', 'E4', 'C4', 'D4', 'F4', 'D4'], 'treble',
                ['Mira la primera nota y toca su tecla.', 'Si la siguiente sube, mueve la mano a la derecha.', 'Si baja, a la izquierda.']),
    'Noviembre': ('La mano izquierda', 'La mano izquierda toca los sonidos graves. El meñique va en DO.', 'izquierda', 0, 8, {0: 5, 1: 4, 2: 3, 3: 2, 4: 1},
                  ['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3'], 'bass',
                  ['Pon el dedo 5 (meñique) en DO.', 'Toca despacio: DO, RE, MI, FA, SOL.', 'Baja de SOL a DO.']),
    'Diciembre': ('La escala de DO', 'Subimos ocho notas seguidas. El pulgar pasa por debajo en FA.', 'derecha', 0, 8, {0: 1, 1: 2, 2: 3, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5},
                  ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'], 'treble',
                  ['Toca 1-2-3.', 'Pasa el pulgar por debajo y toca 1-2-3-4-5.', 'Después baja con calma.']),
    'Enero': ('Cuento el compás', 'Cuento 1-2-3-4. El 1 suena un poco más fuerte.', 'derecha', 0, 8, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
              ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4'], 'treble',
              ['Cuenta en voz alta: 1-2-3-4.', 'Toca una nota en cada número.', 'Toca el 1 con un poco más de fuerza.']),
    'Febrero': ('Rápido y despacio', 'Una nota por golpe es despacio. Dos notas por golpe es más rápido.', 'derecha', 0, 8, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
                ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4'], 'treble',
                ['Toca una nota por palmada.', 'Toca dos notas por palmada.', 'Mantén siempre el mismo pulso.']),
    'Marzo': ('Clave de fa y mano izquierda', 'La clave de fa es para la mano izquierda.', 'izquierda', 0, 8, {0: 5, 1: 4, 2: 3, 3: 2, 4: 1},
              ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3'], 'bass',
              ['Lee las notas en clave de fa.', 'Toca con la mano izquierda.', 'Di el nombre de cada nota.']),
    'Abril': ('Toco y callo', 'En el silencio no toco, pero sigo contando.', 'derecha', 0, 8, {0: 1, 2: 3, 4: 5},
              ['C4', 'E4', 'G4', 'E4', 'C4'], 'treble',
              ['Toca DO, MI y SOL.', 'Cuenta 1-2-3-4 en voz alta.', 'Cuando hay un silencio, levanta la mano un momento.']),
    'Mayo': ('Notas largas', 'La ligadura y el puntillo alargan la nota. Cuento todos los tiempos.', 'derecha', 0, 8, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
             ['E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4'], 'treble',
             ['Toca la melodía despacio.', 'Cuenta los tiempos de cada nota larga.', 'No vuelvas a pulsar la tecla si la nota está ligada.']),
    'Junio': ('Preparo mi concierto', 'Elige una canción que te guste y tócala despacio.', 'derecha', 0, 8, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
              ['C4', 'D4', 'E4', 'F4', 'G4'], 'treble',
              ['Elige tu canción.', 'Tócala tres veces.', 'Tócala una vez para otra persona.']),
}


def K_manos_teclado(nb, inici, dedos, mano):
    h = 142

    def f(c, x, y, w):
        txt(c, x, y - 12, 'MANO %s' % mano.upper(), 11, ETQ, OCRE)
        res = {i: NOMBRES[(inici + i) % 7] for i in dedos}
        K.teclat(c, x + 6, y - 128, w - 12, 90, nb=nb, resalta=res, noms='resalta', color=True, dits=dedos, inici=inici)
    return Blk(h, f)


def al_piano(d, mes):
    tit, mus, mano, ini, nb, dedos, notas, clave, pasos = PIANO[mes]
    d.nuevo(mes)
    d.add(KB.K_titulo_act('♫', 'Al piano: ' + tit), K_mussol(mus),
          K_panel('', 'MIS DEDOS', [K_manos_teclado(nb, ini, dedos, mano)]),
          K_panel('', 'HAZLO ASÍ', [K_pasos(pasos), K_notas(clave, notas, titulo='Las notas de hoy', gap=10), K_hecho()]))


def mapa_curso(d, meses):
    """El camino del curso: diez paradas, de septiembre a junio, con Mussol al principio."""
    d.nuevo('Mi camino')
    d.add(K_titulo('Empezamos', 'El camino del curso', 'Diez paradas. Cada mes avanzo una.'), K_mussol('Cuando termines un mes, pinta su parada. Al final llegas al concierto.'))

    def f(c, x, y, w):
        pts = []
        for k in range(10):
            col = k % 2
            row = k // 2
            px = x + 70 + (row * (w - 140) / 4.0 if (row % 2 == 0) else 0)
            pts.append(None)
        # camino en zigzag: 2 filas de 5
        ys = [y - 60, y - 190]
        xs = [x + 50 + i * (w - 100) / 4.0 for i in range(5)]
        pos = [(xs[i], ys[0]) for i in range(5)] + [(xs[4 - i], ys[1]) for i in range(5)]
        trac(c, 5, SOMBRA)
        for a, b in zip(pos[:-1], pos[1:]):
            c.line(a[0], a[1], b[0], b[1])
        trac(c, 2, OCRE, (6, 5))
        for a, b in zip(pos[:-1], pos[1:]):
            c.line(a[0], a[1], b[0], b[1])
        c.setDash()
        for k, ((px, py), (mes, _, tema)) in enumerate(zip(pos, meses)):
            c.setFillColor(OCRE if k < 9 else NAVY)
            trac(c, 2, NAVY)
            c.circle(px, py, 24, stroke=1, fill=1)
            txt(c, px, py - 7, str(k + 1), 21, SANSB, white, 'c')
            txt(c, px, py - 40, mes, 10.5, SANSB, NAVY, 'c')
            kpar(c, px - 46, py - 54, tema, 8.6, 92, 10, SANS, MUTED)
    d.add(K_panel('', 'MIS DIEZ PARADAS', [Blk(250, f)]))
