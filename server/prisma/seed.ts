import bcrypt from "bcryptjs";
import { prisma } from "../src/prisma";
import { arnauPieces } from "../src/content/pieces";
import { createRepertoireEntryWithLessons, regenerateLessonsForEntry } from "../src/repertoire";

// Fases del generador actual: si un alumno tiene lecciones con fases antiguas
// (de una version anterior del generador), se regeneran automaticamente para
// no dejar sesiones a medio migrar.
const CURRENT_PHASES = new Set(["VISUAL_AGILITY", "EAR_ACUITY", "NOTE_RUSH", "SHEET_PRACTICE"]);

const BADGES = [
  { code: "primera_leccion", name: "Primeros acordes", description: "Completaste tu primera leccion", icon: "🎵" },
  { code: "racha_7", name: "Una semana de practica", description: "7 dias seguidos practicando", icon: "🔥" },
  { code: "racha_30", name: "Un mes de constancia", description: "30 dias seguidos practicando", icon: "🏅" },
  { code: "xp_100", name: "Cien puntos", description: "Alcanzaste 100 XP", icon: "⭐" },
  { code: "xp_500", name: "Quinientos puntos", description: "Alcanzaste 500 XP", icon: "🌟" },
];

function addWeeks(date: Date, weeks: number): Date {
  const d = new Date(date);
  d.setDate(d.getDate() + weeks * 7);
  return d;
}

async function main() {
  console.log("Sembrando base de datos de t-clas...");

  console.log("Creando badges...");
  for (const b of BADGES) {
    await prisma.badge.upsert({ where: { code: b.code }, update: b, create: b });
  }

  console.log("Creando cuenta de profesora (Azucena)...");
  const teacherPasswordHash = await bcrypt.hash("profesora123", 10);
  const teacher = await prisma.user.upsert({
    where: { email: "azucena@t-clas.com" },
    update: {},
    create: { email: "azucena@t-clas.com", passwordHash: teacherPasswordHash, name: "Azucena", role: "TEACHER" },
  });

  console.log("Creando biblioteca de piezas...");
  const pieceRecords = [];
  for (const def of arnauPieces) {
    const pieceFields = {
      composer: def.composer ?? "",
      arranger: def.arranger ?? "",
      ageGroup: def.ageGroup,
      difficultyTier: def.difficultyTier,
      defaultWeeks: def.defaultWeeks ?? 3,
      keySignature: def.keySignature,
      timeSignature: def.timeSignature,
      seasonalTag: def.seasonalTag,
      iconEmoji: def.iconEmoji ?? "🎵",
      aboutText: def.aboutText ?? "",
      tips: def.tips ?? "",
      content: JSON.stringify(def.content),
    };
    const piece = await prisma.piece.upsert({
      where: { title: def.title },
      update: pieceFields,
      create: { title: def.title, ...pieceFields },
    });
    pieceRecords.push(piece);
  }
  console.log(`  ${pieceRecords.length} piezas en la biblioteca.`);

  console.log("Creando alumno de demostracion (Arnau)...");
  let arnauUsername = "arnau";
  let arnauPin: string | null = null;
  const existingArnau = await prisma.user.findUnique({ where: { username: arnauUsername }, include: { studentProfile: true } });

  let arnau = existingArnau;
  if (!existingArnau) {
    arnauPin = "1234";
    const pinHash = await bcrypt.hash(arnauPin, 10);
    arnau = await prisma.user.create({
      data: {
        name: "Arnau",
        username: arnauUsername,
        pinHash,
        role: "STUDENT",
        studentProfile: {
          create: { ageGroup: "KIDS", teacherId: teacher.id, onboarded: true, xpTotal: 0, streakCurrent: 0 },
        },
      },
      include: { studentProfile: true },
    });
  }

  if (arnau?.studentProfile) {
    const existingRepertoire = await prisma.repertoireEntry.findFirst({ where: { studentId: arnau.studentProfile.id } });
    if (!existingRepertoire) {
      console.log("Asignando el repertorio del curso a Arnau...");
      // Empieza "hoy" para que la demo sea usable desde el primer dia
      // (en un alumno real, la profesora elige la fecha real de inicio del curso).
      let cursor = new Date();
      for (const [i, piece] of pieceRecords.entries()) {
        await createRepertoireEntryWithLessons({
          studentProfileId: arnau.studentProfile.id,
          piece,
          orderIndex: i + 1,
          startDate: cursor,
          durationWeeks: piece.defaultWeeks,
          status: i === 0 ? "ACTIVE" : "UPCOMING",
        });
        cursor = addWeeks(cursor, piece.defaultWeeks);
      }
      console.log(`  ${pieceRecords.length} piezas asignadas, curso de septiembre a ${cursor.toISOString().slice(0, 10)}.`);
    } else {
      console.log("  Arnau ya tenia repertorio asignado, se omite.");
    }

    const entries = await prisma.repertoireEntry.findMany({
      where: { studentId: arnau.studentProfile.id },
      include: { lessons: { take: 1, include: { exercises: { take: 1 } } } },
    });
    const pieceById = new Map(pieceRecords.map((p) => [p.id, p]));
    for (const entry of entries) {
      const firstPhase = entry.lessons[0]?.exercises[0]?.phase;
      if (firstPhase && !CURRENT_PHASES.has(firstPhase)) {
        const piece = pieceById.get(entry.pieceId);
        if (piece) {
          console.log(`  Regenerando lecciones de "${piece.title}" con el nuevo formato de sesion...`);
          await regenerateLessonsForEntry(entry.id, piece, entry.durationWeeks);
        }
      }
    }
  }

  console.log("\n¡Listo! Cuentas de acceso:");
  console.log("  Profesora -> azucena@t-clas.com / profesora123");
  if (arnauPin) {
    console.log(`  Arnau (alumno) -> usuario: ${arnauUsername} / PIN: ${arnauPin}`);
  } else {
    console.log(`  Arnau (alumno) -> usuario: ${arnauUsername} (PIN ya asignado previamente)`);
  }
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
