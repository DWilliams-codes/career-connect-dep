import { useNavigate } from "react-router-dom";

export default function SelectAccountTypePage() {
    const navigate = useNavigate();
    return(
        <>
            <div>
                <h1>Account Type Page</h1>
                <button onClick={() => {navigate("/recruiter/sign-up")}}>Recruiter</button>
                <button onClick={() => {navigate("/applicant/sign-up")}}>Applicant</button>
            </div>
        </>
    );
};
