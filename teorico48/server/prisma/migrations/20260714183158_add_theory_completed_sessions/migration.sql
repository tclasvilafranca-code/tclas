-- AlterTable
ALTER TABLE "users" ADD COLUMN     "theoryCompletedSessions" TEXT[] DEFAULT ARRAY[]::TEXT[];
