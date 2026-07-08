import { api } from "./api";

export function isPushSupported(): boolean {
  return "serviceWorker" in navigator && "PushManager" in window;
}

export function registerServiceWorker() {
  if (!("serviceWorker" in navigator)) return;
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").catch((err) => console.warn("No se pudo registrar el service worker:", err));
  });
}

function urlBase64ToUint8Array(base64: string): Uint8Array {
  const padding = "=".repeat((4 - (base64.length % 4)) % 4);
  const base64Safe = (base64 + padding).replace(/-/g, "+").replace(/_/g, "/");
  const raw = atob(base64Safe);
  return Uint8Array.from([...raw].map((c) => c.charCodeAt(0)));
}

export async function getPushSubscriptionStatus(): Promise<boolean> {
  try {
    const res = await api.get<{ subscribed: boolean }>("/push/status");
    return res.subscribed;
  } catch {
    return false;
  }
}

/** Pide permiso de notificaciones y suscribe este navegador a los recordatorios
 * de practica. Devuelve un mensaje de error legible si algo falla (permiso
 * denegado, navegador sin soporte, servidor sin VAPID configurado, etc). */
export async function subscribeToPush(): Promise<{ ok: boolean; error?: string }> {
  if (!isPushSupported()) return { ok: false, error: "Tu navegador no soporta notificaciones push." };

  const { publicKey, configured } = await api.get<{ publicKey: string | null; configured: boolean }>("/push/vapid-public-key");
  if (!configured || !publicKey) return { ok: false, error: "Los recordatorios todavia no estan activados en el servidor." };

  const permission = await Notification.requestPermission();
  if (permission !== "granted") return { ok: false, error: "Has bloqueado los permisos de notificaciones." };

  const registration = await navigator.serviceWorker.ready;
  const subscription = await registration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: urlBase64ToUint8Array(publicKey) as BufferSource,
  });

  const json = subscription.toJSON();
  await api.post("/push/subscribe", { endpoint: json.endpoint, keys: json.keys });
  return { ok: true };
}

export async function unsubscribeFromPush(): Promise<void> {
  if (!isPushSupported()) return;
  const registration = await navigator.serviceWorker.ready;
  const subscription = await registration.pushManager.getSubscription();
  if (!subscription) return;
  await api.post("/push/unsubscribe", { endpoint: subscription.endpoint });
  await subscription.unsubscribe();
}
