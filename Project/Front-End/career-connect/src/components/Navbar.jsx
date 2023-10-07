import { Link } from "react-router-dom";
import { useContext } from "react";
import { userContext } from "../App";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const { user, setUser } = useContext(userContext);
  const navigate = useNavigate();

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light nav-custom">
      <Link className="navbar-brand brand" to="">
        <h1>Career Connect</h1>
      </Link>
      <button
        className="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ml-auto">
          {user ? (
            <>
              <li className="nav-item nav-item-custom">
                <Link className="nav-link" to="/ProfilePage">
                  Profile
                </Link>
              </li>
              <li className="nav-item nav-item-custom">
                <button
                  className="btn btn-primary button-custom"
                  onClick={() => {
                    navigate("/UpdateJobPosting");
                  }}
                >
                  Update Job Posting
                </button>
              </li>
            </>
          ) : (
            <>
              <li className="nav-item nav-item-custom">
                <Link className="nav-link" to="/companies">
                  Find Companies
                </Link>
              </li>
              <li className="nav-item nav-item-custom">
                <Link className="nav-link" to="/sign-in">
                  Sign-In
                </Link>
              </li>
              <li className="nav-item nav-item-custom">
                <button
                  className="btn btn-primary button-custom"
                  onClick={() => {
                    navigate("/UpdateJobPosting");
                  }}
                >
                  Update Job Posting
                </button>
              </li>
            </>
          )}
        </ul>
      </div>
    </nav>
  );
  
}
