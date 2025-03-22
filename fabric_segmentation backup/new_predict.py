import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import os

# Constants
IMG_HEIGHT, IMG_WIDTH = 224, 224
CLASS_NAMES = ['hole', 'pilling', 'snags', 'stain', 'unknown']  # Update this based on your classes

def load_trained_model(model_path):
    """Load the trained model from the specified path."""
    model = load_model(model_path)
    print("Model loaded successfully.")
    return model

def prepare_image(image_path):
    """Preprocess the image to match model input requirements."""
    image = load_img(image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    image = img_to_array(image)  # Convert to numpy array
    image = image / 255.0  # Normalize to [0,1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def predict_image_class(model, image_path):
    """Predict the class of a given image using the loaded model."""
    # Prepare the image
    image = prepare_image(image_path)

    # Predict the class
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)
    confidence = np.max(predictions)

    # Get the class name
    class_name = CLASS_NAMES[predicted_class[0]]
    print(f"Predicted class: {class_name} with confidence: {confidence:.2f}")
    return class_name, confidence

# Load the model
model_path = "new_fabric_damage_detection_vgg16_10_epochs.h5"
model = load_trained_model(model_path)

# Predict an example image
# image_path = r"url_data\train\unknown\1st_floor_hallway.jpg"  # Replace with the path to the image you want to classify
# predict_image_class(model, image_path)
