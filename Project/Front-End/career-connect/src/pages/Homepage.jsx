import { useNavigate } from "react-router-dom";
import JobCard from "../components/JobCard";
import { useState, useEffect } from "react";
import axios from "axios";


export default function HomePage() {
    const navigate = useNavigate();
    //  This is likely a behavior that can be specify within the inputs onChange field
    // set jobs varible
    const [jobs, setjobs] = useState("")
    // set location variable
    const [location, setlocation] = useState("")
    // set job title
    const [jobtitle, setjobtitle] = useState("")
    // update job value
    const jobtitlehandeler  = (event) => {
      setjobtitle(event.target.value)
    };
    // update location value
    const locationhandler = (event) => {
      setlocation(event.target.value)
    }
    // gets all jobs
    const getalljobs= async(jobtitle="") =>{
      try{
        // Pings Api
        const response = await axios.get(`http://localhost:8000/api/v1/job_postings/${jobtitle.replace(" ","")}`,{mode:'cors'})
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
    // create copy to map through
    const joblist = [...jobs]
    
    return (
        <><div className="searchbar">
        <h1>This is the HomePage</h1>
        <h1>Search For Jobs</h1>
        {/* input field to update job search */}
       <input type="text" placeholder="Job Title"  value={jobtitle} onChange={jobtitlehandeler}/>
       {/*  input field to update location */}
       <input type="text" placeholder="Location"  value={location} onChange={locationhandler}/>
      <button onClick={() => {getalljobs(jobtitle)}}>Search</button>
      </div>
      <div>
        <ul className="joblist">
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
    </div>
      </>
    );
  };
  
  