import {useSelector} from "react-redux";
function Message(){
    const count = useSelector((state)=>state.counter.value)
    return(
        <div>
            <h3>Current count = {count}</h3>
            {count === 0 && <p>Counter is 0</p>}
            { count > 0 && <p>Counter is positive</p>}
            {count <0 && <p>Counter is negative</p>}
        </div>
    )
}
export default Message;