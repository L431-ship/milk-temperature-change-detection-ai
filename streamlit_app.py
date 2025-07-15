
import streamlit as st
from logic import get_required_temperature

st.title("Room Temperature Tuner (Non-IoT)")
product = st.selectbox("Select Product", ['Milk', 'Curd', 'Ice-cream', 'Cheese', 'Flavored Milk'])
external_temp = st.number_input("Enter External Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)

if st.button("Predict Required Room Temp"):
    predicted_temp = get_required_temperature(product, external_temp)
    st.success(f"Recommended Room Temperature: {predicted_temp}°C")
