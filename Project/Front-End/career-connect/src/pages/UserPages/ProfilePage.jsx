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
  
    return (
      <>
      {/* Placeholder */}
        <h1>This is  {`${""}`}'s profile</h1>
        <button disabled={''}onClick={logOut}>LogOut</button>
      </>
    );
  };