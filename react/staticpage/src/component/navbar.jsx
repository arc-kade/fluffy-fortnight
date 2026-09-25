import { Link } from "react-router-dom";
function Navbar(){
    return(
        <nav>
            <div>
                <h2>My website</h2>
                <Link to="/">Home </Link>
                <Link to="/services">Services </Link>
                <Link to="/about">About </Link>
                <Link to="/help">Help </Link>
            </div>
        </nav>
    )
}
export default Navbar;