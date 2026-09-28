import { Navigate, Outlet } from "react-router-dom";

function ProtectedRoute() {
    const isLoggedIn = localStorage.getItem("isLoggedIn");
    if(!isLoggedIn){
        return <Navigate to="/" replace />;
    }

    return isLoggedIn ? <Outlet /> : <Navigate to="/" replace />;
}

export default ProtectedRoute;