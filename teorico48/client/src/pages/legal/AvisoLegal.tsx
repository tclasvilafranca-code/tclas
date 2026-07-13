import { LegalLayout, LegalPlaceholder } from "../../components/LegalLayout";

export function AvisoLegal() {
  return (
    <LegalLayout title="Aviso legal" updated="13 de julio de 2026">
      <p>
        En cumplimiento del artículo 10 de la Ley 34/2002, de 11 de julio, de Servicios de la Sociedad de la
        Información y de Comercio Electrónico (LSSI-CE), se ponen a disposición de los usuarios los siguientes
        datos identificativos del titular de este sitio web y de la aplicación Teórico48 (en adelante, "Teórico48"
        o "el Servicio"):
      </p>

      <ul className="list-disc space-y-1 pl-5">
        <li>
          Titular: <LegalPlaceholder>[Nombre completo o razón social]</LegalPlaceholder>
        </li>
        <li>
          NIF/CIF: <LegalPlaceholder>[NIF o CIF]</LegalPlaceholder>
        </li>
        <li>
          Domicilio: <LegalPlaceholder>[Dirección postal completa]</LegalPlaceholder>
        </li>
        <li>
          Email de contacto: <LegalPlaceholder>[email de contacto]</LegalPlaceholder>
        </li>
      </ul>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Objeto</h2>
      <p>
        Teórico48 es una aplicación web de preparación del examen teórico del permiso de conducir, que ofrece
        simulacros de examen, repaso de fallos y seguimiento del progreso del usuario. El acceso a determinadas
        funciones (simulacros ilimitados y repaso de fallos) requiere la contratación del producto de pago único
        "Pack 48h".
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Condiciones de acceso y uso</h2>
      <p>
        El acceso a Teórico48 es gratuito en su modalidad básica, sin perjuicio del coste de conexión a internet
        que corresponda al usuario. El uso del Servicio atribuye la condición de usuario y supone la aceptación
        plena de este aviso legal, de los{" "}
        <a href="/terminos" className="font-semibold text-t48-blue">
          términos de uso
        </a>{" "}
        y de la{" "}
        <a href="/privacidad" className="font-semibold text-t48-blue">
          política de privacidad
        </a>
        .
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Propiedad intelectual e industrial</h2>
      <p>
        El nombre "Teórico48", su logotipo, diseño, estructura de navegación, y el contenido de las preguntas y
        explicaciones del banco de tests son propiedad de su titular o se utilizan con la debida autorización, y
        están protegidos por la normativa de propiedad intelectual e industrial. Queda prohibida su reproducción,
        distribución o comunicación pública total o parcial sin autorización expresa.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Exactitud y finalidad educativa del contenido</h2>
      <p>
        El contenido de Teórico48 tiene una finalidad exclusivamente educativa y de entrenamiento. No se trata de
        un banco de preguntas oficial de la Dirección General de Tráfico (DGT) ni de ninguna autoescuela, y no
        garantiza la superación del examen oficial, que depende de la preparación y el desempeño de cada persona.
        Se procura que el contenido sea preciso y esté actualizado, pero puede contener errores u omisiones;
        recomendamos contrastarlo con fuentes oficiales antes de presentarse al examen real.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Legislación aplicable y jurisdicción</h2>
      <p>
        Este aviso legal se rige por la legislación española. Para la resolución de cualquier controversia, las
        partes se someten a los juzgados y tribunales que correspondan conforme a la normativa de protección de
        consumidores y usuarios aplicable.
      </p>
    </LegalLayout>
  );
}
