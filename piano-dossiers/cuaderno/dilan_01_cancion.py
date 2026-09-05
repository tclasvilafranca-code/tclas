# -*- coding: utf-8 -*-
"""El Cisne (cancion 1) en el formato comun de cancion.py.

   Las dos primeras canciones de Dilan se escribieron antes de que existiera
   cancion.py y cada hoja vivia en su propio build_*_d01.py. El contenido es
   bueno y esta verificado, asi que no se reescribe: se envuelve. Este archivo
   solo junta las piezas en el diccionario CANCION que espera el constructor,
   para que las veinte pasen por el mismo sitio y hereden el rediseno (hojas
   de pentagrama generadas, hoja de relajacion, numeracion de pagina).
"""
import os

import build_ficha_d01 as bf
import build_calentamiento_d01 as bc
import build_lectura_d01 as bl
import build_piano_d01 as bp

CANCION = dict(
    alumno='Dilan', num=1, slug='ElCisne',
    titulo_corto='El Cisne', nivel='avanzado',
    time_sig=(3, 4), key_sig='Sol mayor',
    partitura=bf.SOURCE_PDF,
    yt=bf.YT_URL,
    ficha=bf.CFG,
    calentamiento=bc.CFG,
    agudeza=bl.CFG,
    piano1=bp.PAG1,
    piano2=bp.PAG2,
)
