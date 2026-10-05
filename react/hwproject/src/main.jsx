export function seedAdmin() {
  try {
    const admins = JSON.parse(localStorage.getItem("admins") || "{}");
    if (!admins.admin) {
      admins.admin = { password: "admin123" }; // change this
      localStorage.setItem("admins", JSON.stringify(admins));
    }
  } catch {
    localStorage.setItem("admins", JSON.stringify({ admin: { password: "admin123" } }));
  }
}
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
