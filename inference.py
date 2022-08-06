#!/usr/bin/env python
# coding: utf-8

# In[4]:


# run this cell to import nltk
import nltk
from os import getcwd
import numpy as np
import pandas as pd
from nltk.corpus import twitter_samples 
from utils import process_tweet, build_freqs
from logistic_regression_Twitter_sentiment_analysis import *


# In[5]:


for tweet in ['I am happy', 'I am bad', 'this movie should have been great.', 'great', 'great great', 'great great great', 'great great great great']:
    print( '%s -> %f' % (tweet, predict_tweet(tweet, freqs, theta)))


# In[6]:


#test_case
my_tweet = 'I am learning :)'
predict_tweet(my_tweet, freqs, theta)


# In[14]:






# In[17]:









