# 🏦 Loan Approval Prediction System

## 📌 Project Overview

The Loan Approval Prediction System is an end-to-end Machine Learning project designed to predict whether a loan application is likely to be approved based on applicant demographics, financial details, and credit history.

This project demonstrates the complete Machine Learning lifecycle, including data preprocessing, exploratory data analysis (EDA), feature engineering, model building, evaluation, and deployment using Streamlit.

---

## 🎯 Business Problem

Financial institutions process thousands of loan applications every year. Manual evaluation is time-consuming and may lead to inconsistencies. This project helps automate the loan approval process by predicting loan eligibility using historical applicant data.

---

## 📊 Dataset Features

* Gender
* Married
* Dependents
* Education
* Self Employed
* Applicant Income
* Co-applicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area

### Target Variable

* Loan_Status

  * 1 → Approved
  * 0 → Rejected

---

## ⚙️ Project Workflow

### 1. Data Cleaning

* Handled missing values
* Removed inconsistencies
* Prepared data for analysis

### 2. Exploratory Data Analysis (EDA)

* Loan approval distribution
* Gender-wise approval analysis
* Education-wise approval analysis
* Credit history impact analysis
* Income and loan amount distribution

### 3. Feature Engineering

Created new features:

* TotalIncome
* LoanIncomeRatio
* EMI

### 4. Model Building

Models evaluated:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

### 5. Model Evaluation

Evaluation metrics:

* Accuracy Score
* Classification Report
* Confusion Matrix
* Feature Importance Analysis

### Model Accuracy

**Accuracy: 78.86%**

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit
* Power BI
* Git & GitHub

---

## 🚀 Streamlit Application

The application allows users to:

* Enter applicant information
* Predict loan approval status
* View applicant summary
* Receive instant prediction results

## 📈 Key Insights

* Credit history is one of the strongest indicators of loan approval.
* Applicants with higher total income have a better chance of approval.
* Semiurban property areas showed higher approval rates.
* Graduates generally received more approvals compared to non-graduates.

---

## 🔮 Future Enhancements

* Hyperparameter Tuning
* XGBoost Integration
* Cloud Deployment
* Real-time Database Integration
* Explainable AI (SHAP)

---

## 👨‍💻 Author

Rudhra Roopini

Aspiring Data Scientist | Machine Learning Enthusiast | Generative AI Learner

