#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
print("two-dimensional array")
two_d_array = np.random.randint(1,20, size = (4,6))
print(two_d_array)
print("\nthree-dimensional array")
three_d_array = np.reshape(two_d_array,(3,4,2))
print(three_d_array)


# In[2]:


print("two-dimensional array")
two_d_array = np.random.randint(1,20, size = (4,6))
print(two_d_array)
print("\nthree-dimensional array")
three_d_array = np.reshape(two_d_array,(1,4,2))
print(three_d_array)


# In[3]:


print("two-dimensional array")
two_d_array = np.random.randint(1,20, size = (4,6))
print(two_d_array)
print("\none-dimensional array")
one_d_array = two_d_array.reshape(24)
print(one_d_array)


# In[4]:


one_d_array = two_d_array.reshape(1,24)
print(one_d_array)


# In[ ]:




