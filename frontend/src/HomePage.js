// HomePage.js
import React from 'react';
import './styles.css'; // Import the shared styles

const HomePage = ({ setRoute }) => {
  const handleTraineeButtonClick = () => {
    setRoute('trainee');
  };

  const handleStaffButtonClick = () => {
    const password = prompt('Enter password:');
    if (password === '1234') {
      setRoute('staff');
    }
  };

  return (
    <div className="container home-page">
      <h1>Welcome to the Home Page</h1>
      <button onClick={handleTraineeButtonClick} className="btn trainee-btn">Trainee</button>
      <button onClick={handleStaffButtonClick} className="btn staff-btn">Staff</button>
    </div>
  );
};

export default HomePage;





