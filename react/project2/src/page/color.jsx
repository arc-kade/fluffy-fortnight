import { useState } from "react";
function colorList(){
    const [color,setColor] = useState("")
    return(
        <div>
            <p>Color: {color}</p>
            <button onClick={()=>setColor("Red")}>Set Red</button>
            <button onClick={()=>setColor("Blue")}>Set Blue</button>
            <button onClick={()=>setColor("Green")}>Set Green</button>
        </div>
    )

}
export default colorList;