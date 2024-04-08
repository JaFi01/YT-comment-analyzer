import React from 'react';
import { Card } from 'react-bootstrap';

const AIResponse = ({ gptResponse }) => {
    return (
        <>
            <h2>AI Response:</h2>
            <Card>
                <Card.Body>
                    <p>{JSON.stringify(gptResponse, null, 2)}</p>
                </Card.Body>
            </Card>
            <h2 className="pt-4">Highlighted Comments</h2>
        </>
    );
}

export default AIResponse;