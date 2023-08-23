import CompanyCard from "./CompanyCard";
import { useNavigate } from "react-router-dom";


export default function Companies() {
    const navigate = useNavigate();

    return (
    <>
        <h1>This is a a Companies Page </h1>
        <input type="text" placeholder="Company"   />
    
  <button disabled={''}onClick={() => {navigate(`/ProfilePage`)}}>Search</button>
   
        <CompanyCard/>
        <CompanyCard/>
        <CompanyCard/>
    </>
    );
  };