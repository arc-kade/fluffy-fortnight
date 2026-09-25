import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login(){
    const navigate = useNavigate();
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const handleLogin = (e)=>{
        e.preventDefault()
        if (username==="admin"&&password==="1234"){
            navigate("/mainpage")
        }else{
            alert("Invalid username or password")
        }
    }
return(
    <div>
        <h1>Login</h1>
        <form action="" onSubmit={handleLogin}>
            <input type="text" placeholder="username" value={username} onChange={(e)=>setUsername(e.target.value)}/>
            <input type="password" placeholder="password" value={password} onChange={(e)=>setPassword(e.target.value)} />
            <button type="submit">Login</button>
        </form>
    </div>
)}
export default Login;