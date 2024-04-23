import React, { useState, useEffect } from "react";
import { Container, Row, Col, Button, Spinner, } from "react-bootstrap";
import axios from "axios";
import SentimentChart from "./components/SentimentChart";
import HighlightedComments from "./components/HighlightedComments";
import Description from "./components/Description";
import ErrorYT from "./components/ErrorYT";
import AIResponse from "./components/AIResponse";
import "bootstrap/dist/css/bootstrap.min.css";
import.meta.env.VITE_SERVER_URL_ANALYSIS

function App() {
  const [videoUrl, setVideoUrl] = useState("");
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // This useEffect is designed to wake up the serverless container on Cloud Run when the
  // user requests data for the first time. It aims to reduce cold start time by about 4-5
  // seconds on the initial request. The axios GET request is triggered only when responseData
  // is null, preventing unnecessary calls to the server on subsequent requests.
   useEffect(() => {
    if(responseData == null){
     axios.get(import.meta.env.VITE_SERVER_URL)}
  }, [])

  const handleInputChange = (event) => {
    setVideoUrl(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      setLoading(true);
      const response = await axios.post(import.meta.env.VITE_SERVER_URL_ANALYSIS, {
        video_url: videoUrl,
      });
      setResponseData(response.data);
      setLoading(false);
    } catch (error) {
      setError(error.response.data.message);
      setLoading(false);
    }
  };

  return (
    <Container className="mt-4">
      <Row className="mx-4">
        <h1 className="mb-3">YouTube Comments Sentiment Analysis</h1>
        <Description />
      </Row>
      <Row md={12} className="mx-4 mt-4">
        <form onSubmit={handleSubmit} className="">
          <div className="form-group">
            <label htmlFor="videoUrl"><b>Enter YouTube Video URL:</b></label>
            <br />
            <input
              type="text"
              className="form-control"
              id="videoUrl"
              value={videoUrl}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <Button className="mt-2 p-2" variant="primary" type="submit" disabled={loading}>
              {loading ? (
                <>
                  <Spinner
                    as="span"
                    animation="border"
                    size="sm"
                    role="status"
                    aria-hidden="true"
                  />
                  Loading...
                </>
              ) : (
                ""
              )}
              Check sentiment
            </Button>
          </div>
        </form>
      </Row>
      {error && <p>Error: {error}</p>}
      {responseData && responseData.error_status_YT_url &&(
        <ErrorYT></ErrorYT>
      )}
      


      {responseData && !responseData.error_status_YT_url && (
      <Row className="pt-4">        
          <Col md={5} className="m-3">
            <h2>AI Response:</h2>
            <AIResponse gptResponse={responseData.gpt_response} />
            <h2 className="pt-4">Highlighted Comments</h2>
            <HighlightedComments comments={responseData.comments_highlights} />
          </Col>
          <Col md={6} className="m-3">
            <h2>VADER-based analysis chart:</h2>
            <SentimentChart
              sentiment={{
                negative: responseData.negative_points,
                positive: responseData.positive_points,
              }}
            />
            <h2 className="pt-4">Wordcloud</h2>
            <img className='pt-1' src={responseData.wordcloud_content} alt="Word Cloud" />
          </Col>
        </Row>
      )}  

     
    </Container>
  );
}

export default App;
