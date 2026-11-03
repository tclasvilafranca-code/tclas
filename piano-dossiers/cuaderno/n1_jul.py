# -*- coding: utf-8 -*-
"""JULIO · Expresion, repaso y recital."""
from n1_base import *
from n1_comun import *

MES = 'Julio'

TEST = [
    ('Noviembre', 'Una octava del teclado (de un Do al siguiente) tiene…', ['8 teclas blancas y 4 negras', '7 teclas blancas y 5 negras', '6 teclas blancas y 6 negras'], 'B'),
    ('Noviembre', 'En clave de sol, la 2.ª línea es Sol.', None, 'Verdadero'),
    ('Diciembre', 'La figura de mayor duración es la…', ['redonda', 'blanca', 'semifusa'], 'A'),
    ('Diciembre', 'En un compás de 3/4 caben…', ['tres negras', 'cuatro negras', 'tres blancas'], 'A'),
    ('Diciembre', 'Una blanca con puntillo dura 3 tiempos.', None, 'Verdadero'),
    ('Enero', 'En clave de sol, el Do central se escribe…', ['en la 1.ª línea adicional inferior', 'en la 3.ª línea', 'en la 1.ª línea adicional superior'], 'A'),
    ('Enero', 'Las líneas adicionales solo pueden ir por encima del pentagrama.', None, 'Falso'),
    ('Febrero', 'La escala de Do mayor completa tiene…', ['6 tonos y 1 semitono', '5 tonos y 2 semitonos', '7 tonos'], 'B'),
    ('Febrero', 'Do♯ y Re♭ son la misma tecla.', None, 'Verdadero'),
    ('Marzo', '¿Cuántas semicorcheas caben en una negra?', ['2', '4', '8'], 'B'),
    ('Marzo', 'La ligadura de prolongación une dos notas de sonido distinto y suma sus tiempos.', None, 'Falso'),
    ('Abril', 'La clave de fa se coloca sobre…', ['la 2.ª línea', 'la 4.ª línea', 'la 5.ª línea'], 'B'),
    ('Abril', 'En clave de fa, la nota de la 1.ª línea es…', ['Mi', 'Sol', 'La'], 'B'),
    ('Mayo', 'La armadura de Sol mayor lleva…', ['Fa♯', 'Si♭', 'Do♯'], 'A'),
    ('Mayo', 'Una alteración de la armadura afecta a esa nota en todas las octavas.', None, 'Verdadero'),
    ('Junio', 'La tríada de Do mayor se compone de…', ['Do – Mi – Sol', 'Do – Re – Mi', 'Do – Fa – Sol'], 'A'),
    ('Junio', 'En Do mayor, la cadencia I – IV – V – I es…', ['C – G – F – C', 'C – F – G – C', 'C – Am – Dm – C'], 'B'),
    ('Julio', 'La indicación f (forte) significa…', ['suave', 'fuerte', 'cada vez más rápido'], 'B'),
    ('Julio', 'Staccato indica tocar las notas cortas y separadas.', None, 'Verdadero'),
]


