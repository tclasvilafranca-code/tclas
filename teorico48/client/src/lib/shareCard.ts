export interface ShareCardData {
  percent: number;
  score: number;
  total: number;
  passed: boolean;
  isLearnMode: boolean;
  level: number;
  streak: number;
  xpGained: number;
}

const WIDTH = 1080;
const HEIGHT = 1920;

function roundedRect(ctx: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

function loadImage(src: string): Promise<HTMLImageElement> {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

/** Dibuja una imagen cubriendo todo el rectángulo destino, recortando el sobrante (como object-fit: cover). */
function drawCover(ctx: CanvasRenderingContext2D, img: HTMLImageElement, x: number, y: number, w: number, h: number) {
  const scale = Math.max(w / img.width, h / img.height);
  const sw = w / scale;
  const sh = h / scale;
  const sx = (img.width - sw) / 2;
  const sy = (img.height - sh) / 2;
  ctx.drawImage(img, sx, sy, sw, sh, x, y, w, h);
}

function statChip(ctx: CanvasRenderingContext2D, x: number, y: number, w: number, label: string) {
  const h = 96;
  ctx.fillStyle = "rgba(255,255,255,0.12)";
  roundedRect(ctx, x, y, w, h, 20);
  ctx.fill();
  ctx.strokeStyle = "rgba(255,255,255,0.25)";
  ctx.lineWidth = 2;
  roundedRect(ctx, x, y, w, h, 20);
  ctx.stroke();
  ctx.fillStyle = "#FFFFFF";
  ctx.font = "700 34px Manrope, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(label, x + w / 2, y + h / 2 + 2);
}

/** Genera la imagen de resultado (formato historia, 1080x1920) para compartir
 * en redes. Usa Canvas puro, sin librerías, y la foto ya presente en la
 * Landing para mantener la misma identidad visual. */
export async function renderShareCard(data: ShareCardData): Promise<Blob> {
  await document.fonts.ready;

  const canvas = document.createElement("canvas");
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  const ctx = canvas.getContext("2d");
  if (!ctx) throw new Error("Canvas no soportado");

  // Fondo: foto de carretera + oscurecido, igual que el hero de la Landing.
  ctx.fillStyle = "#111827";
  ctx.fillRect(0, 0, WIDTH, HEIGHT);
  try {
    const img = await loadImage("/images/hero-road.jpg");
    drawCover(ctx, img, 0, 0, WIDTH, HEIGHT);
  } catch {
    // Si la foto no carga (por ejemplo, sin conexión), se queda el fondo oscuro liso.
  }
  ctx.fillStyle = "rgba(17, 24, 39, 0.62)";
  ctx.fillRect(0, 0, WIDTH, HEIGHT);
  const bottomGradient = ctx.createLinearGradient(0, HEIGHT * 0.45, 0, HEIGHT);
  bottomGradient.addColorStop(0, "rgba(17, 24, 39, 0)");
  bottomGradient.addColorStop(1, "rgba(17, 24, 39, 0.75)");
  ctx.fillStyle = bottomGradient;
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  // Marca, arriba a la izquierda.
  roundedRect(ctx, 80, 96, 84, 84, 20);
  ctx.fillStyle = "#2563EB";
  ctx.fill();
  ctx.fillStyle = "#FFFFFF";
  ctx.font = "800 34px Manrope, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText("48", 80 + 42, 96 + 44);
  ctx.textAlign = "left";
  ctx.font = "800 46px Manrope, sans-serif";
  ctx.fillText("Teórico48", 186, 96 + 44);

  // Etiqueta de estado.
  const eyebrow = data.isLearnMode ? "SESIÓN DE APRENDIZAJE" : data.passed ? "SIMULACRO SUPERADO" : "SIMULACRO";
  ctx.font = "800 32px Manrope, sans-serif";
  ctx.fillStyle = "#93C5FD";
  ctx.textAlign = "center";
  ctx.fillText(eyebrow, WIDTH / 2, 640);

  // Número grande.
  ctx.font = "800 280px Manrope, sans-serif";
  ctx.fillStyle = "#FFFFFF";
  ctx.fillText(`${data.percent}%`, WIDTH / 2, 900);

  // Estado / subtítulo.
  const statusColor = data.isLearnMode ? "#93C5FD" : data.passed ? "#4ADE80" : "#F87171";
  const statusText = data.isLearnMode
    ? `${data.score}/${data.total} correctas`
    : data.passed
    ? "¡Aprobado!"
    : "Suspenso, pero cerca";
  ctx.font = "800 64px Manrope, sans-serif";
  ctx.fillStyle = statusColor;
  ctx.fillText(statusText, WIDTH / 2, 1020);

  ctx.font = "500 38px Manrope, sans-serif";
  ctx.fillStyle = "rgba(255,255,255,0.8)";
  ctx.fillText(`${data.score}/${data.total} preguntas correctas`, WIDTH / 2, 1090);

  // Chips de estadísticas.
  const chipY = 1220;
  const chipGap = 24;
  const chipWidth = (WIDTH - 160 - chipGap * 2) / 3;
  statChip(ctx, 80, chipY, chipWidth, `Nivel ${data.level}`);
  statChip(ctx, 80 + chipWidth + chipGap, chipY, chipWidth, `${data.streak}d racha`);
  statChip(ctx, 80 + (chipWidth + chipGap) * 2, chipY, chipWidth, `+${data.xpGained} XP`);

  // Pie: llamada a la acción, coherente con el acceso por código.
  ctx.font = "700 40px Manrope, sans-serif";
  ctx.fillStyle = "#FFFFFF";
  ctx.fillText("¿Quieres el código de acceso?", WIDTH / 2, HEIGHT - 220);
  ctx.font = "700 40px Manrope, sans-serif";
  ctx.fillText("Pregúntame.", WIDTH / 2, HEIGHT - 168);

  ctx.font = "600 30px Manrope, sans-serif";
  ctx.fillStyle = "rgba(255,255,255,0.65)";
  ctx.fillText("Aprende. Practica. Aprueba.", WIDTH / 2, HEIGHT - 90);

  return new Promise((resolve, reject) => {
    canvas.toBlob((blob) => (blob ? resolve(blob) : reject(new Error("No se pudo generar la imagen"))), "image/png");
  });
}
