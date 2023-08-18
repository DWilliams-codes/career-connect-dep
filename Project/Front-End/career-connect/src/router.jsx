import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import HomePage from "./components/Homepage.jsx";
import ProfilePage from "./components/ProfilePage.jsx";
import JobListingsPage from "./components/Job-ListingsPage.jsx";
import SignIn from "./components/SignInPage.jsx";
import Companies from "./components/CompaniesPage.jsx";
import JobSearchPage from "./components/Job-Search.jsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
            {
                path: "profile",
                element: <ProfilePage />,
            },
            {
                path: "job-search",
                element: <JobSearchPage />,
            },
            {
                path: "sign-in",
                element: <SignIn/>,
            },
            {
                path: "companies",
                element: <Companies/>,
            },
            {
                path: "job-listings",
                element: <JobListingsPage/>,
            },
        ],
    },
]);
export default router;