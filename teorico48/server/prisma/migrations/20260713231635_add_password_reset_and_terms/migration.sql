-- AlterTable
ALTER TABLE "users" ADD COLUMN     "resetTokenExpiresAt" TIMESTAMP(3),
ADD COLUMN     "resetTokenHash" TEXT,
ADD COLUMN     "termsAcceptedAt" TIMESTAMP(3);
