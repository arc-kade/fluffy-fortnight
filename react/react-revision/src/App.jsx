import { useState } from 'react'
import Greeting from './components/greeting'
import Button from './components/button'
import Header from './components/header'
import Footer from './components/footer'
import './App.css'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Header />
    <h3>Welcome to my react application</h3>
    <Greeting name = "Abilash" />

    <Button type = "btn-primary" Label="Submit" />
    <br></br>
    <Button type = "btn-danger" Label="Cancel" />
    <Footer />
    </>
  )
}

export default App
