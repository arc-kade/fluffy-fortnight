export const increament = ()=>{
    return{
        type:"INCREAMENT"
    }
}
export const decreament = ()=>{
    return{
        type:"DECREAMENT"
    }
}
export const setMessage=(message)=>{
    return({
        type:"SET_MESSAGE",
        payload: "MESSAGE"  
    })
}
