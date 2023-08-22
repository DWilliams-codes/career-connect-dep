import { useNavigate } from "react-router-dom";
import JobCard from "./JobCard";
import { useState, useEffect } from "react";
import axios from "axios";


export default function HomePage() {
    const navigate = useNavigate();
    //  This is likely a behavior that can be specify within the inputs onChange field
    const [jobs, setjobs] = useState("")
    const [location, setlocation] = useState("")
    const [inputvalue, setinputvalue] = useState("")
    const onchangehandler  = (event) => {
      setinputvalue(event.target.value)
    };
    const locationhandler = (event) => {
      setlocation(event.target.value)
    }
    const getalljobs= async(inputvalue="") =>{
      try{
        const response = await axios.get(`http://localhost:8000/api/v1/job_postings/${inputvalue.replace(" ","")}`,{mode:'cors'})
      .then((response) => {
        setjobs(response.data)
      });
      }
      catch (e){
        console.log(e)
      }
    };
    useEffect(() => {
      getalljobs();
    },[]);
    const joblist = [...jobs]
    
    return (
        <><div className="searchbar">
        <h1>This is the HomePage</h1>
        <h1>Search For Jobs</h1>
       <input type="text" placeholder="Job Title"  value={inputvalue} onChange={onchangehandler}/>
       <input type="text" placeholder="Location"  value={location} onChange={locationhandler}/>
      <button onClick={() => {getalljobs(inputvalue)}}>Search</button>
      </div>
      <div>
        <ul className="joblist">
          {joblist.map((job, idx) => (
            <li key={idx}><JobCard
            jobtitle={job.title} 
            company={job.company}
            location={job.location}
            description={job.description}/>
            </li>
          ))}
        </ul>
    </div>
      </>
    );
  };
  
  