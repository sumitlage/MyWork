# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:11:14 2020

@author: slage
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

import streamlit as st

pickel_in = open('banknote.pkl','rb')
classifier = pickle.load(pickel_in)

def predict(variance,skewness,curtosis,entropy):
    
    result = classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return str(result)


def main():
    st.title("Bank Note Predictive Model")
    variance = st.text_input("variance","Type here")
    skewness = st.text_input("skewness","Type here")
    curtosis = st.text_input("curtosis","Type here")
    entropy = st.text_input("entropy","Type here")
    
    if st.button("Predict"):
       result =  predict(variance,skewness,curtosis,entropy)
       st.success("The predicted output is {}".format(result))
    
if __name__ == '__main__':
    main()