# -*- coding: utf-8 -*-
"""Material verificado de El Cisne (Saint-Saëns, arr. rev. Ricardo Boppré).

   TODO lo que hay aquí está medido sobre el PDF de la partitura; el método y
   los compases exactos están en TRANSCRIPCION_D01_EL_CISNE.md. Lo que no se
   ha medido no aparece: la sección central cromática (cc. 13-42) no se cita
   con detalle en ningún ejercicio.

   Con armadura de Sol mayor los Fa se escriben SIN sostenido explícito: la
   armadura ya los altera, y ponerlo otra vez sería un error de escritura.
"""

TONALIDAD = 'Sol mayor'
COMPAS = (3, 4)

# --- mano izquierda: la célula de acompañamiento, seis corcheas por compás --
CELULA_I   = ['G2', 'D3', 'B3', 'D3', 'B3', 'D3']    # cc. 1-4  · Sol mayor
CELULA_ii  = ['G2', 'E3', 'A3', 'E3', 'A3', 'E3']    # cc. 5-7  · La menor /Sol
CELULA_I7  = ['G2', 'D3', 'F3', 'D3', 'F3', 'D3']    # c.  8    · Sol maj7


_BEAM = [0]


def corcheas(pitches, n=1, agrupar=6):
    """Corcheas con barra: seis por compas bajo una sola barra, como las
       escribe la edicion. Sin 'beam' cada corchea sale con su corchete suelto
       y el pentagrama parece un ejercicio de solfeo, no una partitura."""
    out = []
    for _ in range(n):
        for i, p in enumerate(pitches):
            if i % agrupar == 0:
                _BEAM[0] += 1
            out.append({'pitch': p, 'dur': 'e', 'beam': _BEAM[0]})
    return out


# los ocho primeros compases de la izquierda, tal cual están escritos
MI_1_8 = (corcheas(CELULA_I, 4) + corcheas(CELULA_ii, 3) + corcheas(CELULA_I7))

# --- mano derecha: el tema -------------------------------------------------
MD_3_4 = [{'pitch': 'G5', 'dur': 'q'}, {'pitch': 'F5', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'},
          {'pitch': 'E5', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}]

# cc. 7-9: la escala de Sol mayor completa, escrita dentro de la pieza
MD_7_9 = ([{'pitch': 'E4', 'dur': 'h'}] +
          [{'pitch': p, 'dur': 'e', 'beam': 900} for p in ['F4', 'G4']] +
          [{'pitch': p, 'dur': 'e', 'beam': 901} for p in ['A4', 'B4', 'C5', 'D5', 'E5', 'F5']] +
          [{'pitch': 'G5', 'dur': 'h.'}])
