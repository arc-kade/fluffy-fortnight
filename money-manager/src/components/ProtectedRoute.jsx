import { Navigate } from "react-router-dom";
import { getCurrentUser } from "../utils/storage.js";

// Only logged-in users may see the children; everyone else goes to /login
function ProtectedRoute({ children }) {
  return getCurrentUser() ? children : <Navigate to="/login" replace />;
}

export default ProtectedRoute;
