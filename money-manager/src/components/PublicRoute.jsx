import { Navigate } from "react-router-dom";
import { getCurrentUser } from "../utils/storage.js";

// Login and register pages: logged-in users skip straight to the landing page
function PublicRoute({ children }) {
  return getCurrentUser() ? <Navigate to="/landing" replace /> : children;
}

export default PublicRoute;
