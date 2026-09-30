import { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './studentfroms.css'

function StudentForm() {
  const [student, setStudent] = useState({
    name:"",
    batch:"",
    department:""
  }) ;

  function handleChange(e) {
    const {name,value} = e.target;
    setStudent(prev => ({...prev,[name]: value}));
  }
  function handleSubmit(e) {
    e.preventDefault();
    console.log("Submitted: ",student);
    setStudent({name: "", batch:"", department:""});
  }
  return (
    <div className='container'>
    <form onSubmit={handleSubmit} className='form'>
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
        <input type="text" name='batch' value={student.batch} onChange={handleChange} className="input" required/>
      </label>
      <label className='label'>Enter Student Department:
        <input type="text" name='department' value={student.department} onChange={handleChange} className="input" required />
      </label>
      <button type='submit'>Submit</button>
      <p>Name: {student.name}</p>
      <p>Batch: {student.batch}</p>
      <p>Department: {student.department}</p>
    </form>
    </div>
  )
}


export default StudentForm;