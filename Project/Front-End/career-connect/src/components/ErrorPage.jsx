import { useNavigate } from "react-router-dom";

export default function ErrorPage() {
    const navigate = useNavigate();
    return (
      <><div>
        <h1>ERROR PLEASE RETURN HOME</h1> 
        <button name="home-button" onClick={() => navigate(``)}>Home</button>
        </div>
        </>
    );
  };