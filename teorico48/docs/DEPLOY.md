# Publicar Teórico48 en internet (gratis, sin tarjeta de crédito)

Esta guía está pensada para publicar la app sin necesitar conocimientos de programación. Vas a crear dos cuentas
gratuitas:

1. **Neon** → guarda la base de datos (usuarios, progreso, XP, pagos...) de forma permanente.
2. **Render** → aloja la app en sí (el backend y la página web), con un enlace público tipo
   `https://teorico48-web.onrender.com`.

Ninguna de las dos pide tarjeta de crédito para el plan gratuito. Se tarda unos 15-20 minutos.

> Importante: este repositorio contiene **dos apps distintas** (la de piano de Azucena en la raíz, y Teórico48 en
> la carpeta `teorico48/`). Cada una tiene su propio `render.yaml`. En los pasos de abajo usamos el de Teórico48
> (`teorico48/render.yaml`), no el de la raíz.

---

## Paso 1 · Crear la base de datos en Neon

1. Ve a **[neon.com](https://neon.com)** y crea una cuenta gratis (puedes entrar con tu cuenta de Google).
2. Crea un proyecto nuevo, por ejemplo llamado `teorico48`.
3. En la pantalla del proyecto, busca el panel **"Connection Details"** (Detalles de conexión).
4. Copia el texto que empieza por `postgresql://...` (la "cadena de conexión"). Guárdalo, lo necesitarás en el
   Paso 3.

## Paso 2 · Crear cuenta en Render y desplegar

1. Ve a **[render.com](https://render.com)** y crea una cuenta gratis con **"Continuar con GitHub"** (autoriza el
   acceso cuando te lo pida).
2. Pulsa **"New +"** → **"Blueprint"**.
3. Selecciona el repositorio `tclas`.
4. Render busca `render.yaml` en la raíz del repositorio por defecto. Como el de Teórico48 está en
   `teorico48/render.yaml`, busca la opción para indicar la **ruta del Blueprint** (suele aparecer en un desplegable
   o campo de texto al conectar el repo) y escribe:
   ```
   teorico48/render.yaml
   ```
   Si no encuentras esa opción en tu versión de Render, salta al apartado **"Alternativa: crear los servicios a
   mano"** al final de esta guía — el resultado es el mismo.
5. Render detectará dos servicios: `teorico48-api` (backend) y `teorico48-web` (la página web).

## Paso 3 · Rellenar las variables antes de desplegar

Render te pedirá rellenar algunos valores (marcados como "secretos") antes de desplegar:

**En `teorico48-api`:**

| Variable | Valor |
|---|---|
| `DATABASE_URL` | La cadena `postgresql://...` que copiaste de Neon en el Paso 1 |
| `CLIENT_URL` | `https://teorico48-web.onrender.com` (o la URL real si Render le puso otro nombre) |
| `STRIPE_SECRET_KEY`, `STRIPE_PACK_PRICE_ID`, `STRIPE_WEBHOOK_SECRET` | Déjalos vacíos por ahora — se explican en el Paso 5 |
| `RESEND_API_KEY` | Déjalo vacío por ahora — se explica en el Paso 6 |

**En `teorico48-web`:**

| Variable | Valor |
|---|---|
| `VITE_API_URL` | `https://teorico48-api.onrender.com` (o la URL real de tu servicio `teorico48-api`) |

`JWT_SECRET` se genera solo, no hace falta tocarlo.

> Nota: si al terminar el despliegue la URL real de algún servicio es distinta (Render a veces añade números si el
> nombre ya estaba cogido), no pasa nada: entra en la pestaña **"Environment"** del servicio correspondiente,
> corrige el valor con la URL real, y luego **"Manual Deploy" → "Deploy latest commit"** para aplicar el cambio.

Pulsa **"Apply"** / **"Deploy Blueprint"** y espera unos 5 minutos mientras Render construye ambos servicios.

## Paso 4 · Abrir tu app y cargar el banco de preguntas

Cuando termine, entra en el servicio `teorico48-web` y arriba verás su URL pública. Ese es el enlace de tu app.

El primer despliegue ya carga automáticamente el banco de preguntas (el comando de arranque incluye `npm run
seed`, que solo añade preguntas si la tabla está vacía — en despliegues futuros no duplica nada).

## Paso 5 · Activar los pagos reales con Stripe

1. Crea una cuenta en **[stripe.com](https://stripe.com)**.
2. En el dashboard, crea un **producto** "Pack 48h" con un **precio único** (no recurrente, "One time"). Copia el
   ID del precio (empieza por `price_...`).
3. Copia tu clave secreta (empieza por `sk_test_...` mientras pruebas, o `sk_live_...` para cobrar de verdad).
4. En Render, entra en `teorico48-api` → "Environment" y rellena:
   - `STRIPE_SECRET_KEY` con tu clave secreta
   - `STRIPE_PACK_PRICE_ID` con el ID del precio
5. Para `STRIPE_WEBHOOK_SECRET`: en el dashboard de Stripe ve a **Developers → Webhooks → Add endpoint**, con la
   URL `https://teorico48-api.onrender.com/api/payments/webhook` (usa tu URL real) escuchando el evento
   `checkout.session.completed`. Stripe te dará un secreto `whsec_...`; pégalo en esa variable.
6. Vuelve a desplegar (`Manual Deploy → Deploy latest commit`) para que los cambios de variables surtan efecto.

Sin estos tres valores, la app funciona igual pero el botón de pago devuelve un error controlado en vez de
romperse — puedes desplegar primero y activar Stripe más tarde con calma.

## Paso 6 · Activar el email de "recuperar contraseña" (opcional)

Sin configurar esto, si un usuario pide recuperar su contraseña, el enlace se escribe en los logs del servidor en
vez de enviarse por email — funciona para probarlo tú, pero no sirve para usuarios reales.

1. Crea una cuenta gratis en **[resend.com](https://resend.com)**.
2. Genera una API key y verifica un dominio propio (o usa el dominio de pruebas que te da Resend para empezar).
3. En Render, en `teorico48-api` → "Environment", rellena `RESEND_API_KEY` y, si has verificado tu propio dominio,
   `MAIL_FROM` (por ejemplo `Teórico48 <hola@teorico48.com>`).
4. Vuelve a desplegar para aplicar el cambio.

## Cosas a tener en cuenta

- El plan gratuito de Render "duerme" el backend tras 15 minutos sin uso; la primera petición tras el reposo
  tarda 30-60 segundos en responder. No borra nada, solo va más lento al despertar.
- Los datos (usuarios, progreso, pagos) viven en Neon de forma permanente, independientemente de que Render
  "duerma" o se reinicie.
- Cada vez que subas un cambio nuevo a la rama desplegada, Render vuelve a desplegar automáticamente.

## Alternativa: crear los servicios a mano (si no encuentras la opción de ruta del Blueprint)

1. En Render, **"New +" → "Web Service"**, conecta el repo `tclas`.
2. **Root Directory:** `teorico48/server`. **Build Command:**
   ```
   npm install && npx prisma generate && (npx prisma migrate deploy || npx prisma db push --accept-data-loss) && npm run build
   ```
   **Start Command:** `npm run seed && node dist/index.js`. Añade las mismas variables de entorno del Paso 3.
3. Repite con **"New +" → "Static Site"** para el frontend: **Root Directory:** `teorico48/client`, **Build
   Command:** `npm install && npm run build`, **Publish Directory:** `dist`, y la variable `VITE_API_URL`. Añade
   una regla de reescritura `/* → /index.html` para que funcione la navegación de React.
