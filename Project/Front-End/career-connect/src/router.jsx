import { createBrowserRouter } from "react-router-dom";
import { App } from "./App.jsx";
import HomePage from "./pages/Homepage.jsx";
import ProfilePage from "./pages/UserPages/ProfilePage.jsx";
import Companies from "./pages/CompaniesPage.jsx";
import ErrorPage from "./pages/ErrorPage.jsx";
import SignInPage from "./pages/UserPages/SignInPage.jsx";
import RecruiterSignUpPage from "./pages/UserPages/RecruiterSignUp.jsx";
import ApplicantSignUpPage from "./pages/UserPages/ApplicantSignUp.jsx";
import SelectAccountTypePage from "./pages/UserPages/AccountTypePage.jsx";
import CreateJobPostingsPage from "./pages/CreateJobPostingPage.jsx";
import UpdateJobPostingsPage from "./pages/UpdateJobsPage.jsx";
import JobApplication from "./pages/ApplicationsPage.jsx";
const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        //  Error Page 
        errorElement: <ErrorPage/>,
        children: [
            {   
                // HomePage
                index: true,
                element: <HomePage />,
            },
            {   
                // ProfilePage
                path: "ProfilePage",
                element: <ProfilePage />,
            },
            {   
                // Sign-In Page
                path: "sign-in",
                element: <SignInPage/>,
            },
            {
                // Companies Page
                path: "companies",
                element: <Companies/>,
            },
            {   
                //  Sign-Up Page
                path: "recruiter/sign-up",
                element: <RecruiterSignUpPage />,
            },
            {
                path: "accountTypePage",
                element:<SelectAccountTypePage />,
            },
            {
                path:"applicant/sign-up",
                element: <ApplicantSignUpPage />,
            },
            {
                path:"CreateJobPosting",
                element: <CreateJobPostingsPage />,
            },
            {
                path:"UpdateJobPosting",
                element: <UpdateJobPostingsPage />,
            },
            {
                path:"Application",
                element: <JobApplication />,
            },
        ],
    },
]);
export default router;