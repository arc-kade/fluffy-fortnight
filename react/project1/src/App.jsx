import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
// import './App.css'
import Multiple from './basic.jsx'
import FullName from './name.jsx'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <Multiple /> */}
      <FullName />
    </>
  )
}

export default App
