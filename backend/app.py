from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
from utils.clone_detection import detect_clones
from utils.color_analysis import detect_color_adjustments
from utils.metadata_analysis import analyze_metadata
# Optional
from utils.deepfake_detection import detect_deepfake

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)

    results = {
        "clones_detected": detect_clones(filepath),
        "color_adjustments": detect_color_adjustments(filepath),
        "metadata": analyze_metadata(filepath)
    }
    # Optional: Add deepfake detection
    # results["deepfake_detected"] = detect_deepfake(filepath)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
