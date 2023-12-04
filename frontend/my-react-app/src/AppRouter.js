import React from "react";
import LandingPage from './LandingPage';
import CardPage from './CardPage';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

const AppRouter = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        <Route path = "/cards" element={<CardPage />} />
      </Routes>
    </Router>
  );
};

export default AppRouter;




