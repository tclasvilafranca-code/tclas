import { Route, Routes } from "react-router-dom";
import { NavBar } from "./components/NavBar";
import { ProtectedRoute } from "./components/ProtectedRoute";
import { Landing } from "./pages/Landing";
import { Login, Register } from "./pages/Login";
import { Dashboard } from "./pages/Dashboard";
import { TestRunner } from "./pages/TestRunner";
import { Results } from "./pages/Results";
import { Paywall } from "./pages/Paywall";

export default function App() {
  return (
    <div className="min-h-screen">
      <NavBar />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
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
      </Routes>
    </div>
  );
}
