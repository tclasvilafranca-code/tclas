import { describe, it, expect, afterEach } from "vitest";
import { prisma } from "./prisma";
import { recomputeHearts, loseHeart } from "./gamification";

// Tests de integracion contra la base de datos local real (no mocks): crean su
// propio usuario de usar-y-tirar y lo borran al terminar, para no tocar datos
// reales de ningun alumno.
let createdUserIds: string[] = [];

async function makeTestProfile(overrides: Partial<{ heartsCurrent: number; heartsMax: number; heartsUpdatedAt: Date }> = {}) {
  const user = await prisma.user.create({
    data: {
      name: "Test Hearts",
      username: `test-hearts-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      pinHash: "x",
      role: "STUDENT",
      studentProfile: {
        create: {
          ageGroup: "KIDS",
          heartsCurrent: overrides.heartsCurrent ?? 5,
          heartsMax: overrides.heartsMax ?? 5,
          heartsUpdatedAt: overrides.heartsUpdatedAt ?? new Date(),
        },
      },
    },
    include: { studentProfile: true },
  });
  createdUserIds.push(user.id);
  return user.studentProfile!;
}

afterEach(async () => {
  for (const id of createdUserIds) {
    await prisma.studentProfile.deleteMany({ where: { userId: id } });
    await prisma.user.delete({ where: { id } });
  }
  createdUserIds = [];
});

describe("recomputeHearts", () => {
  it("no cambia nada si ya esta al maximo", async () => {
    const profile = await makeTestProfile({ heartsCurrent: 5, heartsMax: 5 });
    const result = await recomputeHearts(profile);
    expect(result.heartsCurrent).toBe(5);
  });

  it("no regenera corazones si no ha pasado suficiente tiempo", async () => {
    const profile = await makeTestProfile({ heartsCurrent: 2, heartsMax: 5, heartsUpdatedAt: new Date() });
    const result = await recomputeHearts(profile);
    expect(result.heartsCurrent).toBe(2);
  });

  it("regenera 1 corazon por cada 2h transcurridas, sin pasarse del maximo", async () => {
    const threeHoursAgo = new Date(Date.now() - 3 * 60 * 60 * 1000);
    const profile = await makeTestProfile({ heartsCurrent: 2, heartsMax: 5, heartsUpdatedAt: threeHoursAgo });
    const result = await recomputeHearts(profile);
    expect(result.heartsCurrent).toBe(3);
  });

  it("no supera heartsMax aunque haya pasado mucho tiempo", async () => {
    const aWeekAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
    const profile = await makeTestProfile({ heartsCurrent: 2, heartsMax: 5, heartsUpdatedAt: aWeekAgo });
    const result = await recomputeHearts(profile);
    expect(result.heartsCurrent).toBe(5);
  });
});

describe("loseHeart", () => {
  it("resta un corazon", async () => {
    const profile = await makeTestProfile({ heartsCurrent: 3, heartsMax: 5 });
    const result = await loseHeart(profile);
    expect(result.heartsCurrent).toBe(2);
  });

  it("nunca baja de 0", async () => {
    const profile = await makeTestProfile({ heartsCurrent: 0, heartsMax: 5 });
    const result = await loseHeart(profile);
    expect(result.heartsCurrent).toBe(0);
  });
});
