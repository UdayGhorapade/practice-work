#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


print(np.random.random())


# In[3]:


print(np.random.random())
print(np.random.random())
print(np.random.random())
print(np.random.random())


# In[6]:


#np.random.seed()
#random value will not change every time
np.random.seed(5)
np.random.random()
np.random.random()
np.random.random()


# In[10]:


X=np.random.random((4,4))
X


# In[12]:


num = np.random.randint(low = 40, high =100) #range
num


# In[ ]:




