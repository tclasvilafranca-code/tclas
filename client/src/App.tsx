import type { ReactNode } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import { Landing } from "./pages/Landing";
import { Register } from "./pages/Register";
import { Inicio } from "./pages/Inicio";
import { Aprender } from "./pages/Aprender";
import { Practicar } from "./pages/Practicar";
import { Perfil } from "./pages/Perfil";
import { Lesson } from "./pages/Lesson";
import { TeacherDashboard } from "./pages/TeacherDashboard";
import { TeacherStudentDetail } from "./pages/TeacherStudentDetail";
import { AppShell } from "./components/AppShell";
import { Metronome } from "./components/Metronome";
import { ForceChangePinScreen } from "./components/ForceChangePinScreen";

function Splash() {
  return <div className="min-h-screen flex items-center justify-center text-tclas-ink/40">Cargando t-clas...</div>;
}

function RequireStudent({ children }: { children: ReactNode }) {
  const { me, loading } = useAuth();
  if (loading) return <Splash />;
  if (!me) return <Navigate to="/" replace />;
  if (me.role !== "STUDENT") return <Navigate to="/teacher" replace />;
  if (me.mustChangePin) return <ForceChangePinScreen />;
  return (
    <>
      {children}
      <Metronome />
    </>
  );
}

function RequireTeacher({ children }: { children: ReactNode }) {
  const { me, loading } = useAuth();
  if (loading) return <Splash />;
  if (!me) return <Navigate to="/" replace />;
  if (me.role !== "TEACHER") return <Navigate to="/app" replace />;
  if (me.mustChangePin) return <ForceChangePinScreen />;
  return children;
}

function RedirectIfLoggedIn({ children }: { children: ReactNode }) {
  const { me, loading } = useAuth();
  if (loading) return <Splash />;
  if (me) return <Navigate to={me.role === "TEACHER" ? "/teacher" : "/app"} replace />;
  return children;
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<RedirectIfLoggedIn><Landing /></RedirectIfLoggedIn>} />
      <Route path="/login" element={<Navigate to="/" replace />} />
      <Route path="/register" element={<RedirectIfLoggedIn><Register /></RedirectIfLoggedIn>} />
      <Route path="/app" element={<RequireStudent><AppShell /></RequireStudent>}>
        <Route index element={<Inicio />} />
        <Route path="aprender" element={<Aprender />} />
        <Route path="practicar" element={<Practicar />} />
        <Route path="perfil" element={<Perfil />} />
      </Route>
      <Route path="/app/lesson/:id" element={<RequireStudent><Lesson /></RequireStudent>} />
      <Route path="/teacher" element={<RequireTeacher><TeacherDashboard /></RequireTeacher>} />
      <Route path="/teacher/students/:id" element={<RequireTeacher><TeacherStudentDetail /></RequireTeacher>} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
