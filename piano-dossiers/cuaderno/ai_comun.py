# -*- coding: utf-8 -*-
"""Piezas sueltas de las hojas de Aida (formato de adulto, version exigente).

   Aida tiene unos cuarenta anos y **ya habia tocado piano**: el nivel es el de
   Josep, no el de un principiante. Lo que pidio el cliente, literal, es que
   "vaya asentando bases antes de correr", y eso NO se resuelve bajandole el
   liston: se resuelve con el ORDEN del album y con que hoja se le da cada
   semana. El liston es el mismo que el de Josep (escalon 4, hasta la
   semicorchea); lo que cambia es que las cuatro primeras piezas trabajan la
   mano quieta y el arpegio, y las cuatro ultimas son las que corren.

   Se importa lo mismo que Josep, y por los mismos motivos:

     - `reto`      la dificultad concreta de la semana, dicha por su nombre, y
                   con que se gana. Aida tiene nivel para que se le nombre el
                   obstaculo en vez de esquivarlo.
     - `cifrado`   las letras de acorde que SU partitura lleva impresas. Solo
                   en las piezas que las traen de verdad.
     - `escalera`  el metronomo por escalones, con el tempo impreso como meta
                   cuando la edicion lo trae (cuatro de las suyas lo traen).
     - `a_cuatro_manos`  tres de sus diecinueve piezas son duetos (los dos
                   Diabelli y el It's Beginning to Look a Lot Like Christmas),
                   y un dueto no se estudia igual que una pieza solo. La otra
                   parte la toca la profesora en clase: es lo que decidio el
                   cliente, y por eso el bloque habla de que hay que acordar
                   con ella, no con otra alumna.
"""
from jp_comun import (n, ac, sil, corch, semi, acuerdate, escribir,
                      nombres, dibujar, figuras, unir, rodear, colorear,
                      verdadero_falso, ordenar, diferencias, contar,
                      teclado, inventa, plan, metronomo, objetivo, para_clase,
                      reto, cifrado, escalera, a_cuatro_manos)

__all__ = ['n', 'ac', 'sil', 'corch', 'semi', 'acuerdate', 'escribir',
           'nombres', 'dibujar', 'figuras', 'unir', 'rodear', 'colorear',
           'verdadero_falso', 'ordenar', 'diferencias', 'contar', 'teclado',
           'inventa', 'plan', 'metronomo', 'objetivo', 'para_clase',
           'reto', 'cifrado', 'escalera', 'a_cuatro_manos']
