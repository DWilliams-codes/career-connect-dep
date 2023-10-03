import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const JobApplication = ({ jobTitle }) => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [coverLetter, setCoverLetter] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission, e.g., send data to the server
    console.log("Form submitted:", { name, email, coverLetter, jobTitle });
    alert("Application Succesful");
    navigate("/");
  };
  return (
    <div>
      <h2>Apply for {jobTitle}</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="coverLetter">Cover Letter:</label>
          <textarea
            id="coverLetter"
            value={coverLetter}
            onChange={(e) => setCoverLetter(e.target.value)}
            required
          />
          <label htmlFor="resume">Resume:</label>
          <input
            type="file"
            id="resume"
            accept=".pdf, .doc, .docx" // Specify accepted file formats
            onChange={(e) => setResume(e.target.files[0])}
            required
          />
        </div>
        <button type="submit">Submit Application</button>
      </form>
    </div>
  );
};

export default JobApplication;
