import { Link } from "react-router-dom"

export default function Navbar() {

    return(
    <nav>
        {/* home button functionality */}
        <Link to= ""><h1>Career Connect</h1></Link>
        {/* link to companies page */}
        <Link to="/companies">Find Companies</Link>
        {/*  link to signin page */}
        <Link to="/sign-in">Sign-In</Link>
        {/*  link to profilepage */}
        <Link to="/ProfilePage">Profile</Link>
    </nav>
    )
};