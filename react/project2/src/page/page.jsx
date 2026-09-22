import React from "react";
import Header from "../component/header.jsx";
import Footer from "../component/footer.jsx";
import Button from "../component/button.jsx";
import ClickExample from "../component/anything.jsx";
import InputExample from "../component/inputexample.jsx";
import GreetingButton from "../component/greetingbutton.jsx";
import Item from "../component/item.jsx";
import ProductList from "./productlist.jsx";
import Counter from "./usercount.jsx";
import ColorList from "./color.jsx";
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
            <Item />
            <ProductList />
            <ClickExample />
            <InputExample />
            <GreetingButton />
            <Counter />
            <ColorList />
            <Footer />
        </div>
    )
}
export default Page;