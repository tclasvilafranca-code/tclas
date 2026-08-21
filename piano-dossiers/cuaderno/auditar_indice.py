# -*- coding: utf-8 -*-
"""Comprueba que el INDICE del album dice de cada pieza lo mismo que la pieza.

   Cada `build_<alumno>.py` lleva su tabla ETAPAS, y ahi va escrito a mano el
   titulo, la tonalidad y el compas de las 197 piezas. Son 197 pares de datos
   duplicados que hasta ahora no comprobaba nadie: si a una pieza se le corrige
   el compas —como acaba de pasar con tres— y no se toca el indice, el alumno
   abre el cuaderno por la primera pagina y lee un compas y por la quinta lee
   otro. Y el que se cree es el del indice, porque es el que parece oficial.

   La regla: el indice no es un texto, es una VISTA de los datos de la pieza.
   Si no coinciden, manda la pieza (que es la que se ha medido contra el papel)
   y se corrige el indice.

   Uso:  python3 auditar_indice.py            (todos)
         python3 auditar_indice.py arnau      (solo ese alumno)
"""
import contextlib
import re
import importlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

# alumno (como se llama su build_) -> prefijo de sus modulos de pieza
ALUMNOS = [('arnau', 'arnau'), ('luisa', 'lu'), ('josemaria', 'jm'),
           ('eduard', 'ed'), ('merce', 'me'), ('isaac', 'is'),
           ('josep', 'jp'), ('nel', 'nl'), ('dilan', 'dilan'), ('eva', 'eva')]

# Como se escribe en el indice cada tonalidad. `None` en la pieza significa
# "detras de la clave no hay nada", y eso en el indice puede decirse de las dos
# maneras que son ciertas: Do mayor o su relativo, La menor.
# Detras de la clave no hay nada: `key_sig=None`. En el indice eso puede
# decirse de las tres maneras que son ciertas. "Sin armadura" es la que se usa
# cuando la pieza es de modo menor y no se ha MEDIDO cual: escribir "La menor"
# sin haberlo comprobado seria saltarse la norma del proyecto por una casilla.
SIN_ARMADURA = {'Do mayor', 'La menor', 'Sin armadura'}

# Maneras de escribir la MISMA tonalidad. No es tolerancia gratuita: el indice
# de Arnau usa a proposito la forma corta ("Do", "Fa") porque lo lee un nino de
# diez anos, y el de los adultos usa el bemol tipografico. Lo que no vale es que
# el nombre diga OTRA tonalidad, y eso es lo que se comprueba.
# Como se puede escribir cada compas. Las dos grafias de la C valen, y la ficha
# a veces explica el signo ("C (4/4)", "Partido (¢)") o avisa de un cambio a
# mitad ("4/4 y 5/4"): basta con que UNA de sus palabras sea la buena.
COMPAS = {
    (4, 4): {'4/4', 'C'},
    (2, 2): {'2/2', '¢', 'Partido'},
    (3, 4): {'3/4'}, (2, 4): {'2/4'}, (6, 8): {'6/8'},
    (3, 8): {'3/8'}, (9, 8): {'9/8'}, (12, 8): {'12/8'}, (5, 4): {'5/4'},
}

NOTAS = {'do': 'Do', 'sol': 'Sol', 're': 'Re', 'la': 'La', 'mi': 'Mi',
         'fa': 'Fa', 'si': 'Si', 'sib': 'Sib', 'si♭': 'Sib', 'si bemol': 'Sib',
         'mib': 'Mib', 'mi♭': 'Mib', 'mi bemol': 'Mib'}
MODOS = {'': 'mayor', 'mayor': 'mayor', 'menor': 'menor'}


def _canon(texto):
    """Reduce a una sola forma las varias maneras de escribir una tonalidad.

       No es tolerancia gratuita: el indice de Arnau usa a proposito la forma
       corta ("Do", "Fa") porque lo lee un nino de diez anos, la ficha de los
       adultos escribe "Si bemol mayor" y hay quien pone el bemol tipografico.
       Lo que no vale es que el nombre diga OTRA tonalidad, y eso es lo que se
       comprueba.

       OJO con la abreviatura M/m: "Sol M" es Sol mayor y "Sol m" es Sol menor.
       Es el unico sitio del proyecto donde una mayuscula cambia el dato, asi
       que se mira ANTES de bajar el texto a minusculas."""
    t = texto.strip()
    if not t:
        return t
    m = re.match(r'^(.*?)\s*([Mm])$', t)
    if m and m.group(1).strip().lower() in NOTAS:
        return '%s %s' % (NOTAS[m.group(1).strip().lower()],
                          'mayor' if m.group(2) == 'M' else 'menor')
    bajo = t.lower()
    for nota in sorted(NOTAS, key=len, reverse=True):
        if bajo == nota or bajo.startswith(nota + ' '):
            resto = bajo[len(nota):].strip()
            if resto in MODOS:
                return '%s %s' % (NOTAS[nota], MODOS[resto])
    return t


# Separadores con los que el indice y la ficha anuncian un cambio o dan la
# pareja relativa. La BARRA solo vale para la tonalidad ("Sol M / Mi m"): en el
# compas la barra es parte del dato y partir por ahi convertia 4/4 en 4.
CAMBIO = ('\u2192', '->', '·')
CAMBIO_TONO = CAMBIO + ('/', ',')


