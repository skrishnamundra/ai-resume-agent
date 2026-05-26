import React from 'react';
import UploadResume from './components/UploadResume';
import CandidateList from './components/CandidateList';

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>AI Resume Screening Agent</h1>

      <UploadResume />

      <hr />

      <CandidateList />
    </div>
  );
}

export default App;
