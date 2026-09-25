import { Link,NavLink } from "react-router-dom";
import './navbar.css'
function Navbar(){
    return(
        <nav>
            <h2>My website</h2>
            <div>
                <NavLink to="home" >Home </NavLink>
                <NavLink to="services" className={({isActive})=>isActive? "active":"" }>Services </NavLink>
                <NavLink to="about" >About </NavLink>
                <NavLink to="help" >Help </NavLink>
            </div>
        </nav>
    )
}
export default Navbar;