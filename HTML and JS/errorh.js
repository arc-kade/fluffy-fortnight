try{
    const number = "Hello"
    number.toUpperCase()
    console.log(number.toUpperCase())
}
catch(error){
    console.error("Error occured",error.message)
}
finally{
    console.log("Excecution finished")
}
let price = 100
let quantity = 5
let total = price+quantity
console.log(total)

function checkString(input){
    if(!input){
        throw new Error("String cannot be empty")
    }
    return input
}
try{
    console.log(checkString("A"))
}
catch(error){
    console.error(error.message)
}

//HTML page with a 10 second cd. After CD, show all data from an API