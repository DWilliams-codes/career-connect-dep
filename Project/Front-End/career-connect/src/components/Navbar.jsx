import { Link } from "react-router-dom";
import { useContext } from "react";
import { userContext } from "../App";

export default function Navbar() {
    const { user,setUser } = useContext(userContext);
 
    return(
        <div>
        { user ?  <nav>
        {/* home button functionality */}
        <Link to= ""><h1>Career Connect</h1></Link>
        {/* link to companies page */}
        <Link to="/companies">Find Companies</Link>
         {/*  link to profilepage */}
         <Link to="/ProfilePage">Profile</Link>
      </nav> :  <nav>
        <Link to= ""><h1>Career Connect</h1></Link>
  
        <Link to="/companies">Find Companies</Link>
    
        <Link to="/sign-in">Sign-In</Link>
        </nav>}
    </div>
    )
};