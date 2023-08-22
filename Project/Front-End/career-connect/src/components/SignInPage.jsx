import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
export default function SignIn() {
    const navigate = useNavigate();
    const [userName,setUserName] = useState("");
    const [password, setpassword ] = useState("");

    return (
    <>
        <h1>This is a a Sign in page</h1>
        <form onSubmit={console.log("form is working")}>
          <h5>Sign-in</h5>
          <input 
          type="email"
          value={userName}
          onChange={(e) => setUserName(e.target.value)} 
          placeholder="UserName"   />
          <input type="password"
          value={password}
          onChange={(e) => setpassword(e.target.value)} 
          placeholder="Password"   />
          <input type="submit" />
       </form>
  <button disabled={''}onClick={() => {navigate(`/sign-up`)}}>Sign-Up</button>
    </>
    );
  };