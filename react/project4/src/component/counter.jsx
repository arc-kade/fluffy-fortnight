import { useSelector, useDispatch } from "react-redux"
import { increament, decreament } from "../redux/action"
function counter() {
    const count = useSelector((state) => state.count)
    const dispatch = useDispatch()
    return (
        <div>
            <h2>
                Counter: 
            </h2>
            <h3>{count}</h3>
            <button onClick={()=>dispatch(increament())}>Increament </button>
            <button onClick={()=>dispatch(decreament())}>Decreament </button>
        </div>
    )


}
export default counter;