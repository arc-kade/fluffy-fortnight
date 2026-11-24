import { useState } from 'react'
import Greeting from './components/greeting'
import Button from './components/button'
import Header from './components/header'
import Footer from './components/footer'
import State from './components/stateuse'
import './App.css'
function App() {
  return (
    <>
    <Header />
    <h3>Welcome to my react application</h3>
    <Greeting name = "Jester" />
    <State />
    <Button type = "btn-primary" Label="Submit" />
    <br></br>
    <Button type = "btn-danger" Label="Cancel" />
    <Footer />
    </>
  )
}

export default App
