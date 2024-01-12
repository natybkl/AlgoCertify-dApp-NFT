// App.js
import React, { useState } from 'react';
import HomePage from './HomePage';
import TraineeHomePage from './TraineeHomePage';
import StaffHomePage from './StaffHomePage';

const App = () => {
  const [route, setRoute] = useState('home');

  let pageContent;
  if (route === 'home') {
    pageContent = <HomePage setRoute={setRoute} />;
  } else if (route === 'trainee') {
    pageContent = <TraineeHomePage setRoute={setRoute} />;
  } else if (route === 'staff') {
    pageContent = <StaffHomePage setRoute={setRoute} />;
  }

  return <div>{pageContent}</div>;
};

export default App;
