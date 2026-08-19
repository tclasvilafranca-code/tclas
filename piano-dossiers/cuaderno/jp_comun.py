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
from bloques_comun import reto, cifrado, escalera, a_cuatro_manos

__all__ = ['n', 'ac', 'sil', 'corch', 'semi', 'acuerdate', 'escribir',
           'nombres', 'dibujar', 'figuras', 'unir', 'rodear', 'colorear',
           'verdadero_falso', 'ordenar', 'diferencias', 'contar', 'teclado',
           'inventa', 'plan', 'metronomo', 'objetivo', 'para_clase',
           'reto', 'cifrado', 'escalera', 'a_cuatro_manos']


