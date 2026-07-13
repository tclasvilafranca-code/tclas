# Teórico48

_Aprende. Practica. Aprueba._

App para preparar el examen teórico del carnet de conducir con simulacros
cronometrados, repaso automático de fallos, gamificación (XP, nivel, rachas
y medallas) y un plan con cuenta atrás hasta el examen. Incluye monetización
con un pago único ("Pack 48h") vía Stripe.

Este proyecto es independiente de la app de piano (`client/`, `server/` en la
raíz del repo) — vive en su propia carpeta `teorico48/` con su propio
backend, frontend y base de datos.

## Arquitectura

```
server/   API en Node.js + Express + TypeScript + Prisma (PostgreSQL)
client/   App web en React + TypeScript + Vite + Tailwind CSS
```

- **Banco de preguntas** (`server/src/content/questions.ts`): preguntas
  originales agrupadas en 6 categorías (señales, prioridad, velocidad,
  alcohol/drogas, mecánica/documentación, seguridad vial). Al cargarlas
  (`npm run seed`) el orden de las opciones se baraja para que la respuesta
  correcta no quede siempre en la misma posición.
- **Generador de simulacros** (`server/src/generator.ts`): monta tests de 30
  preguntas al azar (modo examen) o centrados solo en las preguntas que el
  alumno ha fallado antes (modo repaso, función premium).
- **Corrección**: se aplica la regla real de la DGT — máximo 3 fallos de 30
  para aprobar.

## Puesta en marcha (desarrollo local)

### 0. Base de datos local

```bash
cd teorico48
docker compose up -d
```

Esto levanta un Postgres en el puerto **5433** (para no chocar con el de la
app de piano, que usa 5432).

### 1. Backend

```bash
cd teorico48/server
npm install
cp .env.example .env
npx prisma migrate dev
npm run seed          # carga el banco de preguntas (60 preguntas)
npm run dev           # http://localhost:4001
```

### 2. Frontend

```bash
cd teorico48/client
npm install
npm run dev            # http://localhost:5174 (con proxy a la API en /api)
```

## Pagos (Stripe) — Pack 48h

El backend usa Stripe Checkout (pago único) para desbloquear simulacros
ilimitados y el modo repaso de fallos:

1. Crea una cuenta en [Stripe](https://stripe.com) (puedes usar el modo test
   para probar sin cobrar de verdad).
2. En el dashboard de Stripe, crea un **producto** "Pack 48h" con un
   **precio único** (no recurrente) — copia el ID del precio (`price_...`).
3. Copia tu clave secreta (`sk_test_...` o `sk_live_...`).
4. Rellena en `server/.env`:
   ```
   STRIPE_SECRET_KEY="sk_test_..."
   STRIPE_PACK_PRICE_ID="price_..."
   ```
5. Para el webhook (que activa el acceso premium tras el pago), en local
   puedes usar la [Stripe CLI](https://stripe.com/docs/stripe-cli):
   ```bash
   stripe listen --forward-to localhost:4001/api/payments/webhook
   ```
   Copia el `whsec_...` que te da y ponlo en `STRIPE_WEBHOOK_SECRET`.

Sin estas variables configuradas, la app funciona igual (tests, simulacros,
etc.) pero el botón de pago devolverá un error controlado en vez de romper
la app.

## Publicar en internet (gratis, con Render)

Este proyecto incluye su propio `render.yaml` en `teorico48/render.yaml`
(distinto del de la app de piano, que está en la raíz del repo). Ver la guía
paso a paso en [`docs/DEPLOY.md`](docs/DEPLOY.md) — pensada para alguien sin
experiencia técnica, incluye cómo activar Stripe y el email de recuperación
de contraseña.

## Decisiones de alcance del MVP

- **Contenido**: las 60 preguntas semilla son un punto de partida para tener
  la app funcionando ya — están escritas a mano a partir del conocimiento
  general del temario público de circulación, no son preguntas oficiales de
  ningún examen real ni de ninguna academia. Antes de usarlas para preparar
  un examen real de verdad, conviene revisarlas y ampliarlas con alguien
  que conozca bien el temario actualizado (las normas cambian).
- **Límite del plan gratuito**: 1 simulacro completo al día; el modo repaso
  de fallos y los simulacros ilimitados son de pago (Pack 48h).
- **Regla de aprobado**: máximo 3 fallos sobre 30 preguntas, igual que en el
  examen real de la DGT.
- **Sin recordatorios** push/email todavía para avisar de la cuenta atrás.
- **Sin editor visual de preguntas**: hoy se añaden editando
  `server/src/content/questions.ts` y volviendo a correr `npm run seed`
  (solo carga si la tabla está vacía, así no duplica en cada despliegue).

## Próximos pasos sugeridos

1. Ampliar el banco de preguntas (categorías con más preguntas, imágenes de
   señales reales).
2. Panel de administración simple para añadir/editar preguntas sin tocar
   código.
3. Recordatorios (email/push) para no perder la cuenta atrás del examen.
4. Analítica básica de conversión (cuántos gratis pasan a Pack 48h).
