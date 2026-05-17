
import streamlit as st
import joblib

# Load trained model
model = joblib.load("student_prediction_model.pkl")

# Title
st.title("MCQ Quiz Analytics System")

# User Inputs
time = st.slider("Time Taken", 10, 60)
attempts = st.slider("Attempts", 1, 5)

# Prediction Button
if st.button("Predict"):
    
    # Prediction
    result = model.predict([[time, attempts]])
    
    # Output
    st.success(f"Result: {result[0]}")