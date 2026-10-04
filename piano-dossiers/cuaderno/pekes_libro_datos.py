# -*- coding: utf-8 -*-
"""EL LIBRO DE PEKES — segundo intento, de cero.

   El cliente rechazo la primera version entera: "esto es una puta mierda,
   ni esta bien planteado ni nada, el diseno esta fatal". Lo que pide en su
   lugar:

   - NADA de semanas ni de dias pautados: un libro de teoria y ejercicios
     que la profesora va usando a su ritmo, no un calendario.
   - Cada concepto teorico se reparte en TRES hojas: teoria (la explicacion),
     al piano (practica fisica de verdad, sentado delante del teclado) y
     ficha (el ejercicio de papel).
   - Blanco y negro, pero "ultra super infantil y bonito": nada de la
     paleta editorial azul noche del resto del proyecto.
   - MUSOL MISOL, el buho de la portada del Canva original, tiene que
     aparecer en cada hoja -- es el que explica las cosas.
   - "no tengas miedo de hacer hojas" -- prioriza que cada hoja respire
     (poco contenido, grande y claro) antes que meter mucho por pagina.

   Este archivo trae SOLO el primer tema, de muestra, para que el cliente
   vea el enfoque antes de que se escriban los otros ~20 temas del curso
   (ver `pekes_datos.py` para el contenido teorico ya escrito la primera
   vez -- se reaprovecha, pero re-redactado para el nuevo formato de 3
   hojas en vez de cramearlo en una).
"""

TEMAS = [
    dict(
        n=1,
        capitulo='EL PIANO Y LAS MANOS',
        titulo='Las partes del piano',
        teoria=dict(
            intro='¡Hola! Soy Musol Misol, y voy a ser tu profe de música '
                  'todo el curso. Antes de tocar ni una nota, tenemos que '
                  'conocer bien nuestro instrumento: el piano.',
            explicacion='El piano tiene siete partes con su propio nombre. '
                        'Algunas las vas a tocar con las manos, y otras solo '
                        'están ahí para ayudar al piano a sonar bien.',
            dato='¿Sabías que un piano grande de concierto puede pesar tanto '
                 'como un coche pequeño?',
            dibujo=('piano_partes', {}),
        ),
        piano=dict(
            intro='Ahora vamos a tocar de verdad. Siéntate delante de tu '
                  'piano o teclado, con la espalda rectita, y sigue estos '
                  'pasos conmigo.',
            pasos=[
                'Abre la tapa (o enciende el teclado) y mira todas las '
                'teclas blancas, de un extremo al otro.',
                'Pasa un dedo despacito por encima de las teclas blancas, '
                'de izquierda a derecha, sin apretar.',
                'Ahora busca las teclas negras: van en grupos de 2 y de 3. '
                'Tócalas suavemente, una a una.',
                'Si tu piano tiene pedal, apóyalo con el pie y escucha '
                'cómo cambia el sonido.',
                'Por último, toca 3 teclas blancas cualquiera, una '
                'detrás de otra, y escucha bien cómo suenan.',
            ],
            consejo='No hace falta tocar fuerte para que suene bien — '
                    'un piano se toca con cariño, no con fuerza.',
        ),
        ficha=dict(
            intro='Mira el dibujo del piano de abajo. Cada parte tiene un '
                  'número. Escribe al lado de cada nombre el número que le '
                  'toca.',
            tipo='numera_grande',
            items=['Teclas blancas', 'Teclas negras', 'Tapa', 'Atril',
                  'Pedal', 'Patas', 'Caja de resonancia'],
            dibujo=('piano_partes', {}),
            reto='Reto extra: colorea de negro todas las teclas negras '
                 'del dibujo.',
        ),
    ),
]
