# -*- coding: utf-8 -*-
"""Santa Tell Me (canción 14 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico); el material medido se
   importa de `dilan_19_santa`. Ver TRANSCRIPCION_D18_20.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por las MANOS —la izquierda picada, la del
       estribillo, el cruce— y el recorrido de la hoja llega al final, como
       aviso.
     - A Eva el recorrido es el PASO 1, y se hace sin piano y con un lápiz.
       Esta pieza está en su álbum por una razón concreta: es la partitura con
       más señales de navegación de todo el cuaderno (segno, casillas 1.ª y
       2.ª, To Coda, 8vb, «LH over RH» y una nota al pie que cambia una nota en
       la repetición). Aquí el problema no es tocar: es saber por dónde vas. Y
       eso no se resuelve tocando más veces, se resuelve leyendo la hoja una
       vez, despacio, antes de tocar nada.

   NO se cita el total de compases: el lector cuenta 13 y es claramente menos
   de lo que hay (los silencios y el picado le rompen la detección de barras).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_19_santa import (n, ac, sil, corch, SOLac, DOac, REac, MImac)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

PICADO = [n('D2', 'e'), sil('e'), n('A2', 'e'), sil('e')]

CANCION = dict(
    alumno='Eva', num=14, nivel='avanzado', slug='SantaTellMe',
    titulo_corto='Santa Tell Me', time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'Santa-tell-me-ariana-grande.pdf'),
    yt='https://www.youtube.com/results?search_query=ariana+grande+santa+tell+me',

    ficha=dict(
        titulo='Santa Tell Me',
        autor='Ariana Grande (2014) · arr. Sadie King',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'), ('Extras', 'Segno · coda · 8vb'),
               ('Mano izq.', 'De dos formas'), ('Especial', 'Cruce de manos')],
        armonia=dict(
            titulo='La partitura con más señales de todo el cuaderno',
            tarjetas=[
                ('EL RECORRIDO', 'Segno y coda',
                 'No se toca de arriba abajo: se salta. Hay que leerlo antes, con un lápiz.'),
                ('DOS IZQUIERDAS', 'Picada y sostenida',
                 'En la estrofa pica notas sueltas; en el estribillo sostiene corcheas seguidas.'),
                ('LH OVER RH', 'La izquierda cruza',
                 'En el c. 4 la izquierda salta por encima de la derecha, al registro agudo.'),
                ('EL PEDAL', 'Viene escrito',
                 'Es la única partitura del álbum donde el arreglista te dice dónde ponerlo.'),
            ],
            pie='Las notas de esta canción no son difíciles. Lo difícil es orientarse: si te equivocas '
                'de casilla o te saltas la coda, da igual lo bien que toques, porque no estás tocando '
                'la canción. Por eso aquí el paso 1 se hace sin piano.',
        ),
        ritmos=[
            ('MI · estrofa', 'picada: corta y suelta, con silencios entre medias',
             PICADO + [n('D2', 'q'), n('A2', 'q')], OCRE, 'bass', SOL),
            ('MI · estribillo', 'y aquí lo contrario: corcheas seguidas sin acentuar',
             [ac(SOLac, 'e')] * 4 + [ac(SOLac, 'q')] * 2, OCRE, 'bass', SOL),
        ],
        especial=[
            'Armadura de un sostenido: todos los Fa son ♯.',
            'Hay un SEGNO, casillas 1.ª y 2.ª, y un “To Coda”.',
            'Hay un 8vb en la izquierda de la introducción: suena una octava más abajo.',
            'En el c. 4 pone “LH over RH”: la izquierda cruza por encima de la derecha.',
            'El pedal viene escrito por el arreglista, cosa que no pasa en ninguna otra.',
            'Una nota al pie avisa de que en la repetición cambia una nota.',
        ],
        reto='Orientarse. Esta hoja no se lee de arriba abajo: hay que saltar al segno, elegir casilla y '
             'salir por la coda. Y todo eso mientras tocas, que es cuando peor se piensa.',
        truco='Antes de tocar una sola nota, sigue la partitura con el dedo y di el recorrido en voz '
              'alta: “intro, segno, casilla uno, vuelvo al segno, casilla dos, to coda, final”. Cinco '
              'minutos. Después márcalo a lápiz con flechas. Es el trabajo más rentable de esta pieza y '
              'no requiere piano.',
        sabias='La canción es de 2014 y Ariana Grande la escribió con el mismo equipo que le hacía los '
               'temas de pop de verano: por eso es un villancico que suena a canción de radio, con la '
               'batería marcando y todo. Es de las pocas navideñas modernas que se han quedado.',
        qr=dict(titulo='Escucha la original',
                texto='Escucha dónde vuelve a empezar la canción. Ese sitio es el segno.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='El paso 1 de esta canción se hace sin piano y con un lápiz en la mano. Es la partitura '
              'con más señales de navegación del cuaderno, y si el recorrido no está claro, tocarla más '
              'veces no arregla nada: solo aprendes a perderte más rápido.',
        reglas=['PRIMERO EL RECORRIDO, Y SIN PIANO', 'PICADO NO ES FUERTE', 'DESPACIO'],
        bloques=[
            dict(num=1, titulo='Lee la hoja antes de tocarla',
                 pista='sin piano y con lápiz · cinco minutos que te ahorran tres semanas',
                 sistemas=[]),
            dict(tipo='nota',
                 etiqueta='EL RECORRIDO, PASO A PASO',
                 texto='1 · Cuatro compases de introducción. 2 · Empieza la estrofa: ahí está el SEGNO, '
                       'la marca a la que vas a volver. 3 · Llegas a la casilla 1.ª, la tocas y repites '
                       'desde el segno. 4 · La segunda vez te saltas la 1.ª y entras por la 2.ª. 5 · '
                       'Sigues hasta donde pone “To Coda” y desde ahí saltas al final. Ojo con la nota '
                       'al pie: “D on the repeat” quiere decir que en la repetición una nota cambia a '
                       'Re. Sigue todo eso con el dedo, dilo en voz alta y márcalo con flechas a lápiz.'),
            dict(num=2, titulo='Las dos izquierdas de esta canción', clef='bass',
                 pista='medidas las dos · en la estrofa pica y en el estribillo sostiene: son dos '
                       'maneras de tocar distintas, no dos volúmenes',
                 sistemas=[
                     dict(cap='a) la estrofa · Re2 y La2 picados, con silencios entre medias: corto no '
                              'quiere decir fuerte, la mano rebota y se va',
                          events=PICADO * 8, bars=4, clef='bass'),
                     dict(cap='b) el estribillo · ocho corcheas por compás sin acentuar ninguna: si '
                              'marcas la primera, esto suena a marcha',
                          events=[ac(SOLac, 'e')] * 8 + [ac(SOLac, 'e')] * 8 + [ac(SOLac, 'w')],
                          staccato=True,
                          bars=3, clef='bass', show_time=False),
                     dict(cap='c) y la introducción, que es la tercera manera: acordes largos abajo, '
                              'con el pedal que la partitura te escribe',
                          events=[ac(SOLac, 'w'), ac(DOac, 'w'), ac(REac, 'w'), ac(SOLac, 'w')],
                          pedal=4,
                          bars=4, clef='bass', show_time=False),
                     dict(cap='d) y solo la nota grave de esos acordes · Sol · Do · Re · Sol: por ahí '
                              'va la armonía de la introducción, y son cuatro notas',
                          events=[n('G2', 'w'), n('C3', 'w'), n('D3', 'w'), n('G2', 'w')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='e) el acompañamiento entero del estribillo, cuatro compases seguidos · '
                              'aquí se ve si el pulso aguanta cuando cambia el acorde',
                          events=[ac(DOac, 'e')] * 8 + [ac(REac, 'e')] * 8 +
                                 [ac(MImac, 'e')] * 8 + [ac(DOac, 'e')] * 8,
                          bars=2, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Con el recorrido claro y las dos izquierdas montadas, lo que queda son dos cosas '
              'concretas: la melodía de la estrofa, que es muy hablada, y el cruce de manos del c. 4, '
              'que se prepara mirando y no de memoria.',
        reglas=['LA MELODÍA, SEPARADA COMO LA VOZ', 'EL CRUCE SE MIRA', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='La melodía de la estrofa',
                 pista='estrofa medida · el ritmo va simplificado · es muy hablada: no la ligues',
                 sistemas=[
                     dict(cap='a) Re · Sol · Sol · Sol · Fa♯ · Mi · Re — sepárala igual que la voz',
                          events=corch(['D4', 'G4', 'G4', 'G4']) + [n('G4'), n('F4')] +
                                 corch(['E4', 'D4', 'D4', 'D4']) + [n('D4', 'h')],
                          bars=2),
                     dict(cap='b) y la frase que sube, que es la más larga de la estrofa · cántala '
                              'entera antes de tocarla, para saber dónde respira',
                          events=corch(['B4', 'A4', 'G4', 'G4']) + [n('E4'), n('B4')] +
                                 corch(['B4', 'A4', 'G4', 'E4']) + [n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ SIGNIFICAN “8vb” Y “LH OVER RH”',
                 texto='8vb sobre la izquierda de la introducción quiere decir que esas notas suenan una '
                       'octava MÁS ABAJO de donde están escritas: se escribe así para no llenar la hoja '
                       'de líneas adicionales. Y “LH over RH” en el c. 4 quiere decir que la mano '
                       'izquierda pasa por ENCIMA de la derecha para tocar en el registro agudo. Las dos '
                       'cosas son instrucciones del arreglista, no adornos: si no las haces, la canción '
                       'suena en el sitio equivocado.'),
            dict(num=4, titulo='El cruce de manos, aislado',
                 pista='“LH over RH” del c. 4 · las notas del salto son andamio en Sol mayor',
                 sistemas=[
                     # Igual que en el cuaderno de Dilan: el cruce va en semicorcheas
                     # y aqui se escribia en negras.
                     dict(cap='a) la bajada del cruce, con su figura: SEMICORCHEAS · coloca primero la '
                              'izquierda arriba sin tocar, cinco veces, y después ya toca',
                          events=[{'pitch': 'G5', 'dur': 's', 'beam': 9520}, {'pitch': 'A5', 'dur': 's', 'beam': 9520}, {'pitch': 'B5', 'dur': 's', 'beam': 9520}, {'pitch': 'D6', 'dur': 's', 'beam': 9520}, {'pitch': 'B5', 'dur': 's', 'beam': 9521}, {'pitch': 'G5', 'dur': 's', 'beam': 9521}, {'pitch': 'D5', 'dur': 's', 'beam': 9521}, {'pitch': 'G5', 'dur': 's', 'beam': 9521}, {'pitch': 'B5', 'dur': 's', 'beam': 9522}, {'pitch': 'D6', 'dur': 's', 'beam': 9522}, {'pitch': 'B5', 'dur': 's', 'beam': 9522}, {'pitch': 'G5', 'dur': 's', 'beam': 9522}, {'pitch': 'D5', 'dur': 's', 'beam': 9523}, {'pitch': 'G5', 'dur': 's', 'beam': 9523}, {'pitch': 'B5', 'dur': 's', 'beam': 9523}, {'pitch': 'D6', 'dur': 's', 'beam': 9523}],
                          bars=1),
                     dict(cap='b) y lo mismo en notas largas, para colocar el brazo antes de saltar · '
                              'el salto se prepara mirando, no de memoria',
                          events=[n('B5', 'h'), n('G5', 'h'), n('D6', 'h'), n('B5', 'h'),
                                  n('G5', 'w')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL PEDAL, QUE AQUÍ TE LO ESCRIBEN',
                 texto='Es la única partitura del cuaderno donde el arreglista te dice dónde poner el '
                       'pedal y dónde soltarlo. Hazle caso literalmente antes de decidir nada por tu '
                       'cuenta: lo pide en los acordes largos de la introducción y en los finales de '
                       'frase, y NO lo pide en los compases picados de la estrofa — ahí se comería el '
                       'picado, que es lo único que hace que esa parte suene a lo que suena.'),
            dict(tipo='escalera', valores=[52, 60, 68, 76, 84, 92],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
