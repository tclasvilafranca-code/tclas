# -*- coding: utf-8 -*-
"""Los bloques que van en TODOS los cuadernos, sea cual sea el formato.

   Norma del cliente (agosto de 2026): *"necesito una igualdad entre álbumes;
   lo único que debe cambiar es el nivel"*. Estos cuatro nacieron en el cuaderno
   de Josep y se quedaron allí una semana; en cuanto se comparó un álbum con
   otro (`comparar_albumes.py`) quedó claro que no eran de Josep, eran del
   proyecto. Viven aquí para que ningún alumno se los pierda por el sitio donde
   estén escritos.

   Lo que sí cambia entre alumnos es **cómo se redactan**, y eso lo pone cada
   archivo de canción: el `reto` de un niño de diez años no se escribe como el
   de un adulto que lleva años en clase.
"""

__all__ = ['reto', 'cifrado', 'escalera', 'a_cuatro_manos']


def reto(texto, como, **kw):
    """El reto de la semana: qué se interpone, y con qué se quita de en medio.

       El reto sin el "cómo" es una queja, así que los dos campos son
       obligatorios. En un alumno al que no se le quiere nombrar el obstáculo
       —José María, que empezó hace poco— se usa `objetivo` en su lugar, que
       dice qué conseguir en vez de qué estorba; para la norma de igualdad los
       dos cuentan como lo mismo."""
    return dict(tipo='reto', reto=texto, como=como,
                etiqueta=kw.get('etiqueta', 'EL RETO DE ESTA SEMANA'),
                etiqueta_como=kw.get('etiqueta_como', 'CÓMO SE GANA'))


def cifrado(acordes, preguntas, **kw):
    """Las letras de acorde IMPRESAS en su partitura, y qué notas son.

       Solo se usa donde la edición las trae. En las demás no se inventa un
       cifrado que el alumno no va a ver en su papel: cada álbum tiene su lista
       comprobada (`CON_CIFRADO` en el módulo de recetas del alumno)."""
    return dict(tipo='cifrado', acordes=list(acordes), preguntas=list(preguntas),
                titulo=kw.get('titulo', 'Los acordes que pone tu partitura'),
                pista=kw.get('pista', 'escribe las tres notas de cada uno, de grave a agudo'),
                filas=kw.get('filas', 3), alto_caja=kw.get('alto_caja', 14.0))


def escalera(*escalones, **kw):
    """El metrónomo por escalones: pares (número, qué se consigue ahí).

       La `meta` tiene que decir SIEMPRE de dónde sale el número: o es el tempo
       impreso en la partitura ("♩ = 124, que es lo que pone tu partitura"), o
       se dice en la propia hoja que la partitura no trae tempo escrito. Un
       número de metrónomo inventado y presentado como si viniera de la edición
       sería exactamente el fallo que este proyecto no comete."""
    return dict(tipo='escalera', escalones=list(escalones),
                meta=kw.get('meta'), notas=list(kw.get('notas', [])),
                titulo=kw.get('titulo', 'La escalera del metrónomo'),
                pista=kw.get('pista', 'no subas un escalón hasta tocarlo dos veces sin fallo'))


def a_cuatro_manos(texto, pista='lo que hay que acordar ANTES de empezar a tocar'):
    """Para las piezas a cuatro manos: un dueto no se estudia solo.

       Usa el mismo dibujo que `escucha` pero con **tipo propio**, porque en
       estos cuadernos `escucha` es el recuadro de "para la próxima clase" y va
       en todas las hojas. Si compartieran tipo, la auditoría de variedad no
       podría contarlos por separado."""
    return dict(tipo='cuatro_manos', titulo='A CUATRO MANOS', pista=pista, texto=texto)
