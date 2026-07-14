import { useEffect } from "react";
import { useLocation } from "react-router-dom";

/** React Router no hace scroll al inicio al cambiar de ruta: sin esto, una
 * página larga (p. ej. el examen) deja la siguiente pantalla (resultados)
 * scrolleada a mitad de página en vez de mostrar la cabecera. */
export function ScrollToTop() {
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  return null;
}
