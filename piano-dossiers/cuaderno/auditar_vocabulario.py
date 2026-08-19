# -*- coding: utf-8 -*-
"""Compara lo que las hojas DICEN que hay en la partitura con lo que DIBUJAN.

   Aplica la norma del proyecto "lo que no sabes hacer, se aprende": si el texto
   de una pieza habla de semicorcheas, de ligaduras, de un staccato o de un
   cresc. y el material de esa pieza no escribe ninguno, el alumno lee una
   explicacion y luego mira un pentagrama que no se parece a su partitura.

   Durante meses la salida fue escribir "esto no lo puedo dibujar, asi que lo
   veras en corcheas". Este auditor existe para que eso no vuelva a pasar sin
   que nadie se entere.

   Uso:  python3 auditar_vocabulario.py            (todas)
         python3 auditar_vocabulario.py jp dilan   (solo esos prefijos)
"""
import sys
import os
import re
import glob
import io
import contextlib
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from niveles import NIVELES, escalon_de

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']

# Que hace falta tener en el escalon para poder dibujar cada recurso. Si el
# alumno no llega, el hueco NO es un fallo: es su nivel haciendo su trabajo.
# El texto de esas piezas ya explica que el pasaje se trabaja reducido, que es
# justo lo correcto para ellas (Luisa leyendo el Titanic, por ejemplo).
REQUISITO = {
    'semicorchea': ('figuras', 's'),
    'tresillo': ('recursos', 'tresillo'),
    'ligadura': ('recursos', 'lig'),
    'staccato': ('recursos', 'art'),
    'acento': ('recursos', 'art'),
    'calderon': ('recursos', 'art'),
    'matiz': ('recursos', 'matiz'),
    'regulador': ('recursos', 'cresc'),
    'pedal': ('recursos', 'pedal'),
}

# recurso -> (patron en el texto, como se detecta en los eventos)
#
# El patron busca la palabra tal y como la escriben las hojas. Se excluye a
# proposito el modo "aqui no se puede dibujar", que era justo la excusa.
VOCABULARIO = {
    'semicorchea': dict(
        patron=r'semicorchea|semicorcheas|cuatro notas (?:en |por )(?:el tiempo de |cada )?(?:un )?golpe',
        evento=lambda e: e.get('dur') in ('s', 's.'),
        arreglo="escribir el pasaje con dur='s' (helper `semi`)"),
    'tresillo': dict(
        patron=r'tresillo|tresillos|tres notas en el (?:sitio|hueco) de dos',
        evento=lambda e: bool(e.get('tresillo')),
        arreglo="marcar los eventos con tresillo=<id>"),
    'ligadura': dict(
        patron=r'ligadura|ligaduras|ligad[ao]s? (?:a|con|entre)|atan? (?:una|la) nota',
        evento=lambda e: bool(e.get('lig')),
        arreglo="marcar la primera nota de cada par con lig=True"),
    'staccato': dict(
        patron=r'staccato|picad[ao]s?',
        evento=lambda e: 'staccato' in _arts(e),
        arreglo="art='staccato' en las notas afectadas"),
    'acento': dict(
        patron=r'\bacento\b|\bacentos\b|acentuad[ao]',
        evento=lambda e: 'acento' in _arts(e),
        arreglo="art='acento'"),
    'calderon': dict(
        patron=r'calder[óo]n',
        evento=lambda e: 'calderon' in _arts(e),
        arreglo="art='calderon'"),
    'matiz': dict(
        patron=r'din[áa]mica|matiz|matices|"p dolce"|\bmp\b|\bmf\b|\bff\b|\bpp\b',
        evento=lambda e: bool(e.get('matiz')),
        arreglo="matiz='p' / 'mf' / ... en la nota donde empieza"),
    'regulador': dict(
        patron=r'cresc|crescendo|diminuendo|dim\.|regulador|reguladores',
        evento=lambda e: bool(e.get('cresc') or e.get('dim')),
        arreglo="cresc=<n_eventos> o dim=<n_eventos>"),
    'pedal': dict(
        patron=r'\bpedal\b',
        evento=lambda e: bool(e.get('pedal')),
        arreglo="pedal=<n_eventos>"),
}


def _arts(e):
    a = e.get('art')
    if not a:
        return ()
    return (a,) if isinstance(a, str) else tuple(a)


