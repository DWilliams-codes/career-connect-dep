


export default function JobCard({jobtitle, company, location, description}) {

    return (
      <><div className="job-card">
        <h2>{jobtitle}</h2> 
        <h3>{company}</h3>
        <p>{location}</p>
        <div>
          <p>{description}</p>
        </div>
        </div>
        </>
    );
  };