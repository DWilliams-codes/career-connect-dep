import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
export default function SignIn() {
    const navigate = useNavigate();
    return (
    <>
        <h1>This is a a Sign in page</h1>
       <input type="text" placeholder="UserName"   />
       <input type="text" placeholder="Password"   />
  <button disabled={''}onClick={() => {navigate(`/ProfilePage`), window.location.reload(false)}}>Login</button>
    </>
    );
  };