# -*- coding: utf-8 -*-
"""El reparto de la hoja de trabajo semanal en el cuaderno de José María.

   Mismo mecanismo que `arnau_recetas`, pero para el formato de adulto: aquí
   hay UNA hoja de trabajo por pieza (19 en total), no dos.

   Diez recetas, cada una usada dos veces (la última, una), y siempre con diez
   hojas de distancia entre sus dos usos. Así no se repite la forma de la hoja
   ni de lejos, que es lo que pide la norma de variedad.

   Lo que NO rota: el `plan` de minutos por día. Está en las 19 hojas a
   propósito, y por eso `auditar_variedad` lo cuenta como estructural. José
   María estudia solo en casa: lo que más le falla no es tocar, es saber por
   dónde empezar cuando se sienta al teclado. Eso no se quita ninguna semana.

   Y lo que no se usa nunca en este cuaderno: sopa de letras, adivinanzas,
   crucigrama, el camino y el ritmo de las palabras. Son de Arnau, que tiene
   diez años. A un adulto le sobran.

   Costes medidos, para cuadrar el llenado de la hoja (la `y` final tiene que
   quedar entre 44 y 132):

     diferencias 143 · cuenta 142 · plan(4) 136 · vf(5) 132 · inventa 127
     teclado 118 · colorea 117 · figuras 114 · vf(4) 114 · nombres 111
     une(4) 108 · dibuja 104 · ordena 104 · rodea 98 · metronomo 96
     escribe 84 · objetivo 60 · escucha 48 · nota 41
"""

RECETAS = {
    'J1':  ['objetivo', 'plan', 'teclado', 'cuenta', 'figuras', 'nota'],
    'J2':  ['plan', 'metronomo', 'diferencias', 'nombres', 'escribe', 'nota'],
    'J3':  ['objetivo', 'plan', 'rodea', 'une', 'colorea', 'nota', 'escucha'],
    'J4':  ['plan', 'vf', 'inventa', 'dibuja', 'metronomo'],
    'J5':  ['objetivo', 'plan', 'ordena', 'cuenta', 'teclado', 'escucha'],
    'J6':  ['plan', 'metronomo', 'nombres', 'colorea', 'escribe', 'escucha'],
    'J7':  ['objetivo', 'plan', 'diferencias', 'figuras', 'une', 'nota'],
    'J8':  ['plan', 'teclado', 'inventa', 'rodea', 'metronomo', 'escucha'],
    'J9':  ['objetivo', 'plan', 'vf', 'dibuja', 'cuenta', 'escucha'],
    'J10': ['plan', 'metronomo', 'ordena', 'colorea', 'nombres', 'escucha'],
}

# 19 piezas: J1..J10 y luego J1..J9.
ORDEN = (['J%d' % i for i in range(1, 11)]
         + ['J%d' % i for i in range(1, 10)])


def receta(num_pieza):
    return ORDEN[num_pieza - 1]


def esqueleto(num_pieza):
    return RECETAS[receta(num_pieza)]


def revisar_reparto(modulos, verbose=True):
    """Comprueba que cada hoja de trabajo lleva los bloques que le manda el
       reparto, en ese orden."""
    fallos, n = [], 0
    for mod in modulos:
        cfg = __import__(mod).CANCION
        for hoja in cfg.get('trabajo') or []:
            n += 1
            quiere = esqueleto(cfg['num'])
            tiene = [b['tipo'] for b in hoja['bloques']]
            if tiene != quiere:
                fallos.append('%02d (%s): lleva %s y el reparto pide %s'
                              % (cfg['num'], receta(cfg['num']),
                                 ' > '.join(tiene), ' > '.join(quiere)))
    if verbose:
        print('  reparto · %d hojas comprobadas contra jm_recetas · %s'
              % (n, 'ok' if not fallos else '%d fuera de sitio' % len(fallos)))
        for f in fallos:
            print('      %s' % f)
    return fallos
