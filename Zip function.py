#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task on zip()

#Zip() function
#The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

#Syntax :
#zip(*iterators)


# In[1]:


name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]


# In[2]:


# using zip() to map values
mapped = zip(name, roll_no, marks)


# In[3]:


# converting values to print as list
mapped = list(mapped)


# In[4]:


# printing resultant values
print("The zipped result is : ", end="")
print(mapped)


# In[ ]:




