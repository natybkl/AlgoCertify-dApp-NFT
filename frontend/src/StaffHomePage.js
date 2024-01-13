// StaffHomePage.js
import React from 'react';
import './styles.css'; // Import the shared styles

const StaffHomePage = ({ setRoute }) => {
  const handleTabClick = (tab) => {
    // Handle tab click for Staff home page if needed
  };

  const handleBackButtonClick = () => {
    setRoute('home');
  };

  return (
    <div className="container staff-home-page">
      <div className="flex-container">
        <div className="sidebar">
          <h3>Staff Dashboard</h3>
          <ul>
            <li>
              <button onClick={() => handleTabClick('optinRequests')}>Opt-in Requests</button>
            </li>
            <li>
              <button onClick={() => handleTabClick('traineeList')}>List of Trainees</button>
            </li>
            <li>
              <button onClick={() => handleTabClick('issueCertificate')}>Issue Certificate</button>
            </li>
          </ul>
        </div>
        <div className="content">
          {/* Render content for Staff home page as needed */}
        </div>
      </div>
      <button onClick={handleBackButtonClick} className="btn back-btn">Back to Home</button>
    </div>
  );
};

export default StaffHomePage;
