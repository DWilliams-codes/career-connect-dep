import CompanyCard from "./CompanyCard";


export default function Companies() {

    return (
    <>
        <h1>This is a a Companies Page </h1>
        <input type="text" placeholder="Company"   />
    
  <button disabled={''}onClick={() => {navigate(`/ProfilePage`), window.location.reload(false)}}>Search</button>
   
        <CompanyCard/>
        <CompanyCard/>
        <CompanyCard/>
    </>
    );
  };