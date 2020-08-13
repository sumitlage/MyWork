from flask import Flask,request,render_template
import numpy as np
import pandas as pd

import sklearn
import pickle

model = pickle.load(open('ITC_Stock_Price.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        Open = round(float(request.form['Open']),2)
        High = round(float(request.form['High']),2)
        Low = round(float(request.form['Low']),2)
        
        if request.form['Volume']=="":
            Volume=0.0
        else:        
            Volume = round(float(request.form['Volume']),2)
    
        date = request.form['Date']
        
        Year = pd.to_datetime(date,format='%Y-%m-%d').year
        Month = pd.to_datetime(date,format='%Y-%m-%d').month
        Day = pd.to_datetime(date,format='%Y-%m-%d').day
        
        prediction = model.predict([[Open,High,Low,Volume,Year,Month,Day]])
        
        return render_template('index.html',Prediction_Text="Closing Price will be {}".format(round(prediction[0],2)))

    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)

