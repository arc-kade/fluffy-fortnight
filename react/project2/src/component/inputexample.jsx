function inputExample(){
    function handleChange(event){
        console.log(event.target.value)
        
    }
    return(
        <input type="text" placeholder="enter an input" onChange={handleChange} />
    )
}
export default inputExample