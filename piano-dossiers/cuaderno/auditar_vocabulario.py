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
# VACIA, y que siga asi. Durante meses hubo aqui DIECISIETE piezas cuyo texto
# explicaba un tresillo o una semicorchea —algunas con su recuadro de "que es un
# tresillo" y todo— y no dibujaban ni uno, con el motivo anotado: "la hoja esta
# llena y meterlo obligaria a borrar material medido".
#
# Era cierto entonces y dejo de serlo cuando la hoja de "Como se estudia" paso a
# paginarse sola. Se comprobo una por una: las seis de Josep y Nel, las nueve de
# Dilan y las cuatro de Eva llevan ya su bloque de tresillos o de semicorcheas,
# con el material de apoyo que hace falta para que la hoja nueva no salga a
# medias. Ninguna perdio un compas medido.
#
# Si alguna vez vuelve a aparecer un caso, la pregunta correcta NO es "¿cabe?"
# sino "¿por que no cabe?": la hoja se parte, y si aun asi no cabe es que a esa
# pieza le falta material, no que le sobre el recurso.
LLENAS = set()

REQUISITO = {
    'semicorchea': ('figuras', 's'),
    # Pide la SEMICORCHEA, no la corchea con puntillo: el ritmo largo-corto
    # es 'e.' + 's', y sin la segunda la primera no se puede escribir (0.75
    # no llena un golpe). Por eso se ata a 's': los escalones 1 y 2, que aun
    # no la tienen, quedan perdonados —y en sus hojas el mismo gesto va
    # escrito al doble de lento, que es como se estudia y no se salta su
    # nivel. Atarlo a 'e.' marcaba como fallo justo lo que estaba bien.
    'puntillo_corto': ('figuras', 's'),
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
        # \b en 'matiz' porque "automatizado" lo contiene, y la negacion delante
        # de 'dinamica' porque hay piezas que dicen justo lo contrario: "no hay
        # dinamicas escritas". Los dos casos daban falsos positivos.
        patron=(r'(?<!no hay )(?<!sin ninguna )(?<!sin )(?<!ni una )din[áa]mica'
                r'|\bmatiz\b|\bmatices\b|"p dolce"'
                r'|\bmp\b|\bmf\b|\bff\b|\bpp\b'),
        evento=lambda e: bool(e.get('matiz')),
        arreglo="matiz='p' / 'mf' / ... en la nota donde empieza"),
    'regulador': dict(
        patron=r'cresc|crescendo|diminuendo|dim\.|regulador|reguladores',
        evento=lambda e: bool(e.get('cresc') or e.get('dim')),
        arreglo="cresc=<n_eventos> o dim=<n_eventos>"),
    # La figura con puntillo CORTA (corchea o semicorchea). Faltaba, y por eso
    # nadie vio que VEINTE piezas la explicaban sin dibujarla: el ritmo de
    # Toreador, el de Rasputin, el del Do-Re-Mi. Es el mismo fallo que las
    # diecisiete del tresillo, solo que este auditor no lo miraba.
    # `REQUISITO` la ata a la figura 'e.', asi que a Arnau y a Luisa —escalon 1,
    # que no la tiene— el hueco se les perdona, que es lo correcto.
    'puntillo_corto': dict(
        patron=(r'corchea con puntillo|corcheas con puntillo|'
                r'negra con puntillo y corchea|puntillo y (?:una )?corchea|'
                r'ritmo con puntillo|semicorchea con puntillo'),
        evento=lambda e: e.get('dur') in ('e.', 's.'),
        arreglo="escribir el pasaje con dur='e.' seguido de dur='s'"),
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


# ---------------------------------------------------------------- digitacion
#
# Caso aparte, y por eso no vive en VOCABULARIO: aqui NO se trata de que falte
# algo por dibujar, sino justo al reves. El cliente decidio que los numeros de
# dedo NO se imprimen nunca (los escribe el alumno), asi que la ausencia es
# correcta y `auditar_niveles` ya falla si alguna nota lleva `number`.
#
# Lo que se colo fue lo otro: al quitar los numeros se cambiaron los cinco
# archivos que los dibujaban, pero no la PROSA del resto. Quedaron 31 piezas
# diciendo "la derecha corre en corcheas con los dedos impresos" o "sigue los
# dedos escritos" encima de un pentagrama sin un solo numero. El alumno que
# estudia solo en casa busca algo que no esta y da por hecho que la hoja salio
# mal impresa; es el mismo fallo que persigue el resto de este auditor —el
# texto cuenta una cosa y el papel ensena otra— solo que al reves.
#
# La regla, entonces: se puede hablar de digitacion todo lo que haga falta,
# pero SIEMPRE diciendo de donde sale (tu partitura, tu edicion, el arreglista)
# o pidiendo al alumno que la escriba el. Lo que no vale es dejarlo colgando,
# porque en una hoja nuestra "los dedos escritos" solo puede leerse como "los
# de aqui".
DEDOS = re.compile(r'digitaci[óo]n|dedos escritos|dedos impresos|dedo escrito|'
                   r'dedo impreso|n[úu]meros? de dedo|dedos? (?:escrit|impres)')

