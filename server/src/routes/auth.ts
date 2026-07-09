import { Router } from "express";
import bcrypt from "bcryptjs";
import { z } from "zod";
import { prisma } from "../prisma";
import { signToken, requireAuth, requireRole, AuthedRequest } from "../auth";
import { recomputeHearts } from "../gamification";

const router = Router();

const registerSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6),
  name: z.string().min(1),
});

// Solo para profesores: los alumnos no se autoregistran, su cuenta la crea el/la profesor/a
// desde el panel (ver /teacher/students) y reciben un usuario + PIN para entrar.
router.post("/register", async (req, res) => {
  const parsed = registerSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });
  }
  const { email, password, name } = parsed.data;

  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    return res.status(409).json({ error: "Ya existe una cuenta con ese email" });
  }

  const passwordHash = await bcrypt.hash(password, 10);
  const user = await prisma.user.create({
    data: { email, passwordHash, name, role: "TEACHER" },
  });

  const token = signToken({ userId: user.id, role: "TEACHER" });
  res.status(201).json({ token, user: { id: user.id, email: user.email, name: user.name, role: user.role } });
});

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string(),
});

router.post("/login", async (req, res) => {
  const parsed = loginSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Datos invalidos" });
  }
  const { email, password } = parsed.data;
  const user = await prisma.user.findUnique({ where: { email } });
  if (!user || !user.passwordHash) return res.status(401).json({ error: "Credenciales incorrectas" });
  const valid = await bcrypt.compare(password, user.passwordHash);
  if (!valid) return res.status(401).json({ error: "Credenciales incorrectas" });

  const token = signToken({ userId: user.id, role: user.role as "STUDENT" | "TEACHER" });
  res.json({ token, user: { id: user.id, email: user.email, name: user.name, role: user.role } });
});

const pinLoginSchema = z.object({
  username: z.string().min(1),
  pin: z.string().min(1),
});

// Entrada por usuario+PIN: pensada originalmente solo para alumnado, pero el
// mecanismo (buscar por username, comprobar PIN) no depende del rol, asi que
// tambien sirve para que una profesora entre igual de simple sin email ni
// contrasena. El rol devuelto es siempre el real de la cuenta (nunca se
// asume "STUDENT"), para que cada quien llegue a su propio panel.
router.post("/pin-login", async (req, res) => {
  const parsed = pinLoginSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });
  const { username, pin } = parsed.data;

  const user = await prisma.user.findUnique({ where: { username: username.toLowerCase() } });
  if (!user || !user.pinHash) return res.status(401).json({ error: "Usuario o PIN incorrectos" });
  const valid = await bcrypt.compare(pin, user.pinHash);
  if (!valid) return res.status(401).json({ error: "Usuario o PIN incorrectos" });

  const token = signToken({ userId: user.id, role: user.role as "STUDENT" | "TEACHER" });
  res.json({ token, user: { id: user.id, name: user.name, role: user.role, username: user.username } });
});

const changePasswordSchema = z.object({
  currentPassword: z.string().min(1),
  newPassword: z.string().min(6),
});

// Solo para profesores (email+password); los alumnos usan PIN y lo cambia
// su profesora desde el panel, no aqui. No habia ninguna forma de cambiar
// la contrasena una vez creada la cuenta.
router.post("/change-password", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = changePasswordSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });

  const user = await prisma.user.findUnique({ where: { id: req.auth!.userId } });
  if (!user || !user.passwordHash) return res.status(400).json({ error: "Esta cuenta no usa contrasena" });

  const valid = await bcrypt.compare(parsed.data.currentPassword, user.passwordHash);
  if (!valid) return res.status(401).json({ error: "La contrasena actual no es correcta" });

  const newHash = await bcrypt.hash(parsed.data.newPassword, 10);
  await prisma.user.update({ where: { id: user.id }, data: { passwordHash: newHash } });
  res.json({ ok: true });
});

const setPinAccessSchema = z.object({
  username: z
    .string()
    .trim()
    .toLowerCase()
    .regex(/^[a-z0-9]{3,16}$/, "El usuario debe tener entre 3 y 16 letras/numeros, sin espacios ni simbolos"),
  pin: z.string().regex(/^\d{4,6}$/, "El PIN debe tener entre 4 y 6 numeros"),
});

// Autoservicio para que la profesora se ponga (o cambie) su propio usuario+PIN,
// como el que ya tienen sus alumnos: entra con su email+contrasena de siempre,
// lo configura una vez, y desde entonces puede entrar tambien con usuario+PIN
// (ver /auth/pin-login). Solo para profesores: el PIN del alumnado lo gestiona
// la profesora desde su panel, no cada alumno por su cuenta.
// No marca mustChangePin: a diferencia del PIN por defecto (1234) de un
// alumno nuevo, aqui es la propia profesora quien elige su PIN a proposito,
// asi que se queda como definitivo sin pedirle confirmarlo otra vez.
router.post("/set-pin-access", requireAuth, requireRole("TEACHER"), async (req: AuthedRequest, res) => {
  const parsed = setPinAccessSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: parsed.error.errors[0]?.message ?? "Datos invalidos" });
  const { username, pin } = parsed.data;

  const existing = await prisma.user.findUnique({ where: { username } });
  if (existing && existing.id !== req.auth!.userId) {
    return res.status(409).json({ error: "Ese usuario ya esta en uso" });
  }

  const pinHash = await bcrypt.hash(pin, 10);
  await prisma.user.update({ where: { id: req.auth!.userId }, data: { username, pinHash, mustChangePin: false } });
  res.json({ ok: true, username });
});

const changePinSchema = z.object({
  newPin: z.string().regex(/^\d{4,6}$/, "El PIN debe tener entre 4 y 6 numeros"),
});

// Cambiar el propio PIN: lo usa cualquier cuenta (alumno o profesor/a) para
// salir del PIN por defecto (1234) la primera vez que entra, y sirve tambien
// como cambio de PIN normal despues. No pide el PIN actual porque ya se
// acaba de usar para autenticar esta misma sesion.
router.post("/change-pin", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = changePinSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: parsed.error.errors[0]?.message ?? "Datos invalidos" });

  const pinHash = await bcrypt.hash(parsed.data.newPin, 10);
  await prisma.user.update({ where: { id: req.auth!.userId }, data: { pinHash, mustChangePin: false } });
  res.json({ ok: true });
});

router.get("/me", requireAuth, async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({
    where: { id: req.auth!.userId },
    include: { studentProfile: { include: { teacher: { select: { name: true } } } } },
  });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  const teacherName = user.studentProfile?.teacher?.name ?? null;
  let studentProfile = user.studentProfile ? (({ teacher, ...rest }) => rest)(user.studentProfile) : null;
  if (studentProfile) {
    studentProfile = await recomputeHearts(studentProfile);
  }

  res.json({
    id: user.id,
    email: user.email,
    username: user.username,
    name: user.name,
    role: user.role,
    mustChangePin: user.mustChangePin,
    teacherName,
    studentProfile,
  });
});

export default router;
