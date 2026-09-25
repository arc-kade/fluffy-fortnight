import { useState } from 'react'
import { BrowserRouter,Routes,Route } from "react-router-dom"
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import Simple from './simple.jsx'
import Usercard from './userCard.jsx'
import Page from './page/page.jsx'
import Landing from './page/landing.jsx'
import Landing2 from './page/landing2.jsx'
import ParentComponent from './page/parentcomponent.jsx'
import DataFetcher from './page/data.jsx'
import Home from './component/home.jsx'
import About from './component/about.jsx'
import Services from './component/service.jsx'
import Help from './component/help.jsx'
import MainPage from './page/mainpage.jsx'
import Login from './page/login.jsx'
import Index from './page/index.jsx'
// import './App.css'

function App() {
  
  return (
    <>
      {/* <Simple name = "Abilash" age = '23' />
      <Simple name = "Perman" age = '12'/> */}
      {/* <Usercard name = "Abilash" age = "23" phone = "1234567890" dep = "CS"/> */}
      {/* <Page /> */}
      {/* <ParentComponent /> */}
      {/* <Landing2 /> */}
      {/* <DataFetcher /> */}
      <BrowserRouter>
        <Routes>
          <Route path = "/" element={<Index />}/>
          <Route path = "/Login" element={<Login />} />
          <Route path='/mainpage' element={<MainPage />}>
            <Route index element={<Home />} />
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
