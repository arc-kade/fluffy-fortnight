// 

// console.log("start")
// const interval=setInterval(()=>{
//     console.log("middle")
// },2000)
// setTimeout(()=>{
//     clearInterval(interval)
// },5000)
// console.log("end")
// let counter =5
// const display=document.getElementById("counter")
// const interval=setInterval(()=>{
//     display.innerText=counter
//     counter--
//     if(counter<0){
//         clearInterval(interval)
//         display.innerText="Time's up"
//     }
// },1000)
// const myPromise=new Promise((resolve,reject)=>{
//     setTimeout(()=>{const success = false
//     if (success){
//         resolve("Task completed successfully")
//     }
//     else{
//         reject("Task failed")
//     }},2000)
// })
// myPromise
// .then(message=>{console.log(message)})
// .catch(error=>{console.error(error)})

fetch("https://jsonplaceholder.typicode.com/posts/")
    .then(response => response.json())
    // .then(data=>{console.log(data)})
    .then(data => {
        console.log(data)
        console.log(data[0].title)
        document.getElementById("title").innerText = data[0].title
    })
    .catch(error => { console.log("error", error) })
fetch("https://jsonplaceholder.typicode.com/posts")

    .then(response => response.json())

    .then(data => {

        const postsContainer = document.getElementById("posts");

        data.forEach(post => {

            const postElement = document.createElement("div");

            postElement.innerHTML = `
                <h2>${post.id}. ${post.title}</h2>
                <p>${post.body}</p>
                <hr>
            `;

            postsContainer.appendChild(postElement);

        });

    })

    .catch(error => {

        console.error("Error:", error);

    });