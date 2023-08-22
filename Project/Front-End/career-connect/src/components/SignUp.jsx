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
    const { setUser } = useContext(userContext)
    const signUp = async(e) => {
        e.preventDefault();
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
        <form onSubmit= {(e) =>signUp(e)}>
          <h5>Create Account</h5>
          <input 
          type="email"
          value={userName}
          onChange={(e) => setUserName(e.target.value)} 
          placeholder="UserName"   />
          <input type="password"
          value={password}
          onChange={(e) => setpassword(e.target.value)} 
          placeholder="Password"   />
          <input type="account type"
          placeholder="account type"
          value={accounttype}
          onChange={(e) => setAccountType(e.target.value)}/>
          <input type="submit" />
       </form>
  <button disabled={''}onClick={() => {navigate(`/sign-in`)}}>Sign-Up</button>
    </>
    );
  };