#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# In[3]:


ax = plt.axes(projection = "3d")


# In[4]:


x = np.random.normal(size = 25)
y = np.random.normal(size = 25)
z = np.random.normal(size = 25)

ax = plt.axes(projection = '3d')

ax.scatter(x,y,z, color = 'red')


# In[5]:


# To change the view we can provide Azimuth angle
ax = plt.axes(projection = '3d')

ax.scatter(x,y,z, color = 'red')
ax.view_init(0,0)


# In[6]:


ax = plt.axes(projection = '3d')

ax.scatter(x,y,z, color = 'red')
ax.view_init(45,45)


# In[ ]:




