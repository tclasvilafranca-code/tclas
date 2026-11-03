# -*- coding: utf-8 -*-
"""MAYO · Armaduras: Sol mayor y Fa mayor."""
from n1_base import *
from n1_comun import *

MES = 'Mayo'


def construir(d):
    d.nuevo('Mayo · Armaduras')
    d.add(banda_mes('Mayo', 'Etapa 3', 'Armaduras: Sol y Fa mayor',
                    'Cómo una alteración fija define la tonalidad: construcción de las escalas de Sol mayor y de Fa mayor.'))
    d.add(caja('dato', 'Tonalidad y armadura', [
        'Una **tonalidad** es el conjunto de notas y relaciones que organiza una pieza alrededor de una tónica. Para no repetir una alteración cada vez que aparece, se escribe una vez '
        'tras la clave: la **armadura**. Las alteraciones de la armadura valen **para todas las notas del mismo nombre, en todas las octavas y durante toda la pieza**.',
        'Una escala mayor siempre sigue la receta **T T S T T T S**. Empezando en otra nota que no sea Do, alguna nota natural no cumple la receta y hay que alterarla:',
        '▸ **Sol mayor** (tónica Sol): para que el séptimo grado esté a un semitono de la tónica, el Fa debe ser **Fa♯**. Armadura: **un sostenido (Fa♯)**.',
        '▸ **Fa mayor** (tónica Fa): para que el cuarto grado esté a un tono del tercero, el Si debe ser **Si♭**. Armadura: **un bemol (Si♭)**.',
        'Orden de las alteraciones: sostenidos **Fa – Do – Sol – Re – La – Mi – Si**; bemoles **Si – Mi – La – Re – Sol – Do – Fa** (el orden inverso).']),
        sistema('Do mayor: sin armadura', [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4']], alto=96, key_sig=None),
        sistema('Sol mayor: un sostenido en la armadura (Fa♯)', [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5']], alto=96, key_sig='Sol mayor'),
        sistema('Fa mayor: un bemol en la armadura (Si♭)', [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4']], alto=96, key_sig='Fa mayor'))
    d.add(ejercicio(1, 'Construir la escala',
                    ['Escribe en la tabla el tono (T) o semitono (S) entre las notas **naturales** de cada escala. Compara con la receta T T S T T T S y señala dónde no coincide: '
                     'ahí hay que alterar la nota.'],
                    'Deducir la armadura a partir de la estructura de la escala, en lugar de memorizarla.'))
    d.add(tabla([66, 66, 66, 66, 66, 66, 66, 29], [['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], ['T/S:', '', '', '', '', '', '', ''],
                                                    ['Receta', 'T', 'T', 'S', 'T', 'T', 'T', 'S']], None, alto=22, size=8.8, zebra=False))
    d.add(tabla([66, 66, 66, 66, 66, 66, 66, 29], [['Fa', 'Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa'], ['T/S:', '', '', '', '', '', '', ''],
                                                    ['Receta', 'T', 'T', 'S', 'T', 'T', 'T', 'S']], None, alto=22, size=8.8, zebra=False))
    sol(MES, 1, 'Construir la escala',
        ['Sol mayor con notas naturales: T T S T T S T → no coincide en los dos últimos intervalos: hay que subir el Fa (Fa♯) para que Mi–Fa♯ sea T y Fa♯–Sol sea S.',
         'Fa mayor con notas naturales: T T T S T T S → no coincide en los intervalos tercero y cuarto: hay que bajar el Si (Si♭) para que La–Si♭ sea S y Si♭–Do sea T.'])
    d.add(ejercicio(2, 'Escribir las escalas con alteraciones',
                    ['Completa cada escala escribiendo **a mano** las alteraciones donde hagan falta (sin armadura). Después, nombra la alteración que has necesitado.'],
                    'Comprobar que cada escala mayor necesita exactamente las alteraciones que predice su estructura.'))
    d.add(fila_notas('treble', ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5'], 'q', bajo='nada', titulo='a) Sol mayor (¿qué nota hay que alterar?)', barras=4),
          fila_notas('treble', ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'], 'q', bajo='nada', titulo='b) Fa mayor (¿qué nota hay que alterar?)', barras=4))
    sol(MES, 2, 'Escribir las escalas', ['a) Fa♯ (7.º grado).  b) Si♭ (4.º grado).'])
    d.add(ejercicio(3, 'Identificar la tonalidad',
                    ['Escribe la tonalidad (Do, Sol o Fa mayor) de cada armadura.'],
                    'Reconocer una tonalidad al primer vistazo.'))
    sig = ['Fa mayor', 'Do mayor', 'Sol mayor', 'Fa mayor']
    for k, kn in enumerate(sig):
        d.add(sistema('%s) Tonalidad: ____________' % SEC[k], [{'rest': True, 'dur': 'w'}], alto=86, key_sig=None if kn == 'Do mayor' else kn))
    sol(MES, 3, 'Identificar la tonalidad', ['  ·  '.join('%s) %s' % (SEC[k], kn) for k, kn in enumerate(sig))])

    # ---- al piano
    d.add(caja('piano', 'Al piano: escalas de Sol y de Fa mayor', [
        'La digitación de **Sol mayor** es la misma que la de Do mayor en las dos manos. En **Fa mayor** la mano derecha usa **1 2 3 4 1 2 3 4** (el pulgar pasa por debajo tras el 4, '
        'que toca el Si♭, para tocar el Do) y la izquierda **5 4 3 2 1 3 2 1**.']))
    g_d = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5']
    f_d = ['F4', 'G4', 'A4', 'Bb4', 'C5', 'D5', 'E5', 'F5']
    d.add(sistema('Sol mayor · mano derecha', [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(g_d, [1, 2, 3, 1, 2, 3, 4, 5])], key_sig='Sol mayor', alto=112),
          sistema('Fa mayor · mano derecha', [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(f_d, [1, 2, 3, 4, 1, 2, 3, 4])], key_sig='Fa mayor', alto=112))
    g_i = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F#3', 'G3']
    f_i = ['F2', 'G2', 'A2', 'Bb2', 'C3', 'D3', 'E3', 'F3']
    d.add(sistema('Sol mayor · mano izquierda', [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(g_i, [5, 4, 3, 2, 1, 3, 2, 1])], clef='bass', key_sig='Sol mayor', alto=112),
          sistema('Fa mayor · mano izquierda', [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(f_i, [5, 4, 3, 2, 1, 3, 2, 1])], clef='bass', key_sig='Fa mayor', alto=112))
    d.add(caja('piano', 'Minueto en Sol · C. Petzold (antes atribuido a J. S. Bach)', [
        'Primera frase, mano derecha. Antes de tocar, analiza: tonalidad, compás y dónde aparece el Fa♯. La digitación es libre: busca la posición de la mano que evite saltos.']))
    mn = [{'pitch': 'D5', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'B4', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'},
          {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'},
          {'pitch': 'E5', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'D5', 'dur': 'e'}, {'pitch': 'E5', 'dur': 'e'}, {'pitch': 'F#5', 'dur': 'e'},
          {'pitch': 'G5', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}]
    d.add(sistema('Minueto en Sol · primera frase', mn, ts=(3, 4), key_sig='Sol mayor', alto=118))
    d.add(ejercicio(4, 'Análisis del Minueto',
                    ['Contesta sobre la partitura.'], 'Preparar una pieza analizándola antes de tocarla.'))
    d.add(tabla([260, 231], [['Tonalidad y armadura', ''], ['Cifra de compás y tiempos por compás', ''], ['Figura de menor duración', ''],
                              ['Nota alterada que aparece en la frase', ''], ['Nota más aguda y más grave', '']], ['Pregunta', 'Respuesta'], alto=26, alin=['l', 'l'], size=9))
    sol(MES, 4, 'Análisis del Minueto', ['Sol mayor (un sostenido, Fa♯) · 3/4, tres tiempos · corchea · Fa♯ (compás 3) · más aguda Sol5, más grave Sol4.'])
    sol(MES, 'Al piano', 'Escalas de Sol y Fa', ['Sol mayor: Sol La Si Do Re Mi Fa♯ Sol. Fa mayor: Fa Sol La Si♭ Do Re Mi Fa. Minueto: Re5 · Sol4 La4 Si4 Do5 · Re5 Sol4 Sol4 · Mi5 Do5 Re5 Mi5 Fa♯5 · Sol5 Sol4 Sol4.'])
