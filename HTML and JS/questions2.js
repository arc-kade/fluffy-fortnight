let colors=["red","blue","green","yellow"]
colors.push("purple")
console.log(colors)
colors.pop()
console.log(colors)
let months=["February","March","April","May"]
months.unshift("January")
console.log(months)
months.shift()
console.log(months)
let numbers=[1,2,3,4,5,6]
let sepNumbers=numbers.slice(0,3)
console.log(sepNumbers)
let fruits = ["apple","banana","kiwi","pear","avocado"]
fruits.splice(2,1,"orange")
console.log(fruits)
for (i=0;i<numbers.length;i++){
    console.log(numbers[i])
}
let studentNames = ["Alice", "Bob", "Charlie", "David", "Emma"];
studentNames.forEach(students=>console.log(students))
fruits.forEach(fruit=>{
    if(fruit.length>5){
        console.log(fruit)
    }
})
numbers=[3,4,9,10,66,45,80]
numbers.forEach(bigNumbers=>{
    if(numbers>50){}
    }
)