import cv2

def detect_clones(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        return {"error": "Failed to load image"}
    
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    
    return {
        "clones_detected": len(keypoints) > 100,
        "keypoints": len(keypoints)  # Return the number of keypoints for debugging
    }
