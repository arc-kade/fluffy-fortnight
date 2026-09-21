import React from "react";
import Header from "../component/header.jsx";
import Footer from "../component/footer.jsx";
import Button from "../component/button.jsx";
import ClickExample from "../component/anything.jsx";
import InputExample from "../component/inputexample.jsx";
import GreetingButton from "../component/greetingbutton.jsx";
function Page(){
    function handleSubmit(){
        alert("Submit button clicked")
    }
    function handleCancel(){
        alert("Cancel button clicked")
    }
    function handleSave(){
        alert("Save button clicked")
    }
    return(
        <div>
            <Header />
            <main>
                <h2>Welcome to my website!</h2>
                <h3>This is my landing page</h3>
                <Button label = "Submit" type = "btn-primary" onClick = {handleSubmit}/>
                <Button label = "Cancel" type = "btn-danger" onClick = {handleCancel}/>
                <Button label = "Save" type = "btn-success" onClick = {handleSave}/>
                
            </main>
            <ClickExample />
            <InputExample />
            <GreetingButton />
            <Footer />
        </div>
    )
}
export default Page;