export interface Env {
  HYPERDRIVE: Hyperdrive;
  RATE_LIMIT_KV: KVNamespace;

  JWT_SECRET: string;
  CLIENT_URL: string;
  STRIPE_SECRET_KEY: string;
  STRIPE_PACK_PRICE_ID: string;
  STRIPE_WEBHOOK_SECRET: string;
  RESEND_API_KEY: string;
  MAIL_FROM: string;
  ADMIN_PASSWORD: string;
  OWNER_EMAIL: string;
}
