#streamlit:- streamlit is a python library which is used to develop a simple web application, without writing code of html, css and js. This library is specially designed to integrate machine learning model in a web application.
import streamlit as st 
import pickle
import warnings
warnings.filterwarnings("ignore")
st.title("Students marks predictor")
sh=st.number_input("Enter study hours")
btn=st.button("Predict")

if btn:
    if sh <= 12:
        model=pickle.load(open("student_marks_prediction.pkl","rb"))
        res=model.predict([[sh]])[0][0].round(2)
        st.success(f"Predicted marks:{res}")
    else:
        st.warning("Invalid input")    


