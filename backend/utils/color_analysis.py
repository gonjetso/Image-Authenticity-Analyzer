import cv2
import numpy as np

def detect_color_adjustments(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        return {"error": "Failed to load image"}
    
    channels = cv2.split(image)
    histograms = [cv2.calcHist([channel], [0], None, [256], [0, 256]) for channel in channels]
    
    # Convert numpy.float32 values to native float
    histogram_variances = [float(np.var(hist)) for hist in histograms]
    
    color_adjustments_detected = all(var < 500 for var in histogram_variances)
    
    return {
        "color_adjustments_detected": color_adjustments_detected,
        "histogram_variances": histogram_variances  # Now it's a list of native floats
    }
