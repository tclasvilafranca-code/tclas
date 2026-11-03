# -*- coding: utf-8 -*-
"""Monta «Mi cuaderno de piano · Nivel 1 · Adultos» completo.

   python3 v1_libro.py            -> entrega/CUADERNO_NIVEL1_ADULTOS.pdf
   BN=1 python3 v1_libro.py       -> version para imprimir en blanco y negro (…_BN.pdf)"""
import io
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v1_base
from v1_base import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v1_extra
import v1_sep, v1_oct, v1_nov, v1_dic, v1_ene, v1_feb, v1_mar, v1_abr, v1_may, v1_jun, v1_anexos
from reportlab.pdfgen import canvas

MODULOS = [('Septiembre', v1_sep), ('Octubre', v1_oct), ('Noviembre', v1_nov), ('Diciembre', v1_dic), ('Enero', v1_ene),
           ('Febrero', v1_feb), ('Marzo', v1_mar), ('Abril', v1_abr), ('Mayo', v1_may), ('Junio', v1_jun)]


def montar(c, prev, portada=True):
    v1_base.SOLUCIONES.clear()
    if portada:
        v1_anexos.portada(c)
    d = Doc(c, 2 if portada else 1, prev)
    v1_anexos.inicio(d)
    v1_anexos.calendario(d)
    for mes, mod in MODULOS:
        d.marca(mes)
        v1_extra.apertura(d, mes)
        mod.construir(d)
        v1_extra.al_piano(d, mes)
    d.marca('Anexos')
    v1_anexos.chuleta(d)
    v1_anexos.glosario(d)
    d.marca('Diario')
    v1_anexos.diario(d)
    d.marca('Soluciones')
    v1_anexos.soluciones(d)
    d.marca('Pautas')
    v1_anexos.pautas(d)
    if os.environ.get('N1_PAR') == '1' and (len(d._paginar()) + (1 if portada else 0)) % 2 == 1:
        d.nuevo('Anexo · Papel pautado')
        d.add(*[pauta_vacia('treble', 4, None) for _ in range(5)], pauta_vacia('bass', 4, None))
    fin = d.fin()
    return d, fin


def main():
    out = os.path.join(HERE, '..', 'cuaderno', 'entrega')
    os.makedirs(out, exist_ok=True)
    bn = os.environ.get('BN') == '1'
    buf = io.BytesIO()
    c1 = canvas.Canvas(buf, pagesize=(W, H))
    d1, _ = montar(c1, {})
    c1.save()
    dst = os.path.join(out, os.environ.get('N1_OUT', 'CUADERNO_NIVEL1_ADULTOS_V1') + '%s.pdf' % ('_BN' if bn else ''))
    c2 = canvas.Canvas(dst, pagesize=(W, H))
    c2.setTitle('Mi cuaderno de piano · Nivel 1 · Adultos')
    c2.setAuthor('T-Clas')
    d2, fin = montar(c2, d1.marcas)
    c2.save()
    print('paginas:', fin - 1, '->', dst)
    print({k: v for k, v in d2.marcas.items()})


if __name__ == '__main__':
    main()
