import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../../utilities";
import { userContext } from "../../App";
import { useContext } from "react";
export default function ApplicantSignUpPage() {
    const navigate = useNavigate();
    const [userName,setUserName] = useState("");
    const [password, setpassword ] = useState("");
    const [name, setName ] = useState("");
    const [ education, setEducation ] = useState("");
    const [ school , setschool ] = useState("");
    const [ field, setfield ] = useState("");
    const { setUser } = useContext(userContext);
    const accounttype = "applicant";
    //  function to sign up user
    const signUp = async(e) => {
        //  prevent page reload
        e.preventDefault();
        //  pings backend api to create user
        try{
        let response = await api.post("users/sign-up/",{
            email : userName,
            password : password,
            account_type : accounttype,
            name : name,
            education : education,
            field : field,
            school : school,
            skills : "NONE",
        });
        let user = response.data.user;
        let token = response.data.token;
        setUser(user);
        localStorage.setItem("token", token);
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        console.log("User created");
        navigate("/ProfilePage");
      }
      catch{
        window.location.reload(true);
      };
    };
    return (
    <>
        <h1>Applicant Registration</h1>
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
          <input 
          type="text"
          value={education}
          onChange={(e) => setEducation(e.target.value)} 
          placeholder="Highest Level of Education"   />
          <input 
          type="text"
          value={field}
          onChange={(e) => setfield(e.target.value)} 
          placeholder="Degree Field"   />
          <input 
          type="text"
          value={school}
          onChange={(e) => setschool(e.target.value)} 
          placeholder="Educational Institution"   />
          <input type="submit"/>
       </form>
  <button onClick={() => {navigate(`/sign-in`)}}>Sign-In</button>
    </>
    );
  };