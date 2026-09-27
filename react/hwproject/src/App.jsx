import { useState } from 'react'
import { BrowserRouter,Routes,Route } from "react-router-dom"
import Index from './page/index.jsx'
import Login from './page/login.jsx'
import Register from './page/register.jsx'
import Landing from './page/landing.jsx'
import Home from './components/home.jsx'
import About from './components/about.jsx'
import Services from './components/services.jsx'
import Help from './components/help.jsx'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path = "/" element={<Index />}/>
          <Route path = "/Login" element={<Login />} />
          <Route path='/Register' element={<Register />} />
          <Route path='/Landing' element={<Landing />}>
            {/* <Route index element={<Landing />} /> */}
            <Route path='home' element={<Home />} />
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
