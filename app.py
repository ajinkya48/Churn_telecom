import pickle
from flask import Flask, request, app, jsonify, url_for, render_templete
import numpy as np
import pandas as pd


app = Flask(__name__)
## Load the model
RFmodel = pickle.load(open('Churn_model_rf_smote.pkl', 'rb'))

@app.route('/')
def home():
    return render_templete('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    