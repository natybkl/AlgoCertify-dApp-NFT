// TraineeHomePage.js
import React, { useState } from 'react';
import './styles.css'; // Import the shared styles

const TraineeHomePage = ({ setRoute }) => {
  const [activeTab, setActiveTab] = useState('dashboard');

  const handleTabClick = (tab) => {
    setActiveTab(tab);
  };

  const handleBackButtonClick = () => {
    setRoute('home');
  };

  return (
    <div className="container trainee-home-page">
      <div className="flex-container">
        <div className="sidebar">
          <h3>Trainee Dashboard</h3>
          <ul>
            <li>
              <button onClick={() => handleTabClick('profile')}>Profile</button>
            </li>
            <li>
              <button onClick={() => handleTabClick('optin')}>Opt-in</button>
            </li>
            <li>
              <button onClick={() => handleTabClick('certificates')}>Issued Certificates</button>
            </li>
            <li>
              <button onClick={() => handleTabClick('dashboard')}>General Statistics Dashboard</button>
            </li>
          </ul>
        </div>
        <div className="content">
          {activeTab === 'dashboard' && <h2>General Statistics Dashboard Content</h2>}
          {activeTab === 'profile' && <h2>Profile Content</h2>}
          {activeTab === 'optin' && <h2>Opt-in Content</h2>}
          {activeTab === 'certificates' && <h2>Issued Certificates Content</h2>}
        </div>
      </div>
      <button onClick={handleBackButtonClick} className="btn back-btn">Back to Home</button>
    </div>
  );
};

export default TraineeHomePage;
