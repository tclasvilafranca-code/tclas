# -*- coding: utf-8 -*-
"""Comprueba que las ALTURAS que la ficha presenta como medidas son las impresas.

   El quinto dato, y el ultimo que no tenia testigo. Los otros cuatro —compas,
   armadura, figura mas corta y tempo— ya se leen del papel y se cruzan solos.
   Las notas no: se transcribian a mano, costaban mucho, y precisamente por eso
   nadie las volvia a mirar.

   Lo destapo una revision a tamano real del album de Arnau. *Polly Put the
   Kettle On* presentaba como "la melodia del principio" lo que es el COMPAS 2,
   y su pentagrama traia dos notas que no estan en la partitura. Al medir las
   demas salieron tres mas: *Silent Night* (dos alumnos) escrita una TERCERA por
   debajo, *El submarino amarillo* y *Aloha Oe* con un Do4 delante que el papel
   no trae.

   QUE COMPARA. Solo las filas de `ficha.ritmos` que DICEN traer las alturas
   medidas: las que hablan de andamio quedan fuera a proposito, porque ahi las
   alturas son material inventado sobre la tonalidad y no tienen que coincidir
   con nada. Son once filas en las 197 piezas — pocas, pero son justo las que el
   alumno lee como "asi empieza mi cancion".

   COMO. `medir_arranque.arranque` lee del PDF el primer compas del pentagrama
   de arriba. Se comparan los NOMBRES de nota (sin alteracion: la armadura ya la
   audita `auditar_tonalidad`) tantos como haya leido el papel. Si el papel no da
   para leerlo, la pieza aparece en la lista de "no se puede medir" y hay que
   mirarla a ojo y anotarla en `MIRADAS` — igual que en `auditar_figuras`.

   LO QUE NO VE, y conviene tener presente antes de fiarse:

     - solo el PRIMER compas, y solo el pentagrama de ARRIBA. Una pieza a cuatro
       manos en la que el alumno lleva la parte de abajo pasa por aqui sin que
       se haya comprobado lo suyo;
     - no lee las figuras, solo las alturas. El ritmo lo cruza `auditar_figuras`;
     - una anacrusa muy pegada a la cifra de compas se le puede escapar, porque
       la cabecera se descuenta por ancho.

   Uso:  python3 auditar_alturas.py
"""
import contextlib
import glob
import importlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import auditar_tonalidad as at                                      # noqa: E402
import medir_arranque as ma                                         # noqa: E402

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'ai', 'dilan', 'eva']

# Una fila entra en la comprobacion si dice que las alturas salen del papel y NO
# dice que sea andamio. La palabra manda: en este proyecto "andamio" significa
# material construido sobre la tonalidad, y ahi las alturas son nuestras.
DICE_MEDIDO = re.compile(r'medid|literal|tal y como|tal como', re.I)
ES_ANDAMIO = re.compile(r'andamio', re.I)

