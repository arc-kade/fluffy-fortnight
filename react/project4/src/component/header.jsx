import {useContext} from 'react';
import UserContext from "../context/UserContext";
function Header(){
    const {user,setUser} = useContext(UserContext)
    return(
        <div> 
        <h1>Welcome, {user}</h1>
        <button onClick={()=>setUser("Doe")}>Change Name</button>
        </div>
    )
}
export default Header;

