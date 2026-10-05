import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

function AdminLogin() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    function handleLogin(e) {
        e.preventDefault();
        let admins = {};
        try {
            admins = JSON.parse(localStorage.getItem("admins") || "{}");
        } catch { }

        const admin = admins[username];
        if (admin && admin.password === password) {
            localStorage.setItem("adminLoggedIn", "true");
            navigate("/admin");
        } else {
            setError("Invalid admin credentials");
        }
    }

    return (
        <div>
            <h1>Admin Login</h1>
            <form onSubmit={handleLogin}>
                <input type="text" placeholder="admin username" value={username}
                    onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="password" value={password}
                    onChange={(e) => setPassword(e.target.value)} />
                {error && <p style={{ color: "red" }}>{error}</p>}
                <button type="submit">Login</button>
            </form>
            <h4>Register new admin<button>
                <Link to="/adminregister">Register</Link>
            </button></h4>
        </div>
    );
}

export default AdminLogin;