import { Route, Routes, useLocation } from "react-router-dom";
import { NavBar } from "./components/NavBar";
import { Footer } from "./components/Footer";
import { ScrollToTop } from "./components/ScrollToTop";
import { ProtectedRoute } from "./components/ProtectedRoute";
import { RequireAdmin } from "./components/RequireAdmin";
import { Landing } from "./pages/Landing";
import { Login, Register } from "./pages/Login";
import { ForgotPassword } from "./pages/ForgotPassword";
import { ResetPassword } from "./pages/ResetPassword";
import { VerifyEmail } from "./pages/VerifyEmail";
import { Dashboard } from "./pages/Dashboard";
import { CategoryStats } from "./pages/CategoryStats";
import { TeoriaExpress } from "./pages/TeoriaExpress";
import { TestRunner } from "./pages/TestRunner";
import { Results } from "./pages/Results";
import { Paywall } from "./pages/Paywall";
import { Gracias } from "./pages/Gracias";
import { NotFound } from "./pages/NotFound";
import { AvisoLegal } from "./pages/legal/AvisoLegal";
import { Privacidad } from "./pages/legal/Privacidad";
import { Terminos } from "./pages/legal/Terminos";
import { AdminLogin } from "./pages/admin/AdminLogin";
import { AdminPanel } from "./pages/admin/AdminPanel";

export default function App() {
  const { pathname } = useLocation();
  // El panel de administrador es una sesión totalmente distinta a la de los
  // usuarios: no tiene sentido mostrar la navegación ni el pie de página normales.
  const isAdminArea = pathname.startsWith("/admin");

  return (
    <div className="flex min-h-screen flex-col">
      <ScrollToTop />
      {!isAdminArea && <NavBar />}
      <div className="flex-1">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/comprar/gracias" element={<Gracias />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/reset-password" element={<ResetPassword />} />
          <Route path="/verify-email" element={<VerifyEmail />} />
          <Route path="/legal" element={<AvisoLegal />} />
          <Route path="/privacidad" element={<Privacidad />} />
          <Route path="/terminos" element={<Terminos />} />
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teoria"
            element={
              <ProtectedRoute>
                <TeoriaExpress />
              </ProtectedRoute>
            }
          />
          <Route
            path="/categorias"
            element={
              <ProtectedRoute>
                <CategoryStats />
              </ProtectedRoute>
            }
          />
          <Route
            path="/learn"
            element={
              <ProtectedRoute>
                <TestRunner mode="learn" />
              </ProtectedRoute>
            }
          />
          <Route
            path="/exam"
            element={
              <ProtectedRoute>
                <TestRunner mode="exam" />
              </ProtectedRoute>
            }
          />
          <Route
            path="/review"
            element={
              <ProtectedRoute>
                <TestRunner mode="review" />
              </ProtectedRoute>
            }
          />
          <Route
            path="/results"
            element={
              <ProtectedRoute>
                <Results />
              </ProtectedRoute>
            }
          />
          <Route
            path="/paywall"
            element={
              <ProtectedRoute>
                <Paywall />
              </ProtectedRoute>
            }
          />
          <Route path="/admin/login" element={<AdminLogin />} />
          <Route
            path="/admin"
            element={
              <RequireAdmin>
                <AdminPanel />
              </RequireAdmin>
            }
          />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
      {!isAdminArea && <Footer />}
    </div>
  );
}
