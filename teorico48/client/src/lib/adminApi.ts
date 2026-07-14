const API_BASE = import.meta.env.VITE_API_URL ?? "";
const ADMIN_TOKEN_KEY = "adminToken";

export class AdminApiError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.status = status;
  }
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = localStorage.getItem(ADMIN_TOKEN_KEY);
  const res = await fetch(`${API_BASE}/api/admin${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...(options.headers ?? {}),
    },
  });

  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    if (res.status === 401) localStorage.removeItem(ADMIN_TOKEN_KEY);
    throw new AdminApiError(data.error ?? "Error de red", res.status);
  }
  return data as T;
}

export interface AccessCode {
  id: string;
  code: string;
  note: string | null;
  createdAt: string;
  expiresAt: string | null;
  usedAt: string | null;
  usedByEmail: string | null;
}

export const adminApi = {
  isLoggedIn: () => !!localStorage.getItem(ADMIN_TOKEN_KEY),
  logout: () => localStorage.removeItem(ADMIN_TOKEN_KEY),
  login: async (password: string) => {
    const { token } = await request<{ token: string }>("/login", {
      method: "POST",
      body: JSON.stringify({ password }),
    });
    localStorage.setItem(ADMIN_TOKEN_KEY, token);
  },
  listCodes: () => request<{ codes: AccessCode[] }>("/access-codes"),
  generateCodes: (input: { count: number; note?: string; expiresInDays?: number }) =>
    request<{ codes: AccessCode[] }>("/access-codes", {
      method: "POST",
      body: JSON.stringify(input),
    }),
};
