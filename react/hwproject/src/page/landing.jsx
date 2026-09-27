import { Outlet } from "react-router-dom";
import Navbar from '../components/navbar.jsx';
function Landing(){
    return(
        <>
        <Navbar />
        <h1>This is the landing page. Welcome in!</h1>
            <Outlet />
       
        </>
    )
}
export default Landing;