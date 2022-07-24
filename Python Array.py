#!/usr/bin/env python
# coding: utf-8

# In[1]:


import array
 
int_array = array.array('i', [1, 2, 3, 4])
 
for a in int_array:
    print(a)


# In[2]:


for b in range(0, len(int_array)):
    print(f'int_array[{b}] = {int_array[b]}')


# In[3]:


for b in range(0, len(int_array)):
    print(f'int_array[{b}] = {int_array[b]}')


# In[4]:


int_array = array.array('i', [1, 2, 3, 4])
int_array.append(-3)
print(int_array)  # array('i', [1, 2, 3, 4, -3])


# In[5]:


int_array = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])
print(int_array[-2])  # 70
print(int_array[-5])  # 40


# In[ ]:




