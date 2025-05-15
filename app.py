import streamlit as st
from model import train_model, predict
from data_preprocessing import preprocess_data
import pandas as pd

# Title of the web app
st.title("Housing Price Prediction")

# Sidebar for user input
st.sidebar.header("User Input")
age = st.sidebar.number_input("Age", min_value=0)
income = st.sidebar.number_input("Income", min_value=0)

# Prepare input data
input_data = pd.DataFrame({
    'Age': [age],
    'Income': [income]
})

# Button for prediction
if st.sidebar.button("Predict"):
    # Preprocess data
    processed_data = preprocess_data(input_data)
    # Make prediction
    prediction = predict(processed_data)
    st.write(f"**Predicted Housing Price:** ${prediction[0]:,.2f}")

# Adding a footer
st.sidebar.markdown("### Made with Streamlit")