def _texto(cfg, mod):
    """Todo el texto en prosa de la pieza, incluido el docstring del modulo."""
    trozos = [mod.__doc__ or '']
    f = cfg.get('ficha') or {}
    for k in ('titulo_ritmos', 'pie_ritmos', 'reto', 'truco', 'sabias'):
        trozos.append(str(f.get(k) or ''))
    trozos += [str(x) for x in (f.get('especial') or [])]
    arm = f.get('armonia') or {}
    trozos.append(str(arm.get('pie') or ''))
    for t in (arm.get('tarjetas') or []):
        trozos += [str(x) for x in t]
    for k in ('piano1', 'piano2'):
        p = cfg.get(k) or {}
        trozos.append(str(p.get('intro') or ''))
        for b in p.get('bloques', []) or []:
            trozos += [str(b.get('titulo') or ''), str(b.get('pista') or ''),
                       str(b.get('texto') or ''), str(b.get('etiqueta') or '')]
            for s in b.get('sistemas', []) or []:
                trozos.append(str(s.get('cap') or ''))
    return ' \n'.join(trozos).lower()


def _eventos(cfg):
    """Los eventos tal y como se van a DIBUJAR.

       Un sistema puede declarar `matiz='p'` en vez de tocar su lista de notas
       (`hoja_piano` lo aplica a la primera nota al imprimir). Aqui se hace lo
       mismo, o el auditor daria por ausente una dinamica que si sale en papel."""
    out = []
    for k in ('piano1', 'piano2'):
        for b in (cfg.get(k) or {}).get('bloques', []) or []:
            for s in b.get('sistemas', []) or []:
                evs = [e for e in (s.get('events', []) or []) if isinstance(e, dict)]
                if s.get('matiz'):
                    evs = evs + [{'matiz': s['matiz']}]
                if s.get('ligar'):
                    evs = evs + [{'lig': True}]
                for _k, _v in (('staccato', {'art': 'staccato'}),
                               ('acento', {'art': 'acento'}),
                               ('calderon', {'art': 'calderon'}),
                               ('cresc', {'cresc': 1}), ('dim', {'dim': 1}),
                               ('pedal', {'pedal': 1})):
                    if s.get(_k):
                        evs = evs + [dict(_v)]
                out += evs
    for r in (cfg.get('ficha') or {}).get('ritmos', []) or []:
        if len(r) > 2 and isinstance(r[2], list):
            out += [e for e in r[2] if isinstance(e, dict)]
    return out


def revisar(modulo):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        mod = importlib.import_module(modulo)
    cfg = getattr(mod, 'CANCION', None)
    if cfg is None:
        return []
    txt = _texto(cfg, mod)
    evs = _eventos(cfg)
    n = escalon_de(cfg.get('alumno', ''))
    nivel = NIVELES.get(n) if n else None
    huecos = []
    for nombre, spec in VOCABULARIO.items():
        if not re.search(spec['patron'], txt):
            continue
        if any(spec['evento'](e) for e in evs):
            continue
        if nivel is not None:
            campo, clave = REQUISITO.get(nombre, (None, None))
            if campo and clave not in nivel[campo]:
                continue     # su escalon no lo admite: el hueco es correcto
        huecos.append((modulo, nombre, spec['arreglo']))
    return huecos


def main(prefijos=None):
    prefijos = prefijos or PREFIJOS
    modulos = []
    for p in prefijos:
        modulos += [os.path.basename(f)[:-3]
                    for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py')))]
    todos = []
    for m in modulos:
        todos += revisar(m)
    if not todos:
        print('\nTODO OK — no hay nada que se cuente en el texto y no se dibuje.')
        return 0
    por_recurso = {}
    for mod, rec, arr in todos:
        por_recurso.setdefault(rec, []).append(mod)
    print('\nSe habla de esto en el texto y NO se dibuja en el material:\n')
    for rec in sorted(por_recurso, key=lambda r: -len(por_recurso[r])):
        mods = por_recurso[rec]
        arr = VOCABULARIO[rec]['arreglo']
        print('  %-12s %2d piezas  ·  %s' % (rec, len(mods), arr))
        for m in mods:
            print('        %s' % m)
    print('\n%d HUECOS DE VOCABULARIO' % len(todos))
    return len(todos)


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:] or None) else 0)
