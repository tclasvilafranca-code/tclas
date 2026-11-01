# -*- coding: utf-8 -*-
"""Monta «Mi cuaderno de piano · Nivel 1 · Adultos» completo.

   python3 n1_libro.py            -> entrega/CUADERNO_NIVEL1_ADULTOS.pdf
   BN=1 python3 n1_libro.py       -> version para imprimir en blanco y negro (…_BN.pdf)"""
import io
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import n1_base
from n1_base import *
import n1_sep, n1_oct, n1_nov, n1_dic, n1_ene, n1_feb, n1_mar, n1_abr, n1_may, n1_jun, n1_anexos
from reportlab.pdfgen import canvas

MODULOS = [('Septiembre', n1_sep), ('Octubre', n1_oct), ('Noviembre', n1_nov), ('Diciembre', n1_dic), ('Enero', n1_ene),
           ('Febrero', n1_feb), ('Marzo', n1_mar), ('Abril', n1_abr), ('Mayo', n1_may), ('Junio', n1_jun)]


def montar(c, prev, portada=True):
    n1_base.SOLUCIONES.clear()
    if portada:
        n1_anexos.portada(c)
    d = Doc(c, 2 if portada else 1, prev)
    n1_anexos.inicio(d)
    n1_anexos.calendario(d)
    for mes, mod in MODULOS:
        d.marca(mes)
        mod.construir(d)
    d.marca('Anexos')
    n1_anexos.chuleta(d)
    n1_anexos.glosario(d)
    d.marca('Diario')
    n1_anexos.diario(d)
    d.marca('Soluciones')
    n1_anexos.soluciones(d)
    d.marca('Pautas')
    n1_anexos.pautas(d)
    fin = d.fin()
    return d, fin


def main():
    out = os.path.join(HERE, 'entrega')
    os.makedirs(out, exist_ok=True)
    bn = os.environ.get('BN') == '1'
    buf = io.BytesIO()
    c1 = canvas.Canvas(buf, pagesize=(W, H))
    d1, _ = montar(c1, {})
    c1.save()
    dst = os.path.join(out, 'CUADERNO_NIVEL1_ADULTOS%s.pdf' % ('_BN' if bn else ''))
    c2 = canvas.Canvas(dst, pagesize=(W, H))
    c2.setTitle('Mi cuaderno de piano · Nivel 1 · Adultos')
    c2.setAuthor('T-Clas')
    d2, fin = montar(c2, d1.marcas)
    c2.save()
    print('paginas:', fin - 1, '->', dst)
    print({k: v for k, v in d2.marcas.items()})


if __name__ == '__main__':
    main()
