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

let counter =5
const display=document.getElementById("counter")
const interval=setInterval(()=>{
    display.innerText=counter
    counter--
    if(counter<0){
        clearInterval(interval)
        display.innerText="Time's up"
    }
},1000)