import type { ReactNode } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import { Landing } from "./pages/Landing";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";
import { Home } from "./pages/Home";
import { Lesson } from "./pages/Lesson";
import { TeacherDashboard } from "./pages/TeacherDashboard";
import { TeacherStudentDetail } from "./pages/TeacherStudentDetail";

function Splash() {
  return <div className="min-h-screen flex items-center justify-center text-tclas-ink/40">Cargando t-clas...</div>;
}

function RequireStudent({ children }: { children: ReactNode }) {
  const { me, loading } = useAuth();
  if (loading) return <Splash />;
  if (!me) return <Navigate to="/login" replace />;
  if (me.role !== "STUDENT") return <Navigate to="/teacher" replace />;
  return children;
}

function RequireTeacher({ children }: { children: ReactNode }) {
  const { me, loading } = useAuth();
  if (loading) return <Splash />;
  if (!me) return <Navigate to="/login" replace />;
  if (me.role !== "TEACHER") return <Navigate to="/app" replace />;
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
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<RedirectIfLoggedIn><Login /></RedirectIfLoggedIn>} />
      <Route path="/register" element={<RedirectIfLoggedIn><Register /></RedirectIfLoggedIn>} />
      <Route path="/app" element={<RequireStudent><Home /></RequireStudent>} />
      <Route path="/app/lesson/:id" element={<RequireStudent><Lesson /></RequireStudent>} />
      <Route path="/teacher" element={<RequireTeacher><TeacherDashboard /></RequireTeacher>} />
      <Route path="/teacher/students/:id" element={<RequireTeacher><TeacherStudentDetail /></RequireTeacher>} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
