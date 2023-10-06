import { useNavigate } from "react-router-dom";

export default function JobCard({jobtitle, company, location, description}) {
  const navigate = useNavigate();
  const addToFavorites = async () => {
    try {
      await api.post(`/api/applicants/${user.id}/job_postings/${job.id}/favorite/`);
      alert("Job added to favorites!");
    } catch (error) {
      console.log(error);
    }
  };
  const removeFromFavorites = async () => {
    try {
      await api.delete(`/api/applicants/${user.id}/job_postings/${job.id}/favorite/`);
      alert("Job removed from favorites!");
    } catch (error) {
      console.log(error);
    }
  };
// This may need some conditional rendering to ensure the card does not display unless the props being rendered on the screen are actually provided.
    return (
      <><div className="job-card">
        <h2>{jobtitle}</h2> 
        <h3>{company}</h3>
        <p>{location}</p>
        {/* placeholder will add to list of favorites on user profile */}
        <button onClick={() => {addToFavorites}}>Add to favorites</button>
        {/* placeholder will remove from list of favorites on user profile */}
        <button onClick={removeFromFavorites}>Remove from Favorites</button>
        {/* will link to application */}
        <button onClick={() => {navigate(`Application`)}}>Apply</button>
        <div>
          <p>{description}</p>
        </div>
        </div>
        </>
    );
  };