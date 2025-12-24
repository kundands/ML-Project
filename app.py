import streamlit as st
import pandas as pd
import numpy as np

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Page config
st.set_page_config(
    page_title="Student Exam Performance Predictor",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("🎓 Student Exam Performance Indicator")
st.subheader("Predict Maths Score")

st.markdown("---")

# Form
with st.form("prediction_form"):
    gender = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    ethnicity = st.selectbox(
        "Race / Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"]
    )

    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "associate's degree",
            "bachelor's degree",
            "high school",
            "master's degree",
            "some college",
            "some high school"
        ]
    )

    lunch = st.selectbox(
        "Lunch Type",
        ["free/reduced", "standard"]
    )

    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        ["none", "completed"]
    )

    reading_score = st.number_input(
        "Reading Score (0 - 100)",
        min_value=0,
        max_value=100,
        step=1
    )

    writing_score = st.number_input(
        "Writing Score (0 - 100)",
        min_value=0,
        max_value=100,
        step=1
    )

    submit = st.form_submit_button("Predict Maths Score")

# Prediction
if submit:
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()

        # st.write("📄 Input Data")
        # st.dataframe(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        st.success(f"✅ Predicted Maths Score: **{results[0]:.2f}**")

    except Exception as e:
        st.error("❌ Error during prediction")
        st.exception(e)
