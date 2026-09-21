import Page from '../page/page.jsx';
function userStatus(){
    const isLoggedIn = true
    function handleLogout(){
        // isLoggedIn = false
        alert("Logout button clicked")

    }
    function handleLogin(){
        // isLoggedIn = true
        alert("Login button clicked")
    }
    
    return(
        <div>
            {isLoggedIn?(
                <div>
                    <h1>Welcom user</h1>
                    <button onClick={handleLogout}>Logout</button>
                    <Page />
                </div>
            ):(
                <div> 
                    <h1>Please Login</h1>
                    <button onClick={handleLogin}>Login</button>
                </div>
            )}
        </div>
    )
}
export default userStatus;