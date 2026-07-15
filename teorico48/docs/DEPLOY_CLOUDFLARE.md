# Mover Teórico48 a Cloudflare (gratis de verdad, para siempre)

Esta guía sustituye a `DEPLOY.md`: en vez de Render (que en su plan gratis se duerme y tiene un tope de horas al
mes), el backend pasa a **Cloudflare Workers**, que no se duerme, no tiene tope de horas y permite uso comercial
en su plan gratuito sin coste.

**Importante: la base de datos no cambia.** Sigues usando la misma base de datos de Neon que ya tienes, con todos
los datos que ya haya (usuarios, códigos, preguntas...). Solo cambia dónde vive el *código* que la consulta.

Se tarda unos 20-30 minutos la primera vez.

---

## Paso 0 · Qué vas a necesitar a mano

- Tu cadena de conexión de Neon (`postgresql://...`), la misma que usaste para Render.
- Tus claves de Stripe, si ya las tenías configuradas (`STRIPE_SECRET_KEY`, `STRIPE_PACK_PRICE_ID`,
  `STRIPE_WEBHOOK_SECRET`).
- Tu clave de Resend (`RESEND_API_KEY`), si la tenías.
- Tu contraseña de administrador (`ADMIN_PASSWORD`) y tu email (`OWNER_EMAIL`).

## Paso 1 · Crear cuenta en Cloudflare e instalar las herramientas

1. Ve a **[dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)** y crea una cuenta gratis.
2. En tu ordenador (o en esta misma sesión de Claude Code si lo prefieres, pidiéndomelo), instala Wrangler, la
   herramienta de línea de comandos de Cloudflare:
   ```
   cd teorico48/worker
   npm install
   ```
3. Inicia sesión con tu cuenta de Cloudflare:
   ```
   npx wrangler login
   ```
   Esto abre el navegador para autorizar el acceso. Una vez autorizado, ya puedes cerrar esa pestaña.

## Paso 2 · Crear el Hyperdrive (conecta el Worker con tu base de datos de Neon)

Hyperdrive es la pieza de Cloudflare que permite que un Worker (que no puede mantener conexiones abiertas como un
servidor normal) hable con una base de datos Postgres normal como la de Neon. Es gratis, sin límites de coste.

```
npx wrangler hyperdrive create teorico48-db --connection-string="TU_CADENA_DE_NEON_AQUI"
```

El comando te devuelve un `id`. Copia ese id y pégalo en `teorico48/worker/wrangler.toml`, sustituyendo
`REPLACE_WITH_HYPERDRIVE_ID`.

## Paso 3 · Crear el espacio KV (para el límite de intentos de login)

```
npx wrangler kv namespace create RATE_LIMIT_KV
```

Copia el `id` que te devuelva y pégalo en `wrangler.toml`, sustituyendo `REPLACE_WITH_KV_NAMESPACE_ID`.

## Paso 4 · Configurar los secretos (contraseñas y claves)

Cada uno de estos comandos te pedirá que pegues el valor y pulses Enter:

```
npx wrangler secret put JWT_SECRET
npx wrangler secret put CLIENT_URL
npx wrangler secret put ADMIN_PASSWORD
npx wrangler secret put OWNER_EMAIL
npx wrangler secret put STRIPE_SECRET_KEY
npx wrangler secret put STRIPE_PACK_PRICE_ID
npx wrangler secret put STRIPE_WEBHOOK_SECRET
npx wrangler secret put RESEND_API_KEY
npx wrangler secret put MAIL_FROM
```

Para `JWT_SECRET`, usa una cadena larga y aleatoria (por ejemplo, genera una con `openssl rand -hex 32` en una
terminal). Para `CLIENT_URL`, de momento pon la URL que tenga tu frontend (lo veremos en el Paso 6); puedes
volver a este paso más tarde para actualizarlo si cambia.

