import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environment: "node",
    // Los tests de hearts/integracion tocan la BD real (con datos de usar-y-tirar
    // que se limpian solos), asi que corren en serie para no pisarse entre ellos.
    fileParallelism: false,
  },
});
