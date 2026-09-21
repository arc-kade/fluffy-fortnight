import Page from "./page"
function userStatus(){
    const isLoggedIn = true
    function handleLogout(){
        alert("Logout button clicked")

    }
    
    return(
        <div>
            {isLoggedIn?(
                <div>
                    <button onClick={handleLogout}>Logout</button>
                    <Page />
                </div>
            ):(
                <div> <h1>Please Login</h1></div>
            )}
        </div>
    )
}
export default userStatus;