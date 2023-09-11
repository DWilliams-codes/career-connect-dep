import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import { userContext } from "../../App";
import { api } from "../../utilities";
import JobCard from "../../components/JobCard";
import { useEffect } from "react";

//  PlaceHolder page
export default function ProfilePage() {
  const navigate = useNavigate();
  const { user,setUser } = useContext(userContext);
  const logOut = async() => {
   
   let response = await api.post("users/log-out/",{user : user});
   if(response.status === 204){
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    delete api.defaults.headers.common["Authorization"];
    setUser(null);
    navigate("/sign-in");
   }
  
  };
  // const getuserfavorites = async(user) => {
  //   // let response = await api.get(`applicants/${user}/`)
  //   let response = await api.get(`applicants/1/`)
  //   // console.log(response)
  // };
  // useEffect(() => {
  //   getuserfavorites();
  // },[]);
    return (
      <>
      {/* Placeholder */}
      {user ? <div><h1>This is  {user}'s profile</h1>
        <button disabled={user==null}onClick={logOut}>LogOut</button>
        <ul>Job Posting's
        <button disabled={user==null}onClick={()=>{navigate("/CreateJobPosting")}}>Create Job Posting</button>
        <button disabled={user==null}onClick={()=>{navigate("/UpdateJobPosting")}}>Update Job Posting</button>
        </ul>
     </div> : 
        <div><h1>You are not Signed in</h1>
        <button onClick={logOut}>LogOut</button>
     </div> }
      </>
    );
  };