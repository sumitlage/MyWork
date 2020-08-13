# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:11:14 2020

@author: slage
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

pickel_in = open('banknote.pkl','rb')

classifier = pickle.load(pickel_in)

app = Flask(__name__)

#decorator to welcome
@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')    
def predict():
    variance = request.args.get('variance', 'int')
    skewness = request.args.get('skewness', 'int')
    curtosis = request.args.get('curtosis', 'int')
    entropy = request.args.get('entropy', 'int')
    
    result = classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "The Predicted class for passed value is "+str(result)

@app.route('/predict_file',methods=['POST'])
def predict_file():
    file = request.files.get('file')
    df_test = pd.read_csv(file)
    result = classifier.predict(df_test)
    
    return "The Predicted class for csv "+str(list(result))

if __name__ == '__main__':
    app.run()