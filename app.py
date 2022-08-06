# run this cell to import nltk
import nltk
from os import getcwd
import numpy as np
import pandas as pd
from nltk.corpus import twitter_samples 
from utils import process_tweet, build_freqs
from logistic_regression_Twitter_sentiment_analysis import *
#from inference import *

User_review = input('phone record') 

def inference_piple():
    User_review = input('phone record') 
    phone_record = User_review
    process_tweet(phone_record)
    print(phone_record)
    y_hat = predict_tweet(phone_record, freqs, theta)
    print(y_hat)
    if y_hat > 0.5:
        print('Positive record')
    else: 
        print('Negative record')

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return inference_piple()
