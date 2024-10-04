import streamlit as st
import pandas as pd
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
    # Map inputs to the exact categories used during model training
    standardized_gender = gender.lower()
    standardized_ethnicity = {
        "Group A": "group A",
        "Group B": "group B",
        "Group C": "group C",
        "Group D": "group D",
        "Group E": "group E"
    }[ethnicity]  # Map to match the training data
    
    # Mapping parental level of education
    standardized_parental_level_of_education = {
        "Associate's degree": "associate's degree",
        "Bachelor's degree": "bachelor's degree",
        "High school": "high school",
        "Master's degree": "master's degree",
        "Some college": "some college",
        "Some high school": "some high school"
    }[parental_level_of_education]
    
    standardized_lunch = lunch.lower()
    standardized_test_preparation_course = test_preparation_course.lower()

    # Create an instance of CustomData with the mapped inputs
    data = CustomData(
        gender=standardized_gender,
        race_ethnicity=standardized_ethnicity,
        parental_level_of_education=standardized_parental_level_of_education,
        lunch=standardized_lunch,
        test_preparation_course=standardized_test_preparation_course,
        reading_score=float(reading_score),
        writing_score=float(writing_score)
    )

    # Convert the input data to a DataFrame
    pred_df = data.get_data_as_data_frame()

    # Initialize the prediction pipeline and make predictions
    predict_pipeline = PredictPipeline()
    try:
        results = predict_pipeline.predict(pred_df)

        # Display the prediction result
        st.success(f"Predicted Math Score: {results[0]}")
    except Exception as e:
        st.error(f"Error occurred during prediction: {str(e)}")
