import { useState, useMemo } from "react";
import { useNavigate } from "react-router-dom";
import "../page/studentforms.css";

function readJSON(key, fallback) {
  try {
    return JSON.parse(localStorage.getItem(key)) ?? fallback;
  } catch {
    return fallback;
  }
}

// unique values, ignoring case and extra spaces ("CS" and "cs " count as one)
function uniqueOptions(values) {
  const map = new Map();
  values.forEach(v => {
    const label = (v || "").trim();
    const key = label.toLowerCase();
    if (key && !map.has(key)) map.set(key, label);
  });
  return [...map.entries()]
    .map(([key, label]) => ({ key, label }))
    .sort((a, b) => a.label.localeCompare(b.label));
}

const norm = (v) => (v || "").trim().toLowerCase();

function AdminPage() {
  const navigate = useNavigate();

  const [teacher, setTeacher] = useState("");
  const [batch, setBatch] = useState("");
  const [department, setDepartment] = useState("");

  // every student from every user, tagged with who entered them
  const allStudents = useMemo(() => {
    const users = readJSON("users", {});
    return Object.keys(users).flatMap(username =>
      readJSON(`students:${username}`, []).map(s => ({ ...s, teacher: username }))
    );
  }, []);

  const teacherOptions = uniqueOptions(allStudents.map(s => s.teacher));
  const batchOptions = uniqueOptions(allStudents.map(s => s.batch));
  const departmentOptions = uniqueOptions(allStudents.map(s => s.department));

  const filtered = allStudents.filter(s =>
    (!teacher || norm(s.teacher) === teacher) &&
    (!batch || norm(s.batch) === batch) &&
    (!department || norm(s.department) === department)
  );

  function clearFilters() {
    setTeacher("");
    setBatch("");
    setDepartment("");
  }

  function handleLogout() {
    localStorage.removeItem("adminLoggedIn");
    navigate("/adminlogin");
  }

  return (
    <div className="admin-page">
      <div className="admin-header">
        <h1>All Students</h1>
        <button onClick={handleLogout}>Logout</button>
      </div>

      <div className="filters">
        <select value={teacher} onChange={e => setTeacher(e.target.value)}>
          <option value="">All teachers</option>
          {teacherOptions.map(o => <option key={o.key} value={o.key}>{o.label}</option>)}
        </select>

        <select value={batch} onChange={e => setBatch(e.target.value)}>
          <option value="">All batches</option>
          {batchOptions.map(o => <option key={o.key} value={o.key}>{o.label}</option>)}
        </select>

        <select value={department} onChange={e => setDepartment(e.target.value)}>
          <option value="">All departments</option>
          {departmentOptions.map(o => <option key={o.key} value={o.key}>{o.label}</option>)}
        </select>

        <button onClick={clearFilters}>Clear filters</button>
      </div>

      <p>Showing {filtered.length} of {allStudents.length} students</p>

      <div className="cards">
        {filtered.map((s, i) => (
          <div key={i} className="card">
            <h3 className="card-title">Student Details</h3>
            <p><strong>Name:</strong> {s.name}</p>
            <p><strong>Batch:</strong> {s.batch}</p>
            <p><strong>Department:</strong> {s.department}</p>
            <p><strong>Entered by:</strong> {s.teacher}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AdminPage;