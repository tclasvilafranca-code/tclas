# -*- coding: utf-8 -*-
"""Montaje del album: lo que no es de una pieza, sino del orden de las hojas.

   NORMA DEL PROYECTO (decision del cliente, vale para TODOS los alumnos):
   **la partitura de una pieza a cuatro manos tiene que verse abierta de un
   vistazo.** Entre dos personas sentadas al mismo piano, pasar una pagina a
   mitad de pieza no es una opcion: las dos paginas de la partitura (Primo y
   Secondo, o el Piano 1 y el Piano 2) tienen que quedar enfrentadas.

   En un cuaderno encuadernado la pagina 1 (la portada) cae a la derecha, asi
   que las paginas que se ven juntas son (2,3), (4,5), (6,7)... La partitura
   tiene que EMPEZAR EN UNA PAGINA PAR. Si el montaje la dejaria empezando en
   una impar, se intercala delante una hoja de PAPEL PAUTADO (la misma de
   `hoja_pauta.py`, que ya va al final de cada pieza): pentagramas vacios que
   no estorban y que ademas sirven para apuntar. Si ya cae en par, no se
   mete nada: una hoja de mas es papel pagado.

   Cada `build_<alumno>.py` monta su album con `anadir_dosier`, que es quien
   decide. La lista de piezas a cuatro manos esta en `DUETOS` y hay que
   ponerla al dar de alta una pieza nueva (lo recuerda `nueva_pieza.py`).
"""
import io
import os

from pypdf import PdfReader
from reportlab.pdfgen import canvas

from portada import W, H
from hoja_pauta import build_pauta

# Nombre del PDF de cada pieza a cuatro manos: '<carpeta>_<nn>_<slug>_CUADERNO.pdf'
DUETOS = {
    'Aida_01_RomanceDiabelli_CUADERNO.pdf',
    'Aida_02_ScherzoDiabelli_CUADERNO.pdf',
    'Aida_10_ItsBeginningToLook_CUADERNO.pdf',
    'Arnau_19_RainRainGoAway_CUADERNO.pdf',
    'Arnau_20_MulberryBush_CUADERNO.pdf',
    'Dilan_17_Arabesque_CUADERNO.pdf',
    'Dilan_20_BeginningChristmas_CUADERNO.pdf',
    'Eduard_08_TheBeginner_CUADERNO.pdf',
    'Eduard_12_VillancicosCuatroManos_CUADERNO.pdf',
    'Eva_15_BeginningChristmas_CUADERNO.pdf',
    'Eva_16_Arabesque_CUADERNO.pdf',
    'Isaac_01_PetiteChanson_CUADERNO.pdf',
    'Isaac_04_TheBeginner_CUADERNO.pdf',
    'Isaac_06_ChristmasSongs_CUADERNO.pdf',
    'Isaac_08_SilentNight4Hands_CUADERNO.pdf',
    'JoseMaria_01_RomanceDiabelli_CUADERNO.pdf',
    'Josep_01_RomanceDiabelli_CUADERNO.pdf',
    'Josep_02_PetiteChanson_CUADERNO.pdf',
    'Josep_10_BellaCiao_CUADERNO.pdf',
    'Josep_14_BeginningChristmas_CUADERNO.pdf',
    'Luisa_01_SonatinaBambini_CUADERNO.pdf',
    'Luisa_03_SonatinaSolMayor_CUADERNO.pdf',
    'Luisa_07_ChristmasSongs_CUADERNO.pdf',
    'Merce_01_SonatinaBambini_CUADERNO.pdf',
    'Merce_08_ChristmasSongs_CUADERNO.pdf',
    'Nel_01_PetiteChanson_CUADERNO.pdf',
    'Nel_07_BellaCiao_CUADERNO.pdf',
    'Jaume_02_RomanceDiabelli_CUADERNO.pdf',
    'Jaume_06_BellaCiao_CUADERNO.pdf',
    'Jaume_12_ItsBeginningToLook_CUADERNO.pdf',
}

INSERTADAS = []          # (album, pieza) donde se ha metido la hoja de pauta


def _hoja_pauta(alumno):
    """Una hoja de papel pautado, suelta, lista para intercalar."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    build_pauta(c, dict(
        kicker='%s · antes del dúo' % alumno, esquina='Papel pautado',
        titulo_pauta='Para escribir',
        pie_pauta='esta hoja deja las dos páginas de la partitura a cuatro manos abiertas a la vez'))
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def anadir_dosier(wr, ruta, alumno=''):
    """Añade las paginas de un dosier al album en construccion, y si es a
       cuatro manos y su partitura caeria empezando en pagina impar, intercala
       antes una hoja de papel pautado. Devuelve True si la ha intercalado."""
    nombre = os.path.basename(ruta)
    metida = False
    # las paginas ya montadas: la siguiente es la n+1, y tiene que ser PAR
    if nombre in DUETOS and len(wr.pages) % 2 == 0:
        wr.add_page(_hoja_pauta(alumno or nombre.split('_')[0]))
        INSERTADAS.append(nombre)
        metida = True
    for p in PdfReader(ruta).pages:
        wr.add_page(p)
    return metida
