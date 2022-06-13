#!/usr/bin/env python
# coding: utf-8

# In[3]:


dict1={
    'Name':'uday',
    'sirname':'Ghorapade'
}
dict1


# In[4]:


len(dict1)


# In[7]:


x=dict1['sirname']
x


# In[8]:


dict1['Name']='sandesh'
dict1


# In[9]:


dict1['village']='manuchiwadi'
dict1


# In[12]:


dict1


# In[18]:


del dict1['Name']


# In[19]:


dict1


# In[21]:


child1 = {
  "name" : "John",
  "year" : 1995
}
child2 = {
  "name" : "Sammy",
  "year" : 2001
}


myfamily = {
  "child1" : child1,
  "child2" : child2
}
myfamily


# In[22]:


myfamily["child1"]["name"]


# In[ ]:




