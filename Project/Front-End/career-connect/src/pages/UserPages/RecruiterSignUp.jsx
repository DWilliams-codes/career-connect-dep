import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../../utilities";
import { userContext } from "../../App";
import { useContext } from "react";
export default function RecruiterSignUpPage() {
    const navigate = useNavigate();
    const [userName,setUserName] = useState("");
    const [password, setpassword ] = useState("");
    const [company, setcompany] = useState("");
    const [name, setName ] = useState("");
    const { setUser } = useContext(userContext);
    const accounttype = "recruiter";
    //  function to sign up user
    const signUp = async(e) => {
        //  prevent page reload
        e.preventDefault();
        //  pings backend api to create user
        try{
        let response = await api.post("users/sign-up/",{
            email : userName,
            password : password,
            name : name,
            account_type : accounttype,
            company : company,
        });
        let user = response.data.user;
        let token = response.data.token;
        setUser(user);
        localStorage.setItem("token", token);
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        console.log("User created");
        navigate("/ProfilePage");
        // window.location.reload(true);
      }
      catch{
        window.alert("You Failed to Sign-Up");
      };
    };
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
          <input 
          type="name"
          value={name}
          onChange={(e) => setName(e.target.value)} 
          placeholder="Name"   />
          {/* input to set password */}
          <input type="password"
          value={password}
          onChange={(e) => setpassword(e.target.value)} 
          placeholder="Password"   />
          {/* input to select company */}
          <input value={company}
          onChange={(e)=> setcompany(e.target.value)}
          placeholder="Company" />
          <input type="submit" />
       </form>
  <button onClick={() => {navigate(`/sign-in`)}}>Sign-In</button>
    </>
    );
  };