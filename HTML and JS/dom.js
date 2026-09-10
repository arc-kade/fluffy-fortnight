const heading = document.getElementById("title")
console.log(heading)
const paragraph = document.querySelector("#p1")
console.log(paragraph)
const paragraph2 = document.querySelector(".box ")
console.log(paragraph2)
const listItems = document.querySelectorAll("li")
// console.log(listItems)
listItems.forEach(item => {
    item.innerText=item.innerText.toUpperCase()
})
const heading1 = document.getElementById("title1")
heading1.innerText="Welcome to JavaScript"
const container=document.getElementById("content")
container.innerHTML="<srtong> this is a strong text</strong>"
const link=document.getElementById("myLink")
link.setAttribute("href","https://google.com")
const box = document.getElementById("mybox")
// box.classList.add("highlight")
box.classList.remove("box")


const button2=document.getElementById("addButton")
const addItem=document.getElementById("addItems")

// addItem.addEventListener("input",()=>{
//     console.log(event.target.value)
// })
button2.addEventListener("click",()=>{
    // const newItem=document.createElement("li")
    // newItem.innerText="new   Item"
    // document.querySelector("#itemList").appendChild(newItem)
    const addItems=document.createElement("li")
    addItems.innerText=addItem.value
    document.querySelector("#itemList").appendChild(addItems)
})
const button1=document.getElementById("myButton")
button1.addEventListener("click",()=>{
    console.log("button clicked")
})
const box2=document.getElementById("box2")
box2.addEventListener("mouseover",()=>{
    console.log("mouse over")
})
const input=document.getElementById("username")
input.addEventListener("input",(event)=>{
    console.log(event.target.value)
})

