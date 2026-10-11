import { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { loginUser } from "../utils/storage.js";
import "../styles/auth.css";

function Login() {
  const navigate = useNavigate();
  const location = useLocation();
  const justRegistered = location.state?.registered === true;

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  function handleSubmit(e) {
    e.preventDefault();

    const result = loginUser(username, password);
    if (!result.ok) {
      setError(result.error);
      return;
    }

    navigate("/landing");
  }

  return (
    <div className="auth-page">
      <form className="auth-card" onSubmit={handleSubmit}>
        <h1>Money Manager</h1>
        <p className="auth-sub">Log in to see your income and expenses.</p>

        {justRegistered && !error && (
          <p className="form-success" role="status">
            Account created. Please log in.
          </p>
        )}

        <label className="field">
          Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            autoComplete="username"
            required
          />
        </label>

        <label className="field">
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="current-password"
            required
          />
        </label>

        {error && <p className="form-error" role="alert">{error}</p>}

        <button type="submit" className="btn btn-primary">Log in</button>

        <p className="auth-switch">
          New here? <Link to="/register">Create an account</Link>
        </p>
      </form>
    </div>
  );
}

export default Login;
