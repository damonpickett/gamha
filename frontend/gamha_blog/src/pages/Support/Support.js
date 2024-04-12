import React, { useEffect } from 'react';
import './Support.css';

const Support = () => {

  useEffect(() => {
    const timer = setTimeout(() => {
      document.querySelector(".page-fade-in-transition").style.opacity = 1;
    }, 100);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="page-fade-in-transition">
      <div className="support-banner">
        <div className="support-overlay-text">
          <h1>Support</h1>
        </div>
      </div>

        <div className="support-content shared-wrapping shared-padding">
            <p>This is the support page</p>
        </div>
    </div>
  );
};

export default Support;