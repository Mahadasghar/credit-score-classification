import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
with open("best_credit_score_model.pkl", "rb") as f:
    model = pickle.load(f)
# Load trained pipeline safely


st.title("📊 Credit Score Classification App")

# Collect user input (must match training feature names in the saved pipeline)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Income", min_value=0, step=1000, value=50000)
num_children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
home_ownership = st.selectbox("Home Ownership", ["Owned", "Rented", "Mortgaged"])

# Predict button
if st.button("Predict Credit Score"):
    # Wrap input into DataFrame with correct column names
    input_df = pd.DataFrame([{
        'Age': age,
        'Income': income,
        'Number of Children': num_children,
        'Gender': gender,
        'Education': education,
        'Marital Status': marital_status,
        'Home Ownership': home_ownership
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Get prediction probabilities
    probas = model.predict_proba(input_df)[0]
    confidence = probas.max() * 100
    predicted_class = model.classes_[probas.argmax()]

    # Display results
    st.success(f"Predicted Credit Score Category: **{prediction}**")
    st.info(f"Confidence: {confidence:.2f}%")

    # Optional: show full probability distribution
    st.write("### Probability Distribution")
    prob_df = pd.DataFrame([probas], columns=model.classes_)
    st.bar_chart(prob_df.T)
