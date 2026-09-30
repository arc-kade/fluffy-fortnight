import { useContext } from "react";
import ThemeContext from "../context/themecontext";
import "./theme.css"

function ToolBar(){
    const {theme,setTheme} = useContext(ThemeContext);
    const toggleTheme = ()=>{setTheme(theme==="light"?"dark":"light")};
    return(
        <div className={`toolbar ${theme}`}>
            <h2>Current Theme:{theme}</h2>
            <button onClick={toggleTheme} aria-label="toggle light and dark theme">Change theme</button>
        </div>
    )
}
export default ToolBar;
