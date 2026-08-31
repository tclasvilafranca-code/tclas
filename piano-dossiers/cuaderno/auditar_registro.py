# -*- coding: utf-8 -*-
"""Comprueba que ninguna nota cuelgue de mas lineas adicionales de las que se
   leen de un vistazo.

   Es el hermano pequeno de la norma "las dos manos van en su sistema de
   piano". Aquella arreglo 144 sistemas que escribian el acorde de la izquierda
   dentro del mismo evento que la melodia y lo dibujaban todo en clave de sol,
   con el Do3 colgando de SEIS lineas adicionales. Lo que no arreglo —porque
   nadie lo estaba mirando— fueron dos cosas que dejan el mismo dibujo ilegible:

     1. los sistemas escritos con `clef='bass'` A MANO en vez de con `manos=`,
        donde la nota de la derecha se queda en el pentagrama de fa. En el
        Gladiator de Merce y de Isaac habia un Mi5 en clave de fa: SEIS lineas
        adicionales, y encima el pie del sistema decia "entra la derecha";
     2. la cadencia I-IV-V-I de `relleno`, que se construye subiendo terceras
        desde el bajo y en segunda inversion se ponia nueve grados por encima:
        con un bajo en Do3 llegaba al Sol4. Eran 248 notas en los diez albumes.

   El limite es DOS lineas adicionales, que es lo que un pianista lee sin
   contar. En clave de fa eso es hasta el Mi4; en clave de sol, desde el La3
   hacia abajo y hasta el La5 hacia arriba.

   LO QUE NO PERSIGUE. Que una nota salga del pentagrama es normal y no es un
   fallo: el Re4 de un bajo que sube, o el Do6 de una escala, se leen bien. Lo
   que persigue es la nota que esta en el pentagrama EQUIVOCADO, que casi
   siempre se reconoce porque el propio pie del sistema dice "la derecha" y la
   nota esta en clave de fa.

   UNA EXCEPCION DE VERDAD, y por eso hay tabla: el cruce de manos. En *My
   Bonnie* la mano izquierda cruza por encima y toca un Sol4, y el ejercicio
   entero va de eso. Escribirlo en clave de sol escondería que lo toca la
   izquierda, que es justo lo que hay que ver.

   Uso:  python3 auditar_registro.py            (todos)
         python3 auditar_registro.py ed arnau   (solo esos prefijos)
"""
import contextlib
import glob
import importlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import hoja_piano                                                # noqa: E402

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'ai', 'dilan', 'eva']

_ORDEN = 'CDEFGAB'

# Hasta donde puede llegar cada clave sin pasar de dos lineas adicionales.
TOPES = {
    'bass':   ('E4', 'C1'),     # dos por arriba (Do4, Mi4) y dos por abajo
    'treble': ('C6', 'A3'),     # dos por arriba (La5, Do6) y dos por abajo (Do4, La3)
}

# Excepciones justificadas: (modulo, altura) -> motivo. Solo para casos en los
# que la nota esta en su pentagrama a proposito y cambiarla escondería lo que
# el ejercicio quiere ensenar.
EXCEPCIONES = {
    ('arnau_14_bonnie', 'G4'): 'el cruce de manos: lo toca la IZQUIERDA por encima, '
                               'y en clave de sol no se vería de quién es',
    ('ai_10_beginning', 'E6'): 'es la nota mas aguda del c. 4, y en SU edicion esta impresa '
                               'igual, con tres lineas adicionales. Bajarla una octava seria '
                               'contarle otra pieza; el ejercicio es justo leer esa cima',
}


def _grado(p):
    return int(p[-1]) * 7 + _ORDEN.index(p[0].upper())


def _piezas(prefijos):
    for pref in prefijos:
        for f in sorted(glob.glob(os.path.join(HERE, pref + '_[0-9]*.py'))):
            m = os.path.basename(f)[:-3]
            try:
                with contextlib.redirect_stdout(io.StringIO()), \
                     contextlib.redirect_stderr(io.StringIO()):
                    cfg = getattr(importlib.import_module(m), 'CANCION', None)
            except Exception:                                    # noqa: BLE001
                continue
            if cfg:
                yield m, cfg


def revisar(prefijos=None):
    fuera = []
    for m, cfg in _piezas(prefijos or PREFIJOS):
        hojas = [cfg.get('piano1'), cfg.get('piano2')]
        for hoja in hojas:
            if not hoja:
                continue
            for b in hoja.get('bloques', []) or []:
                for s in b.get('sistemas', []) or []:
                    clef = s.get('clef') or b.get('clef') or 'treble'
                    # Los sistemas que el motor abre en sistema de piano —los
                    # que llevan `manos=` y los que `_pide_dos_pentagramas`
                    # detecta solo, porque un acorde mezcla los dos registros—
                    # ya reparten cada nota a su pentagrama. Se pregunta al
                    # propio motor en vez de repetir aqui la regla: si un dia
                    # cambia, cambia en los dos sitios a la vez.
                    if s.get('manos') or hoja_piano._pide_dos_pentagramas(
                            s.get('events', []) or [], clef):
                        continue
                    if clef not in TOPES:
                        continue
                    alto, bajo = (_grado(x) for x in TOPES[clef])
                    for e in s.get('events', []) or []:
                        for p in ([e['pitch']] if e.get('pitch')
                                  else e.get('pitches', []) or []):
                            g = _grado(p)
                            if (g > alto or g < bajo) and (m, p) not in EXCEPCIONES:
                                fuera.append((m, clef, p, s.get('cap', '')[:44]))
    return sorted(set(fuera))


def main(prefijos=None):
    malas = revisar(prefijos)
    print('NOTAS EN EL PENTAGRAMA EQUIVOCADO (más de dos líneas adicionales): %d'
          % len(malas))
    for m, clef, p, cap in malas:
        print('   %-22s %-7s %-5s %s' % (m, clef, p, cap))
    if EXCEPCIONES:
        print('\nExcepciones justificadas: %d' % len(EXCEPCIONES))
        for (m, p), por in sorted(EXCEPCIONES.items()):
            print('   %-22s %-5s %s' % (m, p, por))
    if malas:
        return 1
    print('\nREGISTRO OK — ninguna nota cuelga de más de dos líneas adicionales.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
