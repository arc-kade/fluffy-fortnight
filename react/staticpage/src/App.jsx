import { useState } from 'react'
import { BrowserRouter,Routes,Route } from "react-router-dom"
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import Home from './component/home.jsx'
import About from './component/about.jsx'
import Services from './component/service.jsx'
import Help from './component/help.jsx'
import MainPage from './page/mainpage.jsx'
// import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<MainPage />}>
            <Route index='/' element={<Home />} />
            <Route path='about' element ={<About />}/>
            <Route path='services' element ={<Services />}/>
            <Route path='help' element ={<Help />}/>
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
