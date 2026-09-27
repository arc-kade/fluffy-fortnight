import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';
function Login() {
    const navigate = useNavigate();
    const [username,setUsername] = useState("")
    const [password,setPassword] = useState("")
    const [error, setError] = useState("")
    const handleLogin = (e) => {
        e.preventDefault()
        const users = JSON.parse(localStorage.getItem("users") || "{}");
        const user = users[username];
        if (user && user.password === password) {
            navigate("/landing")
        } else {
            setError("Invalid username or password")
        }
    }
    return (
        <div>
            <h1>Login</h1>
            <form action="" onSubmit={handleLogin}>
                <input type="text" placeholder="username" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                {error && <p style={{ color: "red" }}>{error}</p>}
                <button type="submit">Login</button>
            </form>
            <h4>New user? <button>
                <Link to="/register">Register</Link>
            </button></h4>
        </div>
    )
}
export default Login;