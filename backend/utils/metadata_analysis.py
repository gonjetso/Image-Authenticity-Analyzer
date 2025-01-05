from exif import Image

def analyze_metadata(image_path):
    try:
        with open(image_path, 'rb') as img_file:
            img = Image(img_file)
            
            # Check if the EXIF data is present before accessing it
            metadata = {
                "datetime": getattr(img, "datetime_original", "Unknown"),
                "camera_model": getattr(img, "model", "Unknown"),
                "geo_location": getattr(img, "gps_latitude", "Unknown")
            }
        return metadata
    except KeyError as e:
        return {"error": f"EXIF data missing: {str(e)}"}
    except Exception as e:
        return {"error": f"An error occurred while reading EXIF: {str(e)}"}