def construir(d):
    d.nuevo('Julio · Expresión y repaso')
    d.add(banda_mes('Julio', 'Etapa 3', 'Expresión y repaso final',
                    'Dinámica, tempo y articulación: lo que convierte la lectura correcta en interpretación. Revisión del curso y preparación del recital.'))
    d.add(caja('dato', 'Dinámica, tempo y articulación', [
        'La partitura indica no solo qué notas tocar y cuánto duran, sino **cómo**. Las tres familias de indicaciones principales:',
        '▸ **Dinámica** (intensidad): **pp** pianissimo (muy suave) · **p** piano (suave) · **mp** mezzopiano · **mf** mezzoforte · **f** forte (fuerte) · **ff** fortissimo (muy fuerte). '
        'Un **crescendo** (cresc.) va aumentando la intensidad; un **diminuendo** (dim.), disminuyéndola.',
        '▸ **Articulación**: **legato** (ligadura: unir las notas sin cortar el sonido), **staccato** (punto sobre la nota: corta y separada), **acento** (>: atacar con más intensidad) '
        'y **tenuto** (–: mantener el valor completo).']),
        tabla([110, 211, 170], [['Largo', 'muy lento', '♩ ≈ 40–60'], ['Adagio', 'lento', '♩ ≈ 66–76'], ['Andante', 'a paso tranquilo', '♩ ≈ 76–108'],
                                ['Moderato', 'moderado', '♩ ≈ 108–120'], ['Allegro', 'rápido y vivo', '♩ ≈ 120–156'], ['Presto', 'muy rápido', '♩ ≈ 168–200']],
              ['Tempo (italiano)', 'Carácter', 'Pulsos por minuto (orientativo)'], alto=19, size=8.8),
        par('Los términos italianos de tempo indican un carácter más que una cifra exacta: los valores del metrónomo son orientativos y varían según la fuente. '
            'Cuando hay una cifra escrita (♩ = 60), manda la cifra.', 8.8, MUTED))
    mt = [{'pitch': 'C4', 'dur': 'q', 'matiz': 'p', 'art': 'staccato'}, {'pitch': 'E4', 'dur': 'q', 'art': 'staccato'}, {'pitch': 'G4', 'dur': 'q', 'art': 'staccato'},
          {'pitch': 'E4', 'dur': 'q', 'art': 'staccato'}, {'pitch': 'C5', 'dur': 'h', 'matiz': 'f', 'art': 'acento'}, {'pitch': 'G4', 'dur': 'h'}]
    d.add(sistema('Ejemplo: p con staccato, después f con acento', mt, alto=118))
    d.add(ejercicio(1, 'Interpretar los signos',
                    ['Observa el fragmento de arriba y contesta. Después tócalo en el piano respetando los signos.'],
                    'Leer las indicaciones de expresión con la misma atención que las notas.'))
    d.add(tabla([300, 191], [['Intensidad con la que empieza', ''], ['Cómo se articulan las cuatro primeras notas', ''], ['Qué cambia en la nota Do5', ''],
                              ['Cifra de compás y tiempos por compás', '']], ['Pregunta', 'Respuesta'], alto=26, alin=['l', 'l'], size=9))
    sol(MES, 1, 'Interpretar los signos', ['p (piano, suave) · staccato (cortas y separadas) · f (forte) y acento (se ataca con más intensidad) · 4/4, cuatro tiempos.'])
    d.add(ejercicio(2, 'Añadir expresión',
                    ['Copia en el pentagrama la frase de Au clair de la lune (Do Do Do Re · Mi Re · Do Mi Re Re · Do) y añade **dos matices, un crescendo y una articulación** de tu elección. '
                     'Después tócala interpretándola y anota qué efecto buscabas.'],
                    'Decidir la expresión de una frase en lugar de tocarla en un único plano sonoro.'))
    d.add(pauta_vacia('treble', 4, (4, 4), titulo='Mi interpretación'), lineas_escribir(2, 'Qué efecto buscaba:', 20))
    sol(MES, 2, 'Añadir expresión', ['Ejercicio libre. Criterio: los matices y el crescendo van bajo el pentagrama y la articulación junto a la cabeza de las notas.'])

    # ---- repaso
    d.add(caja('tip', 'Método de estudio: aislar, reducir, reinsertar', [
        '▸ **Aísla** el pasaje difícil (uno o dos compases) y estúdialo solo, no la pieza entera.',
        '▸ **Reduce** la dificultad: manos separadas, más lento, solo el ritmo, solo con una nota.',
        '▸ **Reinserta**: vuelve a tocar desde unos compases antes hasta unos compases después, con las dos manos.',
        '▸ **Toca de seguido**: la pieza entera, sin parar aunque falles, como en un concierto; después corrige lo que ha fallado.']))
    d.add(ejercicio(3, 'Revisión del curso',
                    ['Responde a las preguntas de cada mes. En las de **A/B/C** rodea la correcta; en las de **V/F**, marca verdadero o falso. Hazlo sin ayuda y corrige después con el solucionario.'],
                    'Comprobar qué conceptos están consolidados y cuáles hay que repasar.'))
    actual = None
    ans = []
    for i, (mes, preg, ops, resp) in enumerate(TEST):
        if mes != actual:
            actual = mes
            d.add(h2(mes))
        if ops:
            t = '**%d.** %s\n   A) %s     B) %s     C) %s' % (i + 1, preg, ops[0], ops[1], ops[2])
        else:
            t = '**%d.** %s     ☐ Verdadero    ☐ Falso' % (i + 1, preg)
        d.add(par(t, 9.0, INK, despues=3))
        ans.append('%d) %s' % (i + 1, resp))
    sol(MES, 3, 'Revisión del curso', ['  ·  '.join(ans)])

    # ---- recital y autoevaluacion
    d.nuevo()
    d.add(ejercicio(4, 'Programa del recital',
                    ['Elige tres piezas del curso (o de tu repertorio) para tocarlas de seguido. Anota título, autor, tonalidad y compás, y señala el aspecto técnico que más has trabajado en cada una.'],
                    'Preparar una pequeña actuación, la mejor forma de consolidar lo aprendido.'))
    d.add(tabla([30, 150, 100, 100, 111], [['1', '', '', '', ''], ['2', '', '', '', ''], ['3', '', '', '', '']], ['N.º', 'Título y autor', 'Tonalidad', 'Compás', 'Aspecto trabajado'], alto=32, size=9))
    d.add(ejercicio(5, 'Autoevaluación del curso',
                    ['Valora de 1 (me cuesta) a 5 (lo domino) cada bloque, y escribe un objetivo concreto para el próximo curso.'],
                    'Cerrar el curso con un diagnóstico propio y un plan para el siguiente.'))
    temas = ['Lectura en clave de sol', 'Lectura en clave de fa', 'Figuras, silencios y compases', 'Escalas y armaduras', 'Intervalos y acordes', 'Manos juntas y coordinación', 'Expresión e interpretación']
    d.add(tabla([260, 46, 46, 46, 46, 47], [[t, '1', '2', '3', '4', '5'] for t in temas], ['Aspecto', '', '', '', '', ''], alto=22, size=8.8, alin=['l', 'c', 'c', 'c', 'c', 'c']))
    d.add(lineas_escribir(3, 'Mis objetivos para el próximo curso:', 21))
    sol(MES, 4, 'Programa del recital', ['Ejercicio personal.'])
    sol(MES, 5, 'Autoevaluación', ['Ejercicio personal: los bloques con 1–2 se repasan con los ejercicios del mes correspondiente.'])
