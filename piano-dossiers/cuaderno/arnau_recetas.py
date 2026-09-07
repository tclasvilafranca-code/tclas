# -*- coding: utf-8 -*-
"""El reparto de ejercicios por semana en el cuaderno de Arnau.

   Norma de variedad del cliente: dos semanas seguidas no pueden llevar los
   mismos ejercicios en el mismo orden. Con 40 hojas de deberes eso no se puede
   improvisar hoja a hoja, así que el reparto está decidido aquí y las hojas lo
   siguen. Así el auditor puede comprobar dos cosas distintas: que el reparto
   cumple la norma, y que cada hoja cumple el reparto.

   Cómo está hecho
   ---------------
   Hay 20 recetas, cada una con su esqueleto de bloques. Se usan **dos veces
   cada una** a lo largo de las 40 hojas, y siempre con 10 hojas de distancia
   como mínimo, así que Arnau nunca ve la misma forma de hoja dos veces
   seguidas ni parecido.

   El orden de las hojas es: canción 1 semana 1, canción 1 semana 2, canción 2
   semana 1… Las recetas se reparten R1…R20 en las 20 primeras hojas, y luego
   R11…R20 y R1…R10, que es lo que deja la distancia más grande entre los dos
   usos de cada receta.

   Cada receta está calculada para llenar la hoja (la `y` final tiene que
   quedar entre 44 y 132). Los costes en puntos, medidos:

     sopa 275 · crucigrama 231 · diferencias 143 · cuenta 142 · vf(5) 132
     camino(5) 129 · inventa 127 · palmas(3) 124 · teclado 118 · colorea 117
     figuras 114 · vf(4) 114 · nombres 111 · camino(4) 110 · une(4) 108
     adivina(3) 108 · dibuja 104 · ordena 104 · rutina 101 · rodea 98
     escribe 84 · escucha 48 · nota 41

   Donde la receta se queda corta se sube el tamaño del bloque, no se rellena
   con paja: R4, R9 y R16 llevan cinco frases de verdadero o falso en vez de
   cuatro, y R5 y R18 llevan cinco filas de camino en vez de cuatro.
"""

RECETAS = {
    'R1':  ['sopa', 'figuras', 'adivina', 'rutina', 'escucha'],
    'R2':  ['crucigrama', 'nombres', 'colorea', 'rutina', 'escucha'],
    'R3':  ['diferencias', 'cuenta', 'teclado', 'nota', 'rutina', 'escucha'],
    'R4':  ['vf', 'palmas', 'rodea', 'dibuja', 'rutina', 'nota'],
    'R5':  ['camino', 'nombres', 'inventa', 'une', 'rutina', 'escucha'],
    'R6':  ['sopa', 'ordena', 'colorea', 'rutina', 'nota'],
    'R7':  ['crucigrama', 'palmas', 'figuras', 'nota', 'rutina', 'escucha'],
    'R8':  ['teclado', 'adivina', 'rodea', 'cuenta', 'rutina', 'escucha'],
    'R9':  ['diferencias', 'vf', 'dibuja', 'escribe', 'rutina', 'nota'],
    'R10': ['nombres', 'camino', 'palmas', 'une', 'rutina', 'escucha'],
    'R11': ['sopa', 'une', 'vf', 'rutina', 'escucha'],
    'R12': ['cuenta', 'inventa', 'ordena', 'colorea', 'nota', 'rutina'],
    'R13': ['crucigrama', 'diferencias', 'adivina', 'rutina', 'escucha'],
    'R14': ['teclado', 'palmas', 'nombres', 'camino', 'nota', 'rutina'],
    'R15': ['sopa', 'diferencias', 'nota', 'rutina', 'escucha'],
    'R16': ['vf', 'ordena', 'figuras', 'dibuja', 'rutina', 'nota'],
    'R17': ['crucigrama', 'cuenta', 'une', 'rutina', 'nota'],
    'R18': ['camino', 'adivina', 'rodea', 'teclado', 'escribe', 'rutina'],
    'R19': ['palmas', 'inventa', 'nombres', 'vf', 'nota', 'rutina'],
    'R20': ['sopa', 'teclado', 'escribe', 'rutina', 'escucha'],
}

# El orden de las 40 hojas: R1..R20, luego R11..R20 y R1..R10.
ORDEN = (['R%d' % i for i in range(1, 21)]
         + ['R%d' % i for i in range(11, 21)]
         + ['R%d' % i for i in range(1, 11)])


def receta(num_cancion, semana):
    """La receta que le toca a la canción `num_cancion` (1..20) en su semana
       `semana` (1 o 2)."""
    return ORDEN[(num_cancion - 1) * 2 + (semana - 1)]


def esqueleto(num_cancion, semana):
    return RECETAS[receta(num_cancion, semana)]


def revisar_reparto(modulos, verbose=True):
    """Comprueba que cada hoja de deberes lleva los bloques que le manda el
       reparto, en ese orden. Devuelve la lista de fallos."""
    fallos = []
    for mod in modulos:
        cfg = __import__(mod).CANCION
        for semana, hoja in enumerate(cfg.get('deberes') or [], 1):
            quiere = esqueleto(cfg['num'], semana)
            tiene = [b['tipo'] for b in hoja['bloques']]
            if tiene != quiere:
                fallos.append('%02d s%d (%s): lleva %s y el reparto pide %s'
                              % (cfg['num'], semana, receta(cfg['num'], semana),
                                 ' > '.join(tiene), ' > '.join(quiere)))
    if verbose:
        print('  reparto · %d hojas comprobadas contra arnau_recetas · %s'
              % (sum(len(__import__(m).CANCION.get('deberes') or []) for m in modulos),
                 'ok' if not fallos else '%d fuera de sitio' % len(fallos)))
        for f in fallos:
            print('      %s' % f)
    return fallos
