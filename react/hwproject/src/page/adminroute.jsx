import { Navigate } from "react-router-dom";

function AdminRoute({ children }) {
  const ok = localStorage.getItem("adminLoggedIn") === "true";
  return ok ? children : <Navigate to="/adminlogin" replace />;
}

export default AdminRoute;