# t-clas · Piano Learning App

Una app tipo Duolingo para aprender piano, pensada para complementar las clases presenciales de piano de Azucena (marca **t-clas**).

## ¿Que incluye este MVP?

- **Repertorio real y personalizado por alumno**: cada alumno tiene su propia lista de piezas (asignadas por la profesora), en el orden y con la duracion que ella decida — no un temario generico igual para todos.
- **12 tipos de ejercicios**: opcion multiple, nombrar notas, lectura de pentagrama, tocar en el teclado, ritmo (tap en tiempo real), oido musical, intervalos, acordes, escribir la respuesta, relacionar (matching), ordenar una secuencia y decir la respuesta en voz alta (reconocimiento de voz del navegador).
- **Generador automatico de lecciones**: al asignar una pieza a un alumno, la app genera solas las semanas de practica (con ejercicios variados derivados de las notas/ritmo reales de esa pieza) — asignar contenido a un alumno nuevo no requiere escribir codigo.
- **Camino visual tipo "Candy Crush"**: un camino serpenteante de nodos semana a semana, agrupado por pieza, con estado bloqueado/disponible/completado.
- **Piano virtual interactivo**: se toca con el raton, con el teclado del ordenador (A S D F G H J K...) o conectando un piano/teclado MIDI real via Web MIDI API.
- **Gamificacion**: XP, rachas diarias, corazones (vidas) con regeneracion, estrellas por leccion e insignias.
- **Acceso**: la profesora tiene email+contrasena; los alumnos entran con usuario+PIN generados por la profesora (sin autoregistro), pensado para que los mas pequenos puedan entrar facilmente.
- **Panel para Azucena (profesora)**: crea el acceso de cada alumno, gestiona su repertorio (anadir/quitar piezas de la biblioteca compartida, con fecha de inicio y duracion), y ve el progreso de cada uno.

## Arquitectura

```
server/   API en Node.js + Express + TypeScript + Prisma (PostgreSQL)
client/   App web en React + TypeScript + Vite + Tailwind CSS
```

El modelo de contenido tiene 3 capas:
1. **Biblioteca de piezas** (`server/src/content/pieces.ts`): partituras reales, transcritas a datos (notas, ritmo, acordes) — versionable y ampliable sin tocar el motor.
2. **Generador** (`server/src/generator.ts`): a partir de una pieza y una duracion en semanas, genera automaticamente las lecciones y sus ejercicios variados.
3. **Repertorio por alumno** (`RepertoireEntry` en la base de datos): la asignacion real de que alumno lleva que pieza, en que orden y fechas — se gestiona desde el panel de la profesora.

## Puesta en marcha (desarrollo local)

### 0. Base de datos local

Necesitas un PostgreSQL accesible en `localhost:5432`. La forma mas facil es con Docker:

```bash
docker compose up -d
```

### 1. Backend

```bash
cd server
npm install
cp .env.example .env
npx prisma migrate dev
npm run seed        # crea la biblioteca de piezas + cuentas de prueba (incluye el repertorio real de Arnau)
npm run dev          # http://localhost:4000
```

### 2. Frontend

```bash
cd client
npm install
npm run dev          # http://localhost:5173 (con proxy a la API en /api)
```

### Cuentas de prueba (creadas por el seed)

| Rol       | Acceso                          |
|-----------|----------------------------------|
| Profesora | azucena@t-clas.com / profesora123 |
| Alumno    | usuario `arnau` / PIN `1234`      |

## Publicar la app en internet (gratis)

Este repo incluye un `render.yaml` para desplegar en [Render](https://render.com) con muy pocos clics. Ver la guia paso a paso en [`docs/DEPLOY.md`](docs/DEPLOY.md) — pensada para alguien sin experiencia tecnica.

## Decisiones de alcance del MVP

- El "bloqueo" de progreso es lineal (una leccion disponible a la vez, en el orden del repertorio del alumno).
- La deteccion de acordes/ejercicios de ritmo compara contra tolerancias razonables (no hay analisis de audio real del piano fisico; MIDI da notas exactas, pero no se analiza la calidad tonal o el pedal).
- El ejercicio de "decir en voz alta" usa la Web Speech API del navegador (solo Chrome/Edge la soportan bien); en navegadores sin soporte se puede omitir.
- Las piezas transcritas son un extracto representativo (la frase inicial), no la partitura completa nota a nota — suficiente para generar practica de calidad sin necesitar transcribir cada compas.
- No hay todavia sistema de notificaciones push/email para recordar la practica diaria.
- El plan gratuito de Render "duerme" el backend tras 15 minutos sin uso (la primera peticion tras el reposo tarda ~30-60s en responder). Los datos viven en Neon (Postgres) y no se ven afectados por esto.

## Proximos pasos sugeridos

1. Anadir un editor visual de piezas en el panel de la profesora (hoy se anaden editando `server/src/content/pieces.ts`).
2. Replicar el repertorio a mas alumnos (usar a Arnau como plantilla de referencia).
3. Anadir recordatorios (email/push) para mantener la racha diaria.
4. Sustituir la tipografia y paleta de marcador de posicion por la identidad visual real de t-clas.
