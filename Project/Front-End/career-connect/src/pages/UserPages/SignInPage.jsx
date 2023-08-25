import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import { userContext } from "../../App";
import { api } from "../../utilities";
// signs in user
export default function SignInPage() {
    const navigate = useNavigate();
    const [userName,setUserName] = useState("");
    const [password, setpassword ] = useState("");
    const { setUser } = useContext(userContext);
    // gets response from backend api
    const signin = async(e) => {
      e.preventDefault()
      // sign-in on back-end
      let response = await api.post("users/sign-in/",{
        email : userName,
        password : password
      })
      .catch((err) => {
        alert("Invalid credintials")
        console.log(err)
        navigate("/sign-in")
      })
      //  sets user
      let user = response.data.user;
      let token = response.data.token;
      console.log(user)
      console.log(token)
      setUser(user);
      // refactor for deployment
      localStorage.setItem("token", token);
      api.defaults.headers.common["Authorization"] = `Token ${token}`;
      navigate("/ProfilePage");
      // window.location.reload(true);
    }

    return (
    <>
        <h1>This is a a Sign in page</h1>
        {/*  Form to call signin function */}
        <form >
          <h5>Sign-in</h5>
          {/* input to set username */}
          <input 
          type="email"
          value={userName}
          onChange={(e) => setUserName(e.target.value)} 
          placeholder="UserName"   />
          <p>Test Account: Recruiter@test.com</p>
          {/* input to set password */}
          <input type="password"
          value={password}
          onChange={(e) => setpassword(e.target.value)} 
          placeholder="Password"   />
          <input type="submit" onClick={signin} />
          <p>Test Password: 12345</p>
       </form>
       {/*  button to signup page */}
  <button onClick={() => {navigate(`/accountTypePage`)}}>Register</button>
    </>
    );
  };