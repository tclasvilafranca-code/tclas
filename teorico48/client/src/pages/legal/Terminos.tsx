import { LegalLayout, LegalPlaceholder } from "../../components/LegalLayout";

export function Terminos() {
  return (
    <LegalLayout title="Términos de uso" updated="13 de julio de 2026">
      <h2 className="mt-2 text-lg font-bold text-t48-ink">1. Objeto y aceptación</h2>
      <p>
        Estos términos regulan el uso de Teórico48, aplicación web de preparación del examen teórico del permiso
        de conducir mediante simulacros, repaso de fallos y funciones de progreso y gamificación. Al crear una
        cuenta, aceptas íntegramente estos términos, el{" "}
        <a href="/legal" className="font-semibold text-t48-blue">
          aviso legal
        </a>{" "}
        y la{" "}
        <a href="/privacidad" className="font-semibold text-t48-blue">
          política de privacidad
        </a>
        .
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">2. Descripción del servicio</h2>
      <p>
        Teórico48 ofrece, en su plan gratuito, un simulacro de examen al día y seguimiento básico de progreso. El
        producto de pago único "Pack 48h" desbloquea simulacros ilimitados y el modo de repaso centrado en las
        preguntas falladas por el usuario, sin límite de tiempo de acceso ni renovación automática: es un pago
        único, no una suscripción.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">3. Registro y responsabilidad del usuario</h2>
      <p>
        Para usar Teórico48 debes registrarte con un email y una contraseña. Eres responsable de mantener la
        confidencialidad de tus credenciales y de toda actividad realizada desde tu cuenta. Debes proporcionar
        datos veraces en el registro.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">4. Precio, pago y derecho de desistimiento</h2>
      <p>
        El precio del Pack 48h se muestra en la propia aplicación antes de iniciar el pago e incluye los impuestos
        aplicables. El pago se procesa a través de Stripe. Al tratarse de contenido y funcionalidades digitales
        que se activan de forma inmediata tras el pago, al contratar el Pack 48h el usuario solicita expresamente
        el inicio de la prestación del servicio antes de que finalice el plazo legal de desistimiento de 14 días
        naturales, por lo que dicho derecho de desistimiento no resultará de aplicación una vez el acceso premium
        haya sido activado, conforme al artículo 103.m) del Real Decreto Legislativo 1/2007. Si consideras que ha
        habido un error en el cobro, contacta con <LegalPlaceholder>[email de contacto]</LegalPlaceholder> antes de
        iniciar cualquier disputa con tu banco.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">5. Naturaleza educativa del contenido</h2>
      <p>
        El banco de preguntas de Teórico48 es contenido original elaborado con fines educativos, inspirado en la
        normativa pública de tráfico. No es un banco de preguntas oficial de la DGT ni de ninguna autoescuela, y
        no garantiza la superación del examen oficial: el resultado depende de la preparación de cada usuario.
        Teórico48 no sustituye la formación de una autoescuela ni el estudio del manual oficial correspondiente.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">6. Uso aceptable</h2>
      <p>
        No está permitido: intentar acceder a cuentas de otros usuarios, extraer o reutilizar de forma masiva el
        contenido del banco de preguntas con fines comerciales, ni interferir con el funcionamiento normal del
        Servicio.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">7. Disponibilidad y modificaciones</h2>
      <p>
        Teórico48 se presta "tal cual" y "según disponibilidad". Podemos modificar, suspender o interrumpir el
        Servicio, así como actualizar estos términos, informando de los cambios relevantes con antelación
        razonable cuando sea posible.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">8. Limitación de responsabilidad</h2>
      <p>
        En la medida permitida por la ley, Teórico48 no será responsable de los resultados obtenidos por el
        usuario en el examen oficial del permiso de conducir, ni de daños indirectos derivados del uso del
        Servicio.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">9. Legislación aplicable</h2>
      <p>
        Estos términos se rigen por la legislación española. Si eres consumidor, dispones de los mecanismos de
        resolución de conflictos y de reclamación previstos en la normativa de consumo aplicable.
      </p>
    </LegalLayout>
  );
}
