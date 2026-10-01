import { useSelector, useDispatch } from "react-redux"
import { setMessage } from "../redux/action"

function Message(){
    const message= useSelector((state)=>state.message)
    const dispatch= useDispatch()
    const updateMessage=()=>{
        dispatch(setMessage("Hello React"))
    }
    return(
        <div>
            <h2>Message: </h2>
            <p>{message}</p>
            <button onClick={updateMessage}>Send</button>
        </div>
    )
}
export default Message;