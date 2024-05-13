import pickle
import streamlit as st

#load data 
diabetes_diseases = pickle.load(open('Diabetes_Diseases.sav','rb'))

#judul halaman
st.title('Penyakit Pendeteksi Diabetes')

Pregnancies = st.number_input('Pregnancies')
Glucose = st.number_input('Glucose')
BloodPressure = st.number_input('BloodPressure')
SkinThickness = st.number_input('SkinThickness')
Insulin = st.number_input('Insulin')
BMI = st.number_input('BMI')
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
Age = st.number_input('Age')

#prediksi diabetes
diagnosis_d = ''

#tombol prediksi
if st.button('Prediksi Diabetes'):
    prediksi_diabetes = diabetes_diseases.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if(prediksi_diabetes[0]==1):
        diagnosis_d = 'Diabetes'
    else:
        diagnosis_d = 'Tidak Diabetes'

    st.success(diagnosis_d)
