# 🩺 Diabetes Prediction System

An end-to-end Machine Learning web application that predicts the likelihood of diabetes in patients based on medical metrics. Built with **Python**, **Scikit-Learn**, and **Streamlit**.

## 🚀 Project Overview
This project uses the **Pima Indians Diabetes Dataset** to train a **Logistic Regression** model. The application provides a user-friendly interface where healthcare providers or individuals can input health metrics and receive an instant prediction with a confidence score.

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **ML Library:** Scikit-Learn (Modeling & Scaling)
* **Web Framework:** Streamlit (UI & Web Server)
* **Data Processing:** Pandas & Numpy
* **Serialization:** Joblib

---

## 📊 Exploratory Data Analysis (EDA)
During the analysis phase, I used a line plot to visualize how **Glucose Concentration** trends with **Age**, categorized by the **Outcome**. This helped in identifying the clear separation between the two classes.

<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.03.33_AM_fwnvj0.png" width="45%" />
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.03.54_AM_j6lepn.png" width="45%" />
</p>
<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.04.06_AM_db2puv.png" width="45%" />
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161019/Screenshot_2026-04-03_at_1.04.23_AM_vv1iiq.png" width="45%" />
</p>

### 🔍 Key Insights:
- **Strongest Predictors:** Glucose and BMI showed the highest correlation with diabetic outcomes.
- **Biologically Impossible Zeros:** Handled missing data in `BloodPressure`, `Insulin`, and `BMI` by imputing with median values.
- **Age Factor:** Risk volatility increases significantly after age 45.

---

## 🖥️ Streamlit UI Analysis
The application provides an interactive dashboard where users can input patient metrics. The model then processes these through a `StandardScaler` and a `Logistic Regression` classifier to provide a real-time diagnosis.

<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161074/Screenshot_2026-04-03_at_1.47.27_AM_dxycdx.png" width="80%">
  <br>
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161074/Screenshot_2026-04-03_at_1.47.42_AM_fr9uxw.png" width="80%">
</p>

---

## 🏃 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/diabetes-prediction.git](https://github.com/your-username/diabetes-prediction.git)
cd diabetes-prediction