def _primero(texto, seps=CAMBIO):
    """La primera parte de un dato que anuncia un cambio: "Do mayor -> Re mayor"
       o "4/4 · 5/4"."""
    for sep in seps:
        if sep in texto:
            return texto.split(sep)[0].strip()
    return texto.strip()


def _mod(nombre):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return importlib.import_module(nombre)


def piezas_del_indice(alumno):
    """[(num, dict del indice)] tal y como los escribe build_<alumno>.py."""
    mod = _mod('build_%s' % alumno)
    etapas = getattr(mod, 'ETAPAS', None)
    if etapas is None:
        return []
    out = []
    for _titulo, _sub, piezas in etapas:
        for p in piezas:
            out.append((p.get('num'), p))
    return out


def piezas_del_alumno(pref):
    """{num: CANCION} leyendo los modulos de pieza."""
    import glob
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, pref + '_[0-9]*.py'))):
        m = os.path.basename(f)[:-3]
        cfg = getattr(_mod(m), 'CANCION', None)
        if cfg:
            out[cfg.get('num')] = (m, cfg)
    return out


def _revisar_ficha(modulo, cfg):
    """La ficha de la pieza repite tonalidad y compas en su fila de datos."""
    fallos = []
    datos = dict((k, v) for k, v in (cfg.get('ficha') or {}).get('datos', []) or [])
    ks, ts = cfg.get('key_sig'), tuple(cfg.get('time_sig') or ())
    dt = datos.get('Tonalidad')
    if dt:
        d = _canon(_primero(dt, CAMBIO_TONO))
        if ks is None and d not in SIN_ARMADURA:
            fallos.append('%s · la FICHA dice tonalidad %r y la pieza no tiene armadura'
                          % (modulo, dt))
        elif ks is not None and d != ks:
            fallos.append('%s · la FICHA dice tonalidad %r y la pieza declara %r'
                          % (modulo, dt, ks))
    dc = datos.get('Compás')
    if dc:
        # "C (4/4)", "Partido (¢)", "4/4 y 5/4": la ficha explica la grafia o
        # avisa del cambio, y basta con que UNA de sus palabras sea la buena.
        validos = COMPAS.get(ts, set())
        trozos = set(re.split(r'[\s()·,]+', dc)) | {_primero(dc).strip()}
        trozos |= {t.strip() for t in re.split(r'[()·,]', dc)}
        if not (trozos & validos):
            fallos.append('%s · la FICHA dice compás %r y la pieza va en %d/%d'
                          % (modulo, dc, ts[0], ts[1]))
    return fallos


def revisar(alumno, pref):
    fallos = []
    indice = piezas_del_indice(alumno)
    piezas = piezas_del_alumno(pref)
    if not indice:
        return ['%s: build_%s.py no tiene ETAPAS' % (alumno, alumno)]

    vistos = set()
    for num, p in indice:
        vistos.add(num)
        if num not in piezas:
            fallos.append('%s · %s: el índice trae la pieza %s y no existe el módulo'
                          % (alumno, p.get('titulo', '?'), num))
            continue
        modulo, cfg = piezas[num]

        ts = tuple(cfg.get('time_sig') or ())
        dice = _primero(p.get('compas') or '')
        validos = COMPAS.get(ts)
        if validos is None:
            fallos.append('%s · %s: compás %s sin grafía conocida en auditar_indice.COMPAS'
                          % (modulo, p.get('titulo', '?'), ts))
        elif dice not in validos:
            fallos.append('%s · el índice dice compás %r y la pieza va en %d/%d'
                          % (modulo, dice, ts[0], ts[1]))

        ks = cfg.get('key_sig')
        dice_t = _canon(_primero(p.get('tonalidad') or '', CAMBIO_TONO))
        if ks is None:
            if dice_t not in SIN_ARMADURA:
                fallos.append('%s · el índice dice tonalidad %r y la pieza no tiene armadura'
                              % (modulo, dice_t))
        elif dice_t != ks:
            fallos.append('%s · el índice dice tonalidad %r y la pieza declara %r'
                          % (modulo, dice_t, ks))

        # Y la FICHA, que es la pagina que el alumno lee de verdad: el indice se
        # mira una vez y la ficha esta delante cada semana. Es la tercera copia
        # del mismo dato y tambien tiene que decir lo mismo.
        fallos += _revisar_ficha(modulo, cfg)

    for num, (modulo, _cfg) in sorted(piezas.items()):
        if num not in vistos:
            fallos.append('%s · la pieza existe y NO está en el índice de build_%s.py'
                          % (modulo, alumno))
    return fallos


def main(quiero=None):
    total = 0
    for alumno, pref in ALUMNOS:
        if quiero and alumno not in quiero and pref not in quiero:
            continue
        if not os.path.exists(os.path.join(HERE, 'build_%s.py' % alumno)):
            continue
        fallos = revisar(alumno, pref)
        total += len(fallos)
        print('  %-11s %s' % (alumno, 'ok' if not fallos else '%d FALLOS' % len(fallos)))
        for f in fallos[:14]:
            print('      %s' % f)
    if total:
        print('\n%d DESACUERDOS ENTRE EL ÍNDICE Y LAS PIEZAS' % total)
        return 1
    print('\nÍNDICES OK — el índice dice de cada pieza lo mismo que la pieza.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
