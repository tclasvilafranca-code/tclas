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

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']

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
