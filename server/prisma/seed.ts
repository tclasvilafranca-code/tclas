import bcrypt from "bcryptjs";
import { prisma } from "../src/prisma";
import { TrackDef } from "../src/content/defs";
import { kidsTrack } from "../src/content/kidsTrack";
import { teensTrack } from "../src/content/teensTrack";
import { adultsTrack } from "../src/content/adultsTrack";

async function seedTrack(def: TrackDef) {
  const existing = await prisma.track.findUnique({ where: { code: def.code } });
  if (existing) {
    console.log(`  Track "${def.name}" ya existe, se omite.`);
    return existing;
  }

  const track = await prisma.track.create({
    data: { code: def.code, name: def.name, description: def.description, minAge: def.minAge, maxAge: def.maxAge, order: def.order },
  });

  for (const [li, level] of def.levels.entries()) {
    const lvl = await prisma.level.create({
      data: { trackId: track.id, index: li + 1, title: level.title, description: level.description, iconEmoji: level.iconEmoji ?? "🎹" },
    });
    for (const [ui, unit] of level.units.entries()) {
      const u = await prisma.unit.create({
        data: { levelId: lvl.id, index: ui + 1, title: unit.title, description: unit.description },
      });
      for (const [lei, lesson] of unit.lessons.entries()) {
        const les = await prisma.lesson.create({
          data: { unitId: u.id, index: lei + 1, title: lesson.title, description: lesson.description, xpReward: lesson.xpReward ?? 15 },
        });
        for (const [ei, ex] of lesson.exercises.entries()) {
          await prisma.exercise.create({
            data: {
              lessonId: les.id,
              index: ei + 1,
              type: ex.type,
              prompt: ex.prompt,
              data: JSON.stringify(ex.data),
              explanation: ex.explanation,
            },
          });
        }
      }
    }
  }

  const levelCount = def.levels.length;
  const unitCount = def.levels.reduce((a, l) => a + l.units.length, 0);
  const lessonCount = def.levels.reduce((a, l) => a + l.units.reduce((b, u) => b + u.lessons.length, 0), 0);
  console.log(`  Track "${def.name}": ${levelCount} niveles, ${unitCount} unidades, ${lessonCount} lecciones`);

  return track;
}

const BADGES = [
  { code: "primera_leccion", name: "Primeros acordes", description: "Completaste tu primera leccion", icon: "🎵" },
  { code: "racha_7", name: "Una semana de practica", description: "7 dias seguidos practicando", icon: "🔥" },
  { code: "racha_30", name: "Un mes de constancia", description: "30 dias seguidos practicando", icon: "🏅" },
  { code: "xp_100", name: "Cien puntos", description: "Alcanzaste 100 XP", icon: "⭐" },
  { code: "xp_500", name: "Quinientos puntos", description: "Alcanzaste 500 XP", icon: "🌟" },
];

async function main() {
  console.log("Sembrando base de datos de t-clas...");

  console.log("Creando badges...");
  for (const b of BADGES) {
    await prisma.badge.upsert({ where: { code: b.code }, update: b, create: b });
  }

  console.log("Creando tracks y curriculo...");
  const [, , adults] = await Promise.all([seedTrack(kidsTrack), seedTrack(teensTrack), seedTrack(adultsTrack)]);

  console.log("Creando cuenta de profesora (Azucena)...");
  const teacherPasswordHash = await bcrypt.hash("profesora123", 10);
  const teacher = await prisma.user.upsert({
    where: { email: "azucena@t-clas.com" },
    update: {},
    create: {
      email: "azucena@t-clas.com",
      passwordHash: teacherPasswordHash,
      name: "Azucena",
      role: "TEACHER",
    },
  });

  console.log("Creando alumno de demostracion...");
  const studentPasswordHash = await bcrypt.hash("alumno123", 10);
  const student = await prisma.user.upsert({
    where: { email: "alumno@t-clas.com" },
    update: {},
    create: {
      email: "alumno@t-clas.com",
      passwordHash: studentPasswordHash,
      name: "Alumno Demo",
      role: "STUDENT",
      studentProfile: {
        create: { ageGroup: "ADULTS", trackId: adults.id, onboarded: true, xpTotal: 25, streakCurrent: 2, streakLongest: 2, lastActivityDate: new Date() },
      },
    },
    include: { studentProfile: true },
  });

  const firstLesson = await prisma.lesson.findFirst({
    where: { unit: { level: { trackId: adults.id, index: 1 }, index: 1 } },
    orderBy: { index: "asc" },
  });
  if (firstLesson) {
    await prisma.progress.upsert({
      where: { userId_lessonId: { userId: student.id, lessonId: firstLesson.id } },
      update: {},
      create: { userId: student.id, lessonId: firstLesson.id, status: "COMPLETED", stars: 3, bestScore: 100, attempts: 1, completedAt: new Date() },
    });
    const badge = await prisma.badge.findUnique({ where: { code: "primera_leccion" } });
    if (badge) {
      await prisma.userBadge.upsert({
        where: { userId_badgeId: { userId: student.id, badgeId: badge.id } },
        update: {},
        create: { userId: student.id, badgeId: badge.id },
      });
    }
  }

  const hasAssignment = await prisma.assignment.findFirst({ where: { studentId: student.id } });
  if (!hasAssignment) {
    await prisma.assignment.create({
      data: {
        teacherId: teacher.id,
        studentId: student.id,
        lessonId: firstLesson?.id,
        classDate: new Date(),
        note: "Repasa esta leccion antes de nuestra proxima clase presencial y trae dudas sobre la cadencia I-IV-V-I.",
        status: "PENDING",
      },
    });
  }

  console.log("\n¡Listo! Cuentas de prueba:");
  console.log("  Profesora -> azucena@t-clas.com / profesora123");
  console.log("  Alumno    -> alumno@t-clas.com / alumno123");
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
