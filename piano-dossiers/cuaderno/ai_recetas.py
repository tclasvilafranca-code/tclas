# -*- coding: utf-8 -*-
"""El reparto de la hoja de trabajo semanal en el cuaderno de Aida.

   Mismo mecanismo que `jp_recetas`, y con los mismos dos bloques que no pueden
   caer en cualquier pieza porque saldrian falsos:

     - **`cifrado`** solo vale donde la edicion imprime de verdad las letras de
       acorde encima del pentagrama. Comprobado sobre el PDF una a una: piezas
       3, 4, 5, 7, 16 y 19. En las demas, Aida no veria en su papel lo que la
       hoja le pide leer.
     - **`cuatro_manos`** solo vale en los tres duetos: piezas 1, 2 y 10. La
       otra parte la toca la profesora en clase (decision del cliente), y por
       eso el bloque habla de lo que hay que acordar con ella.

   POR QUE LA DISTANCIA MINIMA AQUI ES SIETE Y NO OCHO. En Josep las dos
   recetas de una pareja quedan a ocho hojas. Aqui no se puede, y la razon es
   aritmetica, no de dejadez: con diecinueve piezas, una hoja en el puesto 12 o
   mas tarde solo puede emparejarse con una de las cuatro primeras, y las
   piezas que admiten `cifrado` estan casi todas al principio (3, 4, 5 y 7) y
   sus dos parejas tardias son la 16 y la 19. Con la distancia en ocho, el
   reparto solo deja UNA pareja con cifrado en las dos hojas; con siete deja
   dos, que es lo que hace que el bloque salga cuatro veces en el curso y no
   dos. Siete sigue por encima de lo que audita `auditar_variedad` (seis) y muy
   por encima de lo que nadie nota. `auditar_aida` audita en siete.

       A1  -> 1, 10     duetos
       A2  -> 2         dueto, receta de una sola hoja
       A3  -> 3, 16     con cifrado impreso
       A4  -> 7, 19     con cifrado impreso
       A5  -> 5, 12        A6 -> 6, 13      A7 -> 4, 14
       A8  -> 8, 15        A9 -> 9, 17      A10 -> 11, 18

   Lo que NO rota, y sale las 19 semanas a proposito:

     - **`plan`**, los minutos por dia.
     - **`escucha`**, que aqui es el recuadro de "para la proxima clase". Aida
       viene a clase; el hilo entre lo que hace en casa y lo que pregunta el dia
       de la clase no se corta ninguna semana. Por eso `auditar_aida` los pasa
       los dos como estructurales.

   Y lo que no se usa nunca: sopa de letras, adivinanzas, crucigrama, el camino
   y el ritmo de las palabras. Son de Arnau, que tiene diez anos.

   Costes medidos (los mismos bloques que Josep, misma hoja):

     diferencias 143 · cuenta 142 · plan(4) 136 · vf(5) 132 · inventa 127
     escalera(4) 120 · teclado 118 · colorea 117 · figuras 114 · nombres 111
     cifrado 110 · une(4) 108 · dibuja 104 · ordena 104 · rodea 98
     metronomo 96 · escribe 84 · reto 66 · objetivo 60 · cuatro_manos 59
     escucha 48 · nota 41

   Las diez recetas suman entre 604 y 646, que es la banda en la que la hoja
   cierra con la `y` final entre 44 y 132.
"""

RECETAS = {
    'A1':  ['reto', 'plan', 'cuatro_manos', 'nombres', 'diferencias', 'nota', 'escucha'],
    'A2':  ['plan', 'cuatro_manos', 'escalera', 'cuenta', 'teclado', 'escucha'],
    'A3':  ['reto', 'plan', 'cifrado', 'colorea', 'figuras', 'nota', 'escucha'],
    'A4':  ['plan', 'escalera', 'cifrado', 'vf', 'escribe', 'escucha'],
    'A5':  ['reto', 'plan', 'metronomo', 'une', 'colorea', 'nota', 'escucha'],
    'A6':  ['plan', 'escalera', 'inventa', 'dibuja', 'nombres', 'escucha'],
    'A7':  ['reto', 'plan', 'objetivo', 'teclado', 'ordena', 'figuras', 'escucha'],
    'A8':  ['plan', 'metronomo', 'diferencias', 'rodea', 'dibuja', 'escucha'],
    'A9':  ['reto', 'plan', 'escalera', 'cuenta', 'rodea', 'escucha'],
    'A10': ['plan', 'objetivo', 'vf', 'inventa', 'une', 'escucha'],
}

#        pieza:  1     2     3     4     5     6     7     8     9    10
ORDEN = ['A1', 'A2', 'A3', 'A7', 'A5', 'A6', 'A4', 'A8', 'A9', 'A1',
#                11    12    13    14    15    16    17    18    19
         'A10', 'A5', 'A6', 'A7', 'A8', 'A3', 'A9', 'A10', 'A4']

# Las piezas cuya edicion imprime el cifrado, comprobado sobre el PDF. Si
# alguna vez se cambia el orden del album hay que rehacer el reparto, y esta
# lista es la que dice donde puede ir `cifrado`.
CON_CIFRADO = {3, 4, 5, 7, 16, 19}

# Los tres duetos: los dos Diabelli y el villancico a cuatro manos.
A_CUATRO_MANOS = {1, 2, 10}


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
        print('  reparto · %d hojas comprobadas contra ai_recetas · %s'
              % (n, 'ok' if not fallos else '%d fuera de sitio' % len(fallos)))
        for f in fallos:
            print('      %s' % f)
    return fallos
