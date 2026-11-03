# Cómo se escribe música de verdad en un pentagrama — y qué he estado haciendo mal

Análisis propio, con mediciones reales sobre las partituras publicadas del propio
proyecto y sobre el código del motor. Todo número de aquí está medido, no recordado.

---

## 1. El diagnóstico medido: por qué el material se ve "básico"

### 1.1 El motor siempre justifica al ancho completo

En `notation.draw_system` el espaciado es:

```python
frac = beat_pos / total_beats
x = cursor_x + frac * avail_w
```

Es decir: **coja el contenido que coja, lo estira hasta llenar los ~500 pt de ancho.**
No existe el concepto de "ancho natural" de un compás. Seis negras y veinte negras
ocupan exactamente lo mismo. Ese es el origen técnico de las "notas sueltas que se
tocan en n segundos".

### 1.2 Los números, comparados

Medido sobre las partituras fuente reales (detección de líneas de pentagrama y
barras de compás por píxeles, a 130 dpi):

| Partitura real | pt por compás | **pt por tiempo** |
|---|---|---|
| Baa Baa Black Sheep (4/4, Paterson) | 84–101 | **21–25** |
| Clementine (3/4, DeBenedetti) | 68–95 | **23–32** |
| El Submarino Amarillo (4/4, Escobés) | 49–62 | **12–15** |
| Little Miss Muffet (6/8, Paterson) | 101–127 | **34–42** |

**Rango real: ~12–32 pt por tiempo.** Y caben **5–11 compases por línea**.

Lo que produce mi motor hoy, con los ejercicios que he estado escribiendo:

| Ejercicio mío | compases | **pt por tiempo** |
|---|---|---|
| Chopsticks "6 negras en 3/4" | 2 | **69,6** |
| Baa Baa "8 negras en 4/4" | 2 | **52,2** |
| Puff "4 blancas en 4/4" | 2 | **52,2** |
| Little Miss Muffet "6 corcheas en 6/8" | 1 | **143,3** |

**Entre 2× y 5× más espaciado que una partitura publicada.** Y 1–2 compases por
línea en vez de 5–11.

### 1.3 Mi propio auditor me lo estaba diciendo

`audit_suite.py` marca "sparse" por encima de 45 pt/evento. En **todos** los
dosieres que he generado, **todos** los sistemas salían marcados (55 a 224 pt/evento).
Lo justifiqué como "aceptable pedagógicamente" literalmente cientos de veces. La
herramienta tenía razón y yo la ignoré sistemáticamente.

---

## 2. Cómo se rellena un pentagrama de verdad

### 2.1 El espaciado NO es lineal con la duración

Error mío: una redonda ocupa 4× lo que una negra (`frac = beats/total`).
Convención real de grabado (Gould, *Behind Bars*): el espacio crece de forma
**logarítmica**, no proporcional. Regla práctica usada por los grabadores:

```
ancho(nota) ∝ duración^0,6      (aprox.)
```

Con eso: una blanca ocupa ~1,5× una negra (no 2×), una redonda ~2,3× (no 4×).
Una corchea ~0,66× (no 0,5×). El resultado es que los pasajes de notas largas
no se estiran hasta quedar vacíos, y los de notas cortas no se apelmazan.

### 2.2 Presupuesto de una línea

Con ancho útil ~500 pt y objetivo 25 pt/tiempo:

- **20 tiempos por línea** = 5 compases de 4/4, o 6–7 de 3/4, o 6 de 6/8.
- **16–24 cabezas de nota por línea.** Eso es lo que parece música.
- Lo que yo escribía: 6–8 notas. Tres veces menos.

### 2.3 Tamaño del pentagrama y sistemas por página

Medido en las fuentes reales: alto del pentagrama **19,9–24,4 pt**
(equivale a rastral 3–4, lo normal en método infantil).

El mío con `gap=7,3` → 29,2 pt. Es **más grande que una partitura publicada**.
Combinado con el estiramiento horizontal, por eso cabe tan poquísima música.

Presupuesto correcto para una página de piano de verdad:
- `gap ≈ 5,5–6,0` → pentagrama de 22–24 pt (legible para un niño, tamaño real de método)
- sistema de piano (sol+fa+separación) ≈ 90–100 pt
- alto útil de página tras cabecera ≈ 640 pt → **6 sistemas por página**
- 6 sistemas × 5 compases = **30 compases de música real por página**

Hoy meto ~8 compases por página. Ahí está el "hacer por hacer".

---

## 3. Cómo se construye un ejercicio real: el principio de SECUENCIA

Esto es lo más importante de todo el análisis, y es lo que no he estado haciendo.

Un ejercicio técnico real **no** es un puñado de notas bonitas. Es **una célula
corta transportada sistemáticamente**. Es literalmente lo que hacen todos los
métodos:

- **Hanon**: una figura de 8 notas que sube grado a grado por dos octavas y vuelve.
- **Czerny op. 599 / 849**: un patrón de escala o arpegio secuenciado por la tonalidad.
- **Burgmüller op. 100**: una figura de acompañamiento constante bajo una melodía.
- **Variaciones "Twinkle" de Suzuki**: las mismas notas, patrón rítmico distinto en cada variación.

**La mecánica:**

```
célula:     Do–Re–Mi–Do
secuencia:  Do-Re-Mi-Do │ Re-Mi-Fa-Re │ Mi-Fa-Sol-Mi │ Fa-Sol-La-Fa │ Sol-La-Si-Sol
```

