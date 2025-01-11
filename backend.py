from flask import Flask, request, jsonify, render_template
import os
import cv2
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Directory to store uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Home page
@app.route('/')
def home():
    return render_template('index.html')  # Create an index.html for the upload interface

# Route: Upload and process image
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the image using DeepStream + TAO Toolkit
        results = process_image(filepath)
        
        # Return results
        return jsonify(results)

    return jsonify({"error": "Invalid file type"})

# Function: Process image using DeepStream and TAO Toolkit
def process_image(filepath):
    """
    Simulate the image processing using DeepStream and TAO Toolkit.
    Replace this placeholder with actual DeepStream inference and TAO model loading.
    """
    # Example: Load image and preprocess
    image = cv2.imread(filepath)
    image_resized = cv2.resize(image, (224, 224))  # Resize as per model requirements

    # Placeholder: Simulated inference results
    # Replace this with actual inference code
    # Example: Use TensorRT engine from TAO for inference
    results = {
        "message": "Image processed successfully",
        "similar_products": [
            {"product_id": 101, "name": "Gadget A", "similarity_score": 0.95},
            {"product_id": 202, "name": "Gadget B", "similarity_score": 0.92},
        ]
    }
    return results

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
