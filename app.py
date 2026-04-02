import streamlit as st 
import pandas as pd
import numpy as np
import joblib

model=joblib.load('diabetic_model.pkl')
scaler=joblib.load('scaler.pkl')

st.set_page_config(page_title="Diabetic Prediction App", page_icon=":guardsman:", layout="centered")
st.title("Diabetic Prediction App")
st.write("Please enter the following details to predict whether a person is diabetic or not:")

col1,col2=st.columns(2)

with col1:
    preg=st.number_input("pregnancies", min_value=0, max_value=20, value=2)
    glu=st.number_input("glucose", min_value=0, max_value=200, value=120)
    bp=st.number_input("blood pressure", min_value=0, max_value=200,value=70)
    skin=st.number_input("skin thickness", min_value=0, max_value=100, value=20)

with col2:
    ins=st.number_input("insulin", min_value=0, max_value=1000, value=80)
    bmi=st.number_input("bmi", min_value=0.0, max_value=70.0, value=25.0)
    dpf=st.number_input("diabetes pedigree function", min_value=0.0, max_value=3.0, value=0.5)
    age=st.number_input("age", min_value=0, max_value=120, value=30)

if st.button("Analyze results"):
    input_dict={
        'Pregnancies': preg,
        'Glucose': glu,
        'BloodPressure': bp,
        'SkinThickness': skin,
        'Insulin': ins,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }

    input_df=pd.DataFrame([input_dict])
    scaled_data=scaler.transform(input_df)

    prediction=model.predict(scaled_data)[0]
    probability=model.predict_proba(scaled_data)[0]

    st.divider()
    if prediction == 1:
        st.error(f"### Result: Diabetic")
        st.write(f"**Confidence Score:** {probability[1]:.2%}")
    else:
        st.success(f"### Result: Healthy")
        st.write(f"**Confidence Score:** {probability[0]:.2%}")
    if glu >140 and prediction == 0:
        st.warning("Note: The glucose level is above the normal threshold, but the model predicts healthy. Consider consulting a healthcare professional for further evaluation.")  
st.sidebar.metric("User Glucose", f"{glu} mg/dL", delta=f"{glu-120} from avg")
 