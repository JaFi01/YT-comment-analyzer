import React from 'react';

const ImageComponent = ({ base64ImageData }) => {
  return (
    <div>
      <img src={`data:image/png;base64,${base64ImageData}`} alt="Base64 Image" />
    </div>
  );
};

export default ImageComponent;