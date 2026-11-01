# -*- coding: utf-8 -*-
"""JUNIO · Repaso final y gran concierto."""
from n1_base import *
from reportlab.lib.colors import HexColor

MES = 'Junio'

# (mes, pregunta, opciones | None si verdadero/falso, respuesta)
TEST = [
    ('Septiembre', '¿Cuál de estas figuras dura menos que la negra?', ['Corchea', 'Blanca', 'Redonda'], 'A'),
    ('Septiembre', 'La blanca dura la mitad que la redonda.', None, 'Verdadero'),
    ('Octubre', 'En clave de sol, el Do central se escribe…', ['en la 1.ª línea adicional inferior', 'en la 3.ª línea', 'en la 1.ª línea adicional superior'], 'A'),
    ('Octubre', 'Las líneas adicionales solo pueden ir por encima del pentagrama.', None, 'Falso'),
    ('Noviembre', 'Una octava del teclado (de un Do al siguiente) tiene…', ['8 teclas blancas y 4 negras', '7 teclas blancas y 5 negras', '6 teclas blancas y 6 negras'], 'B'),
    ('Noviembre', 'Entre Mi y Fa hay una tecla negra.', None, 'Falso'),
    ('Diciembre', 'La escala de Do mayor completa tiene…', ['6 tonos y 1 semitono', '5 tonos y 2 semitonos', '7 tonos'], 'B'),
    ('Diciembre', 'En la escala de Do mayor los semitonos están entre Mi–Fa y Si–Do.', None, 'Verdadero'),
    ('Enero', 'En un compás de 3/4 caben…', ['tres negras', 'cuatro negras', 'tres blancas'], 'A'),
    ('Enero', 'Un compás de 2/4 puede llenarse con una sola blanca.', None, 'Verdadero'),
    ('Febrero', '¿Cuántas semicorcheas caben en una negra?', ['2', '4', '8'], 'B'),
    ('Febrero', 'Dos corcheas duran lo mismo que una negra.', None, 'Verdadero'),
    ('Marzo', 'La clave de fa se coloca sobre…', ['la 2.ª línea', 'la 4.ª línea', 'la 5.ª línea'], 'B'),
    ('Marzo', 'En clave de fa, la nota de la 1.ª línea es…', ['Mi', 'Sol', 'La'], 'B'),
    ('Abril', 'El silencio de blanca se coloca…', ['colgado de la 4.ª línea', 'apoyado en la 3.ª línea', 'en el 1.er espacio'], 'B'),
    ('Abril', 'En un compás de 4/4, un silencio de blanca, un silencio de negra y una negra lo completan.', None, 'Verdadero'),
    ('Mayo', 'Una blanca con puntillo dura…', ['2 tiempos', '3 tiempos', '4 tiempos'], 'B'),
    ('Mayo', 'La ligadura de prolongación une dos notas de sonido distinto y suma sus tiempos.', None, 'Falso'),
    ('Repaso', 'La nota de la que parte una escala se llama…', ['tónica', 'sensible', 'dominante'], 'A'),
    ('Repaso', 'En clave de sol, la 2.ª línea es Sol.', None, 'Verdadero'),
]


def diploma():
    h = 330

    def f(c, x, y, w):
        c.setStrokeColor(NAVY)
        c.setLineWidth(2.2)
        c.roundRect(x, y - h, w, h, 8, fill=0, stroke=1)
        c.setStrokeColor(OCRE)
        c.setLineWidth(0.9)
        c.roundRect(x + 8, y - h + 8, w - 16, h - 16, 5, fill=0, stroke=1)
        c.setFillColor(OCRE)
        c.setFont('DejaVuSans-Bold', 8.4)
        c.drawCentredString(x + w / 2, y - 42, 'T-CLAS  ·  EL CUADERNO DEL PIANISTA')
        c.setFillColor(NAVY)
        c.setFont('DejaVuSerif-Bold', 30)
        c.drawCentredString(x + w / 2, y - 92, 'Diploma')
        c.setFont('DejaVuSerif', 12)
        c.drawCentredString(x + w / 2, y - 120, 'de Explorador / Exploradora Musical · Nivel 1')
        c.setFont('DejaVuSans', 9.4)
        c.setFillColor(INK)
        c.drawCentredString(x + w / 2, y - 156, 'Se concede el presente diploma a')
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.8)
        c.line(x + 80, y - 188, x + w - 80, y - 188)
        c.drawCentredString(x + w / 2, y - 220, 'por haber completado el curso 2026/27: notación, teclado, escala de Do mayor,')
        c.drawCentredString(x + w / 2, y - 234, 'compases, ritmo, clave de fa, silencios, ligadura y puntillo.')
        c.line(x + 60, y - 290, x + 190, y - 290)
        c.line(x + w - 190, y - 290, x + w - 60, y - 290)
        c.setFont('DejaVuSans', 7.6)
        c.setFillColor(MUTED)
        c.drawCentredString(x + 125, y - 302, 'Fecha')
        c.drawCentredString(x + w - 125, y - 302, 'El / la profesor(a)')
    return Blk(h + 8, f)


