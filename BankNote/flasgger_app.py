# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:11:14 2020

@author: slage
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

import flasgger
from flasgger import Swagger

pickel_in = open('banknote.pkl','rb')

classifier = pickle.load(pickel_in)

app = Flask(__name__)
Swagger(app)

#decorator to welcome
@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')    
def predict():
    """
    Authenticate bank note
    This use docstrings for specifications
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        
        - name: skewness
          in: query
          type: number
          required: true
        
        - name: curtosis
          in: query
          type: number
          required: true
          
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values                              
    """
    
    variance = request.args.get('variance', 'int')
    skewness = request.args.get('skewness', 'int')
    curtosis = request.args.get('curtosis', 'int')
    entropy = request.args.get('entropy', 'int')
    
    result = classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "The Predicted class for passed value is "+str(result)

@app.route('/predict_file',methods=['POST'])
def predict_file():
    """Authnticate Banknote with file
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    
    responses:
        200:
            description: The output values
    """
    file = request.files.get('file')
    df_test = pd.read_csv(file)
    result = classifier.predict(df_test)
    
    return "The Predicted class for csv "+str(list(result))

if __name__ == '__main__':
    app.run()