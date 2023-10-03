import { Link } from "react-router-dom";
import { useContext } from "react";
import { userContext } from "../App";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const { user, setUser } = useContext(userContext);
  const navigate = useNavigate();

  return (
    <nav className="navbar navbar-expand-lg navbar-light nav-custom">
      <Link className="brand" to="">
        <h1>Career Connect</h1>
      </Link>
      <div className="collapse navbar-collapse">
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
