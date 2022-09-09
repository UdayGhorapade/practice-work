#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


female = pd.read_csv('C:/Users/uday/Desktop/birth.csv')
female.head()


# In[6]:


from datetime import date


# In[7]:


# Get all records for the month of Janaury(1959-01-01 - 1959-01-31). 
# Using boolean is not good method when we are dealing with large datasets.
female[(pd.to_datetime(female['Date']) > pd.Timestamp(date(1959,1,1))) &
 (pd.to_datetime(female['Date']) < pd.Timestamp(date(1959,1,31)))]


# In[ ]:




