import { userContext } from "../App";
import { useContext, useState } from "react";
import { api } from "../utilities";


export default function CreateJobPostingsPage(){
    const { user, setUser } = useContext(userContext);
    const [ title, setTitle ] = useState("");
    const [ job_type, setJobType ] = useState("");
    const [ job_description, setJobDescription ] = useState("");
    const [ degree_type, setDegreeType ] = useState("");
    const [ skills, setSkills ] = useState("");
    const [ salary, setsalary ] = useState("");
    const [ location, setlocation ] = useState("");

    
    const createJobPosting = async (e) => {
            e.preventDefault();
            let response = await api.post("job_postings/",{
                title : title,
                job_type: job_type,
                job_descrition : job_description,
                degree_type : degree_type,
                skills : skills,
                salary : salary,
                location : location
            })
            .catch((e)=>{
            console.log(e)
             alert("Didnt Create Job")
            })
        }

    return(<div>
        <form onSubmit={(e)=>createJobPosting(e)}>
            <h5>Create Job Posting</h5>
            <input 
          type="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)} 
          placeholder="Job Title"   />
           <input 
          type="text"
          value={job_type}
          onChange={(e) => setJobType(e.target.value)} 
          placeholder="Job Type"   />
          <input 
          type="description"
          value={job_description}
          onChange={(e) => setJobDescription(e.target.value)} 
          placeholder="Job Description"   />
          <input 
          type="text"
          value={degree_type}
          onChange={(e) => setDegreeType(e.target.value)} 
          placeholder="Required Degree"   />
          <input 
          type="text"
          value={skills}
          onChange={(e) => setSkills(e.target.value)} 
          placeholder="Required Skill"   />
          <input 
          type="Integer"
          value={salary}
          onChange={(e) => setsalary(e.target.value)} 
          placeholder="Salary"   />
          <input 
          type="text"
          value={location}
          onChange={(e) => setlocation(e.target.value)} 
          placeholder="City, State"   />
          <input
          type="submit"
          />
        </form>
    </div>
    );
};