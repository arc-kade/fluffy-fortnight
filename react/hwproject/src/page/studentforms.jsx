import { useState, useEffect } from 'react';
import "../page/studentforms.css"

function StudentForm() {
  const currentUser = localStorage.getItem("currentUser");
  const storageKey = `students:${currentUser}`;
  const [student, setStudent] = useState({
    name: "",
    batch: "",
    department: "",
    id: ""
  });

  const [submitted, setSubmitted] = useState(()=>{
    try{
      const saved = localStorage.getItem(storageKey);
      return saved ? JSON.parse(saved): [];
    } catch {
      return[];
    }
  });

  // useEffect(() => {
  //   localStorage.setItem(storageKey, JSON.stringify(submitted));
  // }, [storageKey, submitted]);
  const [error, setError] = useState("");

  function handleChange(e) {
    const { name, value } = e.target;
    setStudent(prev => ({ ...prev, [name]: value }));
  }
  function handleSubmit(e) {
    e.preventDefault();
    console.log("Submitted: ", student);

    const exists = submitted.some(s => s.id === student.id);
    if (exists) {
      setError("ID value alredy entered");
      return;
    }
    setError("");
    const updated = [...submitted, student];
    setSubmitted(updated);
    localStorage.setItem(storageKey, JSON.stringify(updated))
    // setSubmitted(prev => [...prev, student]);
    setStudent({ name: "", batch: "", department: "", id: "" });
  }
  return (
    <div className='container'>
      <form onSubmit={handleSubmit} className='form'>
        <label className='label'>Enter Student ID:
          <input
            type="text"
            name="id"
            value={student.id}
            onChange={handleChange}
            className='input'
            required />
        </label>
        <label className='label'>Enter Student name:
          <input
            type="text"
            name='name'
            value={student.name}
            onChange={handleChange}
            className='input'
            required
          />
        </label>
        <label className='label'>Enter Student Batch:
          <input type="text" name='batch' value={student.batch} onChange={handleChange} className="input" required />
        </label>
        <label className='label'>Enter Student Department:
          <input type="text" name='department' value={student.department} onChange={handleChange} className="input" required />
        </label>
        <button type='submit'>Submit</button>
        {error && <p className='error'>{error}</p>}
      </form>
      <div className='cards'>
        {submitted.map((s, index) => (
          <div key={index} className='card'>
            <h3 className='card-title'>Student Details</h3>
            <p><strong>ID:</strong> {s.id}</p>
            <p><strong>Name:</strong> {s.name}</p>
            <p><strong>Batch:</strong> {s.batch}</p>
            <p><strong>Department: </strong>{s.department}</p>
          </div>
        ))}
      </div>
    </div>
  );
}


export default StudentForm;