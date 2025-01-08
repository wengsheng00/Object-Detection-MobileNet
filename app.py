import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Text input
name = st.text_input("Enter your name:", "")

# Slider
age = st.slider("Select your age:", 0, 100, 25)

# Button
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")
    
# Display a chart
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x': range(10),
    'y': np.random.randint(1, 100, 10)
})

st.line_chart(data)