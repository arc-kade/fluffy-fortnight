function greetingButton(){
    function greet(name){
        alert(`Hello, ${name}`)

    }
    return(
        <button onClick={()=>greet("Name")}>Greet</button>
    )
}
export default greetingButton