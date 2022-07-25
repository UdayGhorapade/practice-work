#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What Are the Basic Assumption');get_ipython().run_line_magic('pinfo', 'Assumption')
Features Are Independent

2. Advantages
Work Very well with many number of features
Works Well with Large training Dataset
It converges faster when we are training the model
It also performs well with categorical features
3. Disadvantages
Correlated features affects performance
get_ipython().set_next_input('4. Whether Feature Scaling is required');get_ipython().run_line_magic('pinfo', 'required')
No

get_ipython().set_next_input('5. Impact of Missing Values');get_ipython().run_line_magic('pinfo', 'Values')
Naive Bayes can handle missing data. Attributes are handled separately by the algorithm at both model construction time and prediction time. As such, if a data instance has a missing value for an attribute, it can be ignored while preparing the model, and ignored when a probability is calculated for a class value tutorial

get_ipython().set_next_input('6. Impact of outliers');get_ipython().run_line_magic('pinfo', 'outliers')
It is usually robust to outliers

Different Problem statement you can solve using Naive Baye's
Sentiment Analysis
Spam classification
twitter sentiment analysis
document categorization

