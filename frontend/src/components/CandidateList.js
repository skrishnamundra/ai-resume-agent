import React, { useState } from 'react';
import API from '../api';

function CandidateList() {
  const [jobDescription, setJobDescription] = useState('');
  const [results, setResults] = useState([]);

  const handleRank = async () => {
    const response = await API.post('/resume/rank', {
      job_description: jobDescription
    });

    setResults(response.data);
  };

  return (
    <div>
      <h2>Rank Candidates</h2>

      <textarea
        rows="10"
        cols="80"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <br />

      <button onClick={handleRank}>Rank</button>

      {results.map((candidate, index) => (
        <div key={index}>
          <h3>{candidate.candidate}</h3>
          <pre>{candidate.summary}</pre>
        </div>
      ))}
    </div>
  );
}

export default CandidateList;
