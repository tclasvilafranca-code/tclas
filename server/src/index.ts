import "dotenv/config";
import express from "express";
import cors from "cors";
import authRoutes from "./routes/auth";
import contentRoutes from "./routes/content";
import teacherRoutes from "./routes/teacher";

const app = express();
app.use(cors());
app.use(express.json());

app.get("/api/health", (_req, res) => res.json({ ok: true, service: "t-clas piano API" }));

app.use("/api/auth", authRoutes);
app.use("/api", contentRoutes);
app.use("/api/teacher", teacherRoutes);

app.use((err: any, _req: express.Request, res: express.Response, _next: express.NextFunction) => {
  console.error(err);
  res.status(500).json({ error: "Error interno del servidor" });
});

const PORT = Number(process.env.PORT) || 4000;
app.listen(PORT, () => {
  console.log(`t-clas API escuchando en http://localhost:${PORT}`);
});
