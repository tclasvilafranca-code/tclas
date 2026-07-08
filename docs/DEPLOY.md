# Publicar t-clas en internet (gratis, sin tarjeta de credito)

Esta guia esta pensada para poder publicar la app sin necesidad de saber programar. Vas a crear dos cuentas gratuitas:

1. **Neon** → guarda la base de datos (donde viven los alumnos, el progreso, etc.) para siempre, sin borrarse.
2. **Render** → aloja la app en si (el backend y la pagina web), con un enlace publico tipo `https://tclas-web.onrender.com`.

Ninguna de las dos pide tarjeta de credito para el plan gratuito. Se tarda unos 10-15 minutos.

---

## Paso 1 · Crear la base de datos en Neon

1. Ve a **[neon.com](https://neon.com)** y crea una cuenta gratis (puedes entrar directamente con tu cuenta de Google).
2. Crea un proyecto nuevo, por ejemplo llamado `tclas`.
3. En la pantalla del proyecto, busca el panel **"Connection Details"** (Detalles de conexion).
4. Copia el texto que empieza por `postgresql://...` (es la "cadena de conexion"). Guardalo, lo necesitaras en el Paso 3.

## Paso 2 · Crear cuenta en Render

1. Ve a **[render.com](https://render.com)** y crea una cuenta gratis con **"Continuar con GitHub"** (autoriza el acceso cuando te lo pida).
2. Una vez dentro, pulsa el boton **"New +"** (arriba a la derecha) y elige **"Blueprint"**.
3. Selecciona el repositorio del proyecto (`tclas`). Render detectara automaticamente el archivo `render.yaml` y te mostrara **dos servicios**:
   - `tclas-api` (el backend)
   - `tclas-web` (la pagina web)

## Paso 3 · Rellenar los dos datos que te va a pedir

Render te pedira rellenar 2 valores antes de desplegar (marcados como "secretos"):

- **`DATABASE_URL`** (en el servicio `tclas-api`): pega aqui la cadena de conexion que copiaste de Neon en el Paso 1.
- **`VITE_API_URL`** (en el servicio `tclas-web`): escribe exactamente `https://tclas-api.onrender.com`

> Nota: si al terminar el despliegue ves que la URL real de `tclas-api` es distinta (Render a veces anade numeros si el nombre ya estaba cogido), no pasa nada — mas abajo te explico como corregirlo en 30 segundos.

Pulsa **"Apply"** / **"Deploy Blueprint"** y espera unos 5 minutos mientras Render construye ambos servicios (veras logs en pantalla).

## Paso 4 · Abrir tu app

Cuando termine, entra en el servicio **`tclas-web`** dentro de Render y arriba veras su URL publica, algo como:

```
https://tclas-web.onrender.com
```

¡Ese es el enlace de tu app! Abrelo, y podras entrar con las cuentas de prueba:

| Rol       | Acceso                              |
|-----------|--------------------------------------|
| Profesora | azucena@t-clas.com / profesora123    |
| Alumno    | usuario `arnau` / PIN `1234`         |

## Si la app carga pero no puedes iniciar sesion (error de conexion)

Esto significa que `VITE_API_URL` no coincide con la URL real del backend. Para arreglarlo:

1. Entra en el servicio `tclas-api` en Render y copia su URL real (arriba del todo).
2. Entra en el servicio `tclas-web` → pestaña **"Environment"** → edita `VITE_API_URL` con esa URL exacta.
3. Ve a la pestaña **"Manual Deploy"** → **"Deploy latest commit"** para reconstruir la pagina con el dato corregido.
4. Espera un par de minutos y vuelve a abrir el enlace.

## Cosas a tener en cuenta

- El plan gratuito "duerme" el backend tras 15 minutos sin uso. La primera vez que alguien entra despues de un rato, puede tardar 30-60 segundos en cargar (luego va normal). Esto no borra nada, solo es mas lento al despertar.
- Los datos (alumnos, progreso, rachas...) se guardan en Neon de forma permanente, independientemente de que Render "duerma" o se reinicie.
- Cada vez que se suba un cambio nuevo al repositorio, Render vuelve a desplegar automaticamente — no hace falta repetir estos pasos.
