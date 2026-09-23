import { useState } from "react";
import { useMemo } from "react";
function Calculation({number}){
    const calculate=(num)=>{
        console.log("Number is calculating")
        return num*2
    }
    const result = useMemo(()=>{
        return calculate(number)

    },[number])
    return(
        <div>
            <p>Result: {result}</p>
        </div>
    )
}
function calculationDemo(){
    const [number,setNumber] = useState(0)
    return(
        <div>
            <input type="number" value={number} onChange={(e)=>setNumber(Number(e.target.value))} />
            <Calculation number ={number} />
        </div>
    )
}
export default calculationDemo