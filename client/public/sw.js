// Service worker minimo: solo lo justo para que la app se pueda "instalar"
// (Add to Home Screen) y para recibir notificaciones push. No cachea rutas
// de la API ni intenta funcionar offline: eso es un proyecto aparte.
const CACHE_NAME = "tclas-shell-v1";
const SHELL_ASSETS = ["/", "/manifest.webmanifest"];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(SHELL_ASSETS)).catch(() => {}));
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
  );
  self.clients.claim();
});

self.addEventListener("push", (event) => {
  let data = { title: "t-clas 🎹", body: "Toca para practicar un rato." };
  try {
    if (event.data) data = event.data.json();
  } catch {
    // si el payload no es JSON valido, se usa el mensaje por defecto
  }
  event.waitUntil(
    self.registration.showNotification(data.title, {
      body: data.body,
      icon: "/icon-maskable.svg",
      badge: "/icon-maskable.svg",
    })
  );
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  event.waitUntil(
    self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((clients) => {
      for (const client of clients) {
        if ("focus" in client) return client.focus();
      }
      if (self.clients.openWindow) return self.clients.openWindow("/app");
    })
  );
});
