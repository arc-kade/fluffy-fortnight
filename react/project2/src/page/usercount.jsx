import { useState } from "react";

function counter(){
    const [count,setCount]= useState(0)
    return(
        <div>
            <p>Count : {count}</p>
            <button onClick={()=>setCount(count+1)}>Clicke me</button>
            <button onClick={()=>setCount(count-1)}>Delete Count</button>
        </div>
    )
}

export default counter;