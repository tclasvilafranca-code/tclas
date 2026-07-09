import { prisma } from "./prisma";

export interface MessageDTO {
  id: string;
  body: string;
  fromMe: boolean;
  createdAt: string;
}

/** Trae el hilo completo entre dos personas (profesor/a<->alumno/a) y marca
 * como leidos, de paso, los mensajes que le hayan llegado a quien pide el
 * hilo: abrir la conversacion es lo que la "lee". */
export async function getThread(meId: string, otherId: string): Promise<MessageDTO[]> {
  const messages = await prisma.message.findMany({
    where: {
      OR: [
        { senderId: meId, recipientId: otherId },
        { senderId: otherId, recipientId: meId },
      ],
    },
    orderBy: { createdAt: "asc" },
  });

  const unreadIds = messages.filter((m) => m.recipientId === meId && !m.readAt).map((m) => m.id);
  if (unreadIds.length > 0) {
    await prisma.message.updateMany({ where: { id: { in: unreadIds } }, data: { readAt: new Date() } });
  }

  return messages.map((m) => ({
    id: m.id,
    body: m.body,
    fromMe: m.senderId === meId,
    createdAt: m.createdAt.toISOString(),
  }));
}

export async function sendMessage(fromId: string, toId: string, body: string) {
  return prisma.message.create({ data: { senderId: fromId, recipientId: toId, body } });
}

export async function countUnread(meId: string, fromId?: string): Promise<number> {
  return prisma.message.count({ where: { recipientId: meId, readAt: null, ...(fromId ? { senderId: fromId } : {}) } });
}
