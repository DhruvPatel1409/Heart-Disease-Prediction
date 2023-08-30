import streamlit as st
import numpy as np
import pandas as pd
import pickle

loaded_model = pickle.load(open('C:/Users/ADMIN/Desktop/vs code/streamlit/project5/heart_model.sav','rb'))

# 1--> female 0--> male

def heart_prediction(input_data):

    data_numeric = np.array(input_data).astype(float)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
        return("The person doesn't have a heart disease")
    else:
        return("The person has heart disease")

def main():

    st.title("HEART DISEASE PREDICTOR")
    age = st.number_input("Enter your age : ")
    sex = st.selectbox("Select Gender",("Male","Female"))
    if(sex == "Male"):
        s = 0
    if(sex == "Female"):
        s = 1
    cp = st.number_input("Enter chest pain type : ")
    trestbps = st.number_input("Enter your blood pressure : ")
    chol = st.number_input("Enter your cholestrol level : ")
    fbs = st.number_input("Enter your blood sugar level : ")
    restecg = st.number_input("Enter your ECG level : ")
    thalach = st.number_input("Enter your thalach level : ")
    exang = st.number_input("Enter your exercise angina : ")
    oldpeak = st.number_input("Enter your ST depression : ")
    slope = st.number_input("Enter your slope of ST segment : ")
    ca = st.number_input("Enter your number of major vessels : ")
    thal = st.number_input("Enter your thal level : ")

    diagnosis = ' '

    if st.button('PREDICT'):
        diagnosis = heart_prediction([age, s, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()

