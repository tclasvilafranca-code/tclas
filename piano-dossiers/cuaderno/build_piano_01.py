# -*- coding: utf-8 -*-
"""Hojas de trabajo al piano de la canción 1 (Chopsticks), en dos páginas.

   NADA de lo que hay aquí está inventado: todos los compases salen de la
   transcripción medida en TRANSCRIPCION_01_CHOPSTICKS.md. Cada ejercicio
   dice de qué compases sale, para que el alumno pueda ir a mirarlos.

   Página 1 — DESMONTAR: cada mano por separado, el ataque simultáneo, el
   viaje de intervalos sin relleno, el silencio de los cc. 15-16, y por fin
   los cc. 1-8 tal cual (el paso de reinsertar, que es el que cierra el
   círculo).

   Página 2 — MONTAR: el enlace A->B, la parte B entera en terceras, los dos
   finales, la escalera de tempo y el registro de la semana.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_piano import build_piano

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU', ' Chopsticks.pdf')

KICKER = 'Arnau · canción 1 · Chopsticks'
R = {'rest': True, 'dur': 'q'}


def D(a, b, dur='q'):
    """Un golpe de las dos manos: abajo la izquierda, arriba la derecha."""
    return {'pitches': [a, b], 'dur': dur}


def N(p, dur='q'):
    return {'pitch': p, 'dur': dur}


def rep(ev, n):
    return [dict(ev) for _ in range(n)]


# --- los compases reales, tal como están medidos en la partitura ----------
# parte A, cc. 1-8: las manos se abren en espejo y vuelven
A_IZQ = rep(N('F4'), 6) + rep(N('E4'), 6) + rep(N('D4'), 6) + \
        rep(N('C4'), 4) + [N('D4'), N('E4')]
A_DER = rep(N('G4'), 6) + rep(N('G4'), 6) + rep(N('B4'), 6) + \
        rep(N('C5'), 4) + [N('B4'), N('A4')]
A_18 = rep(D('F4', 'G4'), 6) + rep(D('E4', 'G4'), 6) + rep(D('D4', 'B4'), 6) + \
       rep(D('C4', 'C5'), 4) + [D('D4', 'B4'), D('E4', 'A4')]

# las siete estaciones del viaje, sin las repeticiones de relleno
ESTACIONES = [D('F4', 'G4'), D('E4', 'G4'), D('D4', 'B4'), D('C4', 'C5'),
              D('D4', 'B4'), D('E4', 'A4')]

# cc. 13-16 literales
CC1316 = rep(D('D4', 'B4'), 6) + \
         [D('C4', 'C5'), R, D('F4', 'G4')] + \
         [D('E4', 'C5'), R, D('C5', 'E5')]

# parte B, cc. 17-24 literales: las dos manos en terceras paralelas
B_1724 = [D('B4', 'D5', 'h'), D('A4', 'C5'),
          D('G4', 'B4', 'h'), D('F4', 'A4'),
          D('E4', 'G4', 'h'), D('E4', 'G4'),
          D('E4', 'G4'), D('F4', 'A4'), D('E4', 'G4'),
          D('D4', 'F4', 'h'), D('D4', 'F4'),
          D('D4', 'F4'), D('E4', 'G4'), D('D4', 'F4'),
          D('C4', 'E4', 'h'), D('F4', 'A4'),
          D('E4', 'G4'), R, D('C5', 'E5')]


PAG1 = dict(
    kicker=KICKER,
    esquina='Al piano · desmontar la pieza',
    titulo='Al piano · por partes',
    page_num=7,
    time_sig=(3, 4),
    gap=7.0,
    intro='Esto ya no es preparación: es la partitura, abierta en trozos. Cada ejercicio dice de '
          'qué compases sale. Arréglalos por separado y el último te los devuelve juntos.',
    reglas=['SOLO EL DEDO 2', 'ABAJO = IZQUIERDA · ARRIBA = DERECHA', 'DESPACIO Y SIN PARAR'],
    bloques=[
        dict(num=1, titulo='Cada mano por su lado',
             pista='cc. 1–8 · antes de juntarlas hay que saber qué hace cada una',
             sistemas=[
                 dict(cap='a)  SOLO LA MANO IZQUIERDA — baja Fa-Mi-Re-Do y vuelve',
                      events=A_IZQ, bars=8),
                 dict(cap='b)  SOLO LA MANO DERECHA — no se mueve en 4 compases, y luego sube',
                      events=A_DER, bars=8),
             ]),
        dict(num=2, titulo='Que suene UN golpe, no dos',
             pista='un ataque por compás, y silencio para escucharlo',
             sistemas=[dict(cap='si oyes dos ruidos, las manos no han caído a la vez · repite hasta que suene uno solo',
                            events=[e for d in ESTACIONES + [D('F4', 'G4')]
                                    for e in (d, R, dict(R))], bars=7)]),
        dict(num=3, titulo='El viaje, sin relleno',
             pista='la pieza repite cada posición seis veces · aquí cambias en cada tiempo',
             sistemas=[dict(cap='2ª → 3ª → 6ª → 8ª → 6ª → 4ª  ·  sin mirarte las manos: la distancia se aprende en el brazo',
                            events=ESTACIONES + ESTACIONES, bars=4)]),
        dict(num=4, titulo='El silencio es para viajar',
             pista='cc. 13–16 tal cual · el compás más difícil de la pieza',
             sistemas=[dict(cap='cuenta UN-dos-tres en voz alta también en el silencio',
                            events=CC1316, bars=4)]),
        dict(tipo='nota',
             etiqueta='POR QUÉ CUESTA EL c. 15',
             texto='Mira lo que pasa dentro de ese silencio: en el primer tiempo las manos están '
                   'a una octava, la máxima distancia de toda la pieza, y en el tercero están '
                   'pegadas en una 2ª. El salto entero ocurre mientras no suena nada. El silencio '
                   'no es para descansar: es el tiempo que tienes para viajar. Si llegas tarde, '
                   'no es que toques mal, es que has salido tarde.'),
        dict(num=5, titulo='Ahora sí: los compases 1–8',
             pista='lo de arriba, todo junto y tal como está escrito',
             sistemas=[dict(cap='si los cuatro ejercicios anteriores están hechos, esto ya te sale',
                            events=A_18, bars=8)]),
    ],
)

PAG2 = dict(
    kicker=KICKER,
    esquina='Al piano · montar la pieza',
    titulo='Al piano · montarla',
    page_num=8,
    time_sig=(3, 4),
    gap=7.0,
    intro='La segunda mitad de Chopsticks es otra cosa: las manos dejan de ir en espejo y pasan '
          'a cantar juntas. Aquí está el cambio, la parte B entera, los dos finales y la forma '
          'de subir de velocidad sin ensuciarla.',
    reglas=['SOLO EL DEDO 2', 'LA BLANCA DURA DOS TIEMPOS', 'CUENTA SIEMPRE EN VOZ ALTA'],
    bloques=[
        dict(num=6, titulo='El enlace: donde la pieza cambia',
             pista='cc. 16–19 · es el sitio donde se rompe siempre',
             sistemas=[dict(cap='el último golpe del c. 16 ya es el principio de la melodía: no lo toques como un final',
                            events=[D('E4', 'C5'), R, D('C5', 'E5')] + B_1724[:6],
                            bars=4)]),
        dict(tipo='nota',
             etiqueta='QUÉ HA CAMBIADO',
             texto='En la parte A las manos van en espejo: cuando una sube, la otra baja. En la '
                   'parte B van a la vez, separadas siempre por una 3ª, tocando la misma melodía. '
                   'Es la misma pieza, pero las manos han cambiado de relación — y por eso el '
                   'c. 16 cuesta más que los quince anteriores juntos.'),
        dict(num=7, titulo='La parte B: las terceras que bajan',
             pista='cc. 17–24 · la melodía baja por grados y las dos manos la llevan',
             sistemas=[dict(cap='blanca + negra: el vals · la mano se queda en la tecla toda la blanca, no la sueltes',
                            events=B_1724, bars=4)]),
        dict(tipo='nota',
             etiqueta='UNA COSA MENOS QUE APRENDER',
             texto='Los cc. 25–28 son exactamente los cc. 17–20, y los cc. 29–32 son los cc. 21–24 '
                   'con otro final. La parte B son OCHO compases, no dieciséis: te los aprendes '
                   'una vez y los tocas dos.'),
        dict(num=8, titulo='Los dos finales',
             pista='cc. 23–24 y cc. 31–32 · el mismo gesto, con final distinto',
             sistemas=[dict(cap='el c. 24 lanza otra vez la melodía · el c. 32 la deja caer y se acaba',
                            events=[D('C4', 'E4', 'h'), D('F4', 'A4'),
                                    D('E4', 'G4'), R, D('C5', 'E5'),
                                    D('C4', 'C5'), R, D('F4', 'G4'),
                                    D('E4', 'C5'), R, dict(R)],
                            bars=4)]),
        dict(tipo='escalera',
             valores=[60, 72, 84, 96, 104, 112],
             regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        dict(tipo='tracker',
             titulo='La prueba de la semana',
             pie='Marca el día en que la hayas tocado entera y sin parar, aunque sea muy despacio.'),
    ],
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_piano_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_piano(c, PAG1)
    build_piano(c, PAG2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(tmp).pages:
        writer.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    out = os.path.join(OUT_DIR, 'Arnau_01_Al_Piano_y_Partitura.pdf')
    with open(out, 'wb') as f:
        writer.write(f)
    os.remove(tmp)
    print('generated', out)


if __name__ == '__main__':
    main()
