# -*- coding: utf-8 -*-
"""Auditor de VARIEDAD entre semanas.

   Norma del proyecto (decisión del cliente, vale para todos los alumnos): un
   cuaderno bien medido y bien impreso sigue siendo malo si cada semana el
   alumno se encuentra los mismos ejercicios en el mismo orden, porque deja de
   hacerlos. Lo que se comprueba aquí:

     1. dos semanas seguidas no llevan el mismo esqueleto de ejercicios;
     2. cada hoja trae al menos DOS tipos que no estaban en la hoja anterior;
     3. ningún esqueleto se repite más de `max_repes` veces en el álbum, y
        nunca a menos de `distancia` semanas de distancia;
     4. ningún tipo de ejercicio sale en más del `tope` de las hojas;
     5. se usan al menos `min_tipos` tipos distintos en el álbum.

   El origen: el primer álbum de Arnau tenía 40 hojas de deberes con 8 tipos,
   la semana 1 empezaba siempre por "escribe los nombres" y la semana 2 siempre
   por "rodea los compases iguales".
"""

# Estos dos no son ejercicios, son marcadores de hábito: que salgan todas las
# semanas es justo lo que se quiere, así que no cuentan para el tope de
# frecuencia. `rutina` es la tabla de "qué tocar cada día" del formato corto y
# `plan` es el plan de minutos por día del formato de adulto: es lo que el
# alumno se lleva de la clase para practicar en casa, y es la parte más útil
# de la hoja. Todo lo demás sí cuenta.
ESTRUCTURALES = {'rutina', 'plan'}


def revisar_variedad(hojas, etiqueta, max_repes=2, distancia=6, tope=0.60,
                     min_tipos=12, min_nuevos=2, verbose=True):
    """`hojas` es [(nombre, [tipos de bloque]), ...] EN EL ORDEN DEL ÁLBUM.
       Devuelve la lista de fallos (vacía si todo bien)."""
    fallos = []
    esqueletos = [tuple(t for t in tipos) for _, tipos in hojas]
    nombres = [n for n, _ in hojas]
    n = len(hojas)

    # 1 y 2: contra la hoja anterior
    for i in range(1, n):
        if esqueletos[i] == esqueletos[i - 1]:
            fallos.append('%s: %s repite el esqueleto de %s'
                          % (etiqueta, nombres[i], nombres[i - 1]))
        nuevos = set(esqueletos[i]) - set(esqueletos[i - 1])
        if len(nuevos) < min_nuevos:
            fallos.append('%s: %s solo trae %d tipo(s) nuevo(s) respecto a %s'
                          % (etiqueta, nombres[i], len(nuevos), nombres[i - 1]))

    # 3: repeticiones del mismo esqueleto en todo el álbum
    donde = {}
    for i, esq in enumerate(esqueletos):
        donde.setdefault(esq, []).append(i)
    for esq, idx in donde.items():
        if len(idx) > max_repes:
            fallos.append('%s: el esqueleto %s sale %d veces (%s)'
                          % (etiqueta, ' > '.join(esq), len(idx),
                             ', '.join(nombres[i] for i in idx)))
        for a, b in zip(idx, idx[1:]):
            if b - a < distancia:
                fallos.append('%s: %s y %s llevan el mismo esqueleto y solo hay '
                              '%d hoja(s) entre ellas'
                              % (etiqueta, nombres[a], nombres[b], b - a))

    # 4: frecuencia de cada tipo
    veces = {}
    for esq in esqueletos:
        for t in set(esq):
            veces[t] = veces.get(t, 0) + 1
    for t, v in sorted(veces.items()):
        if t in ESTRUCTURALES:
            continue
        if v > tope * n:
            fallos.append('%s: el tipo "%s" sale en %d de %d hojas (%.0f%%, el '
                          'tope es %.0f%%)' % (etiqueta, t, v, n, 100.0 * v / n,
                                               100 * tope))

    # 5: anchura del repertorio
    if len(veces) < min_tipos:
        fallos.append('%s: solo se usan %d tipos distintos (el mínimo es %d)'
                      % (etiqueta, len(veces), min_tipos))

    if verbose:
        print('  variedad · %d hojas · %d esqueletos distintos · %d tipos'
              % (n, len(donde), len(veces)))
        if not fallos:
            top = sorted(veces.items(), key=lambda kv: -kv[1])[:4]
            print('      los más usados: %s'
                  % ' · '.join('%s %d%%' % (t, round(100.0 * v / n)) for t, v in top))
        for f in fallos:
            print('      %s' % f)
    return fallos


def hojas_de_deberes(modulos):
    """Saca la lista (nombre, tipos) de las hojas de deberes de una lista de
       módulos de canción, en el orden del álbum."""
    hojas = []
    for mod in modulos:
        cfg = __import__(mod).CANCION
        for i, d in enumerate(cfg.get('deberes') or [], 1):
            hojas.append(('%02d s%d' % (cfg['num'], i),
                          [b['tipo'] for b in d['bloques']]))
    return hojas
