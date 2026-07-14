import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./App";
import { AuthProvider } from "./context/AuthContext";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  </StrictMode>
);

// Habilita que la app se pueda instalar (icono en el móvil, pantalla
// completa) y que las recargas sean más rápidas. Solo en producción: en
// desarrollo interferiría con el recargado en caliente de Vite.
if ("serviceWorker" in navigator && import.meta.env.PROD) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").catch((err) => console.error("No se pudo registrar el service worker:", err));
  });
}
