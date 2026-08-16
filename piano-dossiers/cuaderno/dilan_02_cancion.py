# -*- coding: utf-8 -*-
"""Can't Help Falling in Love (cancion 2) en el formato comun de cancion.py.

   Mismo caso que la 1: el contenido ya estaba escrito y verificado en sus
   build_*_d02.py, y aqui solo se envuelve para que pase por el constructor
   comun. Ver dilan_01_cancion.py.
"""
import build_ficha_d02 as bf
import build_calentamiento_d02 as bc
import build_lectura_d02 as bl
import build_piano_d02 as bp

CANCION = dict(
    alumno='Dilan', num=2, slug='CantHelp',
    titulo_corto='Can’t Help Falling in Love', nivel='avanzado',
    time_sig=(3, 4), key_sig='Re mayor',
    nivel_base=1,
    partitura=bf.SOURCE_PDF,
    yt=bf.YT_URL,
    ficha=bf.CFG,
    calentamiento=bc.CFG,
    agudeza=bl.CFG,
    piano1=bp.PAG1,
    piano2=bp.PAG2,
)
