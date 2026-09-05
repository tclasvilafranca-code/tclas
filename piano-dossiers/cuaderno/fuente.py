# -*- coding: utf-8 -*-
"""Acondiciona las partituras que llegan de Drive antes de montarlas.

   Las partituras las sube el cliente a su carpeta de Drive y llegan como
   llegan. En el álbum de José María salieron dos casos que rompían el montaje
   y que van a volver a salir con otros alumnos:

   1. **Una partitura que no es un PDF.** El Adagio de Albinoni venía como
      JPEG. Se convierte a PDF.
   2. **Un PDF que pypdf no sabe copiar.** Trouble (Coldplay) tiene dentro un
      objeto mal formado; `PdfReader` lo abre y cuenta bien las páginas, pero
      al copiarlas a un PDF nuevo pypdf revienta con LimitReachedError. Se
      reescribe con `pdftocairo`, que lo normaliza.

   En los dos casos el archivo acondicionado se guarda AL LADO del original,
   con el sufijo `_ok.pdf`, y se reutiliza si ya existe. Los originales no se
   tocan: son del cliente.

   Nada de esto se versiona (las partituras están fuera del repositorio), así
   que la conversión tiene que poder rehacerse sola en una máquina limpia. Por
   eso vive aquí y no en un script suelto que haya que acordarse de ejecutar.
"""
import os
import subprocess

IMAGENES = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff')


def _es_pdf(ruta):
    try:
        with open(ruta, 'rb') as f:
            return f.read(5) == b'%PDF-'
    except OSError:
        return False


def _copiable(ruta):
    """¿Se pueden copiar sus páginas a un PDF nuevo? Que `PdfReader` lo abra
       no basta: el que falla es el copiado."""
    try:
        from pypdf import PdfReader, PdfWriter
        w = PdfWriter()
        for p in PdfReader(ruta).pages:
            w.add_page(p)
        return True
    except Exception:
        return False


def normalizar(ruta):
    """Devuelve una ruta a un PDF que el montador pueda usar.

       Si el original ya vale, devuelve el original. Si no, deja un `_ok.pdf`
       al lado y devuelve ese. Si el archivo no existe, devuelve la ruta tal
       cual: `cancion.construir` ya sabe avisar de las partituras que faltan."""
    if not os.path.exists(ruta):
        return ruta

    base, ext = os.path.splitext(ruta)
    arreglado = base + '_ok.pdf'
    if os.path.exists(arreglado):
        return arreglado

    if not _es_pdf(ruta):
        if ext.lower() in IMAGENES or _parece_imagen(ruta):
            from PIL import Image
            im = Image.open(ruta)
            if im.mode != 'RGB':
                im = im.convert('RGB')
            im.save(arreglado, 'PDF', resolution=96.0)
            return arreglado
        return ruta

    if _copiable(ruta):
        return ruta

    # PDF con algo dentro que pypdf no sabe copiar: se reescribe entero.
    subprocess.run(['pdftocairo', '-pdf', ruta, arreglado], check=True)
    return arreglado


def _parece_imagen(ruta):
    try:
        from PIL import Image
        with Image.open(ruta):
            return True
    except Exception:
        return False
