import React, { useState } from 'react';
import {Container, Row, Col, Button} from 'react-bootstrap';
import axios from 'axios';
import SentimentChart from './SentimentChart';
import HighlightedComments from './HighlightedComments';
import ImageComponent from './ImageComponent';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [videoUrl, setVideoUrl] = useState('');
  const [password, setPassword] = useState('')
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (event) => {
    setVideoUrl(event.target.value);
    setPassword(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8080/analyze_video', {
        video_url: videoUrl
      });
      setResponseData(response.data);
      console.log(responseData.comments_highlights)
    } catch (error) {
      setError(error.response.data.message);
    }
  };

  return (
    <Container>
      <Row>
        <h1>YouTube Comments Sentiment Analysis</h1> 
        <h2>What is This tool?</h2>
        <p>This is simple program fetching recent comment under YouTube video </p>
      </Row>
      <Row>
      <form onSubmit={handleSubmit}>
        <label>
          Enter YouTube Video URL:
          <input type="text" value={videoUrl} onChange={handleInputChange} />
          <input type="password" value={password} onChange={handleInputChange} />
        </label>
        <Button variant='primary' type='submit'> Submit</Button>
      </form>
      </Row>
      
      {responseData && (
      <Row>      
          <Col md={5}>
          <h2>GPT Response:</h2>
            <p>{JSON.stringify(responseData.gpt_response, null, 2)}</p>
          <h2>Highlighted Comments</h2>
          <HighlightedComments comments={responseData.comments_highlights} />
          
          </Col>
          <Col md={6}>
            <h2>VADER-based analysis:</h2>
            <SentimentChart sentiment={{negative: responseData.negative_points, positive: responseData.positive_points}}/>
            <img src="https://quickchart.io/wordcloud?text=To%20be%20or%20not%20to%20be%2C%20that%20is%20the%20question" alt="Chmura słów" />
          </Col>
        </Row>
      )}
      
      {error && <p>Error: {error}</p>}
    </Container>
  );
}

export default App;