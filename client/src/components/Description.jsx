import Accordion from "react-bootstrap/Accordion";

const Description = () => {
  return (
    <Accordion defaultActiveKey="0">
      <Accordion.Item eventKey="0">
        <Accordion.Header>Quick description of the App</Accordion.Header>
        <Accordion.Body>
          This is a simple app, made to analyze the sentiment of recent comments under a given YouTube video.
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="1">
        <Accordion.Header>How to use?</Accordion.Header>
        <Accordion.Body>
          Paste the url adress of a chosen YouTube video. Then wait a few seconds and read the results. It is suggested to use a movie or game trailer in order to test this app - this will provide the best results.  
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="2">
        <Accordion.Header>Why waiting for results might be long?</Accordion.Header>
        <Accordion.Body>
          It is due to the fact that processing thousands of comments, deciding what is sentiment of them, requesting external APIs takes time.
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="3">
        <Accordion.Header>How to read the results?</Accordion.Header>
        <Accordion.Body>
          AI Response is a response of the most popular comments analyzed by OpenAI API. It is a pretty accurate description and summary of what people think.
          VADER-based analysis chart displays positive and negative emotions expressed in the comments. The number of likes is also taken into consideration.
          WordCloud is a cluster of the words that occur the most.
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
  );
};
export default Description;
