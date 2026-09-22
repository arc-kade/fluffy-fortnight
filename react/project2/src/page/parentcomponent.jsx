import { useState } from "react";
import ChildInput from './childinput'
import ChildDisplay from './childdisplay'
function parentComponent(){
    const [value,setValue]=useState("")
    return(
        <div>
            <ChildInput value ={value} setValue = {setValue}/>
            <ChildDisplay value = {value}/>
        </div>
    )
}
export default parentComponent;