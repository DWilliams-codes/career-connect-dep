import { useNavigate } from "react-router-dom";
import { useContext, useState } from "react";
import { userContext } from "../../App";
import { api } from "../../utilities";
import JobCard from "../../components/JobCard";
import { useEffect } from "react";

//  PlaceHolder page
export default function ProfilePage() {
  const navigate = useNavigate();
  const { user,setUser } = useContext(userContext);
  const [jobs, setjobs] = useState("");
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
  const getuserfavorites = async () => {
    try {
      const response = await api.get(`api/applicants/${user.id}/job_postings/`);
      setjobs(response.data);
    } catch (error) {
      console.log(error);
    }
  };
  
  useEffect(() => {
    getuserfavorites();
  },[]);
  const joblist = [...jobs]
    return (
      <>
      {/* Placeholder */}
      {user ? <div><h1>This is {user}'s profile</h1>
        <button disabled={user==null}onClick={logOut}>LogOut</button>
        <button disabled={user==null}onClick={()=>{navigate("/CreateJobPosting")}}>Create Job Posting</button>
        <button disabled={user==null}onClick={()=>{navigate("/UpdateJobPosting")}}>Update Job Posting</button>
        <ul className="joblist">Job Postings
          {/* map through all jobs creating a card for each */}
          {joblist.map((job, idx) => (
            <li key={idx}><JobCard
            jobtitle={job.title} 
            company={job.company}
            location={job.location}
            description={job.job_description}/>
            </li>
          ))}
        </ul>
     </div> : 
        <div><h1>You are not Signed in</h1>
        <button onClick={logOut}>LogOut</button>
     </div> }
      </>
    );
  };