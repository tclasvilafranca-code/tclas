import { NextFunction, Request, Response } from "express";

type AsyncRouteHandler = (req: Request, res: Response, next: NextFunction) => Promise<unknown>;

/**
 * Express 4 no reenvia automaticamente los rechazos de promesas de los
 * handlers async al middleware de errores: sin este wrapper, un error
 * inesperado (p. ej. una caida puntual de la base de datos) se convierte en
 * una promesa rechazada sin capturar y puede tumbar el proceso entero.
 */
export function asyncHandler(fn: AsyncRouteHandler) {
  return (req: Request, res: Response, next: NextFunction) => {
    fn(req, res, next).catch(next);
  };
}
