# Import necessary libraries
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate synthetic dataset (replace this with your real data)
np.random.seed(42)
num_samples = 1000
gender = np.random.choice([0, 1], size=num_samples)  # 0: Female, 1: Male
age = np.random.randint(18, 65, size=num_samples)
weight = np.random.uniform(45, 100, size=num_samples)
height = np.random.uniform(150, 190, size=num_samples)
calories_intake = 2000 + 10 * age + 7 * weight - 5 * height + np.random.normal(scale=50, size=num_samples)

# Create a feature matrix X and target variable y
X = np.column_stack((gender, age, weight, height))
y = calories_intake

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

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
        input_data = np.array([[gender_numeric, age, weight, height]])
        calories_prediction = model.predict(input_data)[0]

        # Custom styling for success message
        success_message = f'<div style="color:white; font-size:25px;">Predicted Calories Intake: {calories_prediction:.2f} kcal</div>'
        st.markdown(success_message, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
