#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[1,2,3]
b=a.append(4)
print(a)
print(b)


# In[2]:


List = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]

print(List)


# In[3]:


temp = ['python', 'machinelearning', 'deeplearning']

arr = [i[0].upper() for i in temp]

print(arr)


# In[4]:


print([i.lower() for i in "HELLO"])


# In[5]:


l1=[1,2,3]

l2=[4,5,6]

[x*y for x in l1 for y in l2]


# In[6]:


list = ['python', 'learning', '@', 'i2', 'tutorials', 'website']

print(list[0:6:2])


# In[7]:


list1 = [1, 2, 3, 4, 5]

list2 = list1

list2[0] = 0;

print( list1)


# In[ ]:




