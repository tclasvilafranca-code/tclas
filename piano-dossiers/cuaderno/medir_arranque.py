# -*- coding: utf-8 -*-
"""Lee del PDF las ALTURAS del primer compas de la melodia.

   POR QUE EXISTE. De los cinco datos que un dosier afirma sobre el papel, cuatro
   ya se leen solos (compas, armadura, figura mas corta y tempo) y el quinto —las
   NOTAS— se transcribia a mano y no lo comprobaba nadie. Se destapo mirando a
   tamano real el album de Arnau: *Polly Put the Kettle On* presentaba como
   "la melodia del principio" lo que en realidad es el COMPAS 2, y el pentagrama
   de su ficha traia dos notas que no estan ahi. El dato mas laborioso de todos
   —el que mas cuesta transcribir— era el unico sin testigo.

   QUE MIDE, EXACTAMENTE. El primer compas del pentagrama de ARRIBA del primer
   sistema de la primera pagina con musica. Nada mas. No sigue la pieza, no
   empareja compases, no lee ritmos: solo la fila de alturas con la que arranca
   la melodia, que es justo lo que citan las fichas ("Asi empieza") y el primer
   bloque de las hojas al piano.

   COMO LO MIDE:

     1. Rasteriza a 300 ppp y localiza las cinco lineas del pentagrama de arriba
        (`score_reader.pentagramas`, con los umbrales adaptativos de siempre).
     2. Busca la BARRA DIVISORIA: una columna de tinta continua de arriba abajo
        del pentagrama. La primera que haya despues de la clave, la armadura y la
        cifra de compas cierra el compas 1.
     3. Las cabezas de nota salen por EROSION con un rectangulo del tamano de una
        cabeza (9x13 px a 300 ppp). Erosionar se come las plicas, las barras
        finas y las lineas del pentagrama, y deja las cabezas. Las HUECAS
        (blancas y redondas) se parten en dos arcos y se vuelven a juntar por
        cercania: si dos trozos comparten columna y estan a menos de un espacio,
        son la misma nota.
     4. La altura sale de la distancia a las cinco lineas. La ALTERACION no se
        lee: se aplica la de la armadura, que ya esta medida y auditada aparte.

   LO QUE NO PUEDE. Igual que el detector de figuras: si el PDF lleva dentro una
   foto de 60 ppp, las cabezas ocupan tres pixeles y la erosion no distingue una
   cabeza de un borron. En ese caso dice NO MEDIBLE y no se inventa una lista.
   Mas vale no saberlo que creer que se sabe.

   Y tampoco sabe si la melodia esta arriba. En una pieza a cuatro manos donde el
   alumno lleva la parte de abajo, o en un arreglo con la melodia en la izquierda,
   lo que lee es correcto pero no es lo que cita el dosier. Por eso el que cruza
   (`auditar_alturas.py`) compara CONJUNTOS de alturas y contornos, y cuando no
   coinciden lo saca a mirar, no lo da por malo.

   Uso:  python3 medir_arranque.py <partitura.pdf>
"""
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import medir_figuras as mf                                          # noqa: E402
import score_reader as sr                                           # noqa: E402

DPI = 300
# Todas las medidas de cabeza van en ESPACIOS de pentagrama (ver `_cabezas`):
# una edicion imprime el pentagrama a 22 px y otra a 14, y con pixeles fijos el
# lector acertaba en una y fallaba en la otra.

LETRAS = 'CDEFGAB'
# Grado de la linea de arriba de cada clave, contado desde Do0.
CIMA = {'treble': ('F', 5), 'bass': ('A', 3)}


class NoMedible(Exception):
    pass


def _rasterizar(pdf, pagina):
    tmp = tempfile.mkdtemp()
    with open(pdf, 'rb') as fh:
        es_pdf = fh.read(4) == b'%PDF'
    if es_pdf:
        subprocess.run(['pdftoppm', '-png', '-r', str(DPI), '-f', str(pagina),
                        '-l', str(pagina), pdf, os.path.join(tmp, 'pg')],
                       check=True, stderr=subprocess.DEVNULL)
    else:
        Image.open(pdf).convert('L').save(os.path.join(tmp, 'pg-1.png'))
    hijos = sorted(os.path.join(tmp, f) for f in os.listdir(tmp))
    return tmp, (hijos[0] if hijos else None)


def _limpiar(tmp):
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)


def _tinta(path):
    gris = np.array(Image.open(path).convert('L'))
    for u in mf.UMBRALES:
        a = gris < u
        ps = sr.pentagramas(a)
        if ps:
            return a, ps
    raise NoMedible('no se encuentran los pentagramas')


def _lineas(a, top, bot):
    """Las cinco lineas de ese pentagrama, medidas de verdad (no interpoladas).

       `pentagramas` devuelve la de arriba y la de abajo; las tres de en medio se
       podrian repartir a partes iguales, pero un escaneo torcido reparte mal y
       una nota se va de sitio medio espacio, que es justo un grado."""
    banda = a[int(top) - 3:int(bot) + 4]
    filas = banda.sum(axis=1)
    umbral = max(20, filas.max() * 0.5)
    picos = [i for i, v in enumerate(filas) if v >= umbral]
    if not picos:
        raise NoMedible('el pentagrama no tiene lineas legibles')
    grupos, cur = [], [picos[0]]
    for x in picos[1:]:
        if x - cur[-1] <= 2:
            cur.append(x)
        else:
            grupos.append(sum(cur) / float(len(cur)))
            cur = [x]
    grupos.append(sum(cur) / float(len(cur)))
    if len(grupos) != 5:
        raise NoMedible('salen %d lineas, no cinco' % len(grupos))
    return [g + int(top) - 3 for g in grupos]


def _barra(a, arriba_y, abajo_y, desde, hasta):
    """La primera divisoria a partir de `desde`: una columna de tinta continua
       desde la primera linea del pentagrama de arriba hasta la ultima del de
       abajo, o sea de punta a punta del SISTEMA.

       Con el pentagrama de arriba solo, una PLICA larga se cuela: en The
       Wheels on the Bus daba un primer compas de seis espacios y una sola nota
       dentro. En un sistema de piano la divisoria une los dos pentagramas y la
       plica no llega nunca; ese es el rasgo que las separa."""
    y0, y1 = int(arriba_y) + 2, int(abajo_y) - 1
    if y1 <= y0:
        return None
    lleno = a[y0:y1, :].mean(axis=0)
    for x in range(desde, min(hasta, a.shape[1])):
        if lleno[x] >= 0.96:
            return x
    return None


def _tras_la_cabecera(a, lineas, ini):
    """Donde acaba la clave + armadura + cifra y empieza la musica.

       Estaba puesto a ojo en ocho espacios y no vale: en una edicion apretada
       se come la nota de la anacrusa (My Bonnie empieza con una sola corchea
       antes del primer compas y se perdia), y en una holgada deja dentro el
       ultimo sostenido de la armadura. Lo que si es constante es que despues de
       la cifra de compas hay un HUECO en blanco antes de la primera nota."""
    sp = (lineas[-1] - lineas[0]) / 4.0
    banda = a[int(lineas[0] - 1.6 * sp):int(lineas[-1] + 1.6 * sp)].copy()
    base = int(lineas[0] - 1.6 * sp)
    for l in lineas:                      # las lineas del pentagrama no son tinta
        for dy in (-1, 0, 1):
            r = int(round(l)) + dy - base
            if 0 <= r < banda.shape[0]:
                banda[r, :] = False
    tinta = banda.any(axis=0)
    hueco = max(3, int(sp * 0.5))
    seguidos = 0
    for x in range(ini + int(sp * 2), min(a.shape[1], ini + int(sp * 14))):
        seguidos = seguidos + 1 if not tinta[x] else 0
        if seguidos >= hueco:
            return x - hueco + 1
    return ini + int(sp * 8)


def _cabezas(a, lineas, x0, x1):
    """Las cabezas de nota del trozo, LLENAS y HUECAS, cada una con su centro.

       Son dos dibujos distintos y hacen falta las dos cosas:

       - la LLENA (negra, corchea, semicorchea) es una mancha maciza: sale con
         una apertura morfologica del tamano de la cabeza, que se come la plica
         (delgada) y las barras (finas de alto);
       - la HUECA (blanca, redonda) es un anillo, y una apertura se la lleva por
         delante. Lo que si tiene es un AGUJERO CERRADO dentro, y eso se saca
         rellenando la imagen y restandola: lo que aparece es justo el hueco.

       Las medidas van en espacios de pentagrama, no en pixeles: una edicion
       imprime el pentagrama a 22 px y otra a 14, y con constantes fijas el
       lector funcionaba en una y no en la otra."""
    # Solo se miran DOS lineas adicionales arriba y abajo. Mas arriba estan las
    # letras de acorde y las palabras de tempo, y una "B" o una "o" tienen un
    # agujero cerrado igual que una blanca: con la ventana ancha, el Toreador
    # devolvia un Fa6 que en realidad era la "F" del cifrado.
    sp = (lineas[-1] - lineas[0]) / 4.0
    y0 = max(0, int(lineas[0] - 2.4 * sp))
    y1 = min(a.shape[0], int(lineas[-1] + 2.4 * sp))
    sub = a[y0:y1, x0:x1]

    llenas = _llenas(sub, sp)   # negras y corcheas
    huecas = _huecas(sub, sp)   # blancas y redondas
    todas = [(cx + x0, cy + y0) for cx, cy in llenas + huecas]
    todas = [c for c in todas if _es_nota(a, lineas, sp, *c)]
    return _sin_repetir(sorted(todas), sp)


def _es_nota(a, lineas, sp, cx, cy):
    """Fuera del pentagrama, una nota SIEMPRE lleva su linea adicional.

       Encima del pentagrama viven los numeros de dedo, las letras de acorde y
       las palabras de tempo, y a esa altura un digito deja una mancha del
       tamano de una cabeza: el 3 de la digitacion de *Oh When the Saints* se
       leia como un Do6. Lo que ninguno de ellos tiene es la rayita horizontal
       que cruza la cabeza, asi que se pide."""
    if lineas[0] - 0.6 * sp <= cy <= lineas[-1] + 0.6 * sp:
        return True
    fila = a[int(cy) - 3:int(cy) + 4, int(cx - sp * 0.6):int(cx + sp * 0.6)]
    if not fila.size:
        return False
    return fila.any(axis=0).mean() >= 0.95


def _elipse(alto, ancho):
    yy, xx = np.mgrid[0:alto, 0:ancho]
    cy, cx = (alto - 1) / 2.0, (ancho - 1) / 2.0
    return (((yy - cy) / (cy + 0.5)) ** 2 + ((xx - cx) / (cx + 0.5)) ** 2) <= 1.0


def _llenas(sub, sp):
    est = _elipse(max(3, int(round(sp * 0.62))), max(3, int(round(sp * 0.82))))
    ab = ndimage.binary_opening(sub, structure=est)
    lbl, _n = ndimage.label(ab)
    fuera = []
    for s in ndimage.find_objects(lbl):
        ys, xs = s
        ancho, alto = xs.stop - xs.start, ys.stop - ys.start
        if ancho > sp * 2.0 or alto > sp * 1.8:
            continue                      # una barra de corcheas, o un pegote
        if ancho < sp * 0.7 or alto < sp * 0.55:
            continue                      # un puntillo, un trozo de plica
        if not 1.05 <= ancho / float(alto) <= 2.1:
            continue                      # una cabeza es un ovalo TUMBADO
        fuera.append(((xs.start + xs.stop) / 2.0, (ys.start + ys.stop) / 2.0))
    return fuera


def _huecas(sub, sp):
    dentro = ndimage.binary_fill_holes(sub) & ~sub
    lbl, _n = ndimage.label(dentro)
    fuera = []
    for s in ndimage.find_objects(lbl):
        ys, xs = s
        ancho, alto = xs.stop - xs.start, ys.stop - ys.start
        if not (sp * 0.3 <= ancho <= sp * 1.3 and sp * 0.25 <= alto <= sp * 1.1):
            continue
        if not 1.05 <= ancho / float(alto) <= 2.4:
            continue        # el ojo de un bemol y la panza de una C son altos,
                            # no tumbados; el hueco de una blanca si lo es
        fuera.append(((xs.start + xs.stop) / 2.0, (ys.start + ys.stop) / 2.0))
    return fuera


def _sin_repetir(cabezas, sp):
    """Una misma cabeza puede salir por los dos caminos (una blanca gorda pasa
       la apertura y ademas tiene agujero). Dos centros a menos de media cabeza
       son la misma nota."""
    fuera = []
    for cx, cy in cabezas:
        if fuera and abs(cx - fuera[-1][0]) < sp * 0.7 and abs(cy - fuera[-1][1]) < sp * 0.5:
            continue
        fuera.append((cx, cy))
    return fuera


def _altura(cy, lineas, clef):
    """De una coordenada a un nombre de nota. Sin alteracion: la pone la
       armadura, que ya esta medida y auditada en `auditar_tonalidad`."""
    paso = (lineas[-1] - lineas[0]) / 8.0
    grados = int(round((cy - lineas[0]) / paso))
    letra, octava = CIMA[clef]
    i = LETRAS.index(letra) - grados
    return '%s%d' % (LETRAS[i % 7], octava + (i // 7))


def arranque(pdf, pagina=None, clef='treble', pentagrama=0, alteraciones=0):
    """Las alturas del primer compas del pentagrama `pentagrama` del primer
       sistema. Lanza `NoMedible` si el papel no da para leerlas."""
    import medir_partitura as mp
    pg = pagina or mp.primera_de_musica(pdf)
    tmp, ruta = _rasterizar(pdf, pg)
    try:
        if not ruta:
            raise NoMedible('no se puede rasterizar')
        a, ps = _tinta(ruta)
        if len(ps) <= pentagrama:
            raise NoMedible('la pagina no trae ese pentagrama')
        top, bot = ps[pentagrama]
        sp = (bot - top) / 4.0
        if sp < 12:
            raise NoMedible('el pentagrama mide %.0f px de espacio: es una foto '
                            'de poca resolucion' % sp)
        lineas = _lineas(a, top, bot)
        # el arranque del pentagrama, para saber donde acaba la clave
        fila = a[int(top) - 1:int(top) + 2].any(axis=0)
        xs = np.where(fila)[0]
        if not len(xs):
            raise NoMedible('no se ve el pentagrama')
        ini = int(xs[0])
        # despues de la clave van la ARMADURA (una alteracion por sostenido o
        # bemol, algo menos de un espacio cada una) y la CIFRA de compas (dos
        # espacios largos). Sin descontarlas, el ojo de un bemol apoyado en la
        # linea del Si se lee como un Si: pasaba en Polly y en el Toreador, las
        # dos en Fa mayor.
        cab = _tras_la_cabecera(a, lineas, ini) + int((alteraciones + 2.2) * sp)
        # De punta a punta del SISTEMA, que es hasta donde llega la divisoria.
        # En una pieza a CUATRO manos hay dos pianos con su llave cada uno y la
        # divisoria no los une: se mide solo el del alumno (los dos primeros
        # pentagramas), o Mulberry no encuentra ninguna.
        por = mp._por_sistema(a, ps)
        cuantos = min(len(ps), max(1, min(por, 2)))
        ultimo = ps[cuantos - 1][1]

        # Un compas de SILENCIO no es un compas sin medir: My Bonnie empieza con
        # un silencio de negra antes de la primera nota, y con el compas fijo el
        # lector devolvia "no se distingue ninguna cabeza" en una partitura
        # perfectamente legible. Se salta hasta dos compases vacios.
        x = cab
        for _intento in range(3):
            fin = _barra(a, lineas[0], ultimo, x + int(sp * 2), x + int(sp * 70))
            if fin is None:
                raise NoMedible('no se encuentra la divisoria del primer compás')
            cabezas = _cabezas(a, lineas, x, fin)
            if cabezas:
                return [_altura(cy, lineas, clef) for _cx, cy in cabezas]
            x = fin + 3
        raise NoMedible('no se distingue ninguna cabeza de nota')
    finally:
        _limpiar(tmp)


def main(argv):
    if not argv:
        print(__doc__.strip().splitlines()[-1])
        return 2
    for p in argv:
        try:
            print('%-46s %s' % (os.path.basename(p)[:46],
                                ' '.join(arranque(p))))
        except NoMedible as e:
            print('%-46s NO MEDIBLE · %s' % (os.path.basename(p)[:46], e))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
