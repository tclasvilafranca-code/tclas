# -*- coding: utf-8 -*-
"""Cruza el ANDAMIO de las 199 piezas leyendo los datos, no el dibujo.

   Los siete `cruzar_*.py` comparan lo que sale dibujado y solo miran sistemas
   de ocho eventos o mas: es lo correcto para pillar coincidencias que aparecen
   despues de partir las manos, pero se le escapan los sistemas cortos, que en
   un cuaderno de piano son la mayoria.

   Esto hace la comprobacion por el otro lado: abre las piezas, recorre los
   sistemas escritos a mano en `piano1`/`piano2` y busca el mismo material en
   dos piezas distintas, con cuatro eventos ya basta.

   La regla del proyecto no es "que nada se repita": las CITAS literales de
   compases medidos TIENEN que coincidir cuando dos alumnos tocan la misma
   partitura, porque es la misma musica. Lo que no puede repetirse es lo
   INVENTADO. Por eso cada coincidencia se clasifica leyendo la pista del
   bloque y el pie del sistema:

     - si dicen MEDIDO, literal o citan un compas ("c. 12"), es una cita y sale
       marcada como esperada;
     - si no lo dicen, es andamio, y entonces son dos alumnos recibiendo el
       mismo ejercicio inventado sin motivo.

   Sale 1 solo si aparece andamio repetido.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']

# A partir de cuantos eventos merece la pena comparar. Con menos de cuatro
# coinciden hasta los ejercicios que no se parecen en nada.
MINIMO = 4

# Lo que marca material sacado de la partitura: dice que esta medido, lo llama
# literal, cita un compas ("c. 12", "cc. 5-8") o sale de los cifrados impresos.
CITA = re.compile(r'medid[oa]s?\b|literal|\bcc?\.\s*\d|cifrado|tal cual', re.IGNORECASE)

# Y lo que lo desmiente: si la pista dice "andamio", esta inventado, aunque
# ademas cite el compas del que sale la idea. Ojo con las pistas que dicen
# justo lo contrario ("MEDIDO sobre tu partitura, no es andamio"): esas hay que
# quitarlas antes de buscar, o el aviso se lee al reves.
NIEGA = re.compile(r'no\s+es\s+andamio', re.IGNORECASE)
INVENTADO = re.compile(r'andamio', re.IGNORECASE)


def _inventado(texto):
    return bool(INVENTADO.search(NIEGA.sub('', texto)))


def _firma(events):
    """Altura y figura de cada evento: lo que el alumno ve escrito."""
    fuera = []
    for e in events:
        if e.get('rest'):
            fuera.append(('R', e.get('dur')))
        elif e.get('pitches'):
            fuera.append((tuple(e['pitches']), e.get('dur')))
        else:
            fuera.append((e.get('pitch'), e.get('dur')))
    return tuple(fuera)


# La unica coincidencia que se da por buena aun siendo andamio, y por que.
#
# La entrada del Jailhouse Rock: el compas 1 son tres silencios LITERALES y una
# sola nota libre, y esa nota es el Si bemol, que es justo lo que el bloque
# entero viene a ensenar ("El Si bemol: donde vive el blues"). Con lo demas
# medido y el unico hueco ocupado por la nota de la leccion, cambiarsela a tres
# de los cuatro alumnos seria escribir peor a proposito.
EXCUSADAS = {
    (('R', 'h'), ('R', 'q'), ('R', 'e'), ('Bb4', 'e'), ('C5', 'w')):
        'la entrada del Jailhouse: silencios literales y el Si bemol de la leccion',
}


def _excusado(firma, usos):
    return firma in EXCUSADAS


def _sistemas(cfg):
    """(firma, es_cita, etiqueta) de cada sistema escrito a mano de la pieza."""
    fuera = []
    for hoja in [cfg.get('piano1')] + [cfg.get('piano2')]:
        if not hoja:
            continue
        for blq in hoja.get('bloques') or []:
            if blq.get('tipo') == 'nota':
                continue
            pista = blq.get('pista') or ''
            titulo = blq.get('titulo') or ''
            for i, sis in enumerate(blq.get('sistemas') or []):
                events = sis.get('events') or []
                if len(events) < MINIMO:
                    continue
                # El material de `relleno` (escalas, arpegios, cadencias) viene
                # marcado y puede coincidir: es tecnica de la tonalidad.
                if all(e.get('tecnica') for e in events):
                    continue
                # El pie del propio sistema manda sobre la pista del bloque: un
                # bloque puede mezclar una linea de andamio con la cita de un
                # compas, y entonces la pista habla de las dos a la vez.
                cap = sis.get('cap') or ''
                if _inventado(cap):
                    cita = False
                elif CITA.search(cap):
                    cita = True
                else:
                    texto = ' '.join((pista, titulo))
                    cita = bool(CITA.search(texto)) and not _inventado(texto)
                fuera.append((_firma(events), cita,
                              '%s · %s' % (titulo or 'bloque', chr(ord('a') + i)),
                              ' · '.join(x for x in (pista, cap) if x)))
    return fuera


def main(prefijos=None):
    modulos = []
    for p in prefijos or PREFIJOS:
        modulos += [os.path.basename(f)[:-3]
                    for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py')))]

    vistos, total = {}, 0
    for m in modulos:
        # Dilan y Eva parten cada pieza en `_data` (los datos medidos) y
        # `_cancion` (el montaje): solo el segundo trae CANCION.
        cfg = getattr(__import__(m), 'CANCION', None)
        if not cfg:
            continue
        for firma, cita, etiq, pista in _sistemas(cfg):
            total += 1
            vistos.setdefault(firma, []).append((m, cita, etiq, pista))

    citas, andamio = [], []
    for firma, usos in vistos.items():
        if len({u[0] for u in usos}) < 2:
            continue
        # Basta con que UNA de las dos piezas documente de donde sale: si un
        # lado dice "c. 12" y el otro lo cuenta con otras palabras, el material
        # es el mismo compas de la misma partitura y TIENE que coincidir.
        cita = any(u[1] for u in usos) or _excusado(firma, usos)
        (citas if cita else andamio).append((firma, usos))

    print('piezas: %d · sistemas escritos a mano comparados: %d (desde %d eventos)'
          % (len(modulos), total, MINIMO))
    print('\ncitas literales que coinciden (esperado, es la misma partitura): %d' % len(citas))
    for firma, usos in sorted(citas, key=lambda x: -len(x[0])):
        print('   %2d eventos · %s%s' % (len(firma), ', '.join(u[0] for u in usos),
                                         '  ← ' + EXCUSADAS[firma] if firma in EXCUSADAS else ''))

    print('\nandamio inventado repetido en dos piezas (esto SI es un fallo): %d' % len(andamio))
    for firma, usos in sorted(andamio, key=lambda x: -len(x[0])):
        print('   %2d eventos · %s' % (len(firma), ' '.join(
            '%s(%s)' % (p if isinstance(p, str) else '+'.join(p), d) for p, d in firma)))
        for mod, _c, etiq, pista in usos:
            print('        %-20s %s' % (mod, etiq))
            print('        %-20s   pista: %s' % ('', pista or '(sin pista)'))
    return 1 if andamio else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
