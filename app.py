import streamlit as st
import joblib
import numpy as np


model = joblib.load('housing_model.pkl')  

st.title("Housing Price Predictor")

st.markdown("Adjust the values below to estimate the median house value:")

median_income = st.slider("Median Income (in 10k USD)", 0.0, 20.0, 3.0, 0.1)
total_rooms = st.slider("Total Rooms", 1, 10000, 3, 20)
total_bedrooms = st.slider("Total Bedrooms", 1, 1000, 1, 1)
housing_median_age = st.slider("Housing Median Age", 1, 52, 20)
population = st.slider("Population", 1, 30000, 1500, 100)
households = st.slider("Households", 1, 5000, 800, 50)
latitude = st.slider("Latitude", 32.0, 42.0, 36.5, 0.1)
longitude = st.slider("Longitude", -124.0, -114.0, -119.0, 0.1)


if st.button("🔍 Predict Price"):
    input_data = np.array([[median_income, total_rooms, housing_median_age,
                            population, households, latitude, longitude,total_bedrooms]])
    
    prediction = model.predict(input_data)
    st.success(f"🏡 Estimated Median House Value: **${prediction[0]:,.2f}**")
