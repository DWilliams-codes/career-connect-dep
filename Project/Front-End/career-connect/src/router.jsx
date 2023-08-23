import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import HomePage from "./components/Homepage.jsx";
import ProfilePage from "./components/ProfilePage.jsx";
import SignIn from "./components/SignInPage.jsx";
import Companies from "./components/CompaniesPage.jsx";
import ErrorPage from "./components/ErrorPage.jsx";
import SignUpPage from "./components/SignUp.jsx";

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
                element: <SignIn/>,
            },
            {
                // Companies Page
                path: "companies",
                element: <Companies/>,
            },
            {   
                //  Sign-Up Page
                path: "sign-up",
                element: <SignUpPage />,
            },
        ],
    },
]);
export default router;