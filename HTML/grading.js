function name(){
    let name = prompt("Enter your name: ")
}
function getResult(){
    let math = document.getElementById("math").value
    let science = document.getElementById("science").value
    let english = document.getElementById("english").value
    if(math===""||science===""||english===""){
        alert("Enter marks for all subjects")
        return
    }
    math= Number(math)
    science= Number(science)
    english= Number(english)
    let total = math + science + english
    let average = total/3
    document.getElementById("average").innerText="Average: " + average
    let grade = ""
    if (average > 89){
        grade = "S"
        
    }
    else if (average > 79){
        grade = "A"
        
    }
    else if (average > 69){
        grade = "B"
        
    }
    else if (average > 59){
        grade = "C"
        
    }
    else if (average > 49){
        grade = "D"
        
    }
    else if (average > 39){
        grade = "P"
        
    }
    else{
        grade = "F"
        
    }

    document.getElementById("grade").innerText="Grade: " + grade
}