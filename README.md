# EcoHarmony Innovators

## Introduction

This prototype showcases the integration of two artificial intelligence systems: one for predicting crop recommendations based on environmental factors, and the other for analyzing X-ray images to classify various health conditions.

### Crop Prediction System
The Crop Prediction System utilizes machine learning models to recommend suitable crops based on input parameters such as Nitrogen, Phosphorous, Potassium, Temperature, Humidity, pH, and Rainfall. Users can input these values and receive predictions for the top three recommended crops along with their probabilities.

### X-ray Analysis System
The X-ray Analysis System employs a deep learning model to analyze X-ray images and predict the class of the image, such as Covid, Normal, Pneumonia, or Tuberculosis. Users can upload X-ray images to the system, and the predicted class, along with the image, will be displayed.


## Technologies Used

- Python
- Jupyter Notebooks
- TensorFlow
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- HTML
- CSS

## Project Overview

The project consists of the following components:

- **Model Training:** Various machine learning models are trained for medical diagnosis and crop recommendation using relevant datasets.

- **Symptom Prediction:** Given a set of symptoms, the system predicts possible diseases using trained models.

- **Crop Recommendation:** Based on environmental factors like N-P-K levels, temperature, humidity, etc., the system recommends suitable crops.

- **Healthcare Image Classification:** A convolutional neural network (CNN) is trained to classify healthcare images into categories like normal, pneumonia, tuberculosis, and COVID-19.


## Installation

1. Clone the repository:

   ```bash
   git clone [(https://github.com/Mr-Thop/GDSC)]
   ```

2. Install the required libraries:

   ```bash
   pip install streamlit
   pip install tensorflow
   pip install scikit-learn
   pip install matplotlib
   pip install numpy
   pip install seaborn
   pip install joblib
   ```

## Usage

- Open the Terminal and Run
  ```bash
  streamlit run Home_Page.py
  ```
-Then you can Navigate into the Respective Pages and Try them 

- Make Sure that you include all the .pkl and .h5 files within the directory of homepage.py
- Wait Till the Model Loads as it may Take time to load itself (around 3 mins for each)

