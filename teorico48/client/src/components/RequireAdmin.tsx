import type { ReactNode } from "react";
import { Navigate } from "react-router-dom";
import { adminApi } from "../lib/adminApi";

export function RequireAdmin({ children }: { children: ReactNode }) {
  if (!adminApi.isLoggedIn()) return <Navigate to="/admin/login" replace />;
  return <>{children}</>;
}
