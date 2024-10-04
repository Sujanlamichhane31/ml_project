import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit app
st.title("Student Exam Performance Indicator")

# Create form elements using Streamlit
gender = st.selectbox("Select your Gender", ("Male", "Female"))
ethnicity = st.selectbox("Select Ethnicity", ("Group A", "Group B", "Group C", "Group D", "Group E"))
parental_level_of_education = st.selectbox(
    "Select Parental Level of Education",
    ("Associate's degree", "Bachelor's degree", "High school", "Master's degree", "Some college", "Some high school")
)
lunch = st.selectbox("Select Lunch Type", ("Free/Reduced", "Standard"))
test_preparation_course = st.selectbox("Select Test Preparation Course", ("None", "Completed"))
reading_score = st.number_input("Enter your Reading Score (out of 100)", min_value=0, max_value=100, value=0)
writing_score = st.number_input("Enter your Writing Score (out of 100)", min_value=0, max_value=100, value=0)

# Predict button
if st.button("Predict your Math Score"):
    # Create an instance of CustomData with the form inputs
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=float(reading_score),
        writing_score=float(writing_score)
    )

    # Convert the input data to a DataFrame
    pred_df = data.get_data_as_data_frame()

    # Initialize the prediction pipeline and make predictions
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # Display the prediction result
    st.success(f"Predicted Math Score: {results[0]}")
