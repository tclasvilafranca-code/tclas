import { useEffect, useState } from "react";
import { isPushSupported, getPushSubscriptionStatus, subscribeToPush, unsubscribeFromPush } from "../lib/push";

export function NotificationsToggle() {
  const [supported] = useState(isPushSupported());
  const [subscribed, setSubscribed] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!supported) return;
    getPushSubscriptionStatus().then(setSubscribed);
  }, [supported]);

  if (!supported) return null;

  async function toggle() {
    setBusy(true);
    setError(null);
    try {
      if (subscribed) {
        await unsubscribeFromPush();
        setSubscribed(false);
      } else {
        const result = await subscribeToPush();
        if (result.ok) setSubscribed(true);
        else setError(result.error ?? "No se pudo activar");
      }
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="inline-flex flex-col items-start">
      <button
        onClick={toggle}
        disabled={busy}
        className={`text-xs font-semibold rounded-full px-3 py-1.5 border transition-colors disabled:opacity-50
          ${subscribed ? "bg-tclas-sage/10 border-tclas-sage/40 text-tclas-sage" : "bg-tclas-ink/5 border-tclas-ink/15 text-tclas-ink/60 hover:border-tclas-plum/40"}`}
      >
        {subscribed ? "🔔 Recordatorios activados" : "🔕 Activar recordatorios de práctica"}
      </button>
      {error && <p className="text-[11px] text-tclas-rose mt-1">{error}</p>}
    </div>
  );
}
