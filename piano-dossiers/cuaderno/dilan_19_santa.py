# -*- coding: utf-8 -*-
"""Santa Tell Me (Ariana Grande, arr. Sadie King) — Dilan, avanzado.
   Ver TRANSCRIPCION_D18_20.md.

   Sol mayor, un sostenido. Es la partitura con el RECORRIDO mas complicado
   del album: segno, casillas 1a y 2a, To Coda y una nota al pie que avisa de
   que en la repeticion cambia una nota.

   Y trae dos cosas que no aparecen en ninguna otra: PEDAL escrito, un 8vb en
   la izquierda de la introduccion, y un "LH over RH" en el c. 4 — la mano
   izquierda cruza por encima de la derecha.

   NO se cita el total de compases: el lector cuenta 13 y es claramente menos
   de lo que hay (los silencios y el picado le rompen la deteccion de barras).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'
_B = [2700]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='q'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


SOLac = ('G3', 'B3', 'D4')
DOac = ('G3', 'C4', 'E4')
REac = ('F3', 'A3', 'D4')
MImac = ('G3', 'B3', 'E4')

CANCION = dict(
    alumno='Dilan', num=19, nivel='avanzado', slug='SantaTellMe',
    titulo_corto='Santa Tell Me', time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'Santa-tell-me-ariana-grande NAVIDAD.pdf'),
    yt='https://www.youtube.com/results?search_query=ariana+grande+santa+tell+me',

    ficha=dict(
        titulo='Santa Tell Me',
        autor='Ariana Grande (2014) · arr. Sadie King',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'), ('Tempo', '♩=92'),
               ('Mano izq.', 'Picada'), ('Extras', 'Pedal · 8vb')],
        armonia=dict(
            titulo='Lo que trae esta partitura y ninguna otra',
            tarjetas=[
                ('EL RECORRIDO', 'Segno y coda',
                 'Segno, casillas 1.ª y 2.ª, To Coda y una nota al pie. Hay que leerlo antes.'),
                ('LH OVER RH', 'La mano cruza',
                 'En el c. 4 la izquierda pasa por encima de la derecha. Está escrito.'),
                ('EL 8vb', 'Suena más grave',
                 'En la introducción, la izquierda suena una octava por debajo de lo escrito.'),
                ('EL PEDAL', 'Está escrito',
                 'Es la única del cuaderno donde el arreglista te dice dónde ponerlo.'),
            ],
            pie='Casi todas las canciones del cuaderno tienen la dificultad en los dedos. Esta la tiene '
                'en la hoja: entre el segno, las dos casillas, la coda y la nota al pie, se toca en un '
                'orden que no es el orden en que está impresa. Media hora con el dedo siguiendo la '
                'partitura y en voz alta vale más que tres días tocando.',
        ),
        ritmos=[
            ('MI · la intro', 'acordes largos, y suenan una octava más abajo (8vb)',
             [ac(SOLac, 'h'), ac(DOac, 'h')], OCRE, 'bass', SOL),
            ('MI · la estrofa', 'notas graves picadas, con silencios entre medias',
             [n('D2', 'e'), sil('e'), n('A2', 'e'), sil('e'),
              n('D2', 'q'), sil('q')], OCRE, 'bass', SOL),
            ('MD', 'la melodía, en corcheas y muy hablada',
             corch(['D4', 'G4', 'F4', 'G4']) + [n('G4'), n('F4')], AZUL, 'treble', SOL),
        ],
        especial=[
            'Armadura de un sostenido: todos los Fa son ♯. La tonalidad es Sol mayor.',
            'Hay SEGNO, casillas 1.ª y 2.ª, y "To Coda": el orden no es el que está escrito.',
            'Al pie pone "D on the repeat": en la repetición, una nota cambia.',
            'En el c. 4 pone "LH over RH": la izquierda cruza por encima de la derecha.',
            'La izquierda de la introducción lleva 8vb: suena una octava más grave.',
            'El PEDAL viene escrito. Es la única partitura del cuaderno que lo indica.',
        ],
        reto='El recorrido. Puedes tener todas las notas y aun así no saber tocar la canción entera, '
             'porque no sabrás por dónde seguir. Y cuando llegue el "LH over RH", si no lo has '
             'preparado, las dos manos van a chocar.',
        truco='Coge la partitura sin piano y recórrela con el dedo diciendo en voz alta: "intro, segno, '
              'estrofa, casilla 1, vuelvo al segno, casilla 2, sigo hasta To Coda…". Hazlo tres veces. '
              'Y el cruce de manos practícalo despacio, mirando dónde pones cada una.',
        sabias='Ariana Grande la escribió con Savan Kotecha en un estudio de Suecia en pleno agosto, con '
               'treinta grados fuera. Es la única canción de Navidad reciente que ha entrado todos los '
               'años en las listas desde que salió.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en el piano del principio: son esas notas agudas repetidas.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción pide notas picadas con la '
              'izquierda, acordes largos con pedal y, en un sitio, cruzar una mano por encima de la '
              'otra. Aquí se entrenan las tres cosas, en Sol mayor.',
        reglas=['ARMADURA DE SOL: TODOS LOS FA SON ♯', 'PICADO ES CORTO, NO FUERTE', 'MIRA DÓNDE PONES LA MANO'],
        ejercicios=[
            dict(num=1, titulo='Escala de Sol mayor · dos octavas', clef='bass',
                 pista='manos separadas · un solo sostenido, y el pulgar por debajo sin bache',
                 events=corch(['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3']) +
                        corch(['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'G4']) +
                        corch(['G4', 'F4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3']) +
                        corch(['F3', 'E3', 'D3', 'C3', 'B2', 'A2', 'G2', 'G2']),
                 bars_per_line=4),
            dict(num=2, titulo='Notas picadas con silencios', clef='bass',
                 pista='el gesto de la izquierda · la nota es corta, pero no fuerte',
                 events=([n('G2', 'e'), sil('e'), n('D3', 'e'), sil('e')] * 2 +
                         [n('A2', 'e'), sil('e'), n('E3', 'e'), sil('e')] * 2 +
                         [n('C3', 'e'), sil('e'), n('G3', 'e'), sil('e')] * 2 +
                         [n('G2', 'e'), sil('e'), n('D3', 'e'), sil('e')] * 2),
                 bars_per_line=4),
            dict(num=3, titulo='Acordes largos, con pedal', clef='bass',
                 pista='lo contrario del anterior · pisa el pedal, ataca, y cámbialo al acorde siguiente',
                 events=[ac(SOLac, 'w'), ac(DOac, 'w'), ac(REac, 'w'), ac(MImac, 'w'),
                         ac(DOac, 'w'), ac(REac, 'w'), ac(SOLac, 'w'), ac(SOLac, 'w')],
                 bars_per_line=8),
            dict(num=4, titulo='Cruzar la mano por encima',
                 pista='la izquierda salta por encima de la derecha y toca arriba · mira antes de saltar',
                 events=[n('G5'), n('B5'), n('G5'), n('D5'),
                         n('B5'), n('G5'), n('D5'), n('B5'),
                         n('G5', 'w')],
                 bars_per_line=3),
            dict(num=5, titulo='Notas repetidas y agudas',
                 pista='la introducción · la misma nota picoteada arriba del todo, con dedos 3 · 2 · 1',
                 events=corch(['B5'] * 8) + corch(['A5'] * 8) +
                        corch(['G5'] * 8) + corch(['B5'] * 8),
                 bars_per_line=4),
            dict(num=6, titulo='Arpegio de Sol mayor · dos octavas', clef='bass',
                 pista='fundamental · 3ª · 5ª · 8ª · el acorde con el que empieza la canción',
                 events=corch(['G2', 'B2', 'D3', 'G3', 'B3', 'D4', 'G4', 'G4']) +
                        corch(['G4', 'D4', 'B3', 'G3', 'D3', 'B2', 'G2', 'G2']),
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con un sostenido. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Sol: todos los Fa son ♯',
        chuleta_clef='treble',
        chuleta_titulo='EL REGISTRO AGUDO DE LA INTRODUCCIÓN (CLAVE DE SOL)',
        chuleta_pitches=['G4', 'B4', 'D5', 'G5', 'B5', 'D6'],
        chuleta_nombres=['Sol', 'Si', 'Re', 'Sol', 'Si', 'Re'],
        ejercicios=[
            dict(num=1, titulo='Clave de Sol, registro alto',
                 pista='donde va la introducción · con líneas adicionales por arriba',
                 events=[n(p) for p in ('B5', 'G5', 'D6', 'A5', 'C6', 'F5', 'E6', 'B4',
                                        'D5', 'G6', 'A4', 'C5', 'F6', 'E5', 'B5', 'G5')]),
            dict(num=2, titulo='Clave de Fa', clef='bass',
                 pista='donde pica la izquierda en la estrofa · abajo del todo',
                 events=[n(p) for p in ('D2', 'A2', 'G2', 'D3', 'B2', 'E3', 'C3', 'F2',
                                        'G3', 'A3', 'E2', 'B3', 'C4', 'F3', 'D2', 'G2')]),
            dict(num=3, titulo='Leer el acorde de la izquierda', clef='bass',
                 pista='tres notas de golpe · nómbralas de abajo arriba, sin contar las líneas',
                 events=[ac(SOLac), ac(DOac), ac(REac), ac(MImac),
                         ac(DOac), ac(REac), ac(SOLac), ac(SOLac)],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca una nota PICADA o LIGADA. Que diga cuál era: la izquierda de esta canción '
                      'alterna las dos maneras.'),
                ('B', 'Toca dos acordes, uno con pedal y otro sin. Que diga en cuál lo has usado.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('+', 'Y sin escribir: toca una nota muy aguda y otra muy grave, y que diga cuál sonó '
                      'primero sin mirar.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Picada o ligada?', pista='la nota, corta o pegada a la siguiente',
                     n=10, opciones=['picada', 'ligada']),
                dict(letra='B', titulo='¿Con pedal o sin?', pista='el sonido sigue, o se corta',
                     n=8, opciones=['con', 'sin']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Lo que hace que el estribillo de esta canción suene a estribillo no es la melodía: es tu '
              'mano izquierda, que pasa de picar notas sueltas a repetir acordes. Por eso los dos '
              'primeros pasos son las dos izquierdas. No se citan números de compás: entre el segno, '
              'las casillas y la coda, el recuento no es fiable — se cita por SECCIÓN.',
        reglas=['SE CITA POR SECCIÓN, NO POR COMPÁS', 'PICADO ES CORTO, NO FUERTE', 'MIRA ANTES DE CRUZAR'],
        bloques=[
            dict(num=1, titulo='La izquierda de la estrofa: picada', clef='bass',
                 pista='estrofa medida · Re2 y La2 picados, con silencios entre medias',
                 sistemas=[
                     dict(cap='a) corto no quiere decir fuerte · la mano rebota y se va, no aprieta',
                          events=([n('D2', 'e'), sil('e'), n('A2', 'e'), sil('e')] * 2 +
                                  [n('D2', 'e'), sil('e'), n('A2', 'e'), sil('e')] * 2 +
                                  [n('D2', 'e'), sil('e'), n('A2', 'e'), sil('e')] * 2 +
                                  [n('D2', 'e'), sil('e'), n('A2', 'e'), sil('e')] * 2),
                          bars=4, clef='bass'),
                     dict(cap='b) la introducción, que es lo contrario: acordes largos abajo, con pedal',
                          events=[ac(SOLac, 'w'), ac(DOac, 'w'), ac(REac, 'w'), ac(SOLac, 'w')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y solo la nota grave de esos acordes, para oír por dónde va la '
                              'armonía · Sol · Do · Re · Sol',
                          events=[n('G2', 'w'), n('C3', 'w'), n('D3', 'w'), n('G2', 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='DOS IZQUIERDAS DISTINTAS EN LA MISMA CANCIÓN',
                 texto='Al principio la izquierda pica notas sueltas con silencios entre medias, y suena '
                       'hueca, casi nerviosa. Después pasa a acordes repetidos y la canción se llena de '
                       'golpe. Ese cambio de textura es lo que hace que el estribillo suene a estribillo. '
                       'Cuando llegues ahí, no toques más fuerte: toca más lleno.'),
            dict(num=2, titulo='La izquierda del estribillo: acordes', clef='bass',
                 pista='medido · Sol · Si · Re repetido en corcheas · aquí ya no pica: sostiene el pulso',
                 sistemas=[
                     dict(cap='a) ocho corcheas por compás sin acentuar ninguna · si marcas la primera, '
                              'suena a marcha',
                          events=[ac(SOLac, 'e')] * 8 + [ac(SOLac, 'e')] * 8 + [ac(SOLac, 'w')],
                          bars=3, clef='bass'),
                     dict(cap='b) y el acompañamiento entero del estribillo, cuatro compases seguidos',
                          events=[ac(DOac, 'e')] * 8 + [ac(REac, 'e')] * 8 +
                                 [ac(MImac, 'e')] * 8 + [ac(DOac, 'e')] * 8,
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ SIGNIFICA “8vb” Y “LH OVER RH”',
                 texto='El 8vb con línea de puntos debajo del pentagrama quiere decir que eso suena una '
                       'octava MÁS GRAVE de lo escrito, para no llenar la página de líneas adicionales. Y '
                       '“LH over RH” es literal: la izquierda pasa por encima de la derecha y toca '
                       'arriba. Practícalo despacio, mirando dónde pones cada mano.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Esta partitura tiene más señales de recorrido que ninguna otra del cuaderno, y todas hay '
              'que entenderlas antes de tocar. Después queda la melodía y el cruce de manos.',
        reglas=['PRIMERO EL RECORRIDO', 'EL CRUCE, DESPACIO Y MIRANDO', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='La melodía de la estrofa',
                 pista='estrofa medida · el ritmo va simplificado · es muy hablada: no la ligues',
                 sistemas=[
                     dict(cap='a) Re · Sol · Sol · Sol · Fa♯ · Mi · Re — sepárala igual que la voz',
                          events=corch(['D4', 'G4', 'G4', 'G4']) + [n('G4'), n('F4')] +
                                 corch(['E4', 'D4', 'B4', 'A4']) + [n('G4'), n('E4')],
                          bars=2),
                     dict(cap='b) y la frase que sube, que es la más larga de la estrofa · cántala '
                              'entera antes de tocarla, para saber dónde respira',
                          events=corch(['B4', 'A4', 'G4', 'G4']) + [n('E4'), n('B4')] +
                                 corch(['B4', 'A4', 'G4', 'E4']) + [n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=4, titulo='El cruce de manos, aislado',
                 pista='“LH over RH” · la izquierda salta al registro agudo mientras la derecha sigue',
                 sistemas=[
                     dict(cap='a) primero coloca la izquierda arriba sin tocar nada, cinco veces · '
                              'después ya toca',
                          events=[n('D6'), n('B5'), n('G5'), n('B5'),
                                  n('D6'), n('B5'), n('G5'), n('D5'),
                                  n('G5', 'w')],
                          bars=3),
                     dict(cap='b) y lo mismo en notas largas, para colocar el brazo antes de saltar · '
                              'el salto se prepara mirando, no de memoria',
                          events=[n('D6', 'h'), n('B5', 'h'), n('G5', 'h'), n('D5', 'h'),
                                  n('G5', 'w')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL RECORRIDO, PASO A PASO',
                 texto='1 · Cuatro compases de introducción. 2 · Empieza la estrofa: ahí está el SEGNO, '
                       'la marca a la que vas a volver. 3 · Llegas a la casilla 1.ª, la tocas y repites '
                       'desde el segno. 4 · La segunda vez te saltas la 1.ª y entras por la 2.ª. 5 · '
                       'Sigues hasta donde pone “To Coda” y desde ahí saltas al final. Y ojo con la nota '
                       'al pie: “D on the repeat” quiere decir que en la repetición una nota cambia a Re.'),
            dict(tipo='nota',
                 etiqueta='EL PEDAL, QUE AQUÍ VIENE ESCRITO',
                 texto='Es la única partitura del cuaderno donde el arreglista te dice dónde poner el '
                       'pedal. Aprovéchalo: en el resto tienes que decidirlo tú, y aquí puedes aprender '
                       'cómo se hace. La regla que vas a ver aplicada es siempre la misma: se pisa al '
                       'atacar y se cambia justo DESPUÉS de tocar el acorde nuevo. Si lo cambias antes, '
                       'se corta; si tardas de más, se emborrona.'),
            dict(tipo='escalera', valores=[60, 68, 76, 82, 88, 92],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
