# -*- coding: utf-8 -*-
"""El reparto de la hoja de trabajo semanal en el cuaderno de Josep.

   Mismo mecanismo que `jm_recetas`, pero el reparto NO es la rotación simple
   P1..P10 + P1..P9. Aquí hay dos bloques que no pueden caer en cualquier
   pieza, porque saldrían falsos:

     - **`cifrado`** solo vale donde la edición imprime de verdad las letras de
       acorde encima del pentagrama. Comprobado una a una: piezas 5, 8, 11, 13,
       15, 17 y 19. En las demás, Josep no vería en su papel lo que la hoja le
       pide leer.
     - **`cuatro_manos`** solo vale en los cuatro duetos: piezas 1, 2, 10 y 14.

   Así que las parejas de hojas que comparten receta están elegidas para que
   las dos caigan donde el bloque tiene sentido:

       P1  → 1, 10    duetos
       P2  → 2, 14    duetos
       P5  → 5, 15    con cifrado impreso
       P8  → 8, 17    con cifrado impreso
       P10 → 11, 19   con cifrado impreso
       P3  → 3, 12       P4 → 4, 13       P6 → 6, 16
       P7  → 7, 18       P9 → 9 (una sola vez)

   La distancia mínima entre los dos usos de una receta queda en **ocho hojas**
   (la más corta es P10: 11 y 19). En José María eran diez, pero allí ninguna
   receta estaba atada a una propiedad de la partitura. Ocho sigue muy por
   encima de lo que audita `auditar_variedad` (seis) y de lo que nadie nota.

   Lo que NO rota, y sale las 19 semanas a propósito:

     - **`plan`**, los minutos por día. Igual que en José María.
     - **`escucha`**, que aquí es el recuadro de "para la próxima clase". Josep
       viene a clase; el hilo entre lo que hace en casa y lo que pregunta el
       día de la clase no se corta ninguna semana. Por eso `auditar_josep` los
       pasa los dos como estructurales.

   Y lo que no se usa nunca: sopa de letras, adivinanzas, crucigrama, el camino
   y el ritmo de las palabras. Son de Arnau, que tiene diez años.

   Costes medidos, para cuadrar el llenado (la `y` final entre 44 y 132):

     diferencias 143 · cuenta 142 · plan(4) 136 · vf(5) 132 · inventa 127
     escalera(4) 120 · teclado 118 · colorea 117 · figuras 114 · nombres 111
     cifrado 110 · une(4) 108 · dibuja 104 · ordena 104 · rodea 98
     metronomo 96 · escribe 84 · reto 66 · objetivo 60 · cuatro_manos 59
     escucha 48 · nota 41
"""

RECETAS = {
    'P1':  ['reto', 'plan', 'cuatro_manos', 'ordena', 'nombres', 'figuras', 'escucha'],
    'P2':  ['plan', 'cuatro_manos', 'escalera', 'diferencias', 'nombres', 'escucha'],
    'P3':  ['reto', 'plan', 'rodea', 'une', 'colorea', 'nota', 'escucha'],
    'P4':  ['plan', 'metronomo', 'vf', 'inventa', 'dibuja', 'escucha'],
    'P5':  ['reto', 'plan', 'escalera', 'cifrado', 'colorea', 'escucha'],
    'P6':  ['plan', 'metronomo', 'ordena', 'cuenta', 'teclado', 'escucha'],
    'P7':  ['reto', 'plan', 'escalera', 'inventa', 'teclado', 'escucha'],
    'P8':  ['plan', 'escalera', 'cifrado', 'une', 'nombres', 'escucha'],
    'P9':  ['reto', 'plan', 'metronomo', 'escribe', 'diferencias', 'nota', 'escucha'],
    'P10': ['reto', 'plan', 'cifrado', 'vf', 'figuras', 'escucha'],
}

#        pieza:  1     2     3     4     5     6     7     8     9    10
ORDEN = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P1',
#                11    12    13    14    15    16    17    18    19
         'P10', 'P3', 'P4', 'P2', 'P5', 'P6', 'P8', 'P7', 'P10']

# Las piezas cuya edición imprime el cifrado, comprobado sobre el PDF. Si
# alguna vez se cambia el orden del álbum hay que rehacer el reparto, y esta
# lista es la que dice dónde puede ir `cifrado`.
CON_CIFRADO = {5, 8, 11, 13, 15, 17, 19}

# Los cuatro duetos.
A_CUATRO_MANOS = {1, 2, 10, 14}


def receta(num_pieza):
    return ORDEN[num_pieza - 1]


def esqueleto(num_pieza):
    return RECETAS[receta(num_pieza)]


def revisar_reparto(modulos, verbose=True):
    """Comprueba que cada hoja de trabajo lleva los bloques que le manda el
       reparto, en ese orden, y que `cifrado` y `cuatro_manos` solo caen donde
       la partitura los justifica."""
    fallos, n = [], 0
    for mod in modulos:
        cfg = __import__(mod).CANCION
        for hoja in cfg.get('trabajo') or []:
            n += 1
            num = cfg['num']
            quiere = esqueleto(num)
            tiene = [b['tipo'] for b in hoja['bloques']]
            if tiene != quiere:
                fallos.append('%02d (%s): lleva %s y el reparto pide %s'
                              % (num, receta(num), ' > '.join(tiene),
                                 ' > '.join(quiere)))
            if 'cifrado' in tiene and num not in CON_CIFRADO:
                fallos.append('%02d: lleva cifrado y su partitura no imprime '
                              'letras de acorde' % num)
            if 'cuatro_manos' in tiene and num not in A_CUATRO_MANOS:
                fallos.append('%02d: lleva el bloque de duetos y no es un dueto' % num)
    if verbose:
        print('  reparto · %d hojas comprobadas contra jp_recetas · %s'
              % (n, 'ok' if not fallos else '%d fuera de sitio' % len(fallos)))
        for f in fallos:
            print('      %s' % f)
    return fallos
