import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, json, jsonify

model = joblib.load('./models/challa_logistic_regression.sav')

def predict_single(customer, model):
    X = pd.DataFrame([customer])
    y_pred = model.predict_proba(X)[:,1]
    return y_pred[0]


app = Flask('Diabetes')

@app.route('/predict', methods=['POST'])
def  predict():
    customer = request.get_json()
    
    prediction = predict_single(customer, model)
    
    diabetic = prediction >= 0.5
    
    result = {
        'Diabetic_Prediction_Probability': float(prediction),
        'Diabetes_Prediction': float(diabetic)
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port= 9696)
    
    
    