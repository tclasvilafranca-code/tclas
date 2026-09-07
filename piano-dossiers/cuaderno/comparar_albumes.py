# -*- coding: utf-8 -*-
"""Compara los cinco cuadernos y dice cuál se ha quedado atrás.

   NORMA DEL CLIENTE (agosto de 2026, con estas palabras): *"necesito una
   igualdad entre álbumes; lo único que debe cambiar es el nivel"*.

   El problema que resuelve este script es real y ya pasó dos veces: las
   mejoras se iban aplicando **hacia delante**, al alumno que estaba en la
   mesa, y los anteriores se quedaban con una versión vieja del cuaderno. Pasó
   con el recuadro "para la próxima clase" (Arnau lo tenía, Dilan y Eva no) y
   volvió a pasar con los cuatro bloques nuevos de Josep, que José María —mismo
   formato y nivel parecido— no tenía.

   Aquí se escribe el MÍNIMO COMÚN: lo que todo cuaderno tiene que traer, sea
   cual sea el formato. Lo que cambia entre alumnos es el nivel —el lenguaje,
   la dificultad de los ejercicios, cuántas hojas por pieza— y no qué clase de
   ayuda recibe cada uno.

   El mínimo común va en DOS NIVELES, y no por comodidad: exigirlo todo en
   todas las hojas chocaría de frente con la otra norma del cliente, la de
   variedad. Si cuatro bloques fueran fijos en cada hoja, solo quedarían dos
   huecos para rotar y las semanas volverían a parecerse entre sí.

   **Nivel 1 · el esqueleto, en el 100 % de las hojas.** Son lo que sostiene la
   semana, no ejercicios, y por eso repetirlos no cansa:

     plan          qué hacer cada día, con casillas
                   (`plan` en adulto, `rutina` en el formato corto)
     clase         con qué se vuelve el día de la clase (`escucha`)
     escritos      ejercicios escritos de verdad, con la variedad auditada

   **Nivel 2 · presentes en todos los álbumes y en al menos la mitad de las
   hojas.** Rotan, que es lo que pide la norma de variedad, pero ningún alumno
   puede quedarse sin ellos:

     reto          la dificultad de la semana y con qué se gana
                   (`reto`, o `objetivo` donde no se le quiere nombrar el
                   obstáculo al alumno: cuenta igual)
     velocidad     una meta de velocidad: `escalera` donde la partitura trae
                   tempo impreso, `metronomo` donde no

   **Nivel 3 · donde la partitura lo justifica, y solo ahí.** No se cuentan
   por porcentaje porque dependen de la edición, no del alumno:

     cifrado       donde la edición imprime las letras de acorde
     duetos        el bloque de a cuatro manos, en las piezas a cuatro manos
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

# Un rasgo se da por cubierto si la hoja lleva CUALQUIERA de estos bloques.
# `minimo` es la fraccion de hojas que tiene que traerlo: 1.0 para el esqueleto
# y 0.5 para los que rotan.
RASGOS = [
    ('plan',      {'plan', 'rutina'},        1.0, 'qué hacer cada día'),
    ('clase',     {'escucha'},               1.0, 'con qué se vuelve a clase'),
    ('escritos',  None,                      1.0, 'ejercicios escritos'),
    ('reto',      {'reto', 'objetivo'},      0.5, 'la dificultad de la semana'),
    ('velocidad', {'escalera', 'metronomo'}, 0.5, 'una meta de velocidad'),
]

# Los bloques que NO son ejercicio escrito: sirven de esqueleto, no cuentan
# para saber si la hoja trae trabajo de papel.
NO_EJERCICIO = {'plan', 'rutina', 'reto', 'objetivo', 'escalera', 'metronomo',
                'escucha', 'cuatro_manos', 'nota'}

ALBUMES = [
    ('Arnau',      'arnau_[0-9]*.py'),
    ('Dilan',      'dilan_[0-9]*_*.py'),
    ('Eva',        'eva_[0-9]*.py'),
    ('José María', 'jm_[0-9]*.py'),
    ('Josep',      'jp_[0-9]*.py'),
]


def _modulos(patron):
    fs = sorted(glob.glob(os.path.join(HERE, patron)))
    return [os.path.basename(f)[:-3] for f in fs
            if not f.endswith('_data.py') and not f.endswith('_comun.py')]


def hojas_de(mod):
    """Las hojas de trabajo/deberes de una pieza, como listas de tipos."""
    cfg = __import__(mod).CANCION
    out = []
    for clave in ('deberes', 'trabajo'):
        for h in cfg.get(clave) or []:
            out.append([b['tipo'] for b in h['bloques']])
    return cfg, out


def revisar(verbose=True):
    filas, fallos = [], []
    for alumno, patron in ALBUMES:
        mods = _modulos(patron)
        piezas, hojas = 0, []
        for m in mods:
            try:
                cfg, hs = hojas_de(m)
            except Exception as e:                       # pragma: no cover
                fallos.append('%s: no se puede leer %s (%s)' % (alumno, m, e))
                continue
            piezas += 1
            hojas.extend(hs)
        fila = {'alumno': alumno, 'piezas': piezas, 'hojas': len(hojas)}
        if not hojas:
            fila['sin_hoja'] = True
            fallos.append('%s: %d piezas y NINGUNA hoja de trabajo escrita. '
                          'El resto de los cuadernos llevan una por pieza.'
                          % (alumno, piezas))
            filas.append(fila)
            continue
        for nombre, bloques, minimo, _ in RASGOS:
            if bloques is None:
                cubre = sum(1 for h in hojas
                            if any(t not in NO_EJERCICIO for t in h))
            else:
                cubre = sum(1 for h in hojas if bloques & set(h))
            fila[nombre] = cubre
            hace_falta = len(hojas) if minimo >= 1.0 else int(len(hojas) * minimo + 0.999)
            if cubre < hace_falta:
                fallos.append('%s: "%s" está en %d de sus %d hojas y hacen falta %d'
                              % (alumno, nombre, cubre, len(hojas), hace_falta))
        filas.append(fila)

    if verbose:
        cab = ('alumno', 'piezas', 'hojas', 'plan', 'clase', 'escritos',
               'reto', 'velocidad')
        print('%-11s %6s %5s %7s %7s %8s %7s %9s' % cab)
        print('%-11s %6s %5s %7s %7s %8s %7s %9s'
              % ('', '', '', 'todas', 'todas', 'todas', 'mitad', 'mitad'))
        print('-' * 66)
        for f in filas:
            if f.get('sin_hoja'):
                print('%-11s %6d %5d %s' % (f['alumno'], f['piezas'], 0,
                                            '  — sin hoja de trabajo escrita —'))
                continue
            print('%-11s %6d %5d %7s %7s %8s %7s %9s'
                  % (f['alumno'], f['piezas'], f['hojas'],
                     '%d/%d' % (f['plan'], f['hojas']),
                     '%d/%d' % (f['clase'], f['hojas']),
                     '%d/%d' % (f['escritos'], f['hojas']),
                     '%d/%d' % (f['reto'], f['hojas']),
                     '%d/%d' % (f['velocidad'], f['hojas'])))
        print()
        if fallos:
            print('%d desigualdades entre cuadernos:' % len(fallos))
            for f in fallos:
                print('   · %s' % f)
        else:
            print('IGUALDAD OK · los cinco cuadernos traen el mismo mínimo común')
    return fallos


if __name__ == '__main__':
    sys.exit(1 if revisar() else 0)
