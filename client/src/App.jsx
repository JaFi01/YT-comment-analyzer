import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [videoUrl, setVideoUrl] = useState('');
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (event) => {
    setVideoUrl(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8080/analyze_video', {
        video_url: videoUrl
      });
      setResponseData(response.data);
    } catch (error) {
      setError(error.response.data.message);
    }
  };

  return (
    <div>
      <h1>Sentiment Analysis</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter YouTube Video URL:
          <input type="text" value={videoUrl} onChange={handleInputChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
      {responseData && (
        <div>
          <h2>GPT Response:</h2>
          <pre>{JSON.stringify(responseData.gpt_response, null, 2)}</pre>
          <h2>VADER Response:</h2>
          <p>Negative points: {responseData.negative_points}</p>
          <p>Positive points: {responseData.positive_points}</p>
        </div>
      )}
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default App;