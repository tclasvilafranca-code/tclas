# -*- coding: utf-8 -*-
"""Comprueba que cada alumno solo ve las figuras de SU escalon (ver niveles.py).

   Mira el material escrito a mano —`piano1`/`piano2` y los ritmos de la ficha—,
   que es donde se decide el nivel. Las hojas generadas (calentamiento, agudeza
   visual, relajacion) no entran: son notas al azar por diseno del cliente y su
   dificultad la gobierna `cancion.CURVA`.

   Uso:  python3 auditar_niveles.py            (todos)
         python3 auditar_niveles.py arnau lu   (solo esos prefijos)
"""
import sys
import os
import glob
import io
import contextlib
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from niveles import NIVELES, ESCALON, EXCEPCIONES, RACHAS_JUSTIFICADAS, escalon_de

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']

RECURSOS = ('lig', 'art', 'tresillo', 'matiz', 'cresc', 'dim', 'pedal')


def _eventos(cfg):
    """Todos los eventos escritos a mano, con su procedencia."""
    out = []
    for donde, ev in _sistemas(cfg):
        for e in ev:
            out.append((donde, e))
    return out


def _sistemas(cfg):
    """(procedencia, lista de eventos) de cada sistema escrito a mano."""
    out = []
    for k in ('piano1', 'piano2'):
        for b in (cfg.get(k) or {}).get('bloques', []) or []:
            for i, s in enumerate(b.get('sistemas', []) or []):
                donde = '%s b%s s%d' % (k, b.get('num', '-'), i + 1)
                out.append((donde, [e for e in (s.get('events', []) or [])
                                    if isinstance(e, dict)]))
    for r in (cfg.get('ficha') or {}).get('ritmos', []) or []:
        if len(r) > 2 and isinstance(r[2], list):
            out.append(('ficha.ritmos', [e for e in r[2] if isinstance(e, dict)]))
    return out


def _racha_corta(eventos):
    """La racha mas larga de notas cortas seguidas (corcheas o semicorcheas).

       Un silencio corta la racha: es justo lo que da aire y lo que distingue
       'dos corcheas' de 'una carrerilla'."""
    peor = cur = 0
    for e in eventos:
        if e.get('rest'):
            cur = 0
            continue
        if e.get('dur') in ('e', 'e.', 's', 's.'):
            cur += 1
            peor = max(peor, cur)
        else:
            cur = 0
    return peor


def revisar(modulo):
    """Devuelve la lista de incumplimientos de una pieza."""
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        mod = importlib.import_module(modulo)
    cfg = getattr(mod, 'CANCION', None)
    if cfg is None:
        return []
    alumno = cfg.get('alumno', '')
    n = escalon_de(alumno)
    if n is None:
        return ['%s: alumno %r sin escalón asignado en niveles.py' % (modulo, alumno)]
    nivel = NIVELES[n]
    num = cfg.get('num', 0)
    fallos = []

    for donde, e in _eventos(cfg):
        dur = e.get('dur')
        es_sil = bool(e.get('rest'))
        if dur is not None:
            permitidas = nivel['silencios'] if es_sil else nivel['figuras']
            if dur not in permitidas and (modulo, dur) not in EXCEPCIONES:
                fallos.append('%s · %s: %s%r fuera del nivel %d'
                              % (modulo, donde, 'silencio ' if es_sil else '', dur, n))
            minimo = nivel['desde'].get(dur)
            if (minimo and num < minimo and not es_sil
                    and (modulo, dur) not in EXCEPCIONES):
                fallos.append('%s · %s: %r aparece en la pieza %d y el nivel %d '
                              'no la admite antes de la %d'
                              % (modulo, donde, dur, num, n, minimo))
        ps = e.get('pitches')
        if ps and len(ps) > nivel['max_notas_acorde']:
            fallos.append('%s · %s: acorde de %d notas (máximo %d en el nivel %d)'
                          % (modulo, donde, len(ps), nivel['max_notas_acorde'], n))
        for r in RECURSOS:
            if e.get(r) and r not in nivel['recursos']:
                fallos.append('%s · %s: recurso %r fuera del nivel %d'
                              % (modulo, donde, r, n))
        if e.get('number') is not None:
            fallos.append('%s · %s: lleva digitación impresa, y el cliente pidió '
                          'que los dedos los escriba el alumno' % (modulo, donde))

    tope = nivel.get('max_corcheas_seguidas', 99)
    for donde, ev in _sistemas(cfg):
        r = _racha_corta(ev)
        if r > tope and modulo not in RACHAS_JUSTIFICADAS:
            fallos.append('%s · %s: %d notas cortas seguidas (el nivel %d admite %d)'
                          % (modulo, donde, r, n, tope))
    return fallos


def main(prefijos=None):
    prefijos = prefijos or PREFIJOS
    modulos = []
    for p in prefijos:
        modulos += [os.path.basename(f)[:-3]
                    for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py')))]
    total = 0
    por_alumno = {}
    for m in modulos:
        f = revisar(m)
        total += len(f)
        por_alumno.setdefault(m.split('_')[0], []).extend(f)
    for pref in prefijos:
        fs = por_alumno.get(pref, [])
        n = NIVELES[ESCALON.get(pref, 1)]['nombre'] if pref in ESCALON else ''
        print('  %-7s %s' % (pref, 'ok' if not fs else '%d FALLOS' % len(fs)))
        for x in fs[:12]:
            print('      %s' % x)
        if len(fs) > 12:
            print('      ... y %d más' % (len(fs) - 12))
    print('\n%s' % ('NIVELES OK' if not total else '%d INCUMPLIMIENTOS DE NIVEL' % total))
    return total


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:] or None) else 0)
