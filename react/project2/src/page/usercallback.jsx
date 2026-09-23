import { useState } from "react";
import { useCallback } from "react";
function UserCall({increament}){
    console.log("rendered")
    return(
        <button onClick={increament}>increament</button>
    )
}
function UserCallDemo(){
    const [count,setCount]=useState(0)
    const increament = useCallback(()=>{
        setCount((previous)=>previous+1)
    },[])
    return(
        <div>
            <p>Count: {count}</p>
            <UserCall increament={increament} />
        </div>
    )
}
export default UserCallDemo;