import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

import streamlit as st
import pandas as pd
from prediction_helper import predict
import joblib

# Page Configuration
st.set_page_config(page_title="🏥 Health Insurance Plan Predictor", layout="centered")

# App Title
st.title("🏥 Health Insurance Plan Predictor")
st.markdown("Use this tool to estimate your **health insurance premium** based on your profile and lifestyle.")

# Section 1: Basic Info
st.markdown("## 👤 Personal Information")
col1, col2, col3 = st.columns(3)
with col1:
    gender = st.selectbox("Gender", ['Male', 'Female'])
with col2:
    region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
with col3:
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])

# Section 2: Lifestyle Factors
st.markdown("## 💼 Lifestyle and Health")
col4, col5, col6 = st.columns(3)
with col4:
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
with col5:
    smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional', 'Does Not Smoke', 'Not Smoking', 'Smoking=0'])
with col6:
    employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])

col7, _ = st.columns([1, 2])
with col7:
    medical_history = st.selectbox("🩺 Medical History", [
        'No Disease', 'Diabetes', 'High blood pressure', 'Thyroid', 'Heart disease',
        'Diabetes & High blood pressure', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ])

# Section 3: Financial and Risk Factors
st.markdown("## 📊 Additional Information")
col9, col10, col11, col12,col13 = st.columns(5)
with col9:
    age = st.slider("Age", 18, 100, 30)
with col10:
    number_of_dependants = st.slider("Dependents", 0, 10, 1)
with col11:
    genetical_risk = st.slider("Genetical Risk", 0.0, 1.0, 0.3, step=0.01)
with col12:
        income_lakhs = st.number_input("Income (₹ Lakhs)", min_value=0.0, step=0.1, value=5.0)
with col13:
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

# Divider
st.markdown("---")

# Predict Button
if st.button("🔍 Predict Insurance Plan"):
    input_dict = {
        'Gender': gender,
        'Region': region,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Employment Status': employment_status,
        'Medical History': medical_history,
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Insurance Plan':insurance_plan,
        'Genetical Risk': genetical_risk
    }

    prediction = predict(input_dict)
    st.success(f'💰 **Predicted Health Insurance Cost:** ₹{prediction:,.2f}')
