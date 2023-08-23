import axios from "axios";
// set default api to ping backend
export const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1/",
});