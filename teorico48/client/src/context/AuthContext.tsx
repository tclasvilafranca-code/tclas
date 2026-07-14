import { createContext, useContext, useEffect, useState } from "react";
import type { ReactNode } from "react";
import { api, SESSION_EXPIRED_EVENT } from "../lib/api";
import type { User } from "../lib/api";

interface AuthContextValue {
  user: User | null;
  loading: boolean;
  sessionExpired: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, acceptedTerms: boolean, accessCode: string) => Promise<void>;
  logout: () => void;
  refreshUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [sessionExpired, setSessionExpired] = useState(false);

  async function refreshUser() {
    if (!localStorage.getItem("token")) {
      setUser(null);
      return;
    }
    try {
      const { user } = await api.me();
      setUser(user);
    } catch {
      localStorage.removeItem("token");
      setUser(null);
    }
  }

  useEffect(() => {
    refreshUser().finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    function handleSessionExpired() {
      setUser(null);
      setSessionExpired(true);
    }
    window.addEventListener(SESSION_EXPIRED_EVENT, handleSessionExpired);
    return () => window.removeEventListener(SESSION_EXPIRED_EVENT, handleSessionExpired);
  }, []);

  async function login(email: string, password: string) {
    const { token, user } = await api.login(email, password);
    localStorage.setItem("token", token);
    setUser(user);
    setSessionExpired(false);
  }

  async function register(email: string, password: string, acceptedTerms: boolean, accessCode: string) {
    const { token, user } = await api.register(email, password, acceptedTerms, accessCode);
    localStorage.setItem("token", token);
    setUser(user);
    setSessionExpired(false);
  }

  function logout() {
    localStorage.removeItem("token");
    setUser(null);
    setSessionExpired(false);
  }

  return (
    <AuthContext.Provider value={{ user, loading, sessionExpired, login, register, logout, refreshUser }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth debe usarse dentro de AuthProvider");
  return ctx;
}
