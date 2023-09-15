import { Link } from "react-router-dom";
import { useContext } from "react";
import { userContext } from "../App";
import { useNavigate } from "react-router-dom";
export default function Navbar() {
    const { user,setUser } = useContext(userContext);
    const navigate = useNavigate();
    return(
        <div>
        { user ?  <nav class="navbar fixed-top navbar-light bg-light">
        {/* home button functionality */}
        <Link to= ""><h1>Career Connect</h1></Link>
        {/* link to companies page */}
        {/* <Link to="/companies">Find Companies</Link> */}
         {/*  link to profilepage */}
         <Link to="/ProfilePage">Profile</Link>
         <button onClick={()=>{navigate("/UpdateJobPosting")}}>Update Job Posting</button>
      </nav> :  <nav class="navbar fixed-top navbar-light bg-light">
        <Link to= ""><h1>Career Connect</h1></Link>
  
        {/* <Link to="/companies">Find Companies</Link> */}
    
        <Link to="/sign-in">Sign-In</Link>
        <button onClick={()=>{navigate("/UpdateJobPosting")}}>Update Job Posting</button>
        </nav>}
    </div>
    )
};