Si todavía no tienes Stripe o Resend configurados, puedes dejar esos `wrangler secret put` para más adelante —
el Worker funciona igual, simplemente esas funciones (pagos, emails reales) devuelven un error controlado hasta
que los configures, exactamente igual que pasaba con Render.

## Paso 5 · Desplegar el backend

```
npx wrangler deploy
```

Al terminar, te da una URL parecida a `https://teorico48-api.<tu-cuenta>.workers.dev`. Esa es la URL de tu API.
Pruébala visitando `https://esa-url/api/health` — debería responder `{"ok":true}`.

## Paso 6 · Desplegar el frontend en Cloudflare Pages

El frontend (la parte visual, en `teorico48/client`) puede quedarse donde está en Render sin ningún riesgo — los
sitios estáticos de Render no tienen el problema de las horas límite, solo lo tenía el backend. Pero si prefieres
tenerlo todo en el mismo sitio:

1. En el dashboard de Cloudflare, ve a **Workers & Pages → Create → Pages → Connect to Git** y selecciona tu
   repositorio.
2. Configuración de build:
   - **Root directory:** `teorico48/client`
   - **Build command:** `npm install && npm run build`
   - **Build output directory:** `dist`
3. Variable de entorno: `VITE_API_URL` = la URL de tu Worker del Paso 5 (`https://teorico48-api.<tu-cuenta>.workers.dev`).
4. Despliega. Te dará una URL tipo `https://teorico48.pages.dev` (puedes configurar un dominio propio después,
   gratis, desde la misma pantalla).
5. Vuelve al Paso 4 y actualiza `CLIENT_URL` con esta URL real:
   ```
   npx wrangler secret put CLIENT_URL
   ```
   y despliega de nuevo (`npx wrangler deploy`) para que el cambio surta efecto.

## Paso 7 · Actualizar el webhook de Stripe (si ya lo tenías configurado)

En el dashboard de Stripe, en **Developers → Webhooks**, edita el endpoint para que apunte a la nueva URL:
```
https://teorico48-api.<tu-cuenta>.workers.dev/api/payments/webhook
```

## Paso 8 · Comprobar que todo funciona

1. Entra en `/admin` de tu nuevo frontend con tu `ADMIN_PASSWORD` y genera un código de prueba.
2. Regístrate con ese código en `/register`.
3. Haz un simulacro completo y comprueba que se guarda el resultado.
4. Si tenías Stripe activo, prueba una compra en modo test.

## Cuando todo funcione: puedes apagar Render

Una vez confirmes que la nueva versión en Cloudflare funciona igual de bien, entra en tu dashboard de Render y
puedes pausar o eliminar el servicio `teorico48-api` (el backend antiguo) — ya no lo necesitas. El sitio estático
`teorico48-web` puedes dejarlo o eliminarlo también si moviste el frontend a Cloudflare Pages en el Paso 6.

**No borres nada en Neon** — es tu base de datos real, con todos los usuarios y datos, y la sigues usando tal
cual desde el nuevo backend.

---

## Notas técnicas (por si algo falla)

- El código del nuevo backend vive en `teorico48/worker/`, es un proyecto aparte del antiguo `teorico48/server/`
  (que se deja intacto, sin usar, por si algún día quieres volver a Render).
- La contraseña de las cuentas nuevas se cifra con PBKDF2 en vez de bcrypt (más rápido en el entorno de
  Cloudflare, dentro del límite gratuito de 10ms de CPU por petición). Las cuentas que ya existieran, creadas en
  la versión de Render con bcrypt, siguen funcionando igual: el sistema detecta el formato antiguo y lo verifica
  igualmente, sin que nadie se quede fuera ni tenga que restablecer su contraseña.
- El límite de intentos de login usa Workers KV en vez de una lista en memoria: es casi igual de estricto, con
  una pequeña tolerancia bajo mucha concurrencia simultánea, aceptable para el volumen de esta app.
