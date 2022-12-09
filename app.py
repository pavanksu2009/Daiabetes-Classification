# Attribute Information:
# Number of times pregnant
# Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# Diastolic blood pressure (mm Hg)
# Triceps skin fold thickness (mm): Its thickness gives information about the fat reserves of the body
# 2-Hour serum insulin (mu U/ml)
# Body mass index (weight in kg/(height in m)^2)
# Diabetes pedigree function
# Age (years)
# Class variable (0 or 1)

import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load("./models/challa_logistic_regression.sav")


def main():
    st.sidebar.info("Diabetes Prediction APP")
    st.title("Is patient Diabetic or non-Diabetic")
    preg = st.number_input('Number of times person is pregnant: ', min_value= 0.0, max_value= 17.0, value= 0.0)
    plas = st.number_input('Plasma glucose concentration a 2 hours in an oral glucose tolerance test: ',min_value= 20.0, max_value= 199.0, value= 40.0 )
    pres = st.number_input('Diastolic blood pressure (mm Hg): ',min_value= 20.0, max_value= 122.0, value= 24.0)
    skin = st.number_input('Triceps skin fold thickness (mm): ',min_value= 7.0, max_value= 99.0, value= 7.0)
    test = st.number_input('2-Hour serum insulin (mu U/ml): ', min_value= 14.0, max_value= 846.0, value= 14.0)
    mass = st.number_input('Body mass index (weight in kg/(height in m)^2): ', min_value= 18.0, max_value= 67.10, value= 18.0)
    pedi = st.number_input('Diabetes pedigree function: ', min_value= 0.0, max_value= 2.42, value= 0.0)
    age =  st.number_input('Age (years): ', min_value= 21.0, max_value= 81.0, value= 21.0)
    output = ''
     
    customer = {
       'preg': preg,
       'plas': plas,
       'pres': pres,
       'skin': skin,
       'test': test,
       'mass': mass,
       'pedi': pedi,
       'age': age
    }
    ok = st.button("Predict Diabetic or non-Diabetic")
    if ok:
        X = pd.DataFrame([customer])
        y_pred = model.predict_proba(X)[0,1]
        output = y_pred
        if output > 0.5:
            st.write("The patient is Diabetic and the prediction probability is {}". format(output))
        else:
            st.write("The patient is non-Diabetic and the prediction probability is {}".format(output))    
       
if __name__ == '__main__':
    main()               
       
    