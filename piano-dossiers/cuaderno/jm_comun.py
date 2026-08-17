# -*- coding: utf-8 -*-
"""Piezas sueltas de las hojas de José María (formato de adulto).

   Reutiliza las fábricas de bloques que ya existen y añade las tres que solo
   tienen sentido para alguien que estudia solo en casa: el plan de minutos por
   día, la tabla de metrónomo y el objetivo de la semana.

   Los ejercicios se numeran solos en `hoja_deberes.build_deberes`, así que
   aquí no se pone `num` en ningún sitio.
"""
from arnau_comun import (n, ac, sil, corch, juego, acuerdate, escribir,
                         nombres, dibujar, figuras, unir, rodear, colorear,
                         verdadero_falso, ordenar, diferencias, contar,
                         teclado, inventa)

__all__ = ['n', 'ac', 'sil', 'corch', 'juego', 'acuerdate', 'escribir',
           'nombres', 'dibujar', 'figuras', 'unir', 'rodear', 'colorear',
           'verdadero_falso', 'ordenar', 'diferencias', 'contar', 'teclado',
           'inventa', 'plan', 'metronomo', 'objetivo']


def plan(*tramos, **kw):
    """El plan de la semana: pares (minutos, qué hacer).

       Va en las 19 hojas, y a propósito. José María estudia solo: lo que más
       le falla no es tocar, es saber por dónde empezar cuando se sienta al
       teclado. Los minutos son de verdad, no un adorno: si la suma pasa de 25
       o 30, la semana no se hace."""
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
