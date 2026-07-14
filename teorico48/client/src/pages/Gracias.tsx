import { Link } from "react-router-dom";
import { CheckCircle } from "../components/Icons";

export function Gracias() {
  return (
    <div className="mx-auto max-w-md px-4 py-16 text-center">
      <div className="card-lift rounded-3xl border border-slate-200 bg-white p-8">
        <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-t48-green/10 text-t48-green-dark">
          <CheckCircle className="h-7 w-7" />
        </div>
        <h1 className="mt-4 text-2xl font-extrabold tracking-tight text-t48-ink">¡Pago recibido!</h1>
        <p className="mt-3 text-sm text-slate-500">
          En breve recibirás un email con tu código de acceso y las instrucciones para crear tu cuenta y empezar a
          practicar. Si no lo ves en unos minutos, revisa la carpeta de spam.
        </p>
        <Link to="/register" className="btn-primary mt-7 inline-flex px-6 py-2.5">
          Ya tengo mi código
        </Link>
      </div>
    </div>
  );
}
