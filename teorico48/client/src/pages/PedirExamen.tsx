import { useNavigate } from "react-router-dom";
import { Calendar, CheckCircle } from "../components/Icons";

const DGT_SOLICITUD_URL = "https://sede.dgt.gob.es/es/permisos-de-conducir/obtencion-y-gestion-de-permisos/solicitud-de-prueba-de-aptitud-de-examen/";

export function PedirExamen() {
  const navigate = useNavigate();

  return (
    <div className="mx-auto max-w-2xl px-4 py-8 sm:py-10">
      <button onClick={() => navigate("/dashboard")} className="text-sm font-semibold text-slate-500 transition-colors hover:text-t48-ink">
        ← Volver al panel
      </button>
      <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-t48-ink">Pide tu cita para el examen real</h1>
      <p className="mt-1.5 text-slate-500">
        Cuando te sientas preparado, así es como se gestiona de verdad la cita del examen teórico en España. El
        trámite es distinto según cómo te estés preparando.
      </p>

      <div className="card-lift mt-6 rounded-2xl border border-slate-200 bg-white p-6">
        <h2 className="font-bold text-t48-ink">Si vas por autoescuela</h2>
        <p className="mt-2 text-sm text-slate-500">
          Ellos gestionan todo el trámite por ti: pagan la tasa, piden tu informe psicofísico y te asignan la cita.
          Solo tienes que avisarles de que ya te sientes listo para presentarte.
        </p>
      </div>

      <div className="card-lift mt-4 rounded-2xl border border-slate-200 bg-white p-6">
        <h2 className="font-bold text-t48-ink">Si vas por libre (sin autoescuela)</h2>
        <ol className="mt-3 space-y-4 text-sm text-slate-600">
          <Step n={1} title="Consigue el informe de aptitud psicofísica">
            Acude a un Centro de Reconocimiento de Conductores autorizado (búscalo cerca de ti) e indica que es
            para el permiso de conducir. El informe solo es válido durante 90 días, así que pídelo cerca de la
            fecha en que vayas a solicitar el examen.
          </Step>
          <Step n={2} title="Paga la tasa en la Sede Electrónica de la DGT">
            Es la Tasa 2.1 (94,05 € en el momento de escribir esto) y te da derecho a dos convocatorias de examen.
            Se paga antes de registrar la solicitud.
          </Step>
          <Step n={3} title="Presenta la solicitud de la prueba de aptitud">
            Puedes hacerlo online (con Cl@ve, certificado digital o DNI electrónico) o en persona en tu Jefatura
            de Tráfico. Necesitarás: DNI/NIE en vigor, una foto reciente, el informe psicofísico y el justificante
            del pago de la tasa.
          </Step>
          <Step n={4} title="Recibe tu citación">
            La DGT te confirma por email la fecha y hora del examen. También puedes pedir o consultar cita previa
            desde la web o la app de la DGT, o llamando al 060.
          </Step>
        </ol>

        <a
          href={DGT_SOLICITUD_URL}
          target="_blank"
          rel="noopener noreferrer"
          className="btn-primary mt-5 inline-flex px-5 py-2.5 text-sm"
        >
          <Calendar className="h-4 w-4" />
          Ir a la Sede Electrónica de la DGT
        </a>
      </div>

      <p className="mt-5 flex items-start gap-2 text-xs text-slate-400">
        <CheckCircle className="mt-0.5 h-3.5 w-3.5 shrink-0" />
        Esta guía es orientativa: la DGT puede cambiar el procedimiento, las tasas o los requisitos. Comprueba
        siempre la información oficial y actualizada en sede.dgt.gob.es antes de hacer el trámite.
      </p>
    </div>
  );
}

function Step({ n, title, children }: { n: number; title: string; children: string }) {
  return (
    <li className="flex gap-3">
      <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-t48-blue/10 text-xs font-bold text-t48-blue">
        {n}
      </span>
      <div>
        <p className="font-semibold text-t48-ink">{title}</p>
        <p className="mt-0.5 text-slate-500">{children}</p>
      </div>
    </li>
  );
}
