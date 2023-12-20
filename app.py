from flask import Flask,render_template,request,redirect,url_for,session,jsonify, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired 
from flask_cors import CORS,cross_origin
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import pickle
import pandas as pd
import numpy as np
import csv 
import os

app = Flask(__name__)
CORS(app)
app.secret_key = 'Dodong RR'

# Load Dataset Models
# Load the pre-trained regression model
with open('regression.pkl', 'rb') as model_file:
    regression_model = pickle.load(model_file)
# Load the pre-trained model
with open('classification.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/classification")
def classification():
    return render_template('classification.html')

@app.route("/regression")
def regression():
    return render_template('regression.html')

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json()

        # Convert data to a format suitable for prediction (you may need to adjust this based on your model requirements)
        input_data = np.array([float(data['age']), float(data['bilirubin']), float(data['cholesterol']),
                               float(data['albucin']), float(data['tryglicerimes']), float(data['platelets']),
                               float(data['prothrombin']), float(data['stage']), float(data['sex'])]).reshape(1, -1)

        # Make the prediction
        prediction = model.predict(input_data)[0]

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction)})  # Convert the prediction to int for JSON serialization
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route("/predictreg", methods=['POST'])
def predict_reg():
    try:
        # Get the input data from the request
        data = request.get_json()

        # Convert data to a format suitable for regression prediction
        input_data = np.array([float(data['age']), float(data['bmi']), float(data['bmi']), float(data['children']), float(data['alcoholic'])]).reshape(1, -1)

        # Make the regression prediction
        prediction = regression_model.predict(input_data)[0]

        # Return the prediction as JSON
        return jsonify({'prediction': float(prediction)})  # Convert the prediction to float for JSON serialization
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)