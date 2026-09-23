import { useState } from "react";
function colorList(){
    const [color,setColor] = useState("")
    const [colorName,setColorName] = useState("")
    return(
        <div>
            <p style={{color:color}}>Color: {colorName}</p>
            <button onClick={()=>{setColorName("Red");setColor("Green");}}>Set Red</button>
            <button onClick={()=>{setColorName("Green");setColor("Blue");}}>Set Green</button>
            <button onClick={()=>{setColorName("Blue");setColor("Red");}}>Set Blue</button>
            
        </div>
    )

}
export default colorList;