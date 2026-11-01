# Pendientes por alumno (revisar al final, solo si hace falta)

## Eva (dosier en catalán, 144 págs)
- Mariage d'amour: corte de nota/silencio de pedal en la última página de partitura.
- Elegy for the Arctic: tonalidad sin nombrar (solo "4 bemoles").
- Your Song: salto «To Coda» no impreso → acordar con la profesora.
- Padrino y La dispute (Do menor) y Arabesque (La menor): tonalidades deducidas.
- Padrino: nombre del arreglista ilegible (puesto «arranjament per a piano»).

## Sharifa (dosier en catalán, 122 págs, con Mussol Misol)
- Melodische (pieza 4, enero): densa para principiante; valorar moverla o cambiarla.
- «Sabies que?»: datos de memoria, sin verificar en línea.
- Can't Stop, Up, Boig per tu, Lovely, A Thousand Years: PDF de baja resolución, melodía no transcrita nota a nota; Boig per tu en Sol mayor deducido (sin armadura impresa).
- Shallow: logo de Bye Bye Beethoven dentro de los sistemas cc. 21 y 40.

## General
- Cerrar los enlaces públicos de Drive de Martina, Jaume y Alan (partituras con copyright).
- Las partituras no se versionan (students/*/source/).

## Abril (dosier en catalán, 122 págs, con Mussol Misol; empieza ahora, bases)
- Piezas 2, 3, 4, 9, 11, 14 reutilizadas de Sharifa (mismas partituras, verificadas por md5).
- The Scientist y Mamma Mia escritas a mano; resto por asistentes (interrumpidos al final): revisadas a ojo las fichas y varias páginas, no todas.
- Hijo de la luna, Mamma Mia, The Beginner: página apaisada recortada/re-laid; notas algo más pequeñas (≈74 %).
- «Sabies que?» de memoria, sin verificar en línea.
- Mamma Mia: alturas de la melodía no transcritas nota a nota; The Scientist: acordes de la derecha leídos por medición (Fa-La, Fa-Si♭, Fa-Sol).

## Próximos dosieres (carpeta SANT CUGAT del Drive), en este orden
1. LOLA (Drive id 1aDMlko7CHgOwvGAROJvD_NDux2iMsOKz): versiones fáciles (You've Got a Friend in Me, Spring, Gladiator easy, Perfect easy, Twinkle…)
2. Alba (1hIaL54x0hOcsI4YaV8IRXNT5cQzlxDjD): A Thousand Years, Can't Stop, Up, I Have a Dream, Boig per tu…
3. Txell (1oVlVhtWn9ta9FYpug8qhUXJAWzYb-WZf): Perfect, Shallow, Counting Stars, El Golpe, Blanca Navidad…
- Sin partituras en su carpeta (no se puede hacer dosier todavía): NORA, FOIX, ELSA, HERA.
- Ya hechos: EVA, Sharifa, ABRIL. Método: catalán, tema Mussol Misol, sin asistentes, ALUMNA=<nombre>, bajar con gdown si la carpeta es pública.


## Lola, Alba i Txell (fets — dosiers en català)
- **Lola** (8 anys, comença de zero, ha de veure els colors): `ALUMNA=lola python3 cuaderno/mayores_libro.py` → 96 pàgines.
  Partitures pintades amb `cuaderno/colorear_notas.py` (les notes pel seu nom: DO vermell… SI gris); les fonts es
  regeneren amb `python3 cuaderno/lola_preparar.py <carpeta de Drive>`. Les 15 peces: Twinkle, Alouette, Ode to Joy,
  Saints, Clementine, My Bonnie, Puff, You've Got a Friend in Me, La Pantera Rosa, La Primavera (Vivaldi), I Have a Dream,
  Piano Man, Nocturn Op. 9, Honor Him (Gladiator), Perfect. Han quedat fora: «Eso que tú me das» (només xifrat),
  «I See the Light» (escanejada, no es pot pintar), «Himno a la Alegría» (duplica Ode) i «Spring easy» (és la mateixa peça que la
  Primavera). Pendent/atenció: les dades de les peces 7-15 es van llegir amb `volcar_notas.py` + inspecció visual; revisar
  amb la professora els compassos citats si vol validar-los; els «Sabies que?» d'Alouette i My Bonnie estan marcats com a no verificats.
- **Alba** (23 anys, comença ara): `ALUMNA=alba` → 124 pàgines; secció d'exercicis de base (pàgs. 5-14, `ba_front.py`: postura i dits, notes,
  figures, mà dreta, mà esquerra, mans juntes, escales Do/Sol, acords i arpegis, ritme i lectura, rutina setmanal) + 15 peces. Disseny sobri
  (sense Mussol ni colors). Per a Alba no hi ha «Para Elisa»: la seva edició (amb semicorxeres) és massa difícil; s'ha posat el Scherzo de Diabelli.
- **Txell** (12 anys, un any de piano): `ALUMNA=txell` → 124 pàgines; quasi tota la seva carpeta coincideix byte a byte amb partitures ja mesurades
  de Sharifa/Abril (`clonar_spec.py` copia la fitxa canviant número/nom/mes). Dues pàgines inicials: notes (sense colors) i figures.
- Recordatori: tancar els enllaços públics de Drive (partitures amb copyright).

## Cuaderno «Mi cuaderno de piano · Nivel 1 · Adultos» (castellano, noviembre–julio)
- Rehecho para un alumno adulto que empieza de cero en noviembre (50 años, aprende rápido). Origen: `NIVEL 1 ADULTS` de Canva (Drive id `1Pb_rpHyaORPRqMjpaNglgCvZp95u7vnH`), con el temario reordenado y ampliado.
- Montaje: `cd cuaderno && python3.13 n1_libro.py` → `entrega/CUADERNO_NIVEL1_ADULTOS.pdf` (`BN=1` para blanco y negro). Módulos: `n1_base.py` (flujo de páginas y componentes), `n1_comun.py` (diagramas), `n1_nov…n1_jul.py` (un mes cada uno), `n1_anexos.py` (portada, calendario, chuleta, glosario, diario, soluciones, pautas).
- Temario: nov fundamentos (postura, dedos, teclado, pentagrama) · dic figuras, silencios y compás · ene notas adicionales · feb escala de Do, alteraciones, intervalos · mar ritmo, ligadura, 6/8 · abr clave de fa y manos juntas · may armaduras (Sol, Fa) · jun acordes y cadencias · jul expresión y repaso.
- Normas de este cuaderno (petición del cliente): tono adulto sin explicaciones infantiles; los ejercicios de nombrar notas parten del Do (clave de sol) y del Fa (clave de fa); los silencios se muestran dentro del pentagrama (redonda colgando de la 4.ª línea, blanca sobre la 3.ª); dedos y pentagrama al principio.
- Las soluciones salen de los mismos datos que dibujan los ejercicios (`sol(...)`). Verificar con partitura impresa las notas de Himno de la Alegría, Jingle Bells, Au clair de la lune, Frère Jacques y Minueto en Sol (escritas de memoria).
- Entorno: `dibujo_mano.py` pide fuentes (CabinSketch, dkgBd, Leckerli) que pueden faltar en una sesión nueva; basta copiar DejaVu a esas rutas.
