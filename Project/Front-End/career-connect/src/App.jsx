import { useEffect, useState } from 'react';
import { Outlet } from "react-router-dom";
import Navbar from './components/Navbar';
import HomePage from './pages/Homepage';
import { createContext } from 'react';
import { api } from './utilities';
import { useNavigate } from 'react-router-dom';
export const userContext = createContext();


export default function App() {
  // Pass Data on the lowest level it is  specifically needed
  const [user, setUser] = useState(null);
  const navigate = useNavigate();
  const userAuthentication = async() => {
    // get tokent from local storage
    let token = localStorage.getItem("token");
    // checks for authorization on the back-end
    console.log(token)
    if(token){
      api.defaults.headers.common["Authorization"] = `Token ${token}`;
      let response = await api.get("users/");
      // sets user to user object
      console.log(response);
      setUser(response.data);
      console.log(user);
      navigate("");
    }
    else{
      setUser(null);
    }
  };

  useEffect(() => {
    userAuthentication();
    console.log(user);
  },[]);
  return (
    <div>
      <Navbar />
      {/* passes user down to entire app */}
      <userContext.Provider value ={{user, setUser}}>
     <Outlet />
     </userContext.Provider>
    </div>
  );
};


