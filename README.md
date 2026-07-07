# t-clas · Piano Learning App

Una app tipo Duolingo para aprender piano, pensada para complementar las clases presenciales de piano de Azucena (marca **t-clas**).

## ¿Que incluye este MVP?

- **3 caminos de aprendizaje diferenciados por edad**: Los Exploradores del Piano (6-11), Piano Level Up (12-17) y Piano para Adultos (18+), cada uno con 5 niveles, ~11 unidades y 25-26 lecciones (76 lecciones y ~260 ejercicios en total), con pedagogia y tono adaptados a cada grupo.
- **8 tipos de ejercicios**: nombrar notas, lectura de pentagrama, ritmo (tap en tiempo real), oido musical, teoria (opcion multiple), tocar en el teclado, intervalos y acordes.
- **Piano virtual interactivo**: se toca con el raton, con el teclado del ordenador (A S D F G H J K...) o conectando un piano/teclado MIDI real via Web MIDI API.
- **Gamificacion**: XP, rachas diarias, corazones (vidas) con regeneracion, estrellas por leccion e insignias.
- **Cuentas y roles**: alumno y profesora, con registro/login (JWT).
- **Panel para Azucena (profesora)**: ve el progreso de cada alumno por nivel, y puede asignar tareas de la app ligadas a la fecha de una clase presencial, con una nota para el alumno.

## Arquitectura

```
server/   API en Node.js + Express + TypeScript + Prisma (SQLite)
client/   App web en React + TypeScript + Vite + Tailwind CSS
```

El contenido del curriculo (niveles/unidades/lecciones/ejercicios) vive como datos versionables en `server/src/content/*Track.ts` y se carga a la base de datos con un script de seed, para que el equipo pueda seguir ampliandolo sin tocar el motor de la app.

## Puesta en marcha

### 1. Backend

```bash
cd server
npm install
cp .env.example .env
npx prisma migrate dev
npm run seed        # crea el curriculo + cuentas de prueba
npm run dev          # http://localhost:4000
```

### 2. Frontend

```bash
cd client
npm install
npm run dev          # http://localhost:5173 (con proxy a la API en /api)
```

### Cuentas de prueba (creadas por el seed)

| Rol       | Email                | Contrasena     |
|-----------|-----------------------|----------------|
| Profesora | azucena@t-clas.com    | profesora123   |
| Alumno    | alumno@t-clas.com     | alumno123      |

## Decisiones de alcance del MVP

- Base de datos SQLite (cero configuracion) en vez de Postgres, para poder levantar el proyecto sin infraestructura externa. Migrar a Postgres solo requiere cambiar el `provider` y `DATABASE_URL` en `server/prisma/schema.prisma`.
- El "bloqueo" de progreso es lineal (una leccion disponible a la vez por track), sin desbloquear unidades enteras a la vez, para simplificar el MVP.
- La deteccion de acordes/ejercicios de ritmo compara contra tolerancias razonables (no hay analisis de audio real del piano fisico; MIDI da notas exactas, pero no se analiza la calidad tonal o el pedal).
- No hay todavia sistema de notificaciones push/email para recordar la practica diaria, ni tienda de recompensas con gemas.

## Proximos pasos sugeridos

1. Ampliar el contenido de los niveles 2-5 de cada track (actualmente tienen 1 unidad/2 lecciones cada uno; el Nivel 1 esta completo con 3 unidades).
2. Anadir recordatorios (email/push) para mantener la racha diaria.
3. Exportar/imprimir un resumen de progreso para que Azucena lo revise antes de cada clase presencial.
4. Sustituir la tipografia y paleta de marcador de posicion por la identidad visual real de t-clas.