# Basta con que la MISMA frase diga de donde salen los numeros. Se comprueba
# frase a frase y no en toda la pieza: que el docstring lo aclare no arregla un
# pie de foto que tres hojas despues dice "sigue los dedos escritos".
DEDOS_OK = re.compile(r'tu partitura|tu edici[óo]n|la edici[óo]n|esta edici[óo]n|'
                      r'la partitura|el arreglista|c[óo]pia|copia|escribe t[úu]|'
                      r'escribe encima|escribe el|ponles|hayas escrito')


def _frases_propias(cfg):
    """Los textos que describen NUESTRO andamio, no la partitura del alumno.

       La ficha ('especial', las tarjetas de armonia, el docstring) habla de la
       edicion del alumno y ahi decir "trae digitacion impresa" es un dato
       medido y correcto. Lo que se revisa aqui son los rotulos que van pegados
       a un pentagrama dibujado por nosotros."""
    out = []
    f = cfg.get('ficha') or {}
    for r in f.get('ritmos', []) or []:
        if len(r) > 1:
            out.append(('ficha.ritmos', str(r[1])))
    out.append(('ficha.pie_ritmos', str(f.get('pie_ritmos') or '')))
    for k in ('piano1', 'piano2'):
        p = cfg.get(k) or {}
        out.append((k + '.intro', str(p.get('intro') or '')))
        for x in p.get('reglas', []) or []:
            out.append((k + '.reglas', str(x)))
        for b in p.get('bloques', []) or []:
            for kk in ('titulo', 'pista', 'texto'):
                out.append(('%s.%s' % (k, kk), str(b.get(kk) or '')))
            for s in b.get('sistemas', []) or []:
                out.append((k + '.cap', str(s.get('cap') or '')))
    return out


def _revisar_dedos(modulo, cfg):
    malas = []
    for donde, txt in _frases_propias(cfg):
        t = txt.lower()
        if DEDOS.search(t) and not DEDOS_OK.search(t):
            malas.append((modulo, 'digitación',
                          'decir de dónde salen los dedos ("en tu partitura") o '
                          'pedir al alumno que los escriba · %s: %s'
                          % (donde, txt[:70])))
    return malas


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
        if (modulo, nombre) in LLENAS:
            continue     # explicado en el texto; no cabe dibujarlo sin quitar material medido
        if nivel is not None:
            campo, clave = REQUISITO.get(nombre, (None, None))
            if campo and clave not in nivel[campo]:
                continue     # su escalon no lo admite: el hueco es correcto
            # Y ademas: un escalon puede admitir la figura pero no TODAVIA. El
            # 3 tiene la semicorchea desde la pieza 6, asi que en la 3 el hueco
            # sigue siendo correcto y la hoja escribe el gesto al doble de lento.
            desde = (nivel.get('desde') or {}).get(clave)
            if desde and (cfg.get('num') or 0) < desde:
                continue
        huecos.append((modulo, nombre, spec['arreglo']))
    huecos += _revisar_dedos(modulo, cfg)
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
        # El arreglo viaja en cada hueco y no se saca de VOCABULARIO: 'digitación'
        # no vive alli (es la comprobacion inversa) y ademas su mensaje cita la
        # frase concreta que falla, que es lo unico util para arreglarla.
        por_recurso.setdefault(rec, []).append((mod, arr))
    print('\nSe habla de esto en el texto y NO se dibuja en el material:\n')
    for rec in sorted(por_recurso, key=lambda r: -len(por_recurso[r])):
        casos = por_recurso[rec]
        print('  %-12s %2d piezas  ·  %s' % (rec, len(casos), casos[0][1]))
        for m, arr in casos:
            print('        %s' % m if rec in VOCABULARIO else '        %s · %s' % (m, arr))
    print('\n%d HUECOS DE VOCABULARIO' % len(todos))
    return len(todos)


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:] or None) else 0)
