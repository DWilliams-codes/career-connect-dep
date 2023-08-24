import axios from "axios";
//As a stretch goal, considering adding try/catch functionality to your Axios async calls. You might want to display something else than a generic error page (or even worse, a React-generated error page) when a call to your back-end fails. For example, you could wrap the signUp function on your signup component in a try/catch and have the catch case trigger the display of an error message to the user.
// set default api to ping backend
export const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1/",
});