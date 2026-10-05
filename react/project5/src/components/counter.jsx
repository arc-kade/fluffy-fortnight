import { useSelector, useDispatch } from "react-redux";
import { increament, decreament, reset } from "../redux/counterslice";
function Counter(){
    const count = useSelector((state)=>{
        state.counter.value
    })
    const dispatch = useDispatch()
    return (
        <div>
            <h1>Counter</h1>
            <h2>{count}</h2>
            <button onClick={()=>dispatch(increament())}>Increament</button>
            <button onClick={()=>dispatch(decreament())}>Decreament</button>
            <button onClick={()=>dispatch(reset())}>Reset</button>
        </div>
    )
}
export default Counter;