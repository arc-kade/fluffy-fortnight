import { useState, useEffect } from "react";


function State() {
    const [count, setCount] = useState(0)
    useEffect(() => {
        console.log('The count is:', count);

        return () =>{
            console.log("Cleaning up....")
        }
    }, [count]);
    return (
        <div>
            <h2>Count: {count}</h2>
            <button onClick={() => setCount(count + 1)}>Increment</button>
            <button onClick={() => setCount(count - 1)}>Decrement</button>
        </div>
    )
}

export default State