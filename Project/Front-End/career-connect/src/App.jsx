import { useState } from 'react';
import { Outlet } from "react-router-dom";
import Navbar from './components/Navbar';
import HomePage from './components/Homepage';
export default function App() {
  // Pass Data on the lowest level it is  specifically needed
  return (
    <div>
      <Navbar />
     <Outlet />
    </div>
  );
};


