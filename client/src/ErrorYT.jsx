import React from 'react';
import {Row, Alert} from 'react-bootstrap';
import image_err from './images/image_wrongYT.svg'

const ErrorYT = () => {

    return(<>
        <Row className="pt-4">   
            <Alert variant='warning' className='justify-content-center text-center'>
                <div>The provided YouTube link is invalid. Please enter a valid URL.</div>
                <div style={{ width: '200px', height: 'auto', margin: '0 auto'}}>
                    <img src={image_err} style={{ width: '100%', height: 'auto'}} alt="Error Image"/>
                </div>
            </Alert>         
        </Row>
    </>
    )
}

export default ErrorYT