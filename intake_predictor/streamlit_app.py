# Import necessary libraries
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the pre-trained model
model = LinearRegression()
# Assume you have trained the model and stored it in a file (e.g., model.pkl)
# You would load the model like this:
# model = pickle.load(open('model.pkl', 'rb'))

def predict_calories(gender, age, weight, height):
    input_data = np.array([[gender, age, weight, height]])
    calories_prediction = model.predict(input_data)[0]
    return calories_prediction

# Streamlit web application
def main():
    st.title("Calorie Intake Prediction")

    # User input
    gender = st.radio("Select Gender", ["Female", "Male"])
    age = st.slider("Enter Age", 18, 65, 30)
    weight = st.slider("Enter Weight (kg)", 45, 100, 70)
    height = st.slider("Enter Height (cm)", 150, 190, 175)

    # Convert gender to numeric (0 for Female, 1 for Male)
    gender_numeric = 0 if gender == "Female" else 1

    # Make prediction
    if st.button("Predict Calorie Intake"):
        calories_prediction = predict_calories(gender_numeric, age, weight, height)
        st.success(f'Predicted Calories Intake: {calories_prediction:.2f} kcal')

if __name__ == "__main__":
    main()
