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
  <>
    <div className="card mb-3">
      <div className="card-body">
        <h2 className="card-title">{jobtitle}</h2>
        <h3 className="card-subtitle mb-2 text-muted">{company}</h3>
        <p className="card-text">{location}</p>
        <div className="d-flex justify-content-between">
          <button className="btn btn-primary" onClick={addToFavorites}>Add to favorites</button>
          <button className="btn btn-secondary" onClick={removeFromFavorites}>Remove from Favorites</button>
          <button className="btn btn-success" onClick={() => {navigate(`Application`)}}>Apply</button>
        </div>
        <div className="mt-3">
          <p className="card-text">{description}</p>
        </div>
      </div>
    </div>
  </>
);

  };