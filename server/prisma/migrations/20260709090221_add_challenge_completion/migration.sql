-- CreateTable
CREATE TABLE "ChallengeCompletion" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "challengeCode" TEXT NOT NULL,
    "weekStart" TIMESTAMP(3) NOT NULL,
    "xpAwarded" INTEGER NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "ChallengeCompletion_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "ChallengeCompletion_userId_challengeCode_weekStart_key" ON "ChallengeCompletion"("userId", "challengeCode", "weekStart");

-- AddForeignKey
ALTER TABLE "ChallengeCompletion" ADD CONSTRAINT "ChallengeCompletion_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
