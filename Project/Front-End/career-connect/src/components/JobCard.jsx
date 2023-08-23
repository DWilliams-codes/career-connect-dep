


export default function JobCard({jobtitle, company, location, description}) {
// This may need some conditional rendering to ensure the card does not display unless the props being rendered on the screen are actually provided.
    return (
      <><div className="job-card">
        <h2>{jobtitle}</h2> 
        <h3>{company}</h3>
        <p>{location}</p>
        {/* placeholder will add to list of favorites on user profile */}
        <button onClick={() => {navigate(``)}}>Add to favorites</button>
        {/* will link to application */}
        <button onClick={() => {navigate(``)}}>Apply</button>
        <div>
          <p>{description}</p>
        </div>
        </div>
        </>
    );
  };