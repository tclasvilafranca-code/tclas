# -*- coding: utf-8 -*-
"""Piezas sueltas de las hojas de Josep (formato de adulto, versión exigente).

   Josep tiene la edad y el nivel de José María, pero **lleva más tiempo en
   clase**, le gustan los retos y las partituras que no son del todo fáciles.
   El formato es el mismo —seis hojas, con dedos y lectura separadas— y lo que
   cambia es el listón:

     - `reto`      la dificultad concreta de la semana, dicha por su nombre,
                   y con qué se gana. Es lo que en José María es `objetivo`,
                   pero nombrando el obstáculo en vez de esquivarlo.
     - `cifrado`   las letras de acorde que **su** partitura lleva impresas.
                   Solo en las siete piezas que las traen de verdad.
     - `escalera`  el metrónomo por escalones, con el tempo impreso como meta.
     - `a_cuatro_manos`  cuatro de sus diecinueve piezas son duetos, y eso no
                   se estudia igual que una pieza solo.

   Los ejercicios se numeran solos en `hoja_deberes.build_deberes`, así que
   aquí no se pone `num` en ningún sitio.
"""
from arnau_comun import (n, ac, sil, corch, acuerdate, escribir,
                         nombres, dibujar, figuras, unir, rodear, colorear,
                         verdadero_falso, ordenar, diferencias, contar,
                         teclado, inventa)
from jm_comun import plan, metronomo, objetivo, para_clase

__all__ = ['n', 'ac', 'sil', 'corch', 'acuerdate', 'escribir',
           'nombres', 'dibujar', 'figuras', 'unir', 'rodear', 'colorear',
           'verdadero_falso', 'ordenar', 'diferencias', 'contar', 'teclado',
           'inventa', 'plan', 'metronomo', 'objetivo', 'para_clase',
           'reto', 'cifrado', 'escalera', 'a_cuatro_manos']


def reto(texto, como, **kw):
    """El reto de la semana: qué se interpone, y con qué se quita de en medio.

       A un alumno al que le gustan los retos, nombrarle la dificultad le
       funciona mejor que envolvérsela. Pero el reto sin el "cómo" es una
       queja: los dos campos son obligatorios."""
    return dict(tipo='reto', reto=texto, como=como,
                etiqueta=kw.get('etiqueta', 'EL RETO DE ESTA SEMANA'),
                etiqueta_como=kw.get('etiqueta_como', 'CÓMO SE GANA'))


def cifrado(acordes, preguntas, **kw):
    """Las letras de acorde IMPRESAS en su partitura, y qué notas son.

       Solo se usa donde la edición las trae: A comme amour, Un beso y una
       flor, Can't Help Falling in Love, My Favourite Things, What Was I Made
       For, Rasputin y Deck the Halls. En las demás no se inventa un cifrado
       que el alumno no va a ver en su papel."""
    return dict(tipo='cifrado', acordes=list(acordes), preguntas=list(preguntas),
                titulo=kw.get('titulo', 'Los acordes que pone tu partitura'),
                pista=kw.get('pista', 'escribe las tres notas de cada uno, de grave a agudo'),
                filas=kw.get('filas', 3), alto_caja=kw.get('alto_caja', 14.0))


def escalera(*escalones, **kw):
    """El metrónomo por escalones: pares (número, qué se consigue ahí).

       La `meta` tiene que decir SIEMPRE de dónde sale el número: o es el tempo
       impreso en su partitura ("♩ = 124, que es lo que pone tu partitura"), o
       se dice en la propia hoja que la partitura no trae tempo escrito y que
       la meta es tocarla seguida. Un número de metrónomo inventado y
       presentado como si viniera de la edición sería exactamente el fallo que
       este proyecto no comete."""
    return dict(tipo='escalera', escalones=list(escalones),
                meta=kw.get('meta'), notas=list(kw.get('notas', [])),
                titulo=kw.get('titulo', 'La escalera del metrónomo'),
                pista=kw.get('pista', 'no subas un escalón hasta tocarlo dos veces sin fallo'))


def a_cuatro_manos(texto, pista='lo que hay que acordar ANTES de empezar a tocar'):
    """Cuatro de sus diecinueve piezas son duetos, y un dueto no se estudia
       solo: Romance de Diabelli, Petite Chanson, Bella Ciao e It's Beginning.

       Usa el mismo dibujo que `escucha` pero con **tipo propio**, porque en
       este cuaderno `escucha` es el recuadro de "para la próxima clase" y va
       en las 19 hojas. Si compartieran tipo, la auditoría de variedad no
       podría contarlos por separado."""
    return dict(tipo='cuatro_manos', titulo='A CUATRO MANOS', pista=pista, texto=texto)
