import { useNavigate } from "react-router-dom";
import JobCard from "./JobCard";


export default function HomePage() {
    const navigate = useNavigate();

    return (
        <><div className="searchbar">
        <h1>This is the HomePage</h1>
        <h1>Search For Jobs</h1>
       <input type="text" placeholder="Job Title" />
       <input type="text" placeholder="Location"   />
      <button onClick={() => {window.location.reload(false)}}>Search</button>
      </div>
      <div>
        <JobCard />
        <JobCard />
        <JobCard />
        <JobCard />
    </div>
      </>
    );
  };
  
  