def marco_libre(titulo, alto):
    def f(c, x, y, w):
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.9)
        c.setDash(3, 3)
        c.roundRect(x, y - alto, w, alto, 6, fill=0, stroke=1)
        c.setDash()
        c.setFont('DejaVuSans-Bold', 8)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x + 10, y - 14, titulo)
    return Blk(alto + 8, f)


def construir(d):
    d.nuevo('Junio · Repaso final y gran concierto')
    d.add(banda_mes('Junio', '3.er trimestre', 'Repaso final y gran concierto',
                    'Mirar atrás todo lo aprendido, prepararse para tocar delante de otros y celebrarlo.'))
    d.add(caja('dato', '¡Llegó el final del curso!', [
        'Este mes **repasamos** lo aprendido, preparamos un **pequeño concierto**, demostramos nuestra creatividad y compartimos el trabajo con los compañeros. '
        'Es el momento de mostrar todo lo que sabes.']))
    d.add(ejercicio(1, 'Me aprendo mi partitura',
                    ['Elige **una pieza** trabajada durante el curso (puede ser el Himno de la Alegría o cualquiera de tu clase). Repásala y practícala con el método de abajo. '
                     'Si quieres un reto, busca la misma pieza **en otra tonalidad**.',
                     'Anota a la derecha el título, el compositor y la fecha del concierto.'],
                    'Desarrollar la autonomía musical, la memoria auditiva y la expresividad.'))
    d.add(lineas_escribir(1, 'Título y autor: ________________________________________________      Fecha del concierto: ____ / ____ / ______', 20))
    d.add(h2('Mi método de estudio en cuatro pasos'))
    d.add(tabla([30, 120, 341], [
        ['1', '**Aísla**', 'Marca los pasajes difíciles y estudia **solo ese trozo** (dos o cuatro compases), no la pieza entera.'],
        ['2', '**Reduce**', 'Hazlo más fácil: **manos separadas**, más despacio, solo el ritmo, solo con una nota…'],
        ['3', '**Reinserta**', 'Vuelve a **ponerlo en su sitio**: toca desde unos compases antes hasta unos compases después, con las dos manos.'],
        ['4', '**Toca de seguido**', 'Una vez entera, **sin parar** aunque te equivoques, como en el concierto. Después, corrige lo que falló.'],
    ], None, alto=36, zebra=True, size=9.2, alin=['c', 'l', 'l']))
    d.add(casillas(['Sé dónde están los compases difíciles.', 'Toco la mano derecha de memoria.', 'Toco la mano izquierda de memoria.',
                    'La toco entera sin parar.', 'Cuento los silencios y respeto los puntillos.', 'La toco delante de alguien.'], cols=2))
    sol(MES, 1, 'Me aprendo mi partitura', ['Ejercicio personal: se valora seguir los cuatro pasos y tocar sin detenerse.'])

    d.add(ejercicio(2, 'Test musical de repaso',
                    ['Responde a las preguntas de cada mes. En las de **A/B/C** rodea la correcta; en las de **V/F**, marca si es verdadero o falso.',
                     'Hazlo sin ayuda; luego mira las soluciones al final del cuaderno.'],
                    'Repasar los conceptos básicos de teoría musical de forma autónoma.'))
    actual = None
    ans = []
    for i, (mes, preg, ops, resp) in enumerate(TEST):
        if mes != actual:
            actual = mes
            d.add(h2(mes))
        if ops:
            txt = '**%d.** %s\n   A) %s     B) %s     C) %s' % (i + 1, preg, ops[0], ops[1], ops[2])
        else:
            txt = '**%d.** %s     ☐ Verdadero    ☐ Falso' % (i + 1, preg)
        d.add(par(txt, 9.0, INK, despues=3, sangria=0))
        ans.append('%d) %s' % (i + 1, resp))
    sol(MES, 2, 'Test musical de repaso', ['  ·  '.join(ans)])

    d.add(ejercicio(3, 'Concurso de dibujo musical',
                    ['Tienes una semana para hacer tu mejor **dibujo musical**: instrumentos, notas con colores, una escena de un concierto o de una clase… Usa los recursos que quieras: cartulinas, hojas de colores, pergaminos, pinturas…'],
                    'Estimular la creatividad visual ligada al aprendizaje musical.'),
          marco_libre('Mi dibujo musical (o pégalo aquí)', 210))
    sol(MES, 3, 'Concurso de dibujo', ['Libre. Se elegirán los tres dibujos más creativos y musicales.'])
    d.add(ejercicio(4, 'Fiesta final y entrega de premios',
                    ['Prepara tu mejor sonrisa: haremos una **merienda compartida** con todos los compañeros. Expondremos los dibujos musicales, se elegirán los 3 ganadores del concurso '
                     'y se entregará un **diploma musical** por haber completado el curso.'],
                    'Fomentar la convivencia, valorar el esfuerzo del grupo y cerrar el curso con alegría y motivación.'))
    d.add(diploma(),
          caja('tip', 'La actitud del buen pianista', [
              'Un buen pianista sabe que **aprender es un viaje**, un descubrimiento de infinitos tesoros. Para practicar cada día, la pasión por la música que hace que cada nota sea especial '
              'y las ganas de seguir mejorando son claves. Además, **disfrutar y divertirse** mientras tocas es lo que hace que el piano realmente cobre vida.',
              '**Desde T-Clas: ¡feliz musiverano!**']))
