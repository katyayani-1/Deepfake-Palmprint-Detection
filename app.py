from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
import os

app = Flask(__name__)

# Load the trained ResNet model
model = tf.keras.models.load_model("updated_resnet_model_best.h5")

IMAGE_SIZE = 224  # Ensure this matches the model's input size
unique_labels = ['Deepfake', 'Original']  # Swapped labels (Deepfake = 0, Original = 1)

THRESHOLD = 0.3  # Adjusted threshold for better deepfake detection

# Define image preprocessing function
def preprocess_image(img):
    img = img.convert('RGB')  # Convert to RGB if it's RGBA
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))  # Resize image
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize if model was trained with normalization
    return img_array

# Define prediction function with corrected label mapping
def predict(img):
    processed_img = preprocess_image(img)
    prediction = model.predict(processed_img)[0][0]  # Extract probability value

    # Since Deepfake = 0 and Original = 1, adjust classification logic
    class_idx = 0 if prediction < THRESHOLD else 1  # Deepfake if below threshold, else Original
    confidence = 1 - prediction if class_idx == 0 else prediction  # Confidence adjusted to match labels

    return class_idx, confidence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', message='No file uploaded')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', message='No file selected')
        try:
            img = Image.open(file)
            class_idx, confidence = predict(img)
            prediction_label = unique_labels[class_idx]
            confidence_percentage = f"{confidence:.2f}"
            background_color = 'green' if prediction_label == 'Original' else 'red'

            # Save uploaded image to static/uploads
            upload_folder = os.path.join(app.root_path, 'static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            img_filename = f"upload_{np.random.randint(1000000)}.png"
            img_path = os.path.join(upload_folder, img_filename)
            img.save(img_path)
            img_url = f"/static/uploads/{img_filename}"

            return render_template('result.html', prediction=prediction_label, confidence=confidence_percentage, background_color=background_color, img_url=img_url)
        except Exception as e:
            return render_template('upload.html', message=str(e))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