# Partituras cuyo primer compas no se puede leer (una foto de poca resolucion, o
# un arranque que el lector no sabe recortar) y lo que se vio al ampliarlas.
# Mirarlas y no anotar el resultado seria mirarlas para nada.
MIRADAS = {
    # El lector se deja la PRIMERA nota de este compas: esta edicion pega la
    # cifra de compas a la musica y el salto de cabecera se la come. Se miro
    # ampliada del todo (26 ago 2026) y el compas 1 es Do5 · Sol4 · Do5 · Sol4
    # · Do5, negra, negra, corchea, corchea y negra. Se anota aqui en vez de
    # aflojar el detector: al probar a aflojarlo aparecio un Fa5 fantasma en
    # *Los aristogatos* que era la palabra "Adagio".
    'Eso que tu me das.pdf': ['C5', 'G4', 'C5', 'G4', 'C5'],

    # --- We Wish You a Merry Christmas, mirado el 31 de agosto de 2026 ----
    #
    # El lector devuelve ['G4', 'D4'] y no es eso: la pieza empieza con una
    # ANACRUSA de una negra, y al detector le cuadra el primer compas con la
    # anacrusa dentro. Medido a 300 ppp, y comprobado ademas contra la letra
    # impresa debajo (que es la mejor prueba que hay: cada silaba tiene su
    # nota), la entrada es:
    #
    #     anacrusa   Re4                    negra          "1.We"
    #     c. 1       Sol4                   negra          "wish"
    #                Sol4 · La4             corcheas       "you a"
    #                Sol4 · Fa#4            corcheas       "mer-ry"
    #     c. 2       Mi4 · Mi4 · Mi4        negras         "Christ-mas, We"
    #
    # Los Fa van a la tecla negra porque la armadura trae un sostenido.
    # Esta lectura destapo que las citas de Isaac y de Merce decian
    # Re4 · Sol4 · La4 · Si4(blanca con puntillo), que no es lo impreso: ni
    # el ritmo ni las alturas. La aritmetica cuadraba (1+1+1+3 = dos compases
    # de 3/4) y por eso no la cazo ningun auditor.
    # La lista arranca en el COMPAS 1, sin la anacrusa: una fila de la ficha
    # tiene que sumar compases enteros, y anacrusa mas dos compases son siete
    # tiempos en un 3/4. La anacrusa se cuenta en la prosa de la ficha, que es
    # donde se explica; dibujarla con dos silencios delante seria inventarse
    # dos tiempos que el papel no imprime.
    'WE WISH YOU A MERRY CHRISTMAS.pdf':
        ['G4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'E4', 'E4'],
    'We Wish You a Merry Christmas.pdf':
        ['G4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'E4', 'E4'],

    # --- las cinco de Eduard, miradas el 26 de agosto de 2026 ---------------
    #
    # El lector ve tres cabezas en el c. 1 y a la tercera le pone Si5. No es
    # una nota: es la palabra "Swing" impresa encima del pentagrama, que tiene
    # agujeros cerrados igual que una blanca. Ampliado a 300 ppp se ve que las
    # tres cabezas del c. 1 estan en la MISMA linea adicional, la del do
    # central: negra, negra y blanca.
    'Heart and Soul.pdf': ['C4', 'C4', 'C4'],

    # La primera nota cuelga de DOS lineas adicionales y va pegada a la cifra
    # de compas, asi que el descuento de cabecera se la come — el mismo caso
    # que *Eso que tu me das*. Ampliado se ve el La3 (negra), el Mi4 (negra con
    # puntillo) y el Re4 (corchea), y el c. 2 es un Fa4 en redonda.
    'I Have a Dream.pdf': ['A3', 'E4', 'D4', 'F4'],

    # Con tres sostenidos el descuento de cabecera es tan largo que el lector
    # se planta en el c. 3 mal recortado y devuelve un Si4 que es la plica de
    # la primera nota. Ampliado, y con la tabla de lineas al lado, el c. 3 es
    # Do#4, Fa#4 y La4: las tres notas del acorde de Fa# menor.
    'Honor Him Gladiator.pdf': ['C#4', 'F#4', 'A4'],

    # Aqui la primera "cabeza" del c. 1 es el SILENCIO DE BLANCA, que es un
    # rectangulo macizo y pasa la apertura morfologica como si fuera una nota.
    # Lo impreso es: c. 1 silencio de blanca y Fa4; c. 2 Fa4 y Sol4.
    'Piano Man.pdf': ['F4', 'F4', 'G4'],

    # A cuatro manos, y en esta edicion las divisorias no unen ni siquiera los
    # dos pentagramas del Primo, asi que el lector no encuentra el final del
    # primer compas. Ampliado: Mi5, Mi5 y Mi5 (negra, negra y blanca), que es
    # el arranque de *Jingle Bells*.
    'Christmas Songs 4 manos.pdf': ['E5', 'E5', 'E5'],

    # --- las tres de Aida que el lector no sabe recortar, medidas a mano ------
    #
    # A cuatro manos otra vez, y con el mismo problema que el Christmas Songs:
    # las divisorias no unen los dos pentagramas del Piano 1, asi que el lector
    # no encuentra el final del c. 1 y mezcla las dos manos (devuelve
    # E5-A4-E5-F5, y el A4 es del pentagrama de abajo). Medido el 31 de agosto
    # de 2026 sobre las cinco lineas de cada pentagrama: el c. 1 de arriba es
    # un silencio de negra con puntillo, Mi5 (negra) y Fa5 (corchea).
    'Its Beginning to Look 4 manos.pdf': ['E5', 'F5'],
    ' its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf': ['E5', 'F5'],
    'its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf': ['E5', 'F5'],
    'its-beginning-to-look-a-lot-like (4 manos).pdf': ['E5', 'F5'],

    # El c. 1 de la derecha es un COMPAS ENTERO DE SILENCIO y el lector solo
    # salta hasta dos compases vacios cuando no distingue ninguna cabeza; aqui
    # el silencio de redonda es un rectangulo macizo que pasa la apertura como
    # si fuera una nota, asi que devuelve un Do5 fantasma. Lo primero que suena
    # es el c. 2: Re4 Re4 Fa4 Fa4 La4 La4, todo corcheas tras un silencio de
    # negra.
    'The Sound of Silence.pdf': ['D4', 'D4', 'F4', 'F4', 'A4', 'A4'],

    # Empieza con una ANACRUSA de un tiempo (silencio de corchea con puntillo y
    # un Mi4 en semicorchea), asi que al lector le cuadra el "primer compas" con
    # la anacrusa dentro y devuelve E4-B4-A4. El primer compas completo es el
    # c. 2: Si4 (negra con doble puntillo), Mi4 (semicorchea), Si4 (negra con
    # doble puntillo), Sol4 (semicorchea).
    'Gladiator.pdf': ['B4', 'E4', 'B4', 'G4'],

    # El lector DUPLICA cabezas en esta edicion: devuelve diecisiete notas para
    # un compas que tiene doce, con los Do5 y los Mi5 repetidos de dos en dos.
    # Son las semicorcheas mas apretadas de las diecinueve partituras (276
    # pares de barras dobles) y ahi la cabeza, la plica y el arranque de la
    # barra le salen como dos manchas.
    #
    # Medido a 300 ppp el 1 de septiembre de 2026, cabeza a cabeza contra las
    # cinco lineas: el c. 1 son DOS MITADES IGUALES, y cada mitad es un
    # silencio de corchea, dos semicorcheas barradas (Sol4 · Do5) y cuatro mas
    # (Mi5 · Sol4 · Do5 · Mi5). Suma 0,5 + 0,5 + 1 = 2 tiempos por mitad.
    'Preludio n1 Bach.pdf': ['G4', 'C5', 'E5', 'G4', 'C5', 'E5',
                             'G4', 'C5', 'E5', 'G4', 'C5', 'E5'],
}


def _n_alteraciones(key):
    m = re.match(r'(\d)', at.ARMADURA.get(key or '', '0') or '0')
    return int(m.group(1)) if m else 0


def _piezas(prefijos):
    fuera = []
    for p in prefijos:
        for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py'))):
            m = os.path.basename(f)[:-3]
            with contextlib.redirect_stdout(io.StringIO()), \
                 contextlib.redirect_stderr(io.StringIO()):
                cfg = getattr(importlib.import_module(m), 'CANCION', None)
            if not cfg:
                continue
            ficha = cfg.get('ficha') or {}
            filas = ficha.get('ritmos') or []
            if not filas:
                continue
            fila = filas[0]
            texto = (ficha.get('pie_ritmos') or '') + ' ' + (fila[1] or '')
            if ES_ANDAMIO.search(texto) or not DICE_MEDIDO.search(texto):
                continue
            dice = [e['pitch'] for e in fila[2] if e.get('pitch')]
            if len(dice) < 3:
                continue
            fuera.append((m, cfg.get('partitura') or '',
                          _n_alteraciones(cfg.get('key_sig')), dice))
    return fuera


def main(prefijos=None):
    piezas = _piezas(prefijos or PREFIJOS)
    cache, malos, sin_saber = {}, [], []
    for m, ruta, nalt, dice in piezas:
        base = os.path.basename(ruta)
        if base in MIRADAS:
            leido = MIRADAS[base]
        else:
            if not os.path.exists(ruta):
                sin_saber.append((m, base, 'la partitura no está en el disco'))
                continue
            clave = (ruta, nalt)
            if clave not in cache:
                try:
                    cache[clave] = ma.arranque(ruta, alteraciones=nalt)
                except ma.NoMedible as e:
                    cache[clave] = str(e)
                except Exception as e:                               # noqa: BLE001
                    cache[clave] = 'no se ha podido leer: %s' % e
            leido = cache[clave]
        if isinstance(leido, str):
            sin_saber.append((m, base, leido))
            continue
        a = [x[0] for x in dice][:len(leido)]
        b = [x[0] for x in leido]
        if a != b:
            malos.append((m, ' '.join(dice[:8]), ' '.join(leido[:8])))

    print('filas que dicen traer las alturas medidas: %d' % len(piezas))

    print('\nLA FICHA DIBUJA UNAS NOTAS Y LA PARTITURA TRAE OTRAS: %d' % len(malos))
    for m, dice, trae in malos:
        print('   %-22s ficha %-30s papel %s' % (m, dice, trae))

    print('\nPartituras cuyo arranque no se puede leer ni está en MIRADAS: %d'
          % len(sin_saber))
    for m, base, por in sin_saber:
        print('   %-22s %-32s %s' % (m, base[:32], por))

    if malos or sin_saber:
        print('\n%d COSAS QUE MIRAR' % (len(malos) + len(sin_saber)))
        return 1
    print('\nALTURAS OK — lo que la ficha presenta como medido es lo impreso.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
