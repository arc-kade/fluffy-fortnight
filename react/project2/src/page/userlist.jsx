import { useState } from "react";
import { useEffect } from "react";
import axios from "axios";
function userList(){
    const [users,setUsers]=useState([])
    useEffect(()=>{
        axios.get("https://jsonplaceholder.typcode.com/users")
            .then((result)=>{setUsers(result.data)})
            .catch((error)=>{
                console.error("Error fetching users :",error)
            })

    },[])
    return(
        <div>
            {users?(users.map((datas)=>(
                
                <div>
                    <p key={datas.id}>{datas.name}</p>
                    
                </div>
            ))
            ):(
                <p>Loading...</p>
            )}
        </div>
    )
}
export default userList;