# -*- coding: utf-8 -*-
"""Da de alta una pieza nueva: mide su partitura y dice EXACTAMENTE que hay que
   tocar y donde, sin que haya que acordarse de nada.

   Anadir una pieza toca seis sitios y olvidarse de uno no da error, solo sale
   mal impreso: el modulo de la pieza, el indice de `build_<alumno>.py`, la
   lista de PDF de ese mismo build, y las tres tablas de lectura
   (`auditar_compas`, `auditar_tonalidad` y, si la partitura no se puede medir,
   `auditar_figuras.MIRADAS`). Esto los enumera con la linea ya escrita.

   Lo que NO hace, y es a proposito: rellenar el compas y la armadura. Los mide
   quien mira el recorte que deja `medir_partitura`. Si el programa los
   rellenara solo, la tabla de lecturas dejaria de ser un testigo de que
   alguien miro el papel, que es justo para lo que existe.

   Uso:
       python3 nueva_pieza.py <alumno> <num> <partitura.pdf> [slug]

   Ejemplo:
       python3 nueva_pieza.py dilan 21 ../students/dilan/source/DILAN/nueva.pdf
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import medir_partitura as mp                                     # noqa: E402

# alumno -> (prefijo de sus modulos, como se llama en CANCION['alumno'])
ALUMNOS = {
    'arnau': ('arnau', 'Arnau'), 'luisa': ('lu', 'Luisa'),
    'josemaria': ('jm', 'José María'), 'eduard': ('ed', 'Eduard'),
    'merce': ('me', 'Mercè'), 'isaac': ('is', 'Isaac'),
    'josep': ('jp', 'Josep'), 'nel': ('nl', 'Nel'),
    'dilan': ('dilan', 'Dilan'), 'eva': ('eva', 'Eva'),
}


def vecina(pref, num):
    """La pieza del mismo alumno mas cercana en numero: es la que hay que copiar.

       Cada alumno tiene su formato y sus ayudantes (`<pref>_comun.py`), y la
       manera rapida y segura de empezar una pieza es partir de la de al lado,
       no de una plantilla generica que no sabe de que formato hablamos."""
    mejores = []
    for f in sorted(glob.glob(os.path.join(HERE, pref + '_[0-9]*.py'))):
        m = os.path.basename(f)[:-3]
        try:
            n = int(m.split('_')[1])
        except (IndexError, ValueError):
            continue
        mejores.append((abs(n - num), n, m))
    mejores.sort()
    return mejores[0][2] if mejores else None


def main(argv):
    if len(argv) < 3 or argv[0] not in ALUMNOS:
        print(__doc__)
        print('alumnos: %s' % ', '.join(sorted(ALUMNOS)))
        return 2
    alumno, num, pdf = argv[0], int(argv[1]), argv[2]
    pref, nombre = ALUMNOS[alumno]
    slug = argv[3] if len(argv) > 3 else 'PONLE_UN_SLUG'
    modulo = '%s_%02d_%s' % (pref, num, slug.lower())

    if not os.path.exists(pdf):
        print('no existe la partitura: %s' % pdf)
        return 2
    if glob.glob(os.path.join(HERE, '%s_%02d_*.py' % (pref, num))):
        print('OJO: %s ya tiene una pieza con el número %d' % (alumno, num))

    d = mp.medir(pdf)
    mp.informe(d)

    ruta = os.path.relpath(os.path.abspath(pdf), HERE)
    trozos = ', '.join(repr(t) for t in ruta.split(os.sep))
    print('''
════════════════════════════════════════════════════════════════════
LOS SEIS SITIOS QUE HAY QUE TOCAR PARA %s Nº %d
════════════════════════════════════════════════════════════════════

1 · EL MÓDULO DE LA PIEZA   cuaderno/%s.py
      Cópialo de %s, que es su vecina y ya tiene el formato
      y los ayudantes de %s. Y en su CANCION:
          alumno='%s', num=%d, slug='%s',
          time_sig=(?, ?),   key_sig=?,     <- de mirar el recorte
          partitura=os.path.join(HERE, %s),%s

2 · EL ÍNDICE               build_%s.py, en ETAPAS
      dict(num=%d, titulo='...', autor='...',
           tonalidad='...', compas='...', trabaja='...'),
      Tienen que decir lo MISMO que la pieza: lo comprueba auditar_indice.py.

3 · LA LISTA DE PDF         build_%s.py, la lista de ficheros del álbum

4 · EL COMPÁS LEÍDO         auditar_compas.py, en LEIDO
      %-26s (?, ?),

5 · LA ARMADURA LEÍDA       auditar_tonalidad.py, en LEIDO
      %-26s '?',        # '0', '1 SOST', '2 BEM'...
%s
Y al terminar:  python3 auditar_todo.py %s
════════════════════════════════════════════════════════════════════''' % (
        nombre.upper(), num,
        modulo, vecina(pref, num) or '(no tiene vecina todavía)', nombre,
        nombre, num, slug,
        trozos,
        ('\n          # la música empieza en la página %d: la %d es portada'
         % (d['pagina_musica'], d['pagina_musica'] - 1)) if d['portada'] else '',
        alumno, num, alumno,
        repr(modulo) + ':', repr(modulo) + ':',
        ('''
6 · LO QUE SE VE A OJO      auditar_figuras.py, en MIRADAS
      Su partitura NO se puede medir (%s), así que hay
      que mirarla a tamaño grande y anotar si lleva semicorcheas:
      %r: (True/False, 'lo que se ve'),
''' % (d.get('motivo', ''), os.path.basename(pdf))) if not d['medible'] else
        '\n6 · (nada más: su partitura se puede medir sola)\n',
        alumno))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
