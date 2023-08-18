import { useNavigate } from "react-router-dom";



export default function ProfilePage() {
  const navigate = useNavigate();
    return (
      <>
        <h1>This is a Profile</h1>
        <button disabled={''}onClick={() => {navigate(`/sign-in`), window.location.reload(false)}}>LogOut</button>
      </>
    );
  };