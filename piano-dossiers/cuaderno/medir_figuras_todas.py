# -*- coding: utf-8 -*-
"""Mide las figuras de TODAS las partituras y deja el resultado en un archivo.

   Medir tarda (rasteriza 86 partituras a 200 dpi y recorre columna a columna),
   asi que no puede estar dentro de la auditoria de cada alumno. Esto se ejecuta
   a mano cuando cambia una partitura, y `auditar_figuras.py` lee lo guardado.

   Uso:  python3 medir_figuras_todas.py
   Deja: cuaderno/figuras_medidas.json  ·  cuaderno/FIGURAS_MEDIDAS.md
"""
import glob
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import medir_figuras as mf                                       # noqa: E402

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']
JSON = os.path.join(HERE, 'figuras_medidas.json')
MD = os.path.join(HERE, 'FIGURAS_MEDIDAS.md')


def _md5(p):
    try:
        with open(p, 'rb') as fh:
            return hashlib.md5(fh.read()).hexdigest()
    except Exception:                                            # noqa: BLE001
        return None


def escribe(cfg):
    """Cuantas semicorcheas dibuja el dosier, y cuantas de ellas son citas de
       la pieza (lo demas es material de apoyo, marcado `tecnica`)."""
    total = mano = 0
    grupos = []
    for k in ('piano1', 'piano2'):
        for b in (cfg.get(k) or {}).get('bloques', []) or []:
            grupos += b.get('sistemas', []) or []
    for r in (cfg.get('ficha') or {}).get('ritmos', []) or []:
        grupos.append({'events': r[2] if len(r) > 2 else []})
    for e in (cfg.get('calentamiento') or {}).get('ejercicios', []) or []:
        grupos.append(e)
    for s in grupos:
        for e in s.get('events') or []:
            if isinstance(e, dict) and (e.get('dur') or '').startswith('s'):
                total += 1
                if not e.get('tecnica'):
                    mano += 1
    return total, mano


def main():
    modulos = []
    for p in PREFIJOS:
        modulos += [os.path.basename(f)[:-3]
                    for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py')))]
    medido, datos = {}, {}
    for m in modulos:
        cfg = getattr(__import__(m), 'CANCION', None)
        if not cfg:
            continue
        ruta = cfg.get('partitura') or ''
        h = _md5(ruta)
        if h is None:
            datos[m] = dict(estado='sin archivo', partitura=os.path.basename(ruta))
            continue
        if h not in medido:
            try:
                largas, cortas = mf.contar(ruta)
                medido[h] = dict(estado='ok', largas=largas, cortas=cortas)
            except mf.NoMedible as exc:
                medido[h] = dict(estado='no medible', motivo=str(exc))
            except Exception as exc:                             # noqa: BLE001
                medido[h] = dict(estado='error', motivo=str(exc)[:60])
        total, mano = escribe(cfg)
        datos[m] = dict(medido[h])
        datos[m].update(partitura=os.path.basename(ruta), md5=h,
                        escribe=total, escribe_a_mano=mano)
        print('%-22s %-11s %s' % (m, datos[m]['estado'], datos[m].get('largas', '')),
              flush=True)

    with open(JSON, 'w') as fh:
        json.dump(datos, fh, indent=1, sort_keys=True)

    ok = [d for d in datos.values() if d.get('estado') == 'ok']
    nom = sorted({d['partitura'] for d in datos.values() if d.get('estado') == 'no medible'})
    with open(MD, 'w') as fh:
        fh.write("""# La figura impresa en cada partitura — medida sobre el PDF

Generado por `cuaderno/medir_figuras_todas.py`. Los datos vivos están en
`cuaderno/figuras_medidas.json`, que es lo que lee `auditar_figuras.py`.

**barras dobles** = pares de barras paralelas (semicorcheas) encontrados en el
PDF. **rabitos** = tramos cortos, ruidosos, que no deciden nada.

Esto es lo que faltaba: las transcripciones anotaban edición, tonalidad,
compás, tempo y páginas, pero nunca la figura más corta.

## Lo que este documento NO puede decir

**%d partituras salen como NO MEDIBLE.** No son PDF vectoriales: llevan dentro
una foto, a veces de 50 o 60 ppi, y a esa resolución las dos barras de una
semicorchea no se pueden separar. Hay que mirarlas a ojo.

Costó un error que conviene tener escrito: la primera versión daba **321
semicorcheas en el Flying Theme**, que va entero en corcheas.

## Las partituras que hay que mirar a ojo

%s

## La tabla

| pieza | estado | barras dobles | rabitos | escribe | de ellas citadas | partitura |
|---|---|---|---|---|---|---|
""" % (len(nom), '\n'.join('- %s' % p for p in nom)))
        for m in sorted(datos):
            d = datos[m]
            fh.write('| %s | %s | %s | %s | %s | %s | %s |\n'
                     % (m, d.get('estado'), d.get('largas', '—'), d.get('cortas', '—'),
                        d.get('escribe', '—'), d.get('escribe_a_mano', '—'),
                        d.get('partitura', '')))
    print('\n%d piezas · %d medibles · %d partituras no medibles'
          % (len(datos), len(ok), len(nom)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
