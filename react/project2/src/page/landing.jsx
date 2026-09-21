import Page from "./page"
function landing(){
    const isLoggedIn= true
    return (
        <div>
            {isLoggedIn && <Page />}
        </div>
    )
}
export default landing