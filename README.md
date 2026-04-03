# 🩺 Diabetes Prediction System

An end-to-end **Machine Learning web application** that predicts the likelihood of diabetes using patient medical data. Built with **Python, Scikit-Learn, and Streamlit**, this system delivers real-time predictions with an intuitive user interface.

---

## 🚀 Project Overview

This project utilizes the **Pima Indians Diabetes Dataset** to train a **Logistic Regression model** for binary classification.

Users can input health parameters such as glucose level, BMI, age, and more to receive:

* ✅ Instant prediction (Diabetic / Non-Diabetic)
* 📊 Confidence-based output
* ⚡ Real-time inference

The system is designed to support **early detection and healthcare decision-making**.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Machine Learning:** Scikit-learn
* **Frontend / Deployment:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Model Persistence:** Joblib

---

## 📊 Exploratory Data Analysis (EDA)

Comprehensive analysis was conducted to understand feature relationships:

* **Glucose & BMI** → Strongest indicators of diabetes
* **Age Trends** → Risk increases with age
* **Data Cleaning** → Replaced biologically invalid zero values

### 📈 EDA Visualizations

<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.03.33_AM_fwnvj0.png" width="45%"/>
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.03.54_AM_j6lepn.png" width="45%"/>
</p>

<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161020/Screenshot_2026-04-03_at_1.04.06_AM_db2puv.png" width="45%"/>
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161019/Screenshot_2026-04-03_at_1.04.23_AM_vv1iiq.png" width="45%"/>
</p>

---

## 🤖 Model Details

* **Algorithm:** Logistic Regression
* **Preprocessing:** StandardScaler
* **Problem Type:** Binary Classification
* **Focus Metric:** High recall (minimizing false negatives)

---

## 🖥️ Application Interface

The application provides a **Streamlit-based dashboard** where users can:

* Enter patient medical details
* Get real-time predictions
* View model-driven insights

### 💻 UI Preview

<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161074/Screenshot_2026-04-03_at_1.47.27_AM_dxycdx.png" width="45%"/>
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775161074/Screenshot_2026-04-03_at_1.47.42_AM_fr9uxw.png" width="45%"/>
</p>

---

## 📁 Project Structure

```
├── app.py              # Streamlit Web Application
├── diabatic_model.pkl  # Trained ML Model
├── scaler.pkl          # StandardScaler
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## 🏃 How to Run Locally

```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Key Highlights

* End-to-end ML pipeline (EDA → Model → Deployment)
* Real-time prediction system
* Clean and interactive UI
* Healthcare-focused use case
* Optimized for usability and performance

---

## 👨‍💻 Author

**Manu Saviour**
Full Stack Developer • Machine Learning • Data Science

---

## ⭐ Final Note

This project demonstrates the ability to **design, train, and deploy machine learning models into production-ready applications**, with a focus on real-world impact.

> “Turning healthcare data into actionable intelligence.”
