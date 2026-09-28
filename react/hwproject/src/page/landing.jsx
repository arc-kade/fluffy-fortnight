import { Outlet,Link } from "react-router-dom";
import { Navigate, useNavigate } from "react-router-dom";
import Navbar from '../components/navbar.jsx';
import StudentForm from "./studentforms.jsx";
function Landing(){
    const navigate = useNavigate();
    const handleLogout = () => {
    console.log("Before:", localStorage.getItem("isLoggedIn"));

    localStorage.removeItem("isLoggedIn");

    console.log("After:", localStorage.getItem("isLoggedIn"));

    navigate("/");
};
    return(
        <>
        <Navbar />
        <h1>This is the landing page. Welcome in!</h1>
            <Outlet />
        <button onClick={handleLogout}>Logout</button>
        <br />
        <br />
        <br />
        <StudentForm />
        </>
        
    )
}
export default Landing;