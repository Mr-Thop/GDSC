import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the pre-trained model
model = load_model("X-Ray.h5")

# Streamlit UI
st.title("X-Ray Image Classification")

# File uploader for user to provide an image
uploaded_file = st.file_uploader("Choose an X-ray image...", type="jpg")

if st.button("Submit"):
     if uploaded_file is not None:

    # Load and preprocess the user-provided image
         user_img = image.load_img(uploaded_file, target_size=(64, 64))
         user_img_array = image.img_to_array(user_img)
         user_img_array = np.expand_dims(user_img_array, axis=0) / 255.0

    # Make predictions
         predictions = model.predict(user_img_array)

    # Interpret the predictions
         class_names = ['Covid', 'Normal', 'Pneumonia', 'Tuberculosis']
         predicted_class = class_names[np.argmax(predictions)]

    # Display the result
         st.image(user_img, caption=f'Predicted Class: {predicted_class}', use_column_width=True)
