import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the model
model = joblib.load("Crops.pkl")

# Get user input
N = st.number_input("Enter the Nitrogen Value", value=0)
P = st.number_input("Enter the Phosphorous Value", value=0)
K = st.number_input("Enter the Potassium Value", value=0)
temp = st.number_input("Enter the Temperature Value", value=0.0)
humid = st.number_input("Enter the Humidity Value", value=0.0)
ph = st.number_input("Enter the Ph Value", value=0.0)
rain = st.number_input("Enter the Rainfall percentage", value=0.0)

if st.button("Submit"):
    data = {'N': [N], 'P': [P], 'K': [K], 'temperature': [temp], 'humidity': [humid], 'ph': [ph], 'rainfall': [rain]}
    new_data = pd.DataFrame(data)

# Get probability estimates for each class
    predict = model.predict(new_data)
    probabilities = model.predict_proba(new_data)

# Get the top 3 predicted crops and their probabilities
    top3_indices = probabilities.argsort(axis=1)[:, -3:][:, ::-1]
    top3_crops = model.classes_[top3_indices]
    top3_probabilities = probabilities[np.arange(len(probabilities)), top3_indices]

# Print the top 3 predicted crops and their probabilities
    for i, (crops, probs) in enumerate(zip(top3_crops, top3_probabilities)):
        st.markdown("\nTop 3 Crop Recommendations for the given inputs could be : \n")
        for crop, prob in zip(crops, probs):
            st.write(f'''{crop.capitalize()} \t - {prob:.2f}''')

# Display plots in Streamlit
    crop_labels = top3_crops[0]  # Take the top 3 predicted crops
    probabilities = top3_probabilities[0]  # Take the corresponding probabilities

    
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Hide deprecation warning
    st.subheader('Plots:')
    
    # Create a pie chart
    plt.figure(figsize=(12, 5))


# Stacked Bar Chart
    plt.subplot(1, 3, 2)
    plt.bar(crop_labels, probabilities, color=['green', 'orange', 'red'])
    plt.title('Stacked Bar Chart - Crop Recommendations')

# Heatmap
    heatmap_data = pd.DataFrame(data={'Crop Probabilities': probabilities}, index=crop_labels)
    plt.subplot(1, 3, 3)
    sns.heatmap(heatmap_data.T, cmap='viridis', annot=True, cbar=False)
    plt.title('Heatmap - Crop Probabilities')

# Show the plots
    plt.tight_layout()
    st.pyplot(plt)
