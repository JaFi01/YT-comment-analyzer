import React, { useState } from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import axios from "axios";
import SentimentChart from "./SentimentChart";
import HighlightedComments from "./HighlightedComments";
import ImageComponent from "./ImageComponent";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [videoUrl, setVideoUrl] = useState("");
  const [password, setPassword] = useState("");
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (event) => {
    setVideoUrl(event.target.value);
  };
  const handleInputChangePassword = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8080/analyze_video", {
        video_url: videoUrl,
      });
      setResponseData(response.data);
      console.log(responseData.comments_highlights);
    } catch (error) {
      setError(error.response.data.message);
    }
  };

  return (
    <Container className="mt-4">
      <Row className="mx-4">
        <h1>YouTube Comments Sentiment Analysis</h1>
        <h2>What is This tool?</h2>
        <p>
          This is simple program fetching recent comment under YouTube video{" "}
        </p>
        <p>
          It will provide AI based analysis of sentiment of comments, as well as
          walue most popular recent comments{" "}
        </p>
      </Row>
      <Row md={12}>
        <form onSubmit={handleSubmit} className="">
          <div className="form-group">
            <label htmlFor="videoUrl">Enter YouTube Video URL:</label>
            <br />
            <input
              type="text"
              className="form-control"
              id="videoUrl"
              value={videoUrl}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Enter Permission password:</label>
            <br />
            <input
              type="password"
              className="form-control"
              id="password"
              value={password}
              onChange={handleInputChangePassword}
            />
          </div>
          <div>
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </div>
        </form>
      </Row>

      {responseData && (
        <Row className="pt-4">
          <Col md={5} className="m-3">
            <h2>GPT Response:</h2>
            <p>{JSON.stringify(responseData.gpt_response, null, 2)}</p>
            <h2>Highlighted Comments</h2>
            <HighlightedComments comments={responseData.comments_highlights} />
          </Col>
          <Col md={6} className="m-3">
            <h2>VADER-based analysis:</h2>
            <SentimentChart
              sentiment={{
                negative: responseData.negative_points,
                positive: responseData.positive_points,
              }}
            />
            <img src={responseData.wordcloud_content} alt="Word Cloud" />
          </Col>
        </Row>
      )}

      {error && <p>Error: {error}</p>}
    </Container>
  );
}

export default App;