Eso son 5 compases, 20 notas, una línea entera llena — con lógica musical,
entrenamiento real de la mano en cada posición, y el oído reconociendo el patrón.

Lo que yo escribía: `C4 D4 E4 D4 C4 D4`. Seis notas arbitrarias, sin célula, sin
secuencia, sin destino. **No es un ejercicio, es un fragmento.**

**Regla que adopto:** todo ejercicio técnico = una célula identificable + secuencia
de 4–8 compases. Mínimo 16 notas. Si no llena una línea, no es un ejercicio.

---

## 4. Cómo se deriva material de una partitura real

El método profesional es **extraer, no inventar**. Cinco pasos:

1. **EXTRAER** — coger los compases problemáticos *literalmente como están escritos*.
   No notas "parecidas": las notas reales de la pieza.
2. **REDUCIR** — quitarle la carne al hueso: solo el bajo armónico, o solo el
   contorno melódico sin adornos. Esto enseña la estructura.
3. **AISLAR** — sacar el mecanismo difícil (el salto, el cambio de acorde, el paso
   del pulgar) fuera de contexto, solo.
4. **SECUENCIAR** — ese mecanismo aislado, transportado por la tonalidad → ahora sí
   es un ejercicio de verdad, no un fragmento de 2 segundos.
5. **REINSERTAR** — devolverlo a su contexto con los compases de alrededor.

Yo solo hacía una versión mala del paso 3, y encima con notas inventadas. Por eso el
material no se sentía "de esta canción": porque literalmente no lo era.

---

## 5. Teoría musical aplicada de verdad

### 5.1 El error de los acordes: conducción de voces

He escrito **todos** los I–IV–V del proyecto en estado fundamental:

```
Do(Do-Mi-Sol) → Fa(Fa-La-Do) → Sol(Sol-Si-Re) → Do(Do-Mi-Sol)
```

Un método de piano real usa **inversiones** para que las voces se muevan lo mínimo:

```
Do(Do-Mi-Sol) → Fa(Do-Fa-La) → Sol(Si-Re-Sol) → Do(Do-Mi-Sol)
```

Medido con la propia geometría del motor: **la voz superior se mueve 4× más en mi
versión** (4,0 posiciones de pentagrama acumuladas frente a 1,0). Es decir, he
escrito la versión más difícil de tocar Y musicalmente incorrecta para el estilo,
en los 13 alumnos.

### 5.2 La teoría se toca, no se rellena

"Escribe el grado del acorde: Do__ Fa__ Sol__" es una ficha de examen. No enseña
a tocar. La misma teoría, bien aplicada: que el ejercicio **haga tocar** I–IV–V–I
con buena conducción de voces bajo una melodía real. El alumno interioriza la
función armónica por la mano y el oído, que es como se aprende un instrumento.

### 5.3 Lo que sí es teoría útil por nivel

- **Iniciación**: posición de 5 dedos y *cuándo la pieza se sale de ella* (ese es el
  hecho técnico entrenable). Intervalos como unidades de lectura: 2ª = paso,
  3ª = salto, y su forma visual (línea→línea = 3ª).
- **Básico**: el patrón de acompañamiento (bajo de Alberti, vals, bloque) aislado y
  secuenciado. El paso del pulgar. La anacrusa. La frase A-A-B-A como mapa de memoria.
- **En ambos**: la armadura no como dato, sino como *"estas teclas cambian toda la pieza"*,
  practicada tocando solo esas notas por el teclado.

---

## 6. Qué hay que cambiar en el motor

1. **Espaciado no lineal** (`duración^0,6`) en vez de proporcional puro.
2. **Ancho natural**: si el contenido no llena la línea, que la línea **acabe antes**
   (no que se estire). Un sistema corto es correcto; un sistema estirado es feo.
3. **Densidad objetivo** ~25 pt/tiempo, y que el auditor **falle de verdad** si se
   pasa, en vez de avisar y ser ignorado.
4. **`gap` por defecto 5,5–6,0** en vez de 7,3.
5. **Ayuda de secuencia**: una función que tome una célula y la transporte por la
   tonalidad, para que escribir un ejercicio de 5 compases sea trivial y no haya
   excusa para escribir 6 notas sueltas.
6. **Acordes con inversiones** y conducción de voces automática para I–IV–V.
7. **Multi-sistema como norma**, no como excepción: una página de ejercicios debería
   ser una página de música (5–6 sistemas), no cuatro pentagramas flotando.

---

## 7. Lo que sigo necesitando de ti

Esto es lo que el análisis **no** puede resolver solo, y prefiero decirlo a inventármelo:

1. **El nivel real de lectura de cada alumno.** La densidad correcta (12 pt/tiempo vs
   32 pt/tiempo) depende de si el alumno lee con soltura o va nota a nota. No es lo
   mismo Arnau que un adulto que lleva 3 años.
2. **Cuántos compases de la pieza real puedo reproducir.** Extraer literalmente los
   compases de la partitura es lo pedagógicamente correcto, pero las fuentes son de
   free-scores/mfiles con copyright. Para uso en tu clase con tus alumnos no debería
   haber problema, pero dime hasta dónde quieres que llegue.
3. **Cuántas páginas por canción quieres de verdad.** Con la densidad corregida, una
   sola página bien llena puede valer más que las cinco de antes.
