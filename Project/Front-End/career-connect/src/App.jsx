import { useState } from 'react';
import { Outlet } from "react-router-dom";
import Navbar from './components/Navbar';
import HomePage from './components/Homepage';
import { createContext } from 'react';
export const userContext = createContext();


export default function App() {
  // Pass Data on the lowest level it is  specifically needed
  const [user, setUser] = useState(null)
  return (
    <div>
      <Navbar />
      <userContext.Provider value ={{user, setUser}}>
     <Outlet />
     </userContext.Provider>
    </div>
  );
};


