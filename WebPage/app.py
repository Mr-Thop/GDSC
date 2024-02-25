from flask import Flask, render_template, request
import numpy as np
from tensorflow import load_model
from tensorflow  import image
import cv2
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("xray.html")

@app.route("/", methods=["POST"])
def predict():
    model = load_model("X-Ray.h5")

    # Get the user-provided image from the HTML form
    uploaded_file = request.files["file"]
    if uploaded_file:
        # Load and preprocess the user-provided image
        user_img = image.load_img(uploaded_file, target_size=(64, 64))
        user_img_array = image.img_to_array(user_img)
        user_img_array = np.expand_dims(user_img_array, axis=0) / 255.0

        # Make predictions
        predictions = model.predict(user_img_array)

        # Interpret the predictions
        class_names = ['Covid', 'Normal', 'Pneumonia', 'Tuberculosis']
        predicted_class = class_names[np.argmax(predictions)]

        # Convert image to base64 for display in HTML
        _, img_encoded = cv2.imencode('.png', user_img_array[0])
        img_base64 = base64.b64encode(img_encoded).decode('utf-8')

        return render_template("xray.html", prediction=f'Predicted Class: {predicted_class}', img_base64=img_base64)

if __name__ == "__main__":
    app.run(debug=True)
