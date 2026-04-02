# 🩺 Diabetes Prediction System

An end-to-end Machine Learning web application that predicts the likelihood of diabetes in patients based on medical metrics. Built with **Python**, **Scikit-Learn**, and **Streamlit**.

## 🚀 Project Overview
This project uses the **Pima Indians Diabetes Dataset** to train a **Logistic Regression** model. The application provides a user-friendly interface where healthcare providers or individuals can input health metrics and receive an instant prediction with a confidence score.



## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **Library:** Scikit-Learn (Modeling & Scaling)
* **Frontend:** Streamlit (UI & Web Server)
* **Data Handling:** Pandas & Numpy
* **Persistence:** Joblib (Model Serialization)

## 📊 Exploratory Data Analysis (EDA)
Before building the model, an extensive EDA was performed to understand the relationships between features:
* **Glucose & BMI:** Identified as the strongest predictors of diabetes.
* **Age Trends:** Observed that glucose levels and risk factors tend to increase and become more volatile with age.
* **Data Cleaning:** Handled biologically impossible "zero" values in features like Blood Pressure and Insulin.



## 🤖 Model Details
* **Algorithm:** Logistic Regression
* **Preprocessing:** StandardScaler was used to normalize feature ranges.
* **Evaluation:** The model achieves high recall, ensuring that potential diabetic cases are not missed.

## 🏃 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/diabetes-prediction.git](https://github.com/your-username/diabetes-prediction.git)
cd diabetes-prediction
pip install -r requirements.txt
streamlit run app.py

## 📁 Folder Structure
├── app.py              # Streamlit Web Application
├── diabatic_model.pkl  # Trained Logistic Regression Model
├── scaler.pkl          # Fitted StandardScaler Object
├── requirements.txt    # List of dependencies
└── README.md           # Project Documentation

## 📊 Exploratory Data Analysis (EDA)
During the analysis phase, I used a line plot to visualize how **Glucose Concentration** trends with **Age**, categorized by the **Outcome**. This helped in identifying the clear separation between the two classes.

![EDA Line Plot]https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.03.33_AM_fwnvj0.png
https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.03.54_AM_j6lepn.png
https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.04.06_AM_db2puv.png
https://res.cloudinary.com/ddgfjerss/image/upload/v1775161019/Screenshot_2026-04-03_at_1.04.23_AM_vv1iiq.png

## 🖥️ Streamlit UI Analysis
The application provides an interactive dashboard where users can input patient metrics. The model then processes these through a `StandardScaler` and a `Logistic Regression` classifier to provide a real-time diagnosis.

![Streamlit UI Screenshot]https://res.cloudinary.com/ddgfjerss/image/upload/v1775161074/Screenshot_2026-04-03_at_1.47.27_AM_dxycdx.png
https://res.cloudinary.com/ddgfjerss/image/upload/v1775161074/Screenshot_2026-04-03_at_1.47.42_AM_fr9uxw.png
