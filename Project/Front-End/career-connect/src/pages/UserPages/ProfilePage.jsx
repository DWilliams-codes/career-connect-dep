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
    setUser(null);
    navigate("/sign-in");
   };
  
  };
  console.log(user)
  
    return (
      <>
      {/* Placeholder */}
      {user ? <div><h1>This is  {user}'s profile</h1>
        <button disabled={user==null}onClick={logOut}>LogOut</button>
        <ul>Favorites
          <li>JOB CARD PLACEHOLDER</li>
        </ul>
     </div> : 
        <div><h1>You are not Signed in</h1>
        <button disabled={user==null}onClick={logOut}>LogOut</button>
     </div> }
      </>
    );
  };