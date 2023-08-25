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
  // const [loading, setLoading] = useState(true);
  const userAuthentication = async() => {
    // get token from local storage
    let token = localStorage.getItem("token");
    
    // checks for authorization on the back-end
    if(token){
      api.defaults.headers.common["Authorization"] = `Token ${token}`;
      let response = await api.get("users/");
      // sets user to user object
      // let copy = response.data;
      console.log(response.data);
      localStorage.setItem('user', response.data);
      setUser(response.data);
      console.log(user);
      // setLoading(false);
      console.log(token);
      if(user){
        navigate("");
      } else {
      setUser(null);
      // setLoading(false);
    };
  }
};
let local_copy = localStorage.getItem('user');
  useEffect(() => {
    userAuthentication();
    setUser(local_copy);
  },[]);
  return (
    <div>
      <div>
      {/* passes user down to entire app */}
      <userContext.Provider value ={{user, setUser}}>
     <Navbar />
     <Outlet />
     </userContext.Provider>
    </div>
   </div>
  );
};


