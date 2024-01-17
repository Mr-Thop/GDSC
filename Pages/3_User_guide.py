import streamlit as st

# User Guide for Crop Prediction System
def crop_prediction_user_guide():
    st.subheader("Crop Prediction System User Guide")
    st.markdown("""
        1. Enter the values for Nitrogen, Phosphorous, Potassium, Temperature, Humidity, pH, and Rainfall.
        2. Click the "Submit" button to get crop recommendations.
        3. The top three recommended crops along with their probabilities will be displayed.
    """)

# User Guide for X-ray Analysis System
def xray_analysis_user_guide():
    st.subheader("X-ray Analysis System User Guide")
    st.markdown("""
        1. Upload an X-ray image using the file uploader.
        2. The model will predict the class of the X-ray image (e.g., Covid, Normal, Pneumonia, Tuberculosis).
        3. The predicted class along with the image will be displayed.
    """)

# Main Streamlit app
def main():
    st.title("User Guide")

    # Create two columns
    col1,_, col2 = st.columns([1,0.3,1])

    # Crop Prediction System Column
    with col1:
        crop_prediction_user_guide()

    # X-ray Analysis System Column
    with col2:
        xray_analysis_user_guide()

if __name__ == "__main__":
    main()
