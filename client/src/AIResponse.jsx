import React from 'react';
import { Card } from 'react-bootstrap';

const AIResponse = ({ gptResponse }) => {
    return (
            <Card>
                <Card.Body>
                    <p>{JSON.stringify(gptResponse, null, 2)}</p>
                </Card.Body>
            </Card>
    );
}

export default AIResponse;