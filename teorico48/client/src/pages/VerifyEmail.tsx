import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api, ApiError } from "../lib/api";
import { CheckCircle, XCircle } from "../components/Icons";

export function VerifyEmail() {
  const [params] = useSearchParams();
  const { refreshUser } = useAuth();
  const uid = params.get("uid");
  const token = params.get("token");

  const [status, setStatus] = useState<"loading" | "success" | "error">("loading");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!uid || !token) {
      setStatus("error");
      setError("Este enlace no es válido.");
      return;
    }
    api
      .verifyEmail(uid, token)
      .then(() => {
        setStatus("success");
        refreshUser();
      })
      .catch((err) => {
        setStatus("error");
        setError(err instanceof ApiError ? err.message : "No se pudo verificar el email.");
      });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [uid, token]);

  return (
    <div className="mx-auto max-w-sm px-4 py-20 text-center">
      <div className="rounded-2xl border border-slate-200 bg-white p-8 shadow-sm">
        {status === "loading" && <p className="text-slate-500">Verificando tu email...</p>}
        {status === "success" && (
          <>
            <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-t48-green/10 text-t48-green-dark">
              <CheckCircle className="h-6 w-6" />
            </div>
            <p className="mt-4 font-bold text-t48-ink">Email verificado correctamente</p>
            <Link
              to="/dashboard"
              className="mt-5 inline-block rounded-md bg-t48-blue px-4 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark"
            >
              Ir a mi panel
            </Link>
          </>
        )}
        {status === "error" && (
          <>
            <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-t48-red/10 text-t48-red">
              <XCircle className="h-6 w-6" />
            </div>
            <p className="mt-4 font-medium text-t48-red">{error}</p>
            <Link to="/dashboard" className="mt-4 inline-block font-semibold text-t48-blue">
              Ir a mi panel
            </Link>
          </>
        )}
      </div>
    </div>
  );
}
