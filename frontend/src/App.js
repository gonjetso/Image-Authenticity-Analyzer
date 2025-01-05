import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [image, setImage] = useState(null);  // State for storing uploaded image
  const [loading, setLoading] = useState(false); // State to manage loading spinner
  const [result, setResult] = useState(null); // State for storing API result
  const [error, setError] = useState(null);  // State for handling errors

  // Handle file input
  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) {
      alert("Please upload an image.");
      return;
    }

    // Clear previous results and show loading
    setResult(null);
    setError(null);
    setLoading(true);

    // Create form data to send to the backend
    const formData = new FormData();
    formData.append('image', image);

    try {
      // Make POST request to backend
      const response = await axios.post('http://127.0.0.1:5000/analyze', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Set the result
      setResult(response.data);
    } catch (err) {
      // Handle errors
      setError('Error analyzing image.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Image Manipulation Detector</h1>
      
      {/* Upload Form */}
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleImageChange} accept="image/*" />
        <button type="submit" disabled={loading}>Analyze Image</button>
      </form>

      {/* Loading Spinner */}
      {loading && <p>Loading...</p>}

      {/* Display Results */}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      {result && (
        <div>
          <h2>Analysis Results:</h2>
          <ul>
            <li><strong>Clones Detected:</strong> {result.clones_detected ? "Yes" : "No"}</li>
            <li><strong>Color Adjustments:</strong> {result.color_adjustments ? "Yes" : "No"}</li>
            <li><strong>Metadata:</strong>
              <ul>
                <li><strong>Date/Time:</strong> {result.metadata.datetime}</li>
                <li><strong>Camera Model:</strong> {result.metadata.camera_model}</li>
                <li><strong>Geo Location:</strong> {result.metadata.geo_location}</li>
              </ul>
            </li>
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
