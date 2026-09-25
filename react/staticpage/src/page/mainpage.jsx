import { Outlet } from "react-router-dom";
import Navbar from "../component/navbar.jsx";
function MainPage(){
    return(
        <>
        <Navbar />
   
            <Outlet />
       
        </>
    )
}
export default MainPage;