import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';
function Register() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [confirmPassword, setConfirmPassword] = useState("")
    const [error, setError] = useState("");

    const handleRegister = (e) => {
        e.preventDefault()
        if (password !== confirmPassword) {
            setError("Please re-enter the same password")
            return;
        }
        const users = JSON.parse(localStorage.getItem("users") || "{}"); //Pulls the current dictionary of registered users out of localStorage (or starts with an empty object

        if (users[username]) {
            setError("Username already taken");
            return;
        }
        if (username.toLowerCase() === "admin") {
            setError("That username is reserved");
            return;
        }
        users[username] = { password, role: "user" };
        users[username] = { password };
        localStorage.setItem("users", JSON.stringify(users));

        navigate("/login");
    }
    return (
        <div>
            <h1>Register</h1>
            <form action="" onSubmit={handleRegister}>
                <input type="text" placeholder="set username" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <input type="password" placeholder="confirm password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
                {error && <p style={{ color: "red" }}>{error}</p>}
                <button type="submit">Register</button>
            </form>
            <h4>Already have an account? <button >
                <Link to="/login" > Login </Link>
            </button></h4>
        </div>
    )
}
export default Register;