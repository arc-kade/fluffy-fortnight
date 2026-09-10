function getName(){
    let name = prompt("Enter your name: ")
    alert("Hello "+ name)
}
function addNumbers(){
    let num1 = prompt("Enter your first number: ")
    let num2 = prompt("Enter your second number: ")
    let result = Number(num1)+Number(num2)
    // alert("Answer=" + result)
    document.getElementById("result").innerText="Answer ="+result
}

function add(){
    let num1= document.getElementById("num1").value
    let num2= document.getElementById("num2").value
    if(num1==="" || num2===""){
        alert("Please enter both numbers")
        return
    }
    num1= Number(num1)
    num2= Number(num2)
    let result1= num1 + num2
    document.getElementById("result1").innerText="Answer= " + result1
    }
function subtract(){
    let num1= document.getElementById("num1").value
    let num2= document.getElementById("num2").value
    if(num1==="" || num2===""){
        alert("Please enter both numbers")
        return
    }
    num1= Number(num1)
    num2= Number(num2)
    let result1= num1 - num2
    document.getElementById("result1").innerText="Answer= "+result1
}
function multiply(){
    let num1= document.getElementById("num1").value
    let num2= document.getElementById("num2").value
    if(num1==="" || num2===""){
        alert("Please enter both numbers")
        return
    }
    num1= Number(num1)
    num2= Number(num2)
    let result1= num1*num2
    document.getElementById("result1").innerText="Answer= "+result1
}
function divide(){
    let num1= document.getElementById("num1").value
    let num2= document.getElementById("num2").value
    if(num1==="" || num2===""){
        alert("Please enter both numbers")
        return
    }
    num1= Number(num1)
    num2= Number(num2)
    let result1= num1/num2
    document.getElementById("result1").innerText="Answer= "+result1
}
function equal(){
    let num1= document.getElementById("num1").value
    let num2= document.getElementById("num2").value
    if(num1==="" || num2===""){
        alert("Please enter both numbers")
        return
    }
    num1= Number(num1)
    num2= Number(num2)
    
}