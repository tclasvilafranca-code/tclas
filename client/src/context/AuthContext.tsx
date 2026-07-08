import { createContext, useCallback, useContext, useEffect, useState } from "react";
import type { ReactNode } from "react";
import { api, getToken, setToken, clearToken } from "../lib/api";
import type { Me } from "../lib/api";

interface AuthContextValue {
  me: Me | null;
  loading: boolean;
  loginTeacher: (email: string, password: string) => Promise<Me>;
  loginStudent: (username: string, pin: string) => Promise<Me>;
  registerTeacher: (name: string, email: string, password: string) => Promise<Me>;
  logout: () => void;
  refresh: () => Promise<void>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [me, setMe] = useState<Me | null>(null);
  const [loading, setLoading] = useState(true);

  const refresh = useCallback(async () => {
    if (!getToken()) {
      setMe(null);
      setLoading(false);
      return;
    }
    try {
      const data = await api.get<Me>("/auth/me");
      setMe(data);
    } catch {
      clearToken();
      setMe(null);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    refresh();
  }, [refresh]);

  const loginTeacher = useCallback(async (email: string, password: string) => {
    const data = await api.post<{ token: string; user: Me }>("/auth/login", { email, password });
    setToken(data.token);
    const full = await api.get<Me>("/auth/me");
    setMe(full);
    return full;
  }, []);

  const loginStudent = useCallback(async (username: string, pin: string) => {
    const data = await api.post<{ token: string; user: Me }>("/auth/student-login", { username, pin });
    setToken(data.token);
    const full = await api.get<Me>("/auth/me");
    setMe(full);
    return full;
  }, []);

  const registerTeacher = useCallback(async (name: string, email: string, password: string) => {
    const data = await api.post<{ token: string; user: Me }>("/auth/register", { name, email, password });
    setToken(data.token);
    const full = await api.get<Me>("/auth/me");
    setMe(full);
    return full;
  }, []);

  const logout = useCallback(() => {
    clearToken();
    setMe(null);
  }, []);

  return (
    <AuthContext.Provider value={{ me, loading, loginTeacher, loginStudent, registerTeacher, logout, refresh }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth debe usarse dentro de AuthProvider");
  return ctx;
}
