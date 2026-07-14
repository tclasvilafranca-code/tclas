import { LegalLayout, LegalPlaceholder } from "../../components/LegalLayout";

export function Privacidad() {
  return (
    <LegalLayout title="Política de privacidad" updated="13 de julio de 2026">
      <p>
        Esta política de privacidad explica cómo Teórico48 recoge, utiliza y protege los datos personales de sus
        usuarios, conforme al Reglamento (UE) 2016/679 (RGPD) y a la Ley Orgánica 3/2018 de Protección de Datos
        Personales y garantía de los derechos digitales (LOPDGDD).
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Responsable del tratamiento</h2>
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
          Email de contacto para ejercer derechos: <LegalPlaceholder>[email de contacto]</LegalPlaceholder>
        </li>
      </ul>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Datos que se recogen</h2>
      <ul className="list-disc space-y-1 pl-5">
        <li>Datos de registro: email y contraseña (la contraseña se almacena siempre cifrada, nunca en claro).</li>
        <li>Datos de uso: fecha de examen (opcional), resultados de simulacros, respuestas, progreso, XP, rachas y medallas conseguidas.</li>
        <li>
          Datos de compra: al comprar la licencia, antes incluso de crear una cuenta, el pago se procesa
          directamente por <strong>Stripe</strong>, pasarela de pago externa, que recoge tu email para poder
          enviarte el código de acceso. Teórico48 no almacena ni tiene acceso a los datos completos de tu tarjeta.
        </li>
        <li>Datos técnicos básicos derivados del uso del servicio (por ejemplo, fecha de conexión), en la medida necesaria para el funcionamiento y la seguridad de la aplicación.</li>
      </ul>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Finalidad del tratamiento</h2>
      <ul className="list-disc space-y-1 pl-5">
        <li>Gestionar tu cuenta y darte acceso a las funcionalidades de la aplicación.</li>
        <li>Generar y corregir los simulacros, calcular tu progreso, XP, rachas y medallas.</li>
        <li>Procesar el pago único de la licencia y generar el código de acceso para crear la cuenta.</li>
        <li>Enviarte comunicaciones estrictamente necesarias para el servicio (por ejemplo, un email para restablecer tu contraseña si lo solicitas).</li>
      </ul>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Legitimación</h2>
      <p>
        El tratamiento se basa en la ejecución del contrato de prestación del Servicio (compra de la licencia,
        registro y uso de la aplicación) y, cuando corresponda, en tu consentimiento expreso.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Plazo de conservación</h2>
      <p>
        Los datos se conservan mientras mantengas tu cuenta activa. Si solicitas la baja o la supresión de tus
        datos, se eliminarán o anonimizarán salvo que deba conservarse alguna información por obligación legal
        (por ejemplo, facturación).
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Destinatarios y encargados del tratamiento</h2>
      <p>Para poder prestar el Servicio, algunos datos se comparten con los siguientes proveedores, que actúan como encargados del tratamiento:</p>
      <ul className="list-disc space-y-1 pl-5">
        <li><strong>Stripe</strong> (procesamiento del pago de la licencia).</li>
        <li><strong>Render</strong> u otro proveedor de alojamiento (hosting de la aplicación y la base de datos).</li>
        <li><strong>Resend</strong> u otro proveedor de email transaccional (restablecimiento de contraseña, verificación de email y aviso de nuevas compras).</li>
      </ul>
      <p>No se venden ni ceden datos a terceros con fines publicitarios.</p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Tus derechos</h2>
      <p>
        Puedes ejercer en cualquier momento tus derechos de acceso, rectificación, supresión, oposición,
        limitación del tratamiento y portabilidad de tus datos, escribiendo a{" "}
        <LegalPlaceholder>[email de contacto]</LegalPlaceholder>. También tienes derecho a presentar una
        reclamación ante la Agencia Española de Protección de Datos (
        <a href="https://www.aepd.es" target="_blank" rel="noreferrer" className="font-semibold text-t48-blue">
          www.aepd.es
        </a>
        ) si consideras que el tratamiento de tus datos no se ajusta a la normativa.
      </p>

      <h2 className="mt-2 text-lg font-bold text-t48-ink">Seguridad</h2>
      <p>
        Las contraseñas se almacenan cifradas (hash), nunca en texto plano. Se aplican medidas técnicas y
        organizativas razonables para proteger tus datos frente a accesos no autorizados, pérdida o alteración.
      </p>
    </LegalLayout>
  );
}
