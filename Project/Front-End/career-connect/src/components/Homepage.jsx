



export default function HomePage() {

    return (
    <>
       <h1>Search For Jobs</h1>
       <input type="text" placeholder="Job Title"   />
       <input type="text" placeholder="Location"   />
  <button disabled={''}onClick={() => {navigate(`/Job-listings/`), window.location.reload(false)}}>Search</button>
    </>
    );
  };
  
  