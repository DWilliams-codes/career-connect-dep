import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import { userContext } from "../../App";
import { api } from "../../utilities";


//  PlaceHolder page
export default function ProfilePage() {
  const navigate = useNavigate();
  const { user,setUser } = useContext(userContext);
  const logOut = async() => {
   
   let response = await api.post("users/log-out/",{user : user});
   if(response.status === 204){
    localStorage.removeItem("token");
    delete api.defaults.headers.common["Authorization"];
    setUser(null);
    navigate("/sign-in");
   }
  
  };
 
  
    return (
      <>
      {/* Placeholder */}
      {user ? <div><h1>This is  {user}'s profile</h1>
        <button disabled={user==null}onClick={logOut}>LogOut</button>
        <ul>Job Posting's
        <button disabled={user==null}onClick={()=>{navigate("/CreateJobPosting")}}>Create Job Posting</button>
          <li>JOB CARD PLACEHOLDER</li>
        </ul>
     </div> : 
        <div><h1>You are not Signed in</h1>
        <button disabled={user==null}onClick={logOut}>LogOut</button>
     </div> }
      </>
    );
  };