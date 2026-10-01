import { useState, useEffect } from 'react'
import UserContext from './context/UserContext'
import Header from './component/header'
import ThemeContext from './context/themecontext'
import ToolBar from './component/toolbar'
import Counter from './component/counter'
import Message from './component/message'
// import './App.css'

function App() {
  // const [user,setUser] = useState("John")
  const [theme,setTheme] = useState("light")
  useEffect(()=>{
    document.body.className=theme;
  },[theme]);
  return (
    <>
      {/* <UserContext.Provider value={{user,setUser}}>
        <Header />
      </UserContext.Provider> */}
      <ThemeContext.Provider value={{theme,setTheme}}>
        <ToolBar />
      </ThemeContext.Provider>
      <Counter />
      <Message />
    </>
  )
}

export default App
