import React from 'react';
import { Card } from 'react-bootstrap';

const CommentCard = ({ comment }) => {
  return (
    <Card className='mt-1'>
      <Card.Body>
        <Card.Text>{comment[2]}</Card.Text>
        <Card.Subtitle className="mb-2 text-muted">{comment[1]}</Card.Subtitle>
        <Card.Subtitle className="mb-2 text-muted">Likes: {comment[0]}</Card.Subtitle>
      </Card.Body>
    </Card>
  );
};

const HighlightedComments = ({ comments }) => {
  return (
    <div>
      {comments.map((comment, index) => (
        <CommentCard key={index} comment={comment} />
      ))}
    </div>
  );
};

export default HighlightedComments;