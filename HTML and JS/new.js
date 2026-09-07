// let name="Abilash"
// console.log(name)
// // const country = "Spain"
// // country = "Peru"
// console.log(typeof name)
// let age=23.6
// console.log(typeof age)
// let student = true
// console.log(typeof student)
// let phnumber = null
// console.log(typeof phnumber)
// let address
// address="Kochi"
// console.log(address)
// let a =5 
// let b = 10
// let sum = a+b
// let difference = a-b
// console.log(sum)
// console.log(5==="5")
// let age = 25
// let id=true
// console.log(age >=18 && id===true)
// console.log(age >=18 || id===false)
// console.log(`my age is ${age}`)
// install node.js and code runner
// age = 20
// if (age >=20){
//     console.log("Eligible")
// }
// else{
//     console.log("Ineligible")
// }
// let number = 0
// if (number>0){
//     console.log("Number is positive")
// }
// else if(number < 0){
//     console.log("Number is negative")
// }
// else{
//     console.log("number is 0")
// }
// let day = 3
// switch(day){
//     case 1:
//         console.log("Monday")
//         break
//     case 2:
//         console.log("Tuesday")
//         break
//     case 3:
//         console.log("Wednesday")
//         break
//     default:
//         console.log("Error")
//         break
// }
// for(let i=0;i<=5;i++){
//     console.log(i)
// }
// let i=0
// while(i<5){
//     console.log(i)
//     i++
// }
// let i=0
// do{
//     console.log(i)
//     i++
// }while(i<0)
// for(let i=0;i<=5;i++){
//     if(i===3){
//         continue
//     }
//     console.log(i)
// }
// function add(a,b){
//     console.log(a+b)
// }
// add(20,30)
// const add=(a,b)=> a+b
// console.log(add(3,4))
// const greet= name=>`Hello ${name}`
// console.log(greet("Abilash"))
// let name=prompt("Enter your name: ")
// console.log(name)
let fruits = ["apple","banana","orange","strawberry"]
// console.log(fruits[0])
// fruits[1]="kiwi"
// console.log(fruits)
fruits.push("peach")
console.log(fruits)
fruits.pop()
console.log(fruits)
fruits.unshift("pear")
console.log(fruits)
fruits.shift()
console.log(fruits)
let slicedFruits=fruits.slice(0,2)
console.log(slicedFruits)
fruits.splice(1,1,"lemon")
console.log(fruits)
for(let i=0;i<fruits.length;i++){
console.log(fruits[i])
}
fruits.forEach(fruit=>console.log(fruit))
fruits.forEach(fruit=>{
    if(fruit.length>5){
console.log(fruit)
    }
})
let person={
    name:"Abilash",
    age: 23,
    email: "abilash.t.venu@gmail.com",
}
console.log(person)
console.log(person.name)
console.log(person["age"])
person.age=24
console.log(person)
person.phonenumber=9035348007

console.log(person)
let employee={
    name:"Bob",
    address:{
        city:"Chalakkudy",
        district:"Thrissur"
        
    }
}
console.log(employee)
let employees = [
    {name:"John",age:28},
    {name:"Rahul",age:27},
    {name:"Ali",age:29},
]
let youngest=employees.reduce((a,b)=>(a.age<b.age?a:b))
console.log(youngest.name)
let numbers=[1,2,3]
let squared = numbers.map(num=>num*num)
console.log(squared)
let evennumbers=numbers.filter(a=>a%2===0)
console.log(evennumbers)
let sum=numbers.reduce((total,num)=>total+num,0)
console.log(sum)
person={
    name:"Abilash",
    age: 23,
    email: "abilash.t.venu@gmail.com",
}
console.log(Object.keys(person))
console.log(Object.values(person))
console.log(Object.entries(person))