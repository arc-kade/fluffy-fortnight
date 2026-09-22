import { useEffect,useState } from "react";
function dataFetcher(){
    const [data,setData] = useState(null)
    useEffect(()=>{
        fetch("https://jsonplaceholder.typicode.com/posts/")
        .then((response)=>response.json())
        .then((result)=>setData(result))
    },[])

    return(
        <div>
            {data?(data.map(datas=>(
                
                <div>
                    <p key={datas.id}>{datas.title}</p>
                    <p key={datas.id}>{datas.body}</p>
                </div>
            ))
            ):(
                <p>Loading...</p>
            )}
        </div>
    )
}
export default dataFetcher;