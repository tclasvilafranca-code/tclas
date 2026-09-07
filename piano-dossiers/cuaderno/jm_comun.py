# -*- coding: utf-8 -*-
"""Piezas sueltas de las hojas de José María (formato de adulto).

   Reutiliza las fábricas de bloques que ya existen y añade las tres que solo
   tienen sentido para lo que pasa ENTRE una clase y la siguiente: el plan de
   minutos por día, la tabla de metrónomo y el objetivo de la semana.

   Los ejercicios se numeran solos en `hoja_deberes.build_deberes`, así que
   aquí no se pone `num` en ningún sitio.
"""
from bloques_comun import reto, cifrado, escalera, a_cuatro_manos
from arnau_comun import (n, ac, sil, corch, semi, acuerdate, escribir,
                         nombres, dibujar, figuras, unir, rodear, colorear,
                         verdadero_falso, ordenar, diferencias, contar,
                         teclado, inventa)

__all__ = ['n', 'ac', 'sil', 'corch', 'semi', 'acuerdate', 'escribir',
           'nombres', 'dibujar', 'figuras', 'unir', 'rodear', 'colorear',
           'verdadero_falso', 'ordenar', 'diferencias', 'contar', 'teclado',
           'inventa', 'plan', 'metronomo', 'objetivo', 'para_clase',
           'reto', 'cifrado', 'escalera', 'a_cuatro_manos']


def plan(*tramos, **kw):
    """El plan de la semana: pares (minutos, qué hacer).

       Va en las 19 hojas, y a propósito. José María viene a clase, pero los
       otros seis días practica en casa: lo que se pierde ahí no es saber
       tocar, es saber por dónde empezar cuando se sienta al teclado. Los
       minutos son de verdad, no un adorno: si la suma pasa de 25 o 30, la
       semana no se hace."""
    return dict(tipo='plan', titulo=kw.get('titulo', 'El plan de la semana'),
                pista=kw.get('pista', 'no hace falta hacerlo todo el mismo día'),
                tramos=list(tramos), cierre=kw.get('cierre'))


def metronomo(*notas, **kw):
    return dict(tipo='metronomo',
                titulo=kw.get('titulo', 'A qué velocidad te sale'),
                pista=kw.get('pista', 'apunta el número al acabar cada día'),
                notas=list(notas), dias=kw.get('dias'))


def objetivo(texto, etiqueta='EL OBJETIVO DE LA SEMANA'):
    return dict(tipo='objetivo', etiqueta=etiqueta, texto=texto)


def para_clase(texto, pista='para no llegar con la duda encima'):
    """El recuadro que une la semana en casa con la clase siguiente.

       Es el mismo bloque que en el cuaderno de Arnau es "un juego con alguien
       de casa": aquí no, porque José María viene a clase. Lo que le sirve no
       es un juego, es llegar el día de la clase sabiendo qué preguntar y con
       el trabajo hecho por donde tocaba."""
    return dict(tipo='escucha', titulo='PARA LA PRÓXIMA CLASE',
                pista=pista, texto=texto)
