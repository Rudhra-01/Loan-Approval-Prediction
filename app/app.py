import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/loan_model.pkl")

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦"
)

st.title("🏦 Loan Approval Prediction System")
st.header("👤 Personal Information")
st.write("Enter applicant details below.")

# Inputs

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=5000
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0,
    value=2000
)

loan_amount = st.number_input(
    "Requested Loan Amount (₹ in Thousands)",
    min_value=1,
    value=120,
    help="Example: Enter 120 for ₹1,20,000"
)

loan_term = st.selectbox(
    "Loan Repayment Period (Months)",
    [12, 24, 36, 60, 120, 180, 240, 300, 360]
)

credit_history = st.selectbox(
    "Previous Loan Repayment History",
    [
        "Good (No Defaults)",
        "Poor / No History"
    ]
)

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

# Encoding

gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
credit_history = 1 if credit_history == "Good (No Defaults)" else 0

property_map = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}

property_area = property_map[property_area]

# Feature Engineering

total_income = applicant_income + coapplicant_income

loan_income_ratio = (
    loan_amount / total_income
    if total_income > 0 else 0
)

emi = (
    (loan_amount * 1000) / loan_term
)

# Predict

if st.button("Predict Loan Status"):

    input_data = pd.DataFrame([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area,
        total_income,
        loan_income_ratio,
        emi
    ]], columns=[
        'Gender',
        'Married',
        'Dependents',
        'Education',
        'Self_Employed',
        'ApplicantIncome',
        'CoapplicantIncome',
        'LoanAmount',
        'Loan_Amount_Term',
        'Credit_History',
        'Property_Area',
        'TotalIncome',
        'LoanIncomeRatio',
        'EMI'
    ])

    prediction = model.predict(input_data)[0]

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0][1]

        st.metric(
            "Approval Probability",
            f"{probability:.2%}"
        )

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.subheader("Input Summary")
    st.dataframe(input_data)