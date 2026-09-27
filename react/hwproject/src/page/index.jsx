import { Link } from "react-router-dom";


function Index() {
    return (
        <div>
            <button >
                <Link to="/login" > Login </Link>
            </button>
            <button>
                <Link to="/register">Register</Link>
            </button>
        </div>
    )
}
export default Index;