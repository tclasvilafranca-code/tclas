-- AlterTable
ALTER TABLE "RepertoireEntry" ADD COLUMN     "nextReviewAt" TIMESTAMP(3),
ADD COLUMN     "reviewStage" INTEGER NOT NULL DEFAULT 0;
