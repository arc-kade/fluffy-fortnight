import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

const ADMIN_ACCESS_CODE = "school-admin-2026"; // change this

function AdminRegister() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [accessCode, setAccessCode] = useState("");
    const [error, setError] = useState("");

    function handleRegister(e) {
        e.preventDefault();

        if (accessCode !== ADMIN_ACCESS_CODE) {
            setError("Invalid admin access code");
            return;
        }
        if (password !== confirmPassword) {
            setError("Please re-enter the same password");
            return;
        }

        let admins = {};
        try {
            admins = JSON.parse(localStorage.getItem("admins") || "{}");
        } catch { }

        if (admins[username]) {
            setError("Admin username already taken");
            return;
        }

        admins[username] = { password };
        localStorage.setItem("admins", JSON.stringify(admins));
        navigate("/adminlogin");
    }

    return (
        <div>
            <h1>Admin Registration</h1>
            <form onSubmit={handleRegister}>
                <input type="text" placeholder="admin username" value={username}
                    onChange={(e) => setUsername(e.target.value)} required />
                <input type="password" placeholder="password" value={password}
                    onChange={(e) => setPassword(e.target.value)} required />
                <input type="password" placeholder="confirm password" value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)} required />
                <input type="password" placeholder="admin access code" value={accessCode}
                    onChange={(e) => setAccessCode(e.target.value)} required />
                {error && <p style={{ color: "red" }}>{error}</p>}
                <button type="submit">Register Admin</button>
            </form>
            <h4>Existing Admin login:<button>
                <Link to="/admin">Login</Link>
            </button></h4>
        </div>
    );
}

export default AdminRegister;