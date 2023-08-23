import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../utilities";
import { userContext } from "../App";
import { useContext } from "react";
export default function SignUpPage() {
    const navigate = useNavigate();
    const [userName,setUserName] = useState("");
    const [password, setpassword ] = useState("");
    const [accounttype, setAccountType] = useState("");
    const { setUser } = useContext(userContext);
    //  function to sign up user
    const signUp = async(e) => {
        //  prevent page reload
        e.preventDefault();
        //  pings backend api to create user
        let response = await api.post("users/sign-up/",{
            email : userName,
            password : password,
            account_type : accounttype
        })
        let user = response.data.user
        let token = response.data.token
        setUser(user)
        localStorage.setItem("token", token)
        console.log("User created")
        navigate("")
    }
    return (
    <>
        <h1>This is a a Sign-Up page</h1>
        {/* for to run sign-in request */}
        <form onSubmit= {(e) =>signUp(e)}>
          <h5>Create Account</h5>
          {/* input to set userName */}
          <input 
          type="email"
          value={userName}
          onChange={(e) => setUserName(e.target.value)} 
          placeholder="UserName"   />
          {/* input to set password */}
          <input type="password"
          value={password}
          onChange={(e) => setpassword(e.target.value)} 
          placeholder="Password"   />
         {/* input to set account type */}
          <input type="account type"
          placeholder="account type"
          value={accounttype}
          onChange={(e) => setAccountType(e.target.value)}/>
          <input type="submit" />
       </form>
  <button onClick={() => {navigate(`/sign-in`)}}>Sign-Up</button>
    </>
    );
  };