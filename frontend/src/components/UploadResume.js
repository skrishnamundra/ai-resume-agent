import React, { useState } from 'react';
import API from '../api';

function UploadResume() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    await API.post('/resume/upload', formData);

    alert('Resume Uploaded');
  };

  return (
    <div>
      <h2>Upload Resume</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default UploadResume;
