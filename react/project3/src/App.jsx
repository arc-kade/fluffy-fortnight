import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import UserStatus from './components/userstatus'
// import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <UserStatus />
    </>
  )
}

export default App
