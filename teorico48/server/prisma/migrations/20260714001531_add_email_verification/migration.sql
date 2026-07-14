-- AlterTable
ALTER TABLE "users" ADD COLUMN     "emailVerified" BOOLEAN NOT NULL DEFAULT false,
ADD COLUMN     "verifyTokenExpiresAt" TIMESTAMP(3),
ADD COLUMN     "verifyTokenHash" TEXT;
