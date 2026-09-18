import React from "react";
function userCard(props){
    return (
        <div>
    <h1>User details: </h1>
    <h3>Name: {props.name} <br />
        Age: {props.age} <br />
        Phone number: {props.phone} <br />
        Division: {props.dep}</h3> 
    
    </div>
)}
export default userCard;