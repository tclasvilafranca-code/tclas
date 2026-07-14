import { useEffect, useState } from "react";
import { Download, XCircle } from "./Icons";

const DISMISS_KEY = "installPromptDismissed";

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed" }>;
}

function isStandalone() {
  return (
    window.matchMedia("(display-mode: standalone)").matches ||
    (window.navigator as unknown as { standalone?: boolean }).standalone === true
  );
}

function isIOS() {
  return /iphone|ipad|ipod/i.test(window.navigator.userAgent);
}

/** Ofrece instalar la app en escritorio/móvil: usa el diálogo nativo del
 * navegador cuando está disponible (Chrome, Edge, Android) y, si no, unas
 * instrucciones manuales cortas (Safari no dispara "beforeinstallprompt"). */
export function InstallAppPrompt() {
  const [deferredPrompt, setDeferredPrompt] = useState<BeforeInstallPromptEvent | null>(null);
  const [dismissed, setDismissed] = useState(() => localStorage.getItem(DISMISS_KEY) === "1");
  const [installed, setInstalled] = useState(false);
  const [showManual, setShowManual] = useState(false);

  useEffect(() => {
    if (isStandalone()) {
      setInstalled(true);
      return;
    }
    function handleBeforeInstall(e: Event) {
      e.preventDefault();
      setDeferredPrompt(e as BeforeInstallPromptEvent);
    }
    function handleInstalled() {
      setInstalled(true);
      setDeferredPrompt(null);
    }
    window.addEventListener("beforeinstallprompt", handleBeforeInstall);
    window.addEventListener("appinstalled", handleInstalled);
    return () => {
      window.removeEventListener("beforeinstallprompt", handleBeforeInstall);
      window.removeEventListener("appinstalled", handleInstalled);
    };
  }, []);

  function dismiss() {
    localStorage.setItem(DISMISS_KEY, "1");
    setDismissed(true);
  }

  async function handleInstallClick() {
    if (!deferredPrompt) {
      setShowManual((v) => !v);
      return;
    }
    await deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    setDeferredPrompt(null);
  }

  if (installed || dismissed) return null;

  return (
    <div className="mt-4 flex items-start justify-between gap-3 rounded-2xl border border-t48-blue/20 bg-t48-blue/5 px-4 py-3.5 text-sm">
      <div className="flex items-start gap-3">
        <div className="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue">
          <Download className="h-4.5 w-4.5" />
        </div>
        <div>
          <p className="font-bold text-t48-ink">Ten Teórico48 en tu escritorio</p>
          <p className="mt-0.5 text-slate-500">Instálala como una app: abre más rápido y sin la barra del navegador.</p>
          {showManual && !deferredPrompt && (
            <p className="mt-2 text-xs text-slate-500">
              {isIOS()
                ? 'En Safari: pulsa el icono de Compartir y elige "Añadir a pantalla de inicio".'
                : 'En el menú del navegador (⋮ o ⋯ arriba a la derecha), elige "Instalar Teórico48" o "Añadir a pantalla de inicio".'}
            </p>
          )}
          <button onClick={handleInstallClick} className="btn-primary mt-2.5 px-3.5 py-1.5 text-xs">
            {deferredPrompt ? "Instalar ahora" : "¿Cómo la instalo?"}
          </button>
        </div>
      </div>
      <button onClick={dismiss} aria-label="Cerrar" className="text-slate-300 transition-colors hover:text-slate-500">
        <XCircle className="h-5 w-5" />
      </button>
    </div>
  );
}
