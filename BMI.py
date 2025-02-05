import streamlit as st

# Give a title to our app
st.title('Welcome to BMI Calculator')

# Take weight input in kgs
weight = st.number_input("Enter your weight (in kgs)", min_value=0.0)

# Option to choose height measurement
status = st.radio("Select height format:", ('Centimeters', 'Meters'))

# Initialize height and BMI
height = 0
bmi = None

# Take height input based on the selected format
if status == 'Centimeters':
    height = st.number_input("Enter your height (in centimeters)", min_value=0.0)
    height = height / 100  # Convert height from centimeters to meters
elif status == 'Meters':
    height = st.number_input("Enter your height (in meters)", min_value=0.0)