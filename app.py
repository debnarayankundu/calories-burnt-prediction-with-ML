import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the pre-trained model
model = pickle.load(open('calories4.pkl', 'rb'))

# Function to predict calorie expenditure
def pred(features):
    prediction = model.predict(features).reshape(-1, 1)
    return prediction[0]

# Main title and image
st.title('Calorie Expenditure Prediction App')
# Set background image


# Gender selection
st.subheader('Gender')
Gender = st.radio("Select Gender", ['Male', 'Female'])
Gender_male = 1 if Gender == 'Male' else 0

# Input fields
st.subheader('enter the following parameters')
col1, col2, col3 = st.columns(3)
with col1:
    Age = st.number_input("Age", min_value=0, max_value=120, step=1)
with col2:
    Height = st.number_input("Height (cm)", min_value=0.0, max_value=300.0, step=0.1)
with col3:
    Weight = st.number_input("Weight (kg)", min_value=0.0, max_value=500.0, step=0.1)

Duration = st.number_input("Duration (mins)", min_value=0, max_value=600, step=1)
Heart_Rate = st.number_input("Heart Rate (bpm)", min_value=0, max_value=250, step=1)
Body_Temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, step=0.1)


if st.button("Predict"):
    features = [Age, Height, Weight, Duration, Heart_Rate, Body_Temp, Gender_male]
    result = pred([features])
    st.success("You have burnt {} calories".format(result[0]))
