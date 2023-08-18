import { Link } from "react-router-dom"

export default function Navbar() {

    return(
    <nav>
        <h1>Career Connect</h1>
        {/* Add home button functionality to Career Connect H1 later */}
        <Link to= "">Home</Link>
        <Link to="/companies">Find Companies</Link>
        <Link to="/sign-in">Sign-In/Sign-Up</Link>
    </nav>
    )
};