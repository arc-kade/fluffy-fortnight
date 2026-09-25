import { Link } from "react-router-dom";


function Index(){
    return(
        <div>
        <Link to="/login" > Login </Link>
        <Link to="/mainpage">Main Page</Link>
        </div>
    )
}
export default Index;