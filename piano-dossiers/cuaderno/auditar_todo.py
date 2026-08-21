# -*- coding: utf-8 -*-
"""UN SOLO COMANDO. Pasa todas las auditorias del proyecto y da un veredicto.

   Existe porque revisar a ratos no funciona: los fallos gordos de este
   cuaderno (dos compases mal, la figura del Toreador, las semicorcheas que
   nadie dibujaba) no se colaron por falta de auditores, sino porque los
   auditores se ejecutaban de uno en uno, cuando uno se acordaba. Esto los
   ejecuta TODOS, siempre, y dice en una linea si el cuaderno esta para
   imprimir o no.

   Uso:
       python3 auditar_todo.py                  todo, incluidos los diez
                                                auditores por alumno (tarda
                                                unos minutos)
       python3 auditar_todo.py --rapido         solo los cruces contra la
                                                partitura (segundos)
       python3 auditar_todo.py arnau lu         solo esos alumnos
       python3 auditar_todo.py --pixeles        ademas, el control de pixeles
                                                sobre los PDF ya montados

   El orden NO es casual: primero lo que se comprueba contra el papel (compas,
   armadura, figura), porque un dato mal medido invalida todo lo que venga
   despues; luego lo que se comprueba contra las reglas del proyecto (nivel,
   vocabulario, andamio, variedad); y al final lo caro (los diez alumnos y los
   pixeles).
"""
import glob
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'output')

ALUMNOS = ['arnau', 'luisa', 'josemaria', 'eduard', 'merce',
           'isaac', 'josep', 'nel', 'dilan', 'eva']

# prefijo de modulo -> nombre del auditor por alumno. Los dos nombres no
# coinciden (el prefijo es corto porque va en el nombre de 199 ficheros).
PREFIJO = {'arnau': 'arnau', 'lu': 'luisa', 'jm': 'josemaria', 'ed': 'eduard',
           'me': 'merce', 'is': 'isaac', 'jp': 'josep', 'nl': 'nel',
           'dilan': 'dilan', 'eva': 'eva'}

# (script, acepta prefijos, que comprueba)
CONTRA_LA_PARTITURA = [
    ('auditar_compas.py', True, 'el compás que declara cada pieza es el impreso'),
    ('auditar_tonalidad.py', True, 'la armadura declarada es la impresa'),
    ('auditar_figuras.py', True, 'la figura más corta impresa está dibujada'),
    ('auditar_tempo.py', True, 'el tempo que cita la ficha es el impreso'),
]
CONTRA_LAS_REGLAS = [
    ('auditar_niveles.py', True, 'cada alumno solo ve las figuras de su escalón'),
    ('auditar_vocabulario.py', True, 'no se habla de lo que no se dibuja'),
    ('auditar_andamio.py', False, 'el andamio inventado no se repite entre piezas'),
    ('auditar_indice.py', True, 'el índice y la ficha dicen lo mismo que la pieza'),
]


def _correr(script, args):
    t = time.time()
    p = subprocess.run([sys.executable, os.path.join(HERE, script)] + list(args),
                       capture_output=True, text=True, cwd=HERE)
    return p.returncode, p.stdout + p.stderr, time.time() - t


def _linea(nombre, ok, seg, detalle=''):
    print('  %-24s %-6s %5.1fs  %s' % (nombre, 'ok' if ok else 'FALLA', seg, detalle))


def _ultimas(salida, n=8):
    """Las lineas con chicha de una salida que ha fallado."""
    lineas = [l for l in salida.splitlines() if l.strip()
              and 'notation engine ready' not in l]
    return lineas[-n:]


def main(argv):
    rapido = '--rapido' in argv
    pixeles = '--pixeles' in argv
    prefijos = [a for a in argv if not a.startswith('--')]
    # el usuario puede escribir el nombre largo del alumno o el prefijo corto
    inverso = {v: k for k, v in PREFIJO.items()}
    prefijos = [inverso.get(a, a) for a in prefijos]

    fallos = []
    print('\nCONTRA LA PARTITURA — lo que no se mide, no se escribe')
    for script, acepta, que in CONTRA_LA_PARTITURA + CONTRA_LAS_REGLAS:
        if script == 'auditar_niveles.py':
            print('\nCONTRA LAS REGLAS DEL PROYECTO')
        rc, out, seg = _correr(script, prefijos if acepta else [])
        _linea(script[:-3], rc == 0, seg, que)
        if rc:
            fallos.append((script, out))

    if not rapido:
        print('\nPOR ALUMNO — estructura, reparto de ejercicios y variedad')
        quiero = [PREFIJO[p] for p in prefijos] if prefijos else ALUMNOS
        for a in quiero:
            script = 'auditar_%s.py' % a
            if not os.path.exists(os.path.join(HERE, script)):
                continue
            rc, out, seg = _correr(script, [])
            _linea(script[:-3], rc == 0, seg)
            if rc:
                fallos.append((script, out))

    if pixeles:
        print('\nSOBRE EL PAPEL — ninguna página se sale del margen')
        pdfs = sorted(glob.glob(os.path.join(OUT, '*_Cuaderno_del_Pianista_*.pdf')))
        if not pdfs:
            print('  (no hay álbumes montados en output/ · pásalos por build_<alumno>.py)')
        else:
            rc, out, seg = _correr('revisar_pixeles.py', pdfs)
            _linea('revisar_pixeles', rc == 0, seg, '%d álbumes' % len(pdfs))
            if rc:
                fallos.append(('revisar_pixeles.py', out))

    print('')
    if not fallos:
        print('TODO OK — el cuaderno está para imprimir.')
        return 0
    print('%d AUDITORÍAS FALLAN\n' % len(fallos))
    for script, out in fallos:
        print('--- %s' % script)
        for l in _ultimas(out):
            print('    %s' % l)
        print('')
